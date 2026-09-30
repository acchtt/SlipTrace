from __future__ import annotations

import json
from typing import Any

from core import (
    BoardState,
    CarrierStrength,
    DecisionContext,
    FollowLane,
    Grade,
    MatchAssessment,
    Quote,
    RouteStrength,
    ThesisState,
    c2_selection_floor,
    decide_c,
    decide_c2,
    follow_through_lane,
    rank_assessments,
    ranking_key,
)


SCHEMA_VERSION = "football-engine-v1"
MAX_FOLLOW = 6
MAX_RESERVE = 4


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


def _number(obj: dict[str, Any], key: str) -> float:
    value = _required(obj, key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ContractError(f"{key} must be numeric")
    return float(value)


def parse_assessment(obj: dict[str, Any]) -> MatchAssessment:
    if not isinstance(obj, dict):
        raise ContractError("match must be an object")

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
        supported_line=_number(obj, "supported_line"),
        carrier_self_fund=_bool(obj, "carrier_self_fund"),
        independent_upper_tail=_bool(obj, "independent_upper_tail"),
        failure_attacks_route=_bool(obj, "failure_attacks_route"),
        material_suppression=_bool(obj, "material_suppression"),
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
    if model not in {"c", "c2"}:
        raise ContractError("model must be 'c' or 'c2'")

    raw_matches = _required(payload, "matches")
    if not isinstance(raw_matches, list) or not raw_matches:
        raise ContractError("matches must be a non-empty array")

    parsed = [parse_assessment(item) for item in raw_matches]
    ranked = rank_assessments(parsed)

    output = []
    follow_used = 0
    reserve_used = 0

    for rank, item in enumerate(ranked, start=1):
        raw = next(x for x in raw_matches if str(x["match_id"]) == item.match_id)
        row: dict[str, Any] = {
            "rank": rank,
            "match_id": item.match_id,
            "ranking_key": list(ranking_key(item)),
            "supported_line": item.supported_line,
        }

        state = None
        if "board_state" in raw:
            state = _enum(BoardState, raw["board_state"], "board_state")
            row["board_state"] = state.name

        if model == "c" and state is not None:
            base_lane = follow_through_lane(item, state)
            lane = FollowLane.STOP

            if base_lane == FollowLane.FOLLOW:
                if follow_used < MAX_FOLLOW:
                    lane = FollowLane.FOLLOW
                    follow_used += 1
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

        output.append(row)

    result = {
        "schema_version": SCHEMA_VERSION,
        "stage": "board_result",
        "model": model,
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

    return result


def run_decision(payload: dict[str, Any]) -> dict[str, Any]:
    _check_envelope(payload, "decision")

    model = str(payload.get("model", "")).lower()
    if model not in {"c", "c2"}:
        raise ContractError("model must be 'c' or 'c2'")

    raw_match = _required(payload, "match")
    a = parse_assessment(raw_match)

    ctx_obj = _required(payload, "context")
    if not isinstance(ctx_obj, dict):
        raise ContractError("context must be an object")

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
        top_ranked_focus=_bool(ctx_obj, "top_ranked_focus"),
        primary_mechanism_intact=_bool(
            ctx_obj, "primary_mechanism_intact", True
        ),
        wait_reachable=_bool(ctx_obj, "wait_reachable"),
        wait_requires_negative_info=_bool(
            ctx_obj, "wait_requires_negative_info"
        ),
        material_veto=_bool(ctx_obj, "material_veto"),
    )

    decision = decide_c(a, ctx) if model == "c" else decide_c2(a, ctx)
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "stage": "decision_result",
        "model": model,
        "match_id": a.match_id,
        "action": decision.action.value,
        "reason": decision.reason,
        "bridge_used": decision.bridge_used,
    }

    if model == "c2":
        floor, reasons = c2_selection_floor(a)
        result["selection_floor"] = floor.value
        result["selection_floor_reasons"] = list(reasons)

    return result


def dumps(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)
