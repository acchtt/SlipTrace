from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from competition_reliability import apply_reliability_cap, effective_state

from core import (
    BoardState,
    C3PolicyAssessment,
    CarrierStrength,
    CompletionMode,
    DecisionContext,
    FollowLane,
    FundingSource,
    FundingState,
    Grade,
    H2HReviewStatus,
    MatchAssessment,
    PostXiResearchStatus,
    Quote,
    RouteStrength,
    SecondRouteRole,
    ThesisState,
    XiStatus,
    c2_selection_floor,
    c3_board_state,
    c3_ranking_key,
    c3_shadow_lane,
    decide_c3,
    decide_c,
    decide_c2,
    follow_through_lane,
    rank_assessments,
    rank_assessments_c2,
    rank_assessments_c3,
    ranking_key,
    c2_ranking_key,
)


SCHEMA_VERSION = "football-engine-v1"
MAX_FOLLOW = 6
MAX_RESERVE = 4
MAX_FOLLOW_PER_KICKOFF = 2


class ContractError(ValueError):
    pass


def _required(obj: dict[str, Any], key: str) -> Any:
    if key not in obj:
        raise ContractError(f"missing required field: {key}")
    return obj[key]


def _enum(enum_cls, value: Any, field: str):
    if not isinstance(value, str):
        raise ContractError(f"{field} must be a string")
    key = value.strip().upper().replace("-", "_").replace(" ", "_")
    aliases = {
        ("CarrierStrength", "NO_RELIABLE_CARRIER"): "NONE",
        ("CarrierStrength", "NO_CARRIER"): "NONE",
        ("BoardState", "C_FOCUS"): "FOCUS",
        ("BoardState", "C_WATCH"): "WATCH",
        ("BoardState", "C_PASS"): "PASS",
        ("BoardState", "C2_FOCUS"): "FOCUS",
        ("BoardState", "C2_WATCH"): "WATCH",
        ("BoardState", "C2_PASS"): "PASS",
        ("BoardState", "C3_FOCUS"): "FOCUS",
        ("BoardState", "C3_WATCH"): "WATCH",
        ("BoardState", "C3_PASS"): "PASS",
    }
    key = aliases.get((enum_cls.__name__, key), key)
    try:
        return enum_cls[key]
    except KeyError as exc:
        allowed = ", ".join(x.name for x in enum_cls)
        raise ContractError(
            f"invalid {field}={value!r}; allowed: {allowed}"
        ) from exc


def _bool(obj: dict[str, Any], key: str, default: bool = False) -> bool:
    value = obj.get(key, default)
    if not isinstance(value, bool):
        raise ContractError(f"{key} must be boolean")
    return value


def _required_bool(obj: dict[str, Any], key: str) -> bool:
    value = _required(obj, key)
    if not isinstance(value, bool):
        raise ContractError(f"{key} must be boolean")
    return value


