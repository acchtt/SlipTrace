from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from capacity_replenishment import (
    CapacityReplenishmentError,
    next_replenishment_wave,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate and select the next Football Step-1 capacity replenishment wave"
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = next_replenishment_wave(payload)
    except (OSError, json.JSONDecodeError, CapacityReplenishmentError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "status": "CAPACITY REPLENISHMENT FAILED",
                    "error": str(exc),
                },
                indent=2,
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(
        json.dumps(
            {
                "ok": True,
                "capacity_replenishment_status": result["status"],
                **result,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
