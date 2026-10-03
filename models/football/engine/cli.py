from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapter import ContractError, dumps, run_audit_record, run_board, run_decision


def _load(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return json.load(sys.stdin)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic Football C/C2 validation engine"
    )
    parser.add_argument(
        "command",
        choices=("board", "decision", "audit"),
        help="run board ranking, one XI/odds decision, or validate one audit record",
    )
    parser.add_argument(
        "--input",
        help="JSON input file; omit to read stdin",
    )
    args = parser.parse_args()

    try:
        payload = _load(args.input)
        if args.command == "board":
            result = run_board(payload)
        elif args.command == "decision":
            result = run_decision(payload)
        else:
            result = run_audit_record(payload)
    except (ContractError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(dumps({"ok": True, **result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
