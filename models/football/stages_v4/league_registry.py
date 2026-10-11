"""V4 football intake: exact country/competition registry from approved league research.

Registered is not a claim of XI/odds availability, a predicted goal total or
a wager. Conditional/pilot paths stay visible but cannot become an official
board without source-backed match research.
"""
from __future__ import annotations

import re
from typing import Any

def norm(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())

COUNTRIES = {
    "uk": "england", "england": "england",
    "deutschland": "germany", "brasil": "brazil",
    "the netherlands": "netherlands", "holland": "netherlands",
    "czech republic": "czechia", "czechia": "czechia",
    "korea": "south korea", "republic of korea": "south korea",
    "uae": "united arab emirates", "united arab emirates": "united arab emirates",
    "hong kong sar": "hong kong", "hong kong": "hong kong",
    "usa": "united states", "us": "united states",
}
DOMESTIC_EXCLUSIONS = frozenset({
    "bangladesh","israel","kenya","iraq","wales","kuwait","finland",
})
# Never admit generic Premier League/Serie A without the country.
# Denmark, Sweden and Norway were researched and must be in the core pool.
ROUTINE = {
    "england": "premier league|english premier league",
    "germany": "bundesliga|german bundesliga|2 bundesliga|2nd bundesliga",
    "spain": "la liga|laliga",
    "italy": "serie a|italian serie a",
    "france": "ligue 1|french ligue 1",
    "netherlands": "eredivisie|eerste divisie|eerstedivisie",
    "norway": "eliteserien|obos ligaen|obos league|1 divisjon|norway first division",
    "sweden": "allsvenskan",
    "denmark": "superliga|danish superliga",
    "belgium": "pro league|belgian pro league|first division a",
    "portugal": "primeira liga",
    "austria": "bundesliga",
    "scotland": "premiership|scottish premiership",
    "switzerland": "super league|swiss super league",
    "japan": "j1 league|j2 league",
    "south korea": "k league 1",
    "saudi arabia": "saudi pro league",
}
CONDITIONAL = {
    "england": "championship|efl championship",
    "spain": "segunda division|la liga 2",
    "czechia": "czech first league|first league|czech first division|fnl|czech fnl|national football league",
    "poland": "ekstraklasa",
    "hong kong": "hong kong premier league|boc life hong kong premier league|premier league",
    "malaysia": "malaysia super league|liga super|super league",
    "united arab emirates": "uae pro league|adnoc pro league",
    "qatar": "qatar stars league|stars league",
    "south korea": "k league 2",
    "greece": "super league|greek super league",
}
# All researched countries below stay searchable, but are evidence-gated.
# "Pilot" is not an invitation to all unknown divisions from that country.
PILOT = {
    "thailand": "thai league 1|thai league 2",
    "indonesia": "liga 1|super league indonesia",
    "saudi arabia": "first division league|saudi first division",
    "sweden": "superettan",
    "denmark": "1st division|danish first division",
    "japan": "we league cup",
}
EXCLUDED_EXACT = {
    ("germany", "3 liga"), ("germany", "3 liga germany"),
    ("italy", "serie b"), ("france", "ligue 2"), 
    ("norway", "2 divisjon"), ("norway", "3 divisjon"),
}
COMPETITIVE_KINDS = {
    "DOMESTIC_LEAGUE", "WOMENS_TOP_FLIGHT", "DOMESTIC_CUP",
    "CONTINENTAL", "PROTECTED_OFFICIAL",
}
CUPS = {
    ("england", "fa cup"), ("england", "efl cup"),
    ("germany", "dfb pokal"), ("spain", "copa del rey"),
    ("italy", "coppa italia"), ("france", "coupe de france"),
    ("netherlands", "knvb beker"), ("portugal", "taca de portugal"),
    ("japan", "we league cup"),
}

def registry() -> dict[str, dict[str, set[str]]]:
    return {
        lane: {country: {norm(x) for x in options.split("|")}
               for country, options in mapping.items()}
        for lane, mapping in (
            ("ROUTINE", ROUTINE), ("CONDITIONAL", CONDITIONAL), ("PILOT", PILOT)
        )
    }

REGISTRY = registry()

def classify(fixture: dict[str, Any]) -> dict[str, str]:
    country = norm(fixture.get("country"))
    country = COUNTRIES.get(country, country)
    competition = norm(fixture.get("competition"))
    kind = fixture.get("competition_kind")
    if not country or not competition or kind not in COMPETITIVE_KINDS:
        return {"lane": "UNVERIFIED", "reason": "COUNTRY_COMPETITION_KIND_REQUIRED"}
    if (fixture.get("is_friendly") is True or "friendly" in competition
            or "friendlies" in competition):
        return {"lane": "EXCLUDED", "reason": "NONCOMPETITIVE_FRIENDLIES"}
    if kind in {"DOMESTIC_LEAGUE","WOMENS_TOP_FLIGHT","DOMESTIC_CUP"} and country in DOMESTIC_EXCLUSIONS:
        return {"lane": "EXCLUDED", "reason": "USER_DOMESTIC_COUNTRY_EXCLUSION"}
    if (country, competition) in EXCLUDED_EXACT:
        return {"lane": "EXCLUDED", "reason": "USER_EXPLICIT_LEAGUE_EXCLUSION"}
    if kind == "WOMENS_TOP_FLIGHT":
        return {"lane": "CONDITIONAL", "reason": "WOMENS_SENIOR_TOP_FLIGHT_SOURCE_AND_IDENTITY_CHECK"}
    if kind in {"CONTINENTAL", "PROTECTED_OFFICIAL"}:
        return {"lane": "CONDITIONAL", "reason": "OFFICIAL_TOURNAMENT_FORMAT_INCENTIVES_REQUIRED"}
    if kind == "DOMESTIC_CUP":
        if (country, competition) in CUPS:
            return {"lane": "CONDITIONAL", "reason": "MAJOR_CUP_MATCH_FORMAT_REQUIRED"}
        return {"lane": "DISCOVERY", "reason": "UNREGISTERED_OFFICIAL_CUP_GOAL_RESEARCH_REQUIRED"}
    for lane in ("ROUTINE", "CONDITIONAL", "PILOT"):
        if competition in REGISTRY[lane].get(country, set()):
            return {"lane": lane, "reason": "RESEARCHED_LEAGUE_" + lane}
    # An unknown competition is NOT automatically a poor-goals fixture.
    # It enters a separate source-backed discovery screen, never routine.
    # League registration is a familiarity prior, NOT the football filter.
    return {"lane": "DISCOVERY", "reason": "UNREGISTERED_COMPETITIVE_LEAGUE_GOAL_RESEARCH_REQUIRED"}
