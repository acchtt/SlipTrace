from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Iterable


class Grade(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class RouteStrength(IntEnum):
    WEAK = 0
    USABLE = 1
    STRONG = 2


class CarrierStrength(IntEnum):
    NONE = 0
    USABLE = 1
    STRONG = 2


class CompletionMode(Enum):
    NONE = "NONE"
    TWO_SIDED = "TWO_SIDED"
    CARRIER_LED = "CARRIER_LED"
    FORCED_CHAOS = "FORCED_CHAOS"
    MIXED = "MIXED"


class BoardState(IntEnum):
    PASS = 0
    WATCH = 1
    FOCUS = 2


class FollowLane(Enum):
    STOP = "STOP"
    FOCUS_UNFOLLOWED = "FOCUS_UNFOLLOWED"
    RESERVE = "RESERVE"
    FOLLOW = "FOLLOW"


class Step2Authorization(Enum):
    ROUTINE_FOLLOW = "ROUTINE_FOLLOW"
    RESERVE_ACTIVATED = "RESERVE_ACTIVATED"
    USER_EXCEPTION = "USER_EXCEPTION"


class ThesisState(IntEnum):
    BROKEN = 0
    DEGRADED = 1
    PRESERVED = 2


class XiStatus(Enum):
    CONFIRMED = "CONFIRMED"
    RELIABLE = "RELIABLE"
    UNAVAILABLE = "UNAVAILABLE"


class PostXiResearchStatus(Enum):
    FOUND = "FOUND"
    LIMITED = "LIMITED"
    UNAVAILABLE_ATTEMPTED = "UNAVAILABLE_ATTEMPTED"


class H2HReviewStatus(Enum):
    REVIEWED_USABLE = "REVIEWED_USABLE"
    REVIEWED_LIMITED = "REVIEWED_LIMITED"
    NOT_USABLE = "NOT_USABLE"
    UNAVAILABLE = "UNAVAILABLE"


class SelectionFloor(Enum):
    FAIL = "FAIL"
    BORDERLINE = "BORDERLINE"
    CLEAR = "CLEAR"


class Action(Enum):
    PASS = "PASS"
    WAIT = "WAIT"
    BET = "BET"
    BOOK = "BOOK"


class Settlement(Enum):
    LOSS = "LOSS"
    HALF_LOSS = "HALF LOSS"
    PUSH = "PUSH"
    HALF_WIN = "HALF WIN"
    WIN = "WIN"


@dataclass(frozen=True)
class MatchAssessment:
    """Structured football evidence produced by the research/LLM layer.

    The code deliberately does not decide whether a route is STRONG or whether
    H2H suppression is transferable. Those remain research judgments. Once
    assigned, the deterministic engine applies ranking/execution rules
    consistently.
    """

    match_id: str
    home_route: RouteStrength
    away_route: RouteStrength
    carrier: CarrierStrength

    # Explicit qualitative dimensions from the Football C/C2 ranking contract.
    route_reliability: Grade
    independent_route_quality: Grade
    chance_quality: Grade
    failure_resistance: Grade
    xi_robustness: Grade
    evidence_confidence: Grade
    burden_protection: Grade

    # Common Step-1 research basis. This is shared across C/C2 and must
    # describe the frozen football evidence epoch used for the common grades.
    common_evidence_basis: str

    # Required failure/H2H declarations. Empty or omitted evidence must never
    # become an implicit favorable state in the deterministic validator.
    main_failure: str
    h2h_state: str
    h2h_effect: str
    h2h_transferability: str
    h2h_current_corroboration: str
    h2h_material_effect: bool
    h2h_basis: str

    # Legacy/research-layer declaration retained only for audit comparison.
    # Production burden is compiled deterministically from goal certificates.
    supported_line: float
    supported_line_basis: str

    carrier_self_fund: bool
    carrier_self_fund_basis: str
    independent_upper_tail: bool
    independent_upper_tail_basis: str
    failure_attacks_route: bool
    failure_attacks_route_basis: str
    material_suppression: bool
    material_suppression_basis: str

    # Transferability of the evidence used to justify goal-four-plus tails.
    # This is distinct from evidence_confidence: evidence may be confidently
    # observed but still fail to transfer from weak-opposition, cup, red-card
    # or other distorted contexts into the current matchup.
    upper_tail_transferability: Grade | None = None
    upper_tail_transferability_basis: str | None = None

    # Direction of the most comparable available context for G4+.
    # Same-competition / closely comparable senior evidence takes precedence
    # over less-comparable domestic/cup scoring when it is available.
    upper_tail_comparable_context_signal: str | None = None
    upper_tail_comparable_context_basis: str | None = None

    # Frozen V4 Step-0 goal signal. These are common evidence, never market
    # evidence. They are optional for historical compatibility, but the
    # distributed goal-three certificate cannot activate without them.
    goal_signal_priority_score: float | None = None
    goal_signal_mean_over_two_rate: float | None = None
    goal_signal_mean_over_three_rate: float | None = None
    goal_signal_low_draw_trap_rate: float | None = None

    # Football C-owned burden-completion diagnostics. These are deliberately
    # optional in the shared assessment object so C2 does not need to carry
    # C policy labels merely to satisfy a generic parser. The C parser and all
    # C-only deterministic functions fail closed when any field is absent.
    completion_mode: CompletionMode | None = None
    burden_completion_quality: Grade | None = None
    continuation_quality: Grade | None = None
    opponent_leakage: Grade | None = None
    burden_stall_risk: Grade | None = None

    # C2-owned matchup leakage. Never copy C's completion/stall diagnostics
    # into C2. Missing independent leakage evidence leaves prior C2 unchanged.
    c2_opponent_leakage: Grade | None = None
    c2_opponent_leakage_basis: str | None = None

    # Common frozen tournament context. These are research inputs, never
    # bookmaker-derived. Unresolved tournament state remains neutral and must
    # be rechecked by Step 2 before any action is authorized.
    tournament_incentive_required: bool = False
    tournament_incentive_resolution: str = "NOT_APPLICABLE"
    home_incentive: str = "NOT_APPLICABLE"
    away_incentive: str = "NOT_APPLICABLE"
    tiebreak_margin_relevance: str = "NOT_APPLICABLE"
    incentive_effect: str = "NOT_APPLICABLE"
    simultaneous_results_status: str = "NOT_APPLICABLE"

    def __post_init__(self) -> None:
        if not self.common_evidence_basis.strip():
            raise ValueError("common_evidence_basis must be non-empty")
        if not self.main_failure.strip():
            raise ValueError("main_failure must be non-empty")
        if not self.h2h_state.strip():
            raise ValueError("h2h_state must be non-empty")
        for name, value in (
            ("h2h_basis", self.h2h_basis),
            ("carrier_self_fund_basis", self.carrier_self_fund_basis),
            ("independent_upper_tail_basis", self.independent_upper_tail_basis),
            ("failure_attacks_route_basis", self.failure_attacks_route_basis),
            ("material_suppression_basis", self.material_suppression_basis),
        ):
            if not value.strip():
                raise ValueError(f"{name} must be non-empty")
        if not self.supported_line_basis.strip():
            raise ValueError("supported_line_basis must be non-empty")
        if self.supported_line < 0:
            raise ValueError("supported_line must be non-negative")
        _validate_quarter_line(self.supported_line)
        for name, value, low, high in (
            ("goal_signal_priority_score", self.goal_signal_priority_score, 0.0, 100.0),
            ("goal_signal_mean_over_two_rate", self.goal_signal_mean_over_two_rate, 0.0, 1.0),
            ("goal_signal_mean_over_three_rate", self.goal_signal_mean_over_three_rate, 0.0, 1.0),
            ("goal_signal_low_draw_trap_rate", self.goal_signal_low_draw_trap_rate, 0.0, 1.0),
        ):
            if value is not None and not low <= value <= high:
                raise ValueError(f"{name} outside {low}..{high}")
        if self.upper_tail_transferability is not None and not (
            self.upper_tail_transferability_basis
            and self.upper_tail_transferability_basis.strip()
        ):
            raise ValueError(
                "upper_tail_transferability requires a non-empty basis"
            )
        if self.independent_upper_tail and self.upper_tail_transferability is None:
            raise ValueError(
                "independent_upper_tail requires explicit upper_tail_transferability"
            )
        if self.upper_tail_comparable_context_signal is not None:
            if self.upper_tail_comparable_context_signal not in {
                "SUPPORTIVE", "MIXED", "SUPPRESSIVE", "UNAVAILABLE"
            }:
                raise ValueError("invalid upper_tail_comparable_context_signal")
            if not (
                self.upper_tail_comparable_context_basis
                and self.upper_tail_comparable_context_basis.strip()
            ):
                raise ValueError(
                    "upper_tail_comparable_context_signal requires a non-empty basis"
                )
        elif self.upper_tail_comparable_context_basis is not None:
            raise ValueError(
                "upper_tail_comparable_context_basis requires a signal"
            )
        if self.c2_opponent_leakage is not None and not (
            self.c2_opponent_leakage_basis
            and self.c2_opponent_leakage_basis.strip()
        ):
            raise ValueError("C2 leakage grade requires independent non-empty basis")

        allowed_resolution = {"NOT_APPLICABLE", "VERIFIED", "INCENTIVE_RECHECK_REQUIRED"}
        if self.tournament_incentive_resolution not in allowed_resolution:
            raise ValueError("invalid tournament_incentive_resolution")
        allowed_incentives = {
            "NOT_APPLICABLE", "MUST_WIN", "WIN_PREFERRED", "DRAW_ACCEPTABLE",
            "MARGIN_NEEDED", "PROTECT_AGGREGATE", "PROTECT_RESULT",
            "DEAD_RUBBER", "PLACEMENT_ONLY", "UNKNOWN",
        }
        if self.home_incentive not in allowed_incentives:
            raise ValueError("invalid home_incentive")
        if self.away_incentive not in allowed_incentives:
            raise ValueError("invalid away_incentive")
        if self.tiebreak_margin_relevance not in {"NOT_APPLICABLE", "YES", "NO", "UNKNOWN"}:
            raise ValueError("invalid tiebreak_margin_relevance")
        if self.incentive_effect not in {
            "NOT_APPLICABLE", "EXPANSIVE", "NEUTRAL", "SUPPRESSIVE", "MIXED", "UNKNOWN"
        }:
            raise ValueError("invalid incentive_effect")
        if self.simultaneous_results_status not in {
            "NOT_APPLICABLE", "VERIFIED", "LIMITED", "UNKNOWN"
        }:
            raise ValueError("invalid simultaneous_results_status")


@dataclass(frozen=True)
class Quote:
    line: float
    odds: float

    def __post_init__(self) -> None:
        _validate_quarter_line(self.line)
        if self.odds <= 1.0:
            raise ValueError("decimal odds must be > 1.0")


@dataclass(frozen=True)
class ModelQuoteContext:
    """Pure C/C2 price-policy context with no execution/publication authority.

    This is the canonical model-evaluation surface used for both screenshot
    comparison and strict executable decisions. Whether an action may actually
    be published or exposed is handled separately by the execution contract.
    """

    board_state: BoardState
    thesis_state: ThesisState
    quote: Quote
    top_ranked_focus: bool
    primary_mechanism_intact: bool
    wait_reachable: bool
    wait_requires_negative_info: bool
    material_veto: bool


@dataclass(frozen=True)
class DecisionContext:
    """Strict execution context.

    Extra fields below authorize execution/persistence. Model ACT/WAIT/PASS
    policy itself lives in ModelQuoteContext and is shared with non-executable
    observed-quote assessment.
    """

    board_state: BoardState
    official_follow_lane: FollowLane
    step2_authorization: Step2Authorization
    thesis_state: ThesisState
    thesis_state_basis: str
    quote: Quote

    xi_status: XiStatus
    post_xi_research_status: PostXiResearchStatus
    h2h_review_status: H2HReviewStatus
    h2h_rechecked: bool
    h2h_basis: str

    top_ranked_focus: bool
    primary_mechanism_intact: bool
    primary_mechanism_basis: str
    wait_reachable: bool
    wait_reachability_basis: str
    wait_requires_negative_info: bool
    wait_negative_info_basis: str
    material_veto: bool
    material_veto_basis: str


@dataclass(frozen=True)
class Decision:
    action: Action
    reason: str
    bridge_used: bool = False
    book_target_line: float | None = None
    book_min_odds: float | None = None
    book_target_available: bool = False
    current_price_clears_book_target: bool = False


def _validate_quarter_line(line: float) -> None:
    quarter = round(line * 4)
    if abs(line * 4 - quarter) > 1e-9:
        raise ValueError("Asian total line must use 0.25-goal increments")


def require_c_completion(
    a: MatchAssessment,
) -> tuple[CompletionMode, Grade, Grade, Grade, Grade]:
    """Return C-owned diagnostics or fail closed when a C path lacks them."""

    values = (
        a.completion_mode,
        a.burden_completion_quality,
        a.continuation_quality,
        a.opponent_leakage,
        a.burden_stall_risk,
    )
    if any(value is None for value in values):
        raise ValueError(
            "FOOTBALL C COMPLETION DIAGNOSTICS MISSING — "
            "completion_mode / burden_completion_quality / continuation_quality / "
            "opponent_leakage / burden_stall_risk are required for model=c"
        )
    return values  # type: ignore[return-value]


def tournament_incentive_profile(a: MatchAssessment) -> dict[str, int | str | bool]:
    """Compile frozen tournament context into a conservative football modifier.

    Only a VERIFIED tournament state can modify the model. EXPANSIVE can
    strengthen continuation/stall resistance by one grade when a real scoring
    route already exists. SUPPRESSIVE moves those dimensions the other way.
    MIXED/NEUTRAL never manufacture a positive route. Unresolved context is
    neutral here and remains a Step-2 blocker in the adapter.
    """

    if not a.tournament_incentive_required:
        return {
            "status": "NOT_APPLICABLE",
            "effect": "NOT_APPLICABLE",
            "tail_bias": "NEUTRAL",
            "continuation_delta": 0,
            "stall_delta": 0,
            "positive_pressure": False,
            "suppressive_pressure": False,
        }

    if a.tournament_incentive_resolution != "VERIFIED":
        return {
            "status": a.tournament_incentive_resolution,
            "effect": a.incentive_effect,
            "tail_bias": "UNRESOLVED",
            "continuation_delta": 0,
            "stall_delta": 0,
            "positive_pressure": False,
            "suppressive_pressure": False,
        }

    positive_directive = any(
        value in {"MUST_WIN", "WIN_PREFERRED", "MARGIN_NEEDED"}
        for value in (a.home_incentive, a.away_incentive)
    )
    suppressive_directive = any(
        value in {"DRAW_ACCEPTABLE", "PROTECT_AGGREGATE", "PROTECT_RESULT"}
        for value in (a.home_incentive, a.away_incentive)
    )

    if a.incentive_effect == "EXPANSIVE":
        bias = "EXPANSIVE"
        continuation_delta = 1 if positive_directive else 0
        stall_delta = -1 if positive_directive else 0
    elif a.incentive_effect == "SUPPRESSIVE":
        bias = "SUPPRESSIVE"
        continuation_delta = -1
        stall_delta = 1
    else:
        # MIXED and NEUTRAL are deliberately non-positive. A contradictory
        # combination of directives does not get laundered into an OVER boost.
        bias = a.incentive_effect if a.incentive_effect in {"MIXED", "NEUTRAL"} else "NEUTRAL"
        continuation_delta = 0
        stall_delta = 0

    return {
        "status": "VERIFIED",
        "effect": a.incentive_effect,
        "tail_bias": bias,
        "continuation_delta": continuation_delta,
        "stall_delta": stall_delta,
        "positive_pressure": bool(positive_directive and bias == "EXPANSIVE"),
        "suppressive_pressure": bool(suppressive_directive or bias == "SUPPRESSIVE"),
    }


def c_effective_incentive_grades(a: MatchAssessment) -> tuple[Grade, Grade]:
    """Return C continuation/stall grades after verified tournament context."""

    require_c_completion(a)
    profile = tournament_incentive_profile(a)
    continuation_delta = int(profile["continuation_delta"])
    stall_delta = int(profile["stall_delta"])

    # Positive tournament pressure cannot create a scoring mechanism. Require a
    # real STRONG route and at least a usable carrier before applying the boost.
    if continuation_delta > 0 and not (
        max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and not a.material_suppression
        and not a.failure_attacks_route
    ):
        continuation_delta = 0
        stall_delta = 0

    continuation = Grade(
        max(int(Grade.LOW), min(int(Grade.HIGH), int(a.continuation_quality) + continuation_delta))
    )
    stall = Grade(
        max(int(Grade.LOW), min(int(Grade.HIGH), int(a.burden_stall_risk) + stall_delta))
    )
    return continuation, stall


def tournament_incentive_rank_score(a: MatchAssessment) -> int:
    """Small common-evidence rank modifier; never outranks route/chance quality."""

    bias = tournament_incentive_profile(a)["tail_bias"]
    if bias == "EXPANSIVE":
        return 1
    if bias == "SUPPRESSIVE":
        return -1
    return 0


def goal_signal_supports_distributed_goal3(a: MatchAssessment) -> bool:
    """Require frozen Step-0 corroboration for a distributed 2+1 / 1+2 route.

    Keep the original route-score path, but also accept the V4 Step-0
    high-rate alternate path. This prevents intake from admitting a strong
    3+/4+ signal that the certificate compiler then rejects solely because the
    blended priority score is 57-59.
    """

    values = (
        a.goal_signal_priority_score,
        a.goal_signal_mean_over_two_rate,
        a.goal_signal_mean_over_three_rate,
        a.goal_signal_low_draw_trap_rate,
    )
    if any(value is None for value in values):
        return False

    route_score_path = (
        a.goal_signal_priority_score >= 60
        and a.goal_signal_mean_over_two_rate >= 0.65
        and a.goal_signal_low_draw_trap_rate <= 0.20
    )
    high_rate_path = (
        a.goal_signal_mean_over_two_rate >= 0.65
        and a.goal_signal_mean_over_three_rate >= 0.45
        and a.goal_signal_low_draw_trap_rate <= 0.20
    )
    return route_score_path or high_rate_path


def c_carrier_goal3_funded(a: MatchAssessment) -> bool:
    require_c_completion(a)
    return (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c_two_route_goal3_funded(a: MatchAssessment) -> bool:
    """Standard strong two-route goal-three certificate."""

    require_c_completion(a)
    effective_continuation, _ = c_effective_incentive_grades(a)
    return (
        a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and a.burden_completion_quality == Grade.HIGH
        and effective_continuation == Grade.HIGH
        and a.opponent_leakage >= Grade.MEDIUM
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c_distributed_goal3_funded(a: MatchAssessment) -> bool:
    """Fund goal three through a genuine two-sided 2+1 / 1+2 mechanism.

    Frozen scoreline history is corroboration, never a substitute for current
    football strength. Two merely USABLE routes with an all-MEDIUM profile no
    longer combine into a protected G3 certificate by themselves.
    """

    require_c_completion(a)
    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    strong_current_support = (
        max(a.home_route, a.away_route) == RouteStrength.STRONG
        or a.independent_route_quality == Grade.HIGH
    )
    return (
        goal_signal_supports_distributed_goal3(a)
        and a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and a.carrier >= CarrierStrength.USABLE
        and strong_current_support
        and a.burden_completion_quality >= Grade.MEDIUM
        and effective_continuation >= Grade.MEDIUM
        and effective_stall <= Grade.MEDIUM
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and a.opponent_leakage >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c_predictive_high_dimension(a: MatchAssessment) -> bool:
    """Return whether current football quality contains a genuinely HIGH dimension.

    Evidence confidence is deliberately excluded. HIGH evidence confidence means
    that the inputs are well sourced; it is not itself evidence that the scoring
    mechanism is strong enough to upgrade execution.
    """

    require_c_completion(a)
    return any(
        value == Grade.HIGH
        for value in (
            a.route_reliability,
            a.chance_quality,
            a.independent_route_quality,
            a.burden_completion_quality,
        )
    )


def c_goal3_mechanism_class(a: MatchAssessment) -> str:
    """Describe the strongest funded G3 mechanism for ranking/execution audit."""

    require_c_completion(a)
    if c_carrier_goal3_funded(a):
        return "CARRIER"
    if c_two_route_goal3_funded(a):
        return "TWO_ROUTE"
    if c_leakage_goal3_funded(a):
        return "LEAKAGE"
    if c_distributed_goal3_funded(a):
        return "DISTRIBUTED"
    return "NONE"


def c_goal3_mechanism_rank(a: MatchAssessment) -> int:
    """Rank mechanism independence without using market or outcome information."""

    return {
        "NONE": 0,
        "DISTRIBUTED": 1,
        "LEAKAGE": 2,
        "TWO_ROUTE": 3,
        "CARRIER": 4,
    }[c_goal3_mechanism_class(a)]


def c_leakage_goal3_funded(a: MatchAssessment) -> bool:
    """Fund goal three from a STRONG route plus matchup-specific HIGH leakage.

    This replaces the old O2.25-only exception. Once the frozen football facts
    genuinely certify goal three, the certificate is goal-based rather than
    line-based and therefore supports the fully-funded O2.50 burden.
    """

    require_c_completion(a)
    return (
        max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.opponent_leakage == Grade.HIGH
        and a.burden_completion_quality >= Grade.MEDIUM
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def low_burden_leakage_goal3_funded(
    a: MatchAssessment, selected_line: float | None = None
) -> bool:
    """Compatibility alias for the former O2.25-only leakage helper."""

    if selected_line is not None:
        _validate_quarter_line(selected_line)
    return c_leakage_goal3_funded(a)


def c_goal3_funded(a: MatchAssessment) -> bool:
    """Explicit C goal-three certificate."""

    return (
        c_carrier_goal3_funded(a)
        or c_two_route_goal3_funded(a)
        or c_distributed_goal3_funded(a)
        or c_leakage_goal3_funded(a)
    )


def c_effective_upper_tail_transferability(
    a: MatchAssessment,
) -> Grade | None:
    """Apply comparable-context precedence to C's G4+ transferability grade.

    Same-competition or closely comparable senior evidence overrides
    less-comparable domestic/cup scoring when it exists. This uses only frozen
    prospective evidence, never the bookmaker line or observed match outcome.
    """

    grade = a.upper_tail_transferability
    signal = a.upper_tail_comparable_context_signal
    if grade is None or signal is None:
        return None
    if signal == "SUPPRESSIVE":
        return Grade.LOW
    if signal == "MIXED":
        return min(grade, Grade.MEDIUM)
    if signal in {"SUPPORTIVE", "UNAVAILABLE"}:
        return grade
    return None


def c_upper_tail_transferable(a: MatchAssessment) -> bool:
    """Whether frozen evidence can support a C goal-four-plus certificate."""

    effective = c_effective_upper_tail_transferability(a)
    return bool(
        a.independent_upper_tail
        and effective is not None
        and effective >= Grade.MEDIUM
    )


def c_goal4_funded(a: MatchAssessment) -> bool:
    """Explicit C fourth-goal certificate; G3 alone never implies G4."""

    require_c_completion(a)
    if not c_goal3_funded(a):
        return False
    if not c_upper_tail_transferable(a):
        return False
    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    if tournament_incentive_profile(a)["tail_bias"] == "SUPPRESSIVE":
        return (
            a.carrier == CarrierStrength.STRONG
            and a.carrier_self_fund
            and a.independent_upper_tail
            and a.route_reliability == Grade.HIGH
            and a.chance_quality == Grade.HIGH
            and a.failure_resistance == Grade.HIGH
            and a.evidence_confidence == Grade.HIGH
            and effective_continuation >= Grade.MEDIUM
            and effective_stall <= Grade.MEDIUM
        )

    two_strong_routes = (
        a.home_route == RouteStrength.STRONG
        and a.away_route == RouteStrength.STRONG
        and a.independent_route_quality == Grade.HIGH
    )
    carrier_route = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and (
            a.route_reliability == Grade.HIGH
            or two_strong_routes
        )
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_completion_quality >= Grade.MEDIUM
        and effective_continuation >= Grade.MEDIUM
        and effective_stall <= Grade.MEDIUM
    )
    distributed_tail = (
        a.independent_upper_tail
        and a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.independent_route_quality == Grade.HIGH
        and a.route_reliability == Grade.HIGH
        and a.chance_quality >= Grade.MEDIUM
        and (
            two_strong_routes
            or a.failure_resistance == Grade.HIGH
        )
        and a.burden_completion_quality == Grade.HIGH
        and effective_continuation == Grade.HIGH
        and effective_stall <= Grade.MEDIUM
    )
    return (
        (carrier_route or distributed_tail)
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def clearing_goal_funded(a: MatchAssessment, selected_line: float | None = None) -> bool:
    """Compatibility wrapper using exact Asian full-win settlement semantics."""

    burden = a.supported_line if selected_line is None else selected_line
    _validate_quarter_line(burden)
    required = required_full_win_goal(burden)
    if required <= 3:
        return c_goal3_funded(a)
    if required == 4:
        return c_goal4_funded(a)
    if required == 5:
        return c_goal5_funded(a)
    if required == 6:
        return c_goal6_funded(a)
    return False


def funded_goal_certificate_depth(a: MatchAssessment, model: str) -> int:
    """Return the highest independently funded goal certificate for one model."""

    if model == "c":
        funded = (
            (6, c_goal6_funded(a)),
            (5, c_goal5_funded(a)),
            (4, c_goal4_funded(a)),
            (3, c_goal3_funded(a)),
        )
    elif model == "c2":
        funded = (
            (6, c2_goal6_funded(a)),
            (5, c2_goal5_funded(a)),
            (4, c2_goal4_funded(a)),
            (3, c2_goal3_funded(a)),
        )
    else:
        raise ValueError("model must be c or c2")

    for depth, ok in funded:
        if ok:
            return depth
    return 0


def _goal_signal_rank_key(a: MatchAssessment) -> tuple[int, int, int, int, int]:
    """Deterministic frozen Step-0 quantitative comparator.

    Missing evidence ranks below complete evidence; no league, price or final
    score information is admitted here.
    """

    values = (
        a.goal_signal_priority_score,
        a.goal_signal_mean_over_two_rate,
        a.goal_signal_mean_over_three_rate,
        a.goal_signal_low_draw_trap_rate,
    )
    complete = int(all(value is not None for value in values))
    priority = (
        round(a.goal_signal_priority_score * 100)
        if a.goal_signal_priority_score is not None
        else -1
    )
    over_two = (
        round(a.goal_signal_mean_over_two_rate * 10000)
        if a.goal_signal_mean_over_two_rate is not None
        else -1
    )
    over_three = (
        round(a.goal_signal_mean_over_three_rate * 10000)
        if a.goal_signal_mean_over_three_rate is not None
        else -1
    )
    low_draw = (
        -round(a.goal_signal_low_draw_trap_rate * 10000)
        if a.goal_signal_low_draw_trap_rate is not None
        else -10001
    )
    return complete, priority, over_two, over_three, low_draw


def _independent_scoring_structure(a: MatchAssessment) -> bool:
    """Common evidence that the certificate does not rely on one brittle path."""

    two_route = (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and a.independent_route_quality >= Grade.MEDIUM
    )
    self_funded_carrier = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
    )
    return two_route or self_funded_carrier


def c_g3_endpoint_control_pressure(a: MatchAssessment) -> str:
    """Compile pressure that directly attacks the third-goal mechanism.

    HIGH is reserved for a direct hard-control signal: HIGH effective stall,
    a material low-draw trap, or verified+corroborated suppressive H2H.
    Ordinary MEDIUM completion/continuation/stall grades and MIXED context are
    cautions, not synthetic hard vetoes, regardless of how many coexist.
    """

    require_c_completion(a)
    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    trap = a.goal_signal_low_draw_trap_rate

    hard_control = (
        effective_stall == Grade.HIGH
        or (trap is not None and trap >= 0.25)
        or (
            a.h2h_effect == "SUPPRESSIVE"
            and a.h2h_transferability == "VERIFIED"
            and a.h2h_current_corroboration == "VERIFIED"
        )
    )
    if hard_control:
        return "HIGH"

    cautions = (
        effective_stall == Grade.MEDIUM
        or a.burden_completion_quality == Grade.MEDIUM
        or effective_continuation == Grade.MEDIUM
        or a.failure_resistance == Grade.MEDIUM
        or (
            a.h2h_effect in {"SUPPRESSIVE", "MIXED"}
            and a.h2h_transferability in {"VERIFIED", "LIMITED"}
        )
        or a.upper_tail_comparable_context_signal in {"MIXED", "SUPPRESSIVE"}
    )
    return "MODERATE" if cautions else "NONE"


def c_upper_tail_control_pressure(a: MatchAssessment) -> str:
    """Compile G4+ control pressure without erasing an independent G3 floor.

    This diagnostic deliberately reuses existing frozen evidence and changes
    no numerical threshold.  A direct G3 hard control is also a tail hard
    control.  Tail-specific non-transferability or suppressive comparable
    context can block G4+ while leaving a separately funded G3 intact.
    """

    require_c_completion(a)
    g3_pressure = c_g3_endpoint_control_pressure(a)
    if g3_pressure == "HIGH":
        return "HIGH"
    if (
        a.upper_tail_comparable_context_signal == "SUPPRESSIVE"
        or (
            a.independent_upper_tail
            and c_effective_upper_tail_transferability(a) == Grade.LOW
        )
    ):
        return "HIGH"
    if (
        g3_pressure == "MODERATE"
        or a.upper_tail_comparable_context_signal in {"MIXED", "UNAVAILABLE"}
        or not a.independent_upper_tail
    ):
        return "MODERATE"
    return "NONE"


def c_endpoint_control_pressure(a: MatchAssessment) -> str:
    """Historical compatibility alias for the G3-specific pressure field."""

    return c_g3_endpoint_control_pressure(a)


def compile_c_board_state(a: MatchAssessment) -> BoardState:
    """Compile production C board state from certificates and direct vetoes.

    Researcher labels are audit metadata only.  A funded G3 is FOCUS; a
    route-destroying/material suppressive state is PASS; every other researched
    row is REVIEW_ONLY/WATCH.  This introduces no new score threshold and
    prevents both manual demotion of funded structure and manual promotion of
    a no-certificate row.
    """

    require_c_completion(a)
    if c_goal3_funded(a):
        return BoardState.FOCUS
    if a.material_suppression or a.failure_attacks_route:
        return BoardState.PASS
    return BoardState.WATCH


def c_execution_strength(a: MatchAssessment) -> str:
    """Expose execution quality separately from rank/FOLLOW workload priority."""

    return ("FRAGILE", "CONDITIONAL", "ROBUST")[certificate_robustness(a, "c")]


def c_goal3_execution_floor_authorized(a: MatchAssessment) -> bool:
    """Retain direct O2.50 authority for a genuinely funded current G3 floor.

    Certificate robustness may be FRAGILE because the upper tail is weak or
    because broader confidence is conditional. That must not erase an already
    funded third-goal burden. Hard endpoint-control evidence still vetoes the
    floor, and BOOK/unsupported tail extensions remain ROBUST-only.
    """

    require_c_completion(a)
    if not c_goal3_funded(a):
        return False

    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    distributed_only = (
        c_distributed_goal3_funded(a)
        and not c_carrier_goal3_funded(a)
        and not c_two_route_goal3_funded(a)
        and not c_leakage_goal3_funded(a)
    )
    if distributed_only and not c_predictive_high_dimension(a):
        return False

    return (
        c_g3_endpoint_control_pressure(a) != "HIGH"
        and a.burden_completion_quality >= Grade.MEDIUM
        and effective_continuation >= Grade.MEDIUM
        and effective_stall <= Grade.MEDIUM
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c_direct_act_ceiling(a: MatchAssessment) -> float | None:
    """Highest line allowed for direct ACT under current football structure.

    The G3 certificate remains O2.50. A separate settlement-aware intermediate
    profile may authorize O2.75/O3.00/O3.25 without fabricating a G4 certificate.
    Weak distributed-only G3 rows do not receive a floor merely because their
    evidence is well documented.
    """

    anchor = certified_supported_burden(a, "c")
    if anchor is None:
        return None

    robustness = certificate_robustness(a, "c")
    g3_endpoint_pressure = c_g3_endpoint_control_pressure(a)
    upper_tail_pressure = c_upper_tail_control_pressure(a)

    if g3_endpoint_pressure == "HIGH":
        return None

    base: float | None
    if robustness <= 0:
        base = min(anchor, 2.50) if c_goal3_execution_floor_authorized(a) else None
    elif robustness == 1:
        if anchor <= 2.50 and c_goal3_execution_floor_authorized(a):
            base = anchor
        else:
            protected = round(anchor - 0.25, 2)
            if upper_tail_pressure == "HIGH":
                base = 2.50 if c_goal3_execution_floor_authorized(a) else None
            else:
                base = protected if protected >= 0 else None
    elif anchor > 2.50 and upper_tail_pressure == "HIGH":
        base = 2.50 if c_goal3_execution_floor_authorized(a) else None
    else:
        base = anchor

    if abs(anchor - 2.50) <= 1e-9 and not c_goal4_funded(a):
        bridge = c_intermediate_burden_profile(a)
        if bridge["eligible"] and isinstance(bridge["max_direct_line"], (int, float)):
            candidate = float(bridge["max_direct_line"])
            base = candidate if base is None else max(base, candidate)
    return base


def certificate_robustness(a: MatchAssessment, model: str) -> int:
    """Classify funded certificates as FRAGILE=0, CONDITIONAL=1, ROBUST=2.

    This deliberately reuses frozen, independently auditable football inputs.
    It does not parse prose, infer league quality, inspect bookmaker totals, or
    use observed match outcomes.
    """

    depth = funded_goal_certificate_depth(a, model)
    if depth == 0:
        return 0
    if model == "c" and depth >= 4:
        if not c_upper_tail_transferable(a):
            return 0
        effective_transferability = c_effective_upper_tail_transferability(a)
        transferability_cap = (
            1 if effective_transferability == Grade.MEDIUM else 2
        )
    else:
        transferability_cap = 2

    completion_cap = 2
    endpoint_cap = 2
    if model == "c" and depth == 3:
        effective_continuation, _ = c_effective_incentive_grades(a)
        if (
            a.burden_completion_quality == Grade.MEDIUM
            and effective_continuation == Grade.MEDIUM
        ):
            completion_cap = 1
        distributed_only = (
            c_distributed_goal3_funded(a)
            and not c_carrier_goal3_funded(a)
            and not c_two_route_goal3_funded(a)
            and not c_leakage_goal3_funded(a)
        )
        if distributed_only and c_endpoint_control_pressure(a) == "HIGH":
            endpoint_cap = 1
    if a.material_suppression or a.failure_attacks_route:
        return 0
    if (
        a.route_reliability == Grade.LOW
        or a.chance_quality == Grade.LOW
        or a.failure_resistance == Grade.LOW
        or a.evidence_confidence == Grade.LOW
    ):
        return 0

    trap = a.goal_signal_low_draw_trap_rate
    if trap is not None and trap >= 0.30:
        return 0

    signal_complete = all(
        value is not None
        for value in (
            a.goal_signal_priority_score,
            a.goal_signal_mean_over_two_rate,
            a.goal_signal_mean_over_three_rate,
            a.goal_signal_low_draw_trap_rate,
        )
    )
    legacy_strong_signal = bool(
        signal_complete
        and a.goal_signal_priority_score >= 60
        and a.goal_signal_low_draw_trap_rate <= 0.20
        and (
            a.goal_signal_mean_over_two_rate >= 0.65
            or a.goal_signal_mean_over_three_rate >= 0.50
        )
    )
    high_rate_signal = bool(
        signal_complete
        and a.goal_signal_mean_over_two_rate >= 0.65
        and a.goal_signal_mean_over_three_rate >= 0.45
        and a.goal_signal_low_draw_trap_rate <= 0.20
    )
    strong_frozen_signal = legacy_strong_signal or high_rate_signal
    independent_structure = _independent_scoring_structure(a)
    both_routes_strong = (
        a.home_route == RouteStrength.STRONG
        and a.away_route == RouteStrength.STRONG
        and a.independent_route_quality == Grade.HIGH
    )
    repeatable_current_quality = (
        a.route_reliability == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and independent_structure
    )
    strong_carrier_quality = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.route_reliability == Grade.HIGH
        and a.chance_quality == Grade.HIGH
    )
    if strong_frozen_signal and (
        both_routes_strong
        or repeatable_current_quality
        or strong_carrier_quality
    ):
        return min(2, transferability_cap, completion_cap, endpoint_cap)

    # CONDITIONAL requires at least one independently strong current football
    # dimension. A row of broad MEDIUM grades is deliberately not laundered
    # into robustness merely because the raw scoreline history is high.
    supporting_high_dimension = (
        c_predictive_high_dimension(a)
        if model == "c"
        else any(
            value == Grade.HIGH
            for value in (
                a.chance_quality,
                a.route_reliability,
                a.evidence_confidence,
                a.independent_route_quality,
            )
        )
    )
    if (
        strong_frozen_signal
        and independent_structure
        and supporting_high_dimension
    ):
        return 1
    return 0


def _c_endpoint_control_key(a: MatchAssessment) -> tuple[int, int, int]:
    """Prefer lower explicit stall/trap risk without creating a certificate."""

    _, effective_stall = c_effective_incentive_grades(a)
    trap_known = int(a.goal_signal_low_draw_trap_rate is not None)
    trap = (
        -round(a.goal_signal_low_draw_trap_rate * 10000)
        if a.goal_signal_low_draw_trap_rate is not None
        else -10001
    )
    return -int(effective_stall), trap_known, trap


def _c2_endpoint_control_key(a: MatchAssessment) -> tuple[int, int]:
    """C2 endpoint risk uses only common Step-0 evidence, never C stall labels."""

    trap_known = int(a.goal_signal_low_draw_trap_rate is not None)
    trap = (
        -round(a.goal_signal_low_draw_trap_rate * 10000)
        if a.goal_signal_low_draw_trap_rate is not None
        else -10001
    )
    return trap_known, trap


def ranking_key(a: MatchAssessment) -> tuple[int, ...]:
    """Return the deterministic Football C ranking key.

    Execution-relevant current structure now precedes the coarse robustness
    label. This prevents a broadly-MEDIUM distributed G3 from vaulting above a
    self-funded carrier merely because documentation quality pushed the former
    across a robustness boundary.
    """

    require_c_completion(a)
    effective_continuation, _ = c_effective_incentive_grades(a)
    endpoint = _c_endpoint_control_key(a)
    goal_signal = _goal_signal_rank_key(a)
    upper_tail_self_fund = int(
        a.carrier_self_fund and c_upper_tail_transferable(a)
    )
    profile = follow_priority_profile(a)

    return (
        int(c_goal3_execution_floor_authorized(a)),
        c_goal3_mechanism_rank(a),
        int(profile["follow_clearability_score"]),
        certificate_robustness(a, "c"),
        funded_goal_certificate_depth(a, "c"),
        *endpoint,
        int(effective_continuation),
        int(a.burden_completion_quality),
        *goal_signal,
        int(a.route_reliability),
        int(a.independent_route_quality),
        int(a.chance_quality),
        int(a.carrier),
        int(a.failure_resistance),
        int(a.evidence_confidence),
        int(a.burden_protection),
        int(a.opponent_leakage),
        upper_tail_self_fund,
        int(a.xi_robustness),
        tournament_incentive_rank_score(a),
    )


def ranking_key_clearability_challenger(a: MatchAssessment) -> tuple[int, ...]:
    """Frozen market-independent challenger; never outcome-trained.

    The challenger moves the existing burden-normalized clearability and G3
    floor ahead of certificate depth.  It is intentionally separate from the
    champion key until a same-information replay earns promotion.
    """

    require_c_completion(a)
    profile = follow_priority_profile(a)
    endpoint = _c_endpoint_control_key(a)
    goal_signal = _goal_signal_rank_key(a)
    effective_continuation, _ = c_effective_incentive_grades(a)
    g3_floor = (
        int(c_goal3_funded(a)),
        int(c_goal3_execution_floor_authorized(a)),
        int(a.burden_completion_quality),
        int(effective_continuation),
        int(a.route_reliability),
        int(a.failure_resistance),
        int(a.burden_protection),
    )
    return (
        certificate_robustness(a, "c"),
        int(profile["follow_clearability_score"]),
        *g3_floor,
        *endpoint,
        funded_goal_certificate_depth(a, "c"),
        int(profile["follow_upside_score"]),
        int(profile["follow_balanced_score"]),
        *goal_signal,
        int(a.independent_route_quality),
        int(a.chance_quality),
        int(a.carrier),
        int(a.evidence_confidence),
        int(a.opponent_leakage),
        int(a.xi_robustness),
        tournament_incentive_rank_score(a),
    )


def rank_assessments_clearability_challenger(
    items: Iterable[MatchAssessment],
) -> list[MatchAssessment]:
    """Rank the frozen clearability challenger without changing production."""

    return sorted(
        items,
        key=lambda item: (ranking_key_clearability_challenger(item), item.match_id),
        reverse=True,
    )


def rank_assessments(items: Iterable[MatchAssessment]) -> list[MatchAssessment]:
    """Rank Football C under robustness/certificate-first policy."""
    return sorted(
        items,
        key=lambda item: (ranking_key(item), item.match_id),
        reverse=True,
    )


def c2_ranking_key(a: MatchAssessment) -> tuple[int, ...]:
    """Return Football C2's independent robustness/certificate-first key.

    C2 keeps its own route-quality policy. It never imports C completion,
    continuation, opponent-leakage or stall labels. Shared frozen Step-0 facts
    are allowed because they are common evidence, not C judgments.
    """

    self_funded_carrier_quality = (
        int(a.carrier) if a.carrier_self_fund else int(CarrierStrength.NONE)
    )
    independent_or_carrier = max(
        int(a.independent_route_quality),
        self_funded_carrier_quality,
    )
    endpoint = _c2_endpoint_control_key(a)
    goal_signal = _goal_signal_rank_key(a)

    return (
        certificate_robustness(a, "c2"),
        funded_goal_certificate_depth(a, "c2"),
        *endpoint,
        *goal_signal,
        int(a.route_reliability),
        independent_or_carrier,
        int(a.chance_quality),
        int(a.failure_resistance),
        int(a.xi_robustness),
        int(a.evidence_confidence),
        int(a.burden_protection),
        tournament_incentive_rank_score(a),
    )


def rank_assessments_c2(
    items: Iterable[MatchAssessment],
) -> list[MatchAssessment]:
    """Rank Football C2 under its independent robustness/certificate policy."""
    return sorted(
        items,
        key=lambda item: (c2_ranking_key(item), item.match_id),
        reverse=True,
    )


def follow_through_lane(
    a: MatchAssessment,
    board_state: BoardState,
) -> FollowLane:
    """Pure Step-2 *workload eligibility*, never a second football selector.

    Football C already froze the predictive FOCUS/WATCH/PASS classification
    and C ranking before this function runs. A FOCUS match is eligible for
    routine review irrespective of its supported total, goal-three/four
    funding, stall-risk, carrier or failure profile. Those are *predictive*
    inputs and remain fully enforced by C's model-specific Step-2 decision.

    The board adapter allocates the scarce FOLLOW and RESERVE slots by C
    ranking, operational A/B researchability and exact-kickoff capacity.
    This function must never independently turn an official C FOCUS into
    an operational STOP because of the size of the Over market.
    """
    require_c_completion(a)
    return FollowLane.FOLLOW if board_state == BoardState.FOCUS else FollowLane.STOP

def c2_leakage_goal3_funded(a: MatchAssessment) -> bool:
    """Independent C2 HIGH-leakage goal-three certificate."""

    return (
        getattr(a, "c2_opponent_leakage", None) == Grade.HIGH
        and bool(a.c2_opponent_leakage_basis and a.c2_opponent_leakage_basis.strip())
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_low_burden_leakage_goal3_funded(
    a: MatchAssessment, selected_line: float | None = None
) -> bool:
    """Compatibility alias for the former O2.25-only C2 leakage helper."""

    if selected_line is not None:
        _validate_quarter_line(selected_line)
    return c2_leakage_goal3_funded(a)


def c2_two_route_goal3_funded(a: MatchAssessment) -> bool:
    """Standard C2 strong two-route goal-three certificate."""

    return (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality == Grade.HIGH
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_distributed_goal3_funded(a: MatchAssessment) -> bool:
    """C2-owned distributed 2+1 / 1+2 goal-three certificate."""

    return (
        goal_signal_supports_distributed_goal3(a)
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and a.carrier >= CarrierStrength.USABLE
        and a.route_reliability >= Grade.MEDIUM
        and a.independent_route_quality >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_selection_floor(
    a: MatchAssessment,
    selected_line: float | None = None,
) -> tuple[SelectionFloor, tuple[str, ...]]:
    """Apply C2's exact route-quality floor including distributed G3 proof."""

    hard_reasons: list[str] = []
    if a.failure_attacks_route:
        hard_reasons.append("failure mode attacks scoring route")
    if a.material_suppression:
        hard_reasons.append("material current suppression remains")

    two_route_clear = (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and not hard_reasons
    )
    carrier_clear = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and not hard_reasons
    )
    distributed_clear = c2_distributed_goal3_funded(a) and not hard_reasons
    leakage_clear = c2_leakage_goal3_funded(a) and not hard_reasons
    if two_route_clear or carrier_clear or distributed_clear or leakage_clear:
        return SelectionFloor.CLEAR, ()

    if hard_reasons:
        return SelectionFloor.FAIL, tuple(hard_reasons)

    missing_two_route = 0
    reasons: list[str] = []
    if not (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
    ):
        missing_two_route += 1
        reasons.append("two-route floor lacks two usable routes")
    if max(a.home_route, a.away_route) != RouteStrength.STRONG:
        missing_two_route += 1
        reasons.append("two-route floor lacks a strong route")

    missing_carrier = sum(
        (
            a.carrier != CarrierStrength.STRONG,
            not a.carrier_self_fund,
        )
    )
    if missing_two_route <= 1 or missing_carrier <= 1:
        if missing_carrier:
            reasons.append("carrier floor incomplete")
        if not goal_signal_supports_distributed_goal3(a):
            reasons.append("distributed goal signal not corroborated")
        return SelectionFloor.BORDERLINE, tuple(dict.fromkeys(reasons))

    reasons.append("neither exact C2 selection floor clears")
    return SelectionFloor.FAIL, tuple(dict.fromkeys(reasons))


def c2_goal3_funded(a: MatchAssessment) -> bool:
    """Explicit C2 goal-three certificate."""

    carrier_goal3 = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )
    return (
        carrier_goal3
        or c2_two_route_goal3_funded(a)
        or c2_distributed_goal3_funded(a)
        or c2_leakage_goal3_funded(a)
    )


def c2_goal4_funded(a: MatchAssessment) -> bool:
    """Explicit C2 goal-four certificate, independent of C completion labels."""

    if not c2_goal3_funded(a) or not a.independent_upper_tail:
        return False
    incentive_bias = tournament_incentive_profile(a)["tail_bias"]
    grades = (a.route_reliability, a.chance_quality, a.failure_resistance)
    frozen_tail = bool(
        a.goal_signal_mean_over_two_rate is not None
        and a.goal_signal_mean_over_three_rate is not None
        and a.goal_signal_low_draw_trap_rate is not None
        and a.goal_signal_mean_over_two_rate >= 0.65
        and a.goal_signal_mean_over_three_rate >= 0.45
        and a.goal_signal_low_draw_trap_rate <= 0.20
    )
    independent_route_tail_quality = (
        a.route_reliability == Grade.HIGH
        and a.independent_route_quality == Grade.HIGH
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and frozen_tail
    )
    carrier_tail_quality = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
    )
    if incentive_bias == "EXPANSIVE":
        quality = (
            all(grade >= Grade.MEDIUM for grade in grades)
            and sum(int(x) for x in grades) >= 5
        )
    elif incentive_bias == "SUPPRESSIVE":
        quality = (
            all(grade == Grade.HIGH for grade in grades)
            and a.burden_protection == Grade.HIGH
        )
    else:
        quality = (
            all(grade == Grade.HIGH for grade in grades)
            or independent_route_tail_quality
            or carrier_tail_quality
        )
    route_tail = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
    ) or (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.independent_route_quality == Grade.HIGH
    )
    return (
        quality
        and route_tail
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_clearing_goal_funded(a: MatchAssessment, selected_line: float) -> bool:
    """Compatibility wrapper using exact Asian full-win settlement semantics."""

    _validate_quarter_line(selected_line)
    required = required_full_win_goal(selected_line)
    if required <= 3:
        return c2_goal3_funded(a)
    if required == 4:
        return c2_goal4_funded(a)
    if required == 5:
        return c2_goal5_funded(a)
    if required == 6:
        return c2_goal6_funded(a)
    return False


def c_goal5_funded(a: MatchAssessment) -> bool:
    """Prospective C certificate for goal five, frozen before market comparison.

    This deliberately requires a materially stronger football shape than goal
    four. It uses only the pre-market assessment and never bookmaker input.
    """

    require_c_completion(a)
    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    if tournament_incentive_profile(a)["tail_bias"] == "SUPPRESSIVE":
        return False
    return (
        c_goal4_funded(a)
        and a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality >= Grade.MEDIUM
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence == Grade.HIGH
        and a.burden_protection >= Grade.MEDIUM
        and a.burden_completion_quality == Grade.HIGH
        and effective_continuation == Grade.HIGH
        and effective_stall <= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c_goal6_funded(a: MatchAssessment) -> bool:
    """Prospective C certificate for goal six; intentionally exceptional."""

    require_c_completion(a)
    return (
        c_goal5_funded(a)
        and a.independent_route_quality == Grade.HIGH
        and a.failure_resistance == Grade.HIGH
        and a.xi_robustness == Grade.HIGH
        and a.burden_protection == Grade.HIGH
        and (
            (
                a.home_route == RouteStrength.STRONG
                and a.away_route == RouteStrength.STRONG
            )
            or (
                a.completion_mode in {CompletionMode.MIXED, CompletionMode.FORCED_CHAOS}
                and a.opponent_leakage == Grade.HIGH
            )
        )
    )


def c2_goal5_funded(a: MatchAssessment) -> bool:
    """Prospective C2 goal-five certificate from common frozen football evidence."""

    incentive_bias = tournament_incentive_profile(a)["tail_bias"]
    if incentive_bias == "SUPPRESSIVE":
        return False
    failure_floor = Grade.MEDIUM if incentive_bias == "EXPANSIVE" else Grade.HIGH
    return (
        c2_goal4_funded(a)
        and a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and min(a.home_route, a.away_route) >= RouteStrength.USABLE
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance >= failure_floor
        and a.evidence_confidence == Grade.HIGH
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_goal6_funded(a: MatchAssessment) -> bool:
    """Prospective C2 goal-six certificate; no market evidence is admissible."""

    return (
        c2_goal5_funded(a)
        and a.home_route == RouteStrength.STRONG
        and a.away_route == RouteStrength.STRONG
        and a.xi_robustness == Grade.HIGH
        and a.burden_protection == Grade.HIGH
    )


def required_full_win_goal(line: float) -> int:
    """Return integer total required for a full win on an Asian Over line.

    .75 lines need the next goal beyond the nominal threshold because landing
    on the adjacent integer produces only a half win (for example O2.75 at
    exactly three goals).
    """

    _validate_quarter_line(line)
    whole = int(line)
    quarter = round(line - whole, 2)
    return whole + (2 if quarter == 0.75 else 1)


def credible_burden_profile(
    a: MatchAssessment,
    model: str,
) -> dict[str, bool | str | float | int | None]:
    """Describe a market-independent credible tail without changing certificates.

    The certified burden remains the only execution-authoritative line. This
    diagnostic layer exists to prevent the coarse G3->2.50, G4->3.50,
    G5->4.50 ladder from making materially different football shapes look
    identical. It is frozen from football evidence only and must never be
    upgraded by bookmaker prices or final scores.
    """

    if model != "c":
        return {
            "credible_tail_state": "REJECTED",
            "credible_tail_target_goal": None,
            "credible_burden_band_low": None,
            "credible_burden_band_high": None,
            "credible_burden_band_role": "PREMARKET_DIAGNOSTIC_ONLY",
            "credible_tail_market_independent": True,
            "credible_tail_execution_authority": False,
            "credible_tail_basis": "ACTIVE_C_ONLY",
        }

    goal3 = c_goal3_funded(a)
    goal4 = c_goal4_funded(a)
    goal5 = c_goal5_funded(a)
    goal6 = c_goal6_funded(a)
    certified = (
        5.50 if goal6 else
        4.50 if goal5 else
        3.50 if goal4 else
        2.50 if goal3 else
        None
    )
    if certified is None:
        return {
            "credible_tail_state": "REJECTED",
            "credible_tail_target_goal": 3,
            "credible_burden_band_low": None,
            "credible_burden_band_high": None,
            "credible_burden_band_role": "PREMARKET_DIAGNOSTIC_ONLY",
            "credible_tail_market_independent": True,
            "credible_tail_execution_authority": False,
            "credible_tail_basis": "G3_NOT_FUNDED",
        }

    funded_depth = 6 if goal6 else 5 if goal5 else 4 if goal4 else 3
    if funded_depth >= 6:
        return {
            "credible_tail_state": "FUNDED",
            "credible_tail_target_goal": None,
            "credible_burden_band_low": certified,
            "credible_burden_band_high": certified,
            "credible_burden_band_role": "PREMARKET_DIAGNOSTIC_ONLY",
            "credible_tail_market_independent": True,
            "credible_tail_execution_authority": False,
            "credible_tail_basis": "G6_ALREADY_FUNDED; no higher production certificate is defined",
        }

    target_goal = funded_depth + 1
    continuation, stall = c_effective_incentive_grades(a)
    transfer = a.upper_tail_transferability
    comparable = a.upper_tail_comparable_context_signal
    tail_bias = tournament_incentive_profile(a)["tail_bias"]
    sample_over_three = a.goal_signal_mean_over_three_rate
    low_draw = a.goal_signal_low_draw_trap_rate

    transferable_signal = bool(
        transfer is not None
        and transfer >= Grade.MEDIUM
        and comparable != "SUPPRESSIVE"
    )
    sample_tail_support = bool(
        sample_over_three is not None
        and sample_over_three >= 0.50
        and (low_draw is None or low_draw <= 0.25)
    )
    hard_reject = bool(
        a.material_suppression
        or a.failure_attacks_route
        or tail_bias == "SUPPRESSIVE"
        or comparable == "SUPPRESSIVE"
        or transfer is None
        or transfer < Grade.MEDIUM
        or stall > Grade.MEDIUM
    )

    near_funded = False
    mixed = False

    if target_goal == 4:
        carrier_near = (
            a.carrier == CarrierStrength.STRONG
            and a.carrier_self_fund
            and a.route_reliability >= Grade.MEDIUM
            and a.chance_quality == Grade.HIGH
            and a.failure_resistance >= Grade.MEDIUM
            and a.evidence_confidence >= Grade.MEDIUM
            and a.burden_completion_quality >= Grade.MEDIUM
            and continuation >= Grade.MEDIUM
        )
        distributed_near = (
            a.home_route == RouteStrength.STRONG
            and a.away_route == RouteStrength.STRONG
            and a.independent_route_quality == Grade.HIGH
            and a.route_reliability >= Grade.MEDIUM
            and a.chance_quality >= Grade.MEDIUM
            and a.failure_resistance >= Grade.MEDIUM
            and a.burden_completion_quality == Grade.HIGH
            and continuation == Grade.HIGH
        )
        near_funded = bool(
            not hard_reject
            and transferable_signal
            and sample_tail_support
            and (carrier_near or distributed_near)
        )
        mixed = bool(
            not hard_reject
            and transferable_signal
            and continuation >= Grade.MEDIUM
            and (
                (a.carrier == CarrierStrength.STRONG and a.carrier_self_fund)
                or (
                    a.home_route >= RouteStrength.USABLE
                    and a.away_route >= RouteStrength.USABLE
                    and max(a.home_route, a.away_route) == RouteStrength.STRONG
                )
            )
        )
    elif target_goal == 5:
        near_funded = bool(
            not hard_reject
            and goal4
            and transferable_signal
            and sample_tail_support
            and a.carrier == CarrierStrength.STRONG
            and a.carrier_self_fund
            and a.independent_upper_tail
            and a.route_reliability == Grade.HIGH
            and a.independent_route_quality >= Grade.MEDIUM
            and a.chance_quality == Grade.HIGH
            and a.failure_resistance >= Grade.MEDIUM
            and a.evidence_confidence == Grade.HIGH
            and a.burden_protection >= Grade.MEDIUM
            and a.burden_completion_quality >= Grade.MEDIUM
            and continuation == Grade.HIGH
        )
        mixed = bool(
            not hard_reject
            and goal4
            and transferable_signal
            and continuation >= Grade.MEDIUM
        )
    elif target_goal == 6:
        near_funded = bool(
            not hard_reject
            and goal5
            and transferable_signal
            and sample_over_three is not None
            and sample_over_three >= 0.60
            and a.independent_route_quality >= Grade.MEDIUM
            and a.failure_resistance >= Grade.MEDIUM
            and a.xi_robustness >= Grade.MEDIUM
            and a.burden_protection == Grade.HIGH
            and (
                (
                    a.home_route == RouteStrength.STRONG
                    and a.away_route == RouteStrength.STRONG
                )
                or (
                    a.completion_mode in {CompletionMode.MIXED, CompletionMode.FORCED_CHAOS}
                    and a.opponent_leakage == Grade.HIGH
                )
            )
        )
        mixed = bool(
            not hard_reject
            and goal5
            and transferable_signal
            and continuation >= Grade.MEDIUM
        )

    if near_funded:
        state = "NEAR_FUNDED"
        band_low = certified + 0.25
        band_high = certified + 0.75
        basis = (
            f"G{target_goal}_NEAR_FUNDED_PREMARKET: strong next-goal mechanisms "
            "remain just below the full certificate; band is diagnostic only"
        )
    elif funded_depth >= 4:
        state = "FUNDED"
        band_low = certified
        band_high = certified
        basis = (
            f"G{funded_depth}_FUNDED; G{target_goal} not near-funded under the "
            "market-independent diagnostic gate"
        )
    elif mixed:
        state = "MIXED"
        band_low = certified
        band_high = certified + 0.50
        basis = (
            f"G{target_goal}_MIXED_PREMARKET: credible upper-tail evidence exists "
            "but lacks the protected carrier/distributed shape for NEAR_FUNDED"
        )
    else:
        state = "REJECTED"
        band_low = certified
        band_high = certified
        basis = (
            f"G{target_goal}_REJECTED_PREMARKET: next-goal tail lacks sufficient "
            "transferable or continuation support"
        )

    return {
        "credible_tail_state": state,
        "credible_tail_target_goal": target_goal,
        "credible_burden_band_low": band_low,
        "credible_burden_band_high": band_high,
        "credible_burden_band_role": "PREMARKET_DIAGNOSTIC_ONLY",
        "credible_tail_market_independent": True,
        "credible_tail_execution_authority": False,
        "credible_tail_basis": basis,
    }


def prospective_goal_funding(
    a: MatchAssessment,
    model: str,
) -> dict[str, bool | str | float | None]:
    """Freeze explicit G3/G4/G5/G6 certificates before market comparison."""

    if model == "c":
        goal3 = c_goal3_funded(a)
        goal4 = c_goal4_funded(a)
        goal5 = c_goal5_funded(a)
        goal6 = c_goal6_funded(a)
        two_route_goal3 = c_two_route_goal3_funded(a)
        distributed_goal3 = c_distributed_goal3_funded(a)
        leakage_goal3 = c_leakage_goal3_funded(a)
        carrier_goal3 = c_carrier_goal3_funded(a)
    elif model == "c2":
        goal3 = c2_goal3_funded(a)
        goal4 = c2_goal4_funded(a)
        goal5 = c2_goal5_funded(a)
        goal6 = c2_goal6_funded(a)
        two_route_goal3 = c2_two_route_goal3_funded(a)
        distributed_goal3 = c2_distributed_goal3_funded(a)
        leakage_goal3 = c2_leakage_goal3_funded(a)
        carrier_goal3 = (
            a.carrier == CarrierStrength.STRONG
            and a.carrier_self_fund
            and a.route_reliability >= Grade.MEDIUM
            and a.chance_quality >= Grade.MEDIUM
            and a.failure_resistance >= Grade.MEDIUM
            and a.evidence_confidence >= Grade.MEDIUM
            and a.burden_protection >= Grade.MEDIUM
            and not a.material_suppression
            and not a.failure_attacks_route
        )
    else:
        raise ValueError("model must be c or c2")

    if goal5:
        strength = "STRONG"
    elif goal4:
        strength = "MEDIUM"
    elif goal3:
        strength = "WEAK"
    else:
        strength = "NONE"

    ceiling = (
        5.50 if goal6 else
        4.50 if goal5 else
        3.50 if goal4 else
        2.50 if goal3 else
        None
    )
    incentive = tournament_incentive_profile(a)
    effective_continuation = None
    effective_stall = None
    if model == "c":
        effective_continuation, effective_stall = c_effective_incentive_grades(a)
    credible_profile = credible_burden_profile(a, model)
    return {
        "upper_tail_transferability": (
            a.upper_tail_transferability.name
            if model == "c" and a.upper_tail_transferability is not None
            else None
        ),
        "upper_tail_transferability_basis": (
            a.upper_tail_transferability_basis if model == "c" else None
        ),
        "upper_tail_comparable_context_signal": (
            a.upper_tail_comparable_context_signal if model == "c" else None
        ),
        "upper_tail_comparable_context_basis": (
            a.upper_tail_comparable_context_basis if model == "c" else None
        ),
        "effective_upper_tail_transferability": (
            c_effective_upper_tail_transferability(a).name
            if model == "c"
            and c_effective_upper_tail_transferability(a) is not None
            else None
        ),
        "goal3_funded": goal3,
        "goal4_funded": goal4,
        "goal5_funded": goal5,
        "goal6_funded": goal6,
        "goal3_carrier_funded": carrier_goal3,
        "goal3_two_route_funded": two_route_goal3,
        "goal3_distributed_funded": distributed_goal3,
        "goal3_leakage_funded": leakage_goal3,
        "upper_tail_strength": strength,
        "prospective_tail_ceiling": ceiling,
        "certified_supported_burden": ceiling,
        "tournament_incentive_resolution": a.tournament_incentive_resolution,
        "tournament_incentive_effect": a.incentive_effect,
        "tournament_tail_bias": incentive["tail_bias"],
        "tournament_positive_pressure": incentive["positive_pressure"],
        "tournament_suppressive_pressure": incentive["suppressive_pressure"],
        "effective_continuation_quality": (
            effective_continuation.name if effective_continuation is not None else None
        ),
        "effective_burden_stall_risk": (
            effective_stall.name if effective_stall is not None else None
        ),
        **credible_profile,
    }


def certified_supported_burden(
    a: MatchAssessment,
    model: str,
) -> float | None:
    """Compile the authoritative burden from frozen goal certificates."""

    return prospective_goal_funding(a, model)["certified_supported_burden"]


def certified_supported_burden_basis(
    a: MatchAssessment,
    model: str,
) -> str:
    profile = prospective_goal_funding(a, model)
    burden = profile["certified_supported_burden"]
    if burden is None:
        return "NO_CERTIFIED_BURDEN: goal three is not funded by frozen football evidence"
    highest = 6 if profile["goal6_funded"] else 5 if profile["goal5_funded"] else 4 if profile["goal4_funded"] else 3
    mechanisms = []
    if profile["goal3_carrier_funded"]:
        mechanisms.append("CARRIER_G3")
    if profile["goal3_two_route_funded"]:
        mechanisms.append("TWO_ROUTE_G3")
    if profile["goal3_distributed_funded"]:
        mechanisms.append("DISTRIBUTED_G3")
    if profile["goal3_leakage_funded"]:
        mechanisms.append("LEAKAGE_G3")
    mechanism_text = ",".join(mechanisms) or "UPPER_TAIL_ONLY"
    effective_transferability = (
        c_effective_upper_tail_transferability(a) if model == "c" else None
    )
    transferability_text = (
        effective_transferability.name
        if highest >= 4 and effective_transferability is not None
        else "NOT_APPLICABLE"
    )
    comparable_context_text = (
        a.upper_tail_comparable_context_signal
        if model == "c" and a.upper_tail_comparable_context_signal is not None
        else "NOT_APPLICABLE"
    )
    return (
        f"DETERMINISTIC_CERTIFICATE_COMPILER: G{highest} highest funded; "
        f"max fully-funded Asian Over={burden:.2f}; G3 mechanisms={mechanism_text}; "
        f"upper_tail_transferability={transferability_text}; "
        f"comparable_context={comparable_context_text}"
    )



def follow_priority_profile(
    a: MatchAssessment,
) -> dict[str, int | str | bool | float | None]:
    """Score FOCUS workload priority without changing Football C selection.

    The official C rank and G3/G4/G5/G6 certificates remain untouched. This
    bounded workload profile separates protected floor strength from credible
    scoring ceiling so scarce FOLLOW slots are not allocated by a single
    lexicographic cutoff. Bookmaker prices and eventual match results are not
    inputs.

    Historical Step-0 goal signals are deliberately capped at 10 ceiling
    points, so a small rate/priority difference can break a close tie but cannot
    overwhelm materially stronger current football structure.
    """

    require_c_completion(a)
    depth = funded_goal_certificate_depth(a, "c")
    robustness = certificate_robustness(a, "c")
    credible = credible_burden_profile(a, "c")
    certified = certified_supported_burden(a, "c")

    floor = 0
    if depth:
        floor += 8 + max(0, depth - 3) * 6
    floor += robustness * 12
    floor += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[a.route_reliability]
    floor += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[a.failure_resistance]
    floor += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[a.burden_protection]
    floor += {Grade.LOW: 0, Grade.MEDIUM: 3, Grade.HIGH: 6}[a.burden_completion_quality]
    _, effective_stall = c_effective_incentive_grades(a)
    floor += {Grade.LOW: 8, Grade.MEDIUM: 4, Grade.HIGH: 0}[effective_stall]
    trap = a.goal_signal_low_draw_trap_rate
    if trap is not None:
        floor += 6 if trap <= 0.10 else 3 if trap <= 0.20 else 0

    tail_state = str(credible["credible_tail_state"])
    tail_points = {
        "REJECTED": 0,
        "MIXED": 8,
        "FUNDED": 10,
        "NEAR_FUNDED": 18,
    }.get(tail_state, 0)
    ceiling = max(0, depth - 3) * 8 + tail_points

    band_high = credible.get("credible_burden_band_high")
    if (
        certified is not None
        and isinstance(band_high, (int, float))
        and band_high > certified
    ):
        ceiling += min(9, round((float(band_high) - certified) * 12))

    if a.carrier == CarrierStrength.STRONG and a.carrier_self_fund:
        ceiling += 10
    if a.independent_upper_tail:
        ceiling += 8
    if a.home_route == RouteStrength.STRONG and a.away_route == RouteStrength.STRONG:
        ceiling += 6
    elif (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
    ):
        ceiling += 3

    effective_continuation, _ = c_effective_incentive_grades(a)
    ceiling += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[effective_continuation]
    ceiling += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[a.burden_completion_quality]
    ceiling += {Grade.LOW: 0, Grade.MEDIUM: 4, Grade.HIGH: 8}[a.chance_quality]
    ceiling += {Grade.LOW: 0, Grade.MEDIUM: 3, Grade.HIGH: 6}[a.opponent_leakage]

    historical_support = 0
    if a.goal_signal_priority_score is not None:
        historical_support += (
            4 if a.goal_signal_priority_score >= 70
            else 3 if a.goal_signal_priority_score >= 60
            else 2 if a.goal_signal_priority_score >= 50
            else 0
        )
    if a.goal_signal_mean_over_three_rate is not None:
        historical_support += (
            4 if a.goal_signal_mean_over_three_rate >= 0.60
            else 3 if a.goal_signal_mean_over_three_rate >= 0.50
            else 2 if a.goal_signal_mean_over_three_rate >= 0.40
            else 0
        )
    if trap is not None:
        historical_support += 2 if trap <= 0.10 else 1 if trap <= 0.20 else 0
    historical_support = min(10, historical_support)
    ceiling += historical_support

    if floor >= 58:
        floor_tier = "HIGH"
    elif floor >= 42:
        floor_tier = "MEDIUM"
    else:
        floor_tier = "LOW"

    if ceiling >= 58:
        ceiling_tier = "HIGH"
    elif ceiling >= 38:
        ceiling_tier = "MEDIUM"
    else:
        ceiling_tier = "LOW"

    # Workload comparison must normalize for the protected burden itself.
    # A G4/O3.50 certificate is stronger evidence than G3/O2.50, but it is also
    # a materially harder line to clear. FOLLOW is scarce research/assessment
    # capacity, not certificate prestige, so higher burden may not win merely
    # because its raw tail score is larger.
    burden_steps = (
        max(0.0, float(certified) - 2.50)
        if certified is not None
        else 0.0
    )
    floor_burden_penalty = round(burden_steps * 10)
    upside_burden_penalty = round(burden_steps * 18)
    balanced_burden_penalty = round(burden_steps * 12)

    clearability = floor - floor_burden_penalty
    upside = ceiling - upside_burden_penalty
    balanced = floor + ceiling - balanced_burden_penalty

    carrier_g3 = c_carrier_goal3_funded(a)
    distributed_g3 = c_distributed_goal3_funded(a)
    leakage_g3 = c_leakage_goal3_funded(a)
    if carrier_g3 and distributed_g3:
        mechanism_class = "HYBRID"
    elif carrier_g3:
        mechanism_class = "CARRIER"
    elif distributed_g3:
        mechanism_class = "DISTRIBUTED"
    elif leakage_g3:
        mechanism_class = "LEAKAGE"
    else:
        mechanism_class = "OTHER"

    profile = f"{floor_tier}_FLOOR_{ceiling_tier}_CEILING"
    return {
        "follow_floor_score": floor,
        "follow_ceiling_score": ceiling,
        "follow_priority_score": balanced,
        "follow_clearability_score": clearability,
        "follow_upside_score": upside,
        "follow_balanced_score": balanced,
        "follow_burden_penalty_clearability": floor_burden_penalty,
        "follow_burden_penalty_upside": upside_burden_penalty,
        "follow_burden_penalty_balanced": balanced_burden_penalty,
        "follow_mechanism_class": mechanism_class,
        "follow_floor_tier": floor_tier,
        "follow_ceiling_tier": ceiling_tier,
        "follow_priority_profile": profile,
        "follow_history_support_points": historical_support,
        "follow_priority_market_independent": True,
        "follow_priority_execution_authority": False,
    }

def market_line_funded(
    a: MatchAssessment,
    line: float,
    model: str,
) -> bool:
    """Judge a quote solely by the goal needed for a full Asian-settlement win."""

    required = required_full_win_goal(line)
    profile = prospective_goal_funding(a, model)
    if required == 3:
        return bool(profile["goal3_funded"])
    if required == 4:
        return bool(profile["goal4_funded"])
    if required == 5:
        return bool(profile["goal5_funded"])
    if required == 6:
        return bool(profile["goal6_funded"])
    return False


C_INTERMEDIATE_MIN_ODDS = {
    2.75: 1.85,
    3.00: 1.90,
}


def c_intermediate_burden_profile(
    a: MatchAssessment,
) -> dict[str, bool | float | str | list[float] | None]:
    """Compile settlement-aware authority between G3/O2.50 and G4/O3.50.

    This is football-first and market-independent. It never upgrades the G3
    certificate to G4. O2.75 can be supported when a strong G3 has credible
    fourth-goal continuation; O3.00 requires a near-funded fourth-goal profile;
    O3.25 additionally requires strong independent upper-tail evidence because
    exactly three goals is a half-loss at that line.
    """

    require_c_completion(a)
    if not c_goal3_funded(a) or c_goal4_funded(a):
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": "INTERMEDIATE_BURDEN_NOT_APPLICABLE",
        }
    if not c_goal3_execution_floor_authorized(a):
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": "G3_FLOOR_NOT_EXECUTION_AUTHORIZED",
        }
    if certificate_robustness(a, "c") < 1:
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": "FRAGILE_G3_HAS_NO_INTERMEDIATE_BURDEN_AUTHORITY",
        }
    if not c_predictive_high_dimension(a):
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": "NO_GENUINELY_HIGH_PREDICTIVE_DIMENSION",
        }
    if c_upper_tail_control_pressure(a) == "HIGH":
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": "UPPER_TAIL_CONTROL_PRESSURE_HIGH",
        }

    credible = credible_burden_profile(a, "c")
    state = str(credible["credible_tail_state"])
    if state not in {"MIXED", "NEAR_FUNDED"}:
        return {
            "eligible": False,
            "max_direct_line": None,
            "authorized_lines": [],
            "basis": f"CREDIBLE_TAIL_{state}_DOES_NOT_SUPPORT_INTERMEDIATE_BURDEN",
        }

    authorized = [2.75]
    max_line = 2.75
    line_states = {
        "2.75": "AUTHORIZED",
        "3.00": "NOT_AUTHORIZED",
        "3.25": "REQUIRES_G4",
    }
    effective_continuation, _ = c_effective_incentive_grades(a)

    if (
        state == "NEAR_FUNDED"
        and effective_continuation >= Grade.MEDIUM
        and (
            (a.carrier == CarrierStrength.STRONG and a.carrier_self_fund)
            or a.independent_route_quality == Grade.HIGH
        )
    ):
        authorized.append(3.00)
        max_line = 3.00
        line_states["3.00"] = "AUTHORIZED"

    return {
        "eligible": True,
        "max_direct_line": max_line,
        "authorized_lines": authorized,
        "line_states": line_states,
        "basis": (
            "SETTLEMENT_AWARE_G3_TO_G4_BRIDGE; certificate remains O2.50; "
            f"credible_tail={state}; authorized={authorized}; "
            "O3.25 explicitly remains G4-required because three goals is a half-loss"
        ),
    }


C_G3_BOOK_MIN_ODDS = {
    2.75: 1.85,
    3.00: 1.90,
}


def c_g3_book_extension_profile(
    a: MatchAssessment,
) -> dict[str, bool | float | str | None]:
    """Compile a football-strength-gated G3 BOOK ceiling.

    The certified burden remains O2.50. A BOOK extension is not a fallback for
    every funded G3 row: FRAGILE and CONDITIONAL certificates may not extend
    above the certificate. Only ROBUST G3 rows with strong current completion
    quality can reach O2.75, and O3.00 additionally requires independent,
    transferable fourth-goal evidence. G3 alone never emits O3.25/O3.50.

    This policy is market-independent. The screenshot is evaluated only after
    the football target has been authorized.
    """

    require_c_completion(a)
    if not c_goal3_funded(a) or c_goal4_funded(a):
        return {
            "eligible": False,
            "max_book_line": None,
            "book_min_odds": None,
            "basis": "G3-only settlement extension not applicable",
        }

    robustness = certificate_robustness(a, "c")
    if robustness < 2:
        return {
            "eligible": False,
            "max_book_line": None,
            "book_min_odds": None,
            "basis": (
                "G3 BOOK extension requires ROBUST certificate; "
                "FRAGILE/CONDITIONAL G3 cannot extend above O2.50"
            ),
        }

    effective_continuation, effective_stall = c_effective_incentive_grades(a)
    strong_completion = (
        a.burden_completion_quality == Grade.HIGH
        and effective_continuation == Grade.HIGH
        and effective_stall <= Grade.MEDIUM
        and a.route_reliability == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )
    if not strong_completion:
        return {
            "eligible": False,
            "max_book_line": None,
            "book_min_odds": None,
            "basis": (
                "ROBUST G3 lacks HIGH completion/continuation/current-route "
                "quality required for BOOK extension"
            ),
        }

    strong_carrier = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
    )
    independent_g3 = (
        c_two_route_goal3_funded(a)
        or c_distributed_goal3_funded(a)
    )
    if not (strong_carrier or independent_g3):
        return {
            "eligible": False,
            "max_book_line": None,
            "book_min_odds": None,
            "basis": (
                "ROBUST G3 lacks a self-funded STRONG carrier or genuine "
                "independent/distributed route structure"
            ),
        }

    # O2.75 is the maximum generic ROBUST-G3 settlement extension.
    max_line = 2.75

    # O3.00 requires an independently evidenced fourth-goal route even though
    # the full G4/O3.50 certificate remains unfunded. This is deliberately
    # stricter than the generic G3 gate and does not use bookmaker information.
    effective_tail = c_effective_upper_tail_transferability(a)
    over_three = a.goal_signal_mean_over_three_rate
    trap = a.goal_signal_low_draw_trap_rate
    fourth_goal_support = (
        a.independent_upper_tail
        and effective_tail is not None
        and effective_tail >= Grade.MEDIUM
        and a.upper_tail_comparable_context_signal in {"SUPPORTIVE", "MIXED"}
        and a.independent_route_quality >= Grade.MEDIUM
        and over_three is not None
        and over_three >= 0.45
        and trap is not None
        and trap <= 0.20
    )
    if fourth_goal_support:
        max_line = 3.00

    return {
        "eligible": True,
        "max_book_line": max_line,
        "book_min_odds": C_G3_BOOK_MIN_ODDS[max_line],
        "basis": (
            "ROBUST G3 football-strength gate; certificate remains O2.50; "
            + (
                "independent transferable fourth-goal evidence permits O3.00"
                if max_line == 3.00
                else "generic extension capped at O2.75"
            )
            + "; O3.25 is never a G3-only BOOK and O3.50 requires funded G4"
        ),
    }

