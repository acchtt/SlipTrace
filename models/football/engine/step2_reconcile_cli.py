from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from step2_reconcile import Step2ReconciliationError, reconcile_step2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that every due Football Step-2 fixture is accounted for"
    )
    parser.add_argument("--input", required=True, help="Step-2 reconciliation JSON")
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = reconcile_step2(payload)
    except (OSError, json.JSONDecodeError, Step2ReconciliationError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "step2_reconciliation_status": "FAILED",
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
                "step2_reconciliation_status": "PASS",
                **result,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
