from __future__ import annotations

from typing import Any


MAX_FOLLOW = 6
MAX_RESERVE = 4
MAX_ACTIVE = MAX_FOLLOW + MAX_RESERVE

VALID_GRADES = {"A", "B"}
VALID_STATUSES = {
    "PREMATCH_CONFIRMED",
    "STARTED",
    "POSTPONED",
    "CANCELLED",
    "FINISHED",
}
DEFERRED = "OPERATIONAL_CAPACITY_DEFERRED"


class CapacityReplenishmentError(ValueError):
    pass


def _positive_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise CapacityReplenishmentError(f"{field} must be a positive integer")
    return value


def _count(value: Any, field: str, maximum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CapacityReplenishmentError(f"{field} must be a non-negative integer")
    if value > maximum:
        raise CapacityReplenishmentError(
            f"{field} exceeds operational cap {maximum}: {value}"
        )
    return value


def validate_capacity_queue(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not isinstance(candidates, list):
        raise CapacityReplenishmentError("candidates must be an array")

    seen_rank: set[int] = set()
    seen_match: set[str] = set()
    normalized: list[dict[str, Any]] = []

    for index, row in enumerate(candidates):
        if not isinstance(row, dict):
            raise CapacityReplenishmentError(f"candidates[{index}] must be an object")

        match_id = row.get("match_id")
        if not isinstance(match_id, str) or not match_id.strip():
            raise CapacityReplenishmentError(
                f"candidates[{index}].match_id must be non-empty"
            )
        match_id = match_id.strip()
        if match_id in seen_match:
            raise CapacityReplenishmentError(
                f"duplicate match_id in capacity queue: {match_id}"
            )
        seen_match.add(match_id)

        queue_rank = _positive_int(
            row.get("queue_rank"), f"candidates[{index}].queue_rank"
        )
        if queue_rank in seen_rank:
            raise CapacityReplenishmentError(
                f"duplicate Step0 Capacity Queue Rank: {queue_rank}"
            )
        seen_rank.add(queue_rank)

        grade = row.get("operational_grade")
        if grade not in VALID_GRADES:
            raise CapacityReplenishmentError(
                f"capacity queue accepts A/B only: match_id={match_id} grade={grade!r}"
            )

        status = row.get("fixture_status")
        if status not in VALID_STATUSES:
            raise CapacityReplenishmentError(
                f"invalid fixture_status for {match_id}: {status!r}"
            )

        disposition = row.get("disposition")
        if not isinstance(disposition, str) or not disposition:
            raise CapacityReplenishmentError(
                f"candidates[{index}].disposition must be non-empty"
            )

        normalized.append(
            {
                "match_id": match_id,
                "queue_rank": queue_rank,
                "operational_grade": grade,
                "fixture_status": status,
                "disposition": disposition,
            }
        )

    normalized.sort(key=lambda row: row["queue_rank"])
    return normalized


def next_replenishment_wave(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise CapacityReplenishmentError("payload must be an object")

    follow_count = _count(payload.get("follow_count"), "follow_count", MAX_FOLLOW)
    reserve_count = _count(
        payload.get("reserve_count"), "reserve_count", MAX_RESERVE
    )
    active_lane_count = follow_count + reserve_count
    if active_lane_count > MAX_ACTIVE:
        raise CapacityReplenishmentError(
            f"active lane count exceeds {MAX_ACTIVE}: {active_lane_count}"
        )

    queue = validate_capacity_queue(payload.get("candidates"))
    vacancies = MAX_ACTIVE - active_lane_count

    eligible = [
        row
        for row in queue
        if row["disposition"] == DEFERRED
        and row["fixture_status"] == "PREMATCH_CONFIRMED"
    ]
    closed = [
        row
        for row in queue
        if row["disposition"] == DEFERRED
        and row["fixture_status"] != "PREMATCH_CONFIRMED"
    ]

    selected = eligible[:vacancies] if vacancies > 0 else []

    if vacancies == 0:
        status = "ACTIVE_LANE_CAPACITY_FULL"
    elif selected:
        status = "REPLENISHMENT_REQUIRED"
    else:
        status = "QUEUE_EXHAUSTED_OR_CLOSED"

    return {
        "status": status,
        "follow_count": follow_count,
        "reserve_count": reserve_count,
        "active_lane_count": active_lane_count,
        "vacancies": vacancies,
        "selected_match_ids": [row["match_id"] for row in selected],
        "selected_queue_ranks": [row["queue_rank"] for row in selected],
        "remaining_prematch_deferred_count": max(0, len(eligible) - len(selected)),
        "closed_deferred": [
            {
                "match_id": row["match_id"],
                "queue_rank": row["queue_rank"],
                "fixture_status": row["fixture_status"],
                "reason": "REPLENISHMENT SKIPPED — PREMATCH WINDOW CLOSED",
            }
            for row in closed
        ],
    }
