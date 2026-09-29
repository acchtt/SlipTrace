"""Audit helpers for the frozen Football A historical DeepEval corpus.

The historical audit has two purposes:
1. enforce data-integrity/privacy boundaries that MUST fail CI; and
2. surface non-blocking historical workflow signals for QA review without
   rewriting old decisions to current policy.

Outcome data is never fed into semantic judge inputs.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CORPUS_PATH = ROOT / "cases" / "historical_2026-09-24_to_2026-09-29.json"

OUTCOME_MARKERS = (
    "final result:",
    "settled ft:",
    "user later reported ft",
    "user later supplied ft",
    "ft was",
    "counterfactual",
    "official p/l",
    "audit classification",
)

PRIVACY_PATTERNS = (
    re.compile(r"\bVND\b", re.IGNORECASE),
    re.compile(r"\bBETSLIP\b", re.IGNORECASE),
    re.compile(r"\bticket\s+\d{6,}\b", re.IGNORECASE),
    re.compile(r"\b\d{12,}\b"),
)

POST_XI_GATE_START_UTC = "2026-09-25T17:00:00.000Z"  # 2026-09-26 00:00 ICT


def load_corpus(path: Path = CORPUS_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def decision_text(case: dict[str, Any]) -> str:
    decision = case.get("decision") or {}
    parts = [
        decision.get("verdict"),
        decision.get("candidate"),
        decision.get("execution_class"),
        decision.get("supplied_line"),
        decision.get("decision_evidence"),
    ]
    return "\n".join(str(part) for part in parts if part)


def is_official(case: dict[str, Any]) -> bool:
    decision = case.get("decision") or {}
    text = " ".join(
        str(decision.get(key) or "")
        for key in ("verdict", "candidate", "execution_class")
    ).upper()
    return "OFFICIAL BET" in text or "OFFICIAL LOCK" in text


def is_live(case: dict[str, Any]) -> bool:
    return case.get("evidence_epoch") == "LIVE_OR_JUST_STARTED"


def selected_burden(case: dict[str, Any]) -> float | None:
    decision = case.get("decision") or {}
    value = decision.get("supported_target_line")
    if isinstance(value, (int, float)):
        return float(value)

    text = " ".join(
        str(decision.get(key) or "")
        for key in ("candidate", "supplied_line")
    )
    matches = re.findall(r"(?:OVER\s*|\bO)(\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if not matches:
        return None
    try:
        return float(matches[0])
    except ValueError:
        return None


def audit_case(case: dict[str, Any]) -> list[str]:
    """Return findings.

    Prefixes:
      BLOCKING_* -> corpus/privacy/hindsight defects; CI should fail.
      SIGNAL_*   -> historical QA signals only; do not rewrite the old verdict.
    """

    findings: list[str] = []
    rendered = json.dumps(case, ensure_ascii=False)

    for pattern in PRIVACY_PATTERNS:
        if pattern.search(rendered):
            findings.append(f"BLOCKING_PRIVACY_LEAK:{pattern.pattern}")

    evidence = ((case.get("decision") or {}).get("decision_evidence") or "")
    if case.get("semantic_eligible"):
        lowered = evidence.casefold()
        for marker in OUTCOME_MARKERS:
            if marker in lowered:
                findings.append(f"BLOCKING_HINDSIGHT_LEAK:{marker}")

        decision = case.get("decision") or {}
        if not (decision.get("verdict") or decision.get("candidate")):
            findings.append("BLOCKING_MISSING_DECISION_OUTPUT")

    if not case.get("semantic_eligible"):
        return findings

    text = decision_text(case)
    upper = text.upper()

    if is_live(case) and is_official(case):
        has_plan_authority = any(
            token in upper
            for token in (
                "PREDECLARED",
                "LIVE DECAY PLAN",
                "MATCH-SPECIFIC EXCEPTION",
                "ACTIVE EXCEPTION",
            )
        )
        if not has_plan_authority:
            findings.append("SIGNAL_OFFICIAL_LIVE_WITHOUT_EXPLICIT_PLAN_AUTHORITY")

    assessment_time = case.get("assessment_time_utc") or ""
    period = (case.get("assessment_period") or "").upper()
    if (
        assessment_time >= POST_XI_GATE_START_UTC
        and not is_live(case)
        and is_official(case)
        and "XI" in period
    ):
        if "POST-XI RESEARCH" not in upper:
            findings.append("SIGNAL_OFFICIAL_PREMATCH_MISSING_POST_XI_RESEARCH_STATUS")

    burden = selected_burden(case)
    if is_official(case) and burden is not None and burden >= 3.0:
        if "H2H" not in upper:
            findings.append("SIGNAL_O3PLUS_OFFICIAL_WITHOUT_EXPLICIT_H2H_TRACE")

    return findings


def summarize(corpus: dict[str, Any]) -> dict[str, Any]:
    findings = Counter()
    affected: dict[str, list[str]] = {}

    for case in corpus.get("cases", []):
        case_findings = audit_case(case)
        if case_findings:
            affected[case["assessment_id"]] = case_findings
            findings.update(case_findings)

    blocking = sum(
        count for name, count in findings.items() if name.startswith("BLOCKING_")
    )
    signals = sum(
        count for name, count in findings.items() if name.startswith("SIGNAL_")
    )

    return {
        "case_count": corpus.get("case_count", len(corpus.get("cases", []))),
        "semantic_eligible_count": corpus.get("semantic_eligible_count"),
        "settled_case_count": corpus.get("settled_case_count"),
        "blocking_finding_count": blocking,
        "historical_signal_count": signals,
        "finding_counts": dict(sorted(findings.items())),
        "affected_case_count": len(affected),
        "affected_cases": affected,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--fail-on-blocking", action="store_true")
    args = parser.parse_args()

    report = summarize(load_corpus())
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.fail_on_blocking and report["blocking_finding_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
