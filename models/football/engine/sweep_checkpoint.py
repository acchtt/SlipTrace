from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any


CHECKPOINT_VERSION = "football-sweep-checkpoint-v1"
MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK = 6
SOURCE_RECOVERY_COOLDOWN_MINUTES = 30
RUN_STATUS_BY_SOURCE_STATE = {
    "UNTRIED": "RUNNING",
    "ACQUIRED": "RUNNING",
    "SOURCE_BLOCKED": "BLOCKED",
}
PHASES = (
    "SOURCE_ACQUISITION",
    "DISCOVERY_CLASSIFICATION",
    "TARGETED_VERIFICATION",
    "RECONCILIATION",
    "PACKAGING",
    "COMPLETE",
)


class SweepCheckpointError(ValueError):
    pass


@dataclass(frozen=True)
class VerificationChunk:
    run_id: str
    chunk_number: int
    selected_blocks: tuple[str, ...]
    remaining_blocks: tuple[str, ...]
    retry_queue: tuple[str, ...]
    next_phase: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "checkpoint_version": CHECKPOINT_VERSION,
            "run_id": self.run_id,
            "chunk_number": self.chunk_number,
            "selected_verification_blocks": list(self.selected_blocks),
            "remaining_verification_blocks": list(self.remaining_blocks),
            "retry_queue": list(self.retry_queue),
            "pending_verification_blocks": len(self.remaining_blocks),
            "next_phase": self.next_phase,
        }


def run_status_for_source_state(source_state: str) -> str:
    state = _nonempty(source_state, "source_state")
    try:
        return RUN_STATUS_BY_SOURCE_STATE[state]
    except KeyError as exc:
        raise SweepCheckpointError(
            "source_state must be UNTRIED/ACQUIRED/SOURCE_BLOCKED"
        ) from exc


