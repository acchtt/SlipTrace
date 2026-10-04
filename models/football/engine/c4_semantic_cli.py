from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from c4_semantic import C4ContractError, compile_board, reconcile_with_c_board


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Football C4 structured-evidence Step-1 shadow compiler"
    )
    parser.add_argument("--input", required=True, help="C4 board payload JSON")
    parser.add_argument(
        "--c-board",
        required=True,
        help="Frozen Football C board payload JSON used for universe/evidence reconciliation",
    )
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        c_payload = json.loads(Path(args.c_board).read_text(encoding="utf-8"))
        reconcile_with_c_board(payload, c_payload)
        result = compile_board(payload)
        result["c4_reconciled_with_c"] = True
    except (OSError, json.JSONDecodeError, C4ContractError, ValueError) as exc:
        print(
            json.dumps(
                {"ok": False, "c4_execution_status": "FAILED", "error": str(exc)},
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(
        json.dumps(
            {"ok": True, "c4_execution_status": "EXECUTED", **result},
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
