from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from capacity_replenishment import (
    CapacityReplenishmentError,
    select_initial_work_wave,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministically freeze the first Football Step-0 Work wave"
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise CapacityReplenishmentError("initial wave input must be an object")
        result = select_initial_work_wave(
            payload.get("candidates"), budget_policy=payload.get("budget_policy")
        )
    except (OSError, json.JSONDecodeError, CapacityReplenishmentError) as exc:
        print(
            json.dumps(
                {"ok": False, "status": "CAPACITY INITIAL WAVE FAILED", "error": str(exc)},
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
