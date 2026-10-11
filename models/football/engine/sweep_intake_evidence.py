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


LEAGUE_CHANNEL_POLICY = "LEAGUE_CHANNEL_FIRST_V1"

# Operational data-coverage tier, NOT a goals/prediction tier or an
# automatic override of user scope / domestic league exclusions.
# Exact labels deliberately avoid ambiguous names such as "Pro League".
TIER1_CHANNEL_LEAGUES = frozenset({
    "premier league", "english premier league",
    "bundesliga", "german bundesliga",
    "la liga", "laliga", "spanish la liga",
    "serie a", "italian serie a",
    "ligue 1", "french ligue 1",
    "eredivisie", "netherlands eredivisie",
    "primeira liga", "portugal primeira liga",
    "belgian pro league", "belgian first division a",
    "major league soccer", "mls",
    "liga mx", "mexico liga mx",
    "austrian bundesliga",
    "scottish premiership",
    "j1", "j1 league", "japan j1",
    "k league 1", "k1", "korean k league 1",
})

# Only these exact country + competition pairs may use Tier-1 publication
# EXPECTATION at Step 0 without prior XI / Asian-total provider attestations.
# This is NOT automatic A/B admission or proof that a specific quote exists.
TIER1_STANDARD_COUNTRY_LEAGUES = {
    "england": {"premier league", "english premier league"},
    "germany": {"bundesliga", "german bundesliga"},
    "spain": {"la liga", "laliga", "spanish la liga"},
    "italy": {"serie a", "italian serie a"},
    "france": {"ligue 1", "french ligue 1"},
    "netherlands": {"eredivisie", "netherlands eredivisie"},
    "portugal": {"primeira liga", "portugal primeira liga"},
    "belgium": {"belgian pro league", "belgian first division a"},
    "united states": {"major league soccer", "mls"},
    "usa": {"major league soccer", "mls"},
    "canada": {"major league soccer", "mls"},
    "mexico": {"liga mx", "mexico liga mx"},
    "austria": {"austrian bundesliga"},
    "scotland": {"scottish premiership"},
    "japan": {"j1", "j1 league", "japan j1"},
    "south korea": {"k league 1", "k1", "korean k league 1"},
    "korea": {"k league 1", "k1", "korean k league 1"},
}


def _registered_tier1_standard(row: dict[str, Any]) -> bool:
    country = row.get("country")
    name = row.get("competition_name") or row.get("competition")
    return (
        isinstance(country, str) and isinstance(name, str)
        and name.strip().casefold() in TIER1_STANDARD_COUNTRY_LEAGUES.get(
            country.strip().casefold(), frozenset()
        )
    )


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


