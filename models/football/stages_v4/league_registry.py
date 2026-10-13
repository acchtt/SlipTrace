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
    "faroe island": "faroe islands", "faroes": "faroe islands", "faroe": "faroe islands",
    "czech republic": "czechia", "czechia": "czechia",
    "korea": "south korea", "republic of korea": "south korea",
    "uae": "united arab emirates", "united arab emirates": "united arab emirates",
    "hong kong sar": "hong kong", "hong kong": "hong kong",
    "usa": "united states", "us": "united states",
    "cape verde": "cabo verde",
    "swaziland": "eswatini",
    "dr congo": "democratic republic of the congo",
    "congo dr": "democratic republic of the congo",
    "congo drc": "democratic republic of the congo",
    "d r congo": "democratic republic of the congo",
    "democratic republic of congo": "democratic republic of the congo",
    "congo democratic republic": "democratic republic of the congo",
    "republic of congo": "congo",
    "republic of the congo": "congo",
    "the gambia": "gambia",
    "cote d ivoire": "ivory coast",
    "c te d ivoire": "ivory coast",
    "s o tom and pr ncipe": "sao tome and principe",
    "r union": "reunion",
}
AFRICAN_DOMESTIC_COUNTRIES = frozenset({
    "algeria", "angola", "benin", "botswana", "burkina faso", "burundi",
    "cabo verde", "cameroon", "central african republic", "chad", "comoros",
    "congo", "democratic republic of the congo", "djibouti", "egypt",
    "equatorial guinea", "eritrea", "eswatini", "ethiopia", "gabon",
    "gambia", "ghana", "guinea", "guinea bissau", "ivory coast", "kenya",
    "lesotho", "liberia", "libya", "madagascar", "malawi", "mali",
    "mauritania", "mauritius", "morocco", "mozambique", "namibia", "niger",
    "nigeria", "rwanda", "sao tome and principe", "senegal", "seychelles",
    "sierra leone", "somalia", "south africa", "south sudan", "sudan",
    "tanzania", "togo", "tunisia", "uganda", "zambia", "zimbabwe",
    # Provider/regional labels that still represent African domestic football.
    "zanzibar", "reunion", "mayotte", "western sahara",
})
DOMESTIC_EXCLUSIONS = frozenset({
    "bangladesh","israel","kenya","iraq","wales","kuwait",
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
    "finland": "veikkausliiga|finnish veikkausliiga",
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
    "poland": "ekstraklasa|pko bank polski ekstraklasa|pkobp ekstraklasa|i liga|1 liga|liga 1|betclic 1 liga",
    "hong kong": "hong kong premier league|boc life hong kong premier league|premier league",
    "malaysia": "malaysia super league|liga super|super league",
    "united arab emirates": "uae pro league|adnoc pro league",
    "qatar": "qatar stars league|stars league",
    "south korea": "k league 2",
    "greece": "super league|greek super league",
    "romania": "superliga|superliga romaniei|liga i|liga 1|liga ii|liga 2",
    "serbia": "super liga|superliga|mozzart bet super liga|prva liga|first league|mozzart bet prva liga",
    "czechia": "czech first league|first league|czech first division|chance liga|fnl|czech fnl|national football league|chance narodni liga",
    "iceland": "besta deild karla|besta deild|urvalsdeild|urvalsdeild karla|lengjudeild karla|lengjudeild|1 deild|1 deild karla",
    "faroe islands": "meistaradeildin|meistaradeildin menn|faroe islands premier league|betri deildin|betri deildin menn",
    "sweden": "superettan",
    "denmark": "1st division|danish first division|1 division",
    "japan": "we league|women empowerment league|nadeshiko league 1|nadeshiko 1|nadeshiko league 2|nadeshiko 2",
}
# All researched countries below stay searchable, but are evidence-gated.
# "Pilot" is not an invitation to all unknown divisions from that country.
PILOT = {
    "thailand": "thai league 1|thai league 2",
    "indonesia": "liga 1|super league indonesia",
    "saudi arabia": "first division league|saudi first division",
    "iceland": "2 deild|2 deild karla",
    "faroe islands": "1 deild|1 deild menn",
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
    ("japan", "we league kracie cup"),
    ("japan", "kracie cup"),
    ("japan", "empress cup"),
    ("japan", "empress s cup"),
    ("japan", "empress s cup women"),
    ("japan", "jfa empress s cup"),
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
    if kind in {"DOMESTIC_LEAGUE","WOMENS_TOP_FLIGHT","DOMESTIC_CUP"} and country in AFRICAN_DOMESTIC_COUNTRIES:
        return {"lane": "EXCLUDED", "reason": "USER_AFRICA_DOMESTIC_EXCLUSION"}
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
