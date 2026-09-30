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


class BoardState(IntEnum):
    PASS = 0
    WATCH = 1
    FOCUS = 2


class FollowLane(Enum):
    STOP = "STOP"
    RESERVE = "RESERVE"
    FOLLOW = "FOLLOW"


class ThesisState(IntEnum):
    BROKEN = 0
    DEGRADED = 1
    PRESERVED = 2


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

    supported_line: float

    carrier_self_fund: bool = False
    independent_upper_tail: bool = False
    failure_attacks_route: bool = False
    material_suppression: bool = False

    def __post_init__(self) -> None:
        if self.supported_line < 0:
            raise ValueError("supported_line must be non-negative")
        _validate_quarter_line(self.supported_line)


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
    thesis_state: ThesisState
    quote: Quote

    top_ranked_focus: bool = False
    primary_mechanism_intact: bool = True

    wait_reachable: bool = False
    wait_requires_negative_info: bool = False

    material_veto: bool = False


@dataclass(frozen=True)
class Decision:
    action: Action
    reason: str
    bridge_used: bool = False


def _validate_quarter_line(line: float) -> None:
    quarter = round(line * 4)
    if abs(line * 4 - quarter) > 1e-9:
        raise ValueError("Asian total line must use 0.25-goal increments")


def ranking_key(a: MatchAssessment) -> tuple[int, ...]:
    """Return the deterministic lexicographic Football C ranking key.

    Higher is better. This mirrors the text model's stated ordering instead of
    inventing a weighted probability score.
    """

    return (
        int(a.route_reliability),
        int(a.independent_route_quality),
        int(a.carrier),
        int(a.chance_quality),
        int(a.failure_resistance),
        int(a.xi_robustness),
        int(a.evidence_confidence),
        int(a.burden_protection),
    )


def rank_assessments(items: Iterable[MatchAssessment]) -> list[MatchAssessment]:
    return sorted(
        items,
        key=lambda item: (ranking_key(item), item.match_id),
        reverse=True,
    )


def follow_through_lane(
    a: MatchAssessment,
    board_state: BoardState,
) -> FollowLane:
    """Operational follow-through gate.

    This does not alter the Football C board state. It limits which frozen
    candidates consume XI/odds/live attention.

    FOLLOW requires:
    - official C-FOCUS;
    - two usable routes with at least one strong route;
    - STRONG carrier;
    - HIGH route reliability, independent route quality, chance quality,
      failure resistance and evidence confidence;
    - supported burden <= 3.0;
    - no material suppression / route-attacking failure.

    RESERVE is the same core structure but permits MEDIUM failure resistance
    when burden protection is HIGH.

    Everything else remains frozen for audit but stops routine follow-through.
    """

    if board_state != BoardState.FOCUS:
        return FollowLane.STOP

    structural = (
        a.home_route >= RouteStrength.USABLE
        and a.away_route >= RouteStrength.USABLE
        and max(a.home_route, a.away_route) == RouteStrength.STRONG
        and a.carrier == CarrierStrength.STRONG
        and a.route_reliability == Grade.HIGH
        and a.independent_route_quality == Grade.HIGH
        and a.chance_quality == Grade.HIGH
        and a.evidence_confidence == Grade.HIGH
        and a.supported_line <= 3.0
        and not a.failure_attacks_route
        and not a.material_suppression
    )

    if not structural:
        return FollowLane.STOP

    if a.failure_resistance == Grade.HIGH:
        return FollowLane.FOLLOW

    if (
        a.failure_resistance == Grade.MEDIUM
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


def decide_c(a: MatchAssessment, ctx: DecisionContext) -> Decision:
    """Deterministic Football C execution policy."""

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

    if ctx.material_veto or a.material_suppression or a.failure_attacks_route:
        return Decision(Action.PASS, "material football veto remains")

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

    if ctx.thesis_state == ThesisState.BROKEN:
        return Decision(Action.PASS, "thesis broken")

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
