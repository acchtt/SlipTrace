from __future__ import annotations

import json
import math
import re
from typing import Any


SCHEMA_VERSION = "football-step2-reconcile-v2"
LEGACY_SCHEMA_VERSION = "football-step2-reconcile-v1"
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
HEX_SHA = re.compile(r"^[0-9a-f]{40}$")
AIRTABLE_RECORD_ID = re.compile(r"^rec[A-Za-z0-9]{14}$")
C2_ACTION = re.compile(r"^C2-(BET|WAIT|PASS)(?:\s*[—-]\s*SHADOW)?$")


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


def _line(obj: dict[str, Any], key: str) -> float:
    value = _required(obj, key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise Step2ReconciliationError(f"{key} must be a numeric quarter line")
    line = float(value)
    if not math.isfinite(line) or line < 0 or abs(line * 4 - round(line * 4)) > 1e-8:
        raise Step2ReconciliationError(f"{key} must be a nonnegative quarter line")
    return line


def _engine_result(snapshot: dict[str, Any], key: str, action: str, line: float) -> None:
    raw = _required(snapshot, key)
    if isinstance(raw, str):
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise Step2ReconciliationError(f"{key} is not valid result JSON") from exc
    else:
        result = raw
    if not isinstance(result, dict):
        raise Step2ReconciliationError(f"{key} must be a result object")
    if result.get("action") != action:
        raise Step2ReconciliationError(f"{key}.action disagrees with persisted {action}")
    if _line(result, "supported_line") != line:
        raise Step2ReconciliationError(f"{key}.supported_line disagrees with persisted line")


def _check_persisted_decision(match_id: str, row: dict[str, Any]) -> dict[str, str]:
    """Validate an independent Decision State read-back, not merely an engine run."""
    snapshot = _required(row, "decision_state_snapshot")
    if not isinstance(snapshot, dict):
        raise Step2ReconciliationError(
            f"DECISION STATE ATTESTATION MISSING: {match_id} — snapshot must be an object"
        )
    if _text(snapshot, "match_id") != match_id:
        raise Step2ReconciliationError(f"DECISION STATE MATCH MISMATCH: {match_id}")
    record_id = _text(snapshot, "record_id")
    if not AIRTABLE_RECORD_ID.fullmatch(record_id):
        raise Step2ReconciliationError(f"DECISION STATE RECORD ID INVALID: {match_id}")
    if _text(snapshot, "engine_execution_status") != "EXECUTED_C_C2_PAIR":
        raise Step2ReconciliationError(
            f"DECISION STATE INCOMPLETE: {match_id} — C+C2 pair not executed"
        )
    revision = _text(snapshot, "engine_source_revision")
    if not HEX_SHA.fullmatch(revision):
        raise Step2ReconciliationError(
            f"DECISION STATE SOURCE REVISION INVALID: {match_id}"
        )

    c_action = _text(snapshot, "c_action").upper()
    if c_action not in {"C-BET", "C-WAIT", "C-PASS"}:
        raise Step2ReconciliationError(
            f"DECISION STATE INCOMPLETE: {match_id} — invalid official C action"
        )
    c2_action = _text(snapshot, "c2_shadow_action").upper()
    match = C2_ACTION.fullmatch(c2_action)
    if match is None:
        raise Step2ReconciliationError(
            f"DECISION STATE INCOMPLETE: {match_id} — invalid C2 shadow action"
        )
    c_line = _line(snapshot, "c_supported_line")
    c2_line = _line(snapshot, "c2_supported_line")
    _engine_result(snapshot, "engine_c_result", c_action[2:], c_line)
    _engine_result(snapshot, "engine_c2_result", match.group(1), c2_line)
    return {"record_id": record_id, "engine_source_revision": revision}


def reconcile_step2(payload: dict[str, Any]) -> dict[str, Any]:
    """Require exactly one traceable disposition per frozen due fixture.

    Legacy v1 is accepted only for explicit historical replay. New sessions must
    use v2 attestations from a real Decision State read-back.
    """
    if not isinstance(payload, dict):
        raise Step2ReconciliationError("payload must be an object")
    version = payload.get("schema_version")
    if version not in {SCHEMA_VERSION, LEGACY_SCHEMA_VERSION}:
        raise Step2ReconciliationError(f"schema_version must be {SCHEMA_VERSION!r}")
    if version == LEGACY_SCHEMA_VERSION and payload.get("historical_replay") is not True:
        raise Step2ReconciliationError(
            "legacy v1 reconciliation requires explicit historical_replay=true"
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
            raise Step2ReconciliationError(f"invalid official_follow_lane={lane!r}")
        if auth not in ALLOWED_AUTH:
            raise Step2ReconciliationError(f"invalid step2_authorization={auth!r}")
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
    attestations: dict[str, dict[str, str]] = {}
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
        if version == SCHEMA_VERSION:
            if status == "DECISION_STATE_PERSISTED":
                attestations[match_id] = _check_persisted_decision(match_id, row)
            elif status == "LIVE_REROUTED":
                _text(row, "live_handoff_reference")
            else:
                _text(row, "blocker_reason")
                if status == "ENGINE_FAILED_AFTER_ATTEMPT":
                    _text(row, "engine_failure_reason")
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
    persisted = sum(status == "DECISION_STATE_PERSISTED" for status in outcome_by_id.values())
    return {
        "schema_version": version,
        "stage": "step2_reconcile_result",
        "session_id": session_id,
        "all_due_accounted": True,
        "due_count": len(due_by_id),
        "persisted_decision_count": persisted,
        "verified_decision_count": len(attestations),
        "decision_state_attestations": [
            {"match_id": match_id, **attestations[match_id]}
            for match_id in sorted(attestations)
        ],
        "nondecision_disposition_count": len(outcome_by_id) - persisted,
        "outcomes": [
            {"match_id": match_id, "status": outcome_by_id[match_id]}
            for match_id in sorted(outcome_by_id)
        ],
    }


def dumps(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)