def c_g3_book_min_odds(line: float) -> float:
    """Return the pilot minimum price for an authorized G3 BOOK target."""

    _validate_quarter_line(line)
    if line not in C_G3_BOOK_MIN_ODDS:
        raise ValueError("G3 BOOK target must be O2.75 or O3.00")
    return C_G3_BOOK_MIN_ODDS[line]


def _quote_context(ctx: DecisionContext) -> ModelQuoteContext:
    """Drop execution-only fields while preserving the exact model policy state."""

    return ModelQuoteContext(
        board_state=ctx.board_state,
        thesis_state=ctx.thesis_state,
        quote=ctx.quote,
        top_ranked_focus=ctx.top_ranked_focus,
        primary_mechanism_intact=ctx.primary_mechanism_intact,
        wait_reachable=ctx.wait_reachable,
        wait_requires_negative_info=ctx.wait_requires_negative_info,
        material_veto=ctx.material_veto,
    )


def _healthy_wait(ctx: ModelQuoteContext) -> bool:
    return ctx.wait_reachable and not ctx.wait_requires_negative_info


MAX_C_PREGOAL_UNSUPPORTED_WAIT_DROP = 0.25


def _c_wait_target_is_pregoal_reachable(
    a: MatchAssessment,
    ctx: ModelQuoteContext,
) -> bool:
    """Reject manufactured decay targets far below the observed burden.

    WAIT is a pre-goal entry plan, not permission to hope that a materially
    higher market total collapses to C's certificate. A higher unsupported
    quote may wait only one normal Asian-total step (0.25) down to the
    certified burden. A gap of 0.50+ is material disagreement: after the
    football recheck it must either become funded or PASS.
    """

    compiled = certified_supported_burden(a, "c")
    if compiled is None:
        return False
    if ctx.quote.line <= compiled + 1e-9:
        return True
    return (
        ctx.quote.line - compiled
        <= MAX_C_PREGOAL_UNSUPPORTED_WAIT_DROP + 1e-9
    )


