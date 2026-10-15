"""RETIRED historical C+C2 decision-pair entrypoint.

Retired 2026-10-15. Football C is the only active model. Frozen historical
pair receipts remain immutable; they are not replayed through this module.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from adapter import ContractError

RETIRED_REASON = (
    "C2 is retired; active production executes Football C only via "
    "adapter.py / xi_portable.py"
)


def run_pair(c_payload: dict[str, Any], c2_payload: dict[str, Any]) -> dict[str, Any]:
    raise ContractError(RETIRED_REASON)


def run_football_pair(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
) -> dict[str, Any]:
    raise ContractError(RETIRED_REASON)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="RETIRED Football C+C2 pair runner"
    )
    parser.parse_args()
    print(json.dumps({
        "ok": False,
        "status": "RETIRED_MODEL_PATH",
        "reason": RETIRED_REASON,
    }), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
