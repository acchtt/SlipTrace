"""Cheap sweep research-priority filters.

These filters run *after* complete date-surface acquisition and *before*
external deep form research. They never create C/C2 model verdicts, never
hard-exclude a valid competitive fixture, and never override fresh
source-backed football evidence.

Profiles are intentionally conservative and time-bounded. When a profile
expires, the fixture falls back to NEUTRAL_RESEARCH until league research is
refreshed.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from league_registry import norm

SCHEMA = "football-sweep-cheap-filter-v1"

PRIMARY = "PRIMARY_RESEARCH"
SECONDARY = "SECONDARY_RESEARCH"
SPECIAL = "SPECIAL_RESEARCH"
DEFERRED = "DEFERRED_RESEARCH"
NEUTRAL = "NEUTRAL_RESEARCH"

PRIORITY_RANK = {
    PRIMARY: 0,
    SECONDARY: 1,
    SPECIAL: 2,
    DEFERRED: 3,
    NEUTRAL: 4,
}

PROFILE_AS_OF = "2026-10-13T00:00:00Z"
PROFILE_EXPIRES = "2026-11-13T00:00:00Z"


def _utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timezone-aware timestamp required")
    return parsed.astimezone(timezone.utc)


def _team(value: Any) -> str:
    return norm(value)


# Current-event priors are research shortcuts only. They expire quickly and
# must never substitute for actual recent-result collection.
EERSTE_HIGH_EVENT = {
    norm(x) for x in (
        "Heracles", "Heracles Almelo",
        "VVV", "VVV Venlo",
        "FC Emmen", "Emmen",
        "NAC Breda",
        "FC Dordrecht", "Dordrecht",
        "Jong PSV", "PSV Eindhoven II",
        "Jong Ajax", "Ajax II",
        "Jong AZ", "AZ II",
        "Jong Utrecht", "FC Utrecht II", "Utrecht II",
        "De Graafschap",
        "FC Eindhoven",
        "MVV", "MVV Maastricht", "Maastricht",
        "Helmond Sport",
    )
}

WE_LEAGUE_HIGH_EVENT = {
    norm(x) for x in (
        "NTV Beleza", "Tokyo Verdy Beleza", "Nippon TV Tokyo Verdy Beleza",
        "INAC Kobe Leonessa", "INAC Kobe Leonesa",
        "Urawa Red Diamonds Ladies", "Urawa Reds W", "Urawa W",
        "Nojima Stella Kanagawa Sagamihara", "Nojima Stella",
    )
}

WE_CUP_ATTACK_OR_LEAK = {
    norm(x) for x in (
        "NTV Beleza", "Tokyo Verdy Beleza",
        "Urawa Red Diamonds Ladies", "Urawa Reds W",
        "JEF United Ichihara Chiba Ladies", "JEF United W", "JEF United",
        "Cerezo Osaka Sakai Ladies", "Cerezo Osaka W",
        "Sanfrecce Hiroshima Regina", "Sanfrecce Hiroshima W",
        "RB Omiya Ardija Ventus", "Omiya Ardija Ventus",
        "INAC Kobe Leonessa", "INAC Kobe Leonesa",
        "AC Nagano Parceiro Women", "Parceiro Nagano Women",
    )
}

NADESHIKO1_EVENT = {
    norm(x) for x in (
        "Nittaidai", "Nittaidai FC",
        "Shizuoka SSU Bonita", "Shizuoka Bonita",
    )
}


# Big-Five competition status is a data/researchability prior only. It must
# never promote a fixture into active sweep research by league prestige alone.
# Until a separate current team/event profile is researched, missing-evidence
# fixtures from these leagues default to DEFERRED_RESEARCH. Fresh verified
# match goal evidence can still override this at the goals-first screen.
TOP_FIVE_NO_AUTO_PROMOTION = {
    ("england", "premier league"),
    ("england", "english premier league"),
    ("germany", "bundesliga"),
    ("germany", "german bundesliga"),
    ("spain", "la liga"),
    ("spain", "laliga"),
    ("italy", "serie a"),
    ("italy", "italian serie a"),
    ("france", "ligue 1"),
    ("france", "french ligue 1"),
}


def _competition_key(fixture: dict[str, Any]) -> tuple[str, str]:
    return norm(fixture.get("country")), norm(fixture.get("competition"))


def _contains(comp: str, *parts: str) -> bool:
    return any(norm(part) in comp for part in parts)


def classify_research_priority(
    fixture: dict[str, Any], *, at_utc: str,
) -> dict[str, Any]:
    """Return a cheap research priority without excluding the fixture."""
    now = _utc(at_utc)
    expired = now >= _utc(PROFILE_EXPIRES)
    country, comp = _competition_key(fixture)
    home, away = _team(fixture.get("home")), _team(fixture.get("away"))
    teams = {home, away}

    base = {
        "schema_version": SCHEMA,
        "priority": NEUTRAL,
        "priority_rank": PRIORITY_RANK[NEUTRAL],
        "reason": "NO_ACTIVE_CHEAP_FILTER_PROFILE",
        "profile_as_of_utc": PROFILE_AS_OF,
        "profile_expires_utc": PROFILE_EXPIRES,
        "hard_exclude": False,
        "draw_trap_caution": False,
        "requires_match_specific_goal_evidence": True,
        "profile_expired": expired,
    }
    if expired:
        return base

    if (country, comp) in TOP_FIVE_NO_AUTO_PROMOTION:
        return {
            **base,
            "priority": DEFERRED,
            "priority_rank": PRIORITY_RANK[DEFERRED],
            "reason": "TOP_FIVE_STATUS_NOT_A_GOAL_SIGNAL",
            "league_profile": "TOP_FIVE_NO_AUTO_PROMOTION_V1",
            "draw_trap_caution": False,
        }

    # Netherlands Eerste Divisie: league is strongly goal-active, but use the
    # team prior to decide which fixtures get first research attention.
    if country == "netherlands" and _contains(comp, "eerste divisie", "eerstedivisie"):
        if teams & EERSTE_HIGH_EVENT:
            priority, reason = PRIMARY, "EERSTE_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "EERSTE_HIGH_GOAL_LEAGUE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "NED_EERSTE_2026_27",
        }

    if country == "japan":
        # WE League: promising current environment, but early-season sample is
        # still small, so only known high-event teams get the primary boost.
        if _contains(comp, "we league") and not _contains(comp, "cup"):
            if teams & WE_LEAGUE_HIGH_EVENT:
                priority, reason = PRIMARY, "WE_LEAGUE_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "WE_LEAGUE_GOAL_ENVIRONMENT_EARLY_SAMPLE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "JPN_WE_LEAGUE_2026_27",
            }

        # WE League Cup: overall scoring is useful, but 1-1 remains frequent.
        # Do not blanket-promote the whole competition.
        if _contains(comp, "we league cup", "we league kracie cup", "kracie cup"):
            if teams & WE_CUP_ATTACK_OR_LEAK:
                priority, reason = SECONDARY, "WE_CUP_EVENT_TEAM_PRESENT"
            else:
                priority, reason = DEFERRED, "WE_CUP_DRAW_TRAP_CAUTION"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "JPN_WE_CUP_2026_27",
                "draw_trap_caution": True,
            }

        # Nadeshiko 1 has a usable but not blanket-Over environment.
        if _contains(comp, "nadeshiko league 1", "nadeshiko 1"):
            if teams & NADESHIKO1_EVENT:
                priority, reason = SECONDARY, "NADESHIKO1_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "NADESHIKO1_SELECTIVE_GOAL_ENVIRONMENT"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "JPN_NADESHIKO1_2026",
                "draw_trap_caution": True,
            }

        # Nadeshiko 2 is materially lower scoring with many clean-sheet and
        # 0-0/1-1 outcomes. Keep it visible, but do not spend primary research
        # budget unless fresh match evidence later proves a strong goal case.
        if _contains(comp, "nadeshiko league 2", "nadeshiko 2"):
            return {
                **base, "priority": DEFERRED,
                "priority_rank": PRIORITY_RANK[DEFERRED],
                "reason": "NADESHIKO2_LOW_GOAL_DRAW_TRAP_BASE",
                "league_profile": "JPN_NADESHIKO2_2026",
                "draw_trap_caution": True,
            }

        # Empress's Cup mixes divisions and knockout incentives. Competition
        # identity alone is not enough to decide goal friendliness.
        if _contains(comp, "empress cup", "empress s cup", "jfa empress"):
            return {
                **base, "priority": SPECIAL,
                "priority_rank": PRIORITY_RANK[SPECIAL],
                "reason": "EMPRESS_CUP_CROSS_TIER_AND_ROUND_RESEARCH_REQUIRED",
                "league_profile": "JPN_EMPRESS_CUP_2026",
                "draw_trap_caution": True,
                "requires_tier_round_context": True,
            }

    return base
