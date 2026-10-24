"""Zero-authority prospective Football C calibration ledger.

The ledger records frozen decisions and later settlements without feeding any
outcome into selection.  Builders reject hindsight fields at decision time and
settlement creates a new object rather than mutating the frozen record.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


SCHEMA = "football-c-calibration-v1"
OUTCOME_FIELDS = frozenset({
    "ft_score", "total_goals", "g3_reached", "g4_reached",
    "certified_burden_settlement", "evaluated_line_settlement",
    "act_settlement", "settled_at_utc",
})


def _base(match_id: str, evidence_epoch: str) -> dict[str, Any]:
    if not isinstance(match_id, str) or not match_id.strip():
        raise ValueError("calibration Match ID required")
    if not isinstance(evidence_epoch, str) or not evidence_epoch.strip():
        raise ValueError("calibration evidence epoch required")
    return {
        "schema_version": SCHEMA,
        "match_id": match_id.strip(),
        "evidence_epoch": evidence_epoch.strip(),
        "selection_authority": "ZERO",
        "automatic_threshold_learning": False,
    }


def sweep_records(receipt: dict[str, Any]) -> list[dict[str, Any]]:
    """Create one prospective record for every source-ledger fixture."""

    epoch = receipt["run_id"]
    rows = []
    for source in receipt.get("source_ledger", []):
        mid = source.get("match_id")
        if not isinstance(mid, str) or not mid.strip():
            continue
        lane = source.get("intake_lane")
        screen = source.get("goal_screen") or source.get("discovery_screen") or {}
        selected = lane in {"GOAL_PRIORITY", "GOAL_REVIEW", "CONTROL_REVIEW"}
        row = _base(mid, epoch)
        row.update({
            "sweep_state": lane,
            "goal_screen_state": screen.get("status"),
            "control_review": lane == "CONTROL_REVIEW",
            "compiled_board_state": None,
            "researcher_declared_board_state": None,
            "rank": None,
            "follow_lane": None,
            "goal3_funded": None,
            "goal4_funded": None,
            "goal5_funded": None,
            "goal6_funded": None,
            "certified_burden": None,
            "credible_tail_state": None,
            "robustness": None,
            "g3_endpoint_pressure": None,
            "upper_tail_pressure": None,
            "direct_act_ceiling": None,
            "screenshot_visible_ladder": [],
            "selected_evaluated_line": None,
            "selected_evaluated_odds": None,
            "decision": "REVIEW_ONLY" if selected else "SCREENED_OUT",
            "exception_flag": False,
            "pass_had_lower_supported_visible_line": False,
        })
        rows.append(row)
    return rows


def board_records(
    board: dict[str, Any],
    *,
    evidence_epoch: str,
    sweep_by_id: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Compile rank-time records without outcome or market authority."""

    output = []
    sweep_by_id = sweep_by_id or {}
    for item in board.get("matches", []):
        mid = item["match_id"]
        source = sweep_by_id.get(mid, {})
        row = _base(mid, evidence_epoch)
        state = item.get("board_state")
        row.update({
            "sweep_state": source.get("sweep_state"),
            "goal_screen_state": source.get("goal_screen_state"),
            "control_review": bool(source.get("control_review", False)),
            "compiled_board_state": state,
            "researcher_declared_board_state": item.get("declared_board_state"),
            "rank": item.get("rank"),
            "follow_lane": item.get("follow_lane"),
            "goal3_funded": item.get("goal3_funded"),
            "goal4_funded": item.get("goal4_funded"),
            "goal5_funded": item.get("goal5_funded"),
            "goal6_funded": item.get("goal6_funded"),
            "certified_burden": item.get("supported_line"),
            "credible_tail_state": item.get("credible_tail_state"),
            "robustness": item.get(
                "certificate_robustness",
                item.get("execution_strength"),
            ),
            "g3_endpoint_pressure": item.get("g3_endpoint_control_pressure"),
            "upper_tail_pressure": item.get("upper_tail_control_pressure"),
            "direct_act_ceiling": item.get("direct_act_ceiling"),
            "screenshot_visible_ladder": [],
            "selected_evaluated_line": None,
            "selected_evaluated_odds": None,
            "decision": (
                "PASS" if state == "PASS" else "REVIEW_ONLY"
            ),
            "exception_flag": False,
            "pass_had_lower_supported_visible_line": False,
        })
        output.append(row)
    return output


