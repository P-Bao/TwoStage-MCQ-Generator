"""
Evaluate the generated MCQs.
  a) Automatic metrics: BLEU-4, ROUGE-L, ROUGE-2, BERTScore
  b) LLM-as-Judge: Nemotron-3-Ultra-550B via OpenRouter (first 100 MCQs)
Prerequisites:
  - output/mcq_results/mcq_output.json 
  - OPENROUTER_API_KEY in .env
Output:
  - output/evaluation/automatic_metrics.json
  - output/evaluation/llm_judge_results.json
"""

import argparse
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))
load_dotenv()

from src.evaluation.metrics import evaluate_mcq_batch, save_metrics_report
from src.evaluation.llm_judge import LLMJudge


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mcq-path",
        default="./output/mcq_results/mcq_output.json",
        help="Path to generated MCQs JSON",
    )
    parser.add_argument(
        "--output-dir",
        default="./output/evaluation",
        help="Output directory for evaluation results",
    )
    parser.add_argument(
        "--skip-bertscore",
        action="store_true",
        help="Skip BERTScore (slow on CPU)",
    )
    parser.add_argument(
        "--skip-llm-judge",
        action="store_true",
        help="Skip LLM-as-Judge evaluation",
    )
    parser.add_argument(
        "--llm-judge-samples",
        type=int,
        default=100,
        help="Number of MCQs to evaluate with LLM Judge (default: 100)",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Evaluate only first N MCQs (default: all)",
    )
    parser.add_argument(
        "--openrouter-key",
        default=None,
        help="OpenRouter API key (overrides OPENROUTER_API_KEY env var)",
    )
    return parser.parse_args()


def load_mcqs(path: str) -> list[dict]:
    """Load MCQs from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("STEP 4: Evaluation")
    print("=" * 60)

    # Load MCQs
    if not Path(args.mcq_path).exists():
        print(f"ERROR: MCQ results not found: {args.mcq_path}")
        print("Run: notebooks/mcqs-generation.ipynb first.")
        sys.exit(1)

    mcqs = load_mcqs(args.mcq_path)
    
    # Apply sample size limit
    if args.sample_size and args.sample_size < len(mcqs):
        mcqs = mcqs[:args.sample_size]
        print(f"Limited evaluation to first {args.sample_size} MCQs")

    print(f"Loaded {len(mcqs)} MCQs from: {args.mcq_path}")

    
    # a) Automatic Metrics
    print("Automatic Metrics")

    metrics = evaluate_mcq_batch(
        generated_mcqs=mcqs,
        reference_mcqs=None,      
        compute_bert=not args.skip_bertscore,
    )

    metrics_path = output_dir / "automatic_metrics.json"
    save_metrics_report(metrics, str(metrics_path))

    
    # b) LLM-as-Judge
    
    if not args.skip_llm_judge:
        print("LLM-as-Judge Evaluation")
        api_key = (
            args.openrouter_key
            or os.environ.get("OPENROUTER_API_KEY", "")
        )

        if not api_key:
            print("WARNING: OPENROUTER_API_KEY not set. Skipping LLM Judge.")
            print("Set it in .env file or use --openrouter-key argument.")
        else:
            judge = LLMJudge(
                api_key=api_key,
                model="nvidia/nemotron-3-ultra-550b-a55b:free",
                request_delay=1.5,
            )

            judgements = judge.evaluate_batch(
                mcqs=mcqs,
                max_samples=min(args.llm_judge_samples, len(mcqs)),
            )

            judge_path = output_dir / "llm_judge_results.json"
            judge.save_judgements(judgements, str(judge_path))

            summary = judge.summarize_judgements(judgements)
            print("\nLLM Judge Summary:")
            for key, value in summary.items():
                if isinstance(value, float):
                    print(f"  {key}: {value:.3f}")
                else:
                    print(f"  {key}: {value}")
    else:
        print("\nSkipping LLM-as-Judge (--skip-llm-judge).")

    
    # Final Summary
    print("Evaluation Complete!")
    print(f"Output directory: {output_dir.resolve()}")
    for f in sorted(output_dir.iterdir()):
        if f.suffix == ".json":
            print(f"  {f.name}")

    print("\nProject complete!")

if __name__ == "__main__":
    main()
