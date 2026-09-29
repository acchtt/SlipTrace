from __future__ import annotations

from historical_audit import load_corpus, summarize
from semantic_metrics import build_test_case


def test_historical_corpus_is_large_enough_to_be_useful() -> None:
    corpus = load_corpus()
    assert corpus["case_count"] >= 90
    assert corpus["semantic_eligible_count"] >= 80
    assert corpus["settled_case_count"] >= 10


def test_historical_corpus_has_no_privacy_or_hindsight_leaks() -> None:
    report = summarize(load_corpus())
    assert report["blocking_finding_count"] == 0, report


def test_semantic_input_never_contains_audit_outcome() -> None:
    corpus = load_corpus()
    checked = 0
    for case in corpus["cases"]:
        if not case.get("semantic_eligible"):
            continue
        test_case = build_test_case(case)
        rendered = "\n".join(test_case.context or []) + "\n" + test_case.input + "\n" + test_case.actual_output
        # The field itself must never be serialized into judge input.
        assert "audit_outcome" not in rendered
        assert "calibration_track" not in rendered
        checked += 1
    assert checked >= 80
