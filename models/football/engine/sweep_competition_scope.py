"""Cheap, deterministic scope gate BEFORE fixture-level sweep research.

This is NOT a C/C2 model, a confirmed-data source, or a prediction. It
prevents unlisted weak-data domestic competitions from entering the expensive
league-channel verification loop. Source-visible raw fixture IDs stay in the
audit ledger. Required/protected/women's coverage is separately accounted.
"""
from __future__ import annotations

import re
from typing import Any

# Mirror the explicit league environment registry, not a global 'top flight'
# heuristic. Aliases need explicit review before promotion.
PRIORITY_NORMAL = frozenset({
    "eredivisie", "netherlands eredivisie", "bundesliga",
    "german bundesliga", "belgian pro league", "belgian first division a",
    "eliteserien", "norwegian eliteserien", "allsvenskan",
    "sweden allsvenskan", "danish superliga", "superliga denmark",
    "besta deild karla", "iceland premier league", "austrian bundesliga",
    "mls", "major league soccer", "a-league men", "australia a-league men",
    "eerstedivisie", "eerste divisie", "netherlands eerste divisie",
    "premier league", "english premier league", "la liga", "laliga",
    "serie a", "italian serie a", "french ligue 1", "ligue 1",
    "primeira liga", "portugal primeira liga", "scottish premiership",
    "swiss super league", "switzerland super league",
    "brazil serie a", "brazilian serie a", "liga mx",
    "liga de expansion mx", "liga de expansión mx", "ascenso mx",
    "saudi pro league",
})
CONDITIONAL = frozenset({
    "czech first league", "czech first division", "ekstraklasa",
    "greek super league", "greece super league", "romanian liga i",
    "croatian hnl", "serbian superliga", "slovenian prvaliga",
    "slovak nike liga", "slovak niké liga", "hungarian nb i",
    "bulgarian first league", "ireland premier division",
    "republic of ireland premier division", "china super league",
    "chinese super league", "indian super league", "uae pro league",
    "qatar stars league", "peru liga 1", "bolivia primera division",
    "bolivian division profesional", "chile primera division",
    "colombia primera a", "ecuador ligapro serie a",
    "uruguay primera division", "russian premier league",
})
# Explicit user domestic exclusions are stricter than Tier-1 channel status.
EXCLUDED_DOMESTIC_COUNTRIES = frozenset({
    "bangladesh", "israel", "kenya", "iraq", "wales", "kuwait",
    "finland", "japan",
})
LOW_GOAL_DOMESTIC = frozenset({
    ("vietnam", "v league 1"), ("south korea", "k league 1"),
    ("argentina", "argentina primera division"),
    ("argentina", "liga profesional"),
})
VALID_KINDS = frozenset({
    "DOMESTIC_LEAGUE", "DOMESTIC_CUP", "CONTINENTAL",
    "PROTECTED_OFFICIAL", "WOMENS_TOP_FLIGHT",
})
# An actual top-level well-covered final is inspectable if provider proof
# exists; it is not auto-admitted and never authorizes a bookmaker quote.
CUP_INSPECTION = frozenset({
    "australia cup", "fa cup", "efl cup", "dfb pokal",
    "copa del rey", "coppa italia", "coupe de france",
    "knvb beker", "portuguese cup", "taca de portugal",
    "us open cup",
})


def _name(s: Any) -> str:
    if not isinstance(s, str):
        return ""
    return re.sub(r"\s+", " ", re.sub(r"[-_.]+", " ", s.casefold())).strip()


