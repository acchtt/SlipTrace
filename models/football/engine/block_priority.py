"""Deterministic Football C kickoff-block selection priority.

BLOCK_PRIORITY_V1 answers one question only: which fully researched prematch
fixture has the strongest goals opportunity inside the requested block?

It deliberately does not decide prices or change Football C G3/G4/G5/G6
certificates.  Price execution remains owned by the existing XI runtime.

The comparator uses only frozen prematch football evidence.  G3 mechanism class
is a late tiebreaker so a carrier certificate cannot short-circuit materially
stronger activation, leakage, continuation or upper-tail evidence.
"""
from __future__ import annotations

from typing import Any, Iterable

POLICY = "BLOCK_PRIORITY_V1"
ACTIVATION_CONTRACT = "ASSESSMENT_DEPTH_V2"

_GRADE = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
_IGNITION = {"UNAVAILABLE": -1, "LOW": 0, "MEDIUM": 1, "HIGH": 2}
_IGNITION_FIELDS = (
    "current_attack_structure",
    "early_chance_creation",
    "early_concession_opening",
    "game_state_force",
    "weaker_side_state_change",
)
_COMPETITION_STRUCTURE_KINDS = {
    "LEAGUE_REGULAR",
    "GROUP_STAGE",
    "KNOCKOUT_FIRST_LEG",
    "KNOCKOUT_SECOND_LEG",
    "SINGLE_ELIMINATION",
    "FINAL",
    "OTHER_VERIFIED",
}
_COMPETITION_STRUCTURE_SOURCE_TIERS = {
    "OFFICIAL_COMPETITION",
    "PRIMARY_ORGANIZER",
}
_ROUTE = {"NONE": 0, "WEAK": 0, "USABLE": 1, "STRONG": 2}
_BOARD = {"PASS": 0, "WATCH": 1, "FOCUS": 2}
_PRESSURE = {"HIGH": 0, "MODERATE": 1, "NONE": 2}
_EXECUTION = {"FRAGILE": 0, "CONDITIONAL": 1, "ROBUST": 2}
_TAIL = {
    "REJECTED": 0,
    "UNAVAILABLE": 0,
    "MIXED": 1,
    "NEAR_FUNDED": 2,
    "FUNDED": 3,
}
_MECHANISM = {
    "NONE": 0,
    "DISTRIBUTED": 1,
    "TWO_ROUTE": 1,
    "LEAKAGE": 2,
    "CARRIER": 4,
}
_FORBIDDEN_PREMATCH_FIELDS = frozenset({
    "final_score",
    "ft_goals",
    "live_score",
    "match_minute",
    "first_goal_minute",
    "settlement",
    "pnl",
    "result_outcome",
    "eventual_result",
    "odds",
    "price",
    "quote",
    "bookmaker_total",
    "market_line",
    "market_odds",
})


class BlockPriorityError(ValueError):
    pass


def _text(value: Any) -> str:
    return str(value or "").strip().upper().replace("-", "_").replace(" ", "_")


def _grade(row: dict[str, Any], field: str) -> int:
    return _GRADE.get(_text(row.get(field)), -1)


def _route(row: dict[str, Any], field: str) -> int:
    return _ROUTE.get(_text(row.get(field)), -1)


def _scaled_rate(value: Any) -> int:
    if value is None:
        return -1
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return -1
    return round(float(value) * 10000)


def _scaled_number(value: Any, *, factor: int = 100) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return -1
    return round(float(value) * factor)


def _validate_prematch_only(row: dict[str, Any], *, label: str) -> None:
    present = sorted(
        field for field in _FORBIDDEN_PREMATCH_FIELDS
        if field in row and row.get(field) is not None
    )
    if present:
        raise BlockPriorityError(
            f"{label}: BLOCK_PRIORITY_V1 forbids outcome/price fields: "
            + ", ".join(present)
        )


