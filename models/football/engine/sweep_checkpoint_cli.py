from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sweep_checkpoint import (
    SweepCheckpointError,
    advance_after_chunk,
    select_verification_chunk,
    validate_checkpoint,
)


def _load(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Football sweep checkpoint helper")
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("validate")
    v.add_argument("--input", required=True)

    s = sub.add_parser("select")
    s.add_argument("--input", required=True)

    a = sub.add_parser("advance")
    a.add_argument("--input", required=True)
    a.add_argument("--completed", default="")
    a.add_argument("--retry", default="")

    args = parser.parse_args()

    try:
        payload = _load(args.input)
        if args.command == "validate":
            out = {"ok": True, **validate_checkpoint(payload)}
        elif args.command == "select":
            out = {"ok": True, **select_verification_chunk(payload).to_dict()}
        else:
            completed = [x for x in args.completed.split(";") if x]
            retry = [x for x in args.retry.split(";") if x]
            out = {
                "ok": True,
                **advance_after_chunk(
                    payload,
                    completed_blocks=completed,
                    retry_blocks=retry,
                ),
            }
    except (OSError, json.JSONDecodeError, SweepCheckpointError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "status": "SWEEP CHECKPOINT FAILED",
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
