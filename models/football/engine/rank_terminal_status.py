from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class RankTerminalStatusError(ValueError):
    pass


@dataclass(frozen=True)
class RankTerminalStatus:
    code: str
    label: str
    blocked: bool
    complete: bool
    replenishment_required: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "label": self.label,
            "blocked": self.blocked,
            "complete": self.complete,
            "replenishment_required": self.replenishment_required,
        }


def _count(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise RankTerminalStatusError(f"{field} must be a non-negative integer")
    return value


def rank_terminal_status(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise RankTerminalStatusError("payload must be an object")

    ranked = _count(payload.get("ranked_eligible_count"), "ranked_eligible_count")
    holds = _count(payload.get("quarantine_count"), "quarantine_count")
    follow = _count(payload.get("follow_count"), "follow_count")
    reserve = _count(payload.get("reserve_count"), "reserve_count")
    stop = _count(payload.get("stop_count"), "stop_count")
    deferred = _count(
        payload.get("remaining_prematch_deferred_count"),
        "remaining_prematch_deferred_count",
    )
    integrity_failure = payload.get("board_integrity_failure")
    if not isinstance(integrity_failure, bool):
        raise RankTerminalStatusError("board_integrity_failure must be boolean")

    reason = payload.get("integrity_failure_reason")
    if integrity_failure and (not isinstance(reason, str) or not reason.strip()):
        raise RankTerminalStatusError(
            "integrity_failure_reason required when board_integrity_failure=true"
        )

    if follow + reserve + stop != ranked:
        raise RankTerminalStatusError(
            "ranked_eligible_count must equal FOLLOW + RESERVE + STOP"
        )

    if integrity_failure:
        status = RankTerminalStatus(
            code="BLOCKED_INTEGRITY",
            label=f"/rank blocked — {reason.strip()}",
            blocked=True,
            complete=False,
            replenishment_required=False,
        )
    elif follow + reserve < 10 and deferred > 0:
        status = RankTerminalStatus(
            code="REPLENISHMENT_REQUIRED",
            label="/rank continues — replenishment required",
            blocked=False,
            complete=False,
            replenishment_required=True,
        )
    elif ranked == 0:
        status = RankTerminalStatus(
            code="COMPLETE_EMPTY_RANKED_UNIVERSE",
            label="/rank complete — no ranked eligible fixtures",
            blocked=False,
            complete=True,
            replenishment_required=False,
        )
    elif follow == 0:
        status = RankTerminalStatus(
            code="COMPLETE_ZERO_FOLLOW",
            label="/rank complete — 0 FOLLOW",
            blocked=False,
            complete=True,
            replenishment_required=False,
        )
    else:
        status = RankTerminalStatus(
            code="COMPLETE_WITH_FOLLOW",
            label="/rank complete",
            blocked=False,
            complete=True,
            replenishment_required=False,
        )

    out = status.to_dict()
    out.update(
        {
            "ranked_eligible_count": ranked,
            "quarantine_count": holds,
            "follow_count": follow,
            "reserve_count": reserve,
            "stop_count": stop,
            "remaining_prematch_deferred_count": deferred,
        }
    )
    return out