def activation_profile(raw: dict[str, Any]) -> dict[str, Any]:
    """Validate and calibrate the source-backed block-only activation assessment.

    Declared HIGH is never trusted from full-match score history alone. It needs
    structured ignition evidence showing that the current matchup can actually
    open from 0-0. Historical V2 rows without that structure remain readable
    but their HIGH grade is conservatively capped to MEDIUM.
    """

    declared_quality = _text(raw.get("activation_quality"))
    if declared_quality not in _GRADE:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: activation_quality must be LOW/MEDIUM/HIGH"
        )
    basis = raw.get("activation_basis")
    if not isinstance(basis, str) or len(basis.strip()) < 24:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: activation_basis must be substantive"
        )
    refs = raw.get("activation_evidence_refs")
    normalized = (
        [ref.strip() for ref in refs if isinstance(ref, str) and ref.strip()]
        if isinstance(refs, list) else []
    )
    if len(set(normalized)) < 2:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: activation_evidence_refs requires two sources"
        )

    ignition = raw.get("activation_ignition")
    ignition_scores: dict[str, int] = {}
    ignition_basis = None
    ignition_refs: list[str] = []
    if isinstance(ignition, dict):
        for field in _IGNITION_FIELDS:
            value = _text(ignition.get(field))
            if value not in _IGNITION:
                raise BlockPriorityError(
                    f"{raw.get('match_id')}: activation_ignition.{field} must be "
                    "LOW/MEDIUM/HIGH/UNAVAILABLE"
                )
            ignition_scores[field] = _IGNITION[value]
        ignition_basis = ignition.get("basis")
        if not isinstance(ignition_basis, str) or len(ignition_basis.strip()) < 24:
            raise BlockPriorityError(
                f"{raw.get('match_id')}: activation_ignition.basis must be substantive"
            )
        raw_refs = ignition.get("evidence_refs")
        ignition_refs = (
            [ref.strip() for ref in raw_refs if isinstance(ref, str) and ref.strip()]
            if isinstance(raw_refs, list) else []
        )
        if len(set(ignition_refs)) < 2:
            raise BlockPriorityError(
                f"{raw.get('match_id')}: activation_ignition.evidence_refs requires "
                "two sources"
            )
    elif ignition is not None:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: activation_ignition must be an object"
        )

    effective_quality = declared_quality
    calibration = "DECLARED_GRADE_ACCEPTED"
    if declared_quality == "HIGH":
        high_count = sum(value == _IGNITION["HIGH"] for value in ignition_scores.values())
        early_high = any(
            ignition_scores.get(field) == _IGNITION["HIGH"]
            for field in ("early_chance_creation", "early_concession_opening")
        )
        current_structure_ok = (
            ignition_scores.get("current_attack_structure", -1)
            >= _IGNITION["MEDIUM"]
        )
        if not ignition_scores:
            effective_quality = "MEDIUM"
            calibration = "HIGH_CAPPED_MISSING_STRUCTURED_IGNITION"
        elif high_count < 2 or not early_high or not current_structure_ok:
            effective_quality = "MEDIUM"
            calibration = "HIGH_CAPPED_INSUFFICIENT_IGNITION"

    return {
        "activation_quality": declared_quality,
        "effective_activation_quality": effective_quality,
        "activation_score": _GRADE[effective_quality],
        "activation_basis": basis.strip(),
        "activation_evidence_refs": list(dict.fromkeys(normalized)),
        "activation_ignition": ignition_scores,
        "activation_ignition_basis": (
            ignition_basis.strip() if isinstance(ignition_basis, str) else None
        ),
        "activation_ignition_evidence_refs": list(dict.fromkeys(ignition_refs)),
        "activation_calibration": calibration,
    }


def tournament_structure_profile(raw: dict[str, Any]) -> dict[str, Any]:
    """Fail closed on unsupported or internally inconsistent tournament state."""

    required = raw.get("tournament_incentive_required") is True
    if not required:
        return {
            "required": False,
            "verified": True,
            "structure_kind": "NOT_APPLICABLE",
            "source_tier": "NOT_APPLICABLE",
        }

    kind = _text(raw.get("competition_structure_kind"))
    if kind not in _COMPETITION_STRUCTURE_KINDS:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: competition_structure_kind must be one of "
            + ", ".join(sorted(_COMPETITION_STRUCTURE_KINDS))
        )
    basis = raw.get("competition_structure_basis")
    if not isinstance(basis, str) or len(basis.strip()) < 24:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: competition_structure_basis must be substantive"
        )
    source_tier = _text(raw.get("competition_structure_source_tier"))
    if source_tier not in _COMPETITION_STRUCTURE_SOURCE_TIERS:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: competition structure requires an official "
            "competition or primary-organizer source"
        )
    refs = raw.get("competition_structure_evidence_refs")
    normalized = (
        [ref.strip() for ref in refs if isinstance(ref, str) and ref.strip()]
        if isinstance(refs, list) else []
    )
    if len(set(normalized)) < 1:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: competition_structure_evidence_refs requires "
            "at least one official/primary source"
        )

    stage = _text(raw.get("competition_stage"))
    aggregate = _text(raw.get("aggregate_state"))
    knockout_tokens = (
        "QUARTER", "SEMI", "FINAL", "PLAYOFF", "KNOCKOUT", "ROUND_OF", "LAST_"
    )
    if any(token in stage for token in knockout_tokens) and kind in {
        "LEAGUE_REGULAR", "GROUP_STAGE"
    }:
        raise BlockPriorityError(
            f"{raw.get('match_id')}: knockout competition_stage conflicts with "
            f"competition_structure_kind={kind}"
        )
    if kind in {"KNOCKOUT_FIRST_LEG", "KNOCKOUT_SECOND_LEG"}:
        if "NO_AGGREGATE" in aggregate or "SINGLE_MATCH_NO_AGGREGATE" in aggregate:
            raise BlockPriorityError(
                f"{raw.get('match_id')}: two-leg knockout cannot use no-aggregate state"
            )
    if kind in {"LEAGUE_REGULAR", "GROUP_STAGE"} and (
        "FIRST_LEG" in aggregate or "SECOND_LEG" in aggregate
    ):
        raise BlockPriorityError(
            f"{raw.get('match_id')}: regular/group stage conflicts with leg aggregate state"
        )

    return {
        "required": True,
        "verified": True,
        "structure_kind": kind,
        "source_tier": source_tier,
        "evidence_refs": list(dict.fromkeys(normalized)),
        "basis": basis.strip(),
    }


