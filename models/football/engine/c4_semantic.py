from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


SCHEMA_VERSION = "football-c4-semantic-v1"

TRI = {"VERIFIED", "PARTIAL", "NONE"}
PERSONNEL = {"INTACT", "PARTIAL", "DAMAGED"}
COVERAGE = {"COMPLETE", "PARTIAL", "MISSING"}
DRAW_UTILITY = {"VERIFIED", "NOT_APPLICABLE", "NONE"}

ROUTE_SCORE = {"WEAK": 0, "USABLE": 1, "STRONG": 2}
GRADE_SCORE = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
FUNDING_SCORE = {"NONE": 0, "PARTIAL": 1, "VERIFIED": 2}
CARRIER_SCORE = {"NONE": 0, "USABLE": 1, "STRONG": 2}
STATE_SCORE = {"C4-PASS": 0, "C4-WATCH": 1, "C4-FOCUS": 2}
CONTROL_SCORE = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}


class C4ContractError(ValueError):
    pass


@dataclass(frozen=True)
class Anchor:
    state: str
    basis: str


@dataclass(frozen=True)
class SideEvidence:
    creation_repeatability: Anchor
    dangerous_access: Anchor
    service_finishing_continuity: Anchor
    matched_opponent_leakage: Anchor
    personnel_integrity: Anchor
    route_suppression: Anchor
    multi_goal_repeatability: Anchor


@dataclass(frozen=True)
class MatchEvidence:
    match_id: str
    common_evidence_basis: str
    home: SideEvidence
    away: SideEvidence
    mechanism_evidence_coverage: Anchor
    team_news_coverage: Anchor
    competition_context_coverage: Anchor
    continuation_after_first_goal: Anchor
    lead_control_tendency: Anchor
    draw_utility: Anchor
    mechanism_failure: Anchor
    match_suppression: Anchor
    upper_tail_repeatability: Anchor


