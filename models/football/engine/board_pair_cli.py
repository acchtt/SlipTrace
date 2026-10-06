from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from adapter import ContractError, run_board

EXPECTED_MODELS = ("c", "c2")

MODEL_OWNED_FIELDS = {
    "board_state",
    "board_state_basis",
    "supported_line",
    "supported_line_basis",
    "completion_mode",
    "burden_completion_quality",
    "continuation_quality",
    "opponent_leakage",
    "burden_stall_risk",
}

C_ONLY_FIELDS = {
    "completion_mode",
    "burden_completion_quality",
    "continuation_quality",
    "opponent_leakage",
    "burden_stall_risk",
}

COMMON_EVIDENCE_REQUIRED_FIELDS = {
    "common_evidence_basis",
    "operational_viability_grade",
    "xi_expected",
    "market_observability",
    "team_news_observability",
    "operational_viability_reason",
    "competition_reliability_state",
    "competition_reliability_reason",
    "tournament_incentive_required",
}

MODEL_REQUIRED_FIELDS = {
    "c": {
        "board_state",
        "board_state_basis",
        "supported_line",
        "supported_line_basis",
        "completion_mode",
        "burden_completion_quality",
        "continuation_quality",
        "opponent_leakage",
        "burden_stall_risk",
    },
    "c2": {
        "board_state",
        "board_state_basis",
        "supported_line",
        "supported_line_basis",
    },
}


def _load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _indexed(payload: dict[str, Any], model: str) -> dict[str, dict[str, Any]]:
    matches = payload.get("matches")
    if not isinstance(matches, list) or not matches:
        raise ContractError(f"board pair model={model} must contain non-empty matches")

    indexed: dict[str, dict[str, Any]] = {}
    for row in matches:
        if not isinstance(row, dict):
            raise ContractError(f"board pair model={model} match must be an object")
        match_id = str(row.get("match_id", "")).strip()
        if not match_id:
            raise ContractError(f"board pair model={model} missing match_id")
        if match_id in indexed:
            raise ContractError(
                f"BOARD PAIR FAILED — DUPLICATE MATCH ID: model={model} match_id={match_id}"
            )
        indexed[match_id] = row
    return indexed


def _present(row: dict[str, Any], field: str) -> bool:
    if field not in row:
        return False
    value = row[field]
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True


def _validate_step1_contract(row: dict[str, Any], model: str, match_id: str) -> None:
    missing_common = sorted(
        field for field in COMMON_EVIDENCE_REQUIRED_FIELDS if not _present(row, field)
    )
    if missing_common:
        raise ContractError(
            "STEP1 CONTRACT FAILED — COMMON EVIDENCE INCOMPLETE: "
            f"model={model} match_id={match_id} missing={missing_common}"
        )

    if row.get("tournament_incentive_required") is True:
        tournament_fields = (
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
        )
        missing_tournament = sorted(
            field for field in tournament_fields if not _present(row, field)
        )
        if missing_tournament:
            raise ContractError(
                "STEP1 CONTRACT FAILED — TOURNAMENT INCENTIVE INCOMPLETE: "
                f"model={model} match_id={match_id} missing={missing_tournament}"
            )

    missing_model = sorted(
        field for field in MODEL_REQUIRED_FIELDS[model] if not _present(row, field)
    )
    if missing_model:
        raise ContractError(
            "STEP1 CONTRACT FAILED — MODEL SEMANTIC TRACE INCOMPLETE: "
            f"model={model} match_id={match_id} missing={missing_model}"
        )


def _common_view(row: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in row.items() if k not in MODEL_OWNED_FIELDS}


def run_board_pair(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
) -> dict[str, Any]:
    """Run active C+C2 Step-1 boards as one common-evidence fail-closed unit."""
    payloads = {"c": c_payload, "c2": c2_payload}

    for expected_model in EXPECTED_MODELS:
        payload = payloads[expected_model]
        actual_model = str(payload.get("model", "")).lower()
        if actual_model != expected_model:
            raise ContractError(
                f"board pair payload mismatch: expected model={expected_model}, got {actual_model or '<missing>'}"
            )
        if payload.get("stage") != "board":
            raise ContractError(
                f"board pair payload model={expected_model} must use stage=board"
            )

    indexed = {model: _indexed(payloads[model], model) for model in EXPECTED_MODELS}
    match_sets = {model: set(rows) for model, rows in indexed.items()}
    if match_sets["c"] != match_sets["c2"]:
        raise ContractError("BOARD PAIR FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH")

    for match_id in sorted(match_sets["c"]):
        for model in EXPECTED_MODELS:
            _validate_step1_contract(indexed[model][match_id], model, match_id)

        if _common_view(indexed["c"][match_id]) != _common_view(indexed["c2"][match_id]):
            raise ContractError(
                "BOARD PAIR FAILED — COMMON EVIDENCE DRIFT: "
                f"match_id={match_id}"
            )

        leaked_c2 = sorted(set(indexed["c2"][match_id]) & C_ONLY_FIELDS)
        if leaked_c2:
            raise ContractError(
                "BOARD PAIR FAILED — C POLICY FIELD LEAK INTO C2 PAYLOAD: "
                f"match_id={match_id} c2={leaked_c2}"
            )

    results = {model: run_board(payloads[model]) for model in EXPECTED_MODELS}

    return {
        "board_engine_execution_status": "EXECUTED_C_C2_BOARDS",
        "models_executed": list(EXPECTED_MODELS),
        "common_evidence_reconciled": True,
        "match_count": len(match_sets["c"]),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Football C+C2 Step-1 board validation with common-evidence reconciliation"
    )
    parser.add_argument("--c", required=True, help="Football C board payload JSON")
    parser.add_argument("--c2", required=True, help="Football C2 board payload JSON")
    args = parser.parse_args()

    try:
        result = run_board_pair(_load(args.c), _load(args.c2))
    except (ContractError, ValueError, KeyError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({
            "ok": False,
            "board_engine_execution_status": "FAILED_AFTER_ATTEMPT",
            "error": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2

    print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