def _hard_viability(raw: dict[str, Any], compiled: dict[str, Any]) -> tuple[int, int]:
    """First gate: real football viability and funded G3 accessibility.

    HIGH leakage by itself cannot rescue LOW chance quality, a broken scoring
    route or material suppression.  This is a block-selection gate only and
    creates no certificate.
    """

    board = _BOARD.get(_text(compiled.get("board_state")), 0)
    goal3 = int(compiled.get("goal3_funded") is True)
    route_ok = max(_route(raw, "home_route"), _route(raw, "away_route")) >= 1
    chance_ok = _grade(raw, "chance_quality") >= _GRADE["MEDIUM"]
    reliability_ok = _grade(raw, "route_reliability") >= _GRADE["MEDIUM"]
    hard_failure = bool(raw.get("material_suppression")) or bool(
        raw.get("failure_attacks_route")
    )
    structural = route_ok and chance_ok and reliability_ok and not hard_failure

    if board <= 0:
        tier = 0
    elif not structural:
        tier = 1
    elif goal3 and board == _BOARD["FOCUS"]:
        tier = 3
    else:
        tier = 2
    return tier, goal3


def _tail_key(raw: dict[str, Any], compiled: dict[str, Any]) -> tuple[int, int, int, int]:
    goal4 = int(compiled.get("goal4_funded") is True)
    tail_state = _TAIL.get(_text(compiled.get("credible_tail_state")), 0)
    independent = int(bool(compiled.get(
        "independent_upper_tail", raw.get("independent_upper_tail")
    )))
    transfer = _grade(
        {"x": compiled.get(
            "upper_tail_transferability", raw.get("upper_tail_transferability")
        )},
        "x",
    )
    return goal4, tail_state, independent, transfer


def _endpoint_key(raw: dict[str, Any], compiled: dict[str, Any]) -> tuple[int, int, int]:
    pressure = _PRESSURE.get(
        _text(
            compiled.get("g3_endpoint_control_pressure")
            or compiled.get("endpoint_control_pressure")
        ),
        0,
    )
    stall = _grade(raw, "burden_stall_risk")
    # Lower stall is better: LOW=2, MEDIUM=1, HIGH=0.
    stall_resistance = 2 - stall if stall >= 0 else -1
    trap = raw.get("goal_signal_low_draw_trap_rate")
    trap_resistance = (
        10000 - _scaled_rate(trap) if trap is not None else -1
    )
    return pressure, stall_resistance, trap_resistance


def _certificate_depth(compiled: dict[str, Any]) -> int:
    for goal in (6, 5, 4, 3):
        if compiled.get(f"goal{goal}_funded") is True:
            return goal
    return 0


def _mechanism_tiebreak(raw: dict[str, Any], compiled: dict[str, Any]) -> int:
    if bool(compiled.get(
        "g3_current_structure_verified", raw.get("g3_current_structure_verified")
    )):
        return 5
    return _MECHANISM.get(_text(compiled.get("goal3_mechanism_class")), 0)


