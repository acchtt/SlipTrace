#!/usr/bin/env python3
"""Thin deterministic runtime for primary Football C block selection.

This runtime compiles each candidate through the existing Football C board
compiler, then applies BLOCK_PRIORITY_V1.  It cannot evaluate prices and cannot
publish ACT/BOOK/PASS.  Priced decisions remain owned by the XI runtime plus
Decision States persistence/readback.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ENGINE = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))

from adapter import run_board  # noqa: E402
from block_priority import POLICY, BlockPriorityError, rank_block  # noqa: E402

SCHEMA = "football-block-runtime-v1"
PRICE_FIELDS = frozenset({
    "quote", "quotes", "odds", "price", "bookmaker_total", "market_line",
    "market_odds", "visible_ladder", "screenshot_odds",
})


class BlockRuntimeError(ValueError):
    pass


def _reject_price_fields(obj: Any, *, path: str = "payload") -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in PRICE_FIELDS and value is not None:
                raise BlockRuntimeError(
                    f"{path}.{key}: block runtime is football-only; use XI runtime for price"
                )
            _reject_price_fields(value, path=f"{path}.{key}")
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            _reject_price_fields(value, path=f"{path}[{index}]")


def run_block(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise BlockRuntimeError("block payload must be an object")
    if payload.get("schema_version") != SCHEMA:
        raise BlockRuntimeError(f"schema_version must be {SCHEMA}")
    if str(payload.get("model") or "").lower() != "c":
        raise BlockRuntimeError("Football C is the only active block model")

    matches = payload.get("matches")
    if not isinstance(matches, list) or len(matches) < 2:
        raise BlockRuntimeError("complete block requires at least two candidate matches")
    _reject_price_fields(payload)

    board = run_board({
        "schema_version": "football-engine-v1",
        "stage": "board",
        "model": "c",
        "matches": matches,
    })
    priority = rank_block(matches, board["matches"])
    priority_by_id = {row["match_id"]: row for row in priority}
    compiled_by_id = {
        str(row["match_id"]): row for row in board["matches"]
    }

    output = []
    for priority_row in priority:
        mid = priority_row["match_id"]
        compiled = compiled_by_id[mid]
        output.append({
            **priority_row,
            "global_rank_metadata": {
                "rank": compiled.get("rank"),
                "same_kickoff_rank": compiled.get("same_kickoff_rank"),
                "follow_lane": compiled.get("follow_lane"),
                "secondary_only": True,
            },
            "board_state": compiled.get("board_state"),
            "supported_line": compiled.get("supported_line"),
            "supported_line_basis": compiled.get("supported_line_basis"),
            "goal3_funded": compiled.get("goal3_funded"),
            "goal4_funded": compiled.get("goal4_funded"),
            "credible_tail_state": compiled.get("credible_tail_state"),
            "direct_act_ceiling": compiled.get("direct_act_ceiling"),
            "execution_strength": compiled.get("execution_strength"),
            "goal3_mechanism_class": compiled.get("goal3_mechanism_class"),
            "football_assessment_only": True,
            "priced_action": None,
        })

    return {
        "schema_version": SCHEMA,
        "stage": "block_result",
        "model": "c",
        "policy": POLICY,
        "match_count": len(output),
        "matches": output,
        "block_order": [row["match_id"] for row in output],
        "global_rank_is_selection_authority": False,
        "g3_g4_thresholds_changed": False,
        "price_execution_changed": False,
        "priced_publication_authorized": False,
        "publication_status": "FOOTBALL_ASSESSMENT_ONLY_PRICED_DECISION_NOT_PERSISTED",
        "priced_decision_requires": [
            "existing Football C XI deterministic runtime",
            "Decision States write",
            "independent Decision States readback",
            "Step2 publication guard",
        ],
        "outcome_fields_read": False,
    }


def _load(path: str | None) -> dict[str, Any]:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return json.load(sys.stdin)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Football C BLOCK_PRIORITY_V1")
    parser.add_argument("payload", nargs="?", help="JSON payload; stdin when omitted")
    args = parser.parse_args()
    try:
        print(json.dumps(run_block(_load(args.payload)), indent=2, sort_keys=True))
    except (BlockRuntimeError, BlockPriorityError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2))
        raise SystemExit(2)


if __name__ == "__main__":
    main()