def _healthy_c_wait(a: MatchAssessment, ctx: ModelQuoteContext) -> bool:
    """Require a genuinely reachable pre-goal C WAIT.

    A fragile WATCH certificate may stay visible for research, but a reached
    price must not convert that fragile thesis into exposure unless the current
    football assessment has improved to CONDITIONAL-or-better. FOCUS still
    requires explicit reachability, no negative-information dependency, and a
    target no more than one quarter-goal below an unsupported observed line.
    """

    if not _healthy_wait(ctx):
        return False
    if not _c_wait_target_is_pregoal_reachable(a, ctx):
        return False

    # BOOK is an execution path, so workload priority and a merely
    # CONDITIONAL certificate cannot authorize it. Only ROBUST football may
    # create a conditional order target.
    if certificate_robustness(a, "c") < 2:
        return False
    return True


def _supported_soft_price_zone(
    a: MatchAssessment,
    ctx: ModelQuoteContext,
    model: str,
) -> bool:
    """Allow 1.60-1.64 only for a genuinely funded supported burden.

    This is football-evidence based, not a blanket price relaxation. Higher
    unsupported/tail lines retain the normal 1.65 floor.
    """

    compiled = certified_supported_burden(a, model)
    if compiled is None or ctx.quote.line > compiled + 1e-9:
        return False
    if not market_line_funded(a, ctx.quote.line, model):
        return False
    if model == "c":
        return certificate_robustness(a, model) >= 2
    return certificate_robustness(a, model) >= 1


