"""Strict Google Sheets routing for active Football v2 operations.

Google Sheets is the active persistence/readback store from 2026-10-15.
Airtable bases are historical read-only and must never receive new writes.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
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
        if not confirmed_user_slip or workflow not in {"xi", "model_accounting", "audit"}:
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


def parent_first_persistence_plan(
    *, run_id: str, coverage_ids: list[str]
) -> dict[str, Any]:
    """Return the only allowed Sweep Runs -> coverage write sequence."""

    if not isinstance(run_id, str) or not run_id.strip():
        raise GoogleSheetsRouteError("parent Run ID required")
    if (
        not isinstance(coverage_ids, list)
        or any(not isinstance(value, str) for value in coverage_ids)
        or len(set(coverage_ids)) != len(coverage_ids)
        or any(not value.startswith(run_id + "|") for value in coverage_ids)
    ):
        raise GoogleSheetsRouteError(
            "coverage identities must be unique children of the parent Run ID"
        )
    return {
        "policy": "SWEEP_PARENT_READBACK_BEFORE_COVERAGE_CHILDREN_V1",
        "publication_fail_closed": True,
        "steps": [
            {
                "step": 1,
                "operation": "UPSERT",
                "sheet": "Sweep Runs",
                "key_column": "Run ID",
                "keys": [run_id],
            },
            {
                "step": 2,
                "operation": "INDEPENDENT_REFETCH",
                "sheet": "Sweep Runs",
                "key_column": "Run ID",
                "keys": [run_id],
            },
            {
                "step": 3,
                "operation": "UPSERT",
                "sheet": "Daily Coverage Ledger",
                "key_column": "Coverage ID",
                "keys": coverage_ids,
            },
            {
                "step": 4,
                "operation": "INDEPENDENT_REFETCH",
                "sheet": "Daily Coverage Ledger",
                "key_column": "Coverage ID",
                "keys": coverage_ids,
            },
        ],
    }


def _utc_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise GoogleSheetsRouteError(f"{field} timestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise GoogleSheetsRouteError(f"{field} timestamp invalid") from None
    if parsed.tzinfo is None:
        raise GoogleSheetsRouteError(f"{field} timezone required")
    return parsed.astimezone(timezone.utc)


def verify_parent_before_children(
    *,
    run_id: str,
    sweep_integrity_sha256: str,
    parent_readback: dict[str, Any],
    coverage_write_started_at_utc: str,
    coverage_readback_at_utc: str,
) -> bool:
    """Fail closed unless the exact parent existed before child writes began."""

    cfg = _configuration()
    if not isinstance(parent_readback, dict):
        raise GoogleSheetsRouteError("SWEEP_PARENT_READBACK_REQUIRED")
    if (
        parent_readback.get("spreadsheet_id") != cfg["spreadsheet_id"]
        or parent_readback.get("sheet_name") != "Sweep Runs"
        or parent_readback.get("method") != "INDEPENDENT_GOOGLE_SHEETS_REFETCH"
        or parent_readback.get("run_id") != run_id
        or parent_readback.get("sweep_integrity_sha256") != sweep_integrity_sha256
        or parent_readback.get("exists") is not True
    ):
        raise GoogleSheetsRouteError(
            "SWEEP_PARENT_READBACK_REQUIRED: exact Sweep Runs parent missing"
        )
    parent_at = _utc_time(
        parent_readback.get("readback_at_utc"), "parent readback"
    )
    child_write_at = _utc_time(
        coverage_write_started_at_utc, "coverage write start"
    )
    child_read_at = _utc_time(
        coverage_readback_at_utc, "coverage readback"
    )
    if not parent_at <= child_write_at <= child_read_at:
        raise GoogleSheetsRouteError(
            "PARENT_CHILD_PERSISTENCE_ORDER_INVALID: parent readback must precede "
            "coverage write and readback"
        )
    return True
