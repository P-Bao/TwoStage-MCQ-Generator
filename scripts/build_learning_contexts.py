"""
build_learning_contexts.py
---------------------------------
Chunk toàn bộ file .md trong một thư mục INPUT_DIR bằng LangChain + LLM qua OpenRouter, sinh ra `learning_contexts.json` đúng định dạng mà
mcqs-generation.ipynb cần:
    [
      {"text": "...", "title": "...", "keywords": [...], "token_count": 123},
      ...
    ]

Thiết kế để dùng được với model trên OpenRouter:
  - Gộp nhiều chunk thô vào 1 lần gọi LLM (CHUNKS_PER_LLM_CALL) để giảm tổng số request.
  - Rate limiter tôn trọng giới hạn request/phút.
  - Đếm request/ngày, dừng an toàn TRƯỚC khi chạm giới hạn ngày và lưu checkpoint để mai chạy lại là tiếp tục, không mất tiến độ / không tốn lại request đã dùng.
  - Không dùng structured output kiểu tool-calling (nhiều model free không hỗ trợ tốt) mà yêu cầu model trả JSON trong prompt rồi tự parse, có fallback an toàn nếu model trả sai định dạng.
"""

import json
import os
import re
import sys
import time
from collections import deque
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

from dotenv import load_dotenv

# 0. Nạp .env và kiểm tra tham số bắt buộc — in ra template nếu thiếu

ENV_TEMPLATE = """\
# ==== Tạo file .env (cùng thư mục với script) với nội dung sau ====

# --- Bắt buộc ---
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx   # lấy tại https://openrouter.ai/keys

# --- Model (phải là model FREE, id kết thúc bằng :free) ---
# Vài lựa chọn free phổ biến hiện tại (kiểm tra lại tại openrouter.ai/models?max_price=0
# vì danh sách free hay đổi):
#   meta-llama/llama-3.3-70b-instruct:free
#   deepseek/deepseek-r1:free
#   qwen/qwen3-coder:free
#   google/gemini-2.0-flash-exp:free
OPENROUTER_MODEL=meta-llama/llama-3.3-70b-instruct:free

# --- Đường dẫn ---
INPUT_DIR=./input                        # thư mục chứa các file .md
OUTPUT_FILE=./learning_contexts.json     # file output, đúng format cho notebook MCQ
CHECKPOINT_FILE=./checkpoint.jsonl       # lưu tiến độ để resume, đừng xoá khi chưa chạy xong

# --- Tham số cắt chunk ---
CHUNK_SIZE=1500                          # số ký tự tối đa mỗi chunk thô
CHUNK_OVERLAP=100
MIN_CHUNK_TOKENS=100                     # chunk nhỏ hơn sẽ bị gộp/loại

# --- Tối ưu cho tier FREE của OpenRouter ---
CHUNKS_PER_LLM_CALL=6                    # gộp N chunk / 1 lần gọi LLM để giảm số request
REQUESTS_PER_MINUTE=15                   # free tier cho phép 20/phút, để 15 cho an toàn
DAILY_REQUEST_LIMIT=45                   # free tier: 50/ngày (chưa nạp) hoặc 1000/ngày (đã nạp >=$10)
                                          # đặt thấp hơn giới hạn thật một chút cho an toàn

# --- Tuỳ chọn (OpenRouter dùng để thống kê app, không bắt buộc) ---
OPENROUTER_SITE_URL=https://local-script
OPENROUTER_SITE_NAME=mcq-chunking
"""