def _nonempty(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SweepCheckpointError(f"{field} must be a non-empty string")
    return value.strip()


def _string_list(value: Any, field: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SweepCheckpointError(f"{field} must be an array")
    out: list[str] = []
    seen: set[str] = set()
    for item in value:
        item = _nonempty(item, field)
        if item in seen:
            raise SweepCheckpointError(f"{field} contains duplicate block {item!r}")
        seen.add(item)
        out.append(item)
    return out


def validate_checkpoint(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise SweepCheckpointError("checkpoint payload must be an object")

    version = payload.get("checkpoint_version")
    if version != CHECKPOINT_VERSION:
        raise SweepCheckpointError(
            f"checkpoint_version must be {CHECKPOINT_VERSION!r}"
        )

    run_id = _nonempty(payload.get("run_id"), "run_id")
    phase = _nonempty(payload.get("phase"), "phase")
    if phase not in PHASES:
        raise SweepCheckpointError(f"phase must be one of {PHASES}")

    chunk_number = payload.get("chunk_number")
    if isinstance(chunk_number, bool) or not isinstance(chunk_number, int) or chunk_number < 1:
        raise SweepCheckpointError("chunk_number must be a positive integer")

    source_state = _nonempty(
        payload.get("source_acquisition_state"), "source_acquisition_state"
    )
    if source_state not in {"UNTRIED", "ACQUIRED", "SOURCE_BLOCKED"}:
        raise SweepCheckpointError(
            "source_acquisition_state must be UNTRIED/ACQUIRED/SOURCE_BLOCKED"
        )

    pending = _string_list(
        payload.get("pending_verification_blocks"), "pending_verification_blocks"
    )
    retry = _string_list(payload.get("retry_queue"), "retry_queue")
    completed = _string_list(
        payload.get("completed_verification_blocks"), "completed_verification_blocks"
    )

    overlap = (set(pending) | set(retry)) & set(completed)
    if overlap:
        raise SweepCheckpointError(
            f"completed blocks cannot remain pending/retry: {sorted(overlap)}"
        )

    source_hash = payload.get("source_payload_hash")
    if source_state == "ACQUIRED" and (
        not isinstance(source_hash, str) or not source_hash.strip()
    ):
        raise SweepCheckpointError(
            "ACQUIRED checkpoint requires non-empty source_payload_hash"
        )

    if phase in {"TARGETED_VERIFICATION", "RECONCILIATION", "PACKAGING", "COMPLETE"}:
        if source_state != "ACQUIRED":
            raise SweepCheckpointError(
                f"phase {phase} requires source_acquisition_state=ACQUIRED"
            )

    source_blocker_fingerprint = payload.get("source_blocker_fingerprint")
    if source_blocker_fingerprint is not None and (
        not isinstance(source_blocker_fingerprint, str)
        or not source_blocker_fingerprint.strip()
    ):
        raise SweepCheckpointError(
            "source_blocker_fingerprint must be null or a non-empty string"
        )

    source_last_attempt_at = payload.get("source_last_attempt_at")
    if source_last_attempt_at is not None:
        _parse_iso_datetime(source_last_attempt_at, "source_last_attempt_at")

    source_retry_not_before = payload.get("source_retry_not_before")
    if source_retry_not_before is not None:
        _parse_iso_datetime(source_retry_not_before, "source_retry_not_before")

    source_recovery_attempt_count = payload.get("source_recovery_attempt_count", 0)
    if (
        isinstance(source_recovery_attempt_count, bool)
        or not isinstance(source_recovery_attempt_count, int)
        or source_recovery_attempt_count < 0
    ):
        raise SweepCheckpointError(
            "source_recovery_attempt_count must be a non-negative integer"
        )

    return {
        "checkpoint_version": CHECKPOINT_VERSION,
        "run_id": run_id,
        "phase": phase,
        "chunk_number": chunk_number,
        "source_acquisition_state": source_state,
        "source_payload_hash": source_hash.strip() if isinstance(source_hash, str) else None,
        "source_blocker_fingerprint": (
            source_blocker_fingerprint.strip()
            if isinstance(source_blocker_fingerprint, str)
            else None
        ),
        "source_last_attempt_at": source_last_attempt_at,
        "source_retry_not_before": source_retry_not_before,
        "source_recovery_attempt_count": source_recovery_attempt_count,
        "pending_verification_blocks": pending,
        "retry_queue": retry,
        "completed_verification_blocks": completed,
        "last_completed_block": payload.get("last_completed_block"),
    }



def _parse_iso_datetime(value: Any, field: str) -> datetime:
    raw = _nonempty(value, field)
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SweepCheckpointError(
            f"{field} must be an ISO-8601 timestamp with timezone"
        ) from exc
    if parsed.tzinfo is None:
        raise SweepCheckpointError(
            f"{field} must include a timezone offset"
        )
    return parsed


def _source_acquisition_checkpoint_view(payload: dict[str, Any], *, require_blocked: bool) -> dict[str, Any]:
    """Read source-acquisition cursors, including pre-lease legacy shapes."""
    if not isinstance(payload, dict):
        raise SweepCheckpointError("checkpoint payload must be an object")
    if payload.get("checkpoint_version") != CHECKPOINT_VERSION:
        raise SweepCheckpointError(
            f"checkpoint_version must be {CHECKPOINT_VERSION!r}"
        )
    run_id = _nonempty(payload.get("run_id"), "run_id")
    phase = _nonempty(payload.get("phase"), "phase")
    if phase != "SOURCE_ACQUISITION":
        raise SweepCheckpointError(
            "source retry decision requires phase=SOURCE_ACQUISITION"
        )
    source_state = _nonempty(
        payload.get("source_acquisition_state"), "source_acquisition_state"
    )
    if source_state not in {"UNTRIED", "SOURCE_BLOCKED"}:
        raise SweepCheckpointError(
            "source acquisition cursor must be UNTRIED or SOURCE_BLOCKED"
        )
    if require_blocked and source_state != "SOURCE_BLOCKED":
        raise SweepCheckpointError(
            "source retry decision requires source_acquisition_state=SOURCE_BLOCKED"
        )

    chunk_number = payload.get("chunk_number", 1)
    if (
        isinstance(chunk_number, bool)
        or not isinstance(chunk_number, int)
        or chunk_number < 1
    ):
        raise SweepCheckpointError("chunk_number must be a positive integer")

    source_blocker_fingerprint = payload.get("source_blocker_fingerprint")
    if source_blocker_fingerprint is not None and (
        not isinstance(source_blocker_fingerprint, str)
        or not source_blocker_fingerprint.strip()
    ):
        raise SweepCheckpointError(
            "source_blocker_fingerprint must be null or a non-empty string"
        )

    last_attempt = payload.get("source_last_attempt_at")
    if last_attempt is not None:
        _parse_iso_datetime(last_attempt, "source_last_attempt_at")
    retry_not_before = payload.get("source_retry_not_before")
    if retry_not_before is not None:
        _parse_iso_datetime(retry_not_before, "source_retry_not_before")

    attempt_count = payload.get("source_recovery_attempt_count", 0)
    if (
        isinstance(attempt_count, bool)
        or not isinstance(attempt_count, int)
        or attempt_count < 0
    ):
        raise SweepCheckpointError(
            "source_recovery_attempt_count must be a non-negative integer"
        )

    return {
        "run_id": run_id,
        "chunk_number": chunk_number,
        "source_blocker_fingerprint": (
            source_blocker_fingerprint.strip()
            if isinstance(source_blocker_fingerprint, str)
            else None
        ),
        "source_last_attempt_at": last_attempt,
        "source_retry_not_before": retry_not_before,
        "source_recovery_attempt_count": attempt_count,
    }


def source_retry_decision(
    payload: dict[str, Any],
    *,
    now: str,
    current_blocker_fingerprint: str,
) -> dict[str, Any]:
    """Decide whether a SOURCE_BLOCKED run may perform one bounded recovery probe.

    The no-repeat rule is a short-lived lease, not a permanent latch. A changed
    blocker fingerprint always reopens acquisition. An unchanged fingerprint
    reopens after SOURCE_RECOVERY_COOLDOWN_MINUTES. Legacy blocked checkpoints
    without retry metadata are allowed one immediate recovery probe.
    """
    cp = _source_acquisition_checkpoint_view(payload, require_blocked=True)

    current_fp = _nonempty(
        current_blocker_fingerprint, "current_blocker_fingerprint"
    )
    now_dt = _parse_iso_datetime(now, "now")
    stored_fp = cp["source_blocker_fingerprint"]

    if not stored_fp:
        return {
            "should_retry": True,
            "reason": "LEGACY_BLOCKED_CHECKPOINT_NO_FINGERPRINT",
            "cooldown_minutes": SOURCE_RECOVERY_COOLDOWN_MINUTES,
        }

    if stored_fp != current_fp:
        return {
            "should_retry": True,
            "reason": "BLOCKER_FINGERPRINT_CHANGED",
            "cooldown_minutes": SOURCE_RECOVERY_COOLDOWN_MINUTES,
        }

    retry_not_before = cp["source_retry_not_before"]
    if not retry_not_before:
        return {
            "should_retry": True,
            "reason": "LEGACY_BLOCKED_CHECKPOINT_NO_RETRY_LEASE",
            "cooldown_minutes": SOURCE_RECOVERY_COOLDOWN_MINUTES,
        }

    retry_dt = _parse_iso_datetime(retry_not_before, "source_retry_not_before")
    if now_dt >= retry_dt:
        return {
            "should_retry": True,
            "reason": "SOURCE_RECOVERY_LEASE_EXPIRED",
            "cooldown_minutes": SOURCE_RECOVERY_COOLDOWN_MINUTES,
            "retry_not_before": retry_dt.isoformat(),
        }

    return {
        "should_retry": False,
        "reason": "SOURCE_RECOVERY_LEASE_ACTIVE",
        "cooldown_minutes": SOURCE_RECOVERY_COOLDOWN_MINUTES,
        "retry_not_before": retry_dt.isoformat(),
    }


def mark_source_blocked(
    payload: dict[str, Any],
    *,
    blocker_fingerprint: str,
    attempted_at: str,
) -> dict[str, Any]:
    """Persist a bounded retry lease after a failed source acquisition pass."""
    cp = _source_acquisition_checkpoint_view(payload, require_blocked=False)

    fp = _nonempty(blocker_fingerprint, "blocker_fingerprint")
    attempt_dt = _parse_iso_datetime(attempted_at, "attempted_at")
    retry_dt = attempt_dt + timedelta(minutes=SOURCE_RECOVERY_COOLDOWN_MINUTES)

    out = dict(payload)
    out.pop("blocker_fingerprint", None)
    out.update(
        {
            "checkpoint_version": CHECKPOINT_VERSION,
            "run_id": cp["run_id"],
            "phase": "SOURCE_ACQUISITION",
            "chunk_number": cp["chunk_number"],
            "source_acquisition_state": "SOURCE_BLOCKED",
            "source_payload_hash": None,
            "source_blocker_fingerprint": fp,
            "source_last_attempt_at": attempt_dt.isoformat(),
            "source_retry_not_before": retry_dt.isoformat(),
            "source_recovery_attempt_count": cp["source_recovery_attempt_count"] + 1,
        }
    )
    return out

def select_verification_chunk(payload: dict[str, Any]) -> VerificationChunk:
    cp = validate_checkpoint(payload)
    if cp["phase"] != "TARGETED_VERIFICATION":
        raise SweepCheckpointError(
            "chunk selection requires phase=TARGETED_VERIFICATION"
        )

    # Retries are attempted before untouched pending blocks on the next invocation.
    ordered: list[str] = []
    seen: set[str] = set()
    for block in cp["retry_queue"] + cp["pending_verification_blocks"]:
        if block not in seen:
            seen.add(block)
            ordered.append(block)

    selected = ordered[:MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK]
    remaining = ordered[MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK:]

    next_phase = "RECONCILIATION" if not remaining and not selected else "TARGETED_VERIFICATION"

    return VerificationChunk(
        run_id=cp["run_id"],
        chunk_number=cp["chunk_number"],
        selected_blocks=tuple(selected),
        remaining_blocks=tuple(remaining),
        retry_queue=tuple(cp["retry_queue"]),
        next_phase=next_phase,
    )


def advance_after_chunk(
    payload: dict[str, Any],
    *,
    completed_blocks: list[str],
    retry_blocks: list[str] | None = None,
) -> dict[str, Any]:
    cp = validate_checkpoint(payload)
    if cp["phase"] != "TARGETED_VERIFICATION":
        raise SweepCheckpointError(
            "advance requires phase=TARGETED_VERIFICATION"
        )

    completed = _string_list(completed_blocks, "completed_blocks")
    retries = _string_list(retry_blocks or [], "retry_blocks")

    current_order: list[str] = []
    seen: set[str] = set()
    for block in cp["retry_queue"] + cp["pending_verification_blocks"]:
        if block not in seen:
            seen.add(block)
            current_order.append(block)

    current_set = set(current_order)
    unknown_completed = set(completed) - current_set
    unknown_retry = set(retries) - current_set
    if unknown_completed:
        raise SweepCheckpointError(
            f"completed_blocks not in current queue: {sorted(unknown_completed)}"
        )
    if unknown_retry:
        raise SweepCheckpointError(
            f"retry_blocks not in current queue: {sorted(unknown_retry)}"
        )
    if set(completed) & set(retries):
        raise SweepCheckpointError(
            "same block cannot be completed and retried"
        )

    consumed = set(completed) | set(retries)
    untouched = [block for block in current_order if block not in consumed]
    next_order = retries + untouched

    completed_history = cp["completed_verification_blocks"] + completed
    next_phase = "RECONCILIATION" if not next_order else "TARGETED_VERIFICATION"

    return {
        "checkpoint_version": CHECKPOINT_VERSION,
        "run_id": cp["run_id"],
        "phase": next_phase,
        "chunk_number": cp["chunk_number"] + 1,
        "source_acquisition_state": cp["source_acquisition_state"],
        "source_payload_hash": cp["source_payload_hash"],
        "pending_verification_blocks": next_order,
        "retry_queue": retries,
        "completed_verification_blocks": completed_history,
        "last_completed_block": completed[-1] if completed else cp["last_completed_block"],
        "pending_verification_count": len(next_order),
    }
