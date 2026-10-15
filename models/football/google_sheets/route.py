"""Strict Google Sheets routing for active Football v2 operations.

Google Sheets is the active persistence/readback store from 2026-10-15.
Airtable bases are historical read-only and must never receive new writes.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONFIG_PATH = Path(__file__).with_name("ACTIVE_STORE_ROUTING.json")
STORE_ACTIONS = frozenset(("read", "create", "update", "upsert", "append"))


class GoogleSheetsRouteError(ValueError):
    pass


def _configuration() -> dict[str, Any]:
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if cfg.get("schema_version") != "football-google-sheets-routing-v1":
        raise GoogleSheetsRouteError("unknown active-store routing schema")
    sid = cfg.get("spreadsheet_id")
    if not isinstance(sid, str) or not sid.strip():
        raise GoogleSheetsRouteError("active Google Sheets spreadsheet_id missing")
    tabs = cfg.get("tabs")
    if not isinstance(tabs, dict) or "Daily Coverage Ledger" not in tabs:
        raise GoogleSheetsRouteError("active Google Sheets tab map incomplete")
    legacy = cfg.get("legacy_airtable")
    if not isinstance(legacy, dict) or legacy.get("policy") != "HISTORICAL_READ_ONLY_NO_NEW_WRITES":
        raise GoogleSheetsRouteError("Airtable historical-only boundary missing")
    return cfg


def resolve_tab(
    workflow: str,
    tab: str,
    *,
    action: str = "read",
    confirmed_user_slip: bool = False,
) -> dict[str, str]:
    """Return the active spreadsheet/tab/key-column contract for one workflow."""

    cfg = _configuration()
    if workflow not in cfg["workflow_scope"]:
        raise GoogleSheetsRouteError(f"unsupported football workflow: {workflow!r}")
    if action not in STORE_ACTIONS:
        raise GoogleSheetsRouteError(f"unsupported Google Sheets action: {action}")
    spec = cfg["tabs"].get(tab)
    if not isinstance(spec, dict):
        raise GoogleSheetsRouteError(f"unknown active sheet tab: {tab!r}")
    if tab == "Actual Bets — Current" and action != "read":
        if not confirmed_user_slip or workflow not in {"model_accounting", "audit"}:
            raise GoogleSheetsRouteError(
                "actual user bets require explicit verified user slip"
            )
    return {
        "spreadsheetId": cfg["spreadsheet_id"],
        "spreadsheetUrl": cfg["spreadsheet_url"],
        "sheetName": tab,
        "keyColumn": spec["key_column"],
        "workflow": workflow,
        "action": action,
    }


def verify_receipt(
    *,
    expected_spreadsheet: str,
    expected_sheet: str,
    actual_spreadsheet: str,
    actual_sheet: str,
    row_key: str,
    original_record_identity: str,
    readback_record_identity: str,
) -> bool:
    """Fail closed on wrong workbook/tab or mismatched immutable-key readback."""

    cfg = _configuration()
    if (
        expected_spreadsheet != cfg["spreadsheet_id"]
        or actual_spreadsheet != expected_spreadsheet
    ):
        raise GoogleSheetsRouteError(
            "MODEL_SPREADSHEET_MISMATCH: refused cross-workbook write/readback"
        )
    if expected_sheet not in cfg["tabs"] or actual_sheet != expected_sheet:
        raise GoogleSheetsRouteError("MODEL_SHEET_MISMATCH: wrong active tab")
    if not isinstance(row_key, str) or not row_key.strip():
        raise GoogleSheetsRouteError(
            "missing immutable row key from actual Google Sheets readback"
        )
    if (
        not original_record_identity
        or original_record_identity != readback_record_identity
        or row_key != readback_record_identity
    ):
        raise GoogleSheetsRouteError(
            "MODEL_WRITE_READBACK_MISMATCH: immutable row identity differs"
        )
    return True
