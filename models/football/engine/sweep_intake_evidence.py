"""Fail-closed prospective evidence gate for the compact Football Step-0 Work queue.

Pure validation: no network, no model prediction, no source discovery.
Legacy/frozen handoffs do not invoke this module.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from math import isfinite
import re
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

# Source-backed expectation, not confirmed starting XI for a future kickoff.
# An official squad or dependable matchday-lineup provider is permitted for B.
XI_CHANNEL_TYPES = frozenset(
    {"RECENT_CONFIRMED_XI", "PROVIDER_MATCHDAY_COVERAGE", "OFFICIAL_SQUAD_NEWS"}
)
XI_STRONG_TYPES = frozenset(
    {"RECENT_CONFIRMED_XI", "PROVIDER_MATCHDAY_COVERAGE"}
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
    # Standing user scope (2026-10-09): all noncompetitive friendlies
    # are excluded before XI/market qualification, even when a bookmaker
    # lists them. Preserve competitive international qualifiers/tournaments.
    labels = (
        row.get("competition_name"),
        row.get("competition"),
        row.get("fixture_type"),
        row.get("competition_type"),
        row.get("match_type"),
    )
    friendly_named = any(
        isinstance(value, str) and re.search(
            r"\b(?:friendly|friendlies|exhibition|pre[- ]?season)\b",
            value,
            flags=re.IGNORECASE,
        )
        for value in labels
    )
    if row.get("is_friendly") is True or row.get("friendly_scope_excluded") is True or friendly_named:
        defects.append("USER_SCOPE_EXCLUDED_FRIENDLY")

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

    # 24h discovery occurs long before official match-day XIs drop. Require
    # evidence of a usable publication channel, NOT the future starting XI.
    # B/UNCERTAIN remains conditional until the /xi matchday recheck.
    xi_expected = row.get("xi_expected")
    if xi_expected not in {"YES", "UNCERTAIN"}:
        defects.append("XI_CHANNEL_NOT_VERIFIABLE")
    xi_types = []
    for side in ("home", "away"):
        kind = row.get(f"xi_{side}_channel_type")
        url = row.get(f"xi_{side}_channel_source_url")
        if kind not in XI_CHANNEL_TYPES or not _source_url(url):
            defects.append(f"XI_{side.upper()}_PUBLISHING_CHANNEL_UNVERIFIED")
        else:
            xi_types.append(kind)
    if xi_expected == "YES" and len(xi_types) == 2 and any(
        kind not in XI_STRONG_TYPES for kind in xi_types
    ):
        defects.append("XI_EXPECTATION_OVERSTATED")
    if xi_expected == "UNCERTAIN":
        if row.get("operational_viability_grade") != "B":
            defects.append("XI_UNCERTAIN_MUST_BE_CONDITIONAL_B")
        # A squad list alone never establishes that starting XIs will be
        # obtainable. At least one evidenced provider/actual XI channel.
        if not any(kind in XI_STRONG_TYPES for kind in xi_types):
            defects.append("XI_CHANNEL_NO_PUBLISHING_PATH")
    if not _nonempty(row.get("xi_channel_basis")):
        defects.append("XI_CHANNEL_EVIDENCE_BASIS_MISSING")

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
    # Optional corroborating previous XI provenance; if supplied, it must
    # precede the current fixture. Some tournaments lack recent historical XI.
    for side in ("home", "away"):
        source_match = row.get(f"xi_{side}_recent_match_id")
        source_kickoff_value = row.get(f"xi_{side}_recent_match_kickoff_utc")
        if source_match is not None or source_kickoff_value is not None:
            if not _nonempty(source_match) or source_match == row.get("match_id"):
                defects.append(f"XI_{side.upper()}_HISTORICAL_ID_INVALID")
            source_kickoff = _utc_timestamp(source_kickoff_value)
            if source_kickoff is None or (
                kickoff and not (timedelta(0) < kickoff - source_kickoff <= timedelta(days=480))
            ):
                defects.append(f"XI_{side.upper()}_HISTORICAL_FIXTURE_TIME_INVALID")

    recheck = _utc_timestamp(row.get("xi_recheck_due_utc"))
    if recheck is None or (kickoff and not (
        timedelta(minutes=30) <= kickoff - recheck <= timedelta(hours=3)
    )):
        defects.append("XI_PREMATCH_RECHECK_PLAN_MISSING_OR_INVALID")

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
    # Scope exclusions are terminal at classification, even when no
    # expensive XI/Asian-total preflight was attempted.
    if any(code in defects for code in (
        "USER_SCOPE_EXCLUDED", "HARD_SCOPE_EXCLUDED", "USER_SCOPE_EXCLUDED_FRIENDLY"
    )):
        return {
            "work_queue_eligible": False,
            "disposition": "STEP0_OPERATIONAL_OR_SCOPE_EXCLUDED",
            "defects": defects,
        }
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
