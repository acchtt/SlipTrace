from __future__ import annotations

import json
from typing import Any


SCHEMA_VERSION = "football-step2-reconcile-v1"

ALLOWED_LANES = {"FOLLOW", "RESERVE", "STOP"}
ALLOWED_AUTH = {"ROUTINE_FOLLOW", "RESERVE_ACTIVATED", "USER_EXCEPTION"}
ALLOWED_OUTCOMES = {
    "DECISION_STATE_PERSISTED",
    "WAITING_FOR_USER_XI_ODDS",
    "FIXTURE_STATUS_BLOCKED",
    "INTEGRITY_BLOCKED",
    "ENGINE_FAILED_AFTER_ATTEMPT",
    "LIVE_REROUTED",
}


class Step2ReconciliationError(ValueError):
    pass


def _required(obj: dict[str, Any], key: str) -> Any:
    if key not in obj:
        raise Step2ReconciliationError(f"missing required field: {key}")
    return obj[key]


def _text(obj: dict[str, Any], key: str) -> str:
    value = _required(obj, key)
    if not isinstance(value, str) or not value.strip():
        raise Step2ReconciliationError(f"{key} must be a non-empty string")
    return value.strip()


def reconcile_step2(payload: dict[str, Any]) -> dict[str, Any]:
    """Fail closed when any due Step-2 fixture is silently omitted."""

    if not isinstance(payload, dict):
        raise Step2ReconciliationError("payload must be an object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise Step2ReconciliationError(
            f"schema_version must be {SCHEMA_VERSION!r}"
        )
    if payload.get("stage") != "step2_reconcile":
        raise Step2ReconciliationError("stage must be 'step2_reconcile'")

    session_id = _text(payload, "session_id")
    due = _required(payload, "due")
    outcomes = _required(payload, "outcomes")
    if not isinstance(due, list):
        raise Step2ReconciliationError("due must be an array")
    if not isinstance(outcomes, list):
        raise Step2ReconciliationError("outcomes must be an array")

    due_by_id: dict[str, dict[str, str]] = {}
    for row in due:
        if not isinstance(row, dict):
            raise Step2ReconciliationError("due entries must be objects")
        match_id = _text(row, "match_id")
        lane = _text(row, "official_follow_lane").upper()
        auth = _text(row, "step2_authorization").upper()

        if match_id in due_by_id:
            raise Step2ReconciliationError(
                f"STEP2 RECONCILIATION FAILED — DUPLICATE DUE FIXTURE: {match_id}"
            )
        if lane not in ALLOWED_LANES:
            raise Step2ReconciliationError(
                f"invalid official_follow_lane={lane!r}"
            )
        if auth not in ALLOWED_AUTH:
            raise Step2ReconciliationError(
                f"invalid step2_authorization={auth!r}"
            )
        if auth == "ROUTINE_FOLLOW" and lane != "FOLLOW":
            raise Step2ReconciliationError(
                f"STEP2 RECONCILIATION FAILED — ROUTINE_FOLLOW REQUIRES FOLLOW: {match_id}"
            )
        if auth == "RESERVE_ACTIVATED" and lane != "RESERVE":
            raise Step2ReconciliationError(
                f"STEP2 RECONCILIATION FAILED — RESERVE_ACTIVATED REQUIRES RESERVE: {match_id}"
            )
        if lane == "STOP" and auth != "USER_EXCEPTION":
            raise Step2ReconciliationError(
                f"STEP2 RECONCILIATION FAILED — STOP REQUIRES USER_EXCEPTION: {match_id}"
            )

        due_by_id[match_id] = {
            "official_follow_lane": lane,
            "step2_authorization": auth,
        }

    outcome_by_id: dict[str, str] = {}
    for row in outcomes:
        if not isinstance(row, dict):
            raise Step2ReconciliationError("outcome entries must be objects")
        match_id = _text(row, "match_id")
        status = _text(row, "status").upper()

        if match_id in outcome_by_id:
            raise Step2ReconciliationError(
                f"STEP2 RECONCILIATION FAILED — DUPLICATE OUTCOME: {match_id}"
            )
        if status not in ALLOWED_OUTCOMES:
            allowed = ", ".join(sorted(ALLOWED_OUTCOMES))
            raise Step2ReconciliationError(
                f"invalid status={status!r}; allowed: {allowed}"
            )
        outcome_by_id[match_id] = status

    due_ids = set(due_by_id)
    outcome_ids = set(outcome_by_id)

    missing = sorted(due_ids - outcome_ids)
    extras = sorted(outcome_ids - due_ids)
    if missing:
        raise Step2ReconciliationError(
            "STEP2 RECONCILIATION FAILED — SILENT OMISSION: "
            + ", ".join(missing)
        )
    if extras:
        raise Step2ReconciliationError(
            "STEP2 RECONCILIATION FAILED — OUTCOME WITHOUT AUTHORIZATION: "
            + ", ".join(extras)
        )

    persisted = sum(
        status == "DECISION_STATE_PERSISTED"
        for status in outcome_by_id.values()
    )
    pending = len(outcome_by_id) - persisted

    return {
        "schema_version": SCHEMA_VERSION,
        "stage": "step2_reconcile_result",
        "session_id": session_id,
        "all_due_accounted": True,
        "due_count": len(due_by_id),
        "persisted_decision_count": persisted,
        "nondecision_disposition_count": pending,
        "outcomes": [
            {"match_id": match_id, "status": outcome_by_id[match_id]}
            for match_id in sorted(outcome_by_id)
        ],
    }


def dumps(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)
