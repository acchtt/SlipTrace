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
        if self.c2_opponent_leakage is not None and not (
            self.c2_opponent_leakage_basis
            and self.c2_opponent_leakage_basis.strip()
        ):
            raise ValueError("C2 leakage grade requires independent non-empty basis")


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


def low_burden_leakage_goal3_funded(
    a: MatchAssessment, selected_line: float | None = None
) -> bool:
    """Return whether C can fund goal three through a leakage-led O2.25 path.

    Oct-12 calibration showed a recurring false-negative shape: a STRONG route
    facing HIGH opponent leakage was suppressed by recent 1-1/two-goal stall
    history even when the first-two-goal mechanism remained live. This narrow
    route exists only at O2.25 or lower. It does not justify O2.5/O2.75 and does
    not create a fourth-goal tail.

    The safeguard deliberately requires:
      - a STRONG scoring route,
      - HIGH opponent leakage,
      - at least MEDIUM burden-completion and route reliability,
      - at least MEDIUM current chance quality,
      - HIGH burden-stall risk or LOW continuation (the specific suppression
        being counterweighted),
      - no material suppression or route-attacking failure.

    This is not a new generic positive factor. It activates only when the
    current matchup-specific leakage is counterweighting the exact stall/
    continuation suppression identified by the audit. LOW burden-completion
    can never be rescued.
    """
    require_c_completion(a)
    burden = a.supported_line if selected_line is None else selected_line
    _validate_quarter_line(burden)
    if burden > 2.25:
        return False
    return (
        max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.opponent_leakage == Grade.HIGH
        and a.burden_completion_quality >= Grade.MEDIUM
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and (
            a.burden_stall_risk == Grade.HIGH
            or a.continuation_quality == Grade.LOW
        )
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def clearing_goal_funded(a: MatchAssessment, selected_line: float | None = None) -> bool:
    """Return whether C has explicit prospective funding for the clearing goal.

    This is intentionally stricter than FOCUS. It is used by ranking and the
    operational FOLLOW certification, not to narrow the broad C-FOCUS pool.

    For O2.25/O2.5/O2.75, a full win requires goal 3. A carrier-led path must prove
    that goal independently; a merely USABLE supporting route is not enough.
    TWO_SIDED/MIXED can fund it through two usable routes only when both the
    completion and continuation diagnostics are HIGH. O2.25 additionally admits
    the narrow leakage-led route above; that route never extends to O2.5/O2.75.
    O3.0 requires independent upper-tail/self-funding carrier proof because a
    fourth-goal tail cannot be inferred from ordinary two-route shape.
    """
    require_c_completion(a)
    burden = a.supported_line if selected_line is None else selected_line
    _validate_quarter_line(burden)

    # O2.25 still loses half at two goals; O2.0 instead pushes.
    if burden <= 2.0:
        return True

    strong_carrier_goal3 = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and not a.material_suppression
        and not a.failure_attacks_route
    )
    two_route_goal3 = (
        a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and a.burden_completion_quality == Grade.HIGH
        and a.continuation_quality == Grade.HIGH
        and a.opponent_leakage >= Grade.MEDIUM
        and not a.material_suppression
        and not a.failure_attacks_route
    )
    leakage_goal3 = low_burden_leakage_goal3_funded(a, burden)

    if burden < 3.0:
        return strong_carrier_goal3 or two_route_goal3 or leakage_goal3

    # O3.0 FOLLOW needs an independently supported upper tail; ordinary
    # two-sidedness or O2.25 leakage pressure cannot manufacture goal four.
    return strong_carrier_goal3


def ranking_key(a: MatchAssessment) -> tuple[int, ...]:
    """Return the deterministic lexicographic Football C ranking key.

    Higher is better. Selection is now burden-completion first: a credible path
    to clearing the actual protected line outranks cosmetic two-sidedness.
    Lower supported burden is a comparator only after completion/continuation
    quality has already cleared; it never creates a route by itself.
    """

    require_c_completion(a)
    upper_tail_self_fund = int(a.carrier_self_fund and a.independent_upper_tail)
    lower_burden = -round(a.supported_line * 4)

    return (
        int(clearing_goal_funded(a)),
        int(a.continuation_quality),
        -int(a.burden_stall_risk),
        int(a.burden_completion_quality),
        int(a.route_reliability),
        int(a.carrier),
        int(a.failure_resistance),
        int(a.evidence_confidence),
        int(a.burden_protection),
        lower_burden,
        int(a.opponent_leakage),
        upper_tail_self_fund,
        int(a.chance_quality),
        int(a.xi_robustness),
        int(a.independent_route_quality),
    )