def load_config() -> dict:
    load_dotenv()
    missing = []
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        missing.append("OPENROUTER_API_KEY")

    if missing:
        print("Thiếu biến môi trường bắt buộc trong .env:", ", ".join(missing))
        print()
        print(ENV_TEMPLATE)
        sys.exit(1)

    cfg = {
        "api_key": api_key,
        "model": os.environ.get("OPENROUTER_MODEL", "meta-llama/llama-3.3-70b-instruct:free"),
        "input_dir": Path(os.environ.get("INPUT_DIR", "./input")),
        "output_file": Path(os.environ.get("OUTPUT_FILE", "./learning_contexts.json")),
        "checkpoint_file": Path(os.environ.get("CHECKPOINT_FILE", "./checkpoint.jsonl")),
        "chunk_size": int(os.environ.get("CHUNK_SIZE", 1500)),
        "chunk_overlap": int(os.environ.get("CHUNK_OVERLAP", 100)),
        "min_chunk_tokens": int(os.environ.get("MIN_CHUNK_TOKENS", 100)),
        "chunks_per_call": int(os.environ.get("CHUNKS_PER_LLM_CALL", 6)),
        "rpm": int(os.environ.get("REQUESTS_PER_MINUTE", 15)),
        "daily_limit": int(os.environ.get("DAILY_REQUEST_LIMIT", 45)),
        "site_url": os.environ.get("OPENROUTER_SITE_URL", "https://local-script"),
        "site_name": os.environ.get("OPENROUTER_SITE_NAME", "mcq-chunking"),
    }

    if not cfg["model"].endswith(":free"):
        print(f"[warn] OPENROUTER_MODEL='{cfg['model']}' không kết thúc bằng ':free' "
              f"— nếu đây không phải model free, request sẽ bị tính phí.")

    if not cfg["input_dir"].is_dir():
        print(f"Không tìm thấy thư mục INPUT_DIR='{cfg['input_dir']}'. "
              f"Tạo thư mục này và bỏ các file .md vào trong.")
        sys.exit(1)

    return cfg

# 1. Rate limiter: giới hạn request/phút + đếm request/ngày (bền qua lần chạy)
class RateLimiter:
    def __init__(self, rpm: int, daily_limit: int, state_file: Path):
        self.rpm = rpm
        self.daily_limit = daily_limit
        self.state_file = state_file
        self._timestamps = deque()
        self._today, self._count_today = self._load_state()

    def _load_state(self):
        today = date.today().isoformat()
        if self.state_file.exists():
            try:
                data = json.loads(self.state_file.read_text())
                if data.get("date") == today:
                    return today, data.get("count", 0)
            except Exception:
                pass
        return today, 0

    def _save_state(self):
        self.state_file.write_text(json.dumps({"date": self._today, "count": self._count_today}))

    def can_send(self) -> bool:
        today = date.today().isoformat()
        if today != self._today:
            self._today, self._count_today = today, 0
        return self._count_today < self.daily_limit

    def wait_and_register(self):
        now = time.monotonic()
        while self._timestamps and now - self._timestamps[0] > 60:
            self._timestamps.popleft()
        if len(self._timestamps) >= self.rpm:
            sleep_for = 60 - (now - self._timestamps[0]) + 0.5
            if sleep_for > 0:
                time.sleep(sleep_for)
        self._timestamps.append(time.monotonic())
        self._count_today += 1
        self._save_state()

    @property
    def remaining_today(self) -> int:
        return max(0, self.daily_limit - self._count_today)

# 2. LLM qua OpenRouter (LangChain ChatOpenAI, tương thích OpenAI API)
def build_llm(cfg: dict):
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=cfg["model"],
        api_key=cfg["api_key"],
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        max_retries=2,
        timeout=90,
        default_headers={
            "HTTP-Referer": cfg["site_url"],
            "X-Title": cfg["site_name"],
        },
    )


BATCH_PROMPT = """Bạn xử lý các đoạn trích từ giáo trình Kỹ thuật phần mềm để chuẩn bị dữ liệu \
tạo câu hỏi trắc nghiệm (MCQ). Dưới đây là {n} đoạn văn bản, mỗi đoạn có id riêng.

Với MỖI đoạn, hãy xác định:
- title: tiêu đề ngắn gọn (dưới 12 từ)
- keywords: 3-6 từ khóa/thuật ngữ chính (giữ nguyên thuật ngữ tiếng Anh chuyên ngành nếu có)
- is_coherent: true nếu đoạn đủ ngữ nghĩa để tạo câu hỏi trắc nghiệm độc lập, false nếu không

CHỈ trả lời bằng một JSON array hợp lệ, không thêm giải thích, không thêm markdown code fence.
Mỗi phần tử có dạng: {{"id": <id>, "title": "...", "keywords": ["...", "..."], "is_coherent": true|false}}

Các đoạn văn bản:
{items}
"""