def _number(obj: dict[str, Any], key: str) -> float:
    value = _required(obj, key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ContractError(f"{key} must be numeric")
    return float(value)


def _string(obj: dict[str, Any], key: str) -> str:
    value = _required(obj, key)
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{key} must be a non-empty string")
    return value.strip()


def _choice(obj: dict[str, Any], key: str, allowed: set[str]) -> str:
    value = _string(obj, key).upper().replace("-", "_").replace(" ", "_")
    if value not in allowed:
        choices = ", ".join(sorted(allowed))
        raise ContractError(f"invalid {key}={value!r}; allowed: {choices}")
    return value


def _is_unresolved_text(value: str) -> bool:
    normalized = value.strip().upper().replace("-", "_").replace(" ", "_")
    markers = ("UNKNOWN", "LIMITED", "UNRESOLVED", "TBD", "NOT_VERIFIED")
    return any(marker in normalized for marker in markers)


def _kickoff_block(obj: dict[str, Any]) -> str:
    value = _string(obj, "kickoff_ict")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ContractError("kickoff_ict must be ISO-8601") from exc
    if parsed.tzinfo is None:
        raise ContractError("kickoff_ict must include timezone offset")
    return parsed.isoformat(timespec="minutes")


def validate_c_screen_state(a: MatchAssessment, state: BoardState) -> None:
    """Fail closed on an obvious carrier-led C-PASS contradiction."""

    if state != BoardState.PASS:
        return

    carrier_rescue = (
        a.completion_mode in {
            CompletionMode.CARRIER_LED,
            CompletionMode.FORCED_CHAOS,
            CompletionMode.MIXED,
        }
        and a.burden_completion_quality == Grade.HIGH
        and a.continuation_quality == Grade.HIGH
        and a.carrier == CarrierStrength.STRONG
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and a.opponent_leakage >= Grade.MEDIUM
        and a.burden_stall_risk != Grade.HIGH
        and not a.failure_attacks_route
        and not a.material_suppression
    )
    if carrier_rescue:
        raise ContractError(
            "C-PASS CONTRADICTION — HIGH BURDEN-COMPLETION CARRIER PATH "
            "REQUIRES WATCH/FOCUS REVIEW"
        )


def validate_operational_viability(obj: dict[str, Any]) -> dict[str, Any]:
    grade = _choice(obj, "operational_viability_grade", {"A", "B", "C", "D"})
    raw_grade = _choice(
        obj, "raw_operational_viability_grade", {"A", "B", "C", "D"}
    )
    reliability_state = _choice(
        obj,
        "competition_reliability_state",
        {"UNPROVEN", "TRUSTED", "NEUTRAL", "CAUTION", "DEMOTED"},
    )
    reliability_reason = _string(obj, "competition_reliability_reason")
    manual_override = _choice(
        obj,
        "competition_reliability_manual_override",
        {"NONE", "TRUSTED", "NEUTRAL", "CAUTION", "DEMOTED"},
    )
    demoted_probation = _bool(obj, "demoted_probation")

    state = effective_state(reliability_state, manual_override)
    expected_grade = apply_reliability_cap(
        raw_grade,
        state,
        demoted_probation=demoted_probation,
    )
    if grade != expected_grade:
        raise ContractError(
            "ASSESSMENT BLOCKED — COMPETITION RELIABILITY CAP BYPASS: "
            f"raw={raw_grade} state={state} expected={expected_grade} final={grade}"
        )

    xi_expected = _choice(obj, "xi_expected", {"YES", "UNCERTAIN", "NO"})
    market = _choice(obj, "market_observability", {"HIGH", "MEDIUM", "LOW", "NONE"})
    news = _choice(obj, "team_news_observability", {"HIGH", "MEDIUM", "LOW", "NONE"})
    reason = _string(obj, "operational_viability_reason")

    if grade in {"C", "D"}:
        raise ContractError(
            "ASSESSMENT BLOCKED — LOW OPERATIONAL OBSERVABILITY: "
            f"grade={grade}"
        )
    if grade == "A":
        if xi_expected != "YES":
            raise ContractError("operational grade A requires xi_expected=YES")
        if market != "HIGH":
            raise ContractError("operational grade A requires market_observability=HIGH")
        if news not in {"HIGH", "MEDIUM"}:
            raise ContractError("operational grade A requires team_news_observability HIGH/MEDIUM")
    if grade == "B":
        if xi_expected == "NO":
            raise ContractError("operational grade B cannot use xi_expected=NO")
        if market not in {"HIGH", "MEDIUM"}:
            raise ContractError("operational grade B requires market_observability HIGH/MEDIUM")
        if news not in {"HIGH", "MEDIUM"}:
            raise ContractError("operational grade B requires team_news_observability HIGH/MEDIUM")

    return {
        "grade": grade,
        "raw_grade": raw_grade,
        "competition_reliability_state": reliability_state,
        "competition_reliability_effective_state": state,
        "competition_reliability_reason": reliability_reason,
        "competition_reliability_manual_override": manual_override,
        "demoted_probation": demoted_probation,
        "xi_expected": xi_expected,
        "market_observability": market,
        "team_news_observability": news,
        "reason": reason,
    }


def validate_tournament_incentive(obj: dict[str, Any]) -> dict[str, Any]:
    """Fail closed when the tournament-incentive assessment is skipped.

    Every structured assessment must explicitly say whether the tournament
    incentive procedure applies. Non-applicable fixtures use NOT_APPLICABLE.
    Applicable fixtures must persist the complete format/incentive block.
    """

    required = _bool(obj, "tournament_incentive_required")
    if "tournament_incentive_required" not in obj:
        raise ContractError("missing required field: tournament_incentive_required")

    format_status = _choice(
        obj,
        "tournament_format_status",
        {"NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"},
    )
    competition_stage = _string(obj, "competition_stage")
    competition_format = _string(obj, "competition_format")
    draw_resolution = _string(obj, "draw_resolution")
    aggregate_state = _string(obj, "aggregate_state")
    qualification_state = _string(obj, "qualification_state")
    simultaneous_results_status = _choice(
        obj,
        "simultaneous_results_status",
        {"NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"},
    )
    simultaneous_results_note = _string(obj, "simultaneous_results_note")
    home_incentive = _choice(
        obj,
        "home_incentive",
        {
            "NOT_APPLICABLE",
            "MUST_WIN",
            "WIN_PREFERRED",
            "DRAW_ACCEPTABLE",
            "MARGIN_NEEDED",
            "PROTECT_AGGREGATE",
            "PROTECT_RESULT",
            "DEAD_RUBBER",
            "PLACEMENT_ONLY",
            "UNKNOWN",
        },
    )
    away_incentive = _choice(
        obj,
        "away_incentive",
        {
            "NOT_APPLICABLE",
            "MUST_WIN",
            "WIN_PREFERRED",
            "DRAW_ACCEPTABLE",
            "MARGIN_NEEDED",
            "PROTECT_AGGREGATE",
            "PROTECT_RESULT",
            "DEAD_RUBBER",
            "PLACEMENT_ONLY",
            "UNKNOWN",
        },
    )
    tiebreak_margin_relevance = _choice(
        obj,
        "tiebreak_margin_relevance",
        {"NOT_APPLICABLE", "YES", "NO", "UNKNOWN"},
    )
    incentive_effect = _choice(
        obj,
        "incentive_effect",
        {
            "NOT_APPLICABLE",
            "EXPANSIVE",
            "NEUTRAL",
            "SUPPRESSIVE",
            "MIXED",
            "UNKNOWN",
        },
    )

    if required:
        if format_status != "VERIFIED":
            raise ContractError(
                "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                f"tournament_format_status={format_status}"
            )

        resolved_choices = {
            "home_incentive": home_incentive,
            "away_incentive": away_incentive,
            "tiebreak_margin_relevance": tiebreak_margin_relevance,
            "incentive_effect": incentive_effect,
        }
        bad_na = [
            key for key, value in resolved_choices.items()
            if value == "NOT_APPLICABLE"
        ]
        if bad_na:
            raise ContractError(
                "tournament incentive required but fields are NOT_APPLICABLE: "
                + ", ".join(bad_na)
            )

        unresolved_choices = [
            key for key, value in resolved_choices.items()
            if value == "UNKNOWN"
        ]
        if unresolved_choices:
            raise ContractError(
                "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                + ", ".join(unresolved_choices)
            )

        if simultaneous_results_status in {"LIMITED", "UNKNOWN"}:
            raise ContractError(
                "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                f"simultaneous_results_status={simultaneous_results_status}"
            )

        unresolved_text = []
        for key, value in {
            "competition_stage": competition_stage,
            "competition_format": competition_format,
            "draw_resolution": draw_resolution,
            "aggregate_state": aggregate_state,
            "qualification_state": qualification_state,
            "simultaneous_results_note": simultaneous_results_note,
        }.items():
            if _is_unresolved_text(value):
                unresolved_text.append(key)
        if unresolved_text:
            raise ContractError(
                "ASSESSMENT BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                + ", ".join(unresolved_text)
            )
    else:
        expected_na = {
            "tournament_format_status": format_status,
            "home_incentive": home_incentive,
            "away_incentive": away_incentive,
            "tiebreak_margin_relevance": tiebreak_margin_relevance,
            "incentive_effect": incentive_effect,
            "simultaneous_results_status": simultaneous_results_status,
        }
        bad = [key for key, value in expected_na.items() if value != "NOT_APPLICABLE"]
        if bad:
            raise ContractError(
                "non-tournament assessment must use NOT_APPLICABLE for: "
                + ", ".join(bad)
            )
        for key, value in {
            "competition_stage": competition_stage,
            "competition_format": competition_format,
            "draw_resolution": draw_resolution,
            "aggregate_state": aggregate_state,
            "qualification_state": qualification_state,
            "simultaneous_results_note": simultaneous_results_note,
        }.items():
            if value.upper().replace("-", "_").replace(" ", "_") != "NOT_APPLICABLE":
                raise ContractError(
                    f"non-tournament assessment must use NOT_APPLICABLE for {key}"
                )

    return {
        "required": required,
        "format_status": format_status,
        "incentive_effect": incentive_effect,
        "resolution_status": "VERIFIED" if required else "NOT_APPLICABLE",
        "simultaneous_results_status": simultaneous_results_status,
    }


def parse_assessment(obj: dict[str, Any]) -> MatchAssessment:
    if not isinstance(obj, dict):
        raise ContractError("match must be an object")

    validate_operational_viability(obj)
    validate_tournament_incentive(obj)
    _kickoff_block(obj)

    return MatchAssessment(
        match_id=str(_required(obj, "match_id")),
        home_route=_enum(
            RouteStrength, _required(obj, "home_route"), "home_route"
        ),
        away_route=_enum(
            RouteStrength, _required(obj, "away_route"), "away_route"
        ),
        carrier=_enum(
            CarrierStrength, _required(obj, "carrier"), "carrier"
        ),
        route_reliability=_enum(
            Grade, _required(obj, "route_reliability"), "route_reliability"
        ),
        independent_route_quality=_enum(
            Grade,
            _required(obj, "independent_route_quality"),
            "independent_route_quality",
        ),
        chance_quality=_enum(
            Grade, _required(obj, "chance_quality"), "chance_quality"
        ),
        failure_resistance=_enum(
            Grade,
            _required(obj, "failure_resistance"),
            "failure_resistance",
        ),
        xi_robustness=_enum(
            Grade, _required(obj, "xi_robustness"), "xi_robustness"
        ),
        evidence_confidence=_enum(
            Grade,
            _required(obj, "evidence_confidence"),
            "evidence_confidence",
        ),
        burden_protection=_enum(
            Grade,
            _required(obj, "burden_protection"),
            "burden_protection",
        ),
        completion_mode=_enum(
            CompletionMode, _required(obj, "completion_mode"), "completion_mode"
        ),
        burden_completion_quality=_enum(
            Grade,
            _required(obj, "burden_completion_quality"),
            "burden_completion_quality",
        ),
        continuation_quality=_enum(
            Grade, _required(obj, "continuation_quality"), "continuation_quality"
        ),
        opponent_leakage=_enum(
            Grade, _required(obj, "opponent_leakage"), "opponent_leakage"
        ),
        burden_stall_risk=_enum(
            Grade, _required(obj, "burden_stall_risk"), "burden_stall_risk"
        ),
        main_failure=_string(obj, "main_failure"),
        h2h_state=_string(obj, "h2h_state"),
        supported_line=_number(obj, "supported_line"),
        carrier_self_fund=_required_bool(obj, "carrier_self_fund"),
        independent_upper_tail=_required_bool(obj, "independent_upper_tail"),
        failure_attacks_route=_required_bool(obj, "failure_attacks_route"),
        material_suppression=_required_bool(obj, "material_suppression"),
    )


def parse_c3_policy(
    obj: dict[str, Any],
    base: MatchAssessment,
) -> C3PolicyAssessment:
    """Parse C3-only policy fields without changing common C/C2 evidence."""

    return C3PolicyAssessment(
        base=base,
        second_route_role=_enum(
            SecondRouteRole,
            _required(obj, "c3_second_route_role"),
            "c3_second_route_role",
        ),
        goal3_funding=_enum(
            FundingState,
            _required(obj, "c3_goal3_funding"),
            "c3_goal3_funding",
        ),
        goal3_funding_source=_enum(
            FundingSource,
            _required(obj, "c3_goal3_funding_source"),
            "c3_goal3_funding_source",
        ),
        goal3_funding_basis=_string(obj, "c3_goal3_funding_basis"),
        goal4_funding=_enum(
            FundingState,
            _required(obj, "c3_goal4_funding"),
            "c3_goal4_funding",
        ),
        goal4_funding_source=_enum(
            FundingSource,
            _required(obj, "c3_goal4_funding_source"),
            "c3_goal4_funding_source",
        ),
        goal4_funding_basis=_string(obj, "c3_goal4_funding_basis"),
        control_endpoint_risk=_enum(
            Grade,
            _required(obj, "c3_control_endpoint_risk"),
            "c3_control_endpoint_risk",
        ),
        control_endpoint_basis=_string(obj, "c3_control_endpoint_basis"),
    )


def _check_envelope(payload: dict[str, Any], expected_stage: str) -> None:
    if not isinstance(payload, dict):
        raise ContractError("payload must be a JSON object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ContractError(
            f"schema_version must be {SCHEMA_VERSION!r}"
        )
    if payload.get("stage") != expected_stage:
        raise ContractError(f"stage must be {expected_stage!r}")


def run_board(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "board")

    model = str(payload.get("model", "")).lower()
    if model not in {"c", "c2", "c3"}:
        raise ContractError("model must be 'c', 'c2', or 'c3'")

    raw_matches = _required(payload, "matches")
    if not isinstance(raw_matches, list) or not raw_matches:
        raise ContractError("matches must be a non-empty array")

    parsed = [parse_assessment(item) for item in raw_matches]
    if model == "c":
        ranked = rank_assessments(parsed)
    elif model == "c2":
        ranked = rank_assessments_c2(parsed)
    else:
        ranked = rank_assessments_c3(
            [parse_c3_policy(raw, base) for raw, base in zip(raw_matches, parsed)]
        )

    raw_by_id = {str(item["match_id"]): item for item in raw_matches}
    block_rank_by_id: dict[str, int] = {}
    block_counts: dict[str, int] = {}
    for ranked_item in ranked:
        item = ranked_item.base if model == "c3" else ranked_item
        raw = raw_by_id[item.match_id]
        block = _kickoff_block(raw)
        block_counts[block] = block_counts.get(block, 0) + 1
        block_rank_by_id[item.match_id] = block_counts[block]

    output = []
    follow_used = 0
    reserve_used = 0
    follow_by_block: dict[str, int] = {}

    for rank, ranked_item in enumerate(ranked, start=1):
        c3_item = ranked_item if model == "c3" else None
        item = ranked_item.base if model == "c3" else ranked_item
        raw = raw_by_id[item.match_id]
        kickoff_block = _kickoff_block(raw)
        operational_gate = validate_operational_viability(raw)
        incentive_gate = validate_tournament_incentive(raw)
        row: dict[str, Any] = {
            "rank": rank,
            "match_id": item.match_id,
            "ranking_key": list(
                ranking_key(item)
                if model == "c"
                else c2_ranking_key(item)
                if model == "c2"
                else c3_ranking_key(c3_item)
            ),
            "kickoff_ict": raw["kickoff_ict"],
            "same_kickoff_rank": block_rank_by_id[item.match_id],
            "supported_line": item.supported_line,
            "completion_mode": item.completion_mode.value,
            "burden_completion_quality": item.burden_completion_quality.name,
            "continuation_quality": item.continuation_quality.name,
            "opponent_leakage": item.opponent_leakage.name,
            "burden_stall_risk": item.burden_stall_risk.name,
            "operational_viability_grade": operational_gate["grade"],
            "raw_operational_viability_grade": operational_gate["raw_grade"],
            "competition_reliability_state": operational_gate["competition_reliability_state"],
            "competition_reliability_effective_state": operational_gate["competition_reliability_effective_state"],
            "competition_reliability_reason": operational_gate["competition_reliability_reason"],
            "competition_reliability_manual_override": operational_gate["competition_reliability_manual_override"],
            "demoted_probation": operational_gate["demoted_probation"],
            "xi_expected": operational_gate["xi_expected"],
            "market_observability": operational_gate["market_observability"],
            "team_news_observability": operational_gate["team_news_observability"],
            "tournament_incentive_required": incentive_gate["required"],
            "tournament_format_status": incentive_gate["format_status"],
            "incentive_effect": incentive_gate["incentive_effect"],
            "tournament_incentive_resolution": incentive_gate["resolution_status"],
            "simultaneous_results_status": incentive_gate["simultaneous_results_status"],
        }

        state = None
        if "board_state" in raw:
            state = _enum(BoardState, raw["board_state"], "board_state")
            row["board_state"] = state.name
            if model == "c":
                validate_c_screen_state(item, state)

        if model == "c" and state is not None:
            base_lane = follow_through_lane(item, state)
            lane = FollowLane.STOP

            if operational_gate["grade"] == "B":
                if (
                    base_lane in {FollowLane.FOLLOW, FollowLane.RESERVE}
                    and reserve_used < MAX_RESERVE
                ):
                    lane = FollowLane.RESERVE
                    reserve_used += 1
            elif base_lane == FollowLane.FOLLOW:
                block_follow_used = follow_by_block.get(kickoff_block, 0)
                if (
                    follow_used < MAX_FOLLOW
                    and block_follow_used < MAX_FOLLOW_PER_KICKOFF
                ):
                    lane = FollowLane.FOLLOW
                    follow_used += 1
                    follow_by_block[kickoff_block] = block_follow_used + 1
                elif reserve_used < MAX_RESERVE:
                    lane = FollowLane.RESERVE
                    reserve_used += 1
            elif base_lane == FollowLane.RESERVE and reserve_used < MAX_RESERVE:
                lane = FollowLane.RESERVE
                reserve_used += 1

            row["follow_lane"] = lane.value

        if model == "c2":
            floor, reasons = c2_selection_floor(item)
            row["selection_floor"] = floor.value
            row["selection_floor_reasons"] = list(reasons)

        if model == "c3":
            state = c3_board_state(c3_item)
            lane = c3_shadow_lane(c3_item, state)
            row["board_state"] = f"C3-{state.name}"
            row["c3_shadow_lane"] = lane.value
            row["c3_second_route_role"] = c3_item.second_route_role.name
            row["c3_goal3_funding"] = c3_item.goal3_funding.name
            row["c3_goal3_funding_source"] = c3_item.goal3_funding_source.value
            row["c3_goal3_funding_basis"] = c3_item.goal3_funding_basis
            row["c3_goal4_funding"] = c3_item.goal4_funding.name
            row["c3_goal4_funding_source"] = c3_item.goal4_funding_source.value
            row["c3_goal4_funding_basis"] = c3_item.goal4_funding_basis
            row["c3_control_endpoint_risk"] = c3_item.control_endpoint_risk.name
            row["c3_control_endpoint_basis"] = c3_item.control_endpoint_basis

        output.append(row)

    result = {
        "schema_version": SCHEMA_VERSION,
        "stage": "board_result",
        "model": model,
        "ranking_policy": (
            "FOOTBALL_C_BURDEN_COMPLETION"
            if model == "c"
            else "FOOTBALL_C2_FROZEN_ROUTE_QUALITY"
            if model == "c2"
            else "FOOTBALL_C3_CLEARING_GOAL_FUNDING"
        ),
        "match_count": len(output),
        "matches": output,
    }

    if model == "c":
        result["follow_count"] = sum(
            row.get("follow_lane") == FollowLane.FOLLOW.value for row in output
        )
        result["reserve_count"] = sum(
            row.get("follow_lane") == FollowLane.RESERVE.value for row in output
        )
        result["stop_count"] = sum(
            row.get("follow_lane") == FollowLane.STOP.value for row in output
        )
        result["follow_capacity"] = MAX_FOLLOW
        result["reserve_capacity"] = MAX_RESERVE
        result["max_follow_per_exact_kickoff"] = MAX_FOLLOW_PER_KICKOFF

    return result


def run_decision(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "decision")

    model = str(payload.get("model", "")).lower()
    if model not in {"c", "c2", "c3"}:
        raise ContractError("model must be 'c', 'c2', or 'c3'")

    raw_match = _required(payload, "match")
    a = parse_assessment(raw_match)
    c3_a = parse_c3_policy(raw_match, a) if model == "c3" else None

    ctx_obj = _required(payload, "context")
    if not isinstance(ctx_obj, dict):
        raise ContractError("context must be an object")

    if "tournament_incentive_rechecked" not in ctx_obj:
        raise ContractError(
            "missing required field: tournament_incentive_rechecked"
        )
    tournament_incentive_rechecked = _bool(
        ctx_obj, "tournament_incentive_rechecked"
    )
    tournament_incentive_recheck_status = _choice(
        ctx_obj,
        "tournament_incentive_recheck_status",
        {"NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"},
    )
    tournament_gate = validate_tournament_incentive(raw_match)
    if tournament_gate["required"]:
        if not tournament_incentive_rechecked:
            raise ContractError(
                "DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING"
            )
        if tournament_incentive_recheck_status != "VERIFIED":
            raise ContractError(
                "DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                f"recheck_status={tournament_incentive_recheck_status}"
            )
    elif tournament_incentive_recheck_status != "NOT_APPLICABLE":
        raise ContractError(
            "non-tournament decision must use "
            "tournament_incentive_recheck_status=NOT_APPLICABLE"
        )

    xi_status = _enum(
        XiStatus, _required(ctx_obj, "xi_status"), "xi_status"
    )
    if xi_status == XiStatus.UNAVAILABLE:
        raise ContractError(
            "DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING"
        )

    post_xi_research_status = _enum(
        PostXiResearchStatus,
        _required(ctx_obj, "post_xi_research_status"),
        "post_xi_research_status",
    )
    h2h_review_status = _enum(
        H2HReviewStatus,
        _required(ctx_obj, "h2h_review_status"),
        "h2h_review_status",
    )
    h2h_rechecked = _required_bool(ctx_obj, "h2h_rechecked")
    if not h2h_rechecked:
        raise ContractError("DECISION BLOCKED — H2H RECHECK MISSING")

    completion_rechecked = _required_bool(ctx_obj, "completion_rechecked")
    if not completion_rechecked:
        raise ContractError(
            "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING"
        )

    board_state = _enum(
        BoardState, _required(ctx_obj, "board_state"), "board_state"
    )
    thesis_state = _enum(
        ThesisState, _required(ctx_obj, "thesis_state"), "thesis_state"
    )
    quote_obj = _required(ctx_obj, "quote")
    if not isinstance(quote_obj, dict):
        raise ContractError("quote must be an object")

    ctx = DecisionContext(
        board_state=board_state,
        thesis_state=thesis_state,
        quote=Quote(
            line=_number(quote_obj, "line"),
            odds=_number(quote_obj, "odds"),
        ),
        xi_status=xi_status,
        post_xi_research_status=post_xi_research_status,
        h2h_review_status=h2h_review_status,
        h2h_rechecked=h2h_rechecked,
        completion_rechecked=completion_rechecked,
        top_ranked_focus=_required_bool(ctx_obj, "top_ranked_focus"),
        primary_mechanism_intact=_required_bool(
            ctx_obj, "primary_mechanism_intact"
        ),
        wait_reachable=_required_bool(ctx_obj, "wait_reachable"),
        wait_requires_negative_info=_required_bool(
            ctx_obj, "wait_requires_negative_info"
        ),
        material_veto=_required_bool(ctx_obj, "material_veto"),
    )

    decision = (
        decide_c(a, ctx)
        if model == "c"
        else decide_c2(a, ctx)
        if model == "c2"
        else decide_c3(c3_a, ctx)
    )
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "stage": "decision_result",
        "model": model,
        "match_id": a.match_id,
        "action": decision.action.value,
        "reason": decision.reason,
        "bridge_used": decision.bridge_used,
        "tournament_incentive_required": tournament_gate["required"],
        "tournament_format_status": tournament_gate["format_status"],
        "incentive_effect": tournament_gate["incentive_effect"],
        "tournament_incentive_rechecked": tournament_incentive_rechecked,
        "tournament_incentive_recheck_status": tournament_incentive_recheck_status,
        "tournament_incentive_resolution": tournament_gate["resolution_status"],
        "xi_status": xi_status.value,
        "post_xi_research_status": post_xi_research_status.value,
        "h2h_review_status": h2h_review_status.value,
        "h2h_rechecked": h2h_rechecked,
        "completion_rechecked": completion_rechecked,
        "current_burden_completion_quality": a.burden_completion_quality.name,
        "current_continuation_quality": a.continuation_quality.name,
        "current_burden_stall_risk": a.burden_stall_risk.name,
    }

    if model == "c2":
        floor, reasons = c2_selection_floor(a)
        result["selection_floor"] = floor.value
        result["selection_floor_reasons"] = list(reasons)

    if model == "c3":
        result["c3_second_route_role"] = c3_a.second_route_role.name
        result["c3_goal3_funding"] = c3_a.goal3_funding.name
        result["c3_goal3_funding_source"] = c3_a.goal3_funding_source.value
        result["c3_goal4_funding"] = c3_a.goal4_funding.name
        result["c3_goal4_funding_source"] = c3_a.goal4_funding_source.value
        result["c3_control_endpoint_risk"] = c3_a.control_endpoint_risk.name

    return result


