"""Strict model-only Airtable routing. /sweep routing is deliberately external.

The active routing manifest is authority for new /rank, /xi, /live,
model QA, accounting and reports. The model router never modifies
sweep-owned checkpoint records or writes to historical bases.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

CONFIG_PATH = Path(__file__).with_name("ACTIVE_MODEL_ROUTING.json")
MODEL_ACTIONS = frozenset(("read", "create", "update", "upsert"))


class AirtableRouteError(ValueError):
    pass


def _configuration() -> dict[str, Any]:
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if cfg.get("schema_version") != "football-airtable-model-routing-v1":
        raise AirtableRouteError("unknown model-routing schema")
    if cfg.get("explicitly_excluded_workflow") != "sweep":
        raise AirtableRouteError("sweep exemption missing")
    if cfg.get("sweep_policy") != "PRESERVE_EXISTING_SWEEP_ROUTING_UNMODIFIED":
        raise AirtableRouteError("sweep routing would be changed")
    if "Sweep Runs" in cfg.get("tables", {}):
        raise AirtableRouteError("sweep-only table cannot be registered as a model write")
    return cfg


def resolve_table(workflow: str, table: str, *,
                  action: str = "read",
                  confirmed_user_slip: bool = False) -> dict[str, str]:
    """Return explicit model base/table IDs for connector calls.

    For Step0 sweep source records, consume the original frozen ZIP
    and/or existing sweep-run evidence independently. This function is
    intentionally *not* a sweep connector or migration tool.
    """
    cfg = _configuration()
    if workflow not in cfg["workflow_scope"]:
        raise AirtableRouteError(f"unsupported model workflow: {workflow!r}; /sweep unchanged")
    if action not in MODEL_ACTIONS:
        raise AirtableRouteError(f"unsupported Airtable action: {action}")
    if table == "Sweep Runs":
        raise AirtableRouteError("Sweep Runs belongs exclusively to unchanged /sweep workflow")
    table_id = cfg["tables"].get(table)
    if not table_id:
        raise AirtableRouteError(f"unknown model table: {table!r}")
    if table == "Actual Bets — Current" and action != "read":
        if not confirmed_user_slip or workflow not in {"model_accounting", "audit"}:
            raise AirtableRouteError("actual user bets require explicit verified user slip")
    return {
        "baseId": cfg["base_id"],
        "tableId": table_id,
        "tableName": table,
        "workflow": workflow,
        "action": action,
    }


def verify_receipt(*, expected_base: str, expected_table: str,
                   actual_base: str, actual_table: str,
                   record_id: str, original_record_identity: str,
                   readback_record_identity: str) -> bool:
    """Fail closed on wrong destination or mismatched target readback."""
    cfg = _configuration()
    if expected_base != cfg["base_id"] or actual_base != expected_base:
        raise AirtableRouteError("MODEL_BASE_MISMATCH: refused old/cross-workspace write")
    if cfg["tables"].get(expected_table) != actual_table:
        raise AirtableRouteError("MODEL_TABLE_MISMATCH: wrong active table")
    if (not isinstance(record_id, str) or not record_id.startswith("rec")
            or len(record_id) != 17):
        raise AirtableRouteError("missing target record ID from actual Airtable readback")
    if (not original_record_identity or
            original_record_identity != readback_record_identity):
        raise AirtableRouteError("MODEL_WRITE_READBACK_MISMATCH: original identity differs")
    return True
