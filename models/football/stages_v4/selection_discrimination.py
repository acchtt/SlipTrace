"""Prospective selection discrimination for near-boundary Football C G3 rows.

This module never promotes a fixture. It identifies a narrow evidence-loss
class: REVIEW_ONLY rows that already contain a STRONG current scoring route,
a usable reply route, and no LOW/hard-veto axis, yet still fail the deterministic
G3 compiler. Such rows require one bounded source-backed recheck before rank may
treat them as a completed negative qualification.
"""
from __future__ import annotations

from typing import Any

POLICY = "G3_BORDERLINE_DISCRIMINATION_V2"
RESOLUTIONS = frozenset({"CONFIRMED_REVIEW_ONLY", "RESEARCH_UPDATED"})
REQUIRED_CONCLUSIONS = (
    "primary_goal3_path",
    "reply_or_independent_completion",
    "stall_0_0_1_1_2_0",
    "continuation_after_second_goal",
    "principal_failure",
    "grade_reconciliation",
)
THIN = frozenset({
    "CHECKED", "OK", "YES", "NO", "MEDIUM", "HIGH", "LOW", "UNKNOWN",
    "TBD", "N/A", "NA", "SAME", "UNCHANGED",
})

_ROUTE = {"NONE": 0, "USABLE": 1, "STRONG": 2}
_CARRIER = {"NONE": 0, "USABLE": 1, "STRONG": 2}
_GRADE = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def _grade(row: dict[str, Any], key: str) -> int:
    return _GRADE.get(str(row.get(key) or "").upper(), -1)


def requires_borderline_recheck(
    raw: dict[str, Any],
    compiled: dict[str, Any],
) -> bool:
    """Detect the strong-route/all-medium information-loss class.

    Historical goal rates are intentionally absent. The trigger is built only
    from current football mechanism fields and hard-veto state. It therefore
    cannot auto-promote a high-scoring-history row.
    """

    if str(compiled.get("board_state")) != "WATCH":
        return False
    # Grade B is an execution-readiness caution, not a football-quality veto.
    # Restrict only to A/B because C/D are blocked upstream by the operational
    # contract itself.
    if str(compiled.get("operational_viability_grade")) not in {"A", "B"}:
        return False
    if bool(raw.get("material_suppression")) or bool(raw.get("failure_attacks_route")):
        return False

    home = _ROUTE.get(str(raw.get("home_route") or "").upper(), -1)
    away = _ROUTE.get(str(raw.get("away_route") or "").upper(), -1)
    carrier = _CARRIER.get(str(raw.get("carrier") or "").upper(), -1)
    if max(home, away) != _ROUTE["STRONG"] or min(home, away) < _ROUTE["USABLE"]:
        return False
    if carrier < _CARRIER["USABLE"]:
        return False

    required_medium = (
        "route_reliability",
        "chance_quality",
        "failure_resistance",
        "burden_protection",
        "burden_completion_quality",
        "continuation_quality",
        "opponent_leakage",
    )
    if any(_grade(raw, key) < _GRADE["MEDIUM"] for key in required_medium):
        return False
    if _grade(raw, "burden_stall_risk") > _GRADE["MEDIUM"]:
        return False
    return True


def review_borderline_recheck(
    raw: dict[str, Any],
    compiled: dict[str, Any],
) -> dict[str, Any]:
    required = requires_borderline_recheck(raw, compiled)
    if not required:
        return {
            "policy": POLICY,
            "required": False,
            "status": "NOT_REQUIRED",
            "match_id": str(raw.get("match_id") or ""),
        }

    proof = raw.get("selection_recheck")
    missing: list[str] = []
    if not isinstance(proof, dict):
        missing.append("selection_recheck")
        proof = {}

    if proof.get("contract") != POLICY:
        missing.append("contract")
    if proof.get("completed") is not True:
        missing.append("completed")
    if proof.get("market_independent") is not True:
        missing.append("market_independent")

    refs = proof.get("evidence_refs")
    if (
        not isinstance(refs, list)
        or len({str(x).strip() for x in refs if isinstance(x, str) and x.strip()}) < 2
    ):
        missing.append("evidence_refs")

    blocker = proof.get("missing_goal3_requirement")
    if not isinstance(blocker, str) or len(blocker.strip()) < 12:
        missing.append("missing_goal3_requirement")

    resolution = proof.get("resolution")
    if resolution not in RESOLUTIONS:
        missing.append("resolution")

    conclusions = proof.get("conclusions")
    if not isinstance(conclusions, dict):
        missing.extend(REQUIRED_CONCLUSIONS)
        conclusions = {}
    else:
        for key in REQUIRED_CONCLUSIONS:
            value = conclusions.get(key)
            if not isinstance(value, str):
                missing.append(key)
                continue
            normalized = value.strip()
            token = normalized.upper().replace("-", "_").replace(" ", "_")
            if len(normalized) < 24 or token in THIN:
                missing.append(key)

    status = "COMPLETE" if not missing else "PENDING"
    return {
        "policy": POLICY,
        "required": True,
        "status": status,
        "match_id": str(raw.get("match_id") or ""),
        "missing_fields": sorted(set(missing)),
        "resolution": resolution if resolution in RESOLUTIONS else None,
        "evidence_ref_count": (
            len({str(x).strip() for x in refs if isinstance(x, str) and x.strip()})
            if isinstance(refs, list) else 0
        ),
        "no_automatic_promotion": True,
        "outcome_fields_read": False,
    }
