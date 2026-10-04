from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from adapter import ContractError, run_board

EXPECTED_MODELS = ("c", "c2", "c3")

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
    "c3_second_route_role",
    "c3_second_route_role_basis",
    "c3_goal3_funding",
    "c3_goal3_funding_source",
    "c3_goal3_funding_basis",
    "c3_goal4_funding",
    "c3_goal4_funding_source",
    "c3_goal4_funding_basis",
    "c3_control_endpoint_risk",
    "c3_control_endpoint_basis",
    "c3_forced_chaos_verified",
    "c3_forced_chaos_basis",
}

C_ONLY_FIELDS = {
    "completion_mode",
    "burden_completion_quality",
    "continuation_quality",
    "opponent_leakage",
    "burden_stall_risk",
}

C3_ONLY_FIELDS = {
    "c3_second_route_role",
    "c3_second_route_role_basis",
    "c3_goal3_funding",
    "c3_goal3_funding_source",
    "c3_goal3_funding_basis",
    "c3_goal4_funding",
    "c3_goal4_funding_source",
    "c3_goal4_funding_basis",
    "c3_control_endpoint_risk",
    "c3_control_endpoint_basis",
    "c3_forced_chaos_verified",
    "c3_forced_chaos_basis",
}


def _load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _indexed(payload: dict[str, Any], model: str) -> dict[str, dict[str, Any]]:
    matches = payload.get("matches")
    if not isinstance(matches, list) or not matches:
        raise ContractError(f"board triplet model={model} must contain non-empty matches")

    indexed: dict[str, dict[str, Any]] = {}
    for row in matches:
        if not isinstance(row, dict):
            raise ContractError(f"board triplet model={model} match must be an object")
        match_id = str(row.get("match_id", "")).strip()
        if not match_id:
            raise ContractError(f"board triplet model={model} missing match_id")
        if match_id in indexed:
            raise ContractError(
                f"BOARD TRIPLET FAILED — DUPLICATE MATCH ID: model={model} match_id={match_id}"
            )
        indexed[match_id] = row
    return indexed


def _common_view(row: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in row.items() if k not in MODEL_OWNED_FIELDS}


def run_board_triplet(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
    c3_payload: dict[str, Any],
) -> dict[str, Any]:
    """Run Step-1 C/C2/C3 boards as one common-evidence fail-closed unit."""

    payloads = {"c": c_payload, "c2": c2_payload, "c3": c3_payload}

    for expected_model in EXPECTED_MODELS:
        payload = payloads[expected_model]
        actual_model = str(payload.get("model", "")).lower()
        if actual_model != expected_model:
            raise ContractError(
                f"board triplet payload mismatch: expected model={expected_model}, got {actual_model or '<missing>'}"
            )
        if payload.get("stage") != "board":
            raise ContractError(
                f"board triplet payload model={expected_model} must use stage=board"
            )

    indexed = {model: _indexed(payloads[model], model) for model in EXPECTED_MODELS}
    match_sets = {model: set(rows) for model, rows in indexed.items()}
    if not (match_sets["c"] == match_sets["c2"] == match_sets["c3"]):
        raise ContractError(
            "BOARD TRIPLET FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH"
        )

    for match_id in sorted(match_sets["c"]):
        common = {
            model: _common_view(indexed[model][match_id])
            for model in EXPECTED_MODELS
        }
        if not (common["c"] == common["c2"] == common["c3"]):
            raise ContractError(
                "BOARD TRIPLET FAILED — COMMON EVIDENCE DRIFT: "
                f"match_id={match_id}"
            )

        c2_keys = set(indexed["c2"][match_id])
        c3_keys = set(indexed["c3"][match_id])
        c_keys = set(indexed["c"][match_id])

        leaked_c2 = sorted(c2_keys & C_ONLY_FIELDS)
        leaked_c3 = sorted(c3_keys & C_ONLY_FIELDS)
        if leaked_c2 or leaked_c3:
            raise ContractError(
                "BOARD TRIPLET FAILED — C POLICY FIELD LEAK INTO SHADOW PAYLOAD: "
                f"match_id={match_id} c2={leaked_c2} c3={leaked_c3}"
            )

        leaked_c = sorted(c_keys & C3_ONLY_FIELDS)
        leaked_c2_c3 = sorted(c2_keys & C3_ONLY_FIELDS)
        if leaked_c or leaked_c2_c3:
            raise ContractError(
                "BOARD TRIPLET FAILED — C3 POLICY FIELD LEAK INTO C/C2 PAYLOAD: "
                f"match_id={match_id} c={leaked_c} c2={leaked_c2_c3}"
            )

    results = {model: run_board(payloads[model]) for model in EXPECTED_MODELS}

    return {
        "board_engine_execution_status": "EXECUTED_ALL_THREE_BOARDS",
        "models_executed": list(EXPECTED_MODELS),
        "common_evidence_reconciled": True,
        "match_count": len(match_sets["c"]),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Football C/C2/C3 Step-1 board validation with common-evidence reconciliation"
    )
    parser.add_argument("--c", required=True, help="Football C board payload JSON")
    parser.add_argument("--c2", required=True, help="Football C2 board payload JSON")
    parser.add_argument("--c3", required=True, help="Football C3 board payload JSON")
    args = parser.parse_args()

    try:
        result = run_board_triplet(_load(args.c), _load(args.c2), _load(args.c3))
    except (ContractError, ValueError, KeyError, json.JSONDecodeError, OSError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "board_engine_execution_status": "FAILED_AFTER_ATTEMPT",
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