def block_priority_key(
    raw: dict[str, Any],
    compiled: dict[str, Any],
) -> tuple[int, ...]:
    """Return the frozen BLOCK_PRIORITY_V1 lexicographic key.

    Ordering intentionally follows the active repair contract:
    viability/G3 -> activation -> leakage -> continuation -> upper tail ->
    endpoint resistance -> chance -> completion -> frozen goal signal ->
    clearability -> robustness/depth -> mechanism tiebreak.
    """

    _validate_prematch_only(raw, label=str(raw.get("match_id") or "raw"))
    _validate_prematch_only(compiled, label=str(compiled.get("match_id") or "compiled"))
    activation = activation_profile(raw)
    tournament_structure_profile(raw)
    viability = _hard_viability(raw, compiled)
    leakage = _grade(raw, "opponent_leakage")
    continuation = _grade(raw, "continuation_quality")
    tail = _tail_key(raw, compiled)
    endpoint = _endpoint_key(raw, compiled)
    chance = _grade(raw, "chance_quality")
    completion = _grade(raw, "burden_completion_quality")
    goal_signal = (
        _scaled_rate(raw.get("goal_signal_mean_over_three_rate")),
        _scaled_rate(raw.get("goal_signal_mean_over_two_rate")),
        _scaled_number(raw.get("goal_signal_priority_score"), factor=100),
    )
    clearability = _scaled_number(compiled.get("follow_clearability_score"), factor=10)
    robustness = _EXECUTION.get(_text(compiled.get("execution_strength")), 0)
    depth = _certificate_depth(compiled)
    mechanism = _mechanism_tiebreak(raw, compiled)

    return (
        *viability,
        int(activation["activation_score"]),
        leakage,
        continuation,
        *tail,
        *endpoint,
        chance,
        completion,
        *goal_signal,
        clearability,
        robustness,
        depth,
        mechanism,
    )


def priority_diagnostics(
    raw: dict[str, Any],
    compiled: dict[str, Any],
) -> dict[str, Any]:
    activation = activation_profile(raw)
    tournament = tournament_structure_profile(raw)
    viability = _hard_viability(raw, compiled)
    return {
        "policy": POLICY,
        "match_id": str(raw.get("match_id") or compiled.get("match_id") or ""),
        "hard_viability_tier": viability[0],
        "goal3_accessible": bool(viability[1]),
        "activation_quality": activation["activation_quality"],
        "effective_activation_quality": activation["effective_activation_quality"],
        "activation_calibration": activation["activation_calibration"],
        "competition_structure_kind": tournament["structure_kind"],
        "competition_structure_source_tier": tournament["source_tier"],
        "opponent_leakage": _text(raw.get("opponent_leakage")),
        "continuation_quality": _text(raw.get("continuation_quality")),
        "credible_tail_state": _text(compiled.get("credible_tail_state")),
        "goal4_funded": compiled.get("goal4_funded") is True,
        "endpoint_control_pressure": _text(
            compiled.get("g3_endpoint_control_pressure")
            or compiled.get("endpoint_control_pressure")
        ),
        "chance_quality": _text(raw.get("chance_quality")),
        "burden_completion_quality": _text(raw.get("burden_completion_quality")),
        "goal_signal_mean_over_three_rate": raw.get("goal_signal_mean_over_three_rate"),
        "goal_signal_mean_over_two_rate": raw.get("goal_signal_mean_over_two_rate"),
        "follow_clearability_score": compiled.get("follow_clearability_score"),
        "execution_strength": _text(compiled.get("execution_strength")),
        "certificate_depth": _certificate_depth(compiled),
        "goal3_mechanism_class": _text(compiled.get("goal3_mechanism_class")),
        "mechanism_is_late_tiebreaker": True,
        "market_independent": True,
        "outcome_fields_read": False,
    }


def rank_block(
    raw_rows: Iterable[dict[str, Any]],
    compiled_rows: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Rank one complete block deterministically.

    Stable match_id ordering is used only when every football component ties.
    """

    raw_list = [row for row in raw_rows if isinstance(row, dict)]
    compiled_by_id = {
        str(row.get("match_id")): row
        for row in compiled_rows if isinstance(row, dict)
    }
    pairs: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for raw in raw_list:
        mid = str(raw.get("match_id") or "")
        compiled = compiled_by_id.get(mid)
        if not mid or not isinstance(compiled, dict):
            raise BlockPriorityError(f"{mid or '<missing>'}: compiled Football C row required")
        pairs.append((raw, compiled))

    # Stable alphabetical order is the final deterministic tiebreak.
    pairs.sort(key=lambda pair: str(pair[0].get("match_id")))
    pairs.sort(
        key=lambda pair: block_priority_key(pair[0], pair[1]),
        reverse=True,
    )

    ranked: list[dict[str, Any]] = []
    for rank, (raw, compiled) in enumerate(pairs, start=1):
        diagnostics = priority_diagnostics(raw, compiled)
        ranked.append({
            "block_priority_rank": rank,
            "match_id": str(raw.get("match_id")),
            "block_priority_key": list(block_priority_key(raw, compiled)),
            "block_priority_diagnostics": diagnostics,
        })
    return ranked
