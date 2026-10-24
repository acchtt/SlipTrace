from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from evidence_contract import g4_evidence_review, g4_diagnostics
from production_scope import scope_profile

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
    c_g3_book_extension_profile,
    c_intermediate_burden_profile,
    c_goal3_mechanism_class,
    c_endpoint_control_pressure,
    c_g3_endpoint_control_pressure,
    c_upper_tail_control_pressure,
    c_execution_strength,
    c_direct_act_ceiling,
    compile_c_board_state,
    c2_low_burden_leakage_goal3_funded,
    clearing_goal_funded,
    low_burden_leakage_goal3_funded,
    decide_c,
    decide_c2,
    evaluate_c_quote,
    evaluate_c2_quote,
    follow_through_lane,
    follow_priority_profile,
    rank_assessments,
    rank_assessments_c2,
    ranking_key,
    ranking_key_clearability_challenger,
    c2_ranking_key,
    model_wait_target,
    wait_accounting_target,
    market_line_funded,
    prospective_goal_funding,
    certified_supported_burden,
    certified_supported_burden_basis,
)


SCHEMA_VERSION = "football-engine-v1"
MAX_FOLLOW = 7
MAX_RESERVE = 4
MAX_FOLLOW_PER_KICKOFF = 3


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


def _display_board_state(state: BoardState) -> str:
    """User-facing rank label; WATCH is internal metadata, not an /xi verdict."""
    return "REVIEW_ONLY" if state == BoardState.WATCH else state.name


