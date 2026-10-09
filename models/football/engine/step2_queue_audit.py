#!/usr/bin/env python3
"""Compare frozen Step-2 authorization with actual v2 outcome reconciliation.

This reconciles process records only. It does not infer decisions from
fixture names, change model verdicts or touch betting/Airtable records.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from step2_reconcile import reconcile_step2, Step2ReconciliationError
from step2_queue_guard import VERSION as QUEUE_VERSION, Step2QueueError

OPEN_DISPOSITIONS = {
    "WAITING_FOR_USER_XI_ODDS": "RECHECK_XI_AND_EXECUTABLE_QUOTE",
    "FIXTURE_STATUS_BLOCKED": "VERIFY_FIXTURE_STATUS_AND_CLOSE_OR_REROUTE",
    "INTEGRITY_BLOCKED": "RESOLVE_MATERIAL_EVIDENCE_OR_CLOSE_NO_BET",
    "ENGINE_FAILED_AFTER_ATTEMPT": "RETRY_TECHNICAL_EXECUTION_FROM_FROZEN_EPOCH_IF_STILL_LAWFUL",
    "LIVE_REROUTED": "VERIFY_LIVE_HANDOFF_AND_LIVE_DECISION_STATUS",
}


class Step2QueueAuditError(ValueError):
    pass


def _entries(rows: object, *, label: str) -> dict[str, dict]:
    if not isinstance(rows, list):
        raise Step2QueueAuditError(f"{label} must be an array")
    indexed: dict[str, dict] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise Step2QueueAuditError(f"{label} entry must be an object")
        key = row.get("match_id")
        if not isinstance(key, str) or not key.strip():
            raise Step2QueueAuditError(f"{label} match_id must be non-empty")
        if key in indexed:
            raise Step2QueueAuditError(f"DUPLICATE {label}: {key}")
        indexed[key] = row
    return indexed


def audit_queue_outcomes(payload: dict) -> dict:
    if not isinstance(payload, dict) or payload.get("schema_version") != "football-step2-queue-audit-v1":
        raise Step2QueueAuditError("schema_version must be football-step2-queue-audit-v1")
    queue = payload.get("queue_receipt")
    reconciliation = payload.get("reconciliation_input")
    if not isinstance(queue, dict) or not isinstance(reconciliation, dict):
        raise Step2QueueAuditError("queue_receipt and reconciliation_input must be objects")
    if queue.get("schema_version") != QUEUE_VERSION:
        raise Step2QueueAuditError("queue receipt must come from football-step2-queue-v1")
    if queue.get("mode") not in {"ROUTINE", "EXCEPTION_ONLY"}:
        raise Step2QueueAuditError("invalid queue receipt mode")
    if queue.get("mode") == "ROUTINE" and not queue.get("board_snapshot_id"):
        raise Step2QueueAuditError("ROUTINE queue missing frozen board snapshot")
    if reconciliation.get("schema_version") != "football-step2-reconcile-v2":
        raise Step2QueueAuditError("current queue audit requires v2 reconciliation, not historical replay")
    if queue.get("session_id") != reconciliation.get("session_id"):
        raise Step2QueueAuditError("SESSION ID MISMATCH between frozen queue and reconciliation")

    frozen = _entries(queue.get("due"), label="FROZEN DUE")
    provided = _entries(reconciliation.get("due"), label="RECONCILIATION DUE")
    outcome = _entries(reconciliation.get("outcomes"), label="OUTCOME")
    if queue.get("due_count") != len(frozen):
        raise Step2QueueAuditError("FROZEN DUE COUNT MISMATCH")
    missing_due = sorted(frozen.keys() - provided.keys())
    extra_due = sorted(provided.keys() - frozen.keys())
    if missing_due:
        raise Step2QueueAuditError("DUE FIXTURE DROPPED FROM RECONCILIATION: " + ", ".join(missing_due))
    if extra_due:
        raise Step2QueueAuditError("UNAUTHORIZED DUE FIXTURE ADDED: " + ", ".join(extra_due))
    for match_id, entry in frozen.items():
        other = provided[match_id]
        for field in ("official_follow_lane", "step2_authorization"):
            if entry.get(field) != other.get(field):
                raise Step2QueueAuditError(f"FROZEN AUTHORITY DRIFT: {match_id} ({field})")
        if not isinstance(entry.get("authorization_reference"), str) or not entry["authorization_reference"].strip():
            raise Step2QueueAuditError(f"MISSING AUTHORIZATION REFERENCE: {match_id}")
    if set(outcome) != set(frozen):
        missing = sorted(frozen.keys() - outcome.keys())
        extra = sorted(outcome.keys() - frozen.keys())
        raise Step2QueueAuditError(
            "STEP2 OUTCOME COVERAGE MISMATCH — missing="
            + ",".join(missing) + " extra=" + ",".join(extra)
        )

    try:
        result = reconcile_step2(reconciliation)
    except Step2ReconciliationError as exc:
        raise Step2QueueAuditError(f"STEP2 RECONCILIATION REJECTED: {exc}") from exc

    pending = []
    completed = []
    for match_id, entry in sorted(outcome.items()):
        disposition = entry.get("status", "").upper()
        if disposition == "DECISION_STATE_PERSISTED":
            completed.append(match_id)
        else:
            if disposition not in OPEN_DISPOSITIONS:
                raise Step2QueueAuditError(f"UNKNOWN OUTCOME DISPOSITION: {match_id}")
            pending.append({
                "match_id": match_id,
                "status": disposition,
                "follow_up": OPEN_DISPOSITIONS[disposition],
                "reason": entry.get("blocker_reason") or entry.get("engine_failure_reason") or entry.get("live_handoff_reference"),
            })

    if result["verified_decision_count"] != len(completed):
        raise Step2QueueAuditError("VERIFIED DECISION COUNT DOES NOT MATCH COMPLETED CASES")
    return {
        "schema_version": "football-step2-queue-audit-v1",
        "session_id": queue["session_id"],
        "source_run_id": queue.get("source_run_id"),
        "board_snapshot_id": queue.get("board_snapshot_id"),
        "all_due_accounted": result["all_due_accounted"],
        "all_due_completed": not pending,
        "status": "STEP2 SESSION COMPLETE" if not pending else "STEP2 ACCOUNTED WITH OPEN FOLLOW_UPS",
        "due_count": len(frozen),
        "verified_decision_count": len(completed),
        "open_follow_up_count": len(pending),
        "open_follow_ups": pending,
        "verified_decision_match_ids": completed,
        "decision_state_attestations": result.get("decision_state_attestations", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Step-2 frozen due set against v2 outcomes")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        result = audit_queue_outcomes(json.loads(Path(args.input).read_text(encoding="utf-8")))
        print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "status": "STEP2 QUEUE AUDIT FAILED", "reason": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
