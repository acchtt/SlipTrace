#!/usr/bin/env python3
"""Football Stage V4: two clean commands, /sweep and /rank.

No old Step0 ZIP, global women's sweep, 8-fixture cap or bookmaker quote
requirement. Source discovery and Airtable refetch are explicit operations by
the caller; this code never claims to browse sites or publish by itself.
Actual model assessments are computed by existing independent C and C2
engine functions, with the user-retired OLD CLI entrypoints kept retired.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ENGINE = Path(__file__).resolve().parents[1] / "engine"
sys.path.insert(0, str(ENGINE))
from board_pair_cli import run_board_pair  # historic pure implementation; old CLI remains retired
from league_registry import classify
from discovery_goal_gate import screen_discovery
from goals_first_intake import select as select_goal_candidates
from source_completeness import (
    CONTRACT as SOURCE_COMPLETENESS_CONTRACT,
    SourceCompletenessError,
    validate_source_completeness,
)

SCHEMA = "football-stages-v4"
BASE = "appbzxqXYf0lKfD4P"
STEP1_ENGINE_RESULT_FIELD_IDS = {
    "c": "fldhUWNoyXzXfQJ3C",
    "c2": "fldq0n2tDlS58goAm",
}
VALID_MATCH_STATUSES = {"PREMATCH_CONFIRMED","STARTED","FINISHED","POSTPONED","CANCELLED"}
PRICE_FIELDS = {"odds", "bookmaker_total", "price", "final_score", "ft_goals", "live_score", "bet"}
UNRANKED = {"RESEARCH_EVIDENCE_MISSING", "PREMATCH_WINDOW_CLOSED", "SOURCE_CHANGED",
            "MATCH_NEWS_UNVERIFIED", "RESEARCH_BUDGET_EXHAUSTED"}
MAX_SOURCE_AGE_MINUTES = 60
SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC = datetime.fromisoformat(
    "2026-10-12T18:00:00+00:00"
)


class StageError(ValueError):
    pass


def _time(value: Any, name: str) -> datetime:
    if not isinstance(value, str):
        raise StageError(f"{name}: timestamp required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise StageError(f"{name}: invalid timestamp") from None
    if dt.tzinfo is None:
        raise StageError(f"{name}: timezone required")
    return dt.astimezone(timezone.utc)


def _url(value: Any, name: str) -> str:
    if not isinstance(value, str):
        raise StageError(f"{name}: HTTPS source required")
    v = urlsplit(value)
    if v.scheme != "https" or not v.hostname or "." not in v.hostname or v.username or v.password:
        raise StageError(f"{name}: valid public HTTPS source required")
    return value


def _hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":")).encode("utf-8")).hexdigest()


def _verified(obj: Any, expected_status: str) -> None:
    if isinstance(obj, dict) and obj.get("status") == "V4_SWEEP_DERIVED_UNATTESTED":
        raise StageError(
            "V4_ATTESTATION_REQUIRED: This is a derived estimate, not the "
            "production stage output. Obtain the original source.json and "
            "execute stages_v4/stage.py sweep or replay_unattested.py, or "
            "download the verified V4 receipt from GitHub Actions. "
            "Never promote an intake by editing its status or digest."
        )
    if not isinstance(obj, dict) or obj.get("schema_version") != SCHEMA or obj.get("status") != expected_status:
        raise StageError(f"{expected_status}: missing authentic production stage payload")
    digest = obj.get("integrity_sha256")
    if digest != _hash({k: v for k, v in obj.items() if k != "integrity_sha256"}):
        raise StageError("frozen stage integrity SHA256 mismatch")


def sweep(source: dict[str, Any], *, now: str, _historical_registry_only: bool = False,
          _historical_replay: bool = False,
          _historical_no_cheap_filters: bool = False) -> dict[str, Any]:
    """Classify one complete provider date-surface snapshot.

    Prospective production sweeps after the V2 activation boundary must carry
    a fail-closed source-completeness manifest. Historical replays may bypass
    only when explicitly invoked by frozen-history code.
    """
    at = _time(now, "now")
    if not isinstance(source, dict) or source.get("schema_version") != SCHEMA:
        raise StageError("new V4 source snapshot required")
    run_id = source.get("run_id")
    if not isinstance(run_id, str) or not run_id.startswith("V4-") or len(run_id) > 120:
        raise StageError("fresh V4- run ID required (old retired runs cannot resume)")
    start, end = _time(source.get("window_start_utc"), "window_start_utc"), _time(
        source.get("window_end_utc"), "window_end_utc")
    if end <= start or end - start > timedelta(days=2) or end <= at:
        raise StageError("future sweep window must be > 0 and <= 48h")
    provider = source.get("source_family")
    if not isinstance(provider, str) or len(provider.strip()) < 2:
        raise StageError("named actual source family required")
    observed = _time(source.get("source_observed_at_utc"), "source_observed_at_utc")
    if not at - timedelta(minutes=MAX_SOURCE_AGE_MINUTES) <= observed <= at:
        raise StageError("source snapshot stale or from future")
    _url(source.get("source_url"), "source_url")
    fixtures = source.get("fixtures")
    if not isinstance(fixtures, list) or len(fixtures) > 2000:
        raise StageError("source fixture list must be explicit and bounded")
    completeness = None
    strict_completeness = at >= SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC and not _historical_replay
    if strict_completeness or source.get("source_completeness_manifest") is not None:
        try:
            completeness = validate_source_completeness(source, now=at.isoformat())
        except SourceCompletenessError as exc:
            raise StageError(str(exc)) from exc
    elif at >= SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC and _historical_replay:
        # Explicit historical replay is allowed only for an already frozen
        # pre-activation source epoch. New production callers never set this.
        if _time(source.get("source_observed_at_utc"), "source_observed_at_utc") >= SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC:
            raise StageError("SWEEP_LEGACY_REPLAY_AFTER_V2_ACTIVATION_FORBIDDEN")
    ledger, queue, seen = [], [], set()
    for i, raw in enumerate(fixtures):
        # One weak-data fixture must not block other verified matches.
        if (isinstance(raw, dict) and isinstance(raw.get("match_id"), str)
                and raw["match_id"] in seen):
            raise StageError(f"fixture {i}: conflicting duplicate canonical match ID")
        try:
            if not isinstance(raw, dict):
                raise StageError(f"fixture {i} must be a source object")
            if set(raw) & PRICE_FIELDS:
                raise StageError("no bookmaker/live/FT data in Step0 source snapshot")
            mid = raw.get("match_id")
            if (not isinstance(mid, str) or not mid.strip()
                    or mid.upper().startswith("DISCOVERY-") or mid in seen):
                raise StageError(f"fixture {i}: canonical unique source match ID required")
            seen.add(mid)
            home, away = raw.get("home"), raw.get("away")
            if not isinstance(home, str) or not home.strip() or not isinstance(away, str) or not away.strip():
                raise StageError(f"{mid}: real home and away team identities required")
            ko = _time(raw.get("kickoff_utc"), f"{mid}.kickoff_utc")
            link = _url(raw.get("source_url"), f"{mid}.source_url")
            checked = _time(raw.get("observed_at_utc"), f"{mid}.observed_at_utc")
            if not at - timedelta(minutes=MAX_SOURCE_AGE_MINUTES) <= checked <= at:
                raise StageError(f"{mid}: fixture evidence stale/future")
            status = raw.get("fixture_status")
            if status not in VALID_MATCH_STATUSES:
                raise StageError(f"{mid}: source-confirmed fixture status required")
            result = classify(raw)
            # Historical source replay must preserve the policy and digest
            # originally executed, not reinterpret last night's fixtures.
            if _historical_registry_only and result["lane"] == "DISCOVERY":
                result = {
                    "lane": "EXCLUDED",
                    "reason": (
                        "UNRESEARCHED_DOMESTIC_CUP"
                        if raw.get("competition_kind") == "DOMESTIC_CUP"
                        else "UNRESEARCHED_OR_UNVERIFIED_DOMESTIC_DIVISION"
                    ),
                }
            lane, reason = result["lane"], result["reason"]
            discovery_screen = None
            if not (start <= ko < end) or ko <= at or status != "PREMATCH_CONFIRMED":
                lane, reason = "CLOSED", "OUT_OF_WINDOW_STARTED_OR_NOT_PREMATCH"
            elif lane in ("CONDITIONAL", "PILOT", "DISCOVERY"):
                # Unknown league = investigate football; it is NOT model PASS.
                # Run the goal screen independently of XI/market availability.
                if lane == "DISCOVERY":
                    discovery_screen = screen_discovery(
                        run_id=run_id,
                        source_payload_hash=_hash(source),
                        at_utc=at.isoformat(),
                        fixture=raw,
                    )
                proof = raw.get("researchability_status")
                evidence = raw.get("researchability_proof")
                if proof == "VERIFIED":
                    if not isinstance(evidence, dict):
                        raise StageError(f"{mid}: VERIFIED conditional/discovery league requires source evidence")
                    _url(evidence.get("source_url"), f"{mid}.researchability_proof.source_url")
                    stamp = _time(evidence.get("checked_at_utc"),
                                  f"{mid}.researchability_proof.checked_at_utc")
                    if not at - timedelta(days=7) <= stamp <= at:
                        raise StageError(f"{mid}: researchability source evidence stale/future")
                    if evidence.get("match_id") != mid or evidence.get("current_channels_checked") is not True:
                        raise StageError(f"{mid}: conditional/discovery channel proof not bound to fixture")
                elif lane == "DISCOVERY":
                    lane, reason = "PENDING_DISCOVERY", "UNREGISTERED_MATCH_NEEDS_CURRENT_RESEARCHABILITY_PROOF"
                else:
                    lane, reason = "PENDING_RESEARCHABILITY", "RESEARCHED_LEAGUE_NEEDS_CURRENT_CHANNEL_PROOF"
                if result["lane"] == "DISCOVERY" and lane == "DISCOVERY":
                    if raw.get("competition_kind") == "DOMESTIC_CUP":
                        format_proof = raw.get("tournament_format_proof")
                        if not isinstance(format_proof, dict):
                            lane, reason = "PENDING_DISCOVERY", "OFFICIAL_CUP_FORMAT_AND_INCENTIVES_NOT_VERIFIED"
                        else:
                            _url(format_proof.get("source_url"), f"{mid}.tournament_format_proof.source_url")
                            format_checked = _time(format_proof.get("checked_at_utc"),
                                                   f"{mid}.tournament_format_proof.checked_at_utc")
                            if not at - timedelta(days=7) <= format_checked <= at or (
                                format_proof.get("match_id") != mid
                                or format_proof.get("competition_format_verified") is not True
                            ):
                                raise StageError(f"{mid}: cup format proof must be current and fixture-bound")
                    if lane == "DISCOVERY" and discovery_screen["status"] != "DISCOVERY_GOAL_QUALIFIED":
                        lane, reason = "PENDING_DISCOVERY", discovery_screen["reason"]
            item = {
                "source_row_index": i, "match_id": mid, "country": raw.get("country"),
                "competition": raw.get("competition"),
                "competition_kind": raw.get("competition_kind"),
                "home": home, "away": away, "kickoff_utc": ko.isoformat(),
                "fixture_status": status,
                "source_family": provider, "source_url": link,
                "observed_at_utc": checked.isoformat(),
                "researchability_proof": raw.get("researchability_proof") if result["lane"] in ("CONDITIONAL", "PILOT", "DISCOVERY") else None,
                **({} if _historical_registry_only else {
                    "discovery_screen": discovery_screen,
                    "tournament_format_proof": raw.get("tournament_format_proof") if result["lane"] == "DISCOVERY" and raw.get("competition_kind") == "DOMESTIC_CUP" else None,
                }),
                "registry_lane": result["lane"],
                "intake_lane": lane, "reason": reason,
            }
            ledger.append(item)
            if lane in {"ROUTINE","CONDITIONAL","PILOT","DISCOVERY"}:
                queue.append({**item, "football_evidence": raw.get("football_evidence"),
                              "operational_grade": "A" if lane == "ROUTINE" else "B"})
        except StageError as exc:
            ledger.append({
                "source_row_index": i,
                "match_id": raw.get("match_id") if isinstance(raw, dict) else None,
                "country": raw.get("country") if isinstance(raw, dict) else None,
                "competition": raw.get("competition") if isinstance(raw, dict) else None,
                "intake_lane": "PENDING_SOURCE", "reason": str(exc),
            })
            continue
    # Registration admits a fixture to *research*, not to the official
    # goal-positive shortlist. Apply ONE equal goal signal gate to every
    # league, including routine tiers. Preserve historical replay exactly.
    goal_selection = None
    if not _historical_registry_only:
        goal_selection = select_goal_candidates(
            run_id=run_id, at_utc=at.isoformat(), source_hash=_hash(source),
            source_rows=fixtures, ledger=ledger, provisional_queue=queue,
            apply_cheap_filters=not _historical_no_cheap_filters,
        )
        queue = goal_selection["eligible_queue"]
    # Every source-visible fixture stays in the ledger; no arbitrary first-8 cap.
    queue.sort(key=lambda x: (x["kickoff_utc"], x["match_id"]))
    for idx, item in enumerate(queue, 1):
        item["queue_rank"] = idx
    form_warnings = []
    # V4 goal qualification already validated the same source-backed histories.
    # Research order is now derived directly from each selected row's frozen
    # goal_screen instead of invoking a second legacy prescreen engine.
    ordered_rows = sorted(
        queue,
        key=lambda q: (
            -int(isinstance((q.get("goal_screen") or {}).get("priority_score"), (int, float))),
            -float((q.get("goal_screen") or {}).get("priority_score") or 0),
            (q.get("cheap_filter") or {}).get("priority_rank", 4),
            q["kickoff_utc"],
            q["match_id"],
        ),
    )
    order = [row["match_id"] for row in ordered_rows]
    screen = {
        "schema_version": "football-v4-goal-research-manifest-v2",
        "run_id": run_id,
        "source_payload_hash": _hash(ledger),
        "priority_profile": "GOAL_SIGNAL_FIRST_V2",
        "ordered_eligible_match_ids": order,
        "original_rows": [
            {
                "match_id": row["match_id"],
                "queue_rank": row["queue_rank"],
                "operational_grade": row["operational_grade"],
                "screen_status": "QUANTIFIED",
                "priority_score": (row.get("goal_screen") or {}).get("priority_score"),
                "source_screen_fingerprint": (
                    row.get("goal_screen") or {}
                ).get("source_screen_fingerprint"),
            }
            for row in queue
        ],
    }
    screen["screen_fingerprint"] = _hash(screen)
    outcome = {
        "schema_version": SCHEMA, "status": "V4_SWEEP_READY",
        "run_id": run_id, "created_at_utc": at.isoformat(),
        "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
        "source_family": provider, "source_url": source["source_url"],
        "source_observed_at_utc": observed.isoformat(),
        "source_ledger_hash": _hash(ledger),
        "scope": ("RESEARCHED_COUNTRY_LEAGUE_REGISTRY_SOURCE_VISIBLE_ONLY"
                  if _historical_registry_only else "RESEARCHED_PLUS_SOURCE_SCREENED_UNREGISTERED_COMPETITIONS"),
        "fixture_count": len(ledger),
        "eligible_count": len(queue),
        "pending_researchability_count": sum(z["intake_lane"] == "PENDING_RESEARCHABILITY" for z in ledger),
         "pending_source_count": sum(z["intake_lane"] == "PENDING_SOURCE" for z in ledger),
        "excluded_or_closed_count": sum(z["intake_lane"] in {"EXCLUDED","CLOSED","UNVERIFIED"} for z in ledger),
        "source_ledger": ledger, "eligible_queue": queue,
        "research_order": order, "goal_screen_manifest": screen,
        "invalid_historical_form_sources": form_warnings,
        "no_fixed_eight_match_cap": True, "price_required_for_football": False,
        "ranked": False, "published": False, "bet_recorded": False,
    }
    if completeness is not None:
        outcome["source_completeness_contract"] = completeness["source_completeness_contract"]
        outcome["source_completeness_sha256"] = completeness["source_completeness_sha256"]
        outcome["source_completeness"] = completeness
    if not _historical_registry_only:
        outcome["pending_discovery_count"] = sum(
            x["intake_lane"] == "PENDING_DISCOVERY" for x in ledger
        )
        outcome["discovery_qualified_count"] = sum(
            x.get("registry_lane") == "DISCOVERY" and x["intake_lane"] == "GOAL_PRIORITY"
            for x in ledger
        )
        outcome["goal_selection_policy"] = "EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1"
        outcome["goal_research_queue"] = goal_selection["goal_research_queue"]
        outcome["goal_research_order"] = goal_selection["goal_research_order"]
        outcome["priority_research_queue"] = goal_selection.get("priority_research_queue", [])
        outcome["priority_research_order"] = goal_selection.get("priority_research_order", [])
        outcome["deferred_research_queue"] = goal_selection.get("deferred_research_queue", [])
        outcome["priority_research_count"] = goal_selection.get("priority_research_count", 0)
        outcome["deferred_research_count"] = goal_selection.get("deferred_research_count", 0)
        outcome["pending_goal_research_count"] = goal_selection["pending_goal_research_count"]
        outcome["unresearched_goal_history_count"] = goal_selection["unresearched_goal_history_count"]
        outcome["low_goal_signal_count"] = goal_selection["low_goal_signal_count"]
        outcome["verified_goal_qualified_count"] = goal_selection["verified_goal_qualified_count"]
        if "cheap_filter_counts" in goal_selection:
            outcome["cheap_filter_policy"] = "RESEARCH_PRIORITY_V1"
            outcome["cheap_filter_counts"] = goal_selection["cheap_filter_counts"]
        outcome["discovery_watchlist"] = [{
            "match_id": x["match_id"], "country": x["country"],
            "competition": x["competition"], "home": x["home"],
            "away": x["away"], "kickoff_utc": x["kickoff_utc"],
            "intake_lane": x["intake_lane"], "reason": x["reason"],
            "discovery_screen": x.get("discovery_screen"),
        } for x in ledger if x.get("registry_lane") == "DISCOVERY"
          and x.get("intake_lane") in ("GOAL_PRIORITY", "PENDING_DISCOVERY",
                                     "PENDING_GOAL_RESEARCH")]
    outcome["integrity_sha256"] = _hash(outcome)
    return outcome


def verify_rank_source_and_status(
    sweep_receipt: dict[str, Any], original_source: dict[str, Any],
    status_refresh: dict[str, Any], *, now: str,
) -> dict[str, Any]:
    """Replay the native V4 source and validate the exact rank-time full-cohort status payload."""
    return _check_rank_source_and_status(
        sweep_receipt, original_source, status_refresh, _time(now, "rank provenance now")
    )


def _check_rank_source_and_status(
    sweep_receipt: dict[str, Any], original_source: dict[str, Any],
    status_refresh: dict[str, Any], at: datetime,
) -> dict[str, Any]:
    """Require native source replay plus independently gathered current fixture state.

    A matching local SHA256 alone does not prove the input was acquired
    from a real provider. External source verification remains mandatory.
    """
    if not isinstance(original_source, dict):
        raise StageError("V4_SOURCE_REPLAY_REQUIRED: original source.json missing")
    receipt_created = _time(sweep_receipt.get("created_at_utc"), "sweep.created_at_utc")
    is_legacy_receipt = receipt_created < SWEEP_COMPLETENESS_V2_EFFECTIVE_UTC
    if not is_legacy_receipt and sweep_receipt.get("source_completeness_contract") != SOURCE_COMPLETENESS_CONTRACT:
        raise StageError("V4_SOURCE_COMPLETENESS_PROOF_REQUIRED_FOR_POST_REBUILD_SWEEP")
    replayed = sweep(
        original_source,
        now=sweep_receipt["created_at_utc"],
        _historical_replay=is_legacy_receipt,
        _historical_no_cheap_filters=(
            sweep_receipt.get("cheap_filter_policy") != "RESEARCH_PRIORITY_V1"
        ),
    )
    if (replayed["integrity_sha256"] != sweep_receipt["integrity_sha256"]
            or original_source.get("run_id") != sweep_receipt.get("run_id")):
        raise StageError("V4_SOURCE_REPLAY_MISMATCH: receipt differs from original source")
    if not isinstance(status_refresh, dict):
        raise StageError("V4_STATUS_REFRESH_REQUIRED: independently checked fixtures missing")
    if (status_refresh.get("schema_version") != "football-v4-rank-status-refresh-v1"
            or status_refresh.get("run_id") != sweep_receipt["run_id"]
            or status_refresh.get("sweep_integrity_sha256") != sweep_receipt["integrity_sha256"]):
        raise StageError("V4_STATUS_REFRESH_MISMATCH: source/run/hash mismatch")
    checked = _time(status_refresh.get("checked_at_utc"), "status_refresh.checked_at_utc")
    if not at - timedelta(minutes=10) <= checked <= at:
        raise StageError("V4_STATUS_REFRESH_STALE: status check older than 10 minutes")
    rows = status_refresh.get("matches")
    frozen = {q["match_id"]: q for q in sweep_receipt["eligible_queue"]}
    if not isinstance(rows, list) or len(rows) != len(frozen):
        raise StageError("V4_STATUS_REFRESH_INCOMPLETE: full eligible cohort required")
    seen = set()
    statuses = {}
    for row in rows:
        if not isinstance(row, dict):
            raise StageError("V4_STATUS_REFRESH_MALFORMED")
        mid = row.get("match_id")
        if mid not in frozen or mid in seen:
            raise StageError("V4_STATUS_REFRESH_MISMATCH: duplicate/foreign fixture")
        seen.add(mid)
        source = frozen[mid]
        _url(row.get("source_url"), f"{mid}.status_source_url")
        if row["source_url"] != source["source_url"]:
            raise StageError(f"{mid}: status source differs from frozen fixture source")
        observed = _time(row.get("observed_at_utc"), f"{mid}.status_observed_at_utc")
        if not at - timedelta(minutes=10) <= observed <= at or observed > checked:
            raise StageError(f"{mid}: V4_STATUS_REFRESH_STALE")
        updated_ko = _time(row.get("kickoff_utc"), f"{mid}.status_kickoff_utc")
        if updated_ko != _time(source["kickoff_utc"], f"{mid}.frozen_kickoff"):
            raise StageError(f"{mid}: V4_KICKOFF_CHANGED; re-sweep the updated source epoch")
        status = row.get("fixture_status")
        if status not in VALID_MATCH_STATUSES:
            raise StageError(f"{mid}: V4_STATUS_REFRESH_UNKNOWN")
        statuses[mid] = status
    return {
        "status_refresh_sha256": _hash(status_refresh),
        "original_source_sha256": _hash(original_source),
        "status_by_match": statuses,
    }


def rank(sweep_receipt: dict[str, Any], c: dict[str, Any], c2: dict[str, Any],
         unranked_reasons: dict[str, str], *, now: str,
         original_source: dict[str, Any] | None = None,
         status_refresh: dict[str, Any] | None = None) -> dict[str, Any]:
    """Evaluate actual C/C2 inputs against frozen V4 eligible set; never bet."""
    _verified(sweep_receipt, "V4_SWEEP_READY")
    at = _time(now, "now")
    if not _time(sweep_receipt["created_at_utc"], "created") <= at:
        raise StageError("rank clock predates sweep")
    if at > _time(sweep_receipt["created_at_utc"], "created") + timedelta(hours=12):
        raise StageError("sweep source epoch stale; refresh new V4 fixture source")
    queue = sweep_receipt["eligible_queue"]
    if sweep_receipt.get("goal_selection_policy") == "EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1":
        if any(
            not isinstance(row, dict)
            or row.get("intake_lane") != "GOAL_PRIORITY"
            or not isinstance(row.get("goal_screen"), dict)
            or row["goal_screen"].get("status") != "DISCOVERY_GOAL_QUALIFIED"
            for row in queue
        ):
            raise StageError("goal-first shortlist violated: unqualified match cannot enter C/C2 rank")
        manifest = sweep_receipt.get("goal_screen_manifest")
        if queue and (
            not isinstance(manifest, dict)
            or manifest.get("priority_profile") != "GOAL_SIGNAL_FIRST_V1"
        ):
            raise StageError("goal-first ranked source missing genuine goals-priority manifest")
    frozen = {x["match_id"]: x for x in queue}
    if len(frozen) != len(queue):
        raise StageError("frozen eligible queue contains duplicate match ID")
    if not frozen:
        raise StageError("no verified candidates to rank")
    if not isinstance(c, dict) or not isinstance(c2, dict):
        raise StageError("C and C2 source-backed assessment payloads required")
    crows = c.get("matches")
    c2rows = c2.get("matches")
    if not isinstance(crows, list) or not crows or not isinstance(c2rows, list):
        raise StageError("actual source-backed C/C2 evidence required")
    ids = [r.get("match_id") for r in crows if isinstance(r, dict)]
    if len(ids) != len(crows) or len(ids) != len(set(ids)) or not set(ids).issubset(frozen):
        raise StageError("C ranked fixture cohort must be unique subset of frozen V4 fixtures")
    if {r.get("match_id") for r in c2rows if isinstance(r, dict)} != set(ids) or len(c2rows) != len(ids):
        raise StageError("C2 shadow cohort must exactly match C")
    if not isinstance(unranked_reasons, dict) or set(unranked_reasons) != set(frozen) - set(ids):
        raise StageError("every unranked eligible fixture must have an explicit reason")
    if not set(unranked_reasons.values()).issubset(UNRANKED):
        raise StageError("unknown unranked reason; no invented model PASS")
    # Independently reject retrospective prematch selections before any
    # source replay; a late historical rank remains forbidden even when
    # the caller has not supplied a new status observation.
    for mid in ids:
        if at >= _time(frozen[mid]["kickoff_utc"], f"{mid}.kickoff"):
            raise StageError(f"{mid}: retroactive prematch rank forbidden")
    source_proof = verify_rank_source_and_status(
        sweep_receipt, original_source, status_refresh, now=at.isoformat()
    )
    for mid in ids:
        if source_proof["status_by_match"][mid] != "PREMATCH_CONFIRMED":
            raise StageError(f"{mid}: PREMATCH_WINDOW_CLOSED by current fixture status")
    for mid, reason in unranked_reasons.items():
        if reason == "PREMATCH_WINDOW_CLOSED" and (
            source_proof["status_by_match"][mid] == "PREMATCH_CONFIRMED"
            and at < _time(frozen[mid]["kickoff_utc"], f"{mid}.kickoff")
        ):
            raise StageError(f"{mid}: PREMATCH_WINDOW_CLOSED contradicts fresh fixture status")
    for r in crows + c2rows:
        mid = r["match_id"]
        if _time(r.get("kickoff_ict"), f"{mid}.model_kickoff") != _time(
            frozen[mid]["kickoff_utc"], f"{mid}.sweep_kickoff"):
            raise StageError(f"{mid}: kickoff or fixture source identity drift")
        if at >= _time(frozen[mid]["kickoff_utc"], f"{mid}.kickoff"):
            raise StageError(f"{mid}: retroactive prematch rank forbidden")
    # Source-backed goal-first prescreen never skips a more promising match
    # merely because it came after the old first-eight shortlist.
    order = sweep_receipt["research_order"]
    if len(order) != len(frozen) or set(order) != set(frozen):
        raise StageError("source-reconciled full research order corrupted")
    last = max(order.index(mid) for mid in ids)
    for mid in order[:last]:
        if mid not in ids and unranked_reasons[mid] not in {
            "RESEARCH_EVIDENCE_MISSING", "PREMATCH_WINDOW_CLOSED", "MATCH_NEWS_UNVERIFIED", "SOURCE_CHANGED"
        }:
            raise StageError(f"{mid}: earlier research-priority fixture skipped without evidence blocker")
    result = run_board_pair(c, c2)
    if result["board_engine_execution_status"] != "EXECUTED_C_C2_BOARDS":
        raise StageError("independent C and C2 model engines not executed")
    out = {
        "schema_version": SCHEMA, "status": "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK",
        "run_id": sweep_receipt["run_id"],
        "sweep_integrity_sha256": sweep_receipt["integrity_sha256"],
        "rank_at_utc": at.isoformat(),
        "full_queue_count": len(frozen), "ranked_count": len(ids),
        "unranked_reasons": unranked_reasons,
        "board_pair": result, "active_base_id": BASE,
        "c_official": True, "c2_shadow_only": True,
        "publication_authorized": False, "bet_recorded": False,
        "original_source_sha256": source_proof["original_source_sha256"],
        "status_refresh_sha256": source_proof["status_refresh_sha256"],
        "source_replayed": True, "current_fixture_status_checked": True,
    }
    out["integrity_sha256"] = _hash(out)
    return out


def _readback_engine_result(row: dict[str, Any], model: str, match_id: str) -> dict[str, Any]:
    key = f"step1_engine_{model}_result"
    field_id_key = key + "_field_id"
    if row.get(field_id_key) != STEP1_ENGINE_RESULT_FIELD_IDS[model]:
        raise StageError(f"{match_id}: {model} Step1 engine-result Airtable field ID not verified")
    stored = row.get(key)
    if isinstance(stored, str):
        try:
            stored = json.loads(stored)
        except json.JSONDecodeError as exc:
            raise StageError(f"{match_id}: {model} persisted Step1 engine result is malformed JSON") from exc
    if not isinstance(stored, dict):
        raise StageError(f"{match_id}: {model} persisted Step1 engine result missing")
    return stored


def verify_rank(readback: dict[str, Any], rank_receipt: dict[str, Any]) -> dict[str, Any]:
    """Compare caller-refetched Active Airtable rows, not self-assert a save."""
    _verified(rank_receipt, "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK")
    if (not isinstance(readback, dict)
            or readback.get("active_base_id") != BASE
            or readback.get("method") != "INDEPENDENT_AIRTABLE_REFETCH"
            or readback.get("run_id") != rank_receipt["run_id"]
            or readback.get("rank_integrity_sha256") != rank_receipt["integrity_sha256"]
            or readback.get("sweep_integrity_sha256") != rank_receipt["sweep_integrity_sha256"]):
        raise StageError("fresh active Airtable readback and both exact V4 hashes required")
    read_at = _time(readback.get("readback_at_utc"), "readback_at_utc")
    ranked_at = _time(rank_receipt["rank_at_utc"], "rank_at_utc")
    if not ranked_at <= read_at <= ranked_at + timedelta(minutes=30):
        raise StageError("independent Airtable readback timestamp is stale/future")
    original = rank_receipt["board_pair"]["results"]
    rows = readback.get("ranked_rows")
    if not isinstance(rows, list) or len(rows) != rank_receipt["ranked_count"]:
        raise StageError("independent Airtable rank row count mismatch")
    for model in ("c", "c2"):
        indexed = {r["match_id"]: r for r in original[model]["matches"]}
        observed = {r["match_id"]: r for r in rows if isinstance(r, dict) and "match_id" in r}
        if set(indexed) != set(observed) or len(observed) != len(rows):
            raise StageError("independent Airtable ranked fixture identities mismatch")
        for mid, model_row in indexed.items():
            if observed[mid].get("coverage_id") != f"{rank_receipt['run_id']}|{mid}":
                raise StageError(f"{mid}: Airtable immutable coverage identity differs")
            for local, remote in (("rank", f"{model}_rank"),
                                  ("board_state", f"{model}_board_state"),
                                  ("supported_line", f"{model}_supported_line")):
                actual = observed[mid].get(remote)
                if local == "board_state" and isinstance(actual, str):
                    actual = actual.removeprefix("C2-" if model == "c2" else "C-")
                if actual != model_row.get(local):
                    raise StageError(f"{mid} {model} {local}: independent saved value differs")
            stored_result = _readback_engine_result(observed[mid], model, mid)
            if stored_result != model_row:
                raise StageError(f"{mid}: {model} exact Step1 engine evidence differs from Airtable")
            if model == "c" and observed[mid].get("follow_lane") != model_row.get("follow_lane"):
                raise StageError(f"{mid}: official C FOLLOW/RESERVE/STOP lane differs")
    model_evidence_sha256 = _hash(original)
    return {
        "schema_version": SCHEMA, "status": "V4_RANK_PERSISTENCE_VERIFIED",
        "run_id": rank_receipt["run_id"], "rank_sha256": rank_receipt["integrity_sha256"],
        "ranked_count": rank_receipt["ranked_count"],
        "c2_shadow_only": True, "no_bet_created": True,
        "model_evidence_readback_verified": True,
        "model_evidence_sha256": model_evidence_sha256,
        "step1_engine_c_result_field_id": STEP1_ENGINE_RESULT_FIELD_IDS["c"],
        "step1_engine_c2_result_field_id": STEP1_ENGINE_RESULT_FIELD_IDS["c2"],
        "source_replayed": rank_receipt.get("source_replayed") is True,
        "current_fixture_status_checked": rank_receipt.get("current_fixture_status_checked") is True,
        "original_source_sha256": rank_receipt.get("original_source_sha256"),
        "status_refresh_sha256": rank_receipt.get("status_refresh_sha256"),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Clean football V4: source snapshot sweep and paired C/C2 rank")
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sweep")
    s.add_argument("--source", required=True)
    r = sub.add_parser("rank")
    for key in ("sweep", "c", "c2", "unranked", "source", "status-refresh"):
        r.add_argument("--" + key, required=True)
    v = sub.add_parser("verify")
    v.add_argument("--rank", required=True)
    v.add_argument("--readback", required=True)
    p.add_argument("--now", default=datetime.now(timezone.utc).isoformat(),
                   help="Actual UTC time; optional override only for reproducible QA")
    p.add_argument("--output", help="Write resulting immutable JSON receipt to file")
    args = p.parse_args()
    try:
        def load(path: str) -> dict[str, Any]:
            return json.loads(Path(path).read_text(encoding="utf-8"))
        if args.command == "sweep":
            out = sweep(load(args.source), now=args.now)
        elif args.command == "rank":
            out = rank(load(args.sweep), load(args.c), load(args.c2),
                       load(args.unranked), now=args.now,
                       original_source=load(args.source),
                       status_refresh=load(args.status_refresh))
        else:
            out = verify_rank(load(args.readback), load(args.rank))
        encoded = json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(encoded + "\n", encoding="utf-8")
        print(encoded)
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "V4_STAGE_BLOCKED", "stage": args.command,
                          "reason": str(exc)}), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