def _league_channel_defects(row: dict[str, Any]) -> list[str]:
    """Step-0 cheap league-profile admission, never an executable quote."""
    defects: list[str] = []
    profile = row.get("league_channel_profile")
    tier1_registered = _registered_tier1_standard(row)
    if not isinstance(profile, dict):
        if not tier1_registered:
            return ["LEAGUE_CHANNEL_PROFILE_MISSING"]
        # Exact country/league registry is the Step-0 Tier-1 coverage basis.
        # Do not fabricate historical lineup/Asian market proofs or provider URLs.
        profile = {"competition_name": row.get("competition_name") or row.get("competition"),
                   "profile_type": "TIER1_STANDARD"}
    name = row.get("competition_name") or row.get("competition")
    profile_name = profile.get("competition_name")
    if not _nonempty(name) or not _nonempty(profile_name) or (
        name.strip().casefold() != profile_name.strip().casefold()
    ):
        defects.append("LEAGUE_PROFILE_COMPETITION_MISMATCH")
    kind = profile.get("profile_type")
    tier1_waiver = kind == "TIER1_STANDARD" and tier1_registered
    if kind == "TIER1_STANDARD":
        if not _nonempty(name) or name.strip().casefold() not in TIER1_CHANNEL_LEAGUES:
            defects.append("LEAGUE_TIER1_NOT_ALLOWLISTED")
        elif not tier1_registered:
            defects.append("LEAGUE_TIER1_COUNTRY_LEAGUE_MISMATCH")
    elif kind == "PROVEN_LEAGUE":
        for key in ("recent_xi_fixture_count", "recent_asian_total_fixture_count"):
            count = profile.get(key)
            if isinstance(count, bool) or not isinstance(count, int) or count < 2:
                defects.append(f"LEAGUE_PROFILE_{key.upper()}_UNPROVEN")
    else:
        defects.append("LEAGUE_PROFILE_TYPE_UNSUPPORTED")

    if not tier1_waiver:
        # PROVEN_LEAGUE and any non-registered Tier-1 claim retain genuine
        # historic publication proof; conditional lower leagues are unchanged.
        if profile.get("coverage_status") != "VERIFIED_CHANNELS":
            defects.append("LEAGUE_CHANNEL_COVERAGE_UNVERIFIED")
        if not _nonempty(profile.get("season")):
            defects.append("LEAGUE_PROFILE_SEASON_MISSING")
        if not _nonempty(profile.get("evidence_basis")):
            defects.append("LEAGUE_PROFILE_EVIDENCE_BASIS_MISSING")
        for key in ("xi_provider_url", "asian_total_provider_url", "team_news_provider_url"):
            if not _source_url(profile.get(key)):
                defects.append(f"LEAGUE_{key.upper()}_MISSING")
    if row.get("intake_evidence_scope") != "LEAGUE_CHANNEL_ONLY":
        defects.append("LEAGUE_CHANNEL_SCOPE_NOT_DECLARED")
    if row.get("xi_expected") not in {"YES", "UNCERTAIN"}:
        defects.append("LEAGUE_XI_EXPECTATION_MISSING")
    if row.get("xi_expected") == "UNCERTAIN" and row.get("operational_viability_grade") != "B":
        defects.append("XI_UNCERTAIN_MUST_BE_CONDITIONAL_B")
    if row.get("market_observability") not in {"HIGH", "MEDIUM"}:
        defects.append("LEAGUE_MARKET_COVERAGE_NOT_ESTABLISHED")
    if row.get("team_news_observability") not in {"HIGH", "MEDIUM"}:
        defects.append("LEAGUE_TEAM_NEWS_COVERAGE_NOT_ESTABLISHED")

    kickoff = _utc_timestamp(row.get("fixture_kickoff_utc"))
    if row.get("fixture_identity_verified") is not True or not _nonempty(row.get("match_id")):
        defects.append("FIXTURE_IDENTITY_UNVERIFIED")
    if kickoff is None:
        defects.append("FIXTURE_KICKOFF_UTC_UNVERIFIED")
    if not tier1_waiver:
        evidence_time = _utc_timestamp(profile.get("evidence_checked_at_utc"))
        if evidence_time is None or (
            kickoff and not timedelta(0) <= kickoff - evidence_time <= timedelta(days=30)
        ):
            defects.append("LEAGUE_PROFILE_EVIDENCE_STALE_OR_POST_KO")
    recheck = _utc_timestamp(row.get("xi_recheck_due_utc"))
    if recheck is None or (
        kickoff and not timedelta(minutes=30) <= kickoff - recheck <= timedelta(hours=3)
    ):
        defects.append("XI_PREMATCH_RECHECK_PLAN_MISSING_OR_INVALID")
    if row.get("operational_viability_grade") not in {"A", "B"}:
        defects.append("OPERATIONAL_GRADE_NOT_AB")
    return defects



# Targeted, source-local conditional fixtures. Verified historical goal results
# govern research admission only: never a forecast, quote or C/C2 decision.
CHAMPIONSHIP_NAMES = frozenset({
    "championship", "efl championship", "english championship",
    "england championship", "sky bet championship",
})
POLAND_EKSTRAKLASA_NAMES = frozenset({"ekstraklasa"})