def dumps(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)



AUDIT_DIAGNOSIS_TAGS = {
    "MODEL_FALSE_POSITIVE",
    "MODEL_FALSE_NEGATIVE",
    "FOLLOW_PRIORITY_MISS",
    "PROCESS_MISS",
    "EXECUTION_MISS",
    "OPERATIONAL_OPPORTUNITY_COST",
    "NO_OFFICIAL_EXPOSURE",
    "NO_RETROSPECTIVE_MODEL_CHANGE",
    "TOURNAMENT_INCENTIVE_MISS",
    "FORMAT_DATA_MISSING",
    "STALE_INCENTIVE_EPOCH",
    "INCENTIVE_RESOLUTION_BYPASS",
}


def _nullable_number(obj: dict[str, Any], key: str) -> float | None:
    value = _required(obj, key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ContractError(f"{key} must be numeric or null")
    return float(value)


def _nullable_string(obj: dict[str, Any], key: str) -> str | None:
    value = _required(obj, key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{key} must be a non-empty string or null")
    return value.strip()


def run_audit_record(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate one hindsight-safe material fixture audit record."""

    _check_envelope(payload, "audit_record")

    match_id = _string(payload, "match_id")
    model_version = _string(payload, "model_version")

    frozen = _required(payload, "frozen")
    observed = _required(payload, "observed")
    diagnosis = _required(payload, "diagnosis")
    pnl = _required(payload, "pnl_status")
    for name, obj in (
        ("frozen", frozen),
        ("observed", observed),
        ("diagnosis", diagnosis),
        ("pnl_status", pnl),
    ):
        if not isinstance(obj, dict):
            raise ContractError(f"{name} must be an object")

    frozen_out = {
        "c_board_state": _choice(
            frozen, "c_board_state", {"C_PASS", "C_WATCH", "C_FOCUS", "NONE"}
        ),
        "follow_lane": _choice(
            frozen, "follow_lane", {"FOLLOW", "RESERVE", "STOP", "NONE"}
        ),
        "supported_line": _nullable_number(frozen, "supported_line"),
        "completion_mode": _choice(
            frozen,
            "completion_mode",
            {"NONE", "TWO_SIDED", "CARRIER_LED", "FORCED_CHAOS", "MIXED"},
        ),
        "burden_completion_quality": _choice(
            frozen, "burden_completion_quality", {"LOW", "MEDIUM", "HIGH"}
        ),
        "continuation_quality": _choice(
            frozen, "continuation_quality", {"LOW", "MEDIUM", "HIGH"}
        ),
        "opponent_leakage": _choice(
            frozen, "opponent_leakage", {"LOW", "MEDIUM", "HIGH"}
        ),
        "burden_stall_risk": _choice(
            frozen, "burden_stall_risk", {"LOW", "MEDIUM", "HIGH"}
        ),
        "c_action": _choice(
            frozen, "c_action", {"C_BET", "C_WAIT", "C_PASS", "NONE"}
        ),
        "quote_line": _nullable_number(frozen, "quote_line"),
        "quote_odds": _nullable_number(frozen, "quote_odds"),
    }

    observed_out = {
        "ht_score": _nullable_string(observed, "ht_score"),
        "ft_score": _string(observed, "ft_score"),
        "settlement": _choice(
            observed,
            "settlement",
            {
                "WIN",
                "HALF_WIN",
                "PUSH",
                "HALF_LOSS",
                "LOSS",
                "NO_OFFICIAL_EXPOSURE",
                "NOT_APPLICABLE",
            },
        ),
        "completion_materialized": _choice(
            observed, "completion_materialized", {"YES", "NO", "UNKNOWN"}
        ),
        "continuation_materialized": _choice(
            observed, "continuation_materialized", {"YES", "NO", "UNKNOWN"}
        ),
        "carrier_self_fund_materialized": _choice(
            observed,
            "carrier_self_fund_materialized",
            {"YES", "NO", "UNKNOWN", "NOT_APPLICABLE"},
        ),
        "opponent_route_materialized": _choice(
            observed,
            "opponent_route_materialized",
            {"YES", "NO", "UNKNOWN", "NOT_APPLICABLE"},
        ),
    }

    tags = _required(diagnosis, "tags")
    if not isinstance(tags, list) or not tags:
        raise ContractError("diagnosis.tags must be a non-empty array")
    normalized_tags: list[str] = []
    for tag in tags:
        if not isinstance(tag, str):
            raise ContractError("diagnosis.tags entries must be strings")
        norm = tag.strip().upper().replace("-", "_").replace(" ", "_")
        if norm not in AUDIT_DIAGNOSIS_TAGS:
            allowed = ", ".join(sorted(AUDIT_DIAGNOSIS_TAGS))
            raise ContractError(
                f"invalid audit diagnosis tag={tag!r}; allowed: {allowed}"
            )
        normalized_tags.append(norm)

    pre_freeze_miss = _required_bool(diagnosis, "pre_freeze_evidence_miss")
    pre_freeze_note = _nullable_string(diagnosis, "pre_freeze_evidence_note")
    retrospective = _required_bool(diagnosis, "retrospective_hypothesis_only")

    if pre_freeze_miss and not pre_freeze_note:
        raise ContractError(
            "pre_freeze_evidence_note is required when pre_freeze_evidence_miss=true"
        )
    if not pre_freeze_miss and pre_freeze_note is not None:
        raise ContractError(
            "pre_freeze_evidence_note must be null when pre_freeze_evidence_miss=false"
        )

    official_exposure = _required_bool(pnl, "official_c_exposure")
    official_pnl = _nullable_number(pnl, "official_c_model_pnl")
    user_executed = _required_bool(pnl, "user_executed")
    user_pnl = _nullable_number(pnl, "user_pnl")
    c2_shadow_only = _required_bool(pnl, "c2_shadow_only")

    if not official_exposure and official_pnl is not None:
        raise ContractError(
            "official_c_model_pnl must be null when official_c_exposure=false"
        )
    if official_exposure and observed_out["settlement"] in {
        "NO_OFFICIAL_EXPOSURE",
        "NOT_APPLICABLE",
    }:
        raise ContractError(
            "official exposure requires a real exact-line settlement"
        )
    if not official_exposure and observed_out["settlement"] not in {
        "NO_OFFICIAL_EXPOSURE",
        "NOT_APPLICABLE",
    }:
        raise ContractError(
            "non-exposure audit must not assign an official settlement"
        )
    if not user_executed and user_pnl is not None:
        raise ContractError("user_pnl must be null when user_executed=false")

    return {
        "schema_version": SCHEMA_VERSION,
        "stage": "audit_record_result",
        "match_id": match_id,
        "model_version": model_version,
        "frozen": frozen_out,
        "observed": observed_out,
        "diagnosis": {
            "tags": normalized_tags,
            "pre_freeze_evidence_miss": pre_freeze_miss,
            "pre_freeze_evidence_note": pre_freeze_note,
            "retrospective_hypothesis_only": retrospective,
        },
        "pnl_status": {
            "official_c_exposure": official_exposure,
            "official_c_model_pnl": official_pnl,
            "user_executed": user_executed,
            "user_pnl": user_pnl,
            "c2_shadow_only": c2_shadow_only,
        },
    }
