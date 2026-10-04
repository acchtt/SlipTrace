from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from adapter import ContractError, run_decision

EXPECTED_MODELS = ("c", "c2", "c3")


def _load(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run_triplet(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
    c3_payload: dict[str, Any],
) -> dict[str, Any]:
    """Run all three Step-2 validators as one fail-closed unit."""

    payloads = {
        "c": c_payload,
        "c2": c2_payload,
        "c3": c3_payload,
    }

    for expected_model in EXPECTED_MODELS:
        payload = payloads[expected_model]
        actual_model = str(payload.get("model", "")).lower()
        if actual_model != expected_model:
            raise ContractError(
                f"triplet payload mismatch: expected model={expected_model}, got {actual_model or '<missing>'}"
            )
        if payload.get("stage") != "decision":
            raise ContractError(
                f"triplet payload model={expected_model} must use stage=decision"
            )

    results: dict[str, Any] = {}
    for model in EXPECTED_MODELS:
        results[model] = run_decision(payloads[model])

    return {
        "engine_execution_status": "EXECUTED_ALL_THREE",
        "models_executed": list(EXPECTED_MODELS),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run mandatory Football C/C2/C3 Step-2 deterministic validation"
    )
    parser.add_argument("--c", required=True, help="Football C decision payload JSON")
    parser.add_argument("--c2", required=True, help="Football C2 decision payload JSON")
    parser.add_argument("--c3", required=True, help="Football C3 decision payload JSON")
    args = parser.parse_args()

    try:
        result = run_triplet(
            _load(args.c),
            _load(args.c2),
            _load(args.c3),
        )
    except (ContractError, ValueError, KeyError, json.JSONDecodeError, OSError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "engine_execution_status": "FAILED_AFTER_ATTEMPT",
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
