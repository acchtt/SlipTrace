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


class SecondRouteRole(IntEnum):
    NONE = 0
    STATE_DEPENDENT = 1
    EXCHANGE_ONLY = 2
    BURDEN_CONTRIBUTING = 3


class FundingState(IntEnum):
    NOT_REQUIRED = -1
    NONE = 0
    PARTIAL = 1
    VERIFIED = 2


class FundingSource(Enum):
    NONE = "NONE"
    CARRIER = "CARRIER"
    SECOND_ROUTE = "SECOND_ROUTE"
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

    # Required failure/H2H declarations. Empty or omitted evidence must never
    # become an implicit favorable state in the deterministic validator.
    main_failure: str
    h2h_state: str

    supported_line: float

    carrier_self_fund: bool
    independent_upper_tail: bool
    failure_attacks_route: bool
    material_suppression: bool

    # Football C-owned burden-completion diagnostics. These are deliberately
    # optional in the shared assessment object so C2/C3 do not need to carry
    # C policy labels merely to satisfy a generic parser. The C parser and all
    # C-only deterministic functions fail closed when any field is absent.
    completion_mode: CompletionMode | None = None
    burden_completion_quality: Grade | None = None
    continuation_quality: Grade | None = None
    opponent_leakage: Grade | None = None
    burden_stall_risk: Grade | None = None

    def __post_init__(self) -> None:
        if not self.main_failure.strip():
            raise ValueError("main_failure must be non-empty")
        if not self.h2h_state.strip():
            raise ValueError("h2h_state must be non-empty")
        if self.supported_line < 0:
            raise ValueError("supported_line must be non-negative")
        _validate_quarter_line(self.supported_line)


@dataclass(frozen=True)
class C3PolicyAssessment:
    """C3-only burden-funding policy fields layered on common evidence."""

    base: MatchAssessment
    second_route_role: SecondRouteRole
    goal3_funding: FundingState
    goal3_funding_source: FundingSource
    goal3_funding_basis: str
    goal4_funding: FundingState
    goal4_funding_source: FundingSource
    goal4_funding_basis: str
    control_endpoint_risk: Grade
    control_endpoint_basis: str
    forced_chaos_verified: bool

    def __post_init__(self) -> None:
        for name, value in (
            ("goal3_funding_basis", self.goal3_funding_basis),
            ("goal4_funding_basis", self.goal4_funding_basis),
            ("control_endpoint_basis", self.control_endpoint_basis),
        ):
            if not value.strip():
                raise ValueError(f"{name} must be non-empty")

        line = self.base.supported_line
        if line >= 2.0 and self.goal3_funding == FundingState.NOT_REQUIRED:
            raise ValueError("goal3 funding cannot be NOT_REQUIRED for O2.0+")
        if line >= 3.0 and self.goal4_funding == FundingState.NOT_REQUIRED:
            raise ValueError("goal4 funding cannot be NOT_REQUIRED for O3.0+")
        if line < 3.0:
            if self.goal4_funding != FundingState.NOT_REQUIRED:
                raise ValueError("goal4 funding must be NOT_REQUIRED below O3.0")
            if self.goal4_funding_source != FundingSource.NONE:
                raise ValueError("goal4 funding source must be NONE below O3.0")

        for state, source, label in (
            (self.goal3_funding, self.goal3_funding_source, "goal3"),
            (self.goal4_funding, self.goal4_funding_source, "goal4"),
        ):
            if state in {FundingState.VERIFIED, FundingState.PARTIAL} and source == FundingSource.NONE:
                raise ValueError(f"{label} funding requires a non-NONE source")
            if state in {FundingState.NONE, FundingState.NOT_REQUIRED} and source != FundingSource.NONE:
                raise ValueError(f"{label} funding source must be NONE when state={state.name}")

        self._validate_source_integrity(
            self.goal3_funding, self.goal3_funding_source, "goal3"
        )
        if self.goal4_funding != FundingState.NOT_REQUIRED:
            self._validate_source_integrity(
                self.goal4_funding, self.goal4_funding_source, "goal4"
            )

    def _validate_source_integrity(
        self,
        state: FundingState,
        source: FundingSource,
        label: str,
    ) -> None:
        if state != FundingState.VERIFIED:
            return

        base = self.base
        weaker_route = min(base.home_route, base.away_route)

        if source == FundingSource.CARRIER:
            if not (
                base.carrier == CarrierStrength.STRONG
                and base.carrier_self_fund
                and base.independent_upper_tail
                and not base.material_suppression
            ):
                raise ValueError(
                    f"{label} VERIFIED CARRIER source lacks strong self-funded upper-tail proof"
                )

        if source == FundingSource.SECOND_ROUTE:
            if not (
                self.second_route_role == SecondRouteRole.BURDEN_CONTRIBUTING
                and weaker_route >= RouteStrength.USABLE
                and not base.failure_attacks_route
            ):
                raise ValueError(
                    f"{label} VERIFIED SECOND_ROUTE source lacks burden-contributing usable second route"
                )

        if source == FundingSource.FORCED_CHAOS:
            if not self.forced_chaos_verified:
                raise ValueError(
                    f"{label} VERIFIED FORCED_CHAOS source lacks C3 forced-chaos verification"
                )

        if source == FundingSource.MIXED:
            contributors = 0
            if (
                base.carrier == CarrierStrength.STRONG
                and base.carrier_self_fund
                and base.independent_upper_tail
            ):
                contributors += 1
            if (
                self.second_route_role == SecondRouteRole.BURDEN_CONTRIBUTING
                and weaker_route >= RouteStrength.USABLE
            ):
                contributors += 1
            if self.forced_chaos_verified:
                contributors += 1
            if contributors < 2:
                raise ValueError(
                    f"{label} VERIFIED MIXED source requires at least two credible contributors"
                )