def _declared_board_state(
    obj: dict[str, Any],
    *,
    fallback: dict[str, Any] | None = None,
    allow_fallback_without_basis: bool = False,
) -> tuple[BoardState, str, str]:
    """Read the research declaration without granting it production authority.

    New payloads use declared_board_state. Historical receipts with board_state
    remain readable. The basis follows the same precedence.
    """

    if "declared_board_state" in obj:
        field = "declared_board_state"
        raw = obj[field]
        basis_field = "declared_board_state_basis"
        if basis_field not in obj:
            basis_field = "board_state_basis"
    elif "board_state" in obj:
        field = "board_state"
        raw = obj[field]
        basis_field = "board_state_basis"
    elif isinstance(fallback, dict) and "board_state" in fallback:
        field = "board_state"
        raw = fallback[field]
        basis_field = "board_state_basis"
        obj = fallback
    else:
        raise ContractError("missing required field: declared_board_state")

    state = _enum(BoardState, raw, field)
    if basis_field not in obj and allow_fallback_without_basis:
        basis = "LEGACY_CONTEXT_STATE_WITHOUT_DECLARATION_BASIS"
    else:
        basis = _string(obj, basis_field)
    return state, basis, field


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

    independent_upper_tail = _required_bool(obj, "independent_upper_tail")
    transfer_grade_present = "upper_tail_transferability" in obj
    transfer_basis_present = "upper_tail_transferability_basis" in obj
    context_signal_present = "upper_tail_comparable_context_signal" in obj
    context_basis_present = "upper_tail_comparable_context_basis" in obj
    if transfer_grade_present != transfer_basis_present:
        raise ContractError(
            "upper-tail transferability requires both "
            "upper_tail_transferability and upper_tail_transferability_basis"
        )
    if context_signal_present != context_basis_present:
        raise ContractError(
            "upper-tail comparable context requires both "
            "upper_tail_comparable_context_signal and "
            "upper_tail_comparable_context_basis"
        )
    if require_c_completion and independent_upper_tail and not transfer_grade_present:
        raise ContractError(
            "Football C independent_upper_tail requires explicit "
            "upper_tail_transferability and basis"
        )
    if require_c_completion and independent_upper_tail and not context_signal_present:
        raise ContractError(
            "Football C independent_upper_tail requires explicit "
            "upper_tail_comparable_context_signal and basis"
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
        independent_upper_tail=independent_upper_tail,
        independent_upper_tail_basis=_string(obj, "independent_upper_tail_basis"),
        upper_tail_transferability=(
            _enum(
                Grade,
                _required(obj, "upper_tail_transferability"),
                "upper_tail_transferability",
            )
            if transfer_grade_present
            else None
        ),
        upper_tail_transferability_basis=(
            _string(obj, "upper_tail_transferability_basis")
            if transfer_basis_present
            else None
        ),
        upper_tail_comparable_context_signal=(
            _choice(
                obj,
                "upper_tail_comparable_context_signal",
                {"SUPPORTIVE", "MIXED", "SUPPRESSIVE", "UNAVAILABLE"},
            )
            if context_signal_present
            else None
        ),
        upper_tail_comparable_context_basis=(
            _string(obj, "upper_tail_comparable_context_basis")
            if context_basis_present
            else None
        ),
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


G4_RESEARCH_STATUSES = frozenset({
    "G4_NOT_APPLICABLE",
    "G4_RESEARCH_INCOMPLETE",
    "G4_RESEARCH_COMPLETE_REJECTED",
    "G4_RESEARCH_COMPLETE_FUNDED",
    "G4_RESEARCH_COMPLETE_MIXED",
    "G4_RESEARCH_EVIDENCE_LIMITED",
})
G4_PATH_STATES = frozenset({"SUPPORTED", "FAILED", "MIXED", "UNAVAILABLE", "NOT_APPLICABLE"})
G4_CONTINUATION_STATES = frozenset({"HIGH", "MEDIUM", "LOW", "UNAVAILABLE", "NOT_APPLICABLE"})
G4_COMPLETENESS_FIELDS = frozenset({
    "g4_research_status",
    "g4_carrier_path",
    "g4_distributed_path",
    "g4_reply_path",
    "g4_continuation_after_g3",
    "upper_tail_transferability",
    "upper_tail_comparable_context_signal",
})


def _g4_research_profile(
    obj: dict[str, Any],
    a: MatchAssessment,
    *,
    model: str,
) -> dict[str, Any]:
    """Separate a true G4 rejection from an unfinished upper-tail investigation.

    Legacy payloads remain readable. A funded deterministic G4 can be inferred
    as complete; a G3-only payload without the explicit new contract is marked
    INCOMPLETE rather than silently treated as a completed G4 rejection.
    """
    if model != "c":
        return {
            "g4_research_status": "G4_NOT_APPLICABLE",
            "g4_research_explicit": False,
            "g4_carrier_path": "NOT_APPLICABLE",
            "g4_distributed_path": "NOT_APPLICABLE",
            "g4_reply_path": "NOT_APPLICABLE",
            "g4_continuation_after_g3": "NOT_APPLICABLE",
            "g4_research_basis": "retired/non-C path",
        }

    funding = prospective_goal_funding(a, model)
    goal3 = bool(funding["goal3_funded"])
    goal4 = bool(funding["goal4_funded"])
    raw_status = obj.get("g4_research_status")
    explicit = raw_status is not None

    if raw_status is None:
        if goal4:
            status = "G4_RESEARCH_COMPLETE_FUNDED"
            basis = (
                "LEGACY_INFERRED_FROM_DETERMINISTIC_G4: the current factual "
                "payload itself funds G4."
            )
        elif goal3:
            status = "G4_RESEARCH_INCOMPLETE"
            basis = (
                "LEGACY_G3_ONLY_NO_EXPLICIT_G4_COMPLETENESS: G4 was not "
                "proven complete-rejected by the frozen payload."
            )
        else:
            status = "G4_NOT_APPLICABLE"
            basis = "G3_NOT_FUNDED"
        return {
            "g4_research_status": status,
            "g4_research_explicit": False,
            "g4_carrier_path": "UNAVAILABLE" if goal3 and not goal4 else "NOT_APPLICABLE",
            "g4_distributed_path": "UNAVAILABLE" if goal3 and not goal4 else "NOT_APPLICABLE",
            "g4_reply_path": "UNAVAILABLE" if goal3 and not goal4 else "NOT_APPLICABLE",
            "g4_continuation_after_g3": "UNAVAILABLE" if goal3 and not goal4 else "NOT_APPLICABLE",
            "g4_research_basis": basis,
        }

    if not isinstance(raw_status, str) or raw_status not in G4_RESEARCH_STATUSES:
        raise ContractError(
            "g4_research_status must be one of: "
            + ", ".join(sorted(G4_RESEARCH_STATUSES))
        )
    declared_status = raw_status
    # Historical/runtime compatibility: old payloads may declare COMPLETE_MIXED.
    # Production completeness is binary.  Keep MIXED path diagnostics, but
    # compile the terminal non-funded state as COMPLETE_REJECTED.
    status = (
        "G4_RESEARCH_COMPLETE_REJECTED"
        if raw_status == "G4_RESEARCH_COMPLETE_MIXED"
        else raw_status
    )
    if status == "G4_NOT_APPLICABLE":
        if goal3:
            raise ContractError("G4_NOT_APPLICABLE is invalid when G3 is funded")
        return {
            "g4_research_status": status,
            "g4_research_explicit": True,
            "g4_carrier_path": "NOT_APPLICABLE",
            "g4_distributed_path": "NOT_APPLICABLE",
            "g4_reply_path": "NOT_APPLICABLE",
            "g4_continuation_after_g3": "NOT_APPLICABLE",
            "g4_research_basis": _string(obj, "g4_research_basis"),
        }

    if not goal3:
        raise ContractError(f"{status} requires a funded G3 certificate")
    if status == "G4_RESEARCH_COMPLETE_FUNDED" and not goal4:
        raise ContractError(
            "G4_RESEARCH_COMPLETE_FUNDED requires the deterministic C compiler to fund G4"
        )
    if status in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_COMPLETE_REJECTED", "G4_RESEARCH_COMPLETE_MIXED", "G4_RESEARCH_EVIDENCE_LIMITED"} and goal4:
        raise ContractError(
            f"{status} contradicts a deterministic funded G4 certificate"
        )

    paths: dict[str, str] = {}
    for field in ("g4_carrier_path", "g4_distributed_path", "g4_reply_path"):
        value = obj.get(field)
        if value is None and status in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_EVIDENCE_LIMITED"}:
            value = "UNAVAILABLE"
        if not isinstance(value, str) or value not in G4_PATH_STATES:
            raise ContractError(
                f"{field} must be one of: " + ", ".join(sorted(G4_PATH_STATES))
            )
        paths[field] = value

    continuation = obj.get("g4_continuation_after_g3")
    if continuation is None and status in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_EVIDENCE_LIMITED"}:
        continuation = "UNAVAILABLE"
    if (
        not isinstance(continuation, str)
        or continuation not in G4_CONTINUATION_STATES
    ):
        raise ContractError(
            "g4_continuation_after_g3 must be one of: "
            + ", ".join(sorted(G4_CONTINUATION_STATES))
        )
    basis = _string(obj, "g4_research_basis")
    if status == "G4_RESEARCH_COMPLETE_FUNDED":
        if "SUPPORTED" not in paths.values():
            raise ContractError(
                "G4_RESEARCH_COMPLETE_FUNDED requires at least one supported G4 path"
            )
        if continuation in {"UNAVAILABLE", "NOT_APPLICABLE"}:
            raise ContractError(
                "G4_RESEARCH_COMPLETE_FUNDED requires evaluated continuation after G3"
            )

    reviewed = g4_evidence_review(obj, {
        "g4_research_status": status,
        "g4_declared_research_status": declared_status,
        "g4_research_explicit": explicit,
        **paths,
        "g4_continuation_after_g3": continuation,
        "g4_research_basis": basis,
    })
    reviewed["g4_declared_research_status"] = declared_status
    reviewed["g4_status_normalized_from_mixed"] = (
        declared_status == "G4_RESEARCH_COMPLETE_MIXED"
    )
    return reviewed


def _check_envelope(payload: dict[str, Any], expected_stage: str) -> None:
    if not isinstance(payload, dict):
        raise ContractError("payload must be a JSON object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ContractError(
            f"schema_version must be {SCHEMA_VERSION!r}"
        )
    if payload.get("stage") != expected_stage:
        raise ContractError(f"stage must be {expected_stage!r}")


def _follow_portfolio_weight(row: dict[str, Any], role: str) -> int:
    """Comparable workload score for one FOLLOW role."""

    if role == "CLEARABILITY":
        return int(row.get("follow_clearability_score", 0))
    if role == "UPSIDE":
        return int(row.get("follow_upside_score", 0))
    return int(row.get("follow_balanced_score", row.get("follow_priority_score", 0)))


def _allocate_c_follow_lanes(rows: list[dict[str, Any]]) -> None:
    """Allocate FOLLOW as burden-normalized clear/balanced/upside coverage.

    Football C state and certificates are frozen before this allocator runs.
    FOLLOW is workload capacity only. Each exact kickoff can contribute up to
    three complementary nominations:

    1. CLEARABILITY — strongest burden-normalized protected-floor candidate;
    2. BALANCED — strongest remaining all-round current mechanism candidate;
    3. UPSIDE — strongest remaining burden-normalized ceiling candidate.

    This avoids two previous failure modes: certificate depth winning workload
    priority automatically, and a two-row exact-kickoff cap pretending there is
    predictive separation when several FOCUS rows remain credible.
    """

    for row in rows:
        if row.get("board_state") != "FOCUS":
            row["follow_lane"] = FollowLane.STOP.value
            row["follow_portfolio_role"] = "NOT_FOCUS"
            row["follow_portfolio_score"] = None
        else:
            row["follow_lane"] = FollowLane.FOCUS_UNFOLLOWED.value
            row["follow_portfolio_role"] = "UNALLOCATED"
            row["follow_portfolio_score"] = None

    blocks: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        if (
            row.get("board_state") == "FOCUS"
            and row.get("operational_viability_grade") == "A"
        ):
            blocks.setdefault(str(row["kickoff_ict"]), []).append(row)

    primary: list[tuple[dict[str, Any], str, int]] = []
    secondary: list[tuple[dict[str, Any], str, int]] = []

    for kickoff in sorted(blocks):
        candidates = blocks[kickoff]
        clear_pick = max(
            candidates,
            key=lambda row: (
                int(row.get("follow_clearability_score", 0)),
                int(row.get("follow_balanced_score", 0)),
                int(row.get("follow_upside_score", 0)),
                -int(row["rank"]),
            ),
        )
        primary.append(
            (
                clear_pick,
                "CLEARABILITY",
                _follow_portfolio_weight(clear_pick, "CLEARABILITY"),
            )
        )

        remaining = [row for row in candidates if row is not clear_pick]
        if remaining and MAX_FOLLOW_PER_KICKOFF > 1:
            balanced_pick = max(
                remaining,
                key=lambda row: (
                    int(row.get("follow_balanced_score", 0)),
                    int(row.get("follow_upside_score", 0)),
                    int(row.get("follow_clearability_score", 0)),
                    -int(row["rank"]),
                ),
            )
            secondary.append(
                (
                    balanced_pick,
                    "BALANCED",
                    _follow_portfolio_weight(balanced_pick, "BALANCED"),
                )
            )
            remaining = [row for row in remaining if row is not balanced_pick]

        if remaining and MAX_FOLLOW_PER_KICKOFF > 2:
            upside_pick = max(
                remaining,
                key=lambda row: (
                    int(row.get("follow_upside_score", 0)),
                    int(row.get("follow_balanced_score", 0)),
                    int(row.get("follow_clearability_score", 0)),
                    -int(row["rank"]),
                ),
            )
            secondary.append(
                (
                    upside_pick,
                    "UPSIDE",
                    _follow_portfolio_weight(upside_pick, "UPSIDE"),
                )
            )

    selected: list[tuple[dict[str, Any], str, int]] = []
    seen: set[str] = set()

    # First protect one burden-normalized floor candidate at every exact kickoff
    # while capacity permits. This prevents a congested later block from
    # consuming the whole board.
    for row, role, score in sorted(
        primary,
        key=lambda item: (
            item[0]["kickoff_ict"],
            int(item[0].get("follow_clearability_score", 0)),
            -int(item[0]["rank"]),
        ),
    ):
        if len(selected) >= MAX_FOLLOW:
            break
        mid = str(row["match_id"])
        if mid not in seen:
            selected.append((row, role, score))
            seen.add(mid)

    # Remaining slots go to the strongest complementary nominations globally.
    for row, role, score in sorted(
        secondary,
        key=lambda item: (
            item[2],
            int(item[0].get("follow_balanced_score", 0)),
            int(item[0].get("follow_upside_score", 0)),
            int(item[0].get("follow_clearability_score", 0)),
            -int(item[0]["rank"]),
        ),
        reverse=True,
    ):
        if len(selected) >= MAX_FOLLOW:
            break
        mid = str(row["match_id"])
        if mid not in seen:
            selected.append((row, role, score))
            seen.add(mid)

    for row, role, score in selected:
        row["follow_lane"] = FollowLane.FOLLOW.value
        row["follow_portfolio_role"] = role
        row["follow_portfolio_score"] = score

    reserve_pool = [
        row for row in rows
        if row.get("board_state") == "FOCUS"
        and row.get("follow_lane") == FollowLane.FOCUS_UNFOLLOWED.value
    ]
    reserve_pool.sort(
        key=lambda row: (
            1 if row.get("operational_viability_grade") == "A" else 0,
            int(row.get("follow_balanced_score", row.get("follow_priority_score", 0))),
            int(row.get("follow_upside_score", 0)),
            int(row.get("follow_clearability_score", 0)),
            -int(row["rank"]),
        ),
        reverse=True,
    )
    for row in reserve_pool[:MAX_RESERVE]:
        row["follow_lane"] = FollowLane.RESERVE.value
        row["follow_portfolio_role"] = "RESERVE"
        row["follow_portfolio_score"] = int(
            row.get("follow_balanced_score", row.get("follow_priority_score", 0))
        )

    for row in rows:
        if (
            row.get("board_state") == "FOCUS"
            and row.get("follow_lane") == FollowLane.FOCUS_UNFOLLOWED.value
        ):
            row["follow_portfolio_role"] = "FOCUS_UNFOLLOWED"
            row["follow_portfolio_score"] = int(
                row.get("follow_balanced_score", row.get("follow_priority_score", 0))
            )

def run_board(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "board")

    model = _active_model(payload)

    raw_matches = _required(payload, "matches")
    if not isinstance(raw_matches, list) or not raw_matches:
        raise ContractError("matches must be a non-empty array")

    for raw in raw_matches:
        scope = scope_profile(raw)
        if not scope["production_allowed"]:
            raise ContractError("PRODUCTION SCOPE BLOCKED — " + scope["status"])
    parsed = [
        parse_assessment(item, require_c_completion=(model == "c"))
        for item in raw_matches
    ]
    raw_by_id = {str(item["match_id"]): item for item in raw_matches}
    if len(raw_by_id) != len(raw_matches):
        raise ContractError("duplicate match_id in board input")
    compiled_state_by_id = {
        item.match_id: compile_c_board_state(item) for item in parsed
    } if model == "c" else {}
    if model == "c":
        # Football C owns production state. Researcher-declared state remains
        # visible below solely as audit metadata.
        ranked = sorted(
            parsed,
            key=lambda item: (
                compiled_state_by_id[item.match_id],
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

    for rank, ranked_item in enumerate(ranked, start=1):
        item = ranked_item
        raw = raw_by_id[item.match_id]
        kickoff_block = _kickoff_block(raw)
        operational_gate = validate_operational_viability(raw)
        incentive_gate = validate_tournament_incentive(raw)
        tail_profile = prospective_goal_funding(item, model)
        follow_profile = follow_priority_profile(item) if model == "c" else {}
        g4_profile = _g4_research_profile(raw, item, model=model)
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
            **follow_profile,
            **g4_profile,
            "certificate_diagnostics": g4_diagnostics(item),
            "production_scope": scope_profile(raw),
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
            "upper_tail_transferability": (
                item.upper_tail_transferability.name
                if item.upper_tail_transferability is not None
                else None
            ),
            "upper_tail_transferability_basis": item.upper_tail_transferability_basis,
            "upper_tail_comparable_context_signal": item.upper_tail_comparable_context_signal,
            "upper_tail_comparable_context_basis": item.upper_tail_comparable_context_basis,
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
            row["ranking_challenger_key"] = list(
                ranking_key_clearability_challenger(item)
            )
            row["completion_mode"] = item.completion_mode.value
            row["burden_completion_quality"] = item.burden_completion_quality.name
            row["continuation_quality"] = item.continuation_quality.name
            row["opponent_leakage"] = item.opponent_leakage.name
            row["burden_stall_risk"] = item.burden_stall_risk.name
            row["execution_strength"] = c_execution_strength(item)
            row["g3_endpoint_control_pressure"] = c_g3_endpoint_control_pressure(item)
            row["upper_tail_control_pressure"] = c_upper_tail_control_pressure(item)
            row["endpoint_control_pressure"] = c_endpoint_control_pressure(item)
            row["direct_act_ceiling"] = c_direct_act_ceiling(item)
            row["goal3_mechanism_class"] = c_goal3_mechanism_class(item)
            row["intermediate_burden_profile"] = c_intermediate_burden_profile(item)

        declared_state, declared_basis, declared_state_source = (
            _declared_board_state(raw)
        )
        state = (
            compiled_state_by_id[item.match_id]
            if model == "c" else declared_state
        )
        row["board_state"] = state.name
        row["display_state"] = _display_board_state(state)
        row["board_state_basis"] = (
            "DETERMINISTIC_C_CERTIFICATE_COMPILER: funded G3 => FOCUS; "
            "direct route destruction/material suppression => PASS; otherwise REVIEW_ONLY"
            if model == "c" else declared_basis
        )
        row["declared_board_state"] = declared_state.name
        row["declared_board_state_basis"] = declared_basis
        row["declared_board_state_source"] = declared_state_source
        row["board_state_mismatch"] = declared_state != state
        if model == "c":
            validate_c_screen_state(item, state)
        else:
            validate_c2_screen_state(item, state)

        if model == "c2":
            floor, reasons = c2_selection_floor(item)
            row["selection_floor"] = floor.value
            row["selection_floor_reasons"] = list(reasons)
            row["c2_leakage_goal3_funded"] = c2_low_burden_leakage_goal3_funded(item)
            if item.c2_opponent_leakage is not None:
                row["c2_opponent_leakage"] = item.c2_opponent_leakage.name
                row["c2_opponent_leakage_basis"] = item.c2_opponent_leakage_basis

        output.append(row)

    if model == "c":
        _allocate_c_follow_lanes(output)

    result = {
        "schema_version": SCHEMA_VERSION,
        "stage": "board_result",
        "model": model,
        "ranking_policy": (
            "FOOTBALL_C_COMPILED_STATE_CHAMPION_RANK_CLEARABILITY_SHADOW"
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
        result["focus_unfollowed_count"] = sum(
            row.get("follow_lane") == FollowLane.FOCUS_UNFOLLOWED.value
            for row in output
        )
        result["stop_count"] = sum(
            row.get("follow_lane") == FollowLane.STOP.value for row in output
        )
        result["follow_capacity"] = MAX_FOLLOW
        result["reserve_capacity"] = MAX_RESERVE
        result["max_follow_per_exact_kickoff"] = MAX_FOLLOW_PER_KICKOFF
        qa_flags: list[str] = []
        if len(output) >= 5 and all(
            row.get("operational_viability_grade") == "B" for row in output
        ):
            qa_flags.append("OPERATIONAL_GRADE_SATURATION")
        g3_rows = [row for row in output if row.get("goal3_funded") is True]
        if (
            len(g3_rows) >= 5
            and sum(
                row.get("g4_research_status") in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_EVIDENCE_LIMITED"}
                for row in g3_rows
            ) / len(g3_rows) >= 0.80
        ):
            qa_flags.append("UPPER_TAIL_RESEARCH_ANOMALY")
        if any(row.get("g4_declared_research_status") == "G4_RESEARCH_COMPLETE_REJECTED"
               and row.get("g4_evidence_gaps") for row in output):
            qa_flags.append("G4_REJECTION_EVIDENCE_GAPS")
        if any(not row["production_scope"]["production_allowed"] for row in output):
            qa_flags.append("PRODUCTION_SCOPE_UNVERIFIED_OR_EXCLUDED")
        result["qa_flags"] = qa_flags

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
    declared_board_state, declared_board_state_basis, declared_state_source = (
        _declared_board_state(
            match_obj,
            fallback=ctx,
            allow_fallback_without_basis=True,
        )
    )
    board_state = (
        compile_c_board_state(a) if model == "c" else declared_board_state
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
    g4_profile = _g4_research_profile(match_obj, a, model=model)
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
        "declared_board_state": declared_board_state.name,
        "declared_board_state_basis": declared_board_state_basis,
        "declared_board_state_source": declared_state_source,
        "board_state_mismatch": board_state != declared_board_state,
        "rank_state_internal": board_state.name,
        "rank_state_display": _display_board_state(board_state),
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
        **g4_profile,
        "certificate_diagnostics": g4_diagnostics(a),
        "production_scope": scope_profile(match_obj, ctx),
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
            "execution_strength": c_execution_strength(a),
            "g3_endpoint_control_pressure": c_g3_endpoint_control_pressure(a),
            "upper_tail_control_pressure": c_upper_tail_control_pressure(a),
            "endpoint_control_pressure": c_endpoint_control_pressure(a),
            "direct_act_ceiling": c_direct_act_ceiling(a),
            "goal3_mechanism_class": c_goal3_mechanism_class(a),
            "intermediate_burden_profile": c_intermediate_burden_profile(a),
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


CERTIFICATE_UPGRADE_FIELDS = frozenset({
    "g4_path_evidence", "grade_evidence", "failure_mechanisms", "g4_global_blockers",
    "home_route",
    "away_route",
    "carrier",
    "route_reliability",
    "independent_route_quality",
    "chance_quality",
    "failure_resistance",
    "evidence_confidence",
    "burden_protection",
    "carrier_self_fund",
    "independent_upper_tail",
    "upper_tail_transferability",
    "upper_tail_comparable_context_signal",
    "burden_completion_quality",
    "continuation_quality",
    "opponent_leakage",
    "burden_stall_risk",
    "material_suppression",
    "failure_attacks_route",
    "tournament_incentive",
    "g4_research_status",
    "g4_carrier_path",
    "g4_distributed_path",
    "g4_reply_path",
    "g4_continuation_after_g3",
})

MATERIAL_MARKET_DISAGREEMENT_GOALS = 0.50


def _market_disagreement_recheck_gate(
    ctx_obj: dict[str, Any],
    *,
    compiled_burden: float | None,
    observed_line: float,
) -> dict[str, Any]:
    """Hard-gate screenshot /xi when market burden materially exceeds C.

    The market is only a trigger for football research. It can never certify
    or upgrade a goal burden by itself. A material gap uses the existing
    0.50+ movement threshold already distinguished by the decision contract.
    """

    material_gap = (
        compiled_burden is not None
        and observed_line >= compiled_burden + MATERIAL_MARKET_DISAGREEMENT_GOALS
    )
    frozen_g4_status = ctx_obj.get(
        "frozen_board_g4_research_status", "LEGACY_UNKNOWN"
    )
    if frozen_g4_status not in G4_RESEARCH_STATUSES | {"LEGACY_UNKNOWN"}:
        raise ContractError("invalid frozen_board_g4_research_status")
    completeness_recheck = (
        material_gap
        and observed_line >= 3.0
        and frozen_g4_status in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_EVIDENCE_LIMITED"}
    )
    prior_reclassification_recheck = (
        material_gap
        and observed_line >= 3.0
        and frozen_g4_status in {"G4_RESEARCH_COMPLETE_REJECTED", "G4_RESEARCH_COMPLETE_MIXED"}
    )
    if not material_gap:
        return {
            "market_disagreement_recheck_required": False,
            "market_disagreement_recheck_completed": True,
            "market_disagreement_gap_goals": (
                None if compiled_burden is None else observed_line - compiled_burden
            ),
            "market_disagreement_recheck_fields": [],
            "market_disagreement_recheck_evidence_refs": [],
            "market_disagreement_recheck_basis": "NOT_REQUIRED",
            "frozen_board_g4_research_status": frozen_g4_status,
            "certificate_completeness_recheck_required": False,
            "prior_certificate_reclassification_recheck_required": False,
        }

    status = ctx_obj.get("market_disagreement_recheck_status")
    basis = ctx_obj.get("market_disagreement_recheck_basis")
    fields = ctx_obj.get("market_disagreement_recheck_fields")
    refs = ctx_obj.get("market_disagreement_recheck_evidence_refs")

    completed = (
        status == "COMPLETED"
        and isinstance(basis, str)
        and bool(basis.strip())
        and isinstance(fields, list)
        and bool(fields)
        and all(isinstance(x, str) and x.strip() for x in fields)
        and isinstance(refs, list)
        and bool(refs)
        and all(isinstance(x, str) and x.strip() for x in refs)
    )

    normalized_fields = (
        [x.strip() for x in fields]
        if isinstance(fields, list)
        and all(isinstance(x, str) and x.strip() for x in fields)
        else []
    )
    invalid = sorted(set(normalized_fields) - CERTIFICATE_UPGRADE_FIELDS)
    if invalid:
        raise ContractError(
            "market disagreement recheck contains unsupported football fields: "
            + ", ".join(invalid)
        )

    # Any market burden that reaches the G4+ region must explicitly verify
    # the two upper-tail fields named by the /xi authority.
    missing_required_fields: list[str] = []
    if completed and observed_line >= 3.0:
        needed = {
            "upper_tail_transferability",
            "upper_tail_comparable_context_signal",
        }
        missing_required_fields = sorted(needed - set(normalized_fields))
        if missing_required_fields:
            completed = False

    return {
        "market_disagreement_recheck_required": True,
        "market_disagreement_recheck_completed": completed,
        "market_disagreement_gap_goals": observed_line - compiled_burden,
        "market_disagreement_recheck_fields": normalized_fields,
        "market_disagreement_recheck_evidence_refs": (
            [x.strip() for x in refs]
            if isinstance(refs, list)
            and all(isinstance(x, str) and x.strip() for x in refs)
            else []
        ),
        "market_disagreement_recheck_basis": (
            basis.strip() if isinstance(basis, str) and basis.strip() else None
        ),
        "market_disagreement_recheck_missing_fields": missing_required_fields,
        "frozen_board_g4_research_status": frozen_g4_status,
        "certificate_completeness_recheck_required": completeness_recheck,
        "prior_certificate_reclassification_recheck_required": prior_reclassification_recheck,
    }


def _quarter_or_none(value: Any, field: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ContractError(f"{field} must be numeric or null")
    number = float(value)
    if number < 0 or abs(number * 4 - round(number * 4)) > 1e-9:
        raise ContractError(f"{field} must use non-negative 0.25-goal increments")
    return number


def _certificate_upgrade_gate(
    ctx_obj: dict[str, Any],
    compiled_burden: float | None,
    *,
    model: str,
) -> dict[str, Any]:
    """Prevent market-triggered upward certificate drift at /xi.

    For a ranked match with a frozen board certificate, any higher current
    certificate must be justified by explicitly new football evidence in
    certificate-relevant fields. A screenshot/market burden may trigger the
    recheck but is never an eligible upgrade field.
    """

    if model != "c":
        return {
            "frozen_board_available": False,
            "frozen_board_certified_burden": None,
            "certificate_upgrade_status": "NOT_APPLICABLE",
            "certificate_upgrade_basis": "retired/non-C path",
            "certificate_upgrade_new_evidence_fields": [],
            "frozen_board_g4_research_status": "LEGACY_UNKNOWN",
            "certificate_upgraded": False,
        }

    frozen_available = _required_bool(ctx_obj, "frozen_board_available")
    frozen_burden = _quarter_or_none(
        _required(ctx_obj, "frozen_board_certified_burden"),
        "frozen_board_certified_burden",
    )
    frozen_g4_status = ctx_obj.get(
        "frozen_board_g4_research_status", "LEGACY_UNKNOWN"
    )
    if frozen_g4_status not in G4_RESEARCH_STATUSES | {"LEGACY_UNKNOWN"}:
        raise ContractError("invalid frozen_board_g4_research_status")
    status = _choice(
        ctx_obj,
        "certificate_upgrade_status",
        {
            "NOT_UPGRADED",
            "VERIFIED_NEW_FOOTBALL_EVIDENCE",
            "VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH",
            "VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION",
            "NO_FROZEN_BOARD",
        },
    )
    basis = _string(ctx_obj, "certificate_upgrade_basis")
    raw_fields = _required(ctx_obj, "certificate_upgrade_new_evidence_fields")
    if not isinstance(raw_fields, list) or any(
        not isinstance(field, str) or not field.strip() for field in raw_fields
    ):
        raise ContractError(
            "certificate_upgrade_new_evidence_fields must be a list of strings"
        )
    fields = [field.strip() for field in raw_fields]
    invalid = sorted(set(fields) - CERTIFICATE_UPGRADE_FIELDS)
    if invalid:
        raise ContractError(
            "certificate upgrade contains non-football/unsupported fields: "
            + ", ".join(invalid)
        )

    if not frozen_available:
        if frozen_burden is not None:
            raise ContractError(
                "NO_FROZEN_BOARD requires frozen_board_certified_burden=null"
            )
        if status != "NO_FROZEN_BOARD":
            raise ContractError(
                "frozen_board_available=false requires "
                "certificate_upgrade_status=NO_FROZEN_BOARD"
            )
        if fields:
            raise ContractError(
                "NO_FROZEN_BOARD must not claim certificate upgrade fields"
            )
        return {
            "frozen_board_available": False,
            "frozen_board_certified_burden": None,
            "certificate_upgrade_status": status,
            "certificate_upgrade_basis": basis,
            "certificate_upgrade_new_evidence_fields": [],
            "frozen_board_g4_research_status": frozen_g4_status,
            "certificate_upgraded": False,
        }

    upgraded = (
        compiled_burden is not None
        and (frozen_burden is None or compiled_burden > frozen_burden)
    )
    if upgraded:
        completion_repair = (
            frozen_g4_status in {"G4_RESEARCH_INCOMPLETE", "G4_RESEARCH_EVIDENCE_LIMITED"}
            and status == "VERIFIED_CERTIFICATE_COMPLETENESS_RESEARCH"
        )
        prior_misclassification_repair = (
            frozen_g4_status in {"G4_RESEARCH_COMPLETE_REJECTED", "G4_RESEARCH_COMPLETE_MIXED"}
            and status == "VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION"
        )
        if completion_repair:
            if not fields or not (set(fields) & G4_COMPLETENESS_FIELDS):
                raise ContractError(
                    "CERTIFICATE COMPLETENESS UPGRADE BLOCKED — name the "
                    "previously unassessed G4 certificate fields"
                )
        elif prior_misclassification_repair:
            recheck_status = ctx_obj.get("market_disagreement_recheck_status")
            recheck_basis = ctx_obj.get("market_disagreement_recheck_basis")
            recheck_fields = ctx_obj.get("market_disagreement_recheck_fields")
            recheck_refs = ctx_obj.get("market_disagreement_recheck_evidence_refs")
            valid_recheck = (
                recheck_status == "COMPLETED"
                and isinstance(recheck_basis, str)
                and bool(recheck_basis.strip())
                and isinstance(recheck_fields, list)
                and isinstance(recheck_refs, list)
                and bool(recheck_refs)
                and all(isinstance(x, str) and x.strip() for x in recheck_refs)
            )
            if not valid_recheck:
                raise ContractError(
                    "PRIOR CERTIFICATE RECLASSIFICATION BLOCKED — complete the "
                    "source-backed football disagreement recheck first"
                )
            normalized_recheck_fields = {
                x.strip()
                for x in recheck_fields
                if isinstance(x, str) and x.strip()
            }
            required_tail_fields = {
                "upper_tail_transferability",
                "upper_tail_comparable_context_signal",
            }
            if not required_tail_fields.issubset(normalized_recheck_fields):
                raise ContractError(
                    "PRIOR CERTIFICATE RECLASSIFICATION BLOCKED — recheck must "
                    "verify upper-tail transferability and comparable context"
                )
            if not fields or not (set(fields) & G4_COMPLETENESS_FIELDS):
                raise ContractError(
                    "PRIOR CERTIFICATE RECLASSIFICATION BLOCKED — name the "
                    "certificate-relevant G4 fields that were previously "
                    "misclassified or underweighted"
                )
        else:
            if status != "VERIFIED_NEW_FOOTBALL_EVIDENCE":
                raise ContractError(
                    "CERTIFICATE UPGRADE BLOCKED — higher current burden requires "
                    "VERIFIED_NEW_FOOTBALL_EVIDENCE, completed G4 research repair, "
                    "or VERIFIED_PRIOR_CERTIFICATE_MISCLASSIFICATION"
                )
            if not fields:
                raise ContractError(
                    "CERTIFICATE UPGRADE BLOCKED — name at least one newly changed "
                    "certificate-relevant football field"
                )
    else:
        if status != "NOT_UPGRADED":
            raise ContractError(
                "no upward certificate change requires "
                "certificate_upgrade_status=NOT_UPGRADED"
            )
        if fields:
            raise ContractError(
                "NOT_UPGRADED must not claim new certificate-upgrade fields"
            )

    return {
        "frozen_board_available": True,
        "frozen_board_certified_burden": frozen_burden,
        "certificate_upgrade_status": status,
        "certificate_upgrade_basis": basis,
        "certificate_upgrade_new_evidence_fields": fields,
        "frozen_board_g4_research_status": frozen_g4_status,
        "certificate_upgraded": upgraded,
    }


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

    Active Football C exposes ACT/BOOK/PASS. Legacy wait-reachability fields
    remain internal evidence that a conditional target can be reached without a
    negative football event; when valid, C returns BOOK rather than WAIT.
    """

    football = run_football_assessment(payload)
    if not football["production_scope"]["production_allowed"]:
        raise ContractError("PRODUCTION SCOPE BLOCKED — " + football["production_scope"]["status"])
    model = football["model"]
    ctx_obj = _required(payload, "context")
    match_obj = _required(payload, "match")
    a = parse_assessment(match_obj, require_c_completion=(model == "c"))
    compiled_burden = certified_supported_burden(a, model)
    upgrade_gate = _certificate_upgrade_gate(
        ctx_obj, compiled_burden, model=model
    )

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

    disagreement_gate = _market_disagreement_recheck_gate(
        ctx_obj,
        compiled_burden=compiled_burden,
        observed_line=observed.line,
    )
    book_profile = (
        c_g3_book_extension_profile(a)
        if model == "c"
        else {
            "eligible": False,
            "max_book_line": None,
            "book_min_odds": None,
            "basis": "retired/non-C path",
        }
    )

    if (
        disagreement_gate["market_disagreement_recheck_required"]
        and not disagreement_gate["market_disagreement_recheck_completed"]
    ):
        return {
            "schema_version": SCHEMA_VERSION,
            "stage": "observed_quote_evaluation",
            "model": model,
            "match_id": a.match_id,
            "action": "MARKET_DISAGREEMENT_RECHECK_REQUIRED",
            "reason": (
                "observed screenshot burden materially exceeds the current "
                "Football C certificate; complete the required football recheck "
                "and rerun the deterministic certificate before any ACT/BOOK/PASS"
            ),
            "supported_line": compiled_burden,
            "observed_line": observed.line,
            "observed_odds": observed.odds,
            "line_relation": relation,
            **disagreement_gate,
            "execution_authorized": False,
            "publication_authorized": False,
            "model_exposure_created": False,
        }


    if football.get("g4_evidence_gaps"):
        raise ContractError("G4 RESEARCH REQUIRED — " + ", ".join(football["g4_evidence_gaps"]))

    # A started fixture can still be assessed as football, but a prematch quote
    # action must not be recreated retrospectively.
    if football["fixture_status"] != "PREMATCH_CONFIRMED":
        return {
            "schema_version": SCHEMA_VERSION,
            "stage": "observed_quote_evaluation",
            "model": model,
            "match_id": a.match_id,
            "action": "LIVE_PRICE_BURDEN_COMPARISON_ONLY",
            "reason": "started fixture; prematch ACT/BOOK/PASS not re-created",
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

    declared_board_state, declared_board_state_basis, declared_state_source = (
        _declared_board_state(
            match_obj,
            fallback=ctx_obj,
            allow_fallback_without_basis=True,
        )
    )
    board_state = (
        compile_c_board_state(a) if model == "c" else declared_board_state
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
        "rank_state_internal": board_state.name,
        "rank_state_display": _display_board_state(board_state),
        "declared_board_state": declared_board_state.name,
        "declared_board_state_basis": declared_board_state_basis,
        "declared_board_state_source": declared_state_source,
        "board_state_mismatch": board_state != declared_board_state,
        "action": "ACT" if decision.action == Action.BET else decision.action.value,
        "engine_action": decision.action.value,
        "reason": decision.reason,
        "book_target_line": decision.book_target_line,
        "book_min_odds": decision.book_min_odds,
        "book_target_state": (
            "BOOK_TARGET_AVAILABLE" if decision.book_target_available else "NO_BOOK_TARGET"
        ),
        "current_price_clears_book_target": decision.current_price_clears_book_target,
        "book_order_is_exposure": False,
        "g3_book_extension_profile": book_profile,
        "bridge_used": decision.bridge_used,
        "supported_line": compiled_burden,
        "observed_line": observed.line,
        "observed_odds": observed.odds,
        "line_relation": relation,
        "market_line_funded": market_line_funded(a, observed.line, model),
        "execution_strength": (
            c_execution_strength(a) if model == "c" else "RETIRED_SHADOW"
        ),
        "endpoint_control_pressure": (
            c_endpoint_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "g3_endpoint_control_pressure": (
            c_g3_endpoint_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "upper_tail_control_pressure": (
            c_upper_tail_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "direct_act_ceiling": (
            c_direct_act_ceiling(a) if model == "c" else None
        ),
        "goal3_mechanism_class": (
            c_goal3_mechanism_class(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "intermediate_burden_profile": (
            c_intermediate_burden_profile(a) if model == "c" else None
        ),
        **prospective_goal_funding(a, model),
        "wait_target_line": wait_target_line,
        "wait_min_odds": wait_min_odds,
        "wait_reachable": wait_reachable,
        "wait_reachability_basis": wait_basis,
        "wait_requires_negative_info": wait_negative,
        **upgrade_gate,
        **disagreement_gate,
        "execution_authorized": False,
        "publication_authorized": False,
        "model_exposure_created": False,
    }


def evaluate_visible_quote_ladder(
    payload: dict[str, Any],
    quotes: list[dict[str, Any]],
) -> dict[str, Any]:
    """Evaluate only the complete ladder explicitly visible in one screenshot.

    A higher unsupported quote is diagnostic evidence, not authority to erase a
    lower executable line that is visible in the same image.  Selection is
    deterministic: prefer the highest visible ACT; otherwise retain the
    highest line at or below Football C's direct ceiling and return its normal
    BOOK/PASS result.  No line or price is interpolated.
    """

    if not isinstance(quotes, list) or not quotes:
        raise ContractError("visible screenshot ladder must be a non-empty array")

    normalized: list[dict[str, float]] = []
    seen_lines: set[float] = set()
    for index, quote in enumerate(quotes):
        if not isinstance(quote, dict):
            raise ContractError(f"visible ladder quote {index} must be an object")
        line = quote.get("line")
        odds = quote.get("odds")
        if isinstance(line, bool) or not isinstance(line, (int, float)):
            raise ContractError(f"visible ladder quote {index}.line must be numeric")
        if isinstance(odds, bool) or not isinstance(odds, (int, float)):
            raise ContractError(f"visible ladder quote {index}.odds must be numeric")
        item = {"line": float(line), "odds": float(odds)}
        if item["line"] in seen_lines:
            raise ContractError("visible screenshot ladder contains a duplicate line")
        seen_lines.add(item["line"])
        normalized.append(item)

    evaluations = [evaluate_observed_quote(payload, quote) for quote in normalized]
    act_candidates = [row for row in evaluations if row.get("action") == "ACT"]
    if act_candidates:
        selected = max(act_candidates, key=lambda row: float(row["observed_line"]))
        selection_basis = "HIGHEST_VISIBLE_EXECUTABLE_SUPPORTED_LINE"
        supported_visible = True
    else:
        supported_candidates = [
            row
            for row in evaluations
            if isinstance(row.get("direct_act_ceiling"), (int, float))
            and float(row["observed_line"]) <= float(row["direct_act_ceiling"])
        ]
        if supported_candidates:
            selected = max(
                supported_candidates, key=lambda row: float(row["observed_line"])
            )
            selection_basis = "HIGHEST_VISIBLE_LINE_WITHIN_DIRECT_CEILING"
            supported_visible = True
        else:
            # Retain a deterministic diagnostic when no visible line is
            # supported.  This does not invent a replacement price.
            selected = min(evaluations, key=lambda row: float(row["observed_line"]))
            selection_basis = "NO_SUPPORTED_VISIBLE_LINE_LOWEST_VISIBLE_DIAGNOSTIC"
            supported_visible = False

    direct_ceilings = [
        float(row["direct_act_ceiling"])
        for row in evaluations
        if isinstance(row.get("direct_act_ceiling"), (int, float))
    ]
    direct_ceiling = max(direct_ceilings) if direct_ceilings else None
    book_candidates = [
        row for row in evaluations
        if row.get("action") == "BOOK"
        and row.get("book_target_state") == "BOOK_TARGET_AVAILABLE"
    ]
    lowest_visible = min(item["line"] for item in normalized)

    if act_candidates:
        entry_state = "EXECUTABLE_NOW"
        entry_basis = "an exact visible screenshot line clears direct ACT policy"
    elif book_candidates:
        entry_state = "REALISTIC_PREGOAL_TARGET"
        entry_basis = (
            "no direct ACT is visible, but an exact conditional BOOK target is "
            "authorized without inventing a line or requiring a goal"
        )
    elif direct_ceiling is not None and lowest_visible > direct_ceiling + 1e-9:
        entry_state = "PHANTOM_FLOOR"
        entry_basis = (
            f"football direct ceiling is O{direct_ceiling:.2f}, but the lowest "
            f"visible screenshot line is O{lowest_visible:.2f}; the captured "
            "market contained no supported entry"
        )
    else:
        entry_state = "UNSUPPORTED_MARKET"
        entry_basis = (
            "the visible market contains no line/price clearing direct or "
            "conditional football authority"
        )

    result = dict(selected)
    result.update(
        {
            "visible_ladder": normalized,
            "visible_ladder_evaluations": [
                {
                    "line": row.get("observed_line"),
                    "odds": row.get("observed_odds"),
                    "action": row.get("action"),
                    "reason": row.get("reason"),
                    "line_relation": row.get("line_relation"),
                    "direct_act_ceiling": row.get("direct_act_ceiling"),
                    "intermediate_burden_profile": row.get("intermediate_burden_profile"),
                }
                for row in evaluations
            ],
            "selected_visible_line": selected.get("observed_line"),
            "selected_visible_odds": selected.get("observed_odds"),
            "supported_visible_line_found": supported_visible,
            "visible_ladder_selection_basis": selection_basis,
            "entry_feasibility_state": entry_state,
            "entry_feasibility_basis": entry_basis,
            "pass_had_lower_supported_visible_line": bool(
                selected.get("action") == "PASS"
                and direct_ceiling is not None
                and any(item["line"] <= direct_ceiling + 1e-9 for item in normalized)
            ),
            "external_price_searches": 0,
            "inferred_prices": 0,
        }
    )
    return result


def run_decision(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "decision")

    model = _active_model(payload)

    raw_match = _required(payload, "match")
    scope = scope_profile(raw_match, payload.get("context"))
    if not scope["production_allowed"]:
        raise ContractError("PRODUCTION SCOPE BLOCKED — " + scope["status"])
    a = parse_assessment(raw_match, require_c_completion=(model == "c"))
    evidence_profile = _g4_research_profile(raw_match, a, model=model)
    if evidence_profile.get("g4_evidence_gaps"):
        raise ContractError("G4 RESEARCH REQUIRED — " + ", ".join(evidence_profile["g4_evidence_gaps"]))
    compiled_burden = certified_supported_burden(a, model)
    compiled_basis = certified_supported_burden_basis(a, model)

    ctx_obj = _required(payload, "context")
    if not isinstance(ctx_obj, dict):
        raise ContractError("context must be an object")
    upgrade_gate = _certificate_upgrade_gate(
        ctx_obj, compiled_burden, model=model
    )

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

    declared_board_state, declared_board_state_basis, declared_state_source = (
        _declared_board_state(
            raw_match,
            fallback=ctx_obj,
            allow_fallback_without_basis=True,
        )
    )
    board_state = (
        compile_c_board_state(a) if model == "c" else declared_board_state
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
    book_order_status = "NOT_APPLICABLE"
    if decision.action == Action.WAIT:
        # Retired-model compatibility only. Active Football C converts
        # price-only reachable targets into BOOK before this point.
        wait_target_line, wait_min_odds = wait_accounting_target(a, ctx, model)
        accounting_status = "NONE"
        wait_resolution_default = "UNRESOLVED"
    elif decision.action == Action.BET:
        accounting_line = ctx.quote.line
        accounting_odds = ctx.quote.odds
        accounting_status = "DIRECT_BET" if model == "c" else "SHADOW_BET"
        wait_resolution_default = "NOT_APPLICABLE"
    elif decision.action == Action.BOOK:
        # BOOK authorizes a target order only. It creates no model exposure
        # until an actual fill is independently confirmed in reconciliation.
        accounting_status = "NONE"
        wait_resolution_default = "NOT_APPLICABLE"
        book_order_status = "PENDING_UNFILLED"
    else:
        accounting_status = "NONE"
        wait_resolution_default = "NOT_APPLICABLE"

    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "stage": "decision_result",
        "model": model,
        "match_id": a.match_id,
        "rank_state_internal": board_state.name,
        "rank_state_display": _display_board_state(board_state),
        "declared_board_state": declared_board_state.name,
        "declared_board_state_basis": declared_board_state_basis,
        "declared_board_state_source": declared_state_source,
        "board_state_mismatch": board_state != declared_board_state,
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
        "book_target_line": decision.book_target_line,
        "book_min_odds": decision.book_min_odds,
        "book_target_state": (
            "BOOK_TARGET_AVAILABLE" if decision.book_target_available else "NO_BOOK_TARGET"
        ),
        "current_price_clears_book_target": decision.current_price_clears_book_target,
        "book_order_status": book_order_status,
        "book_order_is_exposure": False,
        "g3_book_extension_profile": (
            c_g3_book_extension_profile(a) if model == "c" else None
        ),
        "market_line_funded": market_line_funded(a, ctx.quote.line, model),
        "execution_strength": (
            c_execution_strength(a) if model == "c" else "RETIRED_SHADOW"
        ),
        "endpoint_control_pressure": (
            c_endpoint_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "g3_endpoint_control_pressure": (
            c_g3_endpoint_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "upper_tail_control_pressure": (
            c_upper_tail_control_pressure(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "direct_act_ceiling": (
            c_direct_act_ceiling(a) if model == "c" else None
        ),
        "goal3_mechanism_class": (
            c_goal3_mechanism_class(a) if model == "c" else "NOT_APPLICABLE"
        ),
        "intermediate_burden_profile": (
            c_intermediate_burden_profile(a) if model == "c" else None
        ),
        **prospective_goal_funding(a, model),
        **upgrade_gate,
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
            frozen, "c_action", {"C_BET", "C_BOOK", "C_WAIT", "C_PASS", "NONE"}
        ),
        "quote_line": _nullable_number(frozen, "quote_line"),
        "quote_odds": _nullable_number(frozen, "quote_odds"),
        "book_target_line": (
            _nullable_number(frozen, "book_target_line")
            if "book_target_line" in frozen else None
        ),
        "book_min_odds": (
            _nullable_number(frozen, "book_min_odds")
            if "book_min_odds" in frozen else None
        ),
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
            "BOOK_USER_CONFIRMED",
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
    book_target_line = frozen_out["book_target_line"]
    book_min_odds = frozen_out["book_min_odds"]

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
    elif c_action == "C_BOOK":
        if book_target_line is None or book_min_odds is None:
            raise ContractError(
                "C-BOOK audit requires frozen book_target_line and book_min_odds"
            )
        if official_exposure_basis not in {"NONE", "BOOK_USER_CONFIRMED"}:
            raise ContractError(
                "C-BOOK requires NONE or BOOK_USER_CONFIRMED exposure basis"
            )
        if wait_resolution != "NOT_APPLICABLE":
            raise ContractError("C-BOOK requires wait_resolution=NOT_APPLICABLE")
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

    if official_exposure_basis == "BOOK_USER_CONFIRMED":
        if c_action != "C_BOOK":
            raise ContractError("BOOK_USER_CONFIRMED requires c_action=C-BOOK")
        if not official_exposure:
            raise ContractError("BOOK_USER_CONFIRMED requires official_c_exposure=true")
        if not user_executed:
            raise ContractError("BOOK_USER_CONFIRMED requires user_executed=true")
        if official_exposure_line != book_target_line:
            raise ContractError(
                "BOOK_USER_CONFIRMED exposure line must equal frozen BOOK target"
            )
        if (
            official_exposure_odds is None
            or book_min_odds is None
            or official_exposure_odds + 1e-9 < book_min_odds
        ):
            raise ContractError(
                "BOOK_USER_CONFIRMED exposure odds must meet frozen BOOK minimum"
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