def _format_items(batch: List[dict]) -> str:
    parts = []
    for item in batch:
        parts.append(f'--- id={item["local_id"]} ---\n{item["text"][:3000]}')
    return "\n\n".join(parts)


def _extract_json_array(raw: str) -> Optional[list]:
    raw = raw.strip()
    raw = re.sub(r"^```(json)?", "", raw).strip()
    raw = re.sub(r"```$", "", raw).strip()
    start, end = raw.find("["), raw.rfind("]")
    if start == -1 or end == -1:
        return None
    try:
        return json.loads(raw[start:end + 1])
    except json.JSONDecodeError:
        return None


def enrich_batch(llm, batch: List[dict]) -> Dict[int, dict]:
    """Gọi 1 lần LLM cho cả batch, trả về map local_id -> {title, keywords, is_coherent}."""
    prompt = BATCH_PROMPT.format(n=len(batch), items=_format_items(batch))
    result_map = {}
    try:
        resp = llm.invoke(prompt)
        parsed = _extract_json_array(resp.content)
        if parsed:
            for entry in parsed:
                try:
                    lid = int(entry["id"])
                    result_map[lid] = {
                        "title": str(entry.get("title", ""))[:200],
                        "keywords": list(entry.get("keywords", []))[:8],
                        "is_coherent": bool(entry.get("is_coherent", True)),
                    }
                except Exception:
                    continue
    except Exception as e:
        print(f"  [warn] LLM call lỗi: {e}")

    # fallback cho bất kỳ item nào model bỏ sót / parse fail
    for item in batch:
        if item["local_id"] not in result_map:
            result_map[item["local_id"]] = {
                "title": item.get("fallback_title") or "Untitled",
                "keywords": [],
                "is_coherent": True,
            }
    return result_map

# 3. Cắt thô theo cấu trúc Markdown
def split_markdown_structural(md_text: str, chunk_size: int, chunk_overlap: int):
    from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

    headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
    md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
    header_docs = md_splitter.split_text(md_text)

    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return char_splitter.split_documents(header_docs)

def collect_raw_chunks(cfg: dict, encoder) -> List[dict]:
    """Đọc mọi .md trong input_dir, cắt thô, gộp chunk quá ngắn, gán id ổn định."""
    md_files = sorted(cfg["input_dir"].rglob("*.md"))
    if not md_files:
        print(f"Không tìm thấy file .md nào trong {cfg['input_dir']}")
        sys.exit(1)
    print(f"Tìm thấy {len(md_files)} file .md trong {cfg['input_dir']}")

    all_chunks = []
    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        docs = split_markdown_structural(text, cfg["chunk_size"], cfg["chunk_overlap"])

        merged = []
        for doc in docs:
            n_tok = len(encoder.encode(doc.page_content))
            if merged and n_tok < cfg["min_chunk_tokens"]:
                merged[-1].page_content = merged[-1].page_content.rstrip() + "\n\n" + doc.page_content
            else:
                merged.append(doc)

        for idx, doc in enumerate(merged):
            content = doc.page_content.strip()
            if not content:
                continue
            fallback_title = doc.metadata.get("h3") or doc.metadata.get("h2") or doc.metadata.get("h1") or ""
            all_chunks.append({
                "global_id": f"{md_path.stem}::{idx:05d}",
                "text": content,
                "fallback_title": fallback_title,
                "source_file": md_path.name,
            })
        print(f"  {md_path.name}: {len(merged)} chunk thô")

    print(f"Tổng cộng: {len(all_chunks)} chunk thô trên toàn bộ input/")
    return all_chunks

# 4. Checkpoint: đọc/ghi kết quả đã enrich để resume qua nhiều lần chạy
def load_checkpoint(path: Path) -> Dict[str, dict]:
    done = {}
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        rec = json.loads(line)
                        done[rec["global_id"]] = rec
                    except Exception:
                        pass
    return done


