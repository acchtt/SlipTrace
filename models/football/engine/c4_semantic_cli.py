from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from c4_semantic import C4ContractError, compile_board


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Football C4 structured-evidence Step-1 shadow compiler"
    )
    parser.add_argument("--input", required=True, help="C4 board payload JSON")
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = compile_board(payload)
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
