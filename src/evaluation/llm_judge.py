"""
llm_judge.py
------------
LLM-as-Judge evaluation using OpenRouter API (qua LangChain ChatOpenAI).
Model mặc định: openai/gpt-oss-120b:free

Evaluates MCQ quality on 5 criteria (each 1-5):
  1. Relevance:          Is the question relevant to the context?
  2. Clarity:            Is the question clear and unambiguous?
  3. Difficulty:         Is the difficulty appropriate for university students?
  4. Distractor Quality: Are wrong answers plausible but clearly incorrect?
  5. Overall:            Overall MCQ quality
"""

import json
import os
import re
import time
from pathlib import Path
from typing import Optional

from langchain_openai import ChatOpenAI


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------

JUDGE_PROMPT_TEMPLATE = """You are an expert MCQ (Multiple Choice Question) evaluator for university-level education.
Evaluate the following MCQ carefully.

Context: {context}

Question: {question}
A) {option_a}
B) {option_b}
C) {option_c}
D) {option_d}
Correct Answer: {answer_key}) {correct_answer}

Rate each criterion from 1 (very poor) to 5 (excellent):
1. Relevance (1-5): Is the question directly relevant to and answerable from the context?
2. Clarity (1-5): Is the question clear, specific, and unambiguous?
3. Difficulty (1-5): Is the difficulty appropriate for a university exam (not trivial, not impossible)?
4. Distractor Quality (1-5): Are the 3 wrong answers plausible enough to challenge students but clearly incorrect upon careful reading?
5. Overall Quality (1-5): Overall quality as an exam question.

Respond ONLY with valid JSON (no markdown, no extra text):
{{
  "relevance": <integer 1-5>,
  "clarity": <integer 1-5>,
  "difficulty": <integer 1-5>,
  "distractor_quality": <integer 1-5>,
  "overall": <integer 1-5>,
  "feedback": "<one sentence explaining the main strength or weakness>"
}}"""


# ---------------------------------------------------------------------------
# LLMJudge class
# ---------------------------------------------------------------------------

