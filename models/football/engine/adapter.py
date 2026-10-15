from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from competition_reliability import apply_reliability_cap, effective_state

from core import (
    Action,
    BoardState,
    CarrierStrength,
    CompletionMode,
    DecisionContext,
    FollowLane,
    Grade,
    H2HReviewStatus,
    MatchAssessment,
    ModelQuoteContext,
    PostXiResearchStatus,
    Quote,
    RouteStrength,
    Step2Authorization,
    ThesisState,
    XiStatus,
    c2_selection_floor,
    c2_clearing_goal_funded,
    c_effective_incentive_grades,
    c2_low_burden_leakage_goal3_funded,
    clearing_goal_funded,
    low_burden_leakage_goal3_funded,
    decide_c,
    decide_c2,
    evaluate_c_quote,
    evaluate_c2_quote,
    follow_through_lane,
    rank_assessments,
    rank_assessments_c2,
    ranking_key,
    c2_ranking_key,
    model_wait_target,
    wait_accounting_target,
    market_line_funded,
    prospective_goal_funding,
    certified_supported_burden,
    certified_supported_burden_basis,
)


SCHEMA_VERSION = "football-engine-v1"
MAX_FOLLOW = 6
MAX_RESERVE = 4
MAX_FOLLOW_PER_KICKOFF = 2


class ContractError(ValueError):
    pass


ACTIVE_MODEL = "c"
RETIRED_MODELS = {"c2", "c3", "c4"}


def _active_model(payload: dict[str, Any]) -> str:
    model = str(payload.get("model", "")).lower()
    if model != ACTIVE_MODEL:
        raise ContractError(
            "active production model must be 'c'; C2/C3/C4 are retired and "
            "historical records remain read-only"
        )
    return model


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


def _optional_number(obj: dict[str, Any], key: str) -> float | None:
    if key not in obj or obj[key] is None:
        return None
    value = obj[key]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ContractError(f"{key} must be numeric or null")
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


def validate_h2h_semantics(obj: dict[str, Any]) -> dict[str, Any]:
    """Compile the existing transferable + corroborated H2H rule explicitly."""

    effect = _choice(
        obj,
        "h2h_effect",
        {"SUPPRESSIVE", "OPEN", "MIXED", "NOT_MATERIAL", "UNAVAILABLE"},
    )
    transferability = _choice(
        obj,
        "h2h_transferability",
        {"VERIFIED", "LIMITED", "NOT_TRANSFERABLE", "UNAVAILABLE"},
    )
    corroboration = _choice(
        obj,
        "h2h_current_corroboration",
        {"VERIFIED", "NOT_FOUND", "NOT_APPLICABLE", "UNKNOWN"},
    )
    material_effect = _required_bool(obj, "h2h_material_effect")
    basis = _string(obj, "h2h_basis")

    if material_effect:
        if effect != "SUPPRESSIVE":
            raise ContractError(
                "H2H MATERIAL EFFECT BLOCKED — material H2H effect requires h2h_effect=SUPPRESSIVE"
            )
        if transferability != "VERIFIED":
            raise ContractError(
                "H2H MATERIAL EFFECT BLOCKED — transferability must be VERIFIED"
            )
        if corroboration != "VERIFIED":
            raise ContractError(
                "H2H MATERIAL EFFECT BLOCKED — current corroboration must be VERIFIED"
            )

    if effect == "UNAVAILABLE":
        if transferability != "UNAVAILABLE":
            raise ContractError(
                "UNAVAILABLE H2H requires h2h_transferability=UNAVAILABLE"
            )
        if material_effect:
            raise ContractError(
                "UNAVAILABLE H2H cannot have material effect"
            )

    return {
        "effect": effect,
        "transferability": transferability,
        "current_corroboration": corroboration,
        "material_effect": material_effect,
        "basis": basis,
    }


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
    """Fail closed on C board states that contradict strong current goal routes."""

    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    carrier_rescue = (
        a.completion_mode in {
            CompletionMode.CARRIER_LED,
            CompletionMode.FORCED_CHAOS,
            CompletionMode.MIXED,
        }
        and a.burden_completion_quality == Grade.HIGH
        and effective_continuation == Grade.HIGH
        and a.carrier == CarrierStrength.STRONG
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and a.opponent_leakage >= Grade.MEDIUM
        and effective_stall != Grade.HIGH
        and not a.failure_attacks_route
        and not a.material_suppression
    )
    leakage_focus = (
        low_burden_leakage_goal3_funded(a)
        and a.evidence_confidence >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
    )

    if state == BoardState.PASS and (carrier_rescue or leakage_focus):
        raise ContractError(
            "C-PASS CONTRADICTION — CURRENT GOAL-FUNDING PATH "
            "REQUIRES WATCH/FOCUS REVIEW"
        )
    if state == BoardState.WATCH and leakage_focus:
        raise ContractError(
            "C-WATCH CONTRADICTION — HIGH-LEAKAGE GOAL3 CERTIFICATE "
            "REQUIRES C-FOCUS REVIEW"
        )


