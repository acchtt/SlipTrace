#!/usr/bin/env python3
"""Shared rank/exception authority contract for every active Football C /xi path.

Both the local/direct runtime and the GitHub transport backend must call this
module before evaluating a normal ranked fixture. A routine /xi can never
reconstruct Football C from a free-standing payload. Explicit user exceptions
remain available only when the runtime authority records that the user explicitly
requested `/xi exception`; EXCEPTION is never an automatic fallback.
"""
from __future__ import annotations

from typing import Any


class RankAuthorityError(ValueError):
    pass


VERIFIED_RANK_STATUSES = {
    "V4_RANK_PERSISTENCE_VERIFIED",
    "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED",
}
AUTHORITY_OWNED_FIELDS = {
    "board_state",
    "follow_lane",
    "rank",
}


EXCEPTION_REQUIRED_RESEARCH_FIELDS = frozenset({
    "fixture_identity_status",
    "competition_format_incentive",
    "home_scoring_route",
    "away_scoring_route",
    "carrier_and_chance_creation",
    "availability_and_replacements",
    "failure_mechanisms",
    "completion_continuation_stall",
    "upper_tail_and_comparable_context",
    "h2h_materiality",
    "g4_research_if_g3_funded",
})
EXCEPTION_UPSTREAM_STATES = {
    "FOCUS",
    "WATCH",
    "PASS",
    "UNVERIFIED",
    "NOT_RANKED",
    "OUT_OF_SCOPE",
}
EXCEPTION_STATE_CHANGE_STATUSES = {
    "VERIFIED_NEW_FOOTBALL_EVIDENCE",
    "VERIFIED_PRIOR_MISCLASSIFICATION",
}
EXCEPTION_STATE_CHANGE_FIELDS = frozenset({
    "home_route",
    "away_route",
    "carrier",
    "route_reliability",
    "independent_route_quality",
    "chance_quality",
    "failure_resistance",
    "evidence_confidence",
    "burden_protection",
    "carrier_self_fund",
    "independent_upper_tail",
    "upper_tail_transferability",
    "upper_tail_comparable_context_signal",
    "completion_mode",
    "burden_completion_quality",
    "continuation_quality",
    "opponent_leakage",
    "burden_stall_risk",
    "material_suppression",
    "failure_attacks_route",
    "tournament_incentive",
    "g4_research_status",
    "g4_carrier_path",
    "g4_distributed_path",
    "g4_reply_path",
    "g4_continuation_after_g3",
})


