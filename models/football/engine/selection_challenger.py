"""Football C coordinated selection challenger — SHADOW ONLY.

No execution authorization, BET/BOOK authority, market prices or learned outcome
coefficients. This modules scores the same frozen prematch football evidence as C.
All scoring parts are auditable, including stacked moderate endpoint cautions.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

from core import (
    CarrierStrength, CompletionMode, Grade, MatchAssessment, RouteStrength,
    c_effective_incentive_grades, c_g3_endpoint_control_pressure,
    c_goal3_funded, c_goal3_mechanism_class, c_goal4_funded,
    certified_supported_burden, funded_goal_certificate_depth,
)

SHADOW_POLICY = "C_SELECTION_CHALLENGER_20261026_V1"
# Interpretable ordinal quality score; NOT a probability or an odds model.
GRADE_POINTS = {
    "route_reliability": (0, 8, 16),
    "chance_quality": (0, 8, 16),
    "failure_resistance": (0, 8, 16),
    "burden_completion_quality": (0, 8, 16),
    "effective_continuation": (0, 6, 12),
    "independent_route_quality": (0, 5, 10),
    "opponent_leakage": (0, 3, 6),
}


def entry_readiness(kickoff_ict: str | None, frozen_at_utc: str | None) -> dict[str, Any]:
    """Readiness is opportunity logistics, not a prediction or betting proof."""
    if not kickoff_ict or not frozen_at_utc:
        return {"entry_state": "UNKNOWN", "entry_lead_minutes": None}
    try:
        kickoff = datetime.fromisoformat(kickoff_ict.replace("Z", "+00:00"))
        frozen = datetime.fromisoformat(frozen_at_utc.replace("Z", "+00:00"))
        if kickoff.tzinfo is None or frozen.tzinfo is None:
            raise ValueError("timezone required")
        lead = round((kickoff - frozen).total_seconds() / 60, 1)
    except (ValueError, TypeError):
        return {"entry_state": "UNKNOWN", "entry_lead_minutes": None}
    state = (
        "CLOSED" if lead <= 0 else
        "CRITICAL" if lead < 15 else
        "AT_RISK" if lead < 60 else
        "RESEARCH_LEAD_READY"
    )
    return {"entry_state": state, "entry_lead_minutes": lead}


def _independent_g4_path_quality(raw: dict[str, Any], a: MatchAssessment) -> str:
    """Never infer goal FOUR solely from G3 grades or all-competition rates.

    Original native path evidence requires a nonempty prospective explanation and
    independently checkable references for a carrier/reply/distributed G4 path.
    This is a *selection* proof diagnostic, not a silent rewrite of C certificates.
    """
    if not c_goal4_funded(a):
        return "NOT_APPLICABLE"
    path_evidence = raw.get("g4_path_evidence")
    if not isinstance(path_evidence, dict):
        return "UNVERIFIED"
    for key in ("g4_carrier_path", "g4_reply_path", "g4_distributed_path"):
        item = path_evidence.get(key)
        if isinstance(item, dict) and isinstance(item.get("basis"), str) and len(item["basis"].strip()) >= 40:
            refs = item.get("evidence_refs")
            if isinstance(refs, list) and any(isinstance(ref, str) and ref.strip() for ref in refs):
                return "SOURCED_PATH_RECORDED"
    return "UNVERIFIED"


def selection_quality_profile(a: MatchAssessment, raw: dict[str, Any],
                              frozen_at_utc: str | None = None) -> dict[str, Any]:
    """Selection-tier hypothesis, separately from funded certificate / C action.

    Explicitly penalize stacked MEDIUM control risks rather than turning each
    MEDIUM into an arbitrary hard veto; rank reliable 3-goal paths above weak
    carriers, but preserve all legitimate G3 evidence for retrospective recall.
    """
    timing = entry_readiness(raw.get("kickoff_ict"), frozen_at_utc)
    g3 = c_goal3_funded(a)
    cont, stall = c_effective_incentive_grades(a)
    mechanism = c_goal3_mechanism_class(a)
    grades = {
        "route_reliability": a.route_reliability,
        "chance_quality": a.chance_quality,
        "failure_resistance": a.failure_resistance,
        "burden_completion_quality": a.burden_completion_quality,
        "effective_continuation": cont,
        "independent_route_quality": a.independent_route_quality,
        "opponent_leakage": a.opponent_leakage,
    }
    components = {key: GRADE_POINTS[key][int(val)] for key, val in grades.items()}
    moderate_names = [
        name for name in (
            "route_reliability", "chance_quality", "failure_resistance",
            "burden_completion_quality", "effective_continuation"
        ) if grades[name] == Grade.MEDIUM
    ]
    stacked_caution = max(0, len(moderate_names) - 2) * 5
    trap = a.goal_signal_low_draw_trap_rate
    trap_penalty = (15 if trap is not None and trap >= 0.25 else
                    8 if trap is not None and trap >= 0.20 else 0)
    endpoint_penalty = (
        25 if c_g3_endpoint_control_pressure(a) == "HIGH" else
        8 if stall == Grade.MEDIUM else
        0
    )
    independent_bonus = (
        8 if a.home_route == RouteStrength.STRONG and a.away_route == RouteStrength.STRONG
        else 4 if a.home_route >= RouteStrength.USABLE and a.away_route >= RouteStrength.USABLE
        else 0
    )
    self_funded_bonus = 5 if a.carrier == CarrierStrength.STRONG and a.carrier_self_fund else 0
    one_route_risk = (
        8 if mechanism == "CARRIER" and min(a.home_route, a.away_route) == RouteStrength.WEAK
        and a.failure_resistance == Grade.MEDIUM else 0
    )
    score = (
        sum(components.values()) + independent_bonus + self_funded_bonus
        - stacked_caution - trap_penalty - endpoint_penalty - one_route_risk
    )
    risk = {
        "stacked_moderate_count": len(moderate_names),
        "stacked_moderate_fields": moderate_names,
        "stacked_moderate_penalty": stacked_caution,
        "stall_penalty": endpoint_penalty,
        "draw_trap_penalty": trap_penalty,
        "single_route_penalty": one_route_risk,
    }
    g4_path = _independent_g4_path_quality(raw, a)
    blockers = []
    if not g3:
        blockers.append("NO_INDEPENDENT_G3_CERTIFICATE")
    if c_g3_endpoint_control_pressure(a) == "HIGH":
        blockers.append("HARD_G3_ENDPOINT_CONTROL")
    if a.material_suppression or a.failure_attacks_route:
        blockers.append("DIRECT_ROUTE_FAILURE")
    if g4_path == "UNVERIFIED":
        blockers.append("G4_PATH_PROOF_UNVERIFIED")
    if timing["entry_state"] in {"CLOSED", "CRITICAL"}:
        blockers.append("RANK_TO_KICKOFF_ACCESS_RISK")

    # G4 verification affects high-conviction workload only. It never removes
    # a legitimate football G3 or edits the official compiled supported line.
    strong = (
        g3 and score >= 78 and len(moderate_names) <= 2
        and c_g3_endpoint_control_pressure(a) != "HIGH"
        and g4_path != "UNVERIFIED"
        and timing["entry_state"] not in {"CLOSED", "CRITICAL"}
    )
    tier = (
        "HIGH_CONVICTION" if strong else
        "CONDITIONAL" if g3 and c_g3_endpoint_control_pressure(a) != "HIGH" else
        "REVIEW"
    )
    return {
        "selection_challenger_policy": SHADOW_POLICY,
        "selection_challenger_tier": tier,
        "selection_challenger_score": score,
        "selection_challenger_mechanism": mechanism,
        "selection_challenger_risk": risk,
        "selection_challenger_blockers": blockers,
        "selection_challenger_goal4_proof": g4_path,
        "selection_challenger_route_scenarios": (
            ["SELF_FUNDED_3_PLUS"] if mechanism == "CARRIER" else
            ["TWO_INDEPENDENT_ROUTES_2_PLUS_1"] if mechanism in {"TWO_ROUTE", "DISTRIBUTED"} else
            ["STRONG_ROUTE_AND_VERIFIED_LEAKAGE"] if mechanism == "LEAKAGE" else []
        ),
        "selection_challenger_entry_state": timing["entry_state"],
        "selection_challenger_entry_lead_minutes": timing["entry_lead_minutes"],
        "selection_challenger_certified_burden": certified_supported_burden(a, "c"),
    }


def shadow_follow_allocation(rows: list[dict[str, Any]], cap: int = 7,
                             per_kickoff: int = 3) -> dict[str, Any]:
    """Global high-conviction nominations; never alters official FOLLOW lanes.

    Unknown readiness remains eligible for audit but ranks below actually
    documented prematch lead. Conditional and REVIEW are never auto-promoted.
    An unfilled capacity is valid.
    """
    ranked = sorted(
        (
            row for row in rows
            if row.get("board_state") == "FOCUS"
            and row.get("operational_viability_grade") == "A"
            and row.get("selection_challenger_tier") == "HIGH_CONVICTION"
        ),
        key=lambda row: (
            -int(row["selection_challenger_score"]),
            row["selection_challenger_entry_state"] != "RESEARCH_LEAD_READY",
            -(int(row.get("follow_clearability_score") or 0)),
            str(row["kickoff_ict"]),
            str(row["match_id"]),
        ),
    )
    chosen: list[str] = []
    kickoff_count: dict[str, int] = {}
    for row in ranked:
        kickoff = str(row["kickoff_ict"])
        if len(chosen) >= cap:
            break
        if kickoff_count.get(kickoff, 0) >= per_kickoff:
            continue
        chosen.append(str(row["match_id"]))
        kickoff_count[kickoff] = kickoff_count.get(kickoff, 0) + 1
    return {
        "policy": SHADOW_POLICY,
        "shadow_follow_match_ids": chosen,
        "shadow_follow_count": len(chosen),
        "shadow_capacity_unused": max(0, cap-len(chosen)),
        "shadow_does_not_authorize_execution": True,
    }
