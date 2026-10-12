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

from league_registry import COUNTRIES, norm

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


EREDIVISIE_HIGH_EVENT = {
    norm(x) for x in (
        "PSV", "PSV Eindhoven",
        "Feyenoord", "Feyenoord Rotterdam",
        "Ajax",
        "FC Groningen", "Groningen",
        "Excelsior",
        "Go Ahead Eagles",
        "FC Utrecht", "Utrecht",
        "Sparta Rotterdam",
    )
}

ICELAND_TOP_HIGH_EVENT = {
    norm(x) for x in (
        "KR", "KR Reykjavik", "KR Reykjavík",
        "Fram", "Fram Reykjavik", "Fram Reykjavík",
    )
}

ICELAND_FIRST_HIGH_EVENT = {
    norm(x) for x in (
        "Afturelding", "UMF Afturelding",
        "Fylkir", "Fylkir FC",
        "HK", "HK Kopavogur", "HK Kópavogur",
        "Aegir", "Ægir", "KF Aegir", "KF Ægir",
    )
}

FAROE_TOP_EVENT = {
    norm(x) for x in (
        "HB Torshavn", "HB Tórshavn",
        "NSI Runavik", "NSÍ Runavík",
        "EB Streymur", "EB / Streymur", "EB/Streymur",
    )
}

FAROE_FIRST_HIGH_EVENT = {
    norm(x) for x in (
        "B36 Torshavn II", "B36 Tórshavn II", "B36 II",
        "FC Suduroy", "FC Suðuroy", "Suduroy", "Suðuroy",
    )
}

NORWAY_ELITESERIEN_EVENT = {
    norm(x) for x in (
        "Viking", "Viking FK",
        "Bodo Glimt", "Bodø/Glimt", "FK Bodo Glimt",
        "Molde", "Molde FK",
        "Brann", "SK Brann",
        "Aalesund", "Aalesunds FK",
    )
}

NORWAY_FIRST_HIGH_EVENT = {
    norm(x) for x in (
        "Ranheim", "Ranheim Fotball",
        "Haugesund", "FK Haugesund",
        "Kongsvinger", "Kongsvinger IL",
        "Stromsgodset", "Strømsgodset", "Stromsgodset IF", "Strømsgodset IF",
    )
}

DENMARK_SUPERLIGA_EVENT = {
    norm(x) for x in (
        "FC Copenhagen", "FC Kobenhavn", "FC København",
        "AC Horsens", "Horsens",
    )
}

DENMARK_FIRST_EVENT = {
    norm(x) for x in (
        "Hvidovre", "Hvidovre IF",
        "Vejle", "Vejle Boldklub",
        "Hobro", "Hobro IK",
        "Esbjerg", "Esbjerg fB",
    )
}

SWEDEN_ALLSVENSKAN_EVENT = {
    norm(x) for x in (
        "Sirius", "IK Sirius", "IK Sirius Fotboll",
        "Malmo", "Malmö", "Malmo FF", "Malmö FF",
        "AIK",
        "Brommapojkarna", "IF Brommapojkarna",
    )
}

SWEDEN_SUPERETTAN_EVENT = {
    norm(x) for x in (
        "Falkenberg", "Falkenbergs FF",
        "Varberg", "Varbergs BoIS", "Varbergs BoIS FC",
        "Osters", "Östers", "Osters IF", "Östers IF",
        "IK Brage", "Brage",
        "Helsingborg", "Helsingborgs IF",
    )
}


ROMANIA_SUPERLIGA_EVENT = {
    norm(x) for x in (
        "Universitatea Cluj", "U Cluj", "FC Universitatea Cluj",
        "Universitatea Craiova", "CS Universitatea Craiova",
        "CFR Cluj", "CFR 1907 Cluj",
    )
}

ROMANIA_LIGA2_HIGH_EVENT = {
    norm(x) for x in (
        "CS Dinamo Bucuresti", "CS Dinamo București",
        "Popesti-Leordeni", "Popești-Leordeni", "CS Popesti Leordeni",
        "Concordia", "Concordia Chiajna",
        "Chindia Targoviste", "Chindia Târgoviște",
    )
}

POLAND_EKSTRA_HIGH_EVENT = {
    norm(x) for x in (
        "Rakow Czestochowa", "Raków Częstochowa",
        "Lech Poznan", "Lech Poznań",
        "Gornik Zabrze", "Górnik Zabrze",
        "Wisla Krakow", "Wisła Kraków",
    )
}

