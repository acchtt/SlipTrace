from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Iterable

from core import Settlement, settle_over


SETTLEMENT_VALUE = {
    Settlement.WIN: 1.0,
    Settlement.HALF_WIN: 0.5,
    Settlement.PUSH: 0.0,
    Settlement.HALF_LOSS: -0.5,
    Settlement.LOSS: -1.0,
}

GRADE = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
ROUTE = {"WEAK": 0, "USABLE": 1, "STRONG": 2}
CARRIER = {"NONE": 0, "USABLE": 1, "STRONG": 2}

TRACE_FACTORS = (
    "burden_completion_quality",
    "continuation_quality",
    "burden_stall_risk",
    "carrier_self_fund",
    "independent_upper_tail",
    "independent_second_route",
    "failure_attacks_route",
    "material_suppression",
)

ABLATION_FACTORS = (
    "burden_completion_quality",
    "continuation_quality",
    "burden_stall_risk",
    "carrier_self_fund_upper_tail",
    "carrier",
    "opponent_leakage",
    "burden_protection",
    "supported_line",
    "route_reliability",
    "chance_quality",
    "failure_resistance",
    "evidence_confidence",
    "xi_robustness",
    "independent_route_quality",
)


@dataclass(frozen=True)
class CalibrationObservation:
    observation_id: str
    board_id: str
    match_id: str
    competition: str
    kickoff_ict: str
    c_rank: int
    lane: str
    supported_line: float
    home_route: str
    away_route: str
    carrier: str
    carrier_self_fund: bool
    independent_upper_tail: bool
    route_reliability: str
    independent_route_quality: str
    chance_quality: str
    failure_resistance: str
    xi_robustness: str
    evidence_confidence: str
    burden_protection: str
    completion_mode: str
    burden_completion_quality: str
    continuation_quality: str
    opponent_leakage: str
    burden_stall_risk: str
    failure_attacks_route: bool
    material_suppression: bool
    total_goals: int
    completion_materialized: str
    continuation_materialized: str
    stall_endpoint_observed: str
    eligible: bool = True
    contamination_reason: str = ""


