#!/usr/bin/env python3
"""Matched C/C2 gate ablation. Never fabricates actions, prices or exposures.

C legacy comparator isolates the change in PR #92: previously selected
O2.0/O2.25 burdens bypassed goal-three funding. C2 sensitivity asks only
whether its pre-existing selection-quality floor clears without the added
C2 clearing-goal requirement. No shadow variant is an authorized BET.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from core import (
    CarrierStrength, CompletionMode, Grade, RouteStrength, SelectionFloor,
    c2_clearing_goal_funded, c2_selection_floor, clearing_goal_funded, settle_over,
)


class GateAuditError(ValueError):
    pass


def _timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise GateAuditError("prospective timestamp missing")
    try:
        time = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise GateAuditError("invalid prospective timestamp") from exc
    if time.tzinfo is None:
        raise GateAuditError("timestamp without timezone")
    return time


def _enum(factors: dict, key: str, kind: type):
    value = factors.get(key)
    try:
        return kind[value] if isinstance(value, str) else kind(value)
    except (KeyError, ValueError, TypeError) as exc:
        raise GateAuditError(f"{key} missing or invalid") from exc


def _bool(factors: dict, key: str) -> bool:
    value = factors.get(key)
    if not isinstance(value, bool):
        raise GateAuditError(f"{key} missing or not bool")
    return value


def _snapshot(factors: dict, model: str) -> SimpleNamespace:
    if not isinstance(factors, dict):
        raise GateAuditError("frozen_factors missing")
    data = {
        k: _enum(factors, k, RouteStrength)
        for k in ("home_route", "away_route")
    }
    data["carrier"] = _enum(factors, "carrier", CarrierStrength)
    for k in ("route_reliability", "chance_quality", "failure_resistance",
              "independent_route_quality"):
        data[k] = _enum(factors, k, Grade)
    for k in ("carrier_self_fund", "independent_upper_tail", "material_suppression",
              "failure_attacks_route"):
        data[k] = _bool(factors, k)
    if model == "c":
        data["completion_mode"] = _enum(factors, "completion_mode", CompletionMode)
        for k in ("burden_completion_quality", "continuation_quality",
                  "opponent_leakage", "burden_stall_risk"):
            data[k] = _enum(factors, k, Grade)
    return SimpleNamespace(**data)


def _gate(row: dict) -> dict:
    if not isinstance(row, dict):
        raise GateAuditError("record not object")
    match_id = row.get("match_id")
    epoch = row.get("evidence_epoch_id")
    model = row.get("model")
    if not isinstance(match_id, str) or not match_id.strip() or not isinstance(epoch, str) or not epoch.strip():
        raise GateAuditError("match_id and frozen evidence_epoch_id are required")
    if model not in ("c", "c2"):
        raise GateAuditError("model must be c or c2, retired models not admitted")
    if row.get("freeze_status") not in ("PROSPECTIVE_VERIFIED", "HISTORICAL_FROZEN_UNTIMED"):
        raise GateAuditError("freeze_status missing or unknown")
    prospective = row["freeze_status"] == "PROSPECTIVE_VERIFIED"
    if prospective:
        if _timestamp(row.get("frozen_at_utc")) >= _timestamp(row.get("kickoff_utc")):
            raise GateAuditError("frozen epoch is at/after kickoff")
    selected = row.get("selected_line")
    if isinstance(selected, bool) or not isinstance(selected, (int, float)):
        raise GateAuditError("selected_line must be a real frozen Asian total")
    line = float(selected)
    # Validate supported line without manufacturing an executable quote.
    try:
        settle_over(line, 0)
    except ValueError as exc:
        raise GateAuditError(f"invalid selected_line: {exc}") from exc
    snapshot = _snapshot(row.get("frozen_factors"), model)
    if model == "c":
        current = clearing_goal_funded(snapshot, line)
        # Frozen pre-#92 C source: line < 2.5 was an unconditional goal3 pass.
        comparator = (line < 2.5) or current
        comparator_name = "C_PRE_PR92_LINE_LT_2_5"
    else:
        current = c2_clearing_goal_funded(snapshot, line)
        comparator = c2_selection_floor(snapshot)[0] == SelectionFloor.CLEAR
        comparator_name = "C2_SELECTION_FLOOR_WITHOUT_EXTRA_GOAL_GATE"
    total_goals = row.get("observed_ft_total_goals")
    settled = None
    if total_goals is not None:
        if isinstance(total_goals, bool) or not isinstance(total_goals, int) or total_goals < 0:
            raise GateAuditError("observed_ft_total_goals invalid")
        settled = settle_over(line, total_goals)[0].value
    return {
        "match_id": match_id,
        "evidence_epoch_id": epoch,
        "model": model,
        "freeze_status": row["freeze_status"],
        "line": line,
        "production_goal_gate": current,
        "less_restrictive_comparator_gate": comparator,
        "comparator_name": comparator_name,
        "gate_disagreement": not current and comparator,
        "observed_counterfactual_settlement": settled,
        "bet_authorized": False,
        "actual_user_bet": None,
    }


def audit(payload: dict[str, Any]) -> dict:
    if not isinstance(payload, dict) or payload.get("schema_version") != "football-goal-gate-ablation-v1":
        raise GateAuditError("schema_version invalid")
    rows = payload.get("frozen_rows")
    if not isinstance(rows, list):
        raise GateAuditError("frozen_rows must be an array")
    result = []
    keys: set[tuple[str, str, str]] = set()
    for row in rows:
        item = _gate(row)
        key = (item["match_id"], item["evidence_epoch_id"], item["model"])
        if key in keys:
            raise GateAuditError(f"duplicate model/fixture/epoch: {key}")
        keys.add(key)
        result.append(item)
    groups = defaultdict(dict)
    for item in result:
        groups[(item["match_id"], item["evidence_epoch_id"])][item["model"]] = item
    actual_pairs = [
        group for group in groups.values()
        if set(group) == {"c", "c2"}
        and all(a["freeze_status"] == "PROSPECTIVE_VERIFIED" for a in group.values())
    ]
    counts: dict = {}
    for model in ("c", "c2"):
        subset = [item for item in result if item["model"] == model]
        counts[model] = {
            "n": len(subset),
            "current_gate_true": sum(bool(x["production_goal_gate"]) for x in subset),
            "comparator_gate_true": sum(bool(x["less_restrictive_comparator_gate"]) for x in subset),
            "gate_disagreements": sum(bool(x["gate_disagreement"]) for x in subset),
            "retrospective_disagreement_settlements": dict(Counter(
                x["observed_counterfactual_settlement"]
                for x in subset if x["gate_disagreement"] and x["observed_counterfactual_settlement"] is not None
            )),
        }
    return {
        "ok": True,
        "kind": "GOAL_GATE_ABLATION_ONLY",
        "counts": counts,
        "independent_verified_c_c2_matched_epochs": len(actual_pairs),
        "unpaired_or_unverified_epochs": len(groups) - len(actual_pairs),
        "rows": result,
        "interpretation": (
            "Gate eligibility only. No price, EV, full betting action, paired P/L, "
            "forecast accuracy, or actual exposure inferred. Historical untimed "
            "freeze and counterfactual settlements are exploratory only."
        ),
        "production_rules_changed": False,
    }


def main() -> int:
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = audit(data)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2
    text = json.dumps(result, sort_keys=True, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