def append_checkpoint(path: Path, records: List[dict]):
    with open(path, "a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


# 5. Main
class _ApproxEncoder:
    """Fallback khi không tải được tiktoken (một số môi trường không có mạng ngoài).
    Ước lượng ~4 ký tự/token, đủ dùng để lọc theo MIN_CHUNK_TOKENS."""
    def encode(self, text: str):
        return [0] * max(1, len(text) // 4)

def get_encoder():
    try:
        import tiktoken
        return tiktoken.get_encoding("cl100k_base")
    except Exception as e:
        print(f"[warn] Không tải được tiktoken ({e}); dùng bộ đếm token xấp xỉ (~4 ký tự/token).")
        return _ApproxEncoder()

def main():
    cfg = load_config()
    encoder = get_encoder()

    raw_chunks = collect_raw_chunks(cfg, encoder)

    checkpoint_path = cfg["checkpoint_file"]
    done_map = load_checkpoint(checkpoint_path)
    pending = [c for c in raw_chunks if c["global_id"] not in done_map]
    print(f"Đã enrich trước đó: {len(done_map)} | Còn lại: {len(pending)}")

    if pending:
        llm = build_llm(cfg)
        state_file = checkpoint_path.with_suffix(".state.json")
        limiter = RateLimiter(cfg["rpm"], cfg["daily_limit"], state_file)

        if not limiter.can_send():
            print(f"Đã đạt giới hạn {cfg['daily_limit']} request hôm nay. "
                  f"Chạy lại script vào ngày mai để tiếp tục (checkpoint đã lưu, không mất tiến độ).")
        else:
            batch_size = cfg["chunks_per_call"]
            n_batches = (len(pending) + batch_size - 1) // batch_size
            stopped_early = False

            from tqdm import tqdm
            pbar = tqdm(total=len(pending), desc="Enrich chunks (LLM)")
            for b in range(n_batches):
                if not limiter.can_send():
                    stopped_early = True
                    break

                batch = pending[b * batch_size: (b + 1) * batch_size]
                for i, item in enumerate(batch):
                    item["local_id"] = i

                limiter.wait_and_register()
                result_map = enrich_batch(llm, batch)

                records = []
                for item in batch:
                    meta = result_map[item["local_id"]]
                    n_tok = len(encoder.encode(item["text"]))
                    records.append({
                        "global_id": item["global_id"],
                        "text": item["text"],
                        "title": meta["title"],
                        "keywords": meta["keywords"],
                        "is_coherent": meta["is_coherent"],
                        "token_count": n_tok,
                        "source_file": item["source_file"],
                    })
                append_checkpoint(checkpoint_path, records)
                pbar.update(len(batch))
            pbar.close()

            if stopped_early:
                print(f"\nDừng sớm để tránh vượt giới hạn ngày ({cfg['daily_limit']} request). "
                      f"Checkpoint đã lưu tại {checkpoint_path} — chạy lại script vào ngày mai "
                      f"(hoặc sau khi rate limit reset) để tiếp tục, không mất tiến độ.")

    # ---- Ghi output cuối cùng từ toàn bộ checkpoint hiện có ----
    done_map = load_checkpoint(checkpoint_path)
    final_items = []
    for c in raw_chunks:
        rec = done_map.get(c["global_id"])
        if rec and rec["token_count"] >= cfg["min_chunk_tokens"]:
            final_items.append({
                "text": rec["text"],
                "title": rec["title"],
                "keywords": rec["keywords"],
                "token_count": rec["token_count"],
            })

    with open(cfg["output_file"], "w", encoding="utf-8") as f:
        json.dump(final_items, f, ensure_ascii=False, indent=2)

    remaining = len(raw_chunks) - len(done_map)
    print(f"\nĐã ghi {len(final_items)} chunk vào {cfg['output_file']}")
    if remaining > 0:
        print(f"Còn {remaining} chunk CHƯA được enrich (do giới hạn free tier). "
              f"File output hiện tại là bản tạm — chạy lại script để bổ sung phần còn thiếu.")
    else:
        print("Đã xử lý xong toàn bộ chunk.")

if __name__ == "__main__":
    main()