def _nonempty(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise C4ContractError(f"{field} must be a non-empty string")
    return value.strip()


def _anchor(obj: Any, field: str, allowed: set[str]) -> Anchor:
    if not isinstance(obj, dict):
        raise C4ContractError(f"{field} must be an object with state+basis")
    state = _nonempty(obj.get("state"), f"{field}.state").upper()
    basis = _nonempty(obj.get("basis"), f"{field}.basis")
    if state not in allowed:
        raise C4ContractError(
            f"{field}.state must be one of {sorted(allowed)}, got {state!r}"
        )
    return Anchor(state=state, basis=basis)


def _side(obj: Any, side: str) -> SideEvidence:
    if not isinstance(obj, dict):
        raise C4ContractError(f"{side} must be an object")
    return SideEvidence(
        creation_repeatability=_anchor(
            obj.get("creation_repeatability"),
            f"{side}.creation_repeatability",
            TRI,
        ),
        dangerous_access=_anchor(
            obj.get("dangerous_access"),
            f"{side}.dangerous_access",
            TRI,
        ),
        service_finishing_continuity=_anchor(
            obj.get("service_finishing_continuity"),
            f"{side}.service_finishing_continuity",
            TRI,
        ),
        matched_opponent_leakage=_anchor(
            obj.get("matched_opponent_leakage"),
            f"{side}.matched_opponent_leakage",
            TRI,
        ),
        personnel_integrity=_anchor(
            obj.get("personnel_integrity"),
            f"{side}.personnel_integrity",
            PERSONNEL,
        ),
        route_suppression=_anchor(
            obj.get("route_suppression"),
            f"{side}.route_suppression",
            TRI,
        ),
        multi_goal_repeatability=_anchor(
            obj.get("multi_goal_repeatability"),
            f"{side}.multi_goal_repeatability",
            TRI,
        ),
    )


def parse_match(obj: Any) -> MatchEvidence:
    if not isinstance(obj, dict):
        raise C4ContractError("match must be an object")

    return MatchEvidence(
        match_id=_nonempty(obj.get("match_id"), "match_id"),
        common_evidence_basis=_nonempty(
            obj.get("common_evidence_basis"), "common_evidence_basis"
        ),
        home=_side(obj.get("home"), "home"),
        away=_side(obj.get("away"), "away"),
        mechanism_evidence_coverage=_anchor(
            obj.get("mechanism_evidence_coverage"),
            "mechanism_evidence_coverage",
            COVERAGE,
        ),
        team_news_coverage=_anchor(
            obj.get("team_news_coverage"),
            "team_news_coverage",
            COVERAGE,
        ),
        competition_context_coverage=_anchor(
            obj.get("competition_context_coverage"),
            "competition_context_coverage",
            COVERAGE,
        ),
        continuation_after_first_goal=_anchor(
            obj.get("continuation_after_first_goal"),
            "continuation_after_first_goal",
            TRI,
        ),
        lead_control_tendency=_anchor(
            obj.get("lead_control_tendency"),
            "lead_control_tendency",
            TRI,
        ),
        draw_utility=_anchor(
            obj.get("draw_utility"),
            "draw_utility",
            DRAW_UTILITY,
        ),
        mechanism_failure=_anchor(
            obj.get("mechanism_failure"),
            "mechanism_failure",
            TRI,
        ),
        match_suppression=_anchor(
            obj.get("match_suppression"),
            "match_suppression",
            TRI,
        ),
        upper_tail_repeatability=_anchor(
            obj.get("upper_tail_repeatability"),
            "upper_tail_repeatability",
            TRI,
        ),
    )


def compile_route(side: SideEvidence) -> str:
    if (
        side.creation_repeatability.state == "VERIFIED"
        and side.personnel_integrity.state != "DAMAGED"
        and side.route_suppression.state != "VERIFIED"
        and (
            side.dangerous_access.state == "VERIFIED"
            or side.matched_opponent_leakage.state == "VERIFIED"
        )
        and side.service_finishing_continuity.state != "NONE"
    ):
        return "STRONG"

    support = (
        side.creation_repeatability,
        side.dangerous_access,
        side.service_finishing_continuity,
        side.matched_opponent_leakage,
    )
    supportive = sum(a.state in {"PARTIAL", "VERIFIED"} for a in support)
    verified = sum(a.state == "VERIFIED" for a in support)

    if (
        side.personnel_integrity.state != "DAMAGED"
        and side.route_suppression.state != "VERIFIED"
        and supportive >= 2
        and verified >= 1
    ):
        return "USABLE"

    return "WEAK"


def compile_carrier(
    home_route: str,
    away_route: str,
    home: SideEvidence,
    away: SideEvidence,
) -> tuple[str, str]:
    strong_sides: list[str] = []
    usable_sides: list[str] = []

    for side_name, route, side in (
        ("HOME", home_route, home),
        ("AWAY", away_route, away),
    ):
        if route == "STRONG" and side.multi_goal_repeatability.state == "VERIFIED":
            strong_sides.append(side_name)
        if (
            ROUTE_SCORE[route] >= ROUTE_SCORE["USABLE"]
            and side.multi_goal_repeatability.state in {"PARTIAL", "VERIFIED"}
        ):
            usable_sides.append(side_name)

    if strong_sides:
        return "STRONG", "BOTH" if len(strong_sides) == 2 else strong_sides[0]
    if usable_sides:
        return "USABLE", "BOTH" if len(usable_sides) == 2 else usable_sides[0]
    return "NONE", "NONE"


def compile_chance_quality(
    home: SideEvidence,
    away: SideEvidence,
    home_route: str,
    away_route: str,
) -> str:
    for side in (home, away):
        if (
            side.creation_repeatability.state == "VERIFIED"
            and side.dangerous_access.state == "VERIFIED"
            and side.personnel_integrity.state != "DAMAGED"
        ):
            return "HIGH"

    if max(ROUTE_SCORE[home_route], ROUTE_SCORE[away_route]) >= ROUTE_SCORE["USABLE"]:
        return "MEDIUM"
    return "LOW"


def compile_evidence_confidence(m: MatchEvidence) -> str:
    states = (
        m.mechanism_evidence_coverage.state,
        m.team_news_coverage.state,
        m.competition_context_coverage.state,
    )
    if all(state == "COMPLETE" for state in states):
        return "HIGH"
    if all(state != "MISSING" for state in states):
        return "MEDIUM"
    return "LOW"


def compile_continuation(m: MatchEvidence) -> str:
    return {
        "VERIFIED": "HIGH",
        "PARTIAL": "MEDIUM",
        "NONE": "LOW",
    }[m.continuation_after_first_goal.state]


def compile_control_risk(m: MatchEvidence) -> str:
    continuation = m.continuation_after_first_goal.state
    lead = m.lead_control_tendency.state
    draw = m.draw_utility.state

    if lead == "VERIFIED" or (draw == "VERIFIED" and continuation != "VERIFIED"):
        return "HIGH"
    if lead == "PARTIAL" or continuation == "PARTIAL":
        return "MEDIUM"
    if continuation == "VERIFIED" and lead == "NONE" and draw != "VERIFIED":
        return "LOW"
    return "MEDIUM"


def compile_failure_resistance(m: MatchEvidence) -> str:
    failure = m.mechanism_failure.state
    suppression = m.match_suppression.state
    if "VERIFIED" in {failure, suppression}:
        return "LOW"
    if "PARTIAL" in {failure, suppression}:
        return "MEDIUM"
    return "HIGH"


def compile_funding(
    m: MatchEvidence,
    home_route: str,
    away_route: str,
    carrier: str,
    control_risk: str,
    failure_resistance: str,
    evidence_confidence: str,
) -> tuple[str, str]:
    continuation = m.continuation_after_first_goal.state
    no_verified_veto = (
        m.mechanism_failure.state != "VERIFIED"
        and m.match_suppression.state != "VERIFIED"
    )
    two_route = (
        ROUTE_SCORE[home_route] >= ROUTE_SCORE["USABLE"]
        and ROUTE_SCORE[away_route] >= ROUTE_SCORE["USABLE"]
        and max(ROUTE_SCORE[home_route], ROUTE_SCORE[away_route])
        == ROUTE_SCORE["STRONG"]
    )

    goal3_verified = (
        carrier == "STRONG"
        and continuation == "VERIFIED"
        and no_verified_veto
    ) or (
        two_route
        and continuation == "VERIFIED"
        and control_risk != "HIGH"
        and no_verified_veto
    )

    if goal3_verified:
        goal3 = "VERIFIED"
    elif (
        (
            max(ROUTE_SCORE[home_route], ROUTE_SCORE[away_route])
            == ROUTE_SCORE["STRONG"]
            or (
                ROUTE_SCORE[home_route] >= ROUTE_SCORE["USABLE"]
                and ROUTE_SCORE[away_route] >= ROUTE_SCORE["USABLE"]
            )
        )
        and failure_resistance != "LOW"
        and evidence_confidence != "LOW"
    ):
        goal3 = "PARTIAL"
    else:
        goal3 = "NONE"

    if (
        goal3 == "VERIFIED"
        and carrier == "STRONG"
        and m.upper_tail_repeatability.state == "VERIFIED"
        and continuation == "VERIFIED"
        and control_risk == "LOW"
    ):
        goal4 = "VERIFIED"
    elif (
        goal3 == "VERIFIED"
        and m.upper_tail_repeatability.state in {"PARTIAL", "VERIFIED"}
        and continuation != "NONE"
        and control_risk != "HIGH"
    ):
        goal4 = "PARTIAL"
    else:
        goal4 = "NONE"

    return goal3, goal4


def compile_supported_line(goal3: str, goal4: str) -> float | None:
    if goal3 == "NONE":
        return None
    if goal3 == "PARTIAL":
        return 2.0
    if goal4 == "VERIFIED":
        return 3.0
    if goal4 == "PARTIAL":
        return 2.75
    return 2.5


def compile_state(
    goal3: str,
    control_risk: str,
    failure_resistance: str,
    evidence_confidence: str,
    material_suppression: bool,
    supported_line: float | None,
) -> str:
    if (
        goal3 == "VERIFIED"
        and control_risk == "LOW"
        and GRADE_SCORE[failure_resistance] >= GRADE_SCORE["MEDIUM"]
        and evidence_confidence == "HIGH"
        and not material_suppression
        and supported_line is not None
    ):
        return "C4-FOCUS"

    if (
        supported_line is not None
        and goal3 in {"PARTIAL", "VERIFIED"}
        and control_risk != "HIGH"
        and failure_resistance != "LOW"
        and evidence_confidence != "LOW"
    ):
        return "C4-WATCH"

    return "C4-PASS"


def compile_match(m: MatchEvidence) -> dict[str, Any]:
    home_route = compile_route(m.home)
    away_route = compile_route(m.away)
    carrier, carrier_side = compile_carrier(home_route, away_route, m.home, m.away)
    chance_quality = compile_chance_quality(m.home, m.away, home_route, away_route)
    evidence_confidence = compile_evidence_confidence(m)
    continuation_quality = compile_continuation(m)
    control_risk = compile_control_risk(m)
    failure_resistance = compile_failure_resistance(m)
    goal3, goal4 = compile_funding(
        m,
        home_route,
        away_route,
        carrier,
        control_risk,
        failure_resistance,
        evidence_confidence,
    )
    supported_line = compile_supported_line(goal3, goal4)
    material_suppression = m.match_suppression.state == "VERIFIED"
    failure_attacks_route = m.mechanism_failure.state == "VERIFIED"
    state = compile_state(
        goal3,
        control_risk,
        failure_resistance,
        evidence_confidence,
        material_suppression,
        supported_line,
    )

    trace = [
        f"routes={home_route}/{away_route}",
        f"carrier={carrier}:{carrier_side}",
        f"chance={chance_quality}",
        f"evidence={evidence_confidence}",
        f"continuation={continuation_quality}",
        f"control={control_risk}",
        f"failure_resistance={failure_resistance}",
        f"goal3={goal3}",
        f"goal4={goal4}",
        f"supported_line={supported_line if supported_line is not None else 'NONE'}",
        f"state={state}",
    ]

    return {
        "match_id": m.match_id,
        "c4_state": state,
        "c4_home_route": home_route,
        "c4_away_route": away_route,
        "c4_carrier": carrier,
        "c4_carrier_side": carrier_side,
        "c4_chance_quality": chance_quality,
        "c4_evidence_confidence": evidence_confidence,
        "c4_continuation_quality": continuation_quality,
        "c4_failure_resistance": failure_resistance,
        "c4_control_endpoint_risk": control_risk,
        "c4_goal3_funding": goal3,
        "c4_goal4_funding": goal4,
        "c4_supported_line": supported_line,
        "c4_material_suppression": material_suppression,
        "c4_failure_attacks_route": failure_attacks_route,
        "c4_common_evidence_basis": m.common_evidence_basis,
        "c4_reason_trace": " | ".join(trace),
    }


def _rank_key(row: dict[str, Any]) -> tuple[Any, ...]:
    line = row["c4_supported_line"]
    lower_burden = -(line if line is not None else 99.0)
    return (
        STATE_SCORE[row["c4_state"]],
        FUNDING_SCORE[row["c4_goal3_funding"]],
        FUNDING_SCORE[row["c4_goal4_funding"]],
        CONTROL_SCORE[row["c4_control_endpoint_risk"]],
        CARRIER_SCORE[row["c4_carrier"]],
        GRADE_SCORE[row["c4_chance_quality"]],
        GRADE_SCORE[row["c4_failure_resistance"]],
        GRADE_SCORE[row["c4_evidence_confidence"]],
        lower_burden,
    )


def compile_board(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise C4ContractError("payload must be an object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise C4ContractError(f"schema_version must be {SCHEMA_VERSION!r}")
    if payload.get("stage") != "board":
        raise C4ContractError("stage must be 'board'")

    raw_matches = payload.get("matches")
    if not isinstance(raw_matches, list) or not raw_matches:
        raise C4ContractError("matches must be a non-empty array")

    parsed = [parse_match(row) for row in raw_matches]
    ids = [m.match_id for m in parsed]
    if len(ids) != len(set(ids)):
        raise C4ContractError("duplicate match_id in C4 board")

    rows = [compile_match(m) for m in parsed]
    # Canonical tie-break: match_id ascending after model-owned ranking key.
    rows.sort(key=lambda row: row["match_id"])
    rows.sort(key=_rank_key, reverse=True)

    for idx, row in enumerate(rows, start=1):
        row["c4_rank"] = idx

    return {
        "schema_version": SCHEMA_VERSION,
        "stage": "board_result",
        "model": "c4",
        "c4_scope": "STEP1_SHADOW_ONLY",
        "match_count": len(rows),
        "matches": rows,
    }


def dumps(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)
