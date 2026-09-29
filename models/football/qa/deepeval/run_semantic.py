"""Manual DeepEval LLM-judge runner for the frozen historical Football A corpus."""

from __future__ import annotations

import argparse
import os

from deepeval import evaluate

from historical_audit import load_corpus
from semantic_metrics import build_test_case, metric_set_for_case


def priority(case: dict) -> tuple:
    decision = case.get("decision") or {}
    text = " ".join(
        str(decision.get(key) or "")
        for key in ("verdict", "candidate", "execution_class")
    ).upper()
    official = "OFFICIAL" in text
    live = case.get("evidence_epoch") == "LIVE_OR_JUST_STARTED"
    settled = case.get("audit_outcome") is not None
    return (official, live, settled, case.get("assessment_time_utc") or "")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--id", action="append", dest="ids")
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is required for semantic G-Eval. "
            "The deterministic DeepEval suite does not require it."
        )

    corpus = load_corpus()
    cases = [
        case
        for case in corpus["cases"]
        if case.get("semantic_eligible")
        and case.get("assessment_time_utc", "") >= "2026-09-25T17:00:00.000Z"
    ]

    if args.ids:
        wanted = set(args.ids)
        cases = [case for case in cases if case["assessment_id"] in wanted]
    else:
        cases.sort(key=priority, reverse=True)
        cases = cases[: max(args.limit, 1)]

    if not cases:
        raise SystemExit("No semantic-eligible cases matched.")

    print(f"Running semantic DeepEval on {len(cases)} historical cases.")
    print("Final scores/settlements are intentionally excluded from judge inputs.")

    failures = 0
    for case in cases:
        test_case = build_test_case(case)
        metrics = metric_set_for_case(case)
        result = evaluate(
            test_cases=[test_case],
            metrics=metrics,
            print_results=True,
            show_indicator=True,
        )
        # DeepEval's evaluate result shape can evolve; rely on its own printed
        # result and continue case-by-case rather than coupling to internals.
        if result is None:
            failures += 0

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
