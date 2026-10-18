"""Executable Work fallback: full date evidence -> team research -> native V4.

No model logic lives here. All admission decisions belong to stage.sweep.
Provider failures and unsupported channel/format evidence remain checkpointed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from league_registry import classify
from source_completeness import required_surface_keys
from stage import sweep
from work_source_acquisition import fetch, parse_request

FAMILY = "LiveScore public date API"
DATE_URL = "https://prod-public-api.livescore.com/v1/api/app/date/soccer/{day}/{offset}?MD=1&countryCode=US&locale=en"
TEAM_URL = "https://prod-cdn-team-api.lsmedia1.com/v1/api/app/team/{team}/details?locale=en"


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def stamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


CHECKPOINT_SCHEMA = "football-v4-sweep-research-checkpoint-v2"
RESOLVED_RESEARCH = {"COMPLETE", "EVIDENCE_LIMITED", "STATUS_EXCLUDED"}
STATIC_EVIDENCE_GAPS = {
    "PROVIDER_TEAM_ID_MAPPING_REQUIRED",
    "CURRENT_MECHANISM_STAT_NEWS_CHANNEL_PROOF_REQUIRED",
}


def _resolved(state):
    return isinstance(state, dict) and state.get("research_disposition") in RESOLVED_RESEARCH


def _finish_research_state(state):
    reasons = list(dict.fromkeys(state.get("pending_reasons") or []))
    state["pending_reasons"] = reasons
    if not reasons:
        state["research_disposition"] = "COMPLETE"
        return
    static = all(
        reason in STATIC_EVIDENCE_GAPS
        or reason.endswith("_COMPETITIVE_HISTORY_UNDER_FOUR")
        for reason in reasons
    )
    attempts = int(state.get("attempt_count") or 1)
    if static or attempts >= 2:
        state["research_disposition"] = "EVIDENCE_LIMITED"
        if attempts >= 2 and not static:
            state["retry_exhausted"] = True
    else:
        state["research_disposition"] = "RESEARCH_PENDING"


def _resume_queue(checkpoint):
    order = checkpoint.get("research_order") or []
    states = checkpoint.get("fixtures") or {}
    return [mid for mid in order if not _resolved(states.get(mid))]


def event_time(event, surface_offset_hours=0):
    # LiveScore returns Esd in the timezone requested by the date endpoint.
    # Normalize ICT and UTC views to one instant before merging date surfaces.
    source_tz = timezone(timedelta(hours=surface_offset_hours))
    return datetime.strptime(str(event["Esd"]), "%Y%m%d%H%M%S").replace(
        tzinfo=source_tz
    ).astimezone(timezone.utc).isoformat()


def event_identity(event):
    return tuple(str(event[side][0]["ID"]) for side in ("T1", "T2"))


def event_status(event):
    status = str(event.get("Eps", "")).upper()
    if status == "NS" and event.get("Esid") == 1:
        return "PREMATCH_CONFIRMED"
    if status in {"FT", "AET", "AP"}:
        return "FINISHED"
    if status in {"POSTP", "POSTPONED", "PST"}:
        return "POSTPONED"
    if status in {"CANC", "CANCELLED", "ABANDONED", "AWD"}:
        return "CANCELLED"
    if status in {"HT", "ET", "BT", "PEN"} or re.fullmatch(r"\d+(?:\+\d+)?'?", status):
        return "STARTED"
    # Never silently turn unknown provider codes into a confirmed fixture.
    return "UNKNOWN_PROVIDER_STATUS"


def senior(stage):
    label = stage["Snm"] + " " + (stage.get("Cnm") or stage.get("Csnm") or "")
    if "uefa youth league" in label.lower():
        return True
    if any(x in label.lower() for x in ("premier league 2", "primavera")):
        return False
    # Team names are intentionally absent: a U23 team can play an adult league.
    return not re.search(r"\b(?:u[ -]?(?:1[5-9]|2[0-3])|under[ -]?(?:1[5-9]|2[0-3])|youth)\b", label, re.I)


def competition_kind(stage):
    name = stage["Snm"].lower()
    country = (stage.get("Cnm") or stage.get("Csnm") or "").lower()
    if "uefa youth league" in name:
        return "YOUTH_CONTINENTAL"
    if country in {"international", "world", "europe", "asia", "africa", "south america", "north america", "oceania"}:
        if any(x in name for x in ("champions league", "europa league", "conference league", "libertadores", "sudamericana")):
            return "CONTINENTAL"
        # Generic international labels must not manufacture protected status.
        return "UNVERIFIED"
    if any(x in name for x in ("cup", "copa", "trophy", "pokal", "coupe", "beker")):
        return "DOMESTIC_CUP"
    return "DOMESTIC_LEAGUE"


def stage_blocks(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("Stages"), list):
        raise ValueError("provider date response lacks full Stages array")
    # The date endpoint is a single full-array surface. Stop on contract drift.
    for key in payload:
        if any(word in key.lower() for word in ("pagination", "nextpage", "hasmore", "cursor")):
            raise ValueError("provider pagination contract changed: " + key)
    seen = set()
    result = []
    for block in payload["Stages"]:
        if not isinstance(block.get("Events"), list) or not block.get("Snm"):
            raise ValueError("malformed competition block")
        if not (block.get("Cnm") or block.get("Csnm")):
            raise ValueError("competition country absent")
        if not senior(block):
            continue
        for event in block["Events"]:
            mid = str(event["Eid"])
            if not mid or mid == "None" or mid in seen:
                raise ValueError("missing/duplicate provider event ID")
            seen.add(mid)
            event_identity(event)
            event_time(event)
        result.append(block)
    return result


class Evidence:
    def __init__(self, output):
        self.output = output
        self.index = []

    def get(self, url, name):
        raw, observed = fetch(url)
        payload = json.loads(raw)
        path = self.output / "raw" / (name + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        # An invocation writes into a fresh output directory; no evidence overwrite.
        path.write_bytes(raw)
        item = {"source_url": url, "observed_at_utc": observed,
                "file": str(path.relative_to(self.output)), "sha256": digest(path)}
        self.index.append(item)
        save(self.output / "provenance.json", self.index)
        return payload, item


def acquire(request, evidence):
    start, end, _ = parse_request(request)
    start, end = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    keys = required_surface_keys(start.isoformat(), end.isoformat())
    fixtures, identities, surfaces = {}, {}, []
    for key in keys:
        basis, day = key.split(":")
        offset = 7 if basis == "ICT" else 0
        url = DATE_URL.format(day=day.replace("-", ""), offset=offset)
        payload, proof = evidence.get(url, key.replace(":", "-"))
        blocks, ids = [], []
        for block in stage_blocks(payload):
            mids = [str(e["Eid"]) for e in block["Events"]]
            blocks.append({"country": block.get("Cnm") or block["Csnm"], "competition": block["Snm"],
                           "provider_fixture_count": len(mids), "extracted_fixture_ids": mids})
            ids.extend(mids)
            for event in block["Events"]:
                mid = str(event["Eid"])
                identity = event_identity(event)
                if mid in identities and identities[mid] != identity:
                    raise ValueError("conflicting date-surface team identity: " + mid)
                if mid in fixtures and fixtures[mid]["kickoff_utc"] != event_time(event, offset):
                    raise ValueError("conflicting date-surface kickoff: " + mid)
                identities[mid] = identity
                fixtures[mid] = {"match_id": mid, "country": block.get("Cnm") or block["Csnm"],
                                 "competition": block["Snm"], "competition_kind": competition_kind(block),
                                 "is_friendly": any(x in block["Snm"].lower() for x in ("friendly", "friendlies")),
                                 "home": event["T1"][0]["Nm"], "away": event["T2"][0]["Nm"],
                                 "kickoff_utc": event_time(event, offset), "fixture_status": event_status(event),
                                 "source_url": url, "observed_at_utc": proof["observed_at_utc"],
                                 "provider_team_ids": list(identity)}
        surfaces.append({"surface_key": key, "source_url": url, "observed_at_utc": proof["observed_at_utc"],
                         "pagination_complete": True, "provider_page_count": 1, "pages_fetched": [1],
                         "provider_senior_fixture_count": len(ids), "extracted_fixture_ids": ids,
                         "provider_senior_competition_block_count": len(blocks), "competition_blocks": blocks})
    terminal_start = max(start, end - timedelta(hours=6))
    terminal_ids, terminal_proofs = set(), []
    for key in required_surface_keys(terminal_start.isoformat(), end.isoformat()):
        if not key.startswith("UTC:"):
            continue
        day = key.split(":")[1]
        url = DATE_URL.format(day=day.replace("-", ""), offset=0)
        payload, proof = evidence.get(url, "terminal-" + day)
        terminal_proofs.append(proof)
        for block in stage_blocks(payload):
            for event in block["Events"]:
                mid = str(event["Eid"])
                if terminal_start <= stamp(event_time(event)) < end:
                    terminal_ids.add(mid)
                    if mid in fixtures and (event_identity(event) != identities[mid] or event_time(event) != fixtures[mid]["kickoff_utc"]):
                        raise ValueError("terminal identity/kickoff changed: " + mid)
                if mid in fixtures:
                    fixtures[mid].update(fixture_status=event_status(event), observed_at_utc=proof["observed_at_utc"], source_url=url)
    now = utcnow()
    return {"schema_version": "football-stages-v4", "run_id": request["run_id"],
            "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
            "source_family": FAMILY, "source_url": surfaces[0]["source_url"],
            "source_observed_at_utc": max(x["observed_at_utc"] for x in surfaces),
            "fixtures": list(fixtures.values()),
            "source_completeness_manifest": {
                "schema_version": "football-v4-source-completeness-v2", "acquisition_mode": "DATE_SURFACE_BATCH_V2",
                "league_query_mode": "DATE_SURFACE_ONLY", "registry_prefilter_applied": False,
                "scope_policy": "ALL_SOURCE_VISIBLE_SENIOR_FOOTBALL_BLOCKS", "extraction_complete": True,
                "provider_family": FAMILY, "window_start_utc": start.isoformat(), "window_end_utc": end.isoformat(),
                "checked_at_utc": now, "required_surface_keys": keys, "date_surfaces": surfaces,
                "terminal_sentinel": {"interval_start_utc": terminal_start.isoformat(), "interval_end_utc": end.isoformat(),
                    "checked_at_utc": max(x["observed_at_utc"] for x in terminal_proofs),
                    "complete": True, "independent_refetch": True,
                    "source_urls": [x["source_url"] for x in terminal_proofs],
                    "provider_senior_fixture_count": len(terminal_ids), "extracted_fixture_ids": sorted(terminal_ids)}}}


def competitive_history(payload, team, now):
    if str(payload.get("ID")) != team or not isinstance(payload.get("Stages"), list):
        raise ValueError("team feed identity/schema mismatch")
    results = {}
    for block in payload["Stages"]:
        competition = block.get("Snm", "")
        if not competition or any(x in competition.lower() for x in ("friendly", "friendlies", "testimonial")):
            continue
        for event in block.get("Events", []):
            if event.get("Eps") != "FT":
                continue  # Extra-time/penalty totals cannot replace regulation scores.
            identity = event_identity(event)
            if team not in identity:
                raise ValueError("unrelated event in team history")
            kickoff = stamp(event_time(event))
            if not now - timedelta(days=120) <= kickoff <= now - timedelta(hours=2):
                continue
            home = identity[0] == team
            gf, ga = event["Tr1" if home else "Tr2"], event["Tr2" if home else "Tr1"]
            if not re.fullmatch(r"\d+", str(gf)) or not re.fullmatch(r"\d+", str(ga)):
                raise ValueError("invalid final score")
            row = {"event_id": str(event["Eid"]), "kickoff_utc": kickoff.isoformat(),
                   "goals_for": int(gf), "goals_against": int(ga), "competition": competition}
            if row["event_id"] in results and results[row["event_id"]] != row:
                raise ValueError("conflicting historical result")
            results[row["event_id"]] = row
    return sorted(results.values(), key=lambda x: x["kickoff_utc"], reverse=True)[:10]


def research(source, receipt, evidence, checkpoint):
    fixtures = {f["match_id"]: f for f in source["fixtures"]}
    # Native priority, then all remaining research candidates; no fixed cap.
    order = list(dict.fromkeys(receipt.get("priority_research_order", []) + receipt.get("goal_research_order", [])))
    previous_order = checkpoint.get("research_order")
    if previous_order and previous_order != order:
        # A resume may not silently change its research cohort. A newly refreshed
        # source epoch must create a new checkpoint and explicitly remap reusable IDs.
        raise ValueError("RESEARCH_ORDER_CHANGED: new source epoch/remap required")
    checkpoint["research_order"] = order
    checkpoint.setdefault("fixtures", {})
    resolved_before = [mid for mid in order if _resolved(checkpoint["fixtures"].get(mid))]
    unresolved = [mid for mid in order if mid not in resolved_before]
    checkpoint["reused_match_ids"] = resolved_before
    checkpoint["resume_queue"] = unresolved
    feeds = {}
    deadline = time.monotonic() + 20 * 60
    for index, mid in enumerate(unresolved):
        if time.monotonic() >= deadline:
            checkpoint["unfinished_research_order"] = unresolved[index:]
            checkpoint["resume_queue"] = unresolved[index:]
            checkpoint["resource_limit_reason"] = "RESEARCH_TIME_BUDGET_CHECKPOINTED"
            checkpoint["status"] = "RESEARCH_PENDING"
            save(evidence.output / "checkpoint.json", checkpoint)
            break
        fixture = fixtures[mid]
        previous = checkpoint["fixtures"].get(mid) or {}
        state = {
            "pending_reasons": [],
            "attempt_count": int(previous.get("attempt_count") or 0) + 1,
            "last_attempted_at_utc": utcnow(),
        }
        checkpoint["fixtures"][mid] = state
        ids = fixture.get("provider_team_ids", [])
        if len(ids) != 2 or source["source_family"] != FAMILY:
            state["pending_reasons"].append("PROVIDER_TEAM_ID_MAPPING_REQUIRED")
        else:
            histories, checks = dict(fixture.get("football_evidence") or {}), []
            for side, team in zip(("home", "away"), ids):
                team = str(team)
                try:
                    if not team.isdigit():
                        raise ValueError("unsafe provider team ID")
                    if team not in feeds:
                        try:
                            feeds[team] = evidence.get(TEAM_URL.format(team=team), "team-" + team)
                        except Exception as exc:
                            feeds[team] = exc
                    if isinstance(feeds[team], Exception):
                        raise feeds[team]
                    payload, proof = feeds[team]
                    recent = competitive_history(payload, team, stamp(proof["observed_at_utc"]))
                    histories[side] = {"source_url": proof["source_url"], "observed_at_utc": proof["observed_at_utc"], "recent": recent}
                    if len(recent) < 4:
                        state["pending_reasons"].append(side.upper() + "_COMPETITIVE_HISTORY_UNDER_FOUR")
                    matches = [e for b in payload["Stages"] for e in b.get("Events", []) if str(e.get("Eid")) == mid]
                    if len(matches) != 1 or event_identity(matches[0]) != tuple(map(str, ids)) or event_time(matches[0]) != fixture["kickoff_utc"]:
                        raise ValueError("fixture identity/kickoff not reconciled in team feed")
                    checks.append({"team_id": team, "status": event_status(matches[0]), **proof})
                except Exception as exc:
                    state["pending_reasons"].append(side.upper() + ": " + str(exc))
            fixture["football_evidence"] = histories
            state["status_checks"] = checks
            if len(checks) == 2 and checks[0]["status"] == checks[1]["status"]:
                fixture.update(fixture_status=checks[0]["status"], observed_at_utc=max(x["observed_at_utc"] for x in checks))
            else:
                fixture["fixture_status"] = "UNVERIFIED_STATUS_REFRESH"
                state["pending_reasons"].append("BOTH_TEAM_STATUS_REFRESH_NOT_RECONCILED")
            if classify(fixture)["lane"] in {"CONDITIONAL", "PILOT", "DISCOVERY"} and fixture.get("researchability_status") != "VERIFIED":
                state["pending_reasons"].append("CURRENT_MECHANISM_STAT_NEWS_CHANNEL_PROOF_REQUIRED")
                # An advertised hasStats/hasLineups flag is not actual evidence.
        _finish_research_state(state)
        checkpoint["resume_queue"] = _resume_queue(checkpoint)
        checkpoint["completed_research_count"] = sum(
            1 for mid2 in order if _resolved(checkpoint["fixtures"].get(mid2))
        )
        checkpoint["pending_research_count"] = len(checkpoint["resume_queue"])
        # Persist after every fixture. The normal-chat launcher may mirror these
        # durable checkpoints to GitHub in batches of 3-5 fixtures.
        save(evidence.output / "source.json", source)
        save(evidence.output / "checkpoint.json", checkpoint)



def run(request_path, output, source_path=None, resume_from=None):
    if output.exists() and any(output.iterdir()):
        raise ValueError("output must be fresh; preserve previous evidence and resume into a new directory")
    if source_path and resume_from:
        raise ValueError("choose either --source or --resume-from")
    output.mkdir(parents=True, exist_ok=True)
    evidence = Evidence(output)
    checkpoint = {"schema_version": CHECKPOINT_SCHEMA, "status": "RUNNING", "fixtures": {}, "resume_generation": 0}
    save(output / "checkpoint.json", checkpoint)
    try:
        request = json.loads(request_path.read_text())
        start, end, _ = parse_request(request)
        checkpoint["run_id"] = request["run_id"]
        if end <= stamp(utcnow()):
            raise ValueError("REQUEST_WINDOW_EXPIRED: no network acquisition performed")
        if resume_from:
            resume_path = Path(resume_from)
            if resume_path.is_dir():
                resume_path = resume_path / "checkpoint.json"
            previous = json.loads(resume_path.read_text())
            previous_dir = resume_path.parent
            original_path = previous_dir / "original-source.json"
            working_path = previous_dir / "source.json"
            if not original_path.exists() or not working_path.exists():
                raise ValueError("RESUME_EVIDENCE_MISSING: original-source.json and source.json required")
            raw = original_path.read_bytes()
            original_sha = hashlib.sha256(raw).hexdigest()
            if previous.get("original_source_sha256") != original_sha:
                raise ValueError("RESUME_SOURCE_SHA_MISMATCH")
            source = json.loads(working_path.read_text())
            original = json.loads(raw)
            for candidate in (source, original):
                if candidate["run_id"] != request["run_id"] or stamp(candidate["window_start_utc"]) != start or stamp(candidate["window_end_utc"]) != end:
                    raise ValueError("resume request does not match original source")
            (output / "original-source.json").write_bytes(raw)
            checkpoint = json.loads(json.dumps(previous))
            checkpoint.update(
                schema_version=CHECKPOINT_SCHEMA,
                status="RUNNING",
                resume_generation=int(previous.get("resume_generation") or 0) + 1,
                resumed_from=str(resume_path),
                original_source_sha256=original_sha,
            )
            checkpoint.pop("unfinished_research_order", None)
            checkpoint.pop("resource_limit_reason", None)
            save(output / "checkpoint.json", checkpoint)
        elif source_path:
            raw = source_path.read_bytes()
            (output / "original-source.json").write_bytes(raw)
            source = json.loads(raw)
            if source["run_id"] != request["run_id"] or stamp(source["window_start_utc"]) != start or stamp(source["window_end_utc"]) != end:
                raise ValueError("resume request does not match original source")
            checkpoint["original_source_sha256"] = hashlib.sha256(raw).hexdigest()
        else:
            source = acquire(request, evidence)
            save(output / "original-source.json", source)
            checkpoint["original_source_sha256"] = digest(output / "original-source.json")
        save(output / "source.json", source)
        preliminary = sweep(source, now=utcnow())
        save(output / "listing-receipt.json", preliminary)
        # V4_SWEEP_READY is a structural receipt, never an early-return condition.
        research(source, preliminary, evidence, checkpoint)
        receipt = sweep(source, now=utcnow())
        save(output / "v4_sweep_ready.json", receipt)
        pending = [r for r in receipt["source_ledger"] if r["intake_lane"].startswith("PENDING") or r["intake_lane"] == "UNVERIFIED"]
        limited_ids = {
            mid for mid, state in checkpoint.get("fixtures", {}).items()
            if state.get("research_disposition") == "EVIDENCE_LIMITED"
        }
        actionable_pending = [r for r in pending if r.get("match_id") not in limited_ids]
        if checkpoint.get("unfinished_research_order") or actionable_pending or checkpoint.get("resume_queue"):
            research_status = "RESEARCH_PENDING"
        elif pending:
            research_status = "RESEARCH_COMPLETE_WITH_EVIDENCE_LIMITS"
        else:
            research_status = "RESEARCH_COMPLETE"
        checkpoint.update(
            status=research_status,
            native_v4_executed=True,
            pending_rows=actionable_pending,
            evidence_limited_rows=[r for r in pending if r.get("match_id") in limited_ids],
            eligible_count=receipt["eligible_count"],
            pending_research_count=len(checkpoint.get("resume_queue") or []),
        )
        save(output / "checkpoint.json", checkpoint)
        save(output / "rank-handoff.json", {
            "schema_version": "football-v4-rank-handoff-v1", "status": "V4_RANK_HANDOFF_READY",
            "run_id": source["run_id"], "source_run_id": source["run_id"],
            "source_filename": "source.json", "source_file_sha256": digest(output / "source.json"),
            "receipt_filename": "v4_sweep_ready.json", "receipt_integrity_sha256": receipt["integrity_sha256"],
            "research_status": checkpoint["status"], "eligible_count": receipt["eligible_count"],
            "pending_count": len(actionable_pending), "evidence_limited_count": len(pending) - len(actionable_pending),
            "checkpoint_filename": "checkpoint.json",
            "requires_fresh_status_refresh": True, "rank_must_not_reconstruct_source_from_airtable": True})
        return 0
    except Exception as exc:
        checkpoint.update(status="BLOCKED", error=type(exc).__name__ + ": " + str(exc), checked_at_utc=utcnow())
        save(output / "checkpoint.json", checkpoint)
        return 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", type=Path, help="start from an unchanged saved source; no date-surface acquisition")
    parser.add_argument("--resume-from", type=Path, help="previous output directory or checkpoint.json; reuse enriched source and resolved fixture states")
    args = parser.parse_args()
    return run(args.request, args.output, args.source, args.resume_from)


if __name__ == "__main__":
    raise SystemExit(main())