def _choice(value: str, allowed: dict[str, int] | set[str], field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    key = value.strip().upper().replace("-", "_").replace(" ", "_")
    choices = set(allowed)
    if key not in choices:
        raise ValueError(f"invalid {field}={value!r}; allowed={sorted(choices)}")
    return key


def _bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{field} must be boolean")
    return value


def _number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be numeric")
    return float(value)


def _integer(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{field} must be integer")
    return value


def parse_observation(obj: dict[str, Any]) -> CalibrationObservation:
    required = (
        "observation_id", "board_id", "match_id", "competition", "kickoff_ict",
        "c_rank", "lane", "supported_line", "home_route", "away_route",
        "carrier", "carrier_self_fund", "independent_upper_tail",
        "route_reliability", "independent_route_quality", "chance_quality",
        "failure_resistance", "xi_robustness", "evidence_confidence",
        "burden_protection", "completion_mode", "burden_completion_quality",
        "continuation_quality", "opponent_leakage", "burden_stall_risk",
        "failure_attacks_route", "material_suppression", "total_goals",
        "completion_materialized", "continuation_materialized",
        "stall_endpoint_observed",
    )
    missing = [key for key in required if key not in obj]
    if missing:
        raise ValueError(f"missing calibration fields: {', '.join(missing)}")

    for key in ("observation_id", "board_id", "match_id", "competition", "kickoff_ict"):
        if not isinstance(obj[key], str) or not obj[key].strip():
            raise ValueError(f"{key} must be a non-empty string")

    return CalibrationObservation(
        observation_id=obj["observation_id"].strip(),
        board_id=obj["board_id"].strip(),
        match_id=obj["match_id"].strip(),
        competition=obj["competition"].strip(),
        kickoff_ict=obj["kickoff_ict"].strip(),
        c_rank=_integer(obj["c_rank"], "c_rank"),
        lane=_choice(obj["lane"], {"FOLLOW", "RESERVE", "STOP"}, "lane"),
        supported_line=_number(obj["supported_line"], "supported_line"),
        home_route=_choice(obj["home_route"], ROUTE, "home_route"),
        away_route=_choice(obj["away_route"], ROUTE, "away_route"),
        carrier=_choice(obj["carrier"], CARRIER, "carrier"),
        carrier_self_fund=_bool(obj["carrier_self_fund"], "carrier_self_fund"),
        independent_upper_tail=_bool(obj["independent_upper_tail"], "independent_upper_tail"),
        route_reliability=_choice(obj["route_reliability"], GRADE, "route_reliability"),
        independent_route_quality=_choice(obj["independent_route_quality"], GRADE, "independent_route_quality"),
        chance_quality=_choice(obj["chance_quality"], GRADE, "chance_quality"),
        failure_resistance=_choice(obj["failure_resistance"], GRADE, "failure_resistance"),
        xi_robustness=_choice(obj["xi_robustness"], GRADE, "xi_robustness"),
        evidence_confidence=_choice(obj["evidence_confidence"], GRADE, "evidence_confidence"),
        burden_protection=_choice(obj["burden_protection"], GRADE, "burden_protection"),
        completion_mode=_choice(obj["completion_mode"], {"NONE", "TWO_SIDED", "CARRIER_LED", "FORCED_CHAOS", "MIXED"}, "completion_mode"),
        burden_completion_quality=_choice(obj["burden_completion_quality"], GRADE, "burden_completion_quality"),
        continuation_quality=_choice(obj["continuation_quality"], GRADE, "continuation_quality"),
        opponent_leakage=_choice(obj["opponent_leakage"], GRADE, "opponent_leakage"),
        burden_stall_risk=_choice(obj["burden_stall_risk"], GRADE, "burden_stall_risk"),
        failure_attacks_route=_bool(obj["failure_attacks_route"], "failure_attacks_route"),
        material_suppression=_bool(obj["material_suppression"], "material_suppression"),
        total_goals=_integer(obj["total_goals"], "total_goals"),
        completion_materialized=_choice(obj["completion_materialized"], {"YES", "NO", "UNKNOWN"}, "completion_materialized"),
        continuation_materialized=_choice(obj["continuation_materialized"], {"YES", "NO", "UNKNOWN"}, "continuation_materialized"),
        stall_endpoint_observed=_choice(obj["stall_endpoint_observed"], {"YES", "NO", "UNKNOWN"}, "stall_endpoint_observed"),
        eligible=_bool(obj.get("eligible", True), "eligible"),
        contamination_reason=str(obj.get("contamination_reason", "")).strip(),
    )


def trace_contributions(a: CalibrationObservation) -> dict[str, float]:
    weaker_route = min(ROUTE[a.home_route], ROUTE[a.away_route])
    second_route = {0: 0.0, 1: 0.5, 2: 1.0}[weaker_route]
    completion = {0: 0.0, 1: 1.0, 2: 2.0}[GRADE[a.burden_completion_quality]]
    continuation = {0: 0.0, 1: 1.0, 2: 2.0}[GRADE[a.continuation_quality]]
    stall = {0: 2.0, 1: 0.0, 2: -2.0}[GRADE[a.burden_stall_risk]]
    return {
        "burden_completion_quality": completion,
        "continuation_quality": continuation,
        "burden_stall_risk": stall,
        "carrier_self_fund": 1.0 if a.carrier_self_fund else 0.0,
        "independent_upper_tail": 1.0 if a.independent_upper_tail else 0.0,
        "independent_second_route": second_route,
        "failure_attacks_route": -1.0 if a.failure_attacks_route else 0.0,
        "material_suppression": -1.0 if a.material_suppression else 0.0,
    }


def trace_score(a: CalibrationObservation) -> float:
    return sum(trace_contributions(a).values())


def c_ranking_key(a: CalibrationObservation) -> tuple[int, ...]:
    upper_tail_self_fund = int(a.carrier_self_fund and a.independent_upper_tail)
    lower_burden = -round(a.supported_line * 4)
    return (
        GRADE[a.burden_completion_quality],
        GRADE[a.continuation_quality],
        -GRADE[a.burden_stall_risk],
        upper_tail_self_fund,
        CARRIER[a.carrier],
        GRADE[a.opponent_leakage],
        GRADE[a.burden_protection],
        lower_burden,
        GRADE[a.route_reliability],
        GRADE[a.chance_quality],
        GRADE[a.failure_resistance],
        GRADE[a.evidence_confidence],
        GRADE[a.xi_robustness],
        GRADE[a.independent_route_quality],
    )


def ablated_ranking_key(a: CalibrationObservation, factor: str) -> tuple[int, ...]:
    if factor not in ABLATION_FACTORS:
        raise ValueError(f"unsupported ablation factor: {factor}")
    labels = list(ABLATION_FACTORS)
    values = list(c_ranking_key(a))
    idx = labels.index(factor)
    return tuple(values[:idx] + values[idx + 1 :])


def settlement_value(a: CalibrationObservation) -> tuple[str, float]:
    settlement, _ = settle_over(a.supported_line, a.total_goals)
    return settlement.value.replace(" ", "_"), SETTLEMENT_VALUE[settlement]


def observation_result(a: CalibrationObservation) -> dict[str, Any]:
    settlement, value = settlement_value(a)
    contributions = trace_contributions(a)
    return {
        "observation_id": a.observation_id,
        "board_id": a.board_id,
        "match_id": a.match_id,
        "eligible": a.eligible,
        "contamination_reason": a.contamination_reason,
        "trace_score": trace_score(a),
        "trace_contributions": contributions,
        "support_settlement": settlement,
        "support_value": value,
        "goals_minus_supported_line": round(a.total_goals - a.supported_line, 2),
        "ranking_key": list(c_ranking_key(a)),
    }


def factor_bucket_stats(items: Iterable[CalibrationObservation], factor: str) -> dict[str, dict[str, float | int]]:
    buckets: dict[str, list[CalibrationObservation]] = defaultdict(list)
    for item in items:
        if not item.eligible:
            continue
        value = getattr(item, factor)
        buckets[str(value)].append(item)

    output: dict[str, dict[str, float | int]] = {}
    for value, rows in sorted(buckets.items()):
        outcomes = [settlement_value(row)[1] for row in rows]
        clears = sum(1 for x in outcomes if x > 0)
        fails = sum(1 for x in outcomes if x < 0)
        output[value] = {
            "n": len(rows),
            "support_clear_rate": round(clears / len(rows), 4),
            "support_fail_rate": round(fails / len(rows), 4),
            "average_support_value": round(sum(outcomes) / len(rows), 4),
            "average_goals_minus_line": round(sum(r.total_goals - r.supported_line for r in rows) / len(rows), 4),
        }
    return output


def same_kickoff_ablation(items: Iterable[CalibrationObservation], factor: str) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[CalibrationObservation]] = defaultdict(list)
    for item in items:
        if item.eligible:
            groups[(item.board_id, item.kickoff_ict)].append(item)

    changes: list[dict[str, Any]] = []
    for (board_id, kickoff), rows in groups.items():
        if len(rows) < 2:
            continue
        original = max(rows, key=lambda x: (c_ranking_key(x), x.match_id))
        ablated = max(rows, key=lambda x: (ablated_ranking_key(x, factor), x.match_id))
        if original.match_id == ablated.match_id:
            continue
        original_settlement, original_value = settlement_value(original)
        ablated_settlement, ablated_value = settlement_value(ablated)
        changes.append({
            "board_id": board_id,
            "kickoff_ict": kickoff,
            "factor": factor,
            "original_top": original.match_id,
            "original_settlement": original_settlement,
            "original_support_value": original_value,
            "ablated_top": ablated.match_id,
            "ablated_settlement": ablated_settlement,
            "ablated_support_value": ablated_value,
            "ablation_delta": round(ablated_value - original_value, 2),
        })
    return changes


def analyze(items: Iterable[CalibrationObservation]) -> dict[str, Any]:
    rows = list(items)
    eligible = [x for x in rows if x.eligible]
    return {
        "observation_count": len(rows),
        "eligible_count": len(eligible),
        "observations": [observation_result(x) for x in rows],
        "factor_buckets": {
            factor: factor_bucket_stats(eligible, factor)
            for factor in (
                "burden_completion_quality",
                "continuation_quality",
                "burden_stall_risk",
                "carrier_self_fund",
                "independent_upper_tail",
                "completion_mode",
                "failure_resistance",
            )
        },
        "ablations": {
            factor: same_kickoff_ablation(eligible, factor)
            for factor in ABLATION_FACTORS
        },
    }
