#!/usr/bin/env python3
"""Route an /xi fixture across kickoff without discarding the football assessment.

A started fixture is assessable in the LIVE lane, even minutes after kickoff.
This routing guard NEVER approves an official BET, assumes old prematch odds
are executable, or turns a LIVE_REROUTED receipt into a completed decision.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

SCHEMA = "football-step2-kickoff-transition-v1"
EARLY_LIVE_MINUTES = 15
MAX_LIVE_QUOTE_AGE_SECONDS = 120
SCORE = re.compile(r"^\d{1,2}-\d{1,2}$")
STATUSES = {"PREMATCH_CONFIRMED", "STARTED", "HALFTIME", "FINISHED", "POSTPONED", "CANCELLED", "UNKNOWN"}
EVENT_STATES = {"NONE_VERIFIED", "GOAL", "RED_CARD", "OTHER_MATERIAL", "UNKNOWN"}


class TransitionError(ValueError):
    pass


def _iso(value: Any, key: str) -> datetime:
    if not isinstance(value, str):
        raise TransitionError(f"{key} must be an offset-aware timestamp")
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise TransitionError(f"{key} invalid ISO timestamp") from exc
    if d.utcoffset() is None:
        raise TransitionError(f"{key} requires timezone")
    return d.astimezone(timezone.utc)


def _https_url(value: Any, key: str) -> str:
    if not isinstance(value, str):
        raise TransitionError(f"{key} must be an HTTPS source")
    p = urlsplit(value)
    if p.scheme != "https" or not p.hostname or "." not in p.hostname or p.username or p.password:
        raise TransitionError(f"{key} must be an HTTPS source")
    return value


def _quote_evidence(quote: Any, now: datetime, kickoff: datetime) -> tuple[bool, str]:
    if quote is None:
        return False, "CURRENT_LIVE_QUOTE_REQUIRED"
    if not isinstance(quote, dict):
        raise TransitionError("live_quote must be an object")
    if quote.get("market_phase") != "LIVE":
        return False, "PREMATCH_QUOTE_EXPIRED"
    line = quote.get("total_line")
    odds = quote.get("decimal_odds")
    if isinstance(line, bool) or not isinstance(line, (int, float)) or not math.isfinite(line) or line < 0 or abs(line * 4 - round(line * 4)) > 1e-8:
        return False, "LIVE_TOTAL_INVALID"
    if isinstance(odds, bool) or not isinstance(odds, (int, float)) or not math.isfinite(odds) or odds <= 1:
        return False, "LIVE_ODDS_INVALID"
    try:
        _https_url(quote.get("source_url"), "live_quote.source_url")
        captured = _iso(quote.get("observed_at_utc"), "live_quote.observed_at_utc")
    except TransitionError:
        return False, "LIVE_QUOTE_SOURCE_OR_TIME_INVALID"
    if not kickoff <= captured <= now or (now - captured).total_seconds() > MAX_LIVE_QUOTE_AGE_SECONDS:
        return False, "LIVE_QUOTE_EXPIRED_OR_PRE_KICKOFF"
    return True, "LIVE_QUOTE_CURRENT_AT_ASSESSMENT_EPOCH"


def route_fixture(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA:
        raise TransitionError(f"schema_version must be {SCHEMA}")
    match_id = payload.get("match_id")
    if not isinstance(match_id, str) or not match_id.strip():
        raise TransitionError("match_id is required")
    kickoff = _iso(payload.get("kickoff_utc"), "kickoff_utc")
    now = _iso(payload.get("assessment_at_utc"), "assessment_at_utc")
    status = payload.get("fixture_status")
    if status not in STATUSES:
        raise TransitionError("fixture_status missing or unknown")
    elapsed = round((now - kickoff).total_seconds() / 60, 3)
    base = {
        "ok": True,
        "match_id": match_id,
        "kickoff_minutes_elapsed": elapsed,
        "prematch_quote_can_be_reused": False,
        "prematch_bet_authorized": False,
        "live_bet_authorized": False,
        "actual_user_bet_recorded": False,
    }

    if status == "PREMATCH_CONFIRMED":
        if elapsed < 0:
            return {**base, "route": "PREMATCH_STEP2", "assessment_allowed": True,
                    "quote_status": "MUST_REVALIDATE_PREMATCH_QUOTE",
                    "reason": "Prematch Step2 remains available with currently validated quote"}
        return {**base, "route": "VERIFY_LIVE_STATUS", "assessment_allowed": True,
                "quote_status": "PREMATCH_QUOTE_EXPIRED",
                "reason": "Prematch status contradicts elapsed kickoff time; verify score/status and route live",
                "live_context_complete": False}

    if status in {"STARTED", "HALFTIME"}:
        if elapsed < 0:
            raise TransitionError("started status cannot precede verified kickoff")
        route = "EARLY_LIVE_FAST_PATH" if status == "STARTED" and elapsed <= EARLY_LIVE_MINUTES else "STANDARD_LIVE"
        score = payload.get("score")
        minute = payload.get("match_minute")
        score_valid = isinstance(score, str) and bool(SCORE.fullmatch(score))
        minute_valid = isinstance(minute, (int, float)) and not isinstance(minute, bool) and math.isfinite(minute) and 0 <= minute <= 130
        events = payload.get("material_event_since_frozen", "UNKNOWN")
        if events not in EVENT_STATES:
            raise TransitionError("material_event_since_frozen invalid")
        quote_ok, quote_reason = _quote_evidence(payload.get("live_quote"), now, kickoff)
        current_context = score_valid and minute_valid
        requires_recheck = events != "NONE_VERIFIED"
        if not current_context:
            state = "LIVE_SCORE_AND_MINUTE_REQUIRED"
        elif requires_recheck:
            state = "LIVE_FOOTBALL_RECHECK_REQUIRED"
        elif not quote_ok:
            state = "LIVE_QUOTE_REQUIRED_FOR_ACTION"
        else:
            state = "CURRENT_LIVE_EPOCH_READY_FOR_C_C2_ASSESSMENT"
        return {
            **base, "route": route, "assessment_allowed": True,
            "live_context_complete": current_context,
            "quote_status": quote_reason,
            "live_quote_verified_for_epoch": quote_ok,
            "material_football_recheck_required": requires_recheck,
            "assessment_status": state,
            "requires_new_live_epoch": True,
            "reason": (
                "Continue /xi as a LIVE assessment in this same session; do not require a new /live command. "
                "Recheck score, events and fresh live quote. Complete C official and C2 shadow independently "
                "under the live workflow. A verified current quote is required before any actionable live BET; "
                "the prematch decision engine remains unavailable for STARTED fixtures."
            ),
        }

    if status in {"FINISHED", "POSTPONED", "CANCELLED"}:
        return {**base, "route": "NON_ACTIONABLE_STATUS", "assessment_allowed": status == "FINISHED",
                "quote_status": "NOT_ACTIONABLE",
                "reason": "Historical audit only" if status == "FINISHED" else "Fixture is not currently playable"}
    return {**base, "route": "STATUS_EVIDENCE_REQUIRED", "assessment_allowed": True,
            "quote_status": "UNKNOWN",
            "reason": "Can provide provisional football assessment; verify live fixture state before an action"}


def main() -> int:
    import sys
    parser = argparse.ArgumentParser(description="Prematch to early-live automatic /xi transition")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        result = route_fixture(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