def rank_assessments(items: Iterable[MatchAssessment]) -> list[MatchAssessment]:
    """Rank Football C with the active burden-completion-first policy."""
    return sorted(
        items,
        key=lambda item: (ranking_key(item), item.match_id),
        reverse=True,
    )


def c2_ranking_key(a: MatchAssessment) -> tuple[int, ...]:
    """Return the frozen Football C2 lexicographic ranking key.

    C2 deliberately does NOT inherit Football C's burden-completion-first
    selector. Its frozen challenger specification ranks:
      1. route reliability;
      2. independent route quality / self-funded carrier;
      3. current chance quality;
      4. failure-mode resistance;
      5. XI robustness;
      6. evidence confidence;
      7. burden protection.

    The slash in factor 2 is represented as one combined dimension: whichever
    is stronger between independent-route quality and a genuinely self-funded
    carrier. Market price and supported-line magnitude do not create rank.
    """

    self_funded_carrier_quality = (
        int(a.carrier) if a.carrier_self_fund else int(CarrierStrength.NONE)
    )
    independent_or_carrier = max(
        int(a.independent_route_quality),
        self_funded_carrier_quality,
    )

    return (
        int(a.route_reliability),
        independent_or_carrier,
        int(a.chance_quality),
        int(a.failure_resistance),
        int(a.xi_robustness),
        int(a.evidence_confidence),
        int(a.burden_protection),
    )


def rank_assessments_c2(
    items: Iterable[MatchAssessment],
) -> list[MatchAssessment]:
    """Rank Football C2 under its frozen challenger policy."""
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

def c2_low_burden_leakage_goal3_funded(
    a: MatchAssessment, selected_line: float | None = None
) -> bool:
    """C2-owned goal-three counterweight, never an imported C completion grade.

    Only O2.25 can use independently evidenced HIGH opponent leakage to fund
    goal three when the otherwise credible STRONG route lacks separate upper-
    tail proof. Requires a named C2 leakage basis and high route reliability;
    absent or LOW/MEDIUM leakage evidence cannot upgrade a match. Does not
    prove a fourth goal or waive material football vetoes.
    """
    # Read-only diagnostic shadow probes may carry only route-quality fields.
    # Absence of a C2-specific leakage grade or burden always leaves the old
    # selection result unchanged; never infer HIGH leakage from shared facts.
    burden = getattr(a, "supported_line", None) if selected_line is None else selected_line
    if burden is None or getattr(a, "c2_opponent_leakage", None) != Grade.HIGH:
        return False
    _validate_quarter_line(burden)
    return (
        2.0 < burden <= 2.25
        and a.c2_opponent_leakage == Grade.HIGH
        and bool(a.c2_opponent_leakage_basis and a.c2_opponent_leakage_basis.strip())
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier >= CarrierStrength.USABLE
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.evidence_confidence >= Grade.MEDIUM
        and a.burden_protection >= Grade.MEDIUM
        # Positive independent upper-tail evidence must never make an
        # otherwise qualified O2.25 leakage path worse. This factor is
        # orthogonal here; carrier/two-route proofs may use it separately.
        and not a.material_suppression
        and not a.failure_attacks_route
    )


def c2_selection_floor(
    a: MatchAssessment,
    selected_line: float | None = None,
) -> tuple[SelectionFloor, tuple[str, ...]]:
    """Apply the exact C2 direct-exposure floor where possible.

    BORDERLINE is a QA state only. It means one condition is still unresolved
    and never counts as direct BET proof.
    """

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
        and a.independent_upper_tail
        and not hard_reasons
    )

    # C2's own narrow O2.25 leakage route is a third independent quality
    # certificate. It does not change the standard two-route/carrier floors.
    leakage_clear = c2_low_burden_leakage_goal3_funded(a, selected_line)
    if two_route_clear or carrier_clear or leakage_clear:
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
            not a.independent_upper_tail,
        )
    )

    # Narrow diagnostic state: one unresolved condition from either exact floor
    # and no hard veto. BORDERLINE never authorizes direct exposure.
    if missing_two_route <= 1 or missing_carrier <= 1:
        if missing_carrier:
            reasons.append("carrier floor incomplete")
        return SelectionFloor.BORDERLINE, tuple(dict.fromkeys(reasons))

    reasons.append("neither exact C2 selection floor clears")
    return SelectionFloor.FAIL, tuple(dict.fromkeys(reasons))