POLAND_ILIGA_EVENT = {
    norm(x) for x in (
        "Stal Mielec", "FKS Stal Mielec",
        "Warta Poznan", "Warta Poznań",
        "Nieciecza", "Bruk-Bet Termalica Nieciecza",
    )
}

SERBIA_SUPER_STRONG_EVENT = {
    norm(x) for x in (
        "Partizan", "FK Partizan", "Partizan Beograd",
    )
}

SERBIA_SUPER_EVENT = {
    norm(x) for x in (
        "OFK Beograd",
        "Vojvodina", "FK Vojvodina",
    )
}

SERBIA_PRVA_EVENT = {
    norm(x) for x in (
        "Javor Ivanjica", "FK Javor Ivanjica",
        "Borac Cacak", "Borac Čačak", "FK Borac Cacak", "FK Borac Čačak",
        "Backa Topola", "Bačka Topola", "FK Backa Topola", "FK Bačka Topola",
    )
}

CZECH_FIRST_STRONG_EVENT = {
    norm(x) for x in (
        "Sigma Olomouc", "SK Sigma Olomouc",
    )
}

CZECH_FIRST_EVENT = {
    norm(x) for x in (
        "Slavia Praha", "SK Slavia Praha",
        "Mlada Boleslav", "Mladá Boleslav",
        "Teplice", "FK Teplice",
        "Sparta Praha", "AC Sparta Praha",
        "Viktoria Plzen", "Viktoria Plzeň",
    )
}


BOLIVIA_LFPB_HIGH_EVENT = {
    norm(x) for x in (
        "Independiente Petrolero", "Club Independiente Petrolero",
        "Real Oruro", "CDT Real Oruro",
        "ABB", "Academia del Balompie Boliviano",
        "Bolivar", "Bolívar", "Club Bolivar", "Club Bolívar",
    )
}

CHILE_PRIMERA_HIGH_EVENT = {
    norm(x) for x in (
        "Universidad Catolica", "Universidad Católica", "CD Universidad Católica",
        "Cobresal", "CD Cobresal",
    )
}

PERU_LIGA1_HIGH_EVENT = {
    norm(x) for x in (
        "Juan Pablo II", "Juan Pablo II College",
        "FC Cajamarca", "Cajamarca",
        "Sporting Cristal", "Club Sporting Cristal",
    )
}

BRAZIL_SERIEA_EVENT = {
    norm(x) for x in (
        "Botafogo", "Botafogo FR",
        "Chapecoense", "Chapecoense AF",
        "Santos", "Santos FC", "Santos FC Sao Paulo",
    )
}

COLOMBIA_PRIMERA_EVENT = {
    norm(x) for x in (
        "La Equidad", "CD La Equidad", "CD La Equidad Seguros SA",
    )
}

PARAGUAY_PRIMERA_EVENT = {
    norm(x) for x in (
        "Recoleta", "CD Recoleta",
    )
}

URUGUAY_PRIMERA_EVENT = {
    norm(x) for x in (
        "CA Torque", "Torque", "Montevideo City Torque",
    )
}

VENEZUELA_PRIMERA_EVENT = {
    norm(x) for x in (
        "Rayo Zuliano", "Deportivo Rayo Zuliano",
    )
}

ARGENTINA_PRIMERA_EVENT = {
    norm(x) for x in (
        "Union Santa Fe", "Unión Santa Fe", "CA Union de Santa Fe", "CA Unión de Santa Fe",
    )
}

ECUADOR_SERIEA_STRONG_EVENT = {
    norm(x) for x in (
        "Independiente del Valle", "CSD Independiente del Valle",
    )
}

MLS_HIGH_EVENT = {
    norm(x) for x in (
        "FC Cincinnati", "Cincinnati",
    )
}

LIGA_MX_HIGH_EVENT = {
    norm(x) for x in (
        "Toluca", "Deportivo Toluca", "Deportivo Toluca FC",
        "Cruz Azul", "Cruz Azul FC",
        "FC Juarez", "FC Juárez", "Juarez", "Juárez",
        "Monterrey", "CF Monterrey",
    )
}