def validate_c2_screen_state(a: MatchAssessment, state: BoardState) -> None:
    """Keep C2's independently evidenced leakage G3 certificate out of STOP."""
    if (
        state in {BoardState.WATCH, BoardState.PASS}
        and c2_low_burden_leakage_goal3_funded(a)
    ):
        raise ContractError(
            "C2-WATCH/PASS CONTRADICTION — C2-OWNED HIGH-LEAKAGE GOAL3 "
            "CERTIFICATE REQUIRES C2-FOCUS REVIEW"
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


def validate_tournament_incentive(
    obj: dict[str, Any], *, require_resolution: bool = False
) -> dict[str, Any]:
    """Stage-aware tournament incentive validation.

    Step 1 ranks every otherwise eligible fixture, marking unresolved
    applicable tournament information as INCENTIVE_RECHECK_REQUIRED. This
    never silently declares an unresolved tournament favorable or resolved.

    Step 2 must independently verify the completed tournament state,
    in addition to its current mandatory fresh incentive recheck. Unknown
    inputs cannot authorize a BET, WAIT, PASS or shadow action.
    """

    if "tournament_incentive_required" not in obj:
        raise ContractError("missing required field: tournament_incentive_required")
    required = _bool(obj, "tournament_incentive_required")

    # Missing material detail is deliberately recorded as UNKNOWN for an
    # applicable Step-1 fixture. In particular, partial cup/group evidence
    # cannot remove that fixture from C/C2 research. The original raw
    # evidence stays untouched; only the normalized board gate gets defaults.
    # Non-applicable fixtures retain the exact prior explicit-NA contract.
    fields = obj if not required else {
        **{
            key: "UNKNOWN"
            for key in (
                "tournament_format_status", "competition_stage",
                "competition_format", "draw_resolution", "aggregate_state",
                "qualification_state", "simultaneous_results_status",
                "simultaneous_results_note", "home_incentive",
                "away_incentive", "tiebreak_margin_relevance",
                "incentive_effect",
            )
        },
        **obj,
    }

    format_status = _choice(
        fields,
        "tournament_format_status",
        {"NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"},
    )
    competition_stage = _string(fields, "competition_stage")
    competition_format = _string(fields, "competition_format")
    draw_resolution = _string(fields, "draw_resolution")
    aggregate_state = _string(fields, "aggregate_state")
    qualification_state = _string(fields, "qualification_state")
    simultaneous_results_status = _choice(
        fields,
        "simultaneous_results_status",
        {"NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"},
    )
    simultaneous_results_note = _string(fields, "simultaneous_results_note")
    home_incentive = _choice(
        fields,
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
        fields,
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
        fields,
        "tiebreak_margin_relevance",
        {"NOT_APPLICABLE", "YES", "NO", "UNKNOWN"},
    )
    incentive_effect = _choice(
        fields,
        "incentive_effect",
        {"NOT_APPLICABLE", "EXPANSIVE", "NEUTRAL", "SUPPRESSIVE",
         "MIXED", "UNKNOWN"},
    )

    unresolved: list[str] = []
    if required:
        if format_status != "VERIFIED":
            unresolved.append("tournament_format_status")
        for key, value in {
            "home_incentive": home_incentive,
            "away_incentive": away_incentive,
            "tiebreak_margin_relevance": tiebreak_margin_relevance,
            "incentive_effect": incentive_effect,
        }.items():
            if value in {"NOT_APPLICABLE", "UNKNOWN"}:
                unresolved.append(key)
        if simultaneous_results_status in {"LIMITED", "UNKNOWN"}:
            unresolved.append("simultaneous_results_status")
        for key, value in {
            "competition_stage": competition_stage,
            "competition_format": competition_format,
            "draw_resolution": draw_resolution,
            "aggregate_state": aggregate_state,
            "qualification_state": qualification_state,
            "simultaneous_results_note": simultaneous_results_note,
        }.items():
            if _is_unresolved_text(value):
                unresolved.append(key)
        if require_resolution and unresolved:
            raise ContractError(
                "DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED: "
                + ", ".join(unresolved)
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

    status = (
        "INCENTIVE_RECHECK_REQUIRED" if unresolved
        else "VERIFIED" if required else "NOT_APPLICABLE"
    )
    return {
        "required": required,
        "format_status": format_status,
        "incentive_effect": incentive_effect,
        "resolution_status": status,
        "unresolved_fields": unresolved,
        "recheck_required": required,
        "simultaneous_results_status": simultaneous_results_status,
        "home_incentive": home_incentive,
        "away_incentive": away_incentive,
        "tiebreak_margin_relevance": tiebreak_margin_relevance,
        "qualification_state": qualification_state,
    }


def parse_assessment(
    obj: dict[str, Any],
    *,
    require_c_completion: bool = True,
) -> MatchAssessment:
    if not isinstance(obj, dict):
        raise ContractError("match must be an object")

    validate_operational_viability(obj)
    incentive_gate = validate_tournament_incentive(obj)
    h2h_gate = validate_h2h_semantics(obj)
    _kickoff_block(obj)
    if not require_c_completion and (
        ("c2_opponent_leakage" in obj) != ("c2_opponent_leakage_basis" in obj)
    ):
        raise ContractError(
            "C2 leakage requires both independent c2_opponent_leakage "
            "and c2_opponent_leakage_basis"
        )

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
        common_evidence_basis=_string(obj, "common_evidence_basis"),
        main_failure=_string(obj, "main_failure"),
        h2h_state=_string(obj, "h2h_state"),
        h2h_effect=h2h_gate["effect"],
        h2h_transferability=h2h_gate["transferability"],
        h2h_current_corroboration=h2h_gate["current_corroboration"],
        h2h_material_effect=h2h_gate["material_effect"],
        h2h_basis=h2h_gate["basis"],
        supported_line=_number(obj, "supported_line"),
        supported_line_basis=_string(obj, "supported_line_basis"),
        carrier_self_fund=_required_bool(obj, "carrier_self_fund"),
        carrier_self_fund_basis=_string(obj, "carrier_self_fund_basis"),
        independent_upper_tail=_required_bool(obj, "independent_upper_tail"),
        independent_upper_tail_basis=_string(obj, "independent_upper_tail_basis"),
        failure_attacks_route=_required_bool(obj, "failure_attacks_route"),
        failure_attacks_route_basis=_string(obj, "failure_attacks_route_basis"),
        material_suppression=_required_bool(obj, "material_suppression"),
        material_suppression_basis=_string(obj, "material_suppression_basis"),
        goal_signal_priority_score=_optional_number(obj, "goal_signal_priority_score"),
        goal_signal_mean_over_two_rate=_optional_number(obj, "goal_signal_mean_over_two_rate"),
        goal_signal_mean_over_three_rate=_optional_number(obj, "goal_signal_mean_over_three_rate"),
        goal_signal_low_draw_trap_rate=_optional_number(obj, "goal_signal_low_draw_trap_rate"),
        completion_mode=(
            _enum(CompletionMode, _required(obj, "completion_mode"), "completion_mode")
            if require_c_completion else None
        ),
        burden_completion_quality=(
            _enum(Grade, _required(obj, "burden_completion_quality"), "burden_completion_quality")
            if require_c_completion else None
        ),
        continuation_quality=(
            _enum(Grade, _required(obj, "continuation_quality"), "continuation_quality")
            if require_c_completion else None
        ),
        opponent_leakage=(
            _enum(Grade, _required(obj, "opponent_leakage"), "opponent_leakage")
            if require_c_completion else None
        ),
        burden_stall_risk=(
            _enum(Grade, _required(obj, "burden_stall_risk"), "burden_stall_risk")
            if require_c_completion else None
        ),
        c2_opponent_leakage=(
            _enum(Grade, _required(obj, "c2_opponent_leakage"), "c2_opponent_leakage")
            if not require_c_completion and "c2_opponent_leakage" in obj else None
        ),
        c2_opponent_leakage_basis=(
            _string(obj, "c2_opponent_leakage_basis")
            if not require_c_completion and "c2_opponent_leakage" in obj else None
        ),
        tournament_incentive_required=incentive_gate["required"],
        tournament_incentive_resolution=incentive_gate["resolution_status"],
        home_incentive=incentive_gate["home_incentive"],
        away_incentive=incentive_gate["away_incentive"],
        tiebreak_margin_relevance=incentive_gate["tiebreak_margin_relevance"],
        incentive_effect=incentive_gate["incentive_effect"],
        simultaneous_results_status=incentive_gate["simultaneous_results_status"],
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

    model = _active_model(payload)

    raw_matches = _required(payload, "matches")
    if not isinstance(raw_matches, list) or not raw_matches:
        raise ContractError("matches must be a non-empty array")

    parsed = [
        parse_assessment(item, require_c_completion=(model == "c"))
        for item in raw_matches
    ]
    raw_by_id = {str(item["match_id"]): item for item in raw_matches}
    if len(raw_by_id) != len(raw_matches):
        raise ContractError("duplicate match_id in board input")
    if model == "c":
        # The declared football selection state is the first workload tier.
        # A mechanically funded O2.0 WATCH must not rank above an otherwise
        # valid FOCUS merely because the former's Asian burden can push at 2.
        # Preserve the existing clearing-goal-first ranking *within* each
        # state and all separately enforced Step2 funding/price gates.
        ranked = sorted(
            parsed,
            key=lambda item: (
                _enum(BoardState, _required(raw_by_id[item.match_id], "board_state"), "board_state"),
                ranking_key(item),
                item.match_id,
            ),
            reverse=True,
        )
    else:
        ranked = rank_assessments_c2(parsed)
    block_rank_by_id: dict[str, int] = {}
    block_counts: dict[str, int] = {}
    for ranked_item in ranked:
        item = ranked_item
        raw = raw_by_id[item.match_id]
        block = _kickoff_block(raw)
        block_counts[block] = block_counts.get(block, 0) + 1
        block_rank_by_id[item.match_id] = block_counts[block]

    output = []
    follow_used = 0
    reserve_used = 0
    follow_by_block: dict[str, int] = {}

    for rank, ranked_item in enumerate(ranked, start=1):
        item = ranked_item
        raw = raw_by_id[item.match_id]
        kickoff_block = _kickoff_block(raw)
        operational_gate = validate_operational_viability(raw)
        incentive_gate = validate_tournament_incentive(raw)
        tail_profile = prospective_goal_funding(item, model)
        compiled_burden = certified_supported_burden(item, model)
        compiled_basis = certified_supported_burden_basis(item, model)
        row: dict[str, Any] = {
            "rank": rank,
            "match_id": item.match_id,
            "ranking_key": list(
                ranking_key(item) if model == "c" else c2_ranking_key(item)
            ),
            "kickoff_ict": raw["kickoff_ict"],
            "same_kickoff_rank": block_rank_by_id[item.match_id],
            "supported_line": compiled_burden,
            "supported_line_basis": compiled_basis,
            "supported_line_role": "DETERMINISTIC_CERTIFIED_BURDEN",
            "declared_supported_line": item.supported_line,
            "declared_supported_line_basis": item.supported_line_basis,
            **tail_profile,
            "common_evidence_basis": item.common_evidence_basis,
            "goal_signal_priority_score": item.goal_signal_priority_score,
            "goal_signal_mean_over_two_rate": item.goal_signal_mean_over_two_rate,
            "goal_signal_mean_over_three_rate": item.goal_signal_mean_over_three_rate,
            "goal_signal_low_draw_trap_rate": item.goal_signal_low_draw_trap_rate,
            "main_failure": item.main_failure,
            "h2h_state": item.h2h_state,
            "h2h_effect": item.h2h_effect,
            "h2h_transferability": item.h2h_transferability,
            "h2h_current_corroboration": item.h2h_current_corroboration,
            "h2h_material_effect": item.h2h_material_effect,
            "h2h_basis": item.h2h_basis,
            "carrier_self_fund": item.carrier_self_fund,
            "carrier_self_fund_basis": item.carrier_self_fund_basis,
            "independent_upper_tail": item.independent_upper_tail,
            "independent_upper_tail_basis": item.independent_upper_tail_basis,
            "failure_attacks_route": item.failure_attacks_route,
            "failure_attacks_route_basis": item.failure_attacks_route_basis,
            "material_suppression": item.material_suppression,
            "material_suppression_basis": item.material_suppression_basis,
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
            "home_incentive": incentive_gate["home_incentive"],
            "away_incentive": incentive_gate["away_incentive"],
            "tiebreak_margin_relevance": incentive_gate["tiebreak_margin_relevance"],
            "incentive_effect": incentive_gate["incentive_effect"],
            "tournament_incentive_resolution": incentive_gate["resolution_status"],
            "tournament_incentive_recheck_required": incentive_gate["recheck_required"],
            "tournament_incentive_unresolved_fields": incentive_gate["unresolved_fields"],
            "supported_line_status": (
                "PROVISIONAL_INCENTIVE" if incentive_gate["unresolved_fields"]
                else "FROZEN_FOOTBALL_PRE"
            ),
            "simultaneous_results_status": incentive_gate["simultaneous_results_status"],
        }

        if model == "c":
            row["completion_mode"] = item.completion_mode.value
            row["burden_completion_quality"] = item.burden_completion_quality.name
            row["continuation_quality"] = item.continuation_quality.name
            row["opponent_leakage"] = item.opponent_leakage.name
            row["burden_stall_risk"] = item.burden_stall_risk.name

        state = _enum(
            BoardState,
            _required(raw, "board_state"),
            "board_state",
        )
        board_state_basis = _string(raw, "board_state_basis")
        row["board_state"] = state.name
        row["board_state_basis"] = board_state_basis
        if model == "c":
            validate_c_screen_state(item, state)
        else:
            validate_c2_screen_state(item, state)

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
            row["c2_leakage_goal3_funded"] = c2_low_burden_leakage_goal3_funded(item)
            if item.c2_opponent_leakage is not None:
                row["c2_opponent_leakage"] = item.c2_opponent_leakage.name
                row["c2_opponent_leakage_basis"] = item.c2_opponent_leakage_basis

        output.append(row)

    result = {
        "schema_version": SCHEMA_VERSION,
        "stage": "board_result",
        "model": model,
        "ranking_policy": (
            "FOOTBALL_C_FOCUS_FIRST_BURDEN_COMPLETION"
            if model == "c"
            else "FOOTBALL_C2_FROZEN_ROUTE_QUALITY"
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


def run_football_assessment(payload: dict[str, Any]) -> dict[str, Any]:
    """Assess C or C2 football *without* any quote or executable action.

    Distinct from stage=decision. A started fixture can be assessed at any
    minute with no bookmaker prices; do not call the prematch BET engine.
    Missing current football evidence is reported as a limitation rather
    than being laundered into a priced PASS/WAIT or a false positive.
    """
    _check_envelope(payload, "football_assessment")
    model = _active_model(payload)
    match_obj = _required(payload, "match")
    a = parse_assessment(match_obj, require_c_completion=(model == "c"))
    ctx = _required(payload, "context")
    if not isinstance(ctx, dict):
        raise ContractError("football assessment context must be object")
    status = _choice(
        ctx, "fixture_status",
        {"PREMATCH_CONFIRMED", "STARTED", "HALFTIME", "UNKNOWN"},
    )
    score = ctx.get("score")
    if score is not None:
        if not isinstance(score, str):
            raise ContractError("score must be H-A or null")
        parts = score.split("-")
        if len(parts) != 2 or any(not x.isdigit() or len(x) > 2 for x in parts):
            raise ContractError("score must be H-A or null")
    minute = ctx.get("match_minute")
    if minute is not None:
        if isinstance(minute, bool) or not isinstance(minute, (int, float)) or not 0 <= minute <= 130:
            raise ContractError("match_minute must be 0..130 or null")
    event = _choice(
        ctx,
        "material_event_since_frozen",
        {"NONE_VERIFIED", "GOAL", "RED_CARD", "OTHER_MATERIAL", "UNKNOWN"},
    )
    if status == "PREMATCH_CONFIRMED" and (
        minute is not None or score not in (None, "0-0")
    ):
        raise ContractError("prematch football context cannot contain live score/minute")
    thesis = _choice(
        ctx, "thesis_state", {"PRESERVED", "BROKEN", "UNKNOWN"}
    )
    intact = ctx.get("primary_mechanism_intact")
    if intact is not None and type(intact) is not bool:
        raise ContractError("primary_mechanism_intact must be true/false/null")
    veto = ctx.get("material_veto")
    if veto is not None and type(veto) is not bool:
        raise ContractError("material_veto must be true/false/null")
    board_state = _enum(
        BoardState, _required(ctx, "board_state"), "board_state"
    )
    incentive = validate_tournament_incentive(match_obj)
    needs = []
    if status == "UNKNOWN":
        needs.append("CURRENT_FIXTURE_STATUS_UNVERIFIED")
    if status in {"STARTED", "HALFTIME"} and (minute is None or score is None):
        needs.append("LIVE_SCORE_OR_MINUTE_UNVERIFIED")
    if event != "NONE_VERIFIED":
        needs.append("MATERIAL_EVENT_FOOTBALL_RECHECK")
    if thesis == "UNKNOWN" or intact is None:
        needs.append("CURRENT_PRIMARY_THESIS_UNVERIFIED")
    if veto is None:
        needs.append("CURRENT_MATERIAL_VETO_UNVERIFIED")
    if incentive["resolution_status"] == "INCENTIVE_RECHECK_REQUIRED":
        needs.append("TOURNAMENT_INCENTIVE_RECHECK_REQUIRED")
    risk = (
        thesis == "BROKEN" or intact is False or veto is True
        or a.material_suppression or a.failure_attacks_route
    )
    compiled_burden = certified_supported_burden(a, model)
    compiled_basis = certified_supported_burden_basis(a, model)
    funded_at_frozen_line = compiled_burden is not None
    if risk:
        read = "FOOTBALL_THESIS_ADVERSE"
    elif needs:
        read = "FOOTBALL_ANALYSIS_WITH_EXPLICIT_RECHECKS"
    else:
        read = "FOOTBALL_THESIS_CURRENTLY_INTACT"
    tail_profile = prospective_goal_funding(a, model)
    result = {
        "schema_version": SCHEMA_VERSION,
        "stage": "football_assessment_result",
        "model": model,
        "match_id": a.match_id,
        "fixture_status": status,
        "score": score,
        "match_minute": minute,
        "material_event_since_frozen": event,
        "board_state": board_state.value,
        "football_read": read,
        "football_assessment_completed": True,
        "limitations": needs,
        "home_route": a.home_route.name,
        "away_route": a.away_route.name,
        "carrier": a.carrier.name,
        "route_reliability": a.route_reliability.name,
        "chance_quality": a.chance_quality.name,
        "failure_resistance": a.failure_resistance.name,
        "frozen_supported_line": compiled_burden,
        "frozen_supported_line_funding": funded_at_frozen_line,
        "frozen_supported_line_basis": compiled_basis,
        "supported_line_role": "DETERMINISTIC_CERTIFIED_BURDEN",
        "declared_supported_line": a.supported_line,
        "declared_supported_line_basis": a.supported_line_basis,
        **tail_profile,
        "frozen_line_not_live_executable": True,
        "quote_required_for_football_assessment": False,
        "quote_requested": False,
        "quote_status": "UNPRICED_NOT_REQUIRED_FOR_FOOTBALL",
        "decision_action": "NOT_EVALUATED_NO_CURRENT_PRICE",
        "bet_authorized": False,
        "wait_authorized": False,
        "model_accounting_status": "NONE",
        "actual_user_bet": None,
        "tournament_incentive_required": incentive["required"],
        "tournament_incentive_resolution": incentive["resolution_status"],
        "home_incentive": incentive["home_incentive"],
        "away_incentive": incentive["away_incentive"],
        "tiebreak_margin_relevance": incentive["tiebreak_margin_relevance"],
        "incentive_effect": incentive["incentive_effect"],
        "interpretation": (
            "This is an independent model football assessment, NOT a priced "
            "BET/WAIT/PASS. Frozen supported burden is compiled deterministically "
            "from goal certificates, not chosen by the researcher or market. Only an independently "
            "verified current quote and separate authorization can create "
            "a betting action."
        ),
    }
    if model == "c":
        result.update({
            "completion_mode": a.completion_mode.name,
            "burden_completion_quality": a.burden_completion_quality.name,
            "continuation_quality": a.continuation_quality.name,
            "burden_stall_risk": a.burden_stall_risk.name,
        })
    else:
        floor, reasons = c2_selection_floor(a)
        result.update({
            "selection_floor": floor.value,
            "selection_floor_reasons": list(reasons),
            "c2_leakage_goal3_funded": c2_low_burden_leakage_goal3_funded(a),
        })
        if a.c2_opponent_leakage is not None:
            result["c2_opponent_leakage"] = a.c2_opponent_leakage.name
            result["c2_opponent_leakage_basis"] = a.c2_opponent_leakage_basis
    return result


def evaluate_observed_quote(
    payload: dict[str, Any],
    quote: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate an observed price with C/C2 policy but no execution authority.

    This is the single comparison path for screenshots and other non-executable
    observations. It deliberately reuses the same pure policy functions used by
    run_decision(). Execution-only requirements such as quote revalidation,
    Decision State persistence, XI authorization and publication are not
    manufactured here.

    WAIT is available only when the caller explicitly established
    wait_reachable=true and wait_requires_negative_info=false for this model's
    supported burden. No line-gap heuristic is invented by the wrapper.
    """

    football = run_football_assessment(payload)
    model = football["model"]
    ctx_obj = _required(payload, "context")
    match_obj = _required(payload, "match")
    a = parse_assessment(match_obj, require_c_completion=(model == "c"))
    compiled_burden = certified_supported_burden(a, model)

    if not isinstance(quote, dict):
        raise ContractError("observed quote must be an object")
    raw_line = quote.get("line")
    raw_odds = quote.get("odds")
    if isinstance(raw_line, bool) or not isinstance(raw_line, (int, float)):
        raise ContractError("observed quote.line must be numeric")
    if isinstance(raw_odds, bool) or not isinstance(raw_odds, (int, float)):
        raise ContractError("observed quote.odds must be numeric")
    try:
        observed = Quote(float(raw_line), float(raw_odds))
    except ValueError as exc:
        raise ContractError(str(exc)) from exc

    relation = (
        "NO_CERTIFIED_BURDEN"
        if compiled_burden is None
        else "ABOVE_SUPPORTED_BURDEN"
        if observed.line > compiled_burden
        else "AT_SUPPORTED_BURDEN"
        if observed.line == compiled_burden
        else "BELOW_SUPPORTED_BURDEN"
    )

    # A started fixture can still be assessed as football, but a prematch quote
    # action must not be recreated retrospectively.
    if football["fixture_status"] != "PREMATCH_CONFIRMED":
        return {
            "schema_version": SCHEMA_VERSION,
            "stage": "observed_quote_evaluation",
            "model": model,
            "match_id": a.match_id,
            "action": "LIVE_PRICE_BURDEN_COMPARISON_ONLY",
            "reason": "started fixture; prematch ACT/WAIT/PASS not re-created",
            "supported_line": compiled_burden,
            "observed_line": observed.line,
            "observed_odds": observed.odds,
            "line_relation": relation,
            "execution_authorized": False,
            "publication_authorized": False,
            "model_exposure_created": False,
        }

    if football["football_read"] != "FOOTBALL_THESIS_CURRENTLY_INTACT":
        return {
            "schema_version": SCHEMA_VERSION,
            "stage": "observed_quote_evaluation",
            "model": model,
            "match_id": a.match_id,
            "action": "NOT_EVALUATED_CURRENT_FOOTBALL_RECHECK_REQUIRED",
            "reason": "current football thesis is adverse or incomplete",
            "supported_line": compiled_burden,
            "observed_line": observed.line,
            "observed_odds": observed.odds,
            "line_relation": relation,
            "execution_authorized": False,
            "publication_authorized": False,
            "model_exposure_created": False,
        }

    board_state = _enum(
        BoardState, _required(ctx_obj, "board_state"), "board_state"
    )
    thesis_state = _enum(
        ThesisState, _required(ctx_obj, "thesis_state"), "thesis_state"
    )
    intact = ctx_obj.get("primary_mechanism_intact")
    veto = ctx_obj.get("material_veto")
    if type(intact) is not bool or type(veto) is not bool:
        raise ContractError(
            "observed quote evaluation requires current primary_mechanism_intact "
            "and material_veto booleans"
        )

    top_ranked = ctx_obj.get("top_ranked_focus", False)
    if type(top_ranked) is not bool:
        raise ContractError("top_ranked_focus must be true/false when provided")

    wait_reachable = ctx_obj.get("wait_reachable", False)
    if type(wait_reachable) is not bool:
        raise ContractError("wait_reachable must be true/false when provided")
    wait_negative = ctx_obj.get("wait_requires_negative_info", True)
    if type(wait_negative) is not bool:
        raise ContractError(
            "wait_requires_negative_info must be true/false when provided"
        )
    wait_basis = ctx_obj.get("wait_reachability_basis")
    negative_basis = ctx_obj.get("wait_negative_info_basis")
    if wait_reachable and (
        not isinstance(wait_basis, str) or not wait_basis.strip()
    ):
        raise ContractError(
            "reachable WAIT requires non-empty wait_reachability_basis"
        )
    if wait_negative and (
        negative_basis is not None
        and (not isinstance(negative_basis, str) or not negative_basis.strip())
    ):
        raise ContractError(
            "wait_negative_info_basis must be non-empty when provided"
        )

    qctx = ModelQuoteContext(
        board_state=board_state,
        thesis_state=thesis_state,
        quote=observed,
        top_ranked_focus=top_ranked,
        primary_mechanism_intact=intact,
        wait_reachable=wait_reachable,
        wait_requires_negative_info=wait_negative,
        material_veto=veto,
    )
    decision = (
        evaluate_c_quote(a, qctx)
        if model == "c"
        else evaluate_c2_quote(a, qctx)
    )
    wait_target_line = None
    wait_min_odds = None
    if decision.action == Action.WAIT:
        wait_target_line, wait_min_odds = model_wait_target(a, qctx, model)

    return {
        "schema_version": SCHEMA_VERSION,
        "stage": "observed_quote_evaluation",
        "model": model,
        "match_id": a.match_id,
        "action": "ACT" if decision.action == Action.BET else decision.action.value,
        "engine_action": decision.action.value,
        "reason": decision.reason,
        "bridge_used": decision.bridge_used,
        "supported_line": compiled_burden,
        "observed_line": observed.line,
        "observed_odds": observed.odds,
        "line_relation": relation,
        "market_line_funded": market_line_funded(a, observed.line, model),
        **prospective_goal_funding(a, model),
        "wait_target_line": wait_target_line,
        "wait_min_odds": wait_min_odds,
        "wait_reachable": wait_reachable,
        "wait_reachability_basis": wait_basis,
        "wait_requires_negative_info": wait_negative,
        "execution_authorized": False,
        "publication_authorized": False,
        "model_exposure_created": False,
    }


def run_decision(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "decision")

    model = _active_model(payload)

    raw_match = _required(payload, "match")
    a = parse_assessment(raw_match, require_c_completion=(model == "c"))
    compiled_burden = certified_supported_burden(a, model)
    compiled_basis = certified_supported_burden_basis(a, model)

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
    tournament_gate = validate_tournament_incentive(raw_match, require_resolution=True)
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
    post_xi_research_note = _string(ctx_obj, "post_xi_research_note")

    fixture_status = _choice(
        ctx_obj,
        "fixture_status",
        {
            "PREMATCH_CONFIRMED",
            "STARTED",
            "POSTPONED",
            "CANCELLED",
            "FINISHED",
            "UNKNOWN",
        },
    )
    if fixture_status != "PREMATCH_CONFIRMED":
        raise ContractError(
            "DECISION BLOCKED — STEP2 FIXTURE NOT CONFIRMED PREMATCH: "
            f"fixture_status={fixture_status}"
        )

    quote_revalidated = _required_bool(ctx_obj, "quote_revalidated")
    if not quote_revalidated:
        raise ContractError(
            "DECISION BLOCKED — CURRENT QUOTE NOT REVALIDATED"
        )

    market_history_status = _choice(
        ctx_obj,
        "market_history_status",
        {"FOUND", "PARTIAL", "UNAVAILABLE_ATTEMPTED"},
    )
    market_history_movement = _choice(
        ctx_obj,
        "market_history_movement",
        {
            "UP_0.50_PLUS",
            "UP_0.25",
            "STABLE",
            "DOWN_0.25",
            "DOWN_0.50_PLUS",
            "MIXED",
            "UNCLEAR",
        },
    )
    market_history_conflict_recheck = _choice(
        ctx_obj,
        "market_history_conflict_recheck",
        {
            "NOT_REQUIRED",
            "RECHECKED_FOOTBALL_EXPLAINED",
            "RECHECKED_UNEXPLAINED",
            "LIMITED",
        },
    )
    market_history_note = _string(ctx_obj, "market_history_note")

    if market_history_status == "UNAVAILABLE_ATTEMPTED":
        if market_history_movement != "UNCLEAR":
            raise ContractError(
                "UNAVAILABLE_ATTEMPTED market history requires movement=UNCLEAR"
            )

    h2h_review_status = _enum(
        H2HReviewStatus,
        _required(ctx_obj, "h2h_review_status"),
        "h2h_review_status",
    )
    h2h_rechecked = _required_bool(ctx_obj, "h2h_rechecked")
    if not h2h_rechecked:
        raise ContractError("DECISION BLOCKED — H2H RECHECK MISSING")
    h2h_basis = _string(ctx_obj, "h2h_basis")

    completion_rechecked = None
    c2_route_quality_rechecked = None
    if model == "c":
        completion_rechecked = _required_bool(ctx_obj, "completion_rechecked")
        if not completion_rechecked:
            raise ContractError(
                "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING"
            )
    else:
        c2_route_quality_rechecked = _required_bool(
            ctx_obj, "c2_route_quality_rechecked"
        )
        if not c2_route_quality_rechecked:
            raise ContractError(
                "DECISION BLOCKED — C2 ROUTE-QUALITY RECHECK MISSING"
            )

    board_state = _enum(
        BoardState, _required(ctx_obj, "board_state"), "board_state"
    )
    official_follow_lane = _enum(
        FollowLane,
        _required(ctx_obj, "official_follow_lane"),
        "official_follow_lane",
    )
    step2_authorization = _enum(
        Step2Authorization,
        _required(ctx_obj, "step2_authorization"),
        "step2_authorization",
    )
    thesis_state = _enum(
        ThesisState, _required(ctx_obj, "thesis_state"), "thesis_state"
    )
    thesis_state_basis = _string(ctx_obj, "thesis_state_basis")
    quote_obj = _required(ctx_obj, "quote")
    if not isinstance(quote_obj, dict):
        raise ContractError("quote must be an object")

    ctx = DecisionContext(
        board_state=board_state,
        official_follow_lane=official_follow_lane,
        step2_authorization=step2_authorization,
        thesis_state=thesis_state,
        thesis_state_basis=thesis_state_basis,
        quote=Quote(
            line=_number(quote_obj, "line"),
            odds=_number(quote_obj, "odds"),
        ),
        xi_status=xi_status,
        post_xi_research_status=post_xi_research_status,
        h2h_review_status=h2h_review_status,
        h2h_rechecked=h2h_rechecked,
        h2h_basis=h2h_basis,
        top_ranked_focus=_required_bool(ctx_obj, "top_ranked_focus"),
        primary_mechanism_intact=_required_bool(
            ctx_obj, "primary_mechanism_intact"
        ),
        primary_mechanism_basis=_string(ctx_obj, "primary_mechanism_basis"),
        wait_reachable=_required_bool(ctx_obj, "wait_reachable"),
        wait_reachability_basis=_string(ctx_obj, "wait_reachability_basis"),
        wait_requires_negative_info=_required_bool(
            ctx_obj, "wait_requires_negative_info"
        ),
        wait_negative_info_basis=_string(ctx_obj, "wait_negative_info_basis"),
        material_veto=_required_bool(ctx_obj, "material_veto"),
        material_veto_basis=_string(ctx_obj, "material_veto_basis"),
    )

    decision = decide_c(a, ctx) if model == "c" else decide_c2(a, ctx)

    wait_target_line = None
    wait_min_odds = None
    accounting_line = None
    accounting_odds = None
    if decision.action == Action.WAIT:
        wait_target_line, wait_min_odds = wait_accounting_target(a, ctx, model)
        # A WAIT is a plan, not exposure. Do not assume that a future line was
        # reached or synthesize a model bet at the target price.
        accounting_status = "NONE"
        wait_resolution_default = "UNRESOLVED"
    elif decision.action == Action.BET:
        accounting_line = ctx.quote.line
        accounting_odds = ctx.quote.odds
        accounting_status = "DIRECT_BET" if model == "c" else "SHADOW_BET"
        wait_resolution_default = "NOT_APPLICABLE"
    else:
        accounting_status = "NONE"
        wait_resolution_default = "NOT_APPLICABLE"

    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "stage": "decision_result",
        "model": model,
        "match_id": a.match_id,
        "common_evidence_basis": a.common_evidence_basis,
        "supported_line": compiled_burden,
        "supported_line_basis": compiled_basis,
        "declared_supported_line": a.supported_line,
        "declared_supported_line_basis": a.supported_line_basis,
        "official_follow_lane": official_follow_lane.value,
        "step2_authorization": step2_authorization.value,
        "thesis_state": thesis_state.name,
        "thesis_state_basis": thesis_state_basis,
        "action": decision.action.value,
        "reason": decision.reason,
        "bridge_used": decision.bridge_used,
        "market_line_funded": market_line_funded(a, ctx.quote.line, model),
        **prospective_goal_funding(a, model),
        "supported_line_role": "DETERMINISTIC_CERTIFIED_BURDEN",
        "wait_target_line": wait_target_line,
        "wait_min_odds": wait_min_odds,
        "model_accounting_status": accounting_status,
        "model_accounting_line": accounting_line,
        "model_accounting_odds": accounting_odds,
        "wait_resolution_default": wait_resolution_default,
        "tournament_incentive_required": tournament_gate["required"],
        "tournament_format_status": tournament_gate["format_status"],
        "home_incentive": tournament_gate["home_incentive"],
        "away_incentive": tournament_gate["away_incentive"],
        "tiebreak_margin_relevance": tournament_gate["tiebreak_margin_relevance"],
        "incentive_effect": tournament_gate["incentive_effect"],
        "tournament_incentive_rechecked": tournament_incentive_rechecked,
        "tournament_incentive_recheck_status": tournament_incentive_recheck_status,
        "tournament_incentive_resolution": tournament_gate["resolution_status"],
        "xi_status": xi_status.value,
        "post_xi_research_status": post_xi_research_status.value,
        "post_xi_research_note": post_xi_research_note,
        "fixture_status": fixture_status,
        "quote_revalidated": quote_revalidated,
        "market_history_status": market_history_status,
        "market_history_movement": market_history_movement,
        "market_history_conflict_recheck": market_history_conflict_recheck,
        "market_history_note": market_history_note,
        "h2h_review_status": h2h_review_status.value,
        "h2h_rechecked": h2h_rechecked,
        "h2h_state": a.h2h_state,
        "h2h_effect": a.h2h_effect,
        "h2h_transferability": a.h2h_transferability,
        "h2h_current_corroboration": a.h2h_current_corroboration,
        "h2h_material_effect": a.h2h_material_effect,
        "h2h_basis": h2h_basis,
        "primary_mechanism_basis": ctx.primary_mechanism_basis,
        "wait_reachability_basis": ctx.wait_reachability_basis,
        "wait_negative_info_basis": ctx.wait_negative_info_basis,
        "material_veto_basis": ctx.material_veto_basis,
        "failure_attacks_route_basis": a.failure_attacks_route_basis,
        "material_suppression_basis": a.material_suppression_basis,
        "carrier_self_fund_basis": a.carrier_self_fund_basis,
        "independent_upper_tail_basis": a.independent_upper_tail_basis,
    }

    if model == "c":
        result["completion_rechecked"] = completion_rechecked
        result["current_burden_completion_quality"] = a.burden_completion_quality.name
        result["current_continuation_quality"] = a.continuation_quality.name
        result["current_burden_stall_risk"] = a.burden_stall_risk.name

    if model == "c2":
        result["c2_route_quality_rechecked"] = c2_route_quality_rechecked
        floor, reasons = c2_selection_floor(a)
        result["selection_floor"] = floor.value
        result["selection_floor_reasons"] = list(reasons)

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
        "wait_target_line": _nullable_number(frozen, "wait_target_line"),
        "wait_min_odds": _nullable_number(frozen, "wait_min_odds"),
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
    official_exposure_basis = _choice(
        pnl,
        "official_c_exposure_basis",
        {
            "DIRECT_BET",
            "WAIT_ASSUMED",
            "WAIT_USER_CONFIRMED",
            "WAIT_NOT_REACHED",
            "NONE",
        },
    )
    official_exposure_line = _nullable_number(pnl, "official_c_exposure_line")
    official_exposure_odds = _nullable_number(pnl, "official_c_exposure_odds")
    wait_resolution = _choice(
        pnl,
        "wait_resolution",
        {
            "NOT_APPLICABLE",
            "UNRESOLVED",
            "ASSUMED_REACHED",
            "USER_CONFIRMED",
            "USER_DECLARED_NOT_REACHED",
        },
    )
    legacy_assumed_policy = pnl.get("legacy_assumed_exposure_policy", False)
    if type(legacy_assumed_policy) is not bool:
        raise ContractError("legacy_assumed_exposure_policy must be true/false")
    user_executed = _required_bool(pnl, "user_executed")
    user_pnl = _nullable_number(pnl, "user_pnl")
    c2_shadow_only = _required_bool(pnl, "c2_shadow_only")

    c_action = frozen_out["c_action"]
    wait_target_line = frozen_out["wait_target_line"]
    wait_min_odds = frozen_out["wait_min_odds"]

    if c_action == "C_WAIT":
        if wait_target_line is None or wait_min_odds is None:
            raise ContractError(
                "C-WAIT audit requires frozen wait_target_line and wait_min_odds"
            )
        if official_exposure_basis not in {
            "NONE",
            "WAIT_ASSUMED",
            "WAIT_USER_CONFIRMED",
            "WAIT_NOT_REACHED",
        }:
            raise ContractError(
                "C-WAIT requires NONE / WAIT_USER_CONFIRMED / WAIT_NOT_REACHED "
                "or explicit historical WAIT_ASSUMED exposure basis"
            )
    elif c_action == "C_BET":
        if official_exposure_basis != "DIRECT_BET":
            raise ContractError("C-BET requires official_c_exposure_basis=DIRECT_BET")
        if wait_resolution != "NOT_APPLICABLE":
            raise ContractError("C-BET requires wait_resolution=NOT_APPLICABLE")
    else:
        if official_exposure_basis != "NONE":
            raise ContractError("C-PASS/NONE requires official_c_exposure_basis=NONE")
        if wait_resolution != "NOT_APPLICABLE":
            raise ContractError("C-PASS/NONE requires wait_resolution=NOT_APPLICABLE")

    if official_exposure_basis == "NONE" and c_action == "C_WAIT":
        if official_exposure:
            raise ContractError("unresolved C-WAIT with basis NONE cannot create exposure")
        if wait_resolution != "UNRESOLVED":
            raise ContractError("unresolved C-WAIT requires wait_resolution=UNRESOLVED")
        if official_exposure_line is not None or official_exposure_odds is not None:
            raise ContractError("unresolved C-WAIT requires null exposure line/odds")

    if official_exposure_basis == "WAIT_ASSUMED":
        if not legacy_assumed_policy:
            raise ContractError(
                "WAIT_ASSUMED is retired for current records; "
                "set legacy_assumed_exposure_policy=true only for frozen historical audit"
            )
        if not official_exposure:
            raise ContractError("WAIT_ASSUMED requires official_c_exposure=true")
        if wait_resolution != "ASSUMED_REACHED":
            raise ContractError("WAIT_ASSUMED requires wait_resolution=ASSUMED_REACHED")
        if (
            official_exposure_line != wait_target_line
            or official_exposure_odds != wait_min_odds
        ):
            raise ContractError(
                "WAIT_ASSUMED exposure line/odds must equal frozen WAIT target/minimum"
            )

    if official_exposure_basis == "WAIT_USER_CONFIRMED":
        if not official_exposure:
            raise ContractError("WAIT_USER_CONFIRMED requires official_c_exposure=true")
        if wait_resolution != "USER_CONFIRMED":
            raise ContractError(
                "WAIT_USER_CONFIRMED requires wait_resolution=USER_CONFIRMED"
            )
        if not user_executed:
            raise ContractError(
                "WAIT_USER_CONFIRMED requires user_executed=true"
            )

    if official_exposure_basis == "WAIT_NOT_REACHED":
        if official_exposure:
            raise ContractError("WAIT_NOT_REACHED requires official_c_exposure=false")
        if wait_resolution != "USER_DECLARED_NOT_REACHED":
            raise ContractError(
                "WAIT_NOT_REACHED requires wait_resolution=USER_DECLARED_NOT_REACHED"
            )
        if official_exposure_line is not None or official_exposure_odds is not None:
            raise ContractError(
                "WAIT_NOT_REACHED requires null official exposure line/odds"
            )

    if official_exposure_basis == "DIRECT_BET":
        if not official_exposure:
            raise ContractError("DIRECT_BET requires official_c_exposure=true")
        if (
            official_exposure_line != frozen_out["quote_line"]
            or official_exposure_odds != frozen_out["quote_odds"]
        ):
            raise ContractError(
                "DIRECT_BET exposure line/odds must equal frozen direct quote"
            )

    if official_exposure_basis == "NONE":
        if official_exposure:
            raise ContractError("NONE exposure basis requires official_c_exposure=false")
        if official_exposure_line is not None or official_exposure_odds is not None:
            raise ContractError(
                "NONE exposure basis requires null official exposure line/odds"
            )

    if official_exposure and (
        official_exposure_line is None or official_exposure_odds is None
    ):
        raise ContractError(
            "official exposure requires exact official_c_exposure_line and official_c_exposure_odds"
        )

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
            "legacy_assumed_exposure_policy": legacy_assumed_policy,
            "official_c_model_pnl": official_pnl,
            "official_c_exposure_basis": official_exposure_basis,
            "official_c_exposure_line": official_exposure_line,
            "official_c_exposure_odds": official_exposure_odds,
            "wait_resolution": wait_resolution,
            "user_executed": user_executed,
            "user_pnl": user_pnl,
            "c2_shadow_only": c2_shadow_only,
        },
    }
