"""Finalize a normal-chat V4 sweep from one bounded canonical target set.

This backend owns source refresh, provider goal-history collection, native V4
execution, and rank-handoff persistence. It never runs Football C /rank.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import work_sweep


def _save(path: Path, value) -> None:
    work_sweep.save(path, value)


def _targets(path: Path, run_id: str) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("run_id") != run_id or not isinstance(payload.get("targets"), list):
        raise ValueError("target manifest must match run_id and contain targets[]")
    result, seen = [], set()
    for raw in payload["targets"]:
        row = {"match_id": raw} if isinstance(raw, str) else dict(raw)
        mid = str(row.get("match_id") or "")
        if not mid or mid in seen:
            raise ValueError("target match IDs must be unique and non-empty")
        if row.get("researchability_source_url") is not None:
            url = str(row["researchability_source_url"])
            if not url.startswith("https://"):
                raise ValueError("researchability_source_url must be HTTPS")
        seen.add(mid)
        row["match_id"] = mid
        result.append(row)
    if not 1 <= len(result) <= 30:
        raise ValueError("normal sweep target set must contain 1..30 fixtures")
    return result


def run(request_path: Path, targets_path: Path, output: Path) -> int:
    if output.exists() and any(output.iterdir()):
        raise ValueError("output must be fresh")
    output.mkdir(parents=True, exist_ok=True)
    evidence = work_sweep.Evidence(output)

    request = json.loads(request_path.read_text(encoding="utf-8"))
    start, end, _ = work_sweep.parse_request(request)
    if end <= work_sweep.stamp(work_sweep.utcnow()):
        raise ValueError("REQUEST_WINDOW_EXPIRED")

    targets = _targets(targets_path, request["run_id"])
    target_map = {row["match_id"]: row for row in targets}

    # Always refresh the canonical date surfaces immediately before finalization.
    source = work_sweep.acquire(request, evidence)
    original = copy.deepcopy(source)
    _save(output / "original-source.json", original)

    fixtures = {row["match_id"]: row for row in source["fixtures"]}
    missing = sorted(set(target_map) - set(fixtures))
    if missing:
        raise ValueError("TARGET_NOT_ON_CANONICAL_SOURCE: " + ",".join(missing))

    feeds = {}
    states = {}
    now = work_sweep.utcnow()
    for mid, target in target_map.items():
        fixture = fixtures[mid]
        state = {"match_id": mid, "attempted": False, "pending_reasons": []}

        # Do not waste research time or recreate prematch eligibility after start.
        if fixture.get("fixture_status") != "PREMATCH_CONFIRMED":
            state["research_disposition"] = "STATUS_EXCLUDED"
            state["reason"] = "CURRENT_PROVIDER_STATUS_NOT_PREMATCH"
            states[mid] = state
            continue

        if target.get("researchability_source_url"):
            fixture["researchability_status"] = "VERIFIED"
            fixture["researchability_proof"] = {
                "match_id": mid,
                "source_url": target["researchability_source_url"],
                "checked_at_utc": now,
                "current_channels_checked": True,
            }

        ids = fixture.get("provider_team_ids") or []
        if len(ids) != 2:
            state["research_disposition"] = "EVIDENCE_LIMITED"
            state["pending_reasons"].append("PROVIDER_TEAM_ID_MAPPING_REQUIRED")
            states[mid] = state
            continue

        histories, checks = {}, []
        state["attempted"] = True
        for side, team in zip(("home", "away"), ids):
            team = str(team)
            try:
                if not team.isdigit():
                    raise ValueError("unsafe provider team ID")
                if team not in feeds:
                    try:
                        feeds[team] = evidence.get(
                            work_sweep.TEAM_URL.format(team=team), "team-" + team
                        )
                    except Exception as exc:
                        feeds[team] = exc
                if isinstance(feeds[team], Exception):
                    raise feeds[team]
                payload, proof = feeds[team]
                recent = work_sweep.competitive_history(
                    payload, team, work_sweep.stamp(proof["observed_at_utc"])
                )
                histories[side] = {
                    "source_url": proof["source_url"],
                    "observed_at_utc": proof["observed_at_utc"],
                    "recent": recent,
                }
                if len(recent) < 4:
                    state["pending_reasons"].append(
                        side.upper() + "_COMPETITIVE_HISTORY_UNDER_FOUR"
                    )
                matches = [
                    event
                    for block in payload.get("Stages", [])
                    for event in block.get("Events", [])
                    if str(event.get("Eid")) == mid
                ]
                if (
                    len(matches) != 1
                    or work_sweep.event_identity(matches[0]) != tuple(map(str, ids))
                    or work_sweep.event_time(matches[0]) != fixture["kickoff_utc"]
                ):
                    raise ValueError("fixture identity/kickoff not reconciled in team feed")
                checks.append(
                    {
                        "team_id": team,
                        "status": work_sweep.event_status(matches[0]),
                        **proof,
                    }
                )
            except Exception as exc:
                state["pending_reasons"].append(side.upper() + ": " + str(exc))

        fixture["football_evidence"] = histories
        if len(checks) == 2 and checks[0]["status"] == checks[1]["status"]:
            fixture.update(
                fixture_status=checks[0]["status"],
                observed_at_utc=max(x["observed_at_utc"] for x in checks),
            )
        else:
            fixture["fixture_status"] = "UNVERIFIED_STATUS_REFRESH"
            state["pending_reasons"].append("BOTH_TEAM_STATUS_REFRESH_NOT_RECONCILED")

        if state["pending_reasons"]:
            state["research_disposition"] = "EVIDENCE_LIMITED"
        else:
            state["research_disposition"] = "COMPLETE"
        states[mid] = state

    _save(output / "source.json", source)
    receipt = work_sweep.sweep(source, now=work_sweep.utcnow())
    _save(output / "v4_sweep_ready.json", receipt)

    ledger = {row.get("match_id"): row for row in receipt.get("source_ledger", [])}
    eligible = {row.get("match_id") for row in receipt.get("eligible_queue", [])}
    completed, watch, limited, closed = [], [], [], []
    for mid in target_map:
        state = states[mid]
        row = ledger.get(mid) or {}
        if mid in eligible:
            completed.append(mid)
        elif state.get("research_disposition") == "STATUS_EXCLUDED" or row.get("intake_lane") == "CLOSED":
            closed.append(mid)
        elif state.get("research_disposition") == "EVIDENCE_LIMITED":
            limited.append(mid)
        else:
            screen = row.get("goal_screen") or row.get("discovery_screen") or {}
            if screen.get("status") == "WATCH_GOAL_SIGNAL":
                watch.append(mid)
            elif row.get("intake_lane") in {"PENDING_GOAL_RESEARCH"} and screen.get("status") not in {
                "PENDING_GOAL_HISTORY", "PENDING_SOURCE_SCORING_EVIDENCE"
            }:
                watch.append(mid)
            else:
                limited.append(mid)

    terminal = set(completed + watch + limited + closed)
    unresolved = sorted(set(target_map) - terminal)
    if unresolved:
        raise ValueError("FINALIZER_UNRESOLVED_TARGETS: " + ",".join(unresolved))

    source_sha = work_sweep.digest(output / "source.json")
    handoff = {
        "schema_version": "football-v4-rank-handoff-v1",
        "status": "V4_RANK_HANDOFF_READY",
        "run_id": source["run_id"],
        "source_run_id": source["run_id"],
        "source_filename": "source.json",
        "source_file_sha256": source_sha,
        "receipt_filename": "v4_sweep_ready.json",
        "receipt_integrity_sha256": receipt["integrity_sha256"],
        "active_research_complete": True,
        "active_target_count": len(target_map),
        "eligible_target_count": len(completed),
        "watch_target_count": len(watch),
        "evidence_limited_target_count": len(limited),
        "status_excluded_target_count": len(closed),
        "deferred_source_backlog_count": max(
            0, len(receipt.get("goal_research_order", [])) - len(target_map)
        ),
        "requires_fresh_status_refresh": True,
        "rank_must_not_reconstruct_source_from_airtable": True,
    }
    _save(output / "rank-handoff.json", handoff)
    checkpoint = {
        "schema_version": "football-v4-sweep-research-checkpoint-v2",
        "status": "RESEARCH_COMPLETE",
        "run_id": source["run_id"],
        "original_source_sha256": work_sweep.digest(output / "original-source.json"),
        "source_file_sha256": source_sha,
        "native_receipt_integrity_sha256": receipt["integrity_sha256"],
        "target_states": states,
        "eligible_match_ids": completed,
        "watch_match_ids": watch,
        "evidence_limited_match_ids": limited,
        "status_excluded_match_ids": closed,
        "resume_queue": [],
        "rank_handoff_ready": True,
        "native_v4_sweep_ready": True,
    }
    _save(output / "checkpoint.json", checkpoint)
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--request", type=Path, required=True)
    p.add_argument("--targets", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    try:
        return run(args.request, args.targets, args.output)
    except Exception as exc:
        print(
            f"NORMAL_SWEEP_FINALIZE_FAILED: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