CANADA_CPL_HIGH_EVENT = {
    norm(x) for x in (
        "York United", "York United FC", "York9", "York9 FC",
        "Pacific", "Pacific FC",
        "Atletico Ottawa", "Atlético Ottawa",
    )
}

USL_CHAMP_EVENT = {
    norm(x) for x in (
        "Jacksonville Armada", "Jacksonville Armada FC",
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
    country = norm(fixture.get("country"))
    return COUNTRIES.get(country, country), norm(fixture.get("competition"))


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

    # Netherlands Eredivisie is currently a genuinely high-goal environment,
    # but the season is still young enough that extreme team priors remain
    # time-bounded. League base is SECONDARY; the clearest high-event teams are PRIMARY.
    if country == "netherlands" and _contains(comp, "eredivisie"):
        if teams & EREDIVISIE_HIGH_EVENT:
            priority, reason = PRIMARY, "EREDIVISIE_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "EREDIVISIE_HIGH_GOAL_LEAGUE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "NED_EREDIVISIE_2026_27",
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

    if country == "iceland":
        if _contains(comp, "besta deild", "urvalsdeild"):
            if teams & ICELAND_TOP_HIGH_EVENT:
                priority, reason = PRIMARY, "ICELAND_TOP_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "ICELAND_TOP_HIGH_GOAL_LEAGUE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "ISL_BESTA_2026",
            }
        if _contains(comp, "lengjudeild", "1 deild"):
            if teams & ICELAND_FIRST_HIGH_EVENT:
                priority, reason = PRIMARY, "ICELAND_FIRST_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "ICELAND_FIRST_HIGH_GOAL_LEAGUE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "ISL_LENGJUDEILD_2026",
                "requires_competition_phase_context": True,
            }
        if _contains(comp, "2 deild"):
            return {
                **base, "priority": DEFERRED,
                "priority_rank": PRIORITY_RANK[DEFERRED],
                "reason": "ICELAND_SECOND_HIGH_GOAL_LOW_DATA_PILOT",
                "league_profile": "ISL_2_DEILD_2026",
                "requires_team_identity_check": True,
            }

    if country == "faroe islands":
        if _contains(comp, "meistaradeildin", "faroe islands premier league", "betri deildin"):
            if teams & FAROE_TOP_EVENT:
                priority, reason = SECONDARY, "FAROE_TOP_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "FAROE_TOP_SELECTIVE_GOAL_ENVIRONMENT"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "FRO_MEISTARADEILDIN_2026",
            }
        if _contains(comp, "1 deild"):
            if teams & FAROE_FIRST_HIGH_EVENT:
                priority, reason = PRIMARY, "FAROE_FIRST_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "FAROE_FIRST_EXTREME_GOAL_ENVIRONMENT"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "FRO_1_DEILD_2026",
                "requires_team_identity_check": True,
            }

    if country == "norway":
        if _contains(comp, "eliteserien"):
            if teams & NORWAY_ELITESERIEN_EVENT:
                priority, reason = SECONDARY, "NORWAY_ELITESERIEN_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "NORWAY_ELITESERIEN_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "NOR_ELITESERIEN_2026",
            }
        if _contains(comp, "obos", "1 divisjon", "norway first division"):
            if teams & NORWAY_FIRST_HIGH_EVENT:
                priority, reason = PRIMARY, "NORWAY_FIRST_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "NORWAY_FIRST_HIGH_GOAL_LEAGUE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "NOR_FIRST_2026",
            }

    if country == "denmark":
        if _contains(comp, "superliga") and not _contains(comp, "1st", "1 division"):
            if teams & DENMARK_SUPERLIGA_EVENT:
                priority, reason = SECONDARY, "DENMARK_SUPERLIGA_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "DENMARK_SUPERLIGA_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "DEN_SUPERLIGA_2026_27",
            }
        if _contains(comp, "1st division", "danish first division", "1 division"):
            if teams & DENMARK_FIRST_EVENT:
                priority, reason = SECONDARY, "DENMARK_FIRST_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "DENMARK_FIRST_DRAW_TRAP_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "DEN_FIRST_2026_27",
                "draw_trap_caution": True,
            }

    if country == "sweden":
        if _contains(comp, "allsvenskan"):
            if teams & SWEDEN_ALLSVENSKAN_EVENT:
                priority, reason = SECONDARY, "SWEDEN_ALLSVENSKAN_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "SWEDEN_ALLSVENSKAN_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "SWE_ALLSVENSKAN_2026",
            }
        if _contains(comp, "superettan"):
            if teams & SWEDEN_SUPERETTAN_EVENT:
                priority, reason = SECONDARY, "SWEDEN_SUPERETTAN_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "SWEDEN_SUPERETTAN_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "SWE_SUPERETTAN_2026",
            }

    if country == "romania":
        # Check Liga II before Liga I because normalized "liga ii" contains
        # the literal "liga i".
        if _contains(comp, "liga ii", "liga 2"):
            if teams & ROMANIA_LIGA2_HIGH_EVENT:
                priority, reason = PRIMARY, "ROMANIA_LIGA2_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "ROMANIA_LIGA2_GOAL_POSITIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "ROU_LIGA2_2026_27",
            }
        if _contains(comp, "superliga", "liga i", "liga 1"):
            if teams & ROMANIA_SUPERLIGA_EVENT:
                priority, reason = SECONDARY, "ROMANIA_SUPERLIGA_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "ROMANIA_SUPERLIGA_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "ROU_SUPERLIGA_2026_27",
            }

    if country == "poland":
        if _contains(comp, "ekstraklasa"):
            if teams & POLAND_EKSTRA_HIGH_EVENT:
                priority, reason = PRIMARY, "POLAND_EKSTRA_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "POLAND_EKSTRA_GOAL_POSITIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "POL_EKSTRA_2026_27",
            }
        if _contains(comp, "i liga", "1 liga", "liga 1", "betclic 1 liga"):
            if teams & POLAND_ILIGA_EVENT:
                priority, reason = SECONDARY, "POLAND_ILIGA_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "POLAND_ILIGA_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "POL_ILIGA_2026_27",
                "draw_trap_caution": True,
            }

    if country == "serbia":
        if _contains(comp, "super liga", "superliga", "mozzart bet super liga"):
            if teams & SERBIA_SUPER_STRONG_EVENT:
                priority, reason = PRIMARY, "SERBIA_SUPER_CURRENT_STRONG_EVENT_TEAM"
            elif teams & SERBIA_SUPER_EVENT:
                priority, reason = SECONDARY, "SERBIA_SUPER_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "SERBIA_SUPER_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "SRB_SUPERLIGA_2026_27",
            }
        if _contains(comp, "prva liga", "first league", "mozzart bet prva liga"):
            if teams & SERBIA_PRVA_EVENT:
                priority, reason = SECONDARY, "SERBIA_PRVA_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "SERBIA_PRVA_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "SRB_PRVA_2026_27",
                "draw_trap_caution": True,
            }

    if country == "czechia":
        if _contains(comp, "fnl", "national football league", "chance narodni liga"):
            return {
                **base, "priority": SECONDARY,
                "priority_rank": PRIORITY_RANK[SECONDARY],
                "reason": "CZECH_FNL_GOAL_POSITIVE_BASE",
                "league_profile": "CZE_FNL_2026_27",
            }
        if _contains(comp, "czech first league", "first league", "czech first division", "chance liga"):
            if teams & CZECH_FIRST_STRONG_EVENT:
                priority, reason = PRIMARY, "CZECH_FIRST_CURRENT_STRONG_EVENT_TEAM"
            elif teams & CZECH_FIRST_EVENT:
                priority, reason = SECONDARY, "CZECH_FIRST_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "CZECH_FIRST_SELECTIVE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "CZE_FIRST_2026_27",
            }

    if country == "bolivia" and _contains(comp, "lfpb", "division profesional", "primera division"):
        if teams & BOLIVIA_LFPB_HIGH_EVENT:
            priority, reason = PRIMARY, "BOLIVIA_LFPB_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "BOLIVIA_LFPB_HIGH_GOAL_LEAGUE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "BOL_LFPB_2026",
        }

    if country == "chile" and _contains(comp, "primera division", "liga de primera", "campeonato nacional"):
        if teams & CHILE_PRIMERA_HIGH_EVENT:
            priority, reason = PRIMARY, "CHILE_PRIMERA_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "CHILE_PRIMERA_GOAL_POSITIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "CHI_PRIMERA_2026",
        }

    if country == "peru" and _contains(comp, "liga 1", "primera division"):
        if teams & PERU_LIGA1_HIGH_EVENT:
            priority, reason = PRIMARY, "PERU_LIGA1_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "PERU_LIGA1_GOAL_POSITIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "PER_LIGA1_2026",
        }

    if country == "brazil" and _contains(comp, "serie a", "brasileirao serie a", "campeonato brasileiro serie a"):
        if teams & BRAZIL_SERIEA_EVENT:
            priority, reason = SECONDARY, "BRAZIL_SERIEA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "BRAZIL_SERIEA_SELECTIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "BRA_SERIEA_2026",
        }

    if country == "colombia" and _contains(comp, "categoria primera a", "primera a", "liga betplay"):
        if teams & COLOMBIA_PRIMERA_EVENT:
            priority, reason = SECONDARY, "COLOMBIA_PRIMERA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "COLOMBIA_PRIMERA_SELECTIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "COL_PRIMERA_A_2026",
        }

    if country == "paraguay" and _contains(comp, "division profesional", "primera division", "copa de primera"):
        if teams & PARAGUAY_PRIMERA_EVENT:
            priority, reason = SECONDARY, "PARAGUAY_PRIMERA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "PARAGUAY_PRIMERA_LOW_CONTINUATION_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "PAR_PRIMERA_2026",
            "draw_trap_caution": True,
        }

    if country == "uruguay" and _contains(comp, "primera division", "liga auf"):
        if teams & URUGUAY_PRIMERA_EVENT:
            priority, reason = SECONDARY, "URUGUAY_PRIMERA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "URUGUAY_PRIMERA_LOW_GOAL_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "URU_PRIMERA_2026",
            "draw_trap_caution": True,
        }

    if country == "venezuela" and _contains(comp, "primera division", "liga futve"):
        if teams & VENEZUELA_PRIMERA_EVENT:
            priority, reason = SECONDARY, "VENEZUELA_PRIMERA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "VENEZUELA_PRIMERA_DRAW_TRAP_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "VEN_PRIMERA_2026",
            "draw_trap_caution": True,
        }

    if country == "argentina" and _contains(comp, "primera division", "liga profesional"):
        if teams & ARGENTINA_PRIMERA_EVENT:
            priority, reason = SECONDARY, "ARGENTINA_PRIMERA_CURRENT_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "ARGENTINA_PRIMERA_LOW_GOAL_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "ARG_PRIMERA_2026",
            "draw_trap_caution": True,
        }

    if country == "ecuador" and _contains(comp, "serie a", "liga pro", "primera categoria serie a"):
        if teams & ECUADOR_SERIEA_STRONG_EVENT:
            priority, reason = PRIMARY, "ECUADOR_SERIEA_CURRENT_STRONG_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "ECUADOR_SERIEA_LOW_GOAL_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "ECU_SERIEA_2026",
            "draw_trap_caution": True,
        }

    if country == "united states":
        if _contains(comp, "mls", "major league soccer"):
            if teams & MLS_HIGH_EVENT:
                priority, reason = PRIMARY, "MLS_CURRENT_HIGH_EVENT_TEAM"
            else:
                priority, reason = SECONDARY, "MLS_HIGH_GOAL_LEAGUE_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "USA_MLS_2026",
            }
        if _contains(comp, "usl championship"):
            if teams & USL_CHAMP_EVENT:
                priority, reason = SECONDARY, "USL_CHAMP_CURRENT_EVENT_TEAM"
            else:
                priority, reason = DEFERRED, "USL_CHAMP_HETEROGENEOUS_BASE"
            return {
                **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
                "reason": reason, "league_profile": "USA_USL_CHAMP_2026",
            }

    if country == "mexico" and _contains(comp, "liga mx"):
        if teams & LIGA_MX_HIGH_EVENT:
            priority, reason = PRIMARY, "LIGA_MX_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = DEFERRED, "LIGA_MX_SELECTIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "MEX_LIGA_MX_2026_27",
        }

    if country == "canada" and _contains(comp, "canadian premier league", "cpl"):
        if teams & CANADA_CPL_HIGH_EVENT:
            priority, reason = PRIMARY, "CANADA_CPL_CURRENT_HIGH_EVENT_TEAM"
        else:
            priority, reason = SECONDARY, "CANADA_CPL_GOAL_POSITIVE_BASE"
        return {
            **base, "priority": priority, "priority_rank": PRIORITY_RANK[priority],
            "reason": reason, "league_profile": "CAN_CPL_2026",
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