def c2_clearing_goal_funded(a: MatchAssessment, selected_line: float) -> bool:
    """Independent C2 route-quality proof at the selected total.

    C2 uses no C-owned completion/continuation/stall grading.
    A CLEAR two-route selection floor alone does not fund goal three.
    Only a C2-sourced HIGH-leakage O2.25 counterweight can replace the
    otherwise required upper-tail proof, never at O2.5 or higher.
    """
    _validate_quarter_line(selected_line)
    floor, _ = c2_selection_floor(a, selected_line)
    if floor != SelectionFloor.CLEAR:
        return False
    if selected_line <= 2.0:
        return True

    carrier_goal3 = (
        a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and a.route_reliability >= Grade.MEDIUM
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
    )
    two_route_goal3 = (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.independent_route_quality == Grade.HIGH
        and a.route_reliability == Grade.HIGH
        and a.chance_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.independent_upper_tail
    )
    if selected_line < 3.0:
        return (
            carrier_goal3
            or two_route_goal3
            or c2_low_burden_leakage_goal3_funded(a, selected_line)
        )

    fourth_goal_quality = (
        a.route_reliability == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance == Grade.HIGH
    )
    return fourth_goal_quality and (
        carrier_goal3
        or (
            two_route_goal3
            and a.home_route == RouteStrength.STRONG
            and a.away_route == RouteStrength.STRONG
        )
    )



