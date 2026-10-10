"""Bounded, prospective football-first research scheduler for a frozen Step0 A/B queue.

Only allocates Step1 research time. It does not produce a goal forecast,
modify a frozen Step0 rank, execute C/C2, or authorize a bet.
"""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit
from typing import Any

SCREEN_SCHEMA = "football-goal-route-prescreen-v1"
MANIFEST_SCHEMA = "football-goal-first-research-manifest-v1"
MIN_RESULTS_PER_TEAM = 4
MAX_RESULTS_PER_TEAM = 10
MAX_SOURCE_AGE_HOURS = 168
MAX_MATCH_AGE_DAYS = 120
RESULT_FINISH_BUFFER_MINUTES = 120
EARLY_KICKOFF_PRIORITY_MINUTES = 90
INITIAL_DEEP_RESEARCH = 8


class GoalPrescreenError(ValueError):
    pass


def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise GoalPrescreenError(f"{field} needs timezone-aware ISO timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise GoalPrescreenError(f"{field} invalid ISO timestamp") from exc
    if result.utcoffset() is None:
        raise GoalPrescreenError(f"{field} missing timezone")
    return result.astimezone(timezone.utc)


def _url(value: Any, field: str) -> None:
    if not isinstance(value, str):
        raise GoalPrescreenError(f"{field} missing HTTPS URL")
    p = urlsplit(value)
    if p.scheme != "https" or not p.hostname or "." not in p.hostname or p.username or p.password:
        raise GoalPrescreenError(f"{field} needs public HTTPS source")


def _score_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 20:
        raise GoalPrescreenError(f"{field} must be actual integer goals 0..20")
    return value


def _team_evidence(data: Any, now: datetime, field: str) -> dict[str, float] | None:
    if data is None:
        return None
    if not isinstance(data, dict):
        raise GoalPrescreenError(f"{field} must be object or null")
    recent = data.get("recent")
    if recent is None:
        return None
    if not isinstance(recent, list):
        raise GoalPrescreenError(f"{field}.recent must be list")
    if len(recent) < MIN_RESULTS_PER_TEAM:
        return None
    if len(recent) > MAX_RESULTS_PER_TEAM:
        raise GoalPrescreenError(f"{field} excessive history; max 10")
    _url(data.get("source_url"), f"{field}.source_url")
    observed = _time(data.get("observed_at_utc"), f"{field}.observed_at_utc")
    if not now - timedelta(hours=MAX_SOURCE_AGE_HOURS) <= observed <= now:
        raise GoalPrescreenError(f"{field} source stale or from future")
    seen = set()
    goals_for, goals_against, over2, stalls = 0, 0, 0, 0
    for i, game in enumerate(recent):
        if not isinstance(game, dict):
            raise GoalPrescreenError(f"{field}.recent[{i}] must be object")
        ko = _time(game.get("kickoff_utc"), f"{field}.recent[{i}].kickoff_utc")
        if ko in seen:
            raise GoalPrescreenError(f"{field} duplicate historical match timestamp")
        seen.add(ko)
        if ko > now - timedelta(minutes=RESULT_FINISH_BUFFER_MINUTES):
            raise GoalPrescreenError(f"{field} result not provably finished before screen")
        if ko < now - timedelta(days=MAX_MATCH_AGE_DAYS):
            raise GoalPrescreenError(f"{field} result outside 120-day lookback")
        gf = _score_int(game.get("goals_for"), f"{field}.recent[{i}].goals_for")
        ga = _score_int(game.get("goals_against"), f"{field}.recent[{i}].goals_against")
        goals_for += gf
        goals_against += ga
        over2 += int(gf + ga >= 3)
        stalls += int(gf + ga <= 2)
    n = len(recent)
    return {"gf": goals_for / n, "ga": goals_against / n,
            "over2": over2 / n, "stall": stalls / n, "n": n}


def _fingerprint(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def _canonical_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(rows, key=lambda v: v["queue_rank"])


def _priority(row: dict[str, Any]) -> tuple:
    # A genuinely imminent kickoff is investigated before later kickoffs.
    # Only source-backed recent goals can alter football priority; no FT,
    # odds, bookmaker main line or subjective league Over rate enters.
    return (
        -int(row["urgent_before_kickoff"]),
        -int(row["screen_status"] == "QUANTIFIED"),
        -row["priority_score"] if row["priority_score"] is not None else 0,
        0 if row["operational_grade"] == "A" else 1,
        row["queue_rank"],
    )


def run_prescreen(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema_version") != SCREEN_SCHEMA:
        raise GoalPrescreenError("invalid prescreen schema_version")
    now = _time(payload.get("screen_at_utc"), "screen_at_utc")
    source_hash = payload.get("source_payload_hash")
    run_id = payload.get("run_id")
    if not isinstance(source_hash, str) or len(source_hash.strip()) < 8:
        raise GoalPrescreenError("source_payload_hash must bind original Step0 source")
    if not isinstance(run_id, str) or not run_id.strip():
        raise GoalPrescreenError("run_id missing")
    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise GoalPrescreenError("complete A/B candidates required")
    original, seen_ids, seen_ranks = [], set(), set()
    for i, c in enumerate(candidates):
        if not isinstance(c, dict):
            raise GoalPrescreenError(f"candidate {i} must be object")
        match_id, rank, grade, status = (
            c.get("match_id"), c.get("queue_rank"), c.get("operational_grade"),
            c.get("fixture_status"),
        )
        if not isinstance(match_id, str) or not match_id.strip() or match_id in seen_ids:
            raise GoalPrescreenError("blank/duplicate fixture ID")
        if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 0 or rank in seen_ranks:
            raise GoalPrescreenError("invalid or duplicate original queue rank")
        if grade not in ("A", "B"):
            raise GoalPrescreenError("prescreen takes original A/B queue only")
        if status not in ("PREMATCH_CONFIRMED", "STARTED", "FINISHED", "POSTPONED", "CANCELLED"):
            raise GoalPrescreenError("fixture status must be verified")
        forbidden = {"final_score", "live_score", "ft_goals", "outcome", "model_action",
                     "c_result", "c2_result", "bookmaker_total", "odds", "pnl"}
        if forbidden.intersection(c):
            raise GoalPrescreenError("postmatch, live, model and bookmaker fields forbidden in prescreen")
        ko = _time(c.get("kickoff_utc"), f"{match_id}.kickoff_utc")
        valid = status == "PREMATCH_CONFIRMED" and now < ko
        score, reason, h, a = None, None, None, None
        if valid:
            evidence = c.get("football_evidence")
            if evidence is None:
                reason = "HISTORICAL_TEAM_SOURCES_NOT_YET_AVAILABLE"
            elif not isinstance(evidence, dict):
                raise GoalPrescreenError("football_evidence must be object")
            else:
                h = _team_evidence(evidence.get("home"), now, f"{match_id}.home")
                a = _team_evidence(evidence.get("away"), now, f"{match_id}.away")
                if h is None or a is None:
                    reason = "FEWER_THAN_FOUR_VERIFIED_RECENT_RESULTS_PER_TEAM"
                else:
                    home_route = (h["gf"] + a["ga"]) / 2
                    away_route = (a["gf"] + h["ga"]) / 2
                    carrier = max(home_route, away_route)
                    second_route = min(home_route, away_route)
                    over2 = (h["over2"] + a["over2"]) / 2
                    stall = (h["stall"] + a["stall"]) / 2
                    # A scheduling heuristic, NOT an expected-goals estimate or
                    # a win probability. It cannot become an entry threshold.
                    score = max(0, min(100, round(
                        15 * carrier + 14 * second_route + 22 * over2 - 12 * stall
                    )))
        else:
            reason = "KICKOFF_CLOSED_OR_FIXTURE_NOT_PREMATCH"
        original.append({
            "match_id": match_id, "queue_rank": rank,
            "operational_grade": grade,
            "fixture_status_at_screen": status,
            "kickoff_utc": ko.isoformat(),
            "urgent_before_kickoff": valid and (ko - now).total_seconds() <= 60 * EARLY_KICKOFF_PRIORITY_MINUTES,
            "screen_status": "CLOSED" if not valid else ("EVIDENCE_LIMITED" if score is None else "QUANTIFIED"),
            "priority_score": score, "evidence_limit_reason": reason,
            "home_sample_n": h["n"] if h else 0,
            "away_sample_n": a["n"] if a else 0,
        })
        seen_ids.add(match_id)
        seen_ranks.add(rank)
    if seen_ranks != set(range(1, len(candidates) + 1)):
        raise GoalPrescreenError("full frozen Step0 A/B ranks must be contiguous, unmodified")
    original = _canonical_rows(original)
    eligible = sorted((r for r in original if r["screen_status"] != "CLOSED"), key=_priority)
    ordered = [r["match_id"] for r in eligible]
    manifest = {
        "schema_version": MANIFEST_SCHEMA,
        "run_id": run_id, "source_payload_hash": source_hash,
        "screen_at_utc": now.isoformat(),
        "original_rows": original,
        "ordered_eligible_match_ids": ordered,
    }
    manifest["screen_fingerprint"] = _fingerprint(manifest)
    first = eligible[:INITIAL_DEEP_RESEARCH]
    return {
        "schema_version": SCREEN_SCHEMA,
        "policy": "GOAL_FIRST_STEP1_RESEARCH_V1",
        "run_id": run_id, "original_step0_source_hash": source_hash,
        "full_ab_count": len(original), "quantified_count": sum(r["screen_status"] == "QUANTIFIED" for r in original),
        "evidence_limited_count": sum(r["screen_status"] == "EVIDENCE_LIMITED" for r in original),
        "closed_count": len(original) - len(eligible),
        "initial_research_match_ids": [r["match_id"] for r in first],
        "initial_original_step0_ranks": [r["queue_rank"] for r in first],
        "initial_promoted_from_step0_deferred": [r["match_id"] for r in first if r["queue_rank"] > 8],
        "remaining_research_order": ordered[len(first):],
        "manifest": manifest,
        "disclaimer": "Research scheduling heuristic only; no C/C2 prediction or betting authority.",
    }


def verified_research_order(manifest: dict[str, Any], candidates: list[dict[str, Any]],
                            source_hash: str) -> list[str]:
    if not isinstance(manifest, dict) or manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise GoalPrescreenError("goal-first manifest required for prospective research order")
    proof = manifest.get("screen_fingerprint")
    without_proof = {k: v for k, v in manifest.items() if k != "screen_fingerprint"}
    if not isinstance(proof, str) or _fingerprint(without_proof) != proof:
        raise GoalPrescreenError("goal-first manifest fingerprint mismatch")
    if manifest.get("source_payload_hash") != source_hash:
        raise GoalPrescreenError("goal-first manifest does not match frozen Step0 source")
    rows = manifest.get("original_rows")
    if not isinstance(rows, list) or len(rows) != len(candidates):
        raise GoalPrescreenError("incomplete goal-first A/B queue")
    frozen = {(c["match_id"], c["queue_rank"], c["operational_grade"]) for c in candidates}
    supplied = {(r.get("match_id"), r.get("queue_rank"), r.get("operational_grade")) for r in rows}
    if frozen != supplied or len(supplied) != len(rows):
        raise GoalPrescreenError("goal-first manifest rewrote original A/B identities or ranks")
    ordered = manifest.get("ordered_eligible_match_ids")
    if not isinstance(ordered, list) or len(ordered) != len(set(ordered)):
        raise GoalPrescreenError("duplicated goal-first research order")
    active = [r for r in rows if r.get("screen_status") in ("QUANTIFIED", "EVIDENCE_LIMITED")]
    sorted_expected = [r["match_id"] for r in sorted(active, key=_priority)]
    if ordered != sorted_expected:
        raise GoalPrescreenError("research priority order inconsistent with prescreen evidence")
    return ordered
