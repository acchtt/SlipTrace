from __future__ import annotations

from typing import Any


MAX_FOLLOW = 6
MAX_RESERVE = 4
MAX_ACTIVE = MAX_FOLLOW + MAX_RESERVE
COMPACT_POLICY = "COMPACT_GOAL_ROUTE_V1"
COMPACT_INITIAL_WAVE = 8
COMPACT_TOTAL_RESEARCH = 12
COMPACT_REFILL_ACTIVE_TARGET = 4

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
    policy = payload.get("budget_policy")
    if policy is not None and policy != COMPACT_POLICY:
        raise CapacityReplenishmentError(f"unknown budget_policy: {policy!r}")

    # Existing frozen handoffs omit budget_policy and retain the exact legacy
    # replenishment behavior. Compact works only on explicitly versioned runs.
    researched: set[str] = set()
    research_budget_remaining = None
    if policy == COMPACT_POLICY:
        ids = payload.get("researched_match_ids")
        if not isinstance(ids, list) or any(
            not isinstance(value, str) or not value.strip() for value in ids
        ):
            raise CapacityReplenishmentError(
                "compact researched_match_ids must be a list of nonblank IDs"
            )
        if len(ids) != len(set(ids)):
            raise CapacityReplenishmentError(
                "duplicate researched_match_ids in compact budget"
            )
        researched = set(ids)
        candidate_ids = {row["match_id"] for row in queue}
        unknown = researched - candidate_ids
        if unknown:
            raise CapacityReplenishmentError(
                f"researched_match_ids missing from frozen queue: {sorted(unknown)}"
            )
        if len(researched) > COMPACT_TOTAL_RESEARCH:
            raise CapacityReplenishmentError(
                f"compact research ceiling exceeded: {len(researched)} > {COMPACT_TOTAL_RESEARCH}"
            )
        research_budget_remaining = COMPACT_TOTAL_RESEARCH - len(researched)
        vacancies = min(
            max(0, COMPACT_REFILL_ACTIVE_TARGET - active_lane_count),
            research_budget_remaining,
        )
    else:
        vacancies = MAX_ACTIVE - active_lane_count

    eligible = [
        row
        for row in queue
        if row["disposition"] == DEFERRED
        and row["fixture_status"] == "PREMATCH_CONFIRMED"
        and row["match_id"] not in researched
    ]
    closed = [
        row
        for row in queue
        if row["disposition"] == DEFERRED
        and row["fixture_status"] != "PREMATCH_CONFIRMED"
    ]

    selected = eligible[:vacancies] if vacancies > 0 else []

    if policy == COMPACT_POLICY and research_budget_remaining == 0:
        status = "COMPACT_RESEARCH_BUDGET_EXHAUSTED"
    elif policy == COMPACT_POLICY and active_lane_count >= COMPACT_REFILL_ACTIVE_TARGET:
        status = "COMPACT_ACTIVE_TARGET_SATISFIED"
    elif vacancies == 0:
        status = "ACTIVE_LANE_CAPACITY_FULL"
    elif selected:
        status = "REPLENISHMENT_REQUIRED"
    else:
        status = "QUEUE_EXHAUSTED_OR_CLOSED"

    return {
        "status": status,
        "budget_policy": policy or "LEGACY",
        "follow_count": follow_count,
        "reserve_count": reserve_count,
        "active_lane_count": active_lane_count,
        "vacancies": vacancies,
        "research_budget_remaining": research_budget_remaining,
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


def select_initial_work_wave(
    candidates: list[dict[str, Any]], *, budget_policy: str | None = None
) -> dict[str, Any]:
    """Freeze the first Work wave without changing operational queue order."""
    if budget_policy is not None and budget_policy != COMPACT_POLICY:
        raise CapacityReplenishmentError(f"unknown budget_policy: {budget_policy!r}")
    queue = validate_capacity_queue(candidates)
    ranks = [item["queue_rank"] for item in queue]
    if ranks != list(range(1, len(queue) + 1)):
        raise CapacityReplenishmentError(
            "initial Work queue ranks must be contiguous beginning at 1"
        )
    limit = COMPACT_INITIAL_WAVE if budget_policy == COMPACT_POLICY else 15
    admitted = queue[:limit]
    deferred = queue[limit:]
    return {
        "budget_policy": budget_policy or "LEGACY",
        "initial_wave_limit": limit,
        "admitted_match_ids": [item["match_id"] for item in admitted],
        "admitted_queue_ranks": [item["queue_rank"] for item in admitted],
        "deferred_match_ids": [item["match_id"] for item in deferred],
        "deferred_queue_ranks": [item["queue_rank"] for item in deferred],
        "full_queue_count": len(queue),
    }