def _recent_five_goal_signal_defects(
    row: dict[str, Any], *, field: str, label: str,
) -> list[str]:
    """Both teams' dated, identified last five competitive scorelines.

    A verified source URL refers to a score publication, not future odds/XI.
    Do not materialize fabricated team streaks from static watchlists.
    """
    evidence = row.get(field)
    if not isinstance(evidence, dict):
        return [f"{label}_CHEAP_SIGNAL_MISSING"]
    kickoff = _utc_timestamp(row.get("fixture_kickoff_utc"))
    captured = _utc_timestamp(evidence.get("captured_at_utc"))
    if kickoff is None or captured is None or not (
        timedelta(0) <= kickoff - captured <= timedelta(days=7)
    ):
        return [f"{label}_CHEAP_SIGNAL_STALE_OR_POST_KO"]

    teams = []
    for side in ("home", "away"):
        data = evidence.get(side)
        if not isinstance(data, dict) or not _source_url(data.get("source_url")):
            return [f"{label}_{side.upper()}_GOAL_SOURCE_UNVERIFIED"]
        matches = data.get("recent_competitive_matches")
        if not isinstance(matches, list) or len(matches) != 5:
            return [f"{label}_{side.upper()}_FIVE_RESULTS_INVALID"]
        totals, traps, identities = [], 0, set()
        for match in matches:
            if not isinstance(match, dict):
                return [f"{label}_{side.upper()}_HISTORY_INVALID"]
            ident, when = match.get("match_id"), _utc_timestamp(match.get("kickoff_utc"))
            gf, ga = match.get("goals_for"), match.get("goals_against")
            if (not _nonempty(ident) or ident in identities or
                when is None or kickoff is None or
                not timedelta(0) < kickoff - when <= timedelta(days=120) or
                when > captured or
                # Historical match must be demonstrably completed before
                # its observation; prevent accidentally including live games.
                captured - when < timedelta(hours=2) or
                match.get("competitive") is not True or
                isinstance(gf, bool) or not isinstance(gf, int) or not 0 <= gf <= 20 or
                isinstance(ga, bool) or not isinstance(ga, int) or not 0 <= ga <= 20):
                return [f"{label}_{side.upper()}_HISTORY_INVALID"]
            identities.add(ident)
            totals.append(gf + ga)
            traps += int((gf, ga) in {(0, 0), (1, 1)})
        teams.append({
            "avg": sum(totals) / 5,
            "over_count": sum(n >= 3 for n in totals),
            "trap_count": traps,
            "stall_count": sum(n <= 2 for n in totals),
        })
    h, a = teams
    # Opponent-driven blowouts are not enough when the other team repeatedly
    # ends at 0-0/1-1 or struggles to fund a third goal.
    if any(t["trap_count"] >= 3 or t["stall_count"] >= 4 for t in teams):
        return [f"{label}_LOW_TOTAL_STALL_OR_DRAW_TRAP"]

    qualified = (
        (h["avg"] >= 2.8 and a["avg"] >= 2.8) or
        (max(h["avg"], a["avg"]) >= 3.2 and min(h["avg"], a["avg"]) >= 2.6) or
        (h["over_count"] >= 3 and a["over_count"] >= 3)
    )
    return [] if qualified else [f"{label}_CHEAP_SIGNAL_FAIL"]


def _championship_goal_signal_defects(row: dict[str, Any]) -> list[str]:
    name = row.get("competition_name") or row.get("competition")
    if not _nonempty(name) or name.strip().casefold() not in CHAMPIONSHIP_NAMES:
        return []
    country = row.get("country")
    if _nonempty(country) and country.strip().casefold() != "england":
        return ["CHAMPIONSHIP_PILOT_COUNTRY_MISMATCH"]
    return _recent_five_goal_signal_defects(
        row, field="championship_recent_goal_evidence", label="CHAMPIONSHIP",
    )