def _required_text(obj: dict[str, Any], key: str, *, label: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RankAuthorityError(
            f"EXCEPTION_RESEARCH_REQUIRED: {label}.{key} must be non-empty"
        )
    return value.strip()


def _required_string_list(
    obj: dict[str, Any],
    key: str,
    *,
    label: str,
    minimum: int = 1,
) -> list[str]:
    value = obj.get(key)
    if (
        not isinstance(value, list)
        or len(value) < minimum
        or any(not isinstance(x, str) or not x.strip() for x in value)
    ):
        raise RankAuthorityError(
            f"EXCEPTION_RESEARCH_REQUIRED: {label}.{key} must contain "
            f"at least {minimum} non-empty string(s)"
        )
    normalized = [x.strip() for x in value]
    if len(set(normalized)) != len(normalized):
        raise RankAuthorityError(
            f"EXCEPTION_RESEARCH_REQUIRED: {label}.{key} must not contain duplicates"
        )
    return normalized


def _validate_exception_research(
    supplied: dict[str, Any],
    authority: dict[str, Any],
    *,
    exception_reference: str,
) -> dict[str, Any]:
    """Require a source-backed fresh research epoch for every /xi exception.

    Exception authority is deliberately stricter than a normal ranked /xi:
    there is no sealed FOCUS row to inherit, so the runtime must receive proof
    that the conversational research layer actually rebuilt the full Football C
    evidence package. A user challenge must create a new epoch rather than
    replaying the previous exception payload.
    """

    if supplied.get("stage") != "football_assessment":
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: explicit /xi exception must begin "
            "with a fresh football_assessment stage; direct decision-stage "
            "exception replay is forbidden"
        )

    research = authority.get("exception_research")
    if not isinstance(research, dict):
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: exception_research object missing"
        )
    if research.get("fresh_research_completed") is not True:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: fresh_research_completed must be true"
        )
    if research.get("market_independent") is not True:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: market_independent must be true"
        )

    epoch = _required_text(
        research, "research_epoch_id", label="exception_research"
    )
    supplied_epoch = supplied.get("evidence_epoch_id")
    if not isinstance(supplied_epoch, str) or not supplied_epoch.strip():
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: c_football.evidence_epoch_id missing"
        )
    if epoch != supplied_epoch.strip():
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: research_epoch_id must equal "
            "c_football.evidence_epoch_id"
        )

    context = supplied.get("context")
    if not isinstance(context, dict):
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: c_football.context object missing"
        )
    researched_at = _required_text(
        research, "researched_at_utc", label="exception_research"
    )
    assessment_at = context.get("assessment_at_utc")
    if not isinstance(assessment_at, str) or researched_at != assessment_at.strip():
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: researched_at_utc must equal "
            "context.assessment_at_utc"
        )

    upstream_state = _required_text(
        research, "upstream_state", label="exception_research"
    ).upper().replace("-", "_")
    if upstream_state.startswith("C_"):
        upstream_state = upstream_state[2:]
    if upstream_state not in EXCEPTION_UPSTREAM_STATES:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: unsupported upstream_state="
            + upstream_state
        )

    source_reference = _required_text(
        research, "source_reference", label="exception_research"
    )
    evidence_refs = _required_string_list(
        research,
        "evidence_refs",
        label="exception_research",
        minimum=2,
    )
    checked_fields = set(_required_string_list(
        research,
        "checked_fields",
        label="exception_research",
        minimum=len(EXCEPTION_REQUIRED_RESEARCH_FIELDS),
    ))
    missing = sorted(EXCEPTION_REQUIRED_RESEARCH_FIELDS - checked_fields)
    if missing:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: full Football C exception research "
            "missing checked fields: " + ", ".join(missing)
        )

    revision = str(research.get("revision") or "INITIAL").strip().upper()
    if revision not in {"INITIAL", "REASSESSMENT"}:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: revision must be INITIAL or REASSESSMENT"
        )

    supersedes_reference = None
    supersedes_epoch = None
    challenge_reason = None
    if revision == "REASSESSMENT":
        supersedes_reference = _required_text(
            research, "supersedes_exception_reference", label="exception_research"
        )
        supersedes_epoch = _required_text(
            research, "supersedes_evidence_epoch_id", label="exception_research"
        )
        challenge_reason = _required_text(
            research, "challenge_reason", label="exception_research"
        )
        if supersedes_reference == exception_reference:
            raise RankAuthorityError(
                "EXCEPTION_RESEARCH_REQUIRED: reassessment must use a new "
                "exception_reference"
            )
        if supersedes_epoch == epoch:
            raise RankAuthorityError(
                "EXCEPTION_RESEARCH_REQUIRED: reassessment must create a new "
                "evidence epoch"
            )

    supplied_match = supplied.get("match")
    if not isinstance(supplied_match, dict):
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: c_football.match object missing"
        )
    current_state = _normalize_board_state(
        context.get("board_state", supplied_match.get("board_state"))
    )
    state_change_status = research.get("state_change_status")
    state_change_fields: list[str] = []
    state_change_basis = research.get("state_change_basis")
    if upstream_state in {"WATCH", "PASS"} and current_state == "FOCUS":
        if state_change_status not in EXCEPTION_STATE_CHANGE_STATUSES:
            raise RankAuthorityError(
                "EXCEPTION_RESEARCH_REQUIRED: WATCH/PASS -> FOCUS exception "
                "requires a verified football state-change status"
            )
        if not isinstance(state_change_basis, str) or not state_change_basis.strip():
            raise RankAuthorityError(
                "EXCEPTION_RESEARCH_REQUIRED: WATCH/PASS -> FOCUS exception "
                "requires state_change_basis"
            )
        state_change_fields = _required_string_list(
            research,
            "state_change_fields",
            label="exception_research",
            minimum=1,
        )
        invalid = sorted(set(state_change_fields) - EXCEPTION_STATE_CHANGE_FIELDS)
        if invalid:
            raise RankAuthorityError(
                "EXCEPTION_RESEARCH_REQUIRED: unsupported state-change fields: "
                + ", ".join(invalid)
            )

    return {
        "fresh_research_completed": True,
        "market_independent": True,
        "research_epoch_id": epoch,
        "researched_at_utc": researched_at,
        "upstream_state": upstream_state,
        "source_reference": source_reference,
        "evidence_ref_count": len(evidence_refs),
        "checked_fields": sorted(checked_fields),
        "revision": revision,
        "supersedes_exception_reference": supersedes_reference,
        "supersedes_evidence_epoch_id": supersedes_epoch,
        "challenge_reason": challenge_reason,
        "state_change_status": state_change_status,
        "state_change_fields": state_change_fields,
        "state_change_basis": (
            state_change_basis.strip()
            if isinstance(state_change_basis, str) and state_change_basis.strip()
            else None
        ),
    }