def classify_competition(row: dict[str, Any]) -> dict[str, str]:
    if not isinstance(row, dict):
        raise ValueError("competition must be an object")
    name = _name(row.get("competition_name"))
    country = _name(row.get("country"))
    kind = row.get("competition_kind")
    if not name or not isinstance(kind, str) or kind not in VALID_KINDS:
        return {"lane": "SCOPE_UNRESOLVED", "reason": "COMPETITION IDENTITY/KIND UNVERIFIED"}
    if row.get("is_friendly") is True or "friendly" in name or "friendlies" in name:
        return {"lane": "SCOPE_EXCLUDED", "reason": "USER-SCOPE FRIENDLIES EXCLUDED"}
    # Explicit user exceptions are only per-run, with original scope logged.
    override = row.get("user_one_run_override") is True
    if kind == "DOMESTIC_LEAGUE":
        if country in EXCLUDED_DOMESTIC_COUNTRIES and not override:
            return {"lane": "SCOPE_EXCLUDED", "reason": "EXPLICIT COUNTRY DOMESTIC LEAGUE EXCLUSION"}
        if (country, name) in LOW_GOAL_DOMESTIC and not override:
            return {"lane": "SCOPE_EXCLUDED", "reason": "LOW-GOAL DOMESTIC REGISTRY EXCLUSION"}
        if country == "germany" and name in {"3 liga", "3 liga germany"} and not override:
            return {"lane": "SCOPE_EXCLUDED", "reason": "GERMANY 3. LIGA USER EXCLUSION"}
        if name in PRIORITY_NORMAL:
            return {"lane": "ROUTINE_LEAGUE_PROFILE", "reason": "EXPLICIT PRIORITY/NORMAL REGISTRY"}
        if name in CONDITIONAL:
            return {"lane": "CONDITIONAL_CHEAP_GATE", "reason": "EXPLICIT CONDITIONAL REGISTRY"}
        return {"lane": "SCOPE_EXCLUDED", "reason": "UNLISTED/WEAK-DATA DOMESTIC LEAGUE — NO RESEARCH"}
    if kind == "PROTECTED_OFFICIAL" or kind == "CONTINENTAL":
        return {"lane": "PROTECTED_CONTEXT_REVIEW", "reason": "SENIOR OFFICIAL COMPETITION — SOURCE/INCENTIVE CHECK"}
    if kind == "WOMENS_TOP_FLIGHT":
        if country in EXCLUDED_DOMESTIC_COUNTRIES and not override:
            return {"lane": "RAW_COVERAGE_ONLY", "reason": "USER EXCLUDED DOMESTIC WOMEN'S LEAGUE"}
        return {"lane": "COVERAGE_AUDIT_PROOF_REQUIRED", "reason": "WOMENS TOP-FLIGHT RAW COVERAGE, PROVE CHANNELS FOR WORK"}
    if kind == "DOMESTIC_CUP":
        if name in CUP_INSPECTION:
            return {"lane": "CUP_CHANNEL_REVIEW", "reason": "MAJOR SENIOR CUP — VERIFY STAGE/TEAMS/PROVIDER"}
        return {"lane": "RAW_COVERAGE_ONLY", "reason": "UNLISTED DOMESTIC CUP — NO DEEP ROUTINE SEARCH"}
    raise AssertionError(kind)


def screen_competitions(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(rows, list):
        raise ValueError("competitions must be list")
    buckets: dict[str, list[dict[str, Any]]] = {}
    seen: set[tuple[str, str, str]] = set()
    for i, row in enumerate(rows):
        decision = classify_competition(row)
        key = (_name(row.get("competition_name")), _name(row.get("country")),
               str(row.get("competition_kind")))
        if key in seen:
            raise ValueError(f"duplicate competition at index {i}: {key}")
        seen.add(key)
        buckets.setdefault(decision["lane"], []).append({**row, **decision})
    return {
        "status": "COMPETITION PRE-SCREEN COMPLETE",
        "input_competition_count": len(rows),
        "blocks": buckets,
        "routine_verification_count": sum(len(v) for k, v in buckets.items() if k in {
            "ROUTINE_LEAGUE_PROFILE", "CONDITIONAL_CHEAP_GATE",
            "PROTECTED_CONTEXT_REVIEW", "CUP_CHANNEL_REVIEW",
            "COVERAGE_AUDIT_PROOF_REQUIRED",
        }),
        "raw_ledger_retained": True,
    }
