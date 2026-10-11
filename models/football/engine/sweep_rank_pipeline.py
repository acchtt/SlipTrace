#!/usr/bin/env python3
"""Single local entrypoint for Football v2 Step0 -> Step1.

PREPARE: begin source-backed football research while broad Step0 certification
is still underway. It never yields an official rank or bet.
SEAL: validate final Step0 and independently fetched Sweep Runs evidence,
then atomically produce the official Work ZIP using the existing exporter.
RANK: consume *only* that real ZIP, execute the independent C+C2 engines
once and emit an immutable-to-persistence execution receipt.
PUBLISH: independently compare persisted active Airtable facts to that exact
execution before claiming a completed ranked board.

This orchestration deliberately does not fetch provider pages or Airtable.
Those source/database actions must be performed in the caller and passed as
real evidence. No synthetic market data, no replay of old runs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from board_pair_cli import run_board_pair
from goal_route_prescreen import run_prescreen
from step1_fixture_intake_cli import validate_step1_fixture_evidence
from rank_persistence_reconcile import (
    UNRANKED_REASONS, validate_rank_readback,
)
from step0_handoff_cli import validate_step0_handoff
from step0_package_cli import package as package_step0

SCHEMA = "football-sweep-rank-v3"
MAX_RESEARCH = 20
FIRST_RESEARCH_WAVE = 8
STANDARD_RESEARCH = 12


class SweepRankError(ValueError):
    pass


def _utc(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise SweepRankError(f"{field}: zoned UTC timestamp required")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise SweepRankError(f"{field}: invalid timestamp") from None
    if result.tzinfo is None:
        raise SweepRankError(f"{field}: timezone missing")
    return result.astimezone(timezone.utc)


def _https(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    u = urlsplit(value)
    return u.scheme == "https" and bool(u.hostname and "." in u.hostname) and not u.username and not u.password


def _hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")).hexdigest()


def _queue(rows: Any) -> list[dict[str, Any]]:
    if not isinstance(rows, list) or not rows:
        raise SweepRankError("nonempty complete candidate queue required")
    ids: set[str] = set()
    ranks: set[int] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise SweepRankError("candidate must be an object")
        mid, rank = row.get("match_id"), row.get("step0_capacity_queue_rank")
        if (not isinstance(mid, str) or not mid.strip() or mid.upper().startswith("DISCOVERY-")
                or mid in ids):
            raise SweepRankError("candidate missing canonical unique fixture ID")
        if type(rank) is not int or rank < 1 or rank in ranks:
            raise SweepRankError("original Step0 queue rank invalid/duplicate")
        if row.get("operational_viability_grade") not in ("A", "B"):
            raise SweepRankError("candidate lacks source-evidenced A/B operational grade")
        if row.get("final_step0_disposition", row.get("disposition")) != (
                "ADMITTED_TO_C" if rank <= 8 else "OPERATIONAL_CAPACITY_DEFERRED"):
            raise SweepRankError("candidate disposition differs from unchanged Step0 budget")
        ids.add(mid)
        ranks.add(rank)
    if ranks != set(range(1, len(rows) + 1)):
        raise SweepRankError("queue ranks not contiguous: never renumber partially discovered matches")
    return sorted(rows, key=lambda row: row["step0_capacity_queue_rank"])


def prepare(payload: dict[str, Any]) -> dict[str, Any]:
    """Preliminary research scheduler; NO official /rank authority."""
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise SweepRankError("expected football-sweep-rank-v3")
    if payload.get("run_status") != "RUNNING":
        raise SweepRankError("only the currently RUNNING sweep may stage prospective research")
    if payload.get("source_acquisition_state") != "ACQUIRED":
        raise SweepRankError("source acquisition not completed")
    run_id, source_hash = payload.get("run_id"), payload.get("source_payload_hash")
    if not isinstance(run_id, str) or not run_id.startswith("SWEEP-"):
        raise SweepRankError("stable run ID missing")
    if not isinstance(source_hash, str) or len(source_hash) < 8:
        raise SweepRankError("frozen source seed hash missing")
    now = _utc(payload.get("at_utc"), "at_utc")
    start = _utc(payload.get("window_start_utc"), "window_start_utc")
    end = _utc(payload.get("window_end_utc"), "window_end_utc")
    if not start <= now < end:
        raise SweepRankError("research timestamp outside frozen sweep window")
    queue = _queue(payload.get("candidates"))
    research_rows = []
    for row in queue:
        mid = row["match_id"]
        ko = _utc(row.get("fixture_kickoff_utc"), f"{mid}.fixture_kickoff_utc")
        if not _https(row.get("fixture_source_url")):
            raise SweepRankError(f"{mid}: actual fixture source URL needed")
        if not start <= ko < end:
            raise SweepRankError(f"{mid}: kickoff outside frozen source window")
        if row.get("fixture_status") not in {
            "PREMATCH_CONFIRMED", "STARTED", "POSTPONED", "CANCELLED", "FINISHED",
        }:
            raise SweepRankError(f"{mid}: verified fixture status required")
        status_observed = _utc(row.get("fixture_status_observed_at_utc"),
                               f"{mid}.fixture_status_observed_at_utc")
        if not now - timedelta(minutes=20) <= status_observed <= now:
            raise SweepRankError(f"{mid}: stale or future fixture status observation")
        research_rows.append({
            "match_id": mid,
            "queue_rank": row["step0_capacity_queue_rank"],
            "operational_grade": row["operational_viability_grade"],
            "fixture_status": row["fixture_status"],
            "kickoff_utc": ko.isoformat(),
            "football_evidence": row.get("football_evidence"),
            "country": row.get("country"),
            "competition_name": row.get("competition_name"),
            **({"researched_kickoff_evidence": row["researched_kickoff_evidence"]}
               if "researched_kickoff_evidence" in row else {}),
        })
    screening = run_prescreen({
        "schema_version": "football-goal-route-prescreen-v1",
        "run_id": run_id,
        "source_payload_hash": source_hash,
        "screen_at_utc": now.isoformat(),
        "candidates": research_rows,
    })
    order = screening["manifest"]["ordered_eligible_match_ids"]
    blocking = payload.get("coverage_blockers")
    if not isinstance(blocking, list) or any(not isinstance(x, str) or not x.strip() for x in blocking):
        raise SweepRankError("coverage_blockers must be explicit list (may be empty)")
    preview = {
        "schema_version": SCHEMA,
        "status": "FOOTBALL_RESEARCH_PREPARED_UNOFFICIAL",
        "run_id": run_id,
        "source_payload_hash": source_hash,
        "research_at_utc": now.isoformat(),
        "research_ready_count": len(order),
        "source_backed_queue_count": len(queue),
        "source_backed_fixtures": [{
            "match_id": row["match_id"],
            "fixture_kickoff_utc": _utc(row["fixture_kickoff_utc"], "fixture kickoff").isoformat(),
            "fixture_status": row["fixture_status"],
            "fixture_source_url": row["fixture_source_url"],
        } for row in queue],
        "initial_wave": order[:FIRST_RESEARCH_WAVE],
        "standard_research_order": order[:STANDARD_RESEARCH],
        "adaptive_ceiling": min(MAX_RESEARCH, len(order)),
        "remaining_candidates": order[STANDARD_RESEARCH:MAX_RESEARCH],
        "closed": [x["match_id"] for x in screening["manifest"]["original_rows"] if x["screen_status"] == "CLOSED"],
        "coverage_blockers": list(blocking),
        "goal_first_manifest": screening["manifest"],
        "goal_first_fingerprint": screening["manifest"]["screen_fingerprint"],
        "no_bet": True,
        "official_rank_authorized": False,
        "requires_final_step0_zip": True,
    }
    preview["preview_sha256"] = _hash(preview)
    return preview


def preview_board(
    preview: dict[str, Any], c: dict[str, Any], c2: dict[str, Any], *, at_utc: str,
) -> dict[str, Any]:
    """Research-only C+C2 execution from genuine early source-backed fixtures.

    This can never be published or converted to an executable C bet.
    When Step0 cannot be sealed, no official rank/ledger is created.
    """
    if (not isinstance(preview, dict)
            or preview.get("status") != "FOOTBALL_RESEARCH_PREPARED_UNOFFICIAL"
            or preview.get("official_rank_authorized") is not False
            or preview.get("preview_sha256") != _hash({k: v for k, v in preview.items() if k != "preview_sha256"})):
        raise SweepRankError("unaltered source-backed unofficial preview required")
    now = _utc(at_utc, "at_utc")
    prepared_at = _utc(preview.get("research_at_utc"), "research_at_utc")
    if not prepared_at <= now <= prepared_at + timedelta(minutes=20):
        raise SweepRankError("unofficial research preview is stale")
    backed = {row["match_id"]: row for row in preview["source_backed_fixtures"]}
    allowed = set(preview.get("standard_research_order", []))
    allowed.update(preview.get("remaining_candidates", []))
    if not allowed:
        raise SweepRankError("no current prematch fixtures available for research")
    for model_payload in (c, c2):
        matches = model_payload.get("matches") if isinstance(model_payload, dict) else None
        if not isinstance(matches, list) or not 1 <= len(matches) <= MAX_RESEARCH:
            raise SweepRankError("unofficial model research requires real 1..20 fixtures")
        for row in matches:
            mid = row.get("match_id") if isinstance(row, dict) else None
            if mid not in allowed or mid not in backed:
                raise SweepRankError("unofficial model fixture not in current source-backed research set")
            original_ko = _utc(backed[mid]["fixture_kickoff_utc"], "backed fixture kickoff")
            if _utc(row.get("kickoff_ict"), "model fixture kickoff") != original_ko:
                raise SweepRankError("unofficial model rewrote original backed fixture KO")
            if now >= original_ko or backed[mid]["fixture_status"] != "PREMATCH_CONFIRMED":
                raise SweepRankError("unofficial model research is no longer prematch")
    pair = run_board_pair(c, c2)
    return {
        "schema_version": SCHEMA,
        "status": "C_C2_FOOTBALL_RESEARCH_UNOFFICIAL_NO_BET",
        "run_id": preview["run_id"],
        "source_payload_hash": preview["source_payload_hash"],
        "prepared_preview_sha256": preview["preview_sha256"],
        "board_pair": pair,
        "publication_authority": "NONE",
        "official_c_lane_authorized": False,
        "bet_authorized": False,
        "airtable_write_authorized": False,
        "requires_complete_step0_zip_to_rank": True,
    }


def seal(handoff_file: Path, run_proof_file: Path, text_file: Path, output_zip: Path) -> dict[str, Any]:
    """Atomic final package: all original Step0 + readback requirements apply."""
    handoff = json.loads(handoff_file.read_text(encoding="utf-8"))
    result = package_step0(handoff_file, text_file, run_proof_file, output_zip)
    return {
        "schema_version": SCHEMA,
        "status": "STEP0_OFFICIAL_ZIP_VERIFIED",
        "run_id": handoff["run_id"],
        "source_payload_hash": handoff.get("source_payload_hash"),
        "zip_sha256": result["sha256"],
        "zip_path": str(output_zip),
        "admitted": result["admitted"],
        "no_model_decision": True,
    }


def _open_official_zip(archive_path: Path, expected_sha: str) -> dict[str, Any]:
    if not isinstance(expected_sha, str) or len(expected_sha) != 64:
        raise SweepRankError("independent official ZIP SHA256 required")
    content = archive_path.read_bytes()
    if hashlib.sha256(content).hexdigest() != expected_sha:
        raise SweepRankError("official ZIP SHA256 mismatch: never reconstruct or repackage")
    try:
        with zipfile.ZipFile(archive_path) as z:
            names = z.namelist()
            if names.count("STEP0_HANDOFF.json") != 1 or z.testzip() is not None:
                raise SweepRankError("official ZIP invalid or missing one STEP0_HANDOFF.json")
            handoff = json.loads(z.read("STEP0_HANDOFF.json"))
    except (zipfile.BadZipFile, RuntimeError) as exc:
        raise SweepRankError("official ZIP invalid") from exc
    validate_step0_handoff(handoff, consumer="rank")
    return handoff


def plan_rank(
    official_zip: Path,
    expected_zip_sha256: str,
    sweep_readback: dict[str, Any],
    status_evidence: dict[str, Any],
    *,
    at_utc: str,
) -> dict[str, Any]:
    """One full-queue source-attested goal screen, not a prediction."""
    handoff = _open_official_zip(official_zip, expected_zip_sha256)
    if (sweep_readback.get("run_id") != handoff.get("run_id")
            or sweep_readback.get("run_status") != "COMPLETE"
            or sweep_readback.get("source_payload_hash") != handoff.get("source_payload_hash")
            or sweep_readback.get("official_zip_sha256") != expected_zip_sha256):
        raise SweepRankError("rank plan requires original complete Sweep Runs readback")
    queue = _queue(handoff.get("capacity_queue"))
    if not isinstance(status_evidence, dict) or set(status_evidence) != {r["match_id"] for r in queue}:
        raise SweepRankError("fresh status observation required for every frozen A/B fixture")
    now = _utc(at_utc, "at_utc")
    candidates = []
    for row in queue:
        mid = row["match_id"]
        proof = status_evidence[mid]
        if not isinstance(proof, dict) or not _https(proof.get("source_url")):
            raise SweepRankError(f"{mid}: source-backed current status proof required")
        observed = _utc(proof.get("observed_at_utc"), f"{mid}.observed_at_utc")
        if not now - timedelta(minutes=20) <= observed <= now:
            raise SweepRankError(f"{mid}: stale/future status observation")
        if proof.get("fixture_status") not in {
            "PREMATCH_CONFIRMED", "STARTED", "FINISHED", "POSTPONED", "CANCELLED",
        }:
            raise SweepRankError(f"{mid}: real match status missing")
        data = {
            "match_id": mid, "queue_rank": row["step0_capacity_queue_rank"],
            "operational_grade": row["operational_viability_grade"],
            "fixture_status": proof["fixture_status"],
            "kickoff_utc": row.get("fixture_kickoff_utc"),
            "football_evidence": proof.get("football_evidence"),
            "country": row.get("country"),
            "competition_name": row.get("competition_name"),
        }
        if "researched_kickoff_evidence" in proof:
            data["researched_kickoff_evidence"] = proof["researched_kickoff_evidence"]
        candidates.append(data)
    screen = run_prescreen({
        "schema_version": "football-goal-route-prescreen-v1",
        "run_id": handoff["run_id"],
        "source_payload_hash": handoff["source_payload_hash"],
        "screen_at_utc": now.isoformat(),
        "candidates": candidates,
    })
    answer = {
        "schema_version": SCHEMA,
        "status": "FROZEN_GOAL_FIRST_RESEARCH_PLAN",
        "run_id": handoff["run_id"],
        "source_payload_hash": handoff["source_payload_hash"],
        "official_zip_sha256": expected_zip_sha256,
        "screen_at_utc": now.isoformat(),
        "ordered_eligible_match_ids": screen["manifest"]["ordered_eligible_match_ids"],
        "closed_ids": [r["match_id"] for r in screen["manifest"]["original_rows"]
                       if r["screen_status"] == "CLOSED"],
        "initial_research_ids": screen["initial_research_match_ids"],
        "goal_first_manifest": screen["manifest"],
        "research_count_ceiling": min(MAX_RESEARCH, len(screen["manifest"]["ordered_eligible_match_ids"])),
        "price_not_required": True,
    }
    answer["plan_sha256"] = _hash(answer)
    return answer


def _verify_research_plan(
    plan: dict[str, Any], handoff: dict[str, Any], sha: str,
    now: datetime, ranked: set[str], unranked_reasons: dict[str, str],
) -> None:
    if (not isinstance(plan, dict) or plan.get("status") != "FROZEN_GOAL_FIRST_RESEARCH_PLAN"
            or plan.get("run_id") != handoff.get("run_id")
            or plan.get("source_payload_hash") != handoff.get("source_payload_hash")
            or plan.get("official_zip_sha256") != sha
            or plan.get("plan_sha256") != _hash({k: v for k, v in plan.items() if k != "plan_sha256"})):
        raise SweepRankError("frozen rank plan missing, drifted or not bound to official ZIP")
    at = _utc(plan.get("screen_at_utc"), "screen_at_utc")
    if not at <= now <= at + timedelta(minutes=30):
        raise SweepRankError("rank plan stale; refresh current fixture status before research")
    order = plan.get("ordered_eligible_match_ids")
    closed = plan.get("closed_ids")
    if (not isinstance(order, list) or len(order) != len(set(order))
            or not isinstance(closed, list) or len(closed) != len(set(closed))
            or set(order) & set(closed)):
        raise SweepRankError("invalid frozen goal-first status cohorts")
    ids = {r["match_id"] for r in _queue(handoff["capacity_queue"])}
    if set(order) | set(closed) != ids or not ranked.issubset(order):
        raise SweepRankError("ranked fixtures diverge from frozen eligible goal screen")
    last = max((i for i, mid in enumerate(order) if mid in ranked), default=-1)
    for mid in order[:last]:
        if mid not in ranked and unranked_reasons[mid] not in {
                "MISSING_FOOTBALL_EVIDENCE", "PREMATCH_WINDOW_CLOSED"}:
            raise SweepRankError(f"{mid}: earlier goal-first research skipped without valid source reason")
    for mid in closed:
        if unranked_reasons[mid] != "PREMATCH_WINDOW_CLOSED":
            raise SweepRankError(f"{mid}: non-prematch fixture must remain closed")


def execute_rank(
    official_zip: Path,
    expected_zip_sha256: str,
    sweep_readback: dict[str, Any],
    c: dict[str, Any],
    c2: dict[str, Any],
    unranked_reasons: dict[str, str],
    *,
    at_utc: str,
    research_plan: dict[str, Any],
    fixture_evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    handoff = _open_official_zip(official_zip, expected_zip_sha256)
    run_id = handoff.get("run_id")
    source_hash = handoff.get("source_payload_hash")
    if not isinstance(sweep_readback, dict) or any((
        sweep_readback.get("run_id") != run_id,
        sweep_readback.get("run_status") != "COMPLETE",
        sweep_readback.get("source_payload_hash") != source_hash,
        sweep_readback.get("official_zip_sha256") != expected_zip_sha256,
    )):
        raise SweepRankError("Sweep Runs independent COMPLETE readback disagrees with sealed ZIP")
    now = _utc(at_utc, "at_utc")
    queue = _queue(handoff.get("capacity_queue"))
    if len(queue) > 0 and any(row.get("final_step0_disposition") not in
        {"ADMITTED_TO_C", "OPERATIONAL_CAPACITY_DEFERRED"} for row in queue):
        raise SweepRankError("frozen queue contains non-Work fixture")
    pair_input_ids = [row.get("match_id") for row in c.get("matches", [])]
    if not pair_input_ids or len(pair_input_ids) > MAX_RESEARCH:
        raise SweepRankError("ranking requires 1..20 genuinely researched matches")
    if len(pair_input_ids) != len(set(pair_input_ids)):
        raise SweepRankError("duplicate research fixture")
    frozen = {row["match_id"]: row for row in queue}
    if not set(pair_input_ids).issubset(frozen):
        raise SweepRankError("C rank includes fixture outside frozen A/B Work queue")
    if not isinstance(unranked_reasons, dict) or set(unranked_reasons) != set(frozen) - set(pair_input_ids):
        raise SweepRankError("explicit real reason required for every unranked A/B fixture")
    if any(reason not in UNRANKED_REASONS for reason in unranked_reasons.values()):
        raise SweepRankError("invalid unranked reason; unresearched fixture is not model PASS")
    if handoff.get("strict_intake_policy") == "LEAGUE_CHANNEL_FIRST_V1":
        if not isinstance(fixture_evidence, dict) or set(fixture_evidence) != set(pair_input_ids):
            raise SweepRankError("Step1 real league-first football evidence required for every ranked fixture")
        for mid in pair_input_ids:
            evidence = fixture_evidence[mid]
            if not isinstance(evidence, dict):
                raise SweepRankError(f"{mid}: actual Step1 football evidence object missing")
            actual_frozen = evidence.get("frozen_step0_candidate")
            if actual_frozen != frozen[mid]:
                raise SweepRankError(f"{mid}: frozen Step0 candidate evidence mismatch")
            confirmed = validate_step1_fixture_evidence(evidence)
            if confirmed.get("model_execution_authorized") is not True:
                raise SweepRankError(f"{mid}: Step1 football evidence not authorized")
    # Same freeze is checked again by the pair engine. This additional check
    # prevents the model from processing a fixture after it had kicked off.
    for payload in (c, c2):
        for row in payload.get("matches", []):
            mid = row.get("match_id")
            if mid not in frozen:
                raise SweepRankError("model row not present in source queue")
            if _utc(row.get("kickoff_ict"), f"{mid}.model_kickoff_ict") != _utc(
                frozen[mid].get("fixture_kickoff_utc"), f"{mid}.frozen_kickoff"
            ):
                raise SweepRankError(f"{mid}: Step1 changed frozen fixture KO")
            if now >= _utc(row["kickoff_ict"], f"{mid}.kickoff_ict"):
                raise SweepRankError(f"{mid}: cannot create retrospective prematch rank")
    _verify_research_plan(research_plan, handoff, expected_zip_sha256, now,
                          set(pair_input_ids), unranked_reasons)
    pair = run_board_pair(c, c2)
    ranked = set(pair_input_ids)
    for result in pair["results"].values():
        if set(row["match_id"] for row in result["matches"]) != ranked:
            raise SweepRankError("executed model board dropped/added fixture")
    counts = {lane: sum(
        row["follow_lane"] == lane for row in pair["results"]["c"]["matches"]
    ) for lane in ("FOLLOW", "RESERVE", "STOP")}
    proof = {
        "schema_version": SCHEMA,
        "run_id": run_id, "source_payload_hash": source_hash,
        "official_zip_sha256": expected_zip_sha256,
        "assessed_at_utc": now.isoformat(),
        "rank_plan_sha256": research_plan["plan_sha256"],
        "board_pair": pair,
        "frozen_ab_queue": [
            {"match_id": row["match_id"], "step0_capacity_queue_rank": row["step0_capacity_queue_rank"]}
            for row in queue
        ],
        "unranked_reasons": dict(unranked_reasons),
        "counts": counts,
    }
    return {
        "schema_version": SCHEMA,
        "status": "C_C2_EXECUTED_AWAITING_INDEPENDENT_AIRTABLE_READBACK",
        "execution": proof,
        "execution_sha256": _hash(proof),
        "models_executed": ["c", "c2"],
        "no_bet": True,
        "official_publication_authorized": False,
    }


def publish_rank(execution_receipt: dict[str, Any], readback: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(execution_receipt, dict) or execution_receipt.get("status") != "C_C2_EXECUTED_AWAITING_INDEPENDENT_AIRTABLE_READBACK":
        raise SweepRankError("exact executed board receipt required")
    proof = execution_receipt.get("execution")
    if not isinstance(proof, dict) or _hash(proof) != execution_receipt.get("execution_sha256"):
        raise SweepRankError("board execution digest mismatch")
    if not isinstance(readback, dict):
        raise SweepRankError("independent Airtable readback required")
    if (readback.get("board_pair") != proof["board_pair"]
            or readback.get("run_id") != proof["run_id"]
            or readback.get("source_payload_hash") != proof["source_payload_hash"]
            or readback.get("frozen_ab_queue") != proof["frozen_ab_queue"]
            or readback.get("unranked_reasons") != proof["unranked_reasons"]):
        raise SweepRankError("independent readback does not describe the same executed source/board")
    status = readback.get("terminal_status")
    if (not isinstance(status, dict) or status.get("follow_count") != proof["counts"]["FOLLOW"]
            or status.get("reserve_count") != proof["counts"]["RESERVE"]
            or status.get("stop_count") != proof["counts"]["STOP"]):
        raise SweepRankError("terminal status and C official lane counts disagree")
    verified = validate_rank_readback(readback)
    return {
        "schema_version": SCHEMA,
        "status": "C_C2_RANKED_READBACK_VERIFIED",
        "run_id": proof["run_id"],
        "source_payload_hash": proof["source_payload_hash"],
        "execution_sha256": execution_receipt["execution_sha256"],
        "readback_status": verified["status"],
        "ranked_count": verified["ranked_count"],
        "unranked_count": verified["unranked_count"],
        "official_c_lane_counts": proof["counts"],
        "c2_shadow_only": True,
        "website_published": False,
        "actual_bet_recorded": False,
    }


def main() -> int:
    # Current production Stage 0/1 is decommissioned. Pure functions below
    # remain for immutable historical regression/audit, not user execution.
    from sweep_rank_retired import stop_retired_cli
    return stop_retired_cli("sweep-rank-v3-coordinator")
    p = argparse.ArgumentParser(description="Unified football v2 Step0 / Step1 coordinator")
    sub = p.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare")
    prepare_parser.add_argument("--input", required=True)
    pb = sub.add_parser("preview-board")
    for opt in ("preview", "c", "c2", "at"):
        pb.add_argument("--" + opt, required=True)
    sealed = sub.add_parser("seal")
    for opt in ("handoff", "run-proof", "text", "output"):
        sealed.add_argument("--" + opt, required=True)
    plan = sub.add_parser("plan")
    for opt in ("zip", "sha256", "sweep-readback", "statuses", "at"):
        plan.add_argument("--" + opt, required=True)
    rank = sub.add_parser("rank")
    for opt in ("zip", "sha256", "sweep-readback", "c", "c2", "unranked", "plan", "at"):
        rank.add_argument("--" + opt, required=True)
    rank.add_argument("--fixture-evidence", help="Required for league-first fixture research; current sourced evidence")
    pub = sub.add_parser("publish")
    pub.add_argument("--execution", required=True)
    pub.add_argument("--readback", required=True)
    args = p.parse_args()
    try:
        if args.command == "prepare":
            result = prepare(json.loads(Path(args.input).read_text(encoding="utf-8")))
        elif args.command == "preview-board":
            result = preview_board(
                json.loads(Path(args.preview).read_text(encoding="utf-8")),
                json.loads(Path(args.c).read_text(encoding="utf-8")),
                json.loads(Path(args.c2).read_text(encoding="utf-8")),
                at_utc=args.at,
            )
        elif args.command == "seal":
            result = seal(Path(args.handoff), Path(args.run_proof), Path(args.text), Path(args.output))
        elif args.command == "plan":
            result = plan_rank(
                Path(args.zip), args.sha256,
                json.loads(Path(args.sweep_readback).read_text(encoding="utf-8")),
                json.loads(Path(args.statuses).read_text(encoding="utf-8")),
                at_utc=args.at,
            )
        elif args.command == "rank":
            result = execute_rank(
                Path(args.zip), args.sha256,
                json.loads(Path(args.sweep_readback).read_text(encoding="utf-8")),
                json.loads(Path(args.c).read_text(encoding="utf-8")),
                json.loads(Path(args.c2).read_text(encoding="utf-8")),
                json.loads(Path(args.unranked).read_text(encoding="utf-8")),
                at_utc=args.at,
                research_plan=json.loads(Path(args.plan).read_text(encoding="utf-8")),
                fixture_evidence=(json.loads(Path(args.fixture_evidence).read_text(encoding="utf-8"))
                                  if args.fixture_evidence else None),
            )
        else:
            result = publish_rank(
                json.loads(Path(args.execution).read_text(encoding="utf-8")),
                json.loads(Path(args.readback).read_text(encoding="utf-8")),
            )
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile, json.JSONDecodeError) as exc:
        print(json.dumps({
            "schema_version": SCHEMA,
            "status": "SWEEP_RANK_GATE_BLOCKED",
            "stage": args.command,
            "error": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
