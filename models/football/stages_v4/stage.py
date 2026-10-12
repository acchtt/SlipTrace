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
from goal_route_prescreen import GoalPrescreenError, run_prescreen
from league_registry import classify
from discovery_goal_gate import screen_discovery
from goals_first_intake import select as select_goal_candidates

SCHEMA = "football-stages-v4"
BASE = "appbzxqXYf0lKfD4P"
VALID_MATCH_STATUSES = {"PREMATCH_CONFIRMED","STARTED","FINISHED","POSTPONED","CANCELLED"}
PRICE_FIELDS = {"odds", "bookmaker_total", "price", "final_score", "ft_goals", "live_score", "bet"}
UNRANKED = {"RESEARCH_EVIDENCE_MISSING", "PREMATCH_WINDOW_CLOSED", "SOURCE_CHANGED",
            "MATCH_NEWS_UNVERIFIED", "RESEARCH_BUDGET_EXHAUSTED"}
MAX_SOURCE_AGE_MINUTES = 60


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


def sweep(source: dict[str, Any], *, now: str, _historical_registry_only: bool = False) -> dict[str, Any]:
    """Classify ONE actual provider snapshot, without a worldwide crawl."""
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
        )
        queue = goal_selection["eligible_queue"]
    # Every source-visible fixture stays in the ledger; no arbitrary first-8 cap.
    queue.sort(key=lambda x: (x["kickoff_utc"], x["match_id"]))
    for idx, item in enumerate(queue, 1):
        item["queue_rank"] = idx
    screen = None
    form_warnings = []
    order = [x["match_id"] for x in queue]
    if queue:
        evidence = [{
            "match_id": q["match_id"], "queue_rank": q["queue_rank"],
            "operational_grade": q["operational_grade"],
            "fixture_status": q["fixture_status"], "kickoff_utc": q["kickoff_utc"],
            "country": q["country"], "competition_name": q["competition"],
            "football_evidence": q["football_evidence"],
        } for q in queue]
        # Bad historical form from one provider is an *evidence-limited*
        # research row, not a reason to discard 19 other verified fixtures.
        form_warnings = []
        for row in evidence:
            if row["football_evidence"] is None:
                continue
            try:
                run_prescreen({
                    "schema_version": "football-goal-route-prescreen-v1",
                    "run_id": run_id,
                    "source_payload_hash": _hash(ledger),
                    "screen_at_utc": at.isoformat(),
                    "candidates": [{**row, "queue_rank": 1}],
                })
            except GoalPrescreenError as exc:
                form_warnings.append({"match_id": row["match_id"], "reason": str(exc)})
                row["football_evidence"] = None
        screened = run_prescreen({
            "schema_version": "football-goal-route-prescreen-v1",
            "run_id": run_id,
            "source_payload_hash": _hash(ledger),
            "screen_at_utc": at.isoformat(),
            "candidates": evidence,
        })
        order = screened["manifest"]["ordered_eligible_match_ids"]
        screen = screened["manifest"]
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
    if not _historical_registry_only:
        outcome["pending_discovery_count"] = sum(
            x["intake_lane"] == "PENDING_DISCOVERY" for x in ledger
        )
        outcome["discovery_qualified_count"] = sum(
            x["registry_lane"] == "DISCOVERY" and x["intake_lane"] == "GOAL_PRIORITY"
            for x in ledger
        )
        outcome["goal_selection_policy"] = "EQUAL_SOURCE_BACKED_GOAL_SIGNAL_ALL_LEAGUES_V1"
        outcome["goal_research_queue"] = goal_selection["goal_research_queue"]
        outcome["goal_research_order"] = goal_selection["goal_research_order"]
        outcome["pending_goal_research_count"] = goal_selection["pending_goal_research_count"]
        outcome["unresearched_goal_history_count"] = goal_selection["unresearched_goal_history_count"]
        outcome["low_goal_signal_count"] = goal_selection["low_goal_signal_count"]
        outcome["verified_goal_qualified_count"] = goal_selection["verified_goal_qualified_count"]
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


def rank(sweep_receipt: dict[str, Any], c: dict[str, Any], c2: dict[str, Any],
         unranked_reasons: dict[str, str], *, now: str) -> dict[str, Any]:
    """Evaluate actual C/C2 inputs against frozen V4 eligible set; never bet."""
    _verified(sweep_receipt, "V4_SWEEP_READY")
    at = _time(now, "now")
    if not _time(sweep_receipt["created_at_utc"], "created") <= at:
        raise StageError("rank clock predates sweep")
    if at > _time(sweep_receipt["created_at_utc"], "created") + timedelta(hours=12):
        raise StageError("sweep source epoch stale; refresh new V4 fixture source")
    queue = sweep_receipt["eligible_queue"]
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
    }
    out["integrity_sha256"] = _hash(out)
    return out


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
            if model == "c" and observed[mid].get("follow_lane") != model_row.get("follow_lane"):
                raise StageError(f"{mid}: official C FOLLOW/RESERVE/STOP lane differs")
    return {
        "schema_version": SCHEMA, "status": "V4_RANK_PERSISTENCE_VERIFIED",
        "run_id": rank_receipt["run_id"], "rank_sha256": rank_receipt["integrity_sha256"],
        "ranked_count": rank_receipt["ranked_count"],
        "c2_shadow_only": True, "no_bet_created": True,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Clean football V4: source snapshot sweep and paired C/C2 rank")
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("sweep")
    s.add_argument("--source", required=True)
    r = sub.add_parser("rank")
    for key in ("sweep", "c", "c2", "unranked"):
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
                       load(args.unranked), now=args.now)
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