def with_quote_decision(
    record: dict[str, Any],
    *,
    visible_ladder: list[dict[str, float]],
    selected_line: float | None,
    selected_odds: float | None,
    decision: str,
    exception_flag: bool = False,
) -> dict[str, Any]:
    if record.get("settlement") is not None or any(k in record for k in OUTCOME_FIELDS):
        raise ValueError("cannot rewrite a settled calibration record")
    if decision not in {"ACT", "BOOK", "PASS", "REVIEW_ONLY", "SCREENED_OUT"}:
        raise ValueError("invalid calibration decision")
    updated = deepcopy(record)
    updated["screenshot_visible_ladder"] = deepcopy(visible_ladder)
    updated["selected_evaluated_line"] = selected_line
    updated["selected_evaluated_odds"] = selected_odds
    updated["decision"] = decision
    updated["exception_flag"] = bool(exception_flag)
    supported = updated.get("direct_act_ceiling")
    updated["pass_had_lower_supported_visible_line"] = bool(
        decision == "PASS"
        and isinstance(supported, (int, float))
        and any(float(q["line"]) <= float(supported) for q in visible_ladder)
        and isinstance(selected_line, (int, float))
        and float(selected_line) > float(supported)
    )
    return updated


def xi_record(
    c_input: dict[str, Any],
    football_result: dict[str, Any],
    quote_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create the decision-time zero-authority row emitted by /xi."""

    match_id = str(football_result["match_id"])
    epoch = c_input.get("evidence_epoch_id") or c_input.get("context", {}).get(
        "assessment_at_utc"
    )
    row = _base(match_id, str(epoch))
    context = c_input.get("context") or {}
    decision = "REVIEW_ONLY"
    visible: list[dict[str, float]] = []
    selected_line = selected_odds = None
    if quote_result is not None:
        raw_action = quote_result.get("action")
        decision = raw_action if raw_action in {"ACT", "BOOK", "PASS"} else "REVIEW_ONLY"
        visible = deepcopy(quote_result.get("visible_ladder") or [])
        selected_line = quote_result.get("selected_visible_line")
        selected_odds = quote_result.get("selected_visible_odds")
    row.update({
        "sweep_state": context.get("sweep_state"),
        "goal_screen_state": context.get("goal_screen_state"),
        "control_review": bool(context.get("control_review", False)),
        "compiled_board_state": football_result.get("rank_state_internal"),
        "researcher_declared_board_state": football_result.get("declared_board_state"),
        "rank": context.get("rank"),
        "follow_lane": context.get("official_follow_lane"),
        "goal3_funded": football_result.get("goal3_funded"),
        "goal4_funded": football_result.get("goal4_funded"),
        "goal5_funded": football_result.get("goal5_funded"),
        "goal6_funded": football_result.get("goal6_funded"),
        "certified_burden": football_result.get(
            "frozen_supported_line",
            football_result.get("supported_line"),
        ),
        "credible_tail_state": football_result.get("credible_tail_state"),
        "robustness": football_result.get(
            "certificate_robustness",
            football_result.get("execution_strength"),
        ),
        "g3_endpoint_pressure": football_result.get("g3_endpoint_control_pressure"),
        "upper_tail_pressure": football_result.get("upper_tail_control_pressure"),
        "direct_act_ceiling": football_result.get("direct_act_ceiling"),
        "screenshot_visible_ladder": visible,
        "selected_evaluated_line": selected_line,
        "selected_evaluated_odds": selected_odds,
        "decision": decision,
        "exception_flag": bool(context.get("exception_flag", False)),
        "pass_had_lower_supported_visible_line": bool(
            quote_result and quote_result.get("pass_had_lower_supported_visible_line")
        ),
    })
    return row


def asian_over_settlement(total_goals: int, line: float | None) -> str | None:
    if line is None:
        return None
    quarter = round(float(line) * 4)
    if abs(float(line) * 4 - quarter) > 1e-8:
        raise ValueError("settlement line must use 0.25 increments")
    if quarter % 2 == 0:
        legs = [float(line)]
    elif quarter % 4 == 1:
        legs = [float(line) - 0.25, float(line) + 0.25]
    else:
        legs = [float(line) - 0.25, float(line) + 0.25]
    states = ["WIN" if total_goals > leg else "PUSH" if total_goals == leg else "LOSS" for leg in legs]
    if all(state == "WIN" for state in states):
        return "WIN"
    if all(state == "LOSS" for state in states):
        return "LOSS"
    if all(state == "PUSH" for state in states):
        return "PUSH"
    if "WIN" in states and "PUSH" in states:
        return "HALF_WIN"
    if "LOSS" in states and "PUSH" in states:
        return "HALF_LOSS"
    return "HALF_WIN_HALF_LOSS"


def settle(
    record: dict[str, Any],
    *,
    home_goals: int,
    away_goals: int,
    settled_at_utc: str,
) -> dict[str, Any]:
    """Append outcome-only fields after settlement; never change prematch data."""

    if record.get("settlement") is not None:
        raise ValueError("calibration record already settled")
    if any(type(goal) is not int or goal < 0 for goal in (home_goals, away_goals)):
        raise ValueError("non-negative integer final goals required")
    updated = deepcopy(record)
    total = home_goals + away_goals
    evaluated = asian_over_settlement(total, record.get("selected_evaluated_line"))
    updated["settlement"] = {
        "settled_at_utc": settled_at_utc,
        "ft_score": f"{home_goals}-{away_goals}",
        "total_goals": total,
        "g3_reached": total >= 3,
        "g4_reached": total >= 4,
        "certified_burden_settlement": asian_over_settlement(
            total, record.get("certified_burden")
        ),
        "evaluated_line_settlement": evaluated,
        "act_settlement": evaluated if record.get("decision") == "ACT" else None,
    }
    return updated


def _rate(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 4) if denominator else None


def audit_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Return universal-denominator execution, PASS, screen and rank metrics."""

    settled = [row for row in records if isinstance(row.get("settlement"), dict)]
    acts = [row for row in settled if row.get("decision") == "ACT"]
    act_states = {state: 0 for state in ("WIN", "PUSH", "HALF_WIN", "HALF_LOSS", "LOSS")}
    for row in acts:
        state = row["settlement"].get("act_settlement")
        if state in act_states:
            act_states[state] += 1
    priced_passes = [
        row for row in settled
        if row.get("decision") == "PASS" and row.get("selected_evaluated_line") is not None
    ]
    pass_false_negatives = sum(
        row["settlement"].get("evaluated_line_settlement") in {"WIN", "HALF_WIN"}
        for row in priced_passes
    )
    screen_states = ("DISCOVERY_GOAL_QUALIFIED", "DISCOVERY_GOAL_REVIEW", "WATCH_GOAL_SIGNAL")
    screen = {}
    for state in screen_states:
        cohort = [row for row in settled if row.get("goal_screen_state") == state]
        screen[state] = {
            "count": len(cohort),
            "g3_reached": sum(row["settlement"]["g3_reached"] for row in cohort),
            "g4_reached": sum(row["settlement"]["g4_reached"] for row in cohort),
        }
    focus = [row for row in settled if row.get("compiled_board_state") == "FOCUS"]
    review = [row for row in settled if row.get("compiled_board_state") == "WATCH"]
    supported = [row for row in settled if row.get("certified_burden") is not None]
    def reached(row: dict[str, Any]) -> bool:
        return row["settlement"].get("certified_burden_settlement") in {"WIN", "PUSH", "HALF_WIN"}
    return {
        "record_count": len(records),
        "settled_count": len(settled),
        "execution": {
            "act_count": len(acts),
            "settlements": act_states,
            "act_clear_rate": _rate(
                act_states["WIN"] + act_states["PUSH"] + act_states["HALF_WIN"], len(acts)
            ),
            "average_evaluated_burden": (
                round(sum(float(row["selected_evaluated_line"]) for row in acts) / len(acts), 4)
                if acts else None
            ),
            "act_coverage": _rate(len(acts), len(settled)),
        },
        "pass": {
            "priced_pass_count": len(priced_passes),
            "correctly_rejected": len(priced_passes) - pass_false_negatives,
            "false_negatives": pass_false_negatives,
            "false_negative_rate": _rate(pass_false_negatives, len(priced_passes)),
            "lower_supported_visible_line_count": sum(
                bool(row.get("pass_had_lower_supported_visible_line")) for row in priced_passes
            ),
        },
        "screening": {
            "goal_priority_count": sum(row.get("sweep_state") == "GOAL_PRIORITY" for row in records),
            "goal_review_count": sum(row.get("sweep_state") == "GOAL_REVIEW" for row in records),
            "control_review_count": sum(bool(row.get("control_review")) for row in records),
            "terminal_negative_screen_count": sum(
                row.get("goal_screen_state") == "WATCH_GOAL_SIGNAL" and not row.get("control_review")
                for row in records
            ),
            "outcomes_by_screen_state": screen,
        },
        "ranking": {
            "focus_g3_rate": _rate(sum(row["settlement"]["g3_reached"] for row in focus), len(focus)),
            "review_only_g3_rate": _rate(sum(row["settlement"]["g3_reached"] for row in review), len(review)),
            "focus_g4_rate": _rate(sum(row["settlement"]["g4_reached"] for row in focus), len(focus)),
            "review_only_g4_rate": _rate(sum(row["settlement"]["g4_reached"] for row in review), len(review)),
            "supported_burden_reach": _rate(sum(reached(row) for row in supported), len(supported)),
            "top3_clearability": _rate(sum(reached(row) for row in supported if (row.get("rank") or 9999) <= 3), sum((row.get("rank") or 9999) <= 3 for row in supported)),
            "top5_clearability": _rate(sum(reached(row) for row in supported if (row.get("rank") or 9999) <= 5), sum((row.get("rank") or 9999) <= 5 for row in supported)),
            "certificate_depth_distribution": {
                str(line): sum(row.get("certified_burden") == line for row in records)
                for line in sorted({row.get("certified_burden") for row in records if row.get("certified_burden") is not None})
            },
            "robustness_distribution": {
                str(value): sum(row.get("robustness") == value for row in records)
                for value in sorted({row.get("robustness") for row in records if row.get("robustness") is not None}, key=str)
            },
        },
        "exceptions": [row["match_id"] for row in records if row.get("exception_flag")],
        "selection_authority": "ZERO",
    }