@dataclass(frozen=True)
class Quote:
    line: float
    odds: float

    def __post_init__(self) -> None:
        _validate_quarter_line(self.line)
        if self.odds <= 1.0:
            raise ValueError("decimal odds must be > 1.0")


@dataclass(frozen=True)
class DecisionContext:
    board_state: BoardState
    official_follow_lane: FollowLane
    step2_authorization: Step2Authorization
    thesis_state: ThesisState
    quote: Quote

    xi_status: XiStatus
    post_xi_research_status: PostXiResearchStatus
    h2h_review_status: H2HReviewStatus
    h2h_rechecked: bool
    completion_rechecked: bool

    top_ranked_focus: bool
    primary_mechanism_intact: bool
    wait_reachable: bool
    wait_requires_negative_info: bool
    material_veto: bool


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
        int(a.burden_completion_quality),
        int(a.continuation_quality),
        -int(a.burden_stall_risk),
        upper_tail_self_fund,
        int(a.carrier),
        int(a.opponent_leakage),
        int(a.burden_protection),
        lower_burden,
        int(a.route_reliability),
        int(a.chance_quality),
        int(a.failure_resistance),
        int(a.evidence_confidence),
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


def c3_required_funding(a: C3PolicyAssessment) -> FundingState:
    """Return the weakest funding state required to clear the C3 burden.

    O3.0+ requires a credible path through both goal 3 and goal 4, so the
    weaker of the two funding states governs.
    """
    if a.base.supported_line >= 3.0:
        return min(a.goal3_funding, a.goal4_funding)
    return a.goal3_funding


def c3_ranking_key(a: C3PolicyAssessment) -> tuple[int, ...]:
    """C3 burden-funding-first ranking. Two-sidedness has no direct bonus."""

    base = a.base
    required = c3_required_funding(a)
    source_independence = int(
        (
            a.goal3_funding_source == FundingSource.MIXED
            or a.goal4_funding_source == FundingSource.MIXED
        )
    )
    self_funded_upper_tail = int(
        base.carrier_self_fund and base.independent_upper_tail
    )
    contributing_second_route = int(
        a.second_route_role == SecondRouteRole.BURDEN_CONTRIBUTING
    )
    lower_burden = -round(base.supported_line * 4)

    return (
        int(required),
        -int(a.control_endpoint_risk),
        source_independence,
        self_funded_upper_tail,
        contributing_second_route,
        int(base.failure_resistance),
        int(base.route_reliability),
        int(base.chance_quality),
        int(base.evidence_confidence),
        int(base.burden_protection),
        lower_burden,
    )


def rank_assessments_c3(
    items: Iterable[C3PolicyAssessment],
) -> list[C3PolicyAssessment]:
    return sorted(
        items,
        key=lambda item: (c3_ranking_key(item), item.base.match_id),
        reverse=True,
    )


