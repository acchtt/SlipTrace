from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from adapter import ContractError, run_decision

EXPECTED_MODELS = ("c", "c2")

COMMON_MATCH_FIELDS = (
    "match_id",
    "home_route",
    "away_route",
    "carrier",
    "route_reliability",
    "independent_route_quality",
    "chance_quality",
    "failure_resistance",
    "xi_robustness",
    "evidence_confidence",
    "burden_protection",
    "common_evidence_basis",
    "main_failure",
    "h2h_state",
    "h2h_effect",
    "h2h_transferability",
    "h2h_current_corroboration",
    "h2h_material_effect",
    "h2h_basis",
    "carrier_self_fund",
    "carrier_self_fund_basis",
    "independent_upper_tail",
    "independent_upper_tail_basis",
    "failure_attacks_route",
    "failure_attacks_route_basis",
    "material_suppression",
    "material_suppression_basis",
    "operational_viability_grade",
    "raw_operational_viability_grade",
    "competition_reliability_state",
    "competition_reliability_reason",
    "competition_reliability_manual_override",
    "demoted_probation",
    "xi_expected",
    "market_observability",
    "team_news_observability",
    "operational_viability_reason",
    "tournament_incentive_required",
    "tournament_format_status",
    "competition_stage",
    "competition_format",
    "draw_resolution",
    "aggregate_state",
    "qualification_state",
    "simultaneous_results_status",
    "simultaneous_results_note",
    "home_incentive",
    "away_incentive",
    "tiebreak_margin_relevance",
    "incentive_effect",
    "kickoff_ict",
)

COMMON_CONTEXT_FIELDS = (
    "official_follow_lane",
    "step2_authorization",
    "xi_status",
    "post_xi_research_status",
    "post_xi_research_note",
    "fixture_status",
    "quote_revalidated",
    "market_history_status",
    "market_history_movement",
    "market_history_conflict_recheck",
    "market_history_note",
    "h2h_review_status",
    "h2h_rechecked",
    "h2h_basis",
    "tournament_incentive_rechecked",
    "tournament_incentive_recheck_status",
)


def _load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _epoch_signature(payload: dict[str, Any]) -> str:
    match = payload.get("match")
    context = payload.get("context")
    if not isinstance(match, dict):
        raise ContractError("C+C2 pair requires match object")
    if not isinstance(context, dict):
        raise ContractError("C+C2 pair requires context object")
    frozen = {
        "match": {key: match.get(key) for key in COMMON_MATCH_FIELDS},
        "context": {key: context.get(key) for key in COMMON_CONTEXT_FIELDS},
    }
    return json.dumps(frozen, sort_keys=True, separators=(",", ":"))


def run_pair(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
) -> dict[str, Any]:
    """Run C and C2 as one fail-closed Step-2 validation unit."""
    payloads = {"c": c_payload, "c2": c2_payload}
    signatures = set()

    for expected_model in EXPECTED_MODELS:
        payload = payloads[expected_model]
        actual_model = str(payload.get("model", "")).lower()
        if actual_model != expected_model:
            raise ContractError(
                f"pair payload mismatch: expected model={expected_model}, got {actual_model or '<missing>'}"
            )
        if payload.get("stage") != "decision":
            raise ContractError(
                f"pair payload model={expected_model} must use stage=decision"
            )
        signatures.add(_epoch_signature(payload))

    if len(signatures) != 1:
        raise ContractError(
            "C+C2 pair must share the same frozen common evidence epoch"
        )

    results = {model: run_decision(payloads[model]) for model in EXPECTED_MODELS}

    return {
        "engine_execution_status": "EXECUTED_C_C2_PAIR",
        "models_executed": list(EXPECTED_MODELS),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run mandatory Football C+C2 Step-2 deterministic validation"
    )
    parser.add_argument("--c", required=True, help="Football C decision payload JSON")
    parser.add_argument("--c2", required=True, help="Football C2 decision payload JSON")
    args = parser.parse_args()

    try:
        result = run_pair(_load(args.c), _load(args.c2))
    except (ContractError, ValueError, KeyError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({
            "ok": False,
            "engine_execution_status": "FAILED_AFTER_ATTEMPT",
            "error": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2

    print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