def _poland_ekstraklasa_goal_signal_defects(row: dict[str, Any]) -> list[str]:
    name = row.get("competition_name") or row.get("competition")
    if not _nonempty(name) or name.strip().casefold() not in POLAND_EKSTRAKLASA_NAMES:
        return []
    # Ekstraklasa can appear in sources from other countries; reject an
    # unverified country instead of assuming Poland from the league string.
    country = row.get("country")
    if not _nonempty(country) or country.strip().casefold() != "poland":
        return ["POLAND_EKSTRAKLASA_COUNTRY_UNVERIFIED"]
    return _recent_five_goal_signal_defects(
        row, field="poland_ekstraklasa_recent_goal_evidence",
        label="POLAND_EKSTRAKLASA",
    )


# Short-season Hong Kong/Malaysia league pilots: source-backed proof only.
# Three verified completed matches per side is a deliberately smaller minimum
# than Championship/Poland's five, since October 2026 has very few league rounds.
ASIA_TOPFLIGHT_PILOT_NAMES = {
    "hong kong": frozenset({"premier league", "hong kong premier league",
                           "boc life hong kong premier league"}),
    "hong kong sar": frozenset({"premier league", "hong kong premier league",
                               "boc life hong kong premier league"}),
    "malaysia": frozenset({"super league", "malaysia super league",
                           "malaysian super league", "liga super"}),
}
ASIA_TOPFLIGHT_PILOT_FIELD = "asia_topflight_recent_goal_evidence"


def _asia_topflight_goal_signal_defects(row: dict[str, Any]) -> list[str]:
    name = row.get("competition_name") or row.get("competition")
    country = row.get("country")
    if not isinstance(name, str) or not isinstance(country, str):
        return []
    c, n = country.strip().casefold(), name.strip().casefold()
    if n not in ASIA_TOPFLIGHT_PILOT_NAMES.get(c, frozenset()):
        return []
    prefix = "HKPL" if c in {"hong kong", "hong kong sar"} else "MY_SUPER"
    evidence = row.get(ASIA_TOPFLIGHT_PILOT_FIELD)
    if not isinstance(evidence, dict):
        return [f"{prefix}_RECENT_GOAL_PROOF_MISSING"]
    ko = _utc_timestamp(row.get("fixture_kickoff_utc"))
    captured = _utc_timestamp(evidence.get("captured_at_utc"))
    if ko is None or captured is None or not timedelta(0) <= ko - captured <= timedelta(days=7):
        return [f"{prefix}_RECENT_GOAL_PROOF_STALE_OR_POST_KO"]
    stats = []
    for side in ("home", "away"):
        item = evidence.get(side)
        if not isinstance(item, dict) or not _source_url(item.get("source_url")):
            return [f"{prefix}_{side.upper()}_RESULT_SOURCE_UNVERIFIED"]
        matches = item.get("recent_competitive_matches")
        if not isinstance(matches, list) or not 3 <= len(matches) <= 5:
            return [f"{prefix}_{side.upper()}_THREE_TO_FIVE_RESULTS_REQUIRED"]
        ids, totals, traps = set(), [], 0
        for m in matches:
            if not isinstance(m, dict):
                return [f"{prefix}_{side.upper()}_RESULT_INVALID"]
            match_id, when = m.get("match_id"), _utc_timestamp(m.get("kickoff_utc"))
            gf, ga = m.get("goals_for"), m.get("goals_against")
            if (not _nonempty(match_id) or match_id in ids or
                when is None or not timedelta(hours=2) <= captured - when or
                not timedelta(0) < ko - when <= timedelta(days=120) or
                m.get("competitive") is not True or
                isinstance(gf, bool) or not isinstance(gf, int) or not 0 <= gf <= 20 or
                isinstance(ga, bool) or not isinstance(ga, int) or not 0 <= ga <= 20):
                return [f"{prefix}_{side.upper()}_RESULT_INVALID"]
            ids.add(match_id)
            totals.append(gf + ga)
            traps += int((gf, ga) in {(0, 0), (1, 1)})
        stats.append({"avg": sum(totals) / len(totals),
                      "over": sum(v >= 3 for v in totals) / len(totals),
                      "stalls": sum(v <= 2 for v in totals) / len(totals),
                      "traps": traps / len(totals)})
    home, away = stats
    if any(t["traps"] >= 0.60 or t["stalls"] >= 0.80 for t in stats):
        return [f"{prefix}_REPEATED_STALL_OR_0_0_1_1_TRAP"]
    both = min(home["avg"], away["avg"]) >= 2.8 and min(home["over"], away["over"]) >= 0.4
    carrier = max(home["avg"], away["avg"]) >= 3.4 and min(home["avg"], away["avg"]) >= 2.0 and min(home["over"], away["over"]) >= 0.25
    return [] if (both or carrier) else [f"{prefix}_CHEAP_GOAL_SIGNAL_NOT_PROVEN"]


