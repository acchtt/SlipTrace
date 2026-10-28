"""Football C shadow-only third/fourth-goal vulnerability review.

This audit view is deliberately NON-AUTHORIZING. It does not block G3, lift
G3/G4, change FOCUS/FOLLOW, or use final scores/market prices. A reviewer must
source independent facts prospectively before any proposed policy promotion.
"""
from __future__ import annotations

from typing import Any


RISK_AXES = (
    "route_reliability",
    "failure_resistance",
    "burden_protection",
    "burden_completion_quality",
    "continuation_quality",
    "burden_stall_risk",
)


def review_goal_burden_shadow(row: dict[str, Any]) -> dict[str, Any]:
    """Log coexisting control risks lost when the live veto uses a single OR."""
    d = dict(row)
    funded_g3 = bool(d.get("goal3_funded"))
    funded_g4 = bool(d.get("goal4_funded"))
    medium_axes = [
        axis for axis in RISK_AXES if str(d.get(axis)).upper() == "MEDIUM"
    ]
    higher_burden = d.get("supported_line")
    try:
        higher_burden = float(higher_burden)
    except (ValueError, TypeError):
        higher_burden = None
    warnings: list[str] = []

    if (funded_g3 and d.get("carrier_self_fund")
            and str(d.get("carrier")).upper() == "STRONG"
            and len(medium_axes) >= 3):
        warnings.append("CARRIER_G3_MULTI_MEDIUM_CONTROL")
    if (funded_g3
            and str(d.get("upper_tail_comparable_context_signal")).upper()
            in {"MIXED", "SUPPRESSIVE"}):
        warnings.append("G3_COMPARABLE_CONTEXT_TRANSFER_REVIEW")
    if (funded_g4 or (higher_burden is not None and higher_burden >= 3.5)):
        if str(d.get("upper_tail_transferability")).upper() == "MEDIUM":
            warnings.append("G4_MEDIUM_TRANSFER_REQUIRES_INDEPENDENT_CONTINUATION")
        if str(d.get("continuation_quality")).upper() in {"LOW", "MEDIUM"}:
            warnings.append("G4_CONTINUATION_NOT_STRONG")
    return {
        "policy": "SHADOW_GOAL_PATH_AND_ENDPOINT_STRESS_V1",
        "match_id": d.get("match_id"),
        "production_authority": False,
        "has_funded_g3": funded_g3,
        "has_funded_g4": funded_g4,
        "medium_control_axes": medium_axes,
        "flags": warnings,
        "requires_prospective_source_recheck": bool(warnings),
        "does_not_change": ["G3", "G4", "FOCUS", "FOLLOW", "XI", "ODDS"],
    }