def model_wait_target(
    a: MatchAssessment,
    ctx: ModelQuoteContext,
    model: str | None = None,
) -> tuple[float, float]:
    """Compile the model's declared WAIT target/minimum price.

    A tail-funded quote waits for price at the same quoted burden. Active
    Football C may wait down to its certified burden only when the unsupported
    line gap is at most 0.25. This function never creates assumed exposure.
    """

    compiled = certified_supported_burden(a, model) if model in {"c", "c2"} else None
    if model == "c" and not _c_wait_target_is_pregoal_reachable(a, ctx):
        raise ValueError(
            "WAIT unavailable: certified target is not realistically reachable "
            "before the first goal"
        )
    if model in {"c", "c2"} and market_line_funded(a, ctx.quote.line, model):
        target_line = ctx.quote.line
    elif compiled is not None:
        target_line = min(ctx.quote.line, compiled)
    else:
        raise ValueError("WAIT unavailable: no certified supported burden")
    min_odds = (
        1.60
        if (
            (ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus)
            or _supported_soft_price_zone(a, ctx, model)
        )
        else 1.65
    )
    return target_line, min_odds


def wait_accounting_target(
    a: MatchAssessment,
    ctx: DecisionContext,
    model: str | None = None,
) -> tuple[float, float]:
    """Backward-compatible strict-decision WAIT target helper."""

    return model_wait_target(a, _quote_context(ctx), model)


