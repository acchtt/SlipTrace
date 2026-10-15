#!/usr/bin/env python3
"""Build the public-safe football-v2 board projection from Google Sheets rows.

This module never talks to Google Sheets directly. The orchestration layer reads
only the allowlisted public tabs, passes their refetched rows here, then writes
the resulting JSON to acchtt/football-v2/pages/data/board-feed.json.

Private tabs (Decision States, Actual Bets, engine evidence beyond the exact
board result stored in the coverage row) are never projection inputs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

SCHEMA = "football-v2-public-board-feed-v1"
SOURCE_STORE = "GOOGLE_SHEETS"
SOURCE_WORKBOOK = "Football v2 — Active Operations"
ALLOWED_INPUT_TABS = frozenset(("Daily Coverage Ledger", "Website Picks"))
FORBIDDEN_INPUT_TABS = frozenset((
    "Decision States",
    "Actual Bets — Current",
    "Competition Reliability Events",
    "Factor Calibration Observations",
))
LANE_TO_TIER = {
    "FOLLOW": "FOCUS",
    "RESERVE": "WATCHLIST",
    "STOP": "PASS",
}


class ProjectionError(ValueError):
    pass


def _text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


def _int(value: Any) -> int | None:
    n = _number(value)
    if n is None or int(n) != n:
        return None
    return int(n)


def _slate_date(row: dict[str, Any], kickoff: str) -> str:
    explicit = _text(row.get("Slate Date") or row.get("slateDate"))
    if explicit:
        return explicit
    if "T" in kickoff:
        return kickoff.split("T", 1)[0]
    return ""


def _coverage_row(row: dict[str, Any]) -> dict[str, Any] | None:
    coverage_id = _text(row.get("Coverage ID") or row.get("coverage_id"))
    run_id = _text(row.get("Run ID") or row.get("run_id"))
    match = _text(row.get("Match") or row.get("match"))
    kickoff = _text(row.get("Kickoff ICT") or row.get("kickoff_ict"))
    lane = _text(row.get("C Follow Lane") or row.get("follow_lane")).upper()
    if not coverage_id or not run_id or not match or not kickoff or lane not in LANE_TO_TIER:
        return None
    rank = _int(row.get("C Rank") if "C Rank" in row else row.get("c_rank"))
    line = _number(
        row.get("C Supported Line")
        if "C Supported Line" in row
        else row.get("c_supported_line")
    )
    return {
        "id": coverage_id,
        "sourceCoverageId": coverage_id,
        "boardId": run_id,
        "slateDate": _slate_date(row, kickoff),
        "match": match,
        "competition": _text(row.get("Competition") or row.get("competition")),
        "kickoff": kickoff,
        "displayKickoff": kickoff,
        "tier": LANE_TO_TIER[lane],
        "followLane": lane,
        "cBoardState": _text(
            row.get("C Board State") or row.get("c_board_state")
        ),
        "cRank": rank,
        "cSupportedLine": line,
        "grade": _text(
            row.get("Operational Grade") or row.get("operational_grade")
        ),
        "structure": "",
        "xiStatus": "",
        "marketStatus": "",
        "coverageStatus": _text(
            row.get("Eligibility") or row.get("eligibility")
        ),
        "frozenPreSummary": "",
        "coverageNotes": "",
        "manualScore": None,
        "bsd": None,
    }


def _pick_row(row: dict[str, Any]) -> dict[str, Any] | None:
    key = _text(row.get("Publication Key") or row.get("publication_key"))
    match = _text(row.get("Match") or row.get("match"))
    kickoff = _text(row.get("Kickoff ICT") or row.get("kickoff_ict"))
    if not key or not match or not kickoff:
        return None
    line = _number(row.get("Line") if "Line" in row else row.get("line"))
    odds = _number(row.get("Odds") if "Odds" in row else row.get("odds"))
    return {
        "id": key,
        "pickId": key,
        "publicationKey": key,
        "match": match,
        "competition": _text(row.get("Competition") or row.get("competition")),
        "kickoff": kickoff,
        "displayKickoff": kickoff,
        "modelVersion": "Football C",
        "verdict": _text(row.get("C Action") or row.get("c_action")),
        "line": line,
        "odds": odds,
        "result": _text(row.get("Result Status") or row.get("result")) or "PENDING",
        "recordedAt": _text(row.get("Published At UTC") or row.get("published_at_utc")) or kickoff,
        "manualScore": None,
        "bsd": None,
    }


def build_projection(
    coverage_rows: list[dict[str, Any]],
    pick_rows: list[dict[str, Any]],
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    if not isinstance(coverage_rows, list) or not isinstance(pick_rows, list):
        raise ProjectionError("coverage_rows and pick_rows must be lists")
    schedule = [item for row in coverage_rows if (item := _coverage_row(row))]
    picks = [item for row in pick_rows if (item := _pick_row(row))]
    schedule.sort(key=lambda row: (row["kickoff"], row["cRank"] or 10**9, row["id"]))
    picks.sort(key=lambda row: (row["recordedAt"], row["id"]), reverse=True)
    return {
        "schemaVersion": SCHEMA,
        "sourceStore": SOURCE_STORE,
        "sourceWorkbook": SOURCE_WORKBOOK,
        "generatedAt": generated_at or datetime.now(timezone.utc).isoformat(),
        "projectionPolicy": "PUBLIC_SAFE_GOOGLE_SHEETS_V1",
        "schedule": schedule,
        "picks": picks,
    }


def _load_rows(path: str, expected_tab: str) -> list[dict[str, Any]]:
    if expected_tab not in ALLOWED_INPUT_TABS:
        raise ProjectionError(f"projection input tab is not allowlisted: {expected_tab}")
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        tab = payload.get("sheet_name") or payload.get("sheetName")
        if tab and tab != expected_tab:
            raise ProjectionError(
                f"projection input tab mismatch: expected {expected_tab}, got {tab}"
            )
        rows = payload.get("rows")
    else:
        rows = payload
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ProjectionError(f"{expected_tab}: list of row objects required")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build public-safe football-v2 board feed")
    parser.add_argument("--coverage", required=True)
    parser.add_argument("--picks", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--generated-at")
    args = parser.parse_args()
    projection = build_projection(
        _load_rows(args.coverage, "Daily Coverage Ledger"),
        _load_rows(args.picks, "Website Picks"),
        generated_at=args.generated_at,
    )
    Path(args.output).write_text(
        json.dumps(projection, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
