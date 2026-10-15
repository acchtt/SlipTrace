"""RETIRED historical C+C2 board-pair entrypoint.

Retired 2026-10-15. V4 /rank executes the single active Football C board
through adapter.run_board(). Frozen historical pair receipts remain immutable.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from adapter import ContractError

RETIRED_REASON = (
    "C2 is retired; active V4 /rank executes Football C only through "
    "stages_v4/stage.py and adapter.run_board"
)


def run_board_pair(
    c_payload: dict[str, Any],
    c2_payload: dict[str, Any],
) -> dict[str, Any]:
    raise ContractError(RETIRED_REASON)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="RETIRED Football C+C2 board pair runner"
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