def c_goal5_funded(a: MatchAssessment) -> bool:
    """Prospective C certificate for goal five, frozen before market comparison.

    This deliberately requires a materially stronger football shape than goal
    four. It uses only the pre-market assessment and never bookmaker input.
    """

    require_c_completion(a)
    return (
        clearing_goal_funded(a, 3.0)
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
        and a.continuation_quality == Grade.HIGH
        and a.burden_stall_risk <= Grade.MEDIUM
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

    return (
        c2_clearing_goal_funded(a, 3.0)
        and a.carrier == CarrierStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and min(a.home_route, a.away_route) >= RouteStrength.USABLE
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and a.failure_resistance == Grade.HIGH
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


def prospective_goal_funding(
    a: MatchAssessment,
    model: str,
) -> dict[str, bool | str | float | None]:
    """Freeze the model's goal-3/4/5/6 funding profile before price comparison.

    supported_line remains the certified burden/anchor. The tail profile is a
    separate prospective football object used only to judge whether a later
    quoted total is football-funded. A bookmaker line never upgrades this
    profile.
    """

    if model == "c":
        goal3 = clearing_goal_funded(a, 2.75)
        goal4 = clearing_goal_funded(a, 3.0)
        goal5 = c_goal5_funded(a)
        goal6 = c_goal6_funded(a)
    elif model == "c2":
        goal3 = c2_clearing_goal_funded(a, 2.75)
        goal4 = c2_clearing_goal_funded(a, 3.0)
        goal5 = c2_goal5_funded(a)
        goal6 = c2_goal6_funded(a)
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
        5.75 if goal6 else
        4.75 if goal5 else
        3.75 if goal4 else
        2.75 if goal3 else
        None
    )
    return {
        "goal3_funded": goal3,
        "goal4_funded": goal4,
        "goal5_funded": goal5,
        "goal6_funded": goal6,
        "upper_tail_strength": strength,
        "prospective_tail_ceiling": ceiling,
    }


def market_line_funded(
    a: MatchAssessment,
    line: float,
    model: str,
) -> bool:
    """Return whether a later quoted total is funded by frozen football evidence.

    The certified supported_line is an anchor, not a universal execution
    ceiling. Above it, the quote must clear the appropriate prospective goal
    certificate. The O2.25 leakage exception stays local to O2.25 and cannot
    manufacture support for O2.5/O2.75.
    """

    _validate_quarter_line(line)
    if line <= a.supported_line + 1e-9:
        return (
            clearing_goal_funded(a, line)
            if model == "c"
            else c2_clearing_goal_funded(a, line)
        )

    if line <= 2.25:
        return (
            clearing_goal_funded(a, line)
            if model == "c"
            else c2_clearing_goal_funded(a, line)
        )

    profile = prospective_goal_funding(a, model)
    if line < 3.0:
        return bool(profile["goal3_funded"])
    if line < 4.0:
        return bool(profile["goal4_funded"])
    if line < 5.0:
        return bool(profile["goal5_funded"])
    if line < 6.0:
        return bool(profile["goal6_funded"])
    return False


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


def model_wait_target(
    a: MatchAssessment,
    ctx: ModelQuoteContext,
    model: str | None = None,
) -> tuple[float, float]:
    """Compile the model's declared WAIT target/minimum price.

    A tail-funded quote waits for price at the same quoted burden. An
    unsupported higher burden may only wait for the certified supported_line.
    This function never creates assumed exposure.
    """

    target_line = min(ctx.quote.line, a.supported_line)
    if model in {"c", "c2"} and market_line_funded(a, ctx.quote.line, model):
        target_line = ctx.quote.line
    min_odds = (
        1.60
        if ctx.board_state == BoardState.FOCUS and ctx.top_ranked_focus
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
    """Deterministic Football C ACT/WAIT/PASS policy with no execution authority."""

    require_c_completion(a)

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary scoring mechanism not intact")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

    # Preserve the narrow O2.25 leakage counterweight for current stall checks.
    # It can never fund a higher quoted burden.
    executable_anchor = min(ctx.quote.line, a.supported_line)
    leakage_counterweight = low_burden_leakage_goal3_funded(a, executable_anchor)

    if a.burden_stall_risk == Grade.HIGH and not leakage_counterweight:
        return Decision(Action.PASS, "current burden stall risk is HIGH")

    if a.burden_completion_quality == Grade.LOW:
        return Decision(Action.PASS, "current burden-completion quality is LOW")

    if a.continuation_quality == Grade.LOW and not leakage_counterweight:
        return Decision(Action.PASS, "current continuation quality is LOW")

    at_or_below = ctx.quote.line <= a.supported_line + 1e-9
    line_funded = market_line_funded(a, ctx.quote.line, "c")

    if not line_funded:
        anchor_funded = market_line_funded(a, a.supported_line, "c")
        if not at_or_below and anchor_funded and _healthy_wait(ctx):
            return Decision(
                Action.WAIT,
                "quoted burden lacks prospective certificate; healthy certified target reachable",
            )
        return Decision(
            Action.PASS,
            "C clearing-goal funding missing; prospective tail funding missing at quoted burden",
        )

    if ctx.quote.odds >= 1.65:
        return Decision(
            Action.BET,
            (
                "supported/protected line at normal price"
                if at_or_below
                else "prospective tail certificate funds quoted line"
            ),
        )

    if (
        at_or_below
        and 1.60 <= ctx.quote.odds < 1.65
        and ctx.board_state == BoardState.FOCUS
        and ctx.top_ranked_focus
    ):
        return Decision(Action.BET, "top-focus soft-zone price")

    if _healthy_wait(ctx):
        return Decision(
            Action.WAIT,
            (
                "price blocker with healthy reachable wait"
                if at_or_below
                else "tail-funded quoted burden; price blocker with healthy reachable wait"
            ),
        )

    return Decision(Action.PASS, "price unacceptable without healthy wait path")


def decide_c(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Strict Football C execution policy.

    Execution authorization is validated here, then the exact same model quote
    policy used by observed-price assessment is applied.
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
    gap = round(ctx.quote.line - a.supported_line, 10)
    # Bridges must certify the higher quoted burden, not the O2.25 WAIT target.
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

    # The anchor must still clear C2's own selection/funding floor. Higher
    # totals are judged separately by the frozen prospective tail profile.
    executable_anchor = min(ctx.quote.line, a.supported_line)
    floor, _ = c2_selection_floor(a, executable_anchor)
    if floor != SelectionFloor.CLEAR:
        return Decision(Action.PASS, "C2 selection-quality floor not clear")

    if not c2_clearing_goal_funded(a, executable_anchor):
        return Decision(Action.PASS, "C2 clearing-goal funding missing")

    at_or_below = ctx.quote.line <= a.supported_line + 1e-9
    if at_or_below:
        if ctx.quote.odds >= 1.65:
            return Decision(
                Action.BET,
                "selection floor clear at supported/protected line",
            )

        if (
            1.60 <= ctx.quote.odds < 1.65
            and ctx.board_state == BoardState.FOCUS
            and ctx.top_ranked_focus
        ):
            return Decision(
                Action.BET,
                "top-focus soft-zone price at/below burden",
            )

        if _healthy_wait(ctx):
            return Decision(Action.WAIT, "price blocker with healthy reachable wait")

        return Decision(Action.PASS, "price unacceptable without healthy wait path")

    if market_line_funded(a, ctx.quote.line, "c2"):
        bridge_ok, _ = c2_bridge_eligibility(a, ctx)
        if ctx.quote.odds >= 1.65:
            gap = round(ctx.quote.line - a.supported_line, 2)
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
