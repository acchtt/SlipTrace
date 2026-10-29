"""Non-authorizing Football C G3 evidence and portfolio challengers.

Only frozen pre-kickoff fields may influence these diagnostics. No scores,
prices, bets, certificate upgrades/downgrades, or official FOLLOW assignment.
"""
from __future__ import annotations

from typing import Any

POLICY = "G3_INDEPENDENT_BRIDGE_SHADOW_V1"
PORTFOLIO_POLICY = "FOLLOW_KICKOFF_PROTECTED_SHADOW_V1"
REQUIRED_G3_CLAIMS = ("goal3_primary", "goal3_reply", "two_goal_endpoint")
MEDIUM_AXES = (
    "route_reliability", "failure_resistance", "burden_protection",
    "burden_completion_quality", "continuation_quality", "burden_stall_risk",
    "opponent_leakage",
)


def review_g3_bridge(row: dict[str, Any], frozen: dict[str, Any]) -> dict[str, Any]:
    """Reveal independently *unverified* third-goal bridge vs G4 tail context."""
    proof = frozen.get("goal_route_proof")
    proof = proof if isinstance(proof, dict) else {}
    facts = proof.get("facts")
    indexed = {
        fact.get("fact_id"): fact
        for fact in facts if isinstance(fact, dict) and isinstance(fact.get("fact_id"), str)
    } if isinstance(facts, list) else {}
    unresolved: list[str] = []
    claim_ids: dict[str, set[str]] = {}
    for name in REQUIRED_G3_CLAIMS:
        claim = proof.get(name)
        if not isinstance(claim, dict) or claim.get("status") not in {
            "SUPPORTED", "REJECTED", "CONTROL_RESISTANCE_SUPPORTED",
            "CONTROL_RISK_MATERIAL", "INDEPENDENT_REPLY_NOT_REQUIRED",
        }:
            unresolved.append(name + ".independent_fact_proof_missing")
            continue
        ids = claim.get("fact_ids")
        if not isinstance(ids, list) or not ids or any(
            not isinstance(item, str) or item not in indexed for item in ids
        ):
            unresolved.append(name + ".dated_facts_not_verified")
            continue
        claim_ids[name] = set(ids)
    reply_claim = proof.get("goal3_reply")
    if (isinstance(reply_claim, dict) and reply_claim.get("status") == "SUPPORTED"
            and "goal3_primary" in claim_ids and "goal3_reply" in claim_ids
            and claim_ids["goal3_primary"] & claim_ids["goal3_reply"]):
        unresolved.append("goal3_reply.reuses_primary_fact")
    comparable = proof.get("goal3_comparable_context")
    if not isinstance(comparable, dict) or comparable.get("status") not in {
        "TRANSFERABLE", "MIXED", "NONTRANSFERABLE"
    } or not comparable.get("basis") or not comparable.get("fact_ids"):
        unresolved.append("goal3_comparable_context.independent_proof_missing")
    endpoint = proof.get("goal3_stall_endpoints")
    if not isinstance(endpoint, dict) or not all(
        isinstance(endpoint.get(k), dict) and endpoint[k].get("basis")
        and endpoint[k].get("evidence_refs")
        for k in ("0-0", "1-1", "2-0")
    ):
        unresolved.append("goal3_stall_endpoints.source_proof_missing")
    medium_axes = [k for k in MEDIUM_AXES
                   if str(frozen.get(k, row.get(k, ""))).upper() == "MEDIUM"]
    return {
        "policy": POLICY, "match_id": row.get("match_id"),
        "goal3_funded_frozen": bool(row.get("goal3_funded")),
        "mechanism_frozen": row.get("goal3_mechanism_class"),
        "medium_axes": medium_axes,
        "missing_independent_g3_proofs": sorted(set(unresolved)),
        "source_recheck_required": bool(unresolved),
        "not_a_veto_or_prediction": True, "production_authority": False,
    }


def portfolio_challengers(rows: list[dict[str, Any]], *,
                          max_follow: int = 7) -> dict[str, Any]:
    """Predeclared workload shadows; outcome-blind; never set follow_lane."""
    focus = [r for r in rows if r.get("board_state") == "FOCUS"
             and r.get("operational_viability_grade") == "A"]
    champion = [str(r["match_id"]) for r in focus
                if r.get("follow_lane") == "FOLLOW"]
    ranked = sorted(focus, key=lambda r: (
        int(r["rank"]), str(r["kickoff_ict"]), str(r["match_id"])
    ))
    global_rank = [str(r["match_id"]) for r in ranked[:max_follow]]
    # A late block is defined by the canonical ICT midnight-rollover clock.
    # Reserve two of seven workload slots for >=01:30 ICT when there are
    # prospective A-grade FOCUS matches. No actual outcome enters selection.
    late = [r for r in ranked
            if str(r["kickoff_ict"])[11:16] >= "01:30"
            and str(r["kickoff_ict"])[11:16] <= "03:00"]
    early = [r for r in ranked if r not in late]
    protected = [str(r["match_id"]) for r in late[:min(2, max_follow)]]
    protected += [
        str(r["match_id"]) for r in early[:max_follow-len(protected)]
    ]
    return {
        "policy": PORTFOLIO_POLICY, "max_follow": max_follow,
        "champion_follow_ids": champion,
        "global_rank_shadow_ids": global_rank,
        "late_block_protected_shadow_ids": protected,
        "no_execution_authority": True,
        "changed_official_lanes": False,
    }
