"""
metrics.py
----------
Automatic evaluation metrics for MCQ generation quality.

Metrics:
  - BLEU-4:    n-gram precision for question quality
  - ROUGE-L:   Longest common subsequence for answer quality
  - BERTScore: Semantic similarity using contextual embeddings
"""

import json
from pathlib import Path
from typing import Optional

from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction, corpus_bleu
from rouge_score import rouge_scorer as rouge_lib


# ---------------------------------------------------------------------------
# BLEU-4
# ---------------------------------------------------------------------------

def compute_bleu4_single(reference: str, hypothesis: str) -> float:
    """
    Compute BLEU-4 for a single (reference, hypothesis) pair.

    Args:
        reference:  Gold-standard text.
        hypothesis: Generated text.

    Returns:
        BLEU-4 score in [0, 1].
    """
    ref_tokens = reference.lower().split()
    hyp_tokens = hypothesis.lower().split()
    smoothie = SmoothingFunction().method4
    return sentence_bleu(
        [ref_tokens],
        hyp_tokens,
        weights=(0.25, 0.25, 0.25, 0.25),
        smoothing_function=smoothie,
    )


def compute_bleu4(
    references: list[str],
    hypotheses: list[str],
) -> float:
    """
    Corpus-level BLEU-4.

    Args:
        references:  List of gold-standard strings.
        hypotheses:  List of generated strings (same order).

    Returns:
        Mean BLEU-4 score.
    """
    assert len(references) == len(hypotheses), "Lists must have same length."

    scores = [
        compute_bleu4_single(ref, hyp)
        for ref, hyp in zip(references, hypotheses)
        if ref and hyp
    ]
    return sum(scores) / len(scores) if scores else 0.0


# ---------------------------------------------------------------------------
# ROUGE-L
# ---------------------------------------------------------------------------

def compute_rouge_l_single(reference: str, hypothesis: str) -> float:
    """ROUGE-L F1 for a single pair."""
    scorer = rouge_lib.RougeScorer(["rougeL"], use_stemmer=True)
    result = scorer.score(reference, hypothesis)
    return result["rougeL"].fmeasure


def compute_rouge_l(
    references: list[str],
    hypotheses: list[str],
) -> float:
    """
    Mean ROUGE-L F1 across all pairs.

    Args:
        references:  List of gold-standard strings.
        hypotheses:  List of generated strings.

    Returns:
        Mean ROUGE-L F1 score.
    """
    assert len(references) == len(hypotheses)
    scores = [
        compute_rouge_l_single(ref, hyp)
        for ref, hyp in zip(references, hypotheses)
        if ref and hyp
    ]
    return sum(scores) / len(scores) if scores else 0.0


def compute_rouge2(references: list[str], hypotheses: list[str]) -> float:
    """Mean ROUGE-2 F1."""
    scorer = rouge_lib.RougeScorer(["rouge2"], use_stemmer=True)
    scores = []
    for ref, hyp in zip(references, hypotheses):
        if ref and hyp:
            scores.append(scorer.score(ref, hyp)["rouge2"].fmeasure)
    return sum(scores) / len(scores) if scores else 0.0


# ---------------------------------------------------------------------------
# BERTScore
# ---------------------------------------------------------------------------

def compute_bertscore(
    references: list[str],
    hypotheses: list[str],
    lang: str = "en",
    model_type: str = "microsoft/deberta-xlarge-mnli",
    verbose: bool = False,
) -> dict[str, float]:
    """
    Compute BERTScore for a list of pairs.

    Requires: pip install bert-score

    Args:
        references:  Gold-standard strings.
        hypotheses:  Generated strings.
        lang:        Language code (default "en").
        model_type:  BERT-family model to use for embeddings.
        verbose:     Print progress.

    Returns:
        Dict with keys: precision, recall, f1 (mean values).
    """
    try:
        from bert_score import score as bert_score_fn
    except ImportError:
        raise ImportError("Install bert-score: pip install bert-score")

    # Filter empty strings
    pairs = [(r, h) for r, h in zip(references, hypotheses) if r and h]
    if not pairs:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}

    refs, hyps = zip(*pairs)

    P, R, F1 = bert_score_fn(
        list(hyps),
        list(refs),
        lang=lang,
        model_type=model_type,
        verbose=verbose,
    )

    return {
        "precision": P.mean().item(),
        "recall": R.mean().item(),
        "f1": F1.mean().item(),
    }


# ---------------------------------------------------------------------------
# Combined evaluation
# ---------------------------------------------------------------------------

def evaluate_mcq_batch(
    generated_mcqs: list[dict],
    reference_mcqs: Optional[list[dict]] = None,
    compute_bert: bool = True,
) -> dict:
    """
    Compute all metrics for a batch of MCQs.

    If reference_mcqs is provided, computes metrics against gold standard.
    Otherwise, only computes self-consistency metrics.

    Args:
        generated_mcqs:  List of MCQ dicts from the pipeline.
        reference_mcqs:  Optional list of gold MCQ dicts (same order).
        compute_bert:    Whether to compute BERTScore (slow, requires GPU).

    Returns:
        Dict with all metric scores.
    """
    results = {
        "num_mcqs": len(generated_mcqs),
        "num_valid": sum(
            1 for m in generated_mcqs
            if m.get("question") and m.get("correct_answer")
        ),
    }

    if reference_mcqs is not None:
        assert len(generated_mcqs) == len(reference_mcqs)

        gen_questions = [m.get("question", "") for m in generated_mcqs]
        ref_questions = [m.get("question", "") for m in reference_mcqs]
        gen_answers = [m.get("correct_answer", "") for m in generated_mcqs]
        ref_answers = [m.get("correct_answer", "") for m in reference_mcqs]

        results["question_bleu4"] = compute_bleu4(ref_questions, gen_questions)
        results["question_rouge_l"] = compute_rouge_l(ref_questions, gen_questions)
        results["question_rouge2"] = compute_rouge2(ref_questions, gen_questions)
        results["answer_bleu4"] = compute_bleu4(ref_answers, gen_answers)
        results["answer_rouge_l"] = compute_rouge_l(ref_answers, gen_answers)

        if compute_bert:
            print("[metrics] Computing BERTScore for questions...")
            results["question_bertscore"] = compute_bertscore(ref_questions, gen_questions)
            print("[metrics] Computing BERTScore for answers...")
            results["answer_bertscore"] = compute_bertscore(ref_answers, gen_answers)

    # Self-consistency stats (always computed)
    questions = [m.get("question", "") for m in generated_mcqs]
    answers = [m.get("correct_answer", "") for m in generated_mcqs]
    results["avg_question_length_words"] = (
        sum(len(q.split()) for q in questions if q) / max(1, sum(1 for q in questions if q))
    )
    results["avg_answer_length_words"] = (
        sum(len(a.split()) for a in answers if a) / max(1, sum(1 for a in answers if a))
    )

    return results


def save_metrics_report(metrics: dict, output_path: str) -> None:
    """Save metrics dict to JSON."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(f"[metrics] Saved metrics report to: {output_path}")
    _print_metrics_summary(metrics)


def _print_metrics_summary(metrics: dict) -> None:
    """Pretty-print metrics."""
    print("\n" + "=" * 50)
    print("EVALUATION RESULTS")
    print("=" * 50)
    for key, value in metrics.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for k2, v2 in value.items():
                print(f"    {k2}: {v2:.4f}")
        elif isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    print("=" * 50)