def _normalize_board_state(value: Any) -> str:
    text = str(value or "").strip().upper().replace("-", "_")
    if text.startswith("C_"):
        text = text[2:]
    return text


def _rank_payload(package: dict[str, Any]) -> dict[str, Any]:
    for key in ("native_rank", "rank_receipt"):
        candidate = package.get(key)
        if isinstance(candidate, dict) and isinstance(candidate.get("board"), dict):
            return candidate
    if isinstance(package.get("board"), dict):
        return package
    raise RankAuthorityError("RANK_RECEIPT_REQUIRED: sealed rank board missing")


def authorize_c_football(
    supplied: dict[str, Any],
    authority: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the authority-inherited Football C payload and an audit trace."""

    if not isinstance(supplied, dict):
        raise ValueError("c_football object required")
    if not isinstance(authority, dict):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: explicit authority missing")

    mode = authority.get("mode")
    if mode == "EXCEPTION":
        if authority.get("user_requested_exception") is not True:
            raise RankAuthorityError(
                "RANK_RECEIPT_REQUIRED: EXCEPTION authority requires an explicit "
                "user /xi exception request"
            )
        reference = authority.get("exception_reference")
        if not isinstance(reference, str) or not reference.strip():
            raise RankAuthorityError(
                "RANK_RECEIPT_REQUIRED: exception authority must be explicitly tagged"
            )
        reference = reference.strip()
        research_trace = _validate_exception_research(
            supplied,
            authority,
            exception_reference=reference,
        )
        exception_payload = dict(supplied)
        exception_context = dict(exception_payload.get("context") or {})
        exception_context["exception_research_completed"] = True
        exception_context["exception_research_epoch_id"] = research_trace["research_epoch_id"]
        exception_context["exception_upstream_state"] = research_trace["upstream_state"]
        exception_context["exception_revision"] = research_trace["revision"]
        exception_payload["context"] = exception_context
        return exception_payload, {
            "mode": "EXCEPTION",
            "reference": reference,
            "user_requested_exception": True,
            "rank_state_internal": None,
            "rank_state_display": "EXCEPTION",
            "exception_research": research_trace,
        }

    if mode != "RANKED":
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: ranked or exception authority required"
        )

    package = authority.get("verified_rank_package")
    if not isinstance(package, dict) or package.get("status") not in VERIFIED_RANK_STATUSES:
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: verified rank package missing")

    rank = _rank_payload(package)
    board = rank.get("board") or {}
    rows = board.get("matches")
    frozen = rank.get("frozen_model_input") or {}
    frozen_rows = frozen.get("matches") if isinstance(frozen, dict) else None
    if not isinstance(rows, list) or not isinstance(frozen_rows, list):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: frozen rank evidence missing")

    supplied_match = supplied.get("match")
    if not isinstance(supplied_match, dict):
        raise ValueError("c_football.match object required")
    mid = str(authority.get("match_id") or supplied_match.get("match_id") or "")
    if not mid:
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: match_id missing")

    board_row = next(
        (row for row in rows if isinstance(row, dict) and str(row.get("match_id")) == mid),
        None,
    )
    frozen_row = next(
        (row for row in frozen_rows if isinstance(row, dict) and str(row.get("match_id")) == mid),
        None,
    )
    if not isinstance(board_row, dict) or not isinstance(frozen_row, dict):
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: exact ranked match row missing")

    frozen_board_state = _normalize_board_state(board_row.get("board_state"))
    if frozen_board_state != "FOCUS":
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: routine /xi requires an exact ranked FOCUS board row"
        )

    declared = authority.get("material_evidence_updates") or []
    if not isinstance(declared, list) or any(not isinstance(x, str) for x in declared):
        raise RankAuthorityError("material_evidence_updates must be a field-name array")
    declared_set = set(declared)
    forbidden = declared_set & AUTHORITY_OWNED_FIELDS
    if forbidden:
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: authority-owned fields cannot be material updates: "
            + ", ".join(sorted(forbidden))
        )

    for key, frozen_value in frozen_row.items():
        if key in supplied_match and supplied_match[key] != frozen_value and key not in declared_set:
            raise RankAuthorityError(
                f"RANK_RECEIPT_REQUIRED: undeclared override of frozen field {key}"
            )

    inherited = dict(frozen_row)
    for key in declared_set:
        if key not in supplied_match:
            raise RankAuthorityError(
                f"declared material update absent from match: {key}"
            )
        inherited[key] = supplied_match[key]
    inherited["match_id"] = mid
    # Rank selection itself is immutable at /xi. Updated football fields may
    # change the current certificate, but they cannot silently relabel the
    # original ranked fixture.
    inherited["board_state"] = "C-FOCUS"

    context = supplied.get("context")
    if not isinstance(context, dict):
        raise ValueError("c_football.context object required")
    supplied_context_state = context.get("board_state")
    if (
        supplied_context_state is not None
        and _normalize_board_state(supplied_context_state) != frozen_board_state
    ):
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: context board_state conflicts with frozen rank authority"
        )
    inherited_context = dict(context)
    inherited_context["board_state"] = "C-FOCUS"
    inherited_context["frozen_board_available"] = True
    inherited_context["frozen_board_certified_burden"] = board_row.get("supported_line")
    frozen_g4 = (
        frozen_row.get("g4_research_status")
        or board_row.get("g4_research_status")
        or inherited_context.get("frozen_board_g4_research_status")
    )
    if frozen_g4 is not None:
        inherited_context["frozen_board_g4_research_status"] = frozen_g4

    c_football = dict(supplied)
    c_football["match"] = inherited
    c_football["context"] = inherited_context

    return c_football, {
        "mode": "RANKED",
        "match_id": mid,
        "rank_run_id": rank.get("run_id"),
        "rank_integrity_sha256": rank.get("integrity_sha256"),
        "rank": board_row.get("rank"),
        "frozen_board_state": board_row.get("board_state"),
        "rank_state_internal": "WATCH" if frozen_board_state == "WATCH" else frozen_board_state,
        "rank_state_display": "REVIEW_ONLY" if frozen_board_state == "WATCH" else frozen_board_state,
        "frozen_supported_line": board_row.get("supported_line"),
        "frozen_g4_research_status": frozen_g4,
        "material_evidence_updates": sorted(declared_set),
    }