def validate_shared_league_profiles(rows: list[dict[str, Any]]) -> list[str]:
    """One immutable channel proof per competition in a new Step-0 sweep.

    Reject a fixture-wise collection of different evidence profiles for the
    same league. This does not establish whether a URL is currently reachable:
    the caller must have actually checked its source before freezing it.
    """
    known: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            errors.append("LEAGUE_CHANNEL_FIXTURE_ROW_INVALID")
            continue
        name = row.get("competition_name") or row.get("competition")
        if not _nonempty(name):
            errors.append("LEAGUE_CHANNEL_COMPETITION_NAME_MISSING")
            continue
        profile = row.get("league_channel_profile")
        if not isinstance(profile, dict):
            if not _registered_tier1_standard(row):
                errors.append(f"LEAGUE_CHANNEL_PROFILE_MISSING: {name}")
                continue
            profile = {"competition_name": name, "profile_type": "TIER1_STANDARD"}
        key = f"{str(row.get('country', '')).strip().casefold()}|{name.strip().casefold()}"
        if key in known and known[key] != profile:
            errors.append(f"LEAGUE_CHANNEL_PROFILE_INCONSISTENT: {name}")
        else:
            known[key] = profile
    return sorted(set(errors))


def validate_work_candidate(row: dict[str, Any], *, intake_policy: str = "XI_MARKET_FIRST_V1") -> list[str]:
    """Return explicit operational proof defects, empty only when Work eligible."""
    if not isinstance(row, dict):
        return ["FIXTURE_ROW_INVALID"]

    if intake_policy not in {"XI_MARKET_FIRST_V1", LEAGUE_CHANNEL_POLICY}:
        return ["UNKNOWN_STEP0_INTAKE_POLICY"]
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

    if intake_policy == LEAGUE_CHANNEL_POLICY:
        # Registered country+league Tier-1 fixtures use expected publishing
        # coverage without historic XI/Asian-total proof at Step 0. All other
        # leagues retain PROVEN_LEAGUE proofs. Neither path waives fixture
        # identity, A/B operations or /rank and /xi match-specific research.
        return (defects + _league_channel_defects(row)
                + _championship_goal_signal_defects(row)
                + _poland_ekstraklasa_goal_signal_defects(row)
                + _asia_topflight_goal_signal_defects(row))

    # Legacy XI_MARKET_FIRST_V1 is unchanged for existing running/frozen sweeps.
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


def classify_preflight(row: dict[str, Any], *, intake_policy: str = "XI_MARKET_FIRST_V1") -> dict[str, Any]:
    """Classify without deleting raw discovery or prematurely promoting UNKNOWN."""
    defects = validate_work_candidate(row, intake_policy=intake_policy)
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
