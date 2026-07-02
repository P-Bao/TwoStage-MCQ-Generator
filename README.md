# MCQ Generation with Llama — Two-Stage Pipeline

Triển khai hệ thống sinh câu hỏi trắc nghiệm (MCQ) tự động từ tài liệu văn bản. Dự án này được thiết kế dựa trên ý tưởng kiến trúc **Pipeline (Đường ống 2 giai đoạn)** được đánh giá trong nghiên cứu của Jintao Ling và Muhammad Afzaal. 

Theo bài báo, phương pháp chia quá trình tạo MCQ thành 2 giai đoạn độc lập cho thấy hiệu quả cao trong giáo dục:
1. **QA Generation (Sinh Câu hỏi & Đáp án đúng):** Sử dụng mô hình fine-tune trên tập dữ liệu SQuAD v2.
2. **Distractor Generation (Sinh Đáp án nhiễu):** Sử dụng mô hình fine-tune trên tập dữ liệu DG-RACE để tạo ra các đáp án sai nhưng có độ đánh lừa cao.

*(Dự án của chúng ta kế thừa trực tiếp kiến trúc này nhưng nâng cấp mô hình nền tảng từ T5/BART lên **Llama-3.2-3B-Instruct** để cải thiện chất lượng sinh).*

> **Reference:**
> Ling, J., & Afzaal, M. (2024). *Automatic question-answer pairs generation using pre-trained large language models in higher education*. Computers and Education: Artificial Intelligence, 6, 100252. [https://doi.org/10.1016/j.caeai.2024.100252](https://doi.org/10.1016/j.caeai.2024.100252)

## 🏗️ Architecture

```
PDF / Document
         │
         ▼
[MinerU Extractor (mineru.net)]
         │
         ▼
  [Markdown Files in input/]
         │
         ├────────────────────────────────────┐
         ▼                                    │
┌─────────────────┐                           │
│   QA Generator  │  ← Llama-3.2-3B + LoRA    │
│ (Fine-tuned on  │    (Kaggle T4x2)          │
│   SQuAD v2)     │                           │
└────────┬────────┘                           │
         │ (Question, Correct Answer)         │ (Context)
         ▼                                    │
┌──────────────────────┐ ◄────────────────────┘
│ Distractor Generator │  ← Llama-3.2-3B + LoRA
│ (Fine-tuned on RACE/ │    (Kaggle T4x2)
│   DG-RACE format)    │
└──────────┬───────────┘
           │ (Distractor 1, 2, 3)
           ▼
    ┌──────────────┐
    │  MCQ Output  │  → JSON / CSV
    │  A) ...      │
    │  B) ...      │
    │  C) ...      │
    │  D) ...      │
    └──────────────┘
           │
           ▼
[LLM-as-Judge Evaluation]  ← OpenRouter 
```

## 📁 Project Structure

```
/
├── README.md                          # This file
├── requirements_local.txt             # CPU-only dependencies
├── requirements_kaggle.txt            # GPU dependencies for Kaggle
│

├── input/                             # Chứa dữ liệu đầu vào định dạng markdown
├── output/                            # Chứa dữ liệu đầu ra của pipeline scripts
│
├── src/                               # Source code (Evaluation metrics)
│
├── notebooks/                         # GPU notebooks — chạy trên Kaggle
│   ├── mcqs-train-qa-model.ipynb      # Huấn luyện mô hình QA
│   ├── mcqs-train-distractor-model.ipynb # Huấn luyện mô hình sinh đáp án nhiễu
│   └── mcqs-generation.ipynb          # Sinh MCQ từ dữ liệu đầu vào
│
└── scripts/                           # Scripts tiền xử lý và đánh giá
    ├── build_learning_contexts.py     # Phân tách và trích xuất title/keywords bằng LLM
    └── evaluate.py                    # Đánh giá chất lượng MCQ
```

## 🚀 Quick Start

### Phase 1 — GPU Training (Kaggle)
Tất cả các file notebook trong dự án được thiết kế để chạy trên máy có GPU (Kaggle).
1. Chạy notebook `notebooks/mcqs-train-qa-model.ipynb` (hoặc [Run on Kaggle](https://www.kaggle.com/code/baopv051/mcqs-train-qa-model)) để huấn luyện mô hình QA.
2. Chạy notebook `notebooks/mcqs-train-distractor-model.ipynb` (hoặc [Run on Kaggle](https://www.kaggle.com/code/baopv051/mcqs-train-distractor-model)) để huấn luyện mô hình Distractor.

### Phase 2 — Chuẩn bị Dataset Đầu Vào (Local/CPU)
Tạo dataset bằng cách lấy tài liệu dạng markdown:
1. Đặt các tài liệu dạng `.md` vào thư mục `input/`. 
   *(Nếu tài liệu của bạn không ở định dạng markdown, hãy tải xuống dạng markdown thông qua công cụ: [https://mineru.net/OpenSourceTools/Extractor](https://mineru.net/OpenSourceTools/Extractor) - Lưu ý: Cần tạo tài khoản)*
2. Đảm bảo file `.env` đã được cấu hình đủ các biến (OPENROUTER_API_KEY, INPUT_DIR, OUTPUT_FILE...).
3. Cài đặt thư viện và chạy script để cắt text và dùng LLM tạo chunks:
```bash
pip install -r requirements.txt

python scripts/build_learning_contexts.py
```
Kết quả `learning_contexts.json` sẽ được lưu vào thư mục `output/`.

### Phase 3 — Sinh MCQ (Kaggle)
Sau khi tạo dataset xong và có sẵn các model đã huấn luyện:
- Chạy notebook `notebooks/mcqs-generation.ipynb` (hoặc [Run on Kaggle](https://www.kaggle.com/code/baopv051/mcqs-generation)) để sinh ra các câu hỏi trắc nghiệm từ bộ chunks (learning contexts).

### Phase 4 — Đánh giá (Local/CPU)
Cuối cùng, chạy script đánh giá chất lượng các câu hỏi vừa sinh ra (nếu cần):
```bash
python scripts/evaluate.py
```

## 🔑 APIs & Keys Required

| Service | URL | Key Required |
|---------|-----|-------------|
| PDF Extraction | `https://mineru.net` | Account Required |
| LLM Judge | `https://openrouter.ai/api/v1` | `OPENROUTER_API_KEY` |
| HuggingFace | `https://huggingface.co` | `HF_TOKEN` (for Llama) |

## 📊 Models

| Model | Base | Dataset | Task |
|-------|------|---------|------|
| QA Generator | Llama-3.2-3B-Instruct | SQuAD v2 | Context → Question + Answer |
| Distractor Gen | Llama-3.2-3B-Instruct | RACE (DG-RACE format) | Q+A+Context → 3 Distractors |

## 📈 Evaluation Metrics

- **BLEU-4**: n-gram overlap for question quality
- **ROUGE-L**: Longest common subsequence for answer quality  
- **BERTScore**: Semantic similarity using BERT embeddings
- **LLM-as-Judge**: Nemotron-3-Ultra scores MCQ quality (1-5)