class LLMJudge:
    """
    LLM-as-Judge evaluator using an OpenRouter model via LangChain's
    ChatOpenAI (OpenRouter's API is OpenAI-compatible).

    Args:
        api_key: OpenRouter API key (from OPENROUTER_API_KEY env var).
        model:   OpenRouter model identifier.
        request_delay: Seconds to wait between API calls (rate limiting).
        max_retries:  Retry failed requests this many times.
    """

    DEFAULT_MODEL = "openai/gpt-oss-120b:free"

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        request_delay: float = 1.5,
        max_retries: int = 3,
    ):
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "OpenRouter API key required. Set OPENROUTER_API_KEY env var "
                "or pass api_key argument."
            )
        self.model = model
        self.request_delay = request_delay
        self.max_retries = max_retries

        # LangChain ChatOpenAI trỏ sang OpenRouter (API tương thích OpenAI).
        # max_retries=0 vì ta tự retry thủ công bên dưới để log rõ từng lần thử
        # và xử lý riêng lỗi JSON parse (khác với lỗi mạng/HTTP).
        self._llm = ChatOpenAI(
            model=self.model,
            api_key=self.api_key,
            base_url="https://openrouter.ai/api/v1",
            temperature=0.1,
            max_tokens=300,
            max_retries=0,
            timeout=60,
            default_headers={
                "HTTP-Referer": "https://github.com/mcq-generation-llama",
                "X-Title": "MCQ Generation Research",
            },
        )

    def _build_prompt(self, mcq: dict) -> str:
        """Build the evaluation prompt for one MCQ."""
        options = mcq.get("options", {})
        # Truncate context to avoid exceeding token limits
        context = mcq.get("context", "")[:600]
        return JUDGE_PROMPT_TEMPLATE.format(
            context=context,
            question=mcq.get("question", ""),
            option_a=options.get("A", ""),
            option_b=options.get("B", ""),
            option_c=options.get("C", ""),
            option_d=options.get("D", ""),
            answer_key=mcq.get("answer_key", ""),
            correct_answer=mcq.get("correct_answer", ""),
        )

    @staticmethod
    def _extract_json(content: str) -> dict:
        """Parse JSON from model output, robust to markdown fences and stray text
        (nhiều model free không luôn tuân thủ 'chỉ trả JSON')."""
        content = content.strip()
        content = re.sub(r"^```(json)?", "", content).strip()
        content = re.sub(r"```$", "", content).strip()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            pass

        # Fallback: lấy đoạn { ... } đầu tiên trong response
        start, end = content.find("{"), content.rfind("}")
        if start != -1 and end != -1:
            return json.loads(content[start:end + 1])

        raise json.JSONDecodeError("No JSON object found", content, 0)

    def _call_api(self, prompt: str) -> Optional[dict]:
        """
        Make one call to the OpenRouter model via LangChain.

        Returns:
            Parsed JSON response dict or None on failure.
        """
        content = ""
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self._llm.invoke(prompt)
                content = (response.content or "").strip()
                return self._extract_json(content)

            except json.JSONDecodeError as e:
                print(f"[LLMJudge] JSON parse error (attempt {attempt}/{self.max_retries}): {e}")
                print(f"[LLMJudge] Raw response: {content[:200]}")
                if attempt < self.max_retries:
                    time.sleep(5 * attempt)

            except Exception as e:
                # Lỗi mạng/HTTP/timeout từ LangChain (bao gồm rate limit 429 của
                # tier free trên OpenRouter)
                print(f"[LLMJudge] API error (attempt {attempt}/{self.max_retries}): {e}")
                if attempt < self.max_retries:
                    time.sleep(5 * attempt)

        return None

    def evaluate_mcq(self, mcq: dict) -> Optional[dict]:
        """
        Evaluate a single MCQ.

        Args:
            mcq: MCQ dict with keys: context, question, options, answer_key, correct_answer.

        Returns:
            Dict with scores: relevance, clarity, difficulty, distractor_quality, overall, feedback.
            Returns None if API call fails.
        """
        prompt = self._build_prompt(mcq)
        result = self._call_api(prompt)
        time.sleep(self.request_delay)

        if result is None:
            return None

        # Validate scores are in [1, 5]
        for key in ["relevance", "clarity", "difficulty", "distractor_quality", "overall"]:
            if key in result:
                try:
                    result[key] = max(1, min(5, int(result[key])))
                except (ValueError, TypeError):
                    result[key] = 3  # Default to middle score

        result["chunk_id"] = mcq.get("chunk_id", "")
        result["question"] = mcq.get("question", "")
        return result

    def evaluate_batch(
        self,
        mcqs: list[dict],
        max_samples: int = 100,
        start_idx: int = 0,
    ) -> list[dict]:
        """
        Evaluate a batch of MCQs.

        Args:
            mcqs:        List of MCQ dicts.
            max_samples: Maximum number to evaluate (free tier has limits).
            start_idx:   Index to start from (for resuming).

        Returns:
            List of judgement dicts.
        """
        to_evaluate = mcqs[start_idx : start_idx + max_samples]
        total = len(to_evaluate)
        print(f"[LLMJudge] Evaluating {total} MCQs using {self.model}...")

        judgements = []
        for i, mcq in enumerate(to_evaluate, 1):
            print(f"[LLMJudge] {i}/{total}: chunk_id={mcq.get('chunk_id', '?')}")
            result = self.evaluate_mcq(mcq)
            if result is not None:
                judgements.append(result)
            else:
                print(f"[LLMJudge] Skipping chunk {mcq.get('chunk_id', '?')} due to API failure.")

        print(f"[LLMJudge] Completed. Got {len(judgements)}/{total} judgements.")
        return judgements

    def summarize_judgements(self, judgements: list[dict]) -> dict:
        """
        Compute mean scores across all judgements.

        Args:
            judgements: List of judgement dicts.

        Returns:
            Dict with mean scores and standard deviations.
        """
        if not judgements:
            return {}

        criteria = ["relevance", "clarity", "difficulty", "distractor_quality", "overall"]
        summary = {"num_evaluated": len(judgements)}

        for criterion in criteria:
            scores = [j[criterion] for j in judgements if criterion in j]
            if scores:
                mean = sum(scores) / len(scores)
                variance = sum((s - mean) ** 2 for s in scores) / len(scores)
                std = variance ** 0.5
                summary[f"{criterion}_mean"] = round(mean, 3)
                summary[f"{criterion}_std"] = round(std, 3)

        return summary

    def save_judgements(self, judgements: list[dict], output_path: str) -> None:
        """Save judgements to JSON file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        output = {
            "summary": self.summarize_judgements(judgements),
            "judgements": judgements,
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"[LLMJudge] Saved {len(judgements)} judgements to: {output_path}")
        summary = output["summary"]
        if summary:
            print(f"[LLMJudge] Overall mean score: {summary.get('overall_mean', 'N/A')}")


# ---------------------------------------------------------------------------
# Convenience function
# ---------------------------------------------------------------------------

def run_llm_judge(
    mcqs_path: str,
    output_path: str,
    api_key: Optional[str] = None,
    max_samples: int = 100,
) -> dict:
    """
    Load MCQs from JSON, run LLM judge, save results.

    Args:
        mcqs_path:   Path to mcq_output.json.
        output_path: Where to save llm_judge_results.json.
        api_key:     OpenRouter API key.
        max_samples: Number of MCQs to evaluate.

    Returns:
        Summary dict.
    """
    with open(mcqs_path, "r", encoding="utf-8") as f:
        mcqs = json.load(f)

    print(f"[LLMJudge] Loaded {len(mcqs)} MCQs from: {mcqs_path}")

    judge = LLMJudge(api_key=api_key)
    judgements = judge.evaluate_batch(mcqs, max_samples=max_samples)
    judge.save_judgements(judgements, output_path)

    return judge.summarize_judgements(judgements)


if __name__ == "__main__":
    import sys
    mcqs_path = sys.argv[1] if len(sys.argv) > 1 else "./outputs/mcq_results/mcq_output.json"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "./outputs/evaluation/llm_judge_results.json"

    summary = run_llm_judge(mcqs_path, output_path)
    print("Summary:", json.dumps(summary, indent=2))
