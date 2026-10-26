"""Prospective, fact-level proof for goal-route research.

Only a research completeness contract: no predictive grades, G3/G4 certificates,
FOCUS, /xi, market quotes or final scores are modified. The contract is opt-in
by a versioned /rank payload and preserves historical sealed receipt replay.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any

POLICY = "SOURCE_INDEPENDENT_GOAL_PATHS_V1"
CLAIM_FIELDS = (
    "goal3_primary", "goal3_reply", "two_goal_endpoint",
    "fourth_goal_after_three", "main_failure",
)
GRADE_FIELDS = (
    "route_reliability", "chance_quality", "failure_resistance",
    "burden_completion_quality", "continuation_quality",
)
STATUSES = {
    "goal3_primary": {"SUPPORTED", "REJECTED"},
    "goal3_reply": {"SUPPORTED", "INDEPENDENT_REPLY_NOT_REQUIRED", "REJECTED"},
    "two_goal_endpoint": {"CONTROL_RESISTANCE_SUPPORTED", "CONTROL_RISK_MATERIAL", "REJECTED"},
    "fourth_goal_after_three": {"SUPPORTED", "REJECTED", "NOT_APPLICABLE"},
    "main_failure": {"ASSESSED"},
}


def _timestamp(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return stamp if stamp.tzinfo is not None else None
    except ValueError:
        return None


def _string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _ids(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(v, str) and bool(v.strip()) for v in value
    ) and len(value) == len(set(value))


def review_goal_route_proof(
    row: dict[str, Any],
    *,
    rank_at_utc: str,
    kickoff_utc: str,
) -> dict[str, Any]:
    """Fail-closed on unverifiable independence, never convert to PASS.

    Each fact has its own dated observation and references. Repeating a URL
    across separate facts is permitted, but reusing the exact same fact as
    independent goals or merely cloning the same grade link is not.
    """
    gaps: list[str] = []
    warnings: list[str] = []
    proof = row.get("goal_route_proof")
    if not isinstance(proof, dict):
        return {"status": "INCOMPLETE", "gaps": ["goal_route_proof.missing"],
                "warnings": [], "proof_policy": POLICY, "grade_overlap": None}
    if proof.get("version") != POLICY:
        gaps.append("version.mismatch")

    cutoff = _timestamp(rank_at_utc)
    kickoff = _timestamp(kickoff_utc)
    if cutoff is None or kickoff is None:
        gaps.append("source_epoch.invalid")

    raw_facts = proof.get("facts")
    facts: dict[str, dict[str, Any]] = {}
    if not isinstance(raw_facts, list) or not raw_facts:
        gaps.append("facts.missing")
    else:
        for i, fact in enumerate(raw_facts):
            if not isinstance(fact, dict):
                gaps.append(f"facts.{i}.invalid")
                continue
            fid = fact.get("fact_id")
            if not _string(fid) or fid in facts:
                gaps.append(f"facts.{i}.duplicate_or_missing_id")
                continue
            facts[fid] = fact
            if not _string(fact.get("basis")):
                gaps.append(f"facts.{fid}.basis")
            refs = fact.get("evidence_refs")
            if not _ids(refs):
                gaps.append(f"facts.{fid}.evidence_refs")
            ts = _timestamp(fact.get("observed_at_utc"))
            if ts is None or (cutoff is not None and ts > cutoff) or (kickoff is not None and ts >= kickoff):
                gaps.append(f"facts.{fid}.prospective_timestamp")

    claim_refs: dict[str, set[str]] = {}
    claim_sources: dict[str, set[str]] = {}
    for field in CLAIM_FIELDS:
        claim = proof.get(field)
        if not isinstance(claim, dict):
            gaps.append(f"{field}.missing")
            continue
        if claim.get("status") not in STATUSES[field]:
            gaps.append(f"{field}.status")
        if not _string(claim.get("basis")):
            gaps.append(f"{field}.basis")
        ids = claim.get("fact_ids")
        if not _ids(ids):
            gaps.append(f"{field}.fact_ids")
            continue
        claim_refs[field] = set(ids)
        missing = set(ids) - set(facts)
        if missing:
            gaps.append(f"{field}.unknown_fact_ids")
        claim_sources[field] = {
            url for fid in ids if fid in facts
            for url in facts[fid].get("evidence_refs", [])
            if isinstance(url, str)
        }

    first = claim_refs.get("goal3_primary", set())
    reply = claim_refs.get("goal3_reply", set())
    fourth = claim_refs.get("fourth_goal_after_three", set())
    # A home/away reply must have independent factual support from a carrier
    # or primary attack. One scored-history sample alone is not two routes.
    if first and reply and first & reply and proof.get("goal3_reply", {}).get("status") == "SUPPORTED":
        gaps.append("goal3_reply.fact_recycled_from_primary")
    if reply and first and claim_sources.get("goal3_primary", set()) & claim_sources.get("goal3_reply", set()):
        warnings.append("goal3_primary_reply_shared_source_family_verify_separate_observations")
    if fourth and first and not (fourth - first):
        # Fourth-goal proof requires at least one additional fact; not a
        # copy of exactly the same evidence used to certify goal three.
        if proof.get("fourth_goal_after_three", {}).get("status") == "SUPPORTED":
            gaps.append("fourth_goal_after_three.no_additional_fact")

    links = proof.get("grade_fact_links")
    overlap = None
    if not isinstance(links, dict):
        gaps.append("grade_fact_links.missing")
    else:
        sets: list[frozenset[str]] = []
        for field in GRADE_FIELDS:
            values = links.get(field)
            if not _ids(values) or not set(values).issubset(facts):
                gaps.append(f"grade_fact_links.{field}")
                continue
            sets.append(frozenset(values))
        if sets:
            overlap = {
                "linked_dimensions": len(sets),
                "unique_fact_sets": len(set(sets)),
                "all_dimensions_share_exact_same_facts": (
                    len(sets) >= 3 and len(set(sets)) == 1
                ),
            }
            if overlap["all_dimensions_share_exact_same_facts"]:
                gaps.append("grade_fact_links.all_dimensions_recycle_same_facts")

    # Positive-route disagreements trigger research, never a hidden
    # after-the-fact downgrade of a funded G3 / G4.
    if row.get("carrier_self_fund") is True and proof.get("goal3_primary", {}).get("status") != "SUPPORTED":
        gaps.append("carrier_self_fund.primary_route_conflict")
    if row.get("independent_upper_tail") is True and proof.get("fourth_goal_after_three", {}).get("status") == "NOT_APPLICABLE":
        gaps.append("independent_upper_tail.fourth_goal_not_reviewed")

    return {
        "status": "INCOMPLETE" if gaps else "COMPLETE",
        "gaps": sorted(set(gaps)),
        "warnings": sorted(set(warnings)),
        "proof_policy": POLICY,
        "grade_overlap": overlap,
        "fact_count": len(facts),
        "no_certificate_or_grade_changes": True,
    }