def _validate_step2_authorization(
    ctx: DecisionContext,
    *,
    require_c_focus: bool,
) -> None:
    """Fail closed when Step-2 workload authorization does not match C's lane."""

    if ctx.step2_authorization == Step2Authorization.USER_EXCEPTION:
        return

    expected_lane = (
        FollowLane.FOLLOW
        if ctx.step2_authorization == Step2Authorization.ROUTINE_FOLLOW
        else FollowLane.RESERVE
    )
    if ctx.official_follow_lane != expected_lane:
        raise ValueError(
            "DECISION BLOCKED — STEP2 AUTHORIZATION/LANE MISMATCH: "
            f"authorization={ctx.step2_authorization.value}, "
            f"official_follow_lane={ctx.official_follow_lane.value}"
        )

    if require_c_focus and ctx.board_state != BoardState.FOCUS:
        raise ValueError(
            "DECISION BLOCKED — ROUTINE/RESERVE C STEP2 REQUIRES C-FOCUS"
        )


def evaluate_c_quote(a: MatchAssessment, ctx: ModelQuoteContext) -> Decision:
    """Deterministic Football C ACT/BOOK/PASS policy with no execution authority.

    Active C no longer emits a user-facing WAIT for a price-only condition.
    When a previously valid WAIT target is reachable, it is represented as an
    unfilled BOOK target instead. BOOK remains zero exposure until a fill is
    independently confirmed.
    """

    require_c_completion(a)

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary scoring mechanism not intact")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

    compiled_anchor = certified_supported_burden(a, "c")
    execution_strength = c_execution_strength(a)
    endpoint_pressure = c_endpoint_control_pressure(a)
    direct_act_ceiling = c_direct_act_ceiling(a)
    goal3_counterweight = (
        c_leakage_goal3_funded(a)
        or c_distributed_goal3_funded(a)
    )
    effective_continuation, effective_stall = c_effective_incentive_grades(a)

    if effective_stall == Grade.HIGH and not goal3_counterweight:
        return Decision(Action.PASS, "current effective burden stall risk is HIGH")

    if a.burden_completion_quality == Grade.LOW:
        return Decision(Action.PASS, "current burden-completion quality is LOW")

    if effective_continuation == Grade.LOW and not goal3_counterweight:
        return Decision(Action.PASS, "current effective continuation quality is LOW")

    at_or_below = (
        compiled_anchor is not None
        and ctx.quote.line <= compiled_anchor + 1e-9
    )
    line_funded = market_line_funded(a, ctx.quote.line, "c")

    if not line_funded:
        intermediate = c_intermediate_burden_profile(a)
        authorized_intermediate = (
            bool(intermediate["eligible"])
            and ctx.quote.line in set(intermediate["authorized_lines"])
        )
        if authorized_intermediate:
            min_odds = C_INTERMEDIATE_MIN_ODDS[ctx.quote.line]
            if ctx.quote.odds + 1e-9 >= min_odds:
                return Decision(
                    Action.BET,
                    (
                        f"settlement-aware intermediate burden O{ctx.quote.line:.2f} "
                        f"clears football bridge and price floor {min_odds:.2f}; "
                        "G3 certificate remains O2.50 and no G4 is fabricated"
                    ),
                )
            if ctx.quote.line <= 3.00:
                return Decision(
                    Action.BOOK,
                    (
                        f"intermediate burden O{ctx.quote.line:.2f} is football-authorized "
                        f"but requires {min_odds:.2f}+; current {ctx.quote.odds:.2f} "
                        "remains an unfilled target"
                    ),
                    book_target_line=ctx.quote.line,
                    book_min_odds=min_odds,
                    book_target_available=True,
                    current_price_clears_book_target=False,
                )
            return Decision(
                Action.PASS,
                (
                    f"O{ctx.quote.line:.2f} intermediate burden requires {min_odds:.2f}+; "
                    "O3.25 is not converted into a generic G3 BOOK target"
                ),
            )

        book_profile = c_g3_book_extension_profile(a)
        if (
            compiled_anchor is not None
            and abs(compiled_anchor - 2.50) <= 1e-9
            and ctx.board_state == BoardState.FOCUS
            and not at_or_below
            and bool(book_profile["eligible"])
        ):
            max_book_line = float(book_profile["max_book_line"])
            target_line = min(ctx.quote.line, max_book_line)
            if (
                ctx.quote.line - target_line
                > MAX_C_PREGOAL_UNSUPPORTED_WAIT_DROP + 1e-9
            ):
                return Decision(
                    Action.PASS,
                    (
                        f"generic G3 BOOK target O{target_line:.2f} is more than "
                        "0.25 below the visible burden and is not realistically "
                        "reachable before a goal"
                    ),
                )
            target_min_odds = c_g3_book_min_odds(target_line)
            clears_target = ctx.quote.odds + 1e-9 >= target_min_odds
            return Decision(
                Action.BOOK,
                (
                    f"G3 protected certificate remains O2.50; settlement-aware "
                    + (
                        f"conditional order target O{target_line:.2f} "
                        f"@ {target_min_odds:.2f}+ is currently fillable; "
                        f"O3.50 still requires G4"
                        if clears_target else
                        f"conditional order target O{target_line:.2f} "
                        f"@ {target_min_odds:.2f}+ is authorized but current "
                        f"{ctx.quote.odds:.2f} is below the floor, so it remains unfilled"
                    )
                ),
                book_target_line=target_line,
                book_min_odds=target_min_odds,
                book_target_available=True,
                current_price_clears_book_target=clears_target,
            )

        if compiled_anchor is not None and not at_or_below and _healthy_c_wait(a, ctx):
            target_line, target_min_odds = model_wait_target(a, ctx, "c")
            return Decision(
                Action.BOOK,
                (
                    "quoted burden lacks prospective certificate; the one-step "
                    f"certified target is reachable as BOOK O{target_line:.2f} "
                    f"@ {target_min_odds:.2f}+"
                ),
                book_target_line=target_line,
                book_min_odds=target_min_odds,
                book_target_available=True,
                current_price_clears_book_target=False,
            )
        if (
            compiled_anchor is not None
            and not at_or_below
            and ctx.wait_reachable
            and ctx.quote.line - compiled_anchor
                > MAX_C_PREGOAL_UNSUPPORTED_WAIT_DROP + 1e-9
        ):
            return Decision(
                Action.PASS,
                "unsupported market burden is more than 0.25 above the C certificate; "
                "do not manufacture a pre-goal decay WAIT",
            )
        return Decision(
            Action.PASS,
            "C clearing-goal funding missing; prospective tail funding missing "
            "and no settlement-aware BOOK extension clears",
        )

    if direct_act_ceiling is None:
        return Decision(
            Action.PASS,
            (
                "hard endpoint-control or current G3-floor quality blocks direct ACT"
                if endpoint_pressure == "HIGH" or execution_strength == "FRAGILE"
                else "direct ACT ceiling unavailable"
            ),
        )

    if ctx.quote.line > direct_act_ceiling + 1e-9:
        return Decision(
            Action.PASS,
            f"quoted burden exceeds direct ACT ceiling O{direct_act_ceiling:.2f}",
        )

    if ctx.quote.odds >= 1.65:
        return Decision(
            Action.BET,
            (
                "ROBUST supported/protected line at normal price"
                if execution_strength == "ROBUST"
                else (
                    "CONDITIONAL supported/protected line at normal price"
                    if execution_strength == "CONDITIONAL"
                    else "FRAGILE certificate retained only at funded G3 floor"
                )
            ),
        )

    if (
        execution_strength == "ROBUST"
        and at_or_below
        and 1.60 <= ctx.quote.odds < 1.65
        and (
            (ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus)
            or _supported_soft_price_zone(a, ctx, "c")
        )
    ):
        return Decision(
            Action.BET,
            (
                "ROBUST top-focus soft-zone price"
                if ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus
                else "ROBUST certified supported-line soft-zone price"
            ),
        )

    if _healthy_c_wait(a, ctx):
        target_line, target_min_odds = model_wait_target(a, ctx, "c")
        return Decision(
            Action.BOOK,
            (
                f"price blocker; conditional BOOK O{target_line:.2f} "
                f"@ {target_min_odds:.2f}+ is reachable"
            ),
            book_target_line=target_line,
            book_min_odds=target_min_odds,
            book_target_available=True,
            current_price_clears_book_target=False,
        )

    return Decision(Action.PASS, "price unacceptable without a valid conditional BOOK target")