def c3_board_state(a: C3PolicyAssessment) -> BoardState:
    base = a.base
    required = c3_required_funding(a)

    if base.material_suppression or base.failure_attacks_route:
        return BoardState.PASS
    if required in {FundingState.NONE, FundingState.NOT_REQUIRED}:
        return BoardState.PASS
    if a.control_endpoint_risk == Grade.HIGH:
        forced_chaos_escape = (
            a.forced_chaos_verified
            and required == FundingState.VERIFIED
            and (
                a.goal3_funding_source in {FundingSource.FORCED_CHAOS, FundingSource.MIXED}
                or a.goal4_funding_source in {FundingSource.FORCED_CHAOS, FundingSource.MIXED}
            )
        )
        return BoardState.WATCH if forced_chaos_escape else BoardState.PASS

    if (
        required == FundingState.VERIFIED
        and a.control_endpoint_risk == Grade.LOW
        and base.route_reliability >= Grade.MEDIUM
        and base.evidence_confidence == Grade.HIGH
    ):
        return BoardState.FOCUS

    return BoardState.WATCH


def c3_shadow_lane(a: C3PolicyAssessment, state: BoardState) -> FollowLane:
    base = a.base
    required = c3_required_funding(a)

    if state == BoardState.FOCUS:
        if (
            required == FundingState.VERIFIED
            and a.control_endpoint_risk == Grade.LOW
            and base.failure_resistance == Grade.HIGH
            and base.evidence_confidence == Grade.HIGH
            and base.supported_line <= 3.0
        ):
            return FollowLane.FOLLOW
        return FollowLane.RESERVE

    if state == BoardState.WATCH and (
        required == FundingState.PARTIAL
        or a.control_endpoint_risk == Grade.MEDIUM
    ):
        return FollowLane.RESERVE

    return FollowLane.STOP


def follow_through_lane(
    a: MatchAssessment,
    board_state: BoardState,
) -> FollowLane:
    """Burden-completion follow-through gate.

    FOLLOW no longer requires two usable scoring routes. A match may clear via:
    - TWO_SIDED: two usable routes with at least one STRONG route;
    - CARRIER_LED: one STRONG route plus a self-funding STRONG carrier,
      independent upper-tail proof and opponent leakage;
    - FORCED_CHAOS: verified football/incentive persistence that gives the
      match a credible continuation path.

    In every case the selector asks where the goal that clears the protected
    burden comes from. HIGH stall risk is a hard STOP for routine follow-up.
    """

    require_c_completion(a)

    if board_state != BoardState.FOCUS:
        return FollowLane.STOP

    if a.material_suppression or a.failure_attacks_route:
        return FollowLane.STOP

    if a.burden_stall_risk == Grade.HIGH:
        return FollowLane.STOP

    if a.supported_line > 3.0:
        return FollowLane.STOP

    common = (
        a.carrier == CarrierStrength.STRONG
        and a.route_reliability == Grade.HIGH
        and a.chance_quality >= Grade.MEDIUM
        and a.evidence_confidence == Grade.HIGH
    )
    if not common:
        return FollowLane.STOP

    two_sided = (
        a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
        and a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
    )

    carrier_led = (
        a.completion_mode in {CompletionMode.CARRIER_LED, CompletionMode.MIXED}
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier_self_fund
        and a.independent_upper_tail
        and a.opponent_leakage >= Grade.MEDIUM
    )

    forced_chaos = (
        a.completion_mode in {CompletionMode.FORCED_CHAOS, CompletionMode.MIXED}
        and max(a.home_route, a.away_route) >= RouteStrength.USABLE
        and a.continuation_quality == Grade.HIGH
    )

    if not (two_sided or carrier_led or forced_chaos):
        return FollowLane.STOP

    if (
        a.burden_completion_quality == Grade.HIGH
        and a.continuation_quality == Grade.HIGH
        and a.failure_resistance == Grade.HIGH
        and a.burden_stall_risk == Grade.LOW
    ):
        return FollowLane.FOLLOW

    if (
        a.burden_completion_quality >= Grade.MEDIUM
        and a.continuation_quality >= Grade.MEDIUM
        and a.failure_resistance >= Grade.MEDIUM
        and a.burden_protection == Grade.HIGH
    ):
        return FollowLane.RESERVE

    return FollowLane.STOP


