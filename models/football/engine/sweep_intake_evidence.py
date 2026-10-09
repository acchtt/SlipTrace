"""Fail-closed prospective evidence gate for the compact Football Step-0 Work queue.

Pure validation: no network, no model prediction, no source discovery.
Legacy/frozen handoffs do not invoke this module.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from math import isfinite
from typing import Any
from urllib.parse import urlparse


SUPPORTED_COMPETITION_TIERS = frozenset(
    {
        "PROTECTED_OFFICIAL",
        "VERIFIED_PROFESSIONAL",
        "VERIFIED_WOMEN_TOP_FLIGHT",
        "MAJOR_SENIOR_DOMESTIC_CUP",
        "USER_EXCEPTION",
    }
)

REQUIRED_XI_FIELDS = (
    "xi_home_recent_match_id",
    "xi_away_recent_match_id",
    "xi_home_lineup_source_url",
    "xi_away_lineup_source_url",
)

REQUIRED_MARKET_FIELDS = (
    "asian_total_market_match_id",
    "asian_total_fixture_source_url",
    "asian_total_market_observed_at_utc",
    "asian_total_market_line",
    "asian_total_market_bookmaker",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _source_url(value: Any) -> bool:
    if not _nonempty(value):
        return False
    try:
        uri = urlparse(value.strip())
    except (ValueError, AttributeError):
        return False
    return (
        uri.scheme == "https"
        and bool(uri.hostname)
        and "." in uri.hostname
        and not uri.username
        and not uri.password
    )


def _utc_timestamp(value: Any) -> datetime | None:
    if not _nonempty(value):
        return None
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None or dt.utcoffset() is None:
        return None
    return dt.astimezone(timezone.utc)


def validate_work_candidate(row: dict[str, Any]) -> list[str]:
    """Return explicit operational proof defects, empty only when Work eligible."""
    if not isinstance(row, dict):
        return ["FIXTURE_ROW_INVALID"]

    defects: list[str] = []
    if row.get("preflight_complete") is not True:
        defects.append("STEP0_PREFLIGHT_INCOMPLETE")
    if row.get("user_scope_excluded") is True:
        defects.append("USER_SCOPE_EXCLUDED")
    if row.get("hard_scope_excluded") is True:
        defects.append("HARD_SCOPE_EXCLUDED")

    if row.get("competition_support_tier") not in SUPPORTED_COMPETITION_TIERS:
        defects.append("COMPETITION_SUPPORT_UNVERIFIED")
    if not _source_url(row.get("competition_official_url")):
        defects.append("COMPETITION_SOURCE_MISSING")
    if not _nonempty(row.get("competition_support_reason")):
        defects.append("COMPETITION_SUPPORT_BASIS_MISSING")

    if row.get("xi_expected") != "YES":
        defects.append("XI_CHANNEL_NOT_VERIFIABLE")
    if not (
        all(_nonempty(row.get(k)) for k in REQUIRED_XI_FIELDS[:2])
        and all(_source_url(row.get(k)) for k in REQUIRED_XI_FIELDS[2:])
    ):
        defects.append("XI_BOTH_TEAMS_RECENT_CONFIRMED_EVIDENCE_MISSING")

    if row.get("market_observability") not in {"HIGH", "MEDIUM"}:
        defects.append("CURRENT_ASIAN_TOTAL_UNAVAILABLE")
    if not _nonempty(row.get("match_id")) or (
        row.get("asian_total_market_match_id") != row.get("match_id")
    ):
        defects.append("CURRENT_ASIAN_TOTAL_FIXTURE_ID_MISMATCH")
    if not _source_url(row.get("asian_total_fixture_source_url")):
        defects.append("CURRENT_ASIAN_TOTAL_SOURCE_MISSING")
    if not _nonempty(row.get("asian_total_market_bookmaker")):
        defects.append("CURRENT_ASIAN_TOTAL_BOOKMAKER_MISSING")

    line = row.get("asian_total_market_line")
    if isinstance(line, bool) or not isinstance(line, (int, float, str)):
        defects.append("CURRENT_ASIAN_TOTAL_LINE_MISSING")
    else:
        try:
            numeric_line = float(line)
        except (ValueError, OverflowError):
            numeric_line = 0
        if not isfinite(numeric_line) or not 0.5 <= numeric_line <= 10.0:
            defects.append("CURRENT_ASIAN_TOTAL_LINE_MISSING")

    if row.get("team_news_observability") not in {"HIGH", "MEDIUM"}:
        defects.append("TEAM_NEWS_NOT_OBSERVABLE")
    if not _source_url(row.get("team_news_source_url")):
        defects.append("TEAM_NEWS_SOURCE_MISSING")

    if row.get("fixture_identity_verified") is not True:
        defects.append("FIXTURE_IDENTITY_UNVERIFIED")
    kickoff = _utc_timestamp(row.get("fixture_kickoff_utc"))
    if kickoff is None:
        defects.append("FIXTURE_KICKOFF_UTC_UNVERIFIED")

    market_time = _utc_timestamp(row.get("asian_total_market_observed_at_utc"))
    if market_time is None:
        defects.append("CURRENT_ASIAN_TOTAL_TIME_UNVERIFIED")
    for side in ("home", "away"):
        source_match = row.get(f"xi_{side}_recent_match_id")
        if _nonempty(source_match) and source_match == row.get("match_id"):
            defects.append("XI_RECENT_FIXTURE_ID_NOT_HISTORICAL")
        source_kickoff = _utc_timestamp(
            row.get(f"xi_{side}_recent_match_kickoff_utc")
        )
        if source_kickoff is None:
            defects.append(f"XI_{side.upper()}_HISTORICAL_FIXTURE_TIME_MISSING")
        elif kickoff and not (
            timedelta(0) < kickoff - source_kickoff <= timedelta(days=240)
        ):
            defects.append(f"XI_{side.upper()}_HISTORICAL_FIXTURE_TIME_STALE")

    if market_time and kickoff and not (
        timedelta(0) <= kickoff - market_time <= timedelta(hours=72)
    ):
        defects.append("CURRENT_ASIAN_TOTAL_STALE_OR_POST_KO")

    if row.get("operational_viability_grade") not in {"A", "B"}:
        defects.append("OPERATIONAL_GRADE_NOT_AB")

    return defects


def classify_preflight(row: dict[str, Any]) -> dict[str, Any]:
    """Classify without deleting raw discovery or prematurely promoting UNKNOWN."""
    defects = validate_work_candidate(row)
    if not defects:
        return {"work_queue_eligible": True, "disposition": "READY_FOR_AB_QUEUE", "defects": []}
    if not isinstance(row, dict) or row.get("preflight_complete") is not True:
        return {
            "work_queue_eligible": False,
            "disposition": "PREFLIGHT_INCOMPLETE_NO_WORK",
            "defects": defects,
        }
    return {
        "work_queue_eligible": False,
        "disposition": "STEP0_OPERATIONAL_OR_SCOPE_EXCLUDED",
        "defects": defects,
    }