def decide_c(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Strict Football C execution policy.

    Execution authorization is validated here, then the exact same active-C
    ACT/BOOK/PASS quote policy used by observed-price assessment is applied.
    """

    require_c_completion(a)
    _validate_step2_authorization(ctx, require_c_focus=True)
    return evaluate_c_quote(a, _quote_context(ctx))


def c2_bridge_eligibility(
    a: MatchAssessment,
    ctx: ModelQuoteContext,
) -> tuple[bool, tuple[str, ...]]:
    """Check the text C2 Focus Market-Gap Bridge deterministically."""

    reasons: list[str] = []
    compiled_anchor = certified_supported_burden(a, "c2")
    gap = round(ctx.quote.line - compiled_anchor, 10) if compiled_anchor is not None else 999.0
    floor, _ = c2_selection_floor(a, ctx.quote.line)

    if ctx.board_state != BoardState.FOCUS:
        reasons.append("not C2-FOCUS")
    if gap <= 0 or gap > 0.50:
        reasons.append("market gap outside +0.25/+0.50 bridge")
    if ctx.thesis_state == ThesisState.BROKEN:
        reasons.append("thesis broken")
    if not ctx.primary_mechanism_intact:
        reasons.append("primary mechanism damaged")
    if floor != SelectionFloor.CLEAR:
        reasons.append("selection-quality floor not clear")

    routes = sorted((a.home_route, a.away_route), reverse=True)
    route_condition = (
        routes[0] == RouteStrength.STRONG
        and (
            routes[1] == RouteStrength.STRONG
            or (
                routes[1] >= RouteStrength.USABLE
                and a.carrier == CarrierStrength.STRONG
            )
        )
    )
    if not route_condition:
        reasons.append("route/carrier bridge condition not met")

    if not a.independent_upper_tail:
        reasons.append("independent non-market upper-tail proof missing")
    if a.material_suppression or ctx.material_veto:
        reasons.append("material suppression remains")
    if ctx.quote.odds < 1.65:
        reasons.append("price below bridge floor")
    if not c2_clearing_goal_funded(a, ctx.quote.line):
        reasons.append("C2 clearing-goal funding missing at bridge line")

    return not reasons, tuple(reasons)


def evaluate_c2_quote(a: MatchAssessment, ctx: ModelQuoteContext) -> Decision:
    """Deterministic C2 shadow ACT/WAIT/PASS policy with no execution authority."""

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary scoring mechanism not intact")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

    compiled_anchor = certified_supported_burden(a, "c2")
    if compiled_anchor is None:
        return Decision(Action.PASS, "C2 has no certified supported burden")

    floor, _ = c2_selection_floor(a, min(ctx.quote.line, compiled_anchor))
    if floor != SelectionFloor.CLEAR:
        return Decision(Action.PASS, "C2 selection-quality floor not clear")

    at_or_below = ctx.quote.line <= compiled_anchor + 1e-9
    if at_or_below:
        if ctx.quote.odds >= 1.65:
            return Decision(
                Action.BET,
                "selection floor clear at supported/protected line",
            )

        if (
            1.60 <= ctx.quote.odds < 1.65
            and (
                (ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus)
                or _supported_soft_price_zone(a, ctx, "c2")
            )
        ):
            return Decision(
                Action.BET,
                (
                    "top-focus soft-zone price at/below burden"
                    if ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus
                    else "certified supported-line soft-zone price"
                ),
            )

        if _healthy_wait(ctx):
            return Decision(Action.WAIT, "price blocker with healthy reachable wait")

        return Decision(Action.PASS, "price unacceptable without healthy wait path")

    if market_line_funded(a, ctx.quote.line, "c2"):
        bridge_ok, _ = c2_bridge_eligibility(a, ctx)
        if ctx.quote.odds >= 1.65:
            gap = round(ctx.quote.line - compiled_anchor, 2)
            return Decision(
                Action.BET,
                (
                    f"FOCUS MARKET-GAP BRIDGE +{gap:.2f}"
                    if bridge_ok
                    else "prospective tail certificate funds quoted line"
                ),
                bridge_used=bridge_ok,
            )
        if _healthy_wait(ctx):
            return Decision(
                Action.WAIT,
                "tail-funded quoted burden; price blocker with healthy reachable wait",
            )
        return Decision(Action.PASS, "price unacceptable without healthy wait path")

    if _healthy_wait(ctx):
        return Decision(
            Action.WAIT,
            "quoted burden lacks prospective certificate; healthy certified target reachable",
        )

    return Decision(
        Action.PASS,
        "quoted burden lacks prospective goal funding and wait is unrealistic",
    )


def decide_c2(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Strict C2 execution policy using the shared pure quote policy."""

    _validate_step2_authorization(ctx, require_c_focus=False)
    return evaluate_c2_quote(a, _quote_context(ctx))


def _split_quarter_line(line: float) -> tuple[float, ...]:
    _validate_quarter_line(line)
    q = round(line * 4)
    frac = q % 4
    base = q // 4

    if frac == 1:
        return (float(base), base + 0.5)
    if frac == 3:
        return (base + 0.5, float(base + 1))
    return (line,)


def settle_over(
    line: float,
    total_goals: int,
    odds: float | None = None,
) -> tuple[Settlement, float | None]:
    """Settle an Asian Over total and optionally return flat 1u profit."""

    if total_goals < 0:
        raise ValueError("total_goals must be non-negative")
    if odds is not None and odds <= 1.0:
        raise ValueError("decimal odds must be > 1.0")

    results: list[str] = []
    profits: list[float] = []

    for component in _split_quarter_line(line):
        if total_goals > component:
            results.append("W")
            if odds is not None:
                profits.append(odds - 1.0)
        elif total_goals == component:
            results.append("P")
            if odds is not None:
                profits.append(0.0)
        else:
            results.append("L")
            if odds is not None:
                profits.append(-1.0)

    if all(x == "W" for x in results):
        settlement = Settlement.WIN
    elif all(x == "L" for x in results):
        settlement = Settlement.LOSS
    elif all(x == "P" for x in results):
        settlement = Settlement.PUSH
    elif set(results) == {"W", "P"}:
        settlement = Settlement.HALF_WIN
    elif set(results) == {"L", "P"}:
        settlement = Settlement.HALF_LOSS
    else:
        raise AssertionError(f"unexpected component settlement: {results}")

    unit_profit = None if odds is None else sum(profits) / len(profits)
    return settlement, unit_profit