def c2_selection_floor(
    a: MatchAssessment,
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

    if two_route_clear or carrier_clear:
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


def _healthy_wait(ctx: DecisionContext) -> bool:
    return ctx.wait_reachable and not ctx.wait_requires_negative_info


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


def decide_c(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Deterministic Football C execution policy."""

    require_c_completion(a)
    _validate_step2_authorization(ctx, require_c_focus=True)

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary scoring mechanism not intact")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

    if a.burden_stall_risk == Grade.HIGH:
        return Decision(Action.PASS, "current burden stall risk is HIGH")

    if a.burden_completion_quality == Grade.LOW:
        return Decision(Action.PASS, "current burden-completion quality is LOW")

    if a.continuation_quality == Grade.LOW:
        return Decision(Action.PASS, "current continuation quality is LOW")

    at_or_below = ctx.quote.line <= a.supported_line + 1e-9

    if at_or_below:
        if ctx.quote.odds >= 1.65:
            return Decision(Action.BET, "supported/protected line at normal price")

        if (
            1.60 <= ctx.quote.odds < 1.65
            and ctx.board_state == BoardState.FOCUS
            and ctx.top_ranked_focus
        ):
            return Decision(Action.BET, "top-focus soft-zone price")

        if _healthy_wait(ctx):
            return Decision(Action.WAIT, "price blocker with healthy reachable wait")

        return Decision(Action.PASS, "price unacceptable without healthy wait path")

    if _healthy_wait(ctx):
        return Decision(
            Action.WAIT,
            "market above supported burden; healthy target reachable",
        )

    return Decision(
        Action.PASS,
        "unsupported burden and no healthy reachable wait",
    )


def c2_bridge_eligibility(
    a: MatchAssessment,
    ctx: DecisionContext,
) -> tuple[bool, tuple[str, ...]]:
    """Check the text C2 Focus Market-Gap Bridge deterministically."""

    reasons: list[str] = []
    gap = round(ctx.quote.line - a.supported_line, 10)
    floor, _ = c2_selection_floor(a)

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

    return not reasons, tuple(reasons)


def decide_c2(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Deterministic C2 shadow execution policy."""

    _validate_step2_authorization(ctx, require_c_focus=False)

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary scoring mechanism not intact")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

    floor, _ = c2_selection_floor(a)
    if floor != SelectionFloor.CLEAR:
        return Decision(Action.PASS, "C2 selection-quality floor not clear")

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

    bridge_ok, _ = c2_bridge_eligibility(a, ctx)
    if bridge_ok:
        gap = round(ctx.quote.line - a.supported_line, 2)
        return Decision(
            Action.BET,
            f"FOCUS MARKET-GAP BRIDGE +{gap:.2f}",
            bridge_used=True,
        )

    if _healthy_wait(ctx):
        return Decision(
            Action.WAIT,
            "above burden; bridge fails but healthy target reachable",
        )

    return Decision(
        Action.PASS,
        "above burden; bridge fails and wait is unrealistic",
    )


def decide_c3(a: C3PolicyAssessment, ctx: DecisionContext) -> Decision:
    """C3 shadow execution: funding integrity first, same price policy as C."""

    _validate_step2_authorization(ctx, require_c_focus=False)

    base = a.base
    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")
    if not ctx.primary_mechanism_intact:
        return Decision(Action.PASS, "primary funding mechanism not intact")
    if ctx.material_veto or base.material_suppression or base.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")
    if c3_required_funding(a) != FundingState.VERIFIED:
        return Decision(Action.PASS, "required clearing-goal funding not VERIFIED")
    if a.control_endpoint_risk != Grade.LOW:
        return Decision(Action.PASS, "control-endpoint risk is not LOW")
    if ctx.board_state != BoardState.FOCUS:
        return Decision(Action.PASS, "frozen C3 direct shadow BET requires C3-FOCUS")
    if c3_board_state(a) != BoardState.FOCUS:
        return Decision(Action.PASS, "current C3 burden-funding state is not FOCUS")

    at_or_below = ctx.quote.line <= base.supported_line + 1e-9

    if at_or_below:
        if ctx.quote.odds >= 1.65:
            return Decision(Action.BET, "C3 verified funding at supported/protected line")
        if (
            1.60 <= ctx.quote.odds < 1.65
            and ctx.top_ranked_focus
        ):
            return Decision(Action.BET, "C3 top-focus soft-zone price")
        if _healthy_wait(ctx):
            return Decision(Action.WAIT, "C3 price blocker with healthy reachable wait")
        return Decision(Action.PASS, "C3 price unacceptable without healthy wait path")

    if _healthy_wait(ctx):
        return Decision(
            Action.WAIT,
            "market above C3 supported burden; funding intact and target reachable",
        )

    return Decision(Action.PASS, "above C3 burden and wait unrealistic")


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
