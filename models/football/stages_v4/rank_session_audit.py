"""Prospective full-slate deadline and rerank diagnostics.

Read-only operational telemetry.  Never promotes/demotes Football C selections,
invents a pre-kickoff assessment, or treats closed research as completed research.
All diagnostics stay attached to one sealed source cohort.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any


def _time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _previous_assessments(previous: dict[str, Any] | None) -> dict[str, str]:
    if not isinstance(previous, dict):
        return {}
    recorded = previous.get("prematch_opportunity_manifest")
    if isinstance(recorded, list):
        return {
            r["match_id"]: r["first_C_assessed_at_utc"]
            for r in recorded
            if isinstance(r, dict)
            and isinstance(r.get("match_id"), str)
            and isinstance(r.get("first_C_assessed_at_utc"), str)
        }
    # Legacy compatibility: an earlier rank's frozen input *proves* only that
    # its assessment existed by that rank epoch. Never backdate to sweep time.
    stamp = previous.get("rank_at_utc")
    rows = (previous.get("frozen_model_input") or {}).get("matches", [])
    if not isinstance(stamp, str) or not isinstance(rows, list):
        return {}
    return {
        row["match_id"]: stamp
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("match_id"), str)
    }


def prematch_opportunity(
    frozen: dict[str, dict[str, Any]],
    *,
    now: str,
    current_ids: set[str],
    previous_rank: dict[str, Any] | None,
) -> dict[str, Any]:
    """Count terminal closures without ever retrospectively funding a model."""
    at = _time(now)
    prev = _previous_assessments(previous_rank)
    manifest = []
    for mid, row in frozen.items():
        kickoff_str = row["kickoff_utc"]
        kickoff = _time(kickoff_str)
        first = prev.get(mid)
        if first is not None and _time(first) >= kickoff:
            first = None  # stale or later data cannot prove prematch completion
        if first is None and mid in current_ids and at < kickoff:
            first = now
        missed = at >= kickoff and first is None
        manifest.append({
            "match_id": mid,
            "kickoff_utc": kickoff_str,
            "first_C_assessed_at_utc": first,
            "ever_prematch_C_assessed": first is not None,
            "deadline_state": (
                "PREMATCH_RESEARCH_MISSED" if missed else
                "PREMATCH_C_ASSESSED" if first is not None else
                "PREMATCH_RESEARCH_OUTSTANDING"
            ),
        })
    manifest.sort(key=lambda item: (item["kickoff_utc"], item["match_id"]))
    return {
        "policy": "PREMATCH_COVERAGE_DEADLINES_V1",
        "full_queue_count": len(manifest),
        "ever_prematch_assessed_count": sum(x["ever_prematch_C_assessed"] for x in manifest),
        "never_assessed_before_kickoff_count": sum(
            x["deadline_state"] == "PREMATCH_RESEARCH_MISSED" for x in manifest
        ),
        "open_unassessed_count": sum(
            x["deadline_state"] == "PREMATCH_RESEARCH_OUTSTANDING" for x in manifest
        ),
        "manifest": manifest,
        "priority_open_match_ids": [
            x["match_id"] for x in manifest
            if x["deadline_state"] == "PREMATCH_RESEARCH_OUTSTANDING"
        ],
    }


def rank_transitions(
    current: list[dict[str, Any]],
    *,
    previous_rank: dict[str, Any] | None,
    coverage_manifest: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Preserve earlier FOLLOW membership, including now-started fixtures."""
    old_rows = []
    if isinstance(previous_rank, dict):
        old_rows = (previous_rank.get("research_assessment") or {}).get("matches") or []
    prior = {
        r["match_id"]: r for r in old_rows
        if isinstance(r, dict) and isinstance(r.get("match_id"), str)
    }
    new = {
        r["match_id"]: r for r in current
        if isinstance(r, dict) and isinstance(r.get("match_id"), str)
    }
    disposition = {
        r["match_id"]: r.get("disposition")
        for r in coverage_manifest
        if isinstance(r, dict) and isinstance(r.get("match_id"), str)
    }
    changes = []
    for mid in sorted(set(prior) | set(new)):
        old, new_row = prior.get(mid), new.get(mid)
        old_lane = old.get("follow_lane") if old else None
        new_lane = new_row.get("follow_lane") if new_row else None
        old_cert = old.get("supported_line") if old else None
        new_cert = new_row.get("supported_line") if new_row else None
        if old is None:
            status = "NEW"
        elif new_row is None:
            status = "CLOSED" if disposition.get(mid) == "STATUS_EXCLUDED" else "DROPPED"
        elif old_lane == new_lane and old_cert == new_cert:
            status = "UNCHANGED"
        elif old_lane == "FOLLOW" and new_lane != "FOLLOW":
            status = "DEMOTED"
        elif old_lane != "FOLLOW" and new_lane == "FOLLOW":
            status = "PROMOTED"
        else:
            status = "CHANGED"
        changes.append({
            "match_id": mid,
            "transition": status,
            "previous_lane": old_lane,
            "current_lane": new_lane,
            "previous_supported_line": old_cert,
            "current_supported_line": new_cert,
            "previous_rank": old.get("rank") if old else None,
            "current_rank": new_row.get("rank") if new_row else None,
            "prior_follow_history_preserved": old_lane == "FOLLOW",
            "reason": (
                "KICKOFF_OR_STATUS_CLOSED_PRIOR_DECISION_RETAINED" if status == "CLOSED"
                else "UPDATED_FROZEN_FOOTBALL_OR_PORTFOLIO_CAPACITY" if status in
                {"DEMOTED", "PROMOTED", "CHANGED"}
                else "NEW_PREMATCH_C_EVIDENCE" if status == "NEW"
                else "NO_CHANGE"
            ),
        })
    return changes
