from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from model_bet_accounting import (
    ModelBetAccountingError,
    compile_fixture_accounting,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile/settle one C/C2/C3/C4 football model-accounting fixture"
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = compile_fixture_accounting(payload)
    except (OSError, json.JSONDecodeError, ModelBetAccountingError) as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "status": "MODEL ACCOUNTING FAILED",
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
