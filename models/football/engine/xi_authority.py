#!/usr/bin/env python3
"""Shared rank/exception authority contract for every active Football C /xi path.

Both the local/direct runtime and the GitHub transport backend must call this
module before evaluating a normal ranked fixture. A routine /xi can never
reconstruct Football C from a free-standing payload. Explicit user exceptions
remain available only when the runtime authority records that the user explicitly
requested `/xi exception`; EXCEPTION is never an automatic fallback.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


class RankAuthorityError(ValueError):
    pass


def _engine_policy_fingerprint() -> str:
    """Hash the same active policy files pinned by stages_v4/stage.py."""

    football_root = Path(__file__).resolve().parents[1]
    paths = (
        football_root / "engine" / "core.py",
        football_root / "engine" / "adapter.py",
        football_root / "engine" / "xi_authority.py",
        football_root / "engine" / "xi_portable.py",
        football_root / "stages_v4" / "stage.py",
    )
    digest = hashlib.sha256()
    for file_path in paths:
        digest.update(str(file_path.relative_to(football_root)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


VERIFIED_RANK_STATUSES = {
    "V4_RANK_PERSISTENCE_VERIFIED",
    "V4_RANK_PARTIAL_PERSISTENCE_VERIFIED",
}

BLOCK_RUNTIME_SCHEMA = "football-block-runtime-v1"
BLOCK_PRIORITY_POLICY = "BLOCK_PRIORITY_V1"
BLOCK_AUTHORITY_OWNED_FIELDS = frozenset({
    "match_id",
    "activation_quality",
    "activation_basis",
    "activation_evidence_refs",
})

POLICY_LOCK_EFFECTIVE_UTC = datetime.fromisoformat("2026-10-24T18:00:00+00:00")
ASSESSMENT_DEPTH_V1_EFFECTIVE_UTC = datetime.fromisoformat("2026-11-02T01:45:00+00:00")
ASSESSMENT_DEPTH_V2_EFFECTIVE_UTC = datetime.fromisoformat("2026-11-04T00:00:00+00:00")
ASSESSMENT_DEPTH_V1_CONTRACT = "ASSESSMENT_DEPTH_V1"
ASSESSMENT_DEPTH_V2_CONTRACT = "ASSESSMENT_DEPTH_V2"
ASSESSMENT_DEPTH_REQUIRED_CHECKS = frozenset({
    "primary_scoring_route",
    "secondary_reply_route",
    "carrier_capacity",
    "current_chance_creation",
    "goal3_mechanism",
    "goal4_mechanism",
    "stall_0_0",
    "stall_1_1",
    "continuation_2_0",
    "opponent_leakage",
    "named_failure_mechanism",
    "availability_replacements",
    "h2h_transferability",
    "tournament_incentive",
    "match_context",
    "supported_burden_basis",
})
ASSESSMENT_DEPTH_THIN_TOKENS = frozenset({
    "CHECKED", "OK", "YES", "NO", "MEDIUM", "HIGH", "LOW",
    "UNKNOWN", "UNCHECKED", "NOT_CHECKED", "TBD", "N/A", "NA",
})
AUTHORITY_OWNED_FIELDS = {
    "board_state",
    "follow_lane",
    "rank",
}


EXCEPTION_REQUIRED_RESEARCH_FIELDS = frozenset({
    "fixture_identity_status",
    "competition_format_incentive",
    "rivalry_rest_travel_fatigue_context",
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
    "match_context_review_status",
    "rivalry_context",
    "rest_load_context",
    "travel_load_context",
    "fatigue_context",
    "match_context_effect",
    "match_context_basis",
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
    supplied_match = supplied.get("match")
    if not isinstance(supplied_match, dict):
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: c_football.match object missing"
        )
    source_urls = _required_string_list(
        supplied_match,
        "source_urls",
        label="c_football.match",
        minimum=2,
    )
    missing_source_links = sorted(set(evidence_refs) - set(source_urls))
    if missing_source_links:
        raise RankAuthorityError(
            "EXCEPTION_RESEARCH_REQUIRED: exception evidence_refs must be "
            "attached to c_football.match.source_urls: "
            + ", ".join(missing_source_links)
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


def _assessment_at_utc(payload: dict[str, Any]) -> datetime:
    context = payload.get("context")
    if not isinstance(context, dict):
        raise ValueError("c_football.context object required")
    raw = context.get("assessment_at_utc")
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError("c_football.context.assessment_at_utc required")
    value = raw.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("invalid c_football.context.assessment_at_utc") from exc
    if parsed.tzinfo is None:
        raise ValueError("c_football.context.assessment_at_utc must be timezone-aware")
    return parsed


def _validate_assessment_depth(supplied: dict[str, Any]) -> dict[str, Any]:
    """Fail closed on thin post-activation Football C assessments."""

    assessment_at = _assessment_at_utc(supplied)
    if assessment_at < ASSESSMENT_DEPTH_V1_EFFECTIVE_UTC:
        return {
            "required": False,
            "contract": "LEGACY_PRE_ASSESSMENT_DEPTH_V1",
            "assessment_at_utc": assessment_at.isoformat(),
        }

    expected_contract = (
        ASSESSMENT_DEPTH_V2_CONTRACT
        if assessment_at >= ASSESSMENT_DEPTH_V2_EFFECTIVE_UTC
        else ASSESSMENT_DEPTH_V1_CONTRACT
    )

    depth = supplied.get("assessment_depth")
    if not isinstance(depth, dict):
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth object missing"
        )
    if depth.get("contract") != expected_contract:
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.contract must be "
            + expected_contract
        )
    if depth.get("completed") is not True:
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.completed must be true"
        )
    if depth.get("market_independent") is not True:
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.market_independent must be true"
        )

    epoch = depth.get("evidence_epoch_id")
    supplied_epoch = supplied.get("evidence_epoch_id")
    if not isinstance(epoch, str) or not epoch.strip():
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.evidence_epoch_id required"
        )
    if not isinstance(supplied_epoch, str) or epoch.strip() != supplied_epoch.strip():
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment-depth epoch must equal "
            "c_football.evidence_epoch_id"
        )

    assessed_at = depth.get("assessed_at_utc")
    context = supplied.get("context")
    context_at = context.get("assessment_at_utc") if isinstance(context, dict) else None
    if not isinstance(assessed_at, str) or assessed_at.strip() != str(context_at or "").strip():
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.assessed_at_utc "
            "must equal context.assessment_at_utc"
        )

    refs = depth.get("evidence_refs")
    if (
        not isinstance(refs, list)
        or len(refs) < 2
        or any(not isinstance(x, str) or not x.strip() for x in refs)
    ):
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.evidence_refs "
            "must contain at least two non-empty football references"
        )
    normalized_refs = [x.strip() for x in refs]
    if len(set(normalized_refs)) != len(normalized_refs):
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.evidence_refs "
            "must not contain duplicates"
        )

    checks = depth.get("checks")
    if not isinstance(checks, dict):
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: assessment_depth.checks object missing"
        )
    missing = sorted(ASSESSMENT_DEPTH_REQUIRED_CHECKS - set(checks))
    if missing:
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: missing substantive checks: "
            + ", ".join(missing)
        )

    thin: list[str] = []
    for key in sorted(ASSESSMENT_DEPTH_REQUIRED_CHECKS):
        value = checks.get(key)
        if not isinstance(value, str):
            thin.append(key)
            continue
        normalized = value.strip()
        token = normalized.upper().replace("-", "_").replace(" ", "_")
        if len(normalized) < 16 or token in ASSESSMENT_DEPTH_THIN_TOKENS:
            thin.append(key)
    if thin:
        raise RankAuthorityError(
            "ASSESSMENT_RESEARCH_INCOMPLETE: thin/non-substantive assessment "
            "conclusions: " + ", ".join(thin)
        )

    activation_trace = None
    if expected_contract == ASSESSMENT_DEPTH_V2_CONTRACT:
        match = supplied.get("match")
        if not isinstance(match, dict):
            raise RankAuthorityError(
                "ASSESSMENT_RESEARCH_INCOMPLETE: V2 requires c_football.match"
            )
        activation_quality = str(
            match.get("activation_quality") or ""
        ).strip().upper()
        if activation_quality not in {"LOW", "MEDIUM", "HIGH"}:
            raise RankAuthorityError(
                "ASSESSMENT_RESEARCH_INCOMPLETE: activation_quality must be "
                "LOW/MEDIUM/HIGH"
            )
        activation_basis = match.get("activation_basis")
        if not isinstance(activation_basis, str) or len(activation_basis.strip()) < 24:
            raise RankAuthorityError(
                "ASSESSMENT_RESEARCH_INCOMPLETE: activation_basis must be substantive"
            )
        activation_refs = match.get("activation_evidence_refs")
        normalized_activation_refs = (
            [
                ref.strip()
                for ref in activation_refs
                if isinstance(ref, str) and ref.strip()
            ]
            if isinstance(activation_refs, list)
            else []
        )
        if len(set(normalized_activation_refs)) < 2:
            raise RankAuthorityError(
                "ASSESSMENT_RESEARCH_INCOMPLETE: activation_evidence_refs "
                "must contain at least two distinct football references"
            )
        missing_activation_refs = sorted(
            set(normalized_activation_refs) - set(normalized_refs)
        )
        if missing_activation_refs:
            raise RankAuthorityError(
                "ASSESSMENT_RESEARCH_INCOMPLETE: activation evidence refs must "
                "also be present in assessment_depth.evidence_refs: "
                + ", ".join(missing_activation_refs)
            )
        activation_trace = {
            "quality": activation_quality,
            "basis": activation_basis.strip(),
            "evidence_refs": list(dict.fromkeys(normalized_activation_refs)),
            "block_selection_only": True,
            "certificate_authority": False,
            "price_execution_authority": False,
        }

    return {
        "required": True,
        "contract": expected_contract,
        "completed": True,
        "market_independent": True,
        "evidence_epoch_id": epoch.strip(),
        "assessment_at_utc": assessment_at.isoformat(),
        "evidence_ref_count": len(normalized_refs),
        "checks": sorted(ASSESSMENT_DEPTH_REQUIRED_CHECKS),
        "activation": activation_trace,
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


def _canonical_sha256(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, ensure_ascii=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _validated_block_package(
    package: dict[str, Any],
    *,
    match_id: str,
) -> tuple[dict[str, Any], dict[str, Any], str]:
    request = package.get("request")
    result = package.get("result")
    if not isinstance(request, dict) or not isinstance(result, dict):
        raise RankAuthorityError(
            "BLOCK_RECEIPT_REQUIRED: verified block package must contain request and result"
        )
    if request.get("schema_version") != BLOCK_RUNTIME_SCHEMA:
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block request schema mismatch")
    if str(request.get("model") or "").lower() != "c":
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block request must be Football C")
    matches = request.get("matches")
    if not isinstance(matches, list) or len(matches) < 2:
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: complete block request missing")
    if (
        result.get("schema_version") != BLOCK_RUNTIME_SCHEMA
        or result.get("stage") != "block_result"
        or str(result.get("model") or "").lower() != "c"
        or result.get("policy") != BLOCK_PRIORITY_POLICY
    ):
        raise RankAuthorityError(
            "BLOCK_RECEIPT_REQUIRED: persisted result is not BLOCK_PRIORITY_V1"
        )
    if result.get("outcome_fields_read") is not False:
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block result must remain prospective")
    if result.get("priced_publication_authorized") is not False:
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block receipt cannot carry price authority")
    if result.get("input_sha256") != _canonical_sha256(request):
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block request/result integrity mismatch")

    frozen_row = next(
        (row for row in matches
         if isinstance(row, dict) and str(row.get("match_id")) == match_id),
        None,
    )
    rows = result.get("matches")
    result_row = next(
        (row for row in rows
         if isinstance(row, dict) and str(row.get("match_id")) == match_id),
        None,
    ) if isinstance(rows, list) else None
    if not isinstance(frozen_row, dict) or not isinstance(result_row, dict):
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: exact block candidate missing")
    if result_row.get("frozen_match_sha256") != _canonical_sha256(frozen_row):
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: frozen block candidate integrity mismatch")

    order = result.get("block_order")
    rank = result_row.get("block_priority_rank")
    if (
        not isinstance(order, list)
        or not isinstance(rank, int)
        or rank < 1
        or rank > len(order)
        or order[rank - 1] != match_id
    ):
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block priority rank/order mismatch")

    epochs = request.get("evidence_epochs")
    epoch = epochs.get(match_id) if isinstance(epochs, dict) else None
    if not isinstance(epoch, str) or not epoch.strip():
        raise RankAuthorityError(
            "BLOCK_RECEIPT_REQUIRED: persisted candidate missing assessment evidence epoch"
        )
    if result_row.get("evidence_epoch_id") != epoch:
        raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: block evidence epoch mismatch")
    return frozen_row, result_row, epoch.strip()


def _inherit_frozen_match(
    supplied_match: dict[str, Any],
    frozen_row: dict[str, Any],
    declared: list[str],
    *,
    authority_prefix: str,
    forbidden_fields: frozenset[str],
) -> tuple[dict[str, Any], set[str]]:
    if not isinstance(declared, list) or any(not isinstance(x, str) for x in declared):
        raise RankAuthorityError(
            f"{authority_prefix}: material_evidence_updates must be a field-name array"
        )
    declared_set = set(declared)
    forbidden = declared_set & forbidden_fields
    if forbidden:
        raise RankAuthorityError(
            f"{authority_prefix}: authority-owned fields cannot be material updates: "
            + ", ".join(sorted(forbidden))
        )
    for key, frozen_value in frozen_row.items():
        if (
            key in supplied_match
            and supplied_match[key] != frozen_value
            and key not in declared_set
        ):
            raise RankAuthorityError(
                f"{authority_prefix}: undeclared override of frozen field {key}"
            )
    inherited = dict(frozen_row)
    for key in declared_set:
        if key not in supplied_match:
            raise RankAuthorityError(
                f"{authority_prefix}: declared material update absent from match: {key}"
            )
        inherited[key] = supplied_match[key]
    inherited["match_id"] = str(frozen_row.get("match_id"))
    return inherited, declared_set


def authorize_c_football(
    supplied: dict[str, Any],
    authority: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the authority-inherited Football C payload and an audit trace."""

    if not isinstance(supplied, dict):
        raise ValueError("c_football object required")
    if not isinstance(authority, dict):
        raise RankAuthorityError(
            "XI_AUTHORITY_REQUIRED: BLOCK, RANKED or explicit EXCEPTION authority missing"
        )

    mode = authority.get("mode")
    if mode == "BLOCK":
        if supplied.get("stage") != "football_assessment":
            raise RankAuthorityError(
                "BLOCK_RECEIPT_REQUIRED: block-led /xi requires football_assessment"
            )
        depth = _validate_assessment_depth(supplied)
        if depth.get("contract") != ASSESSMENT_DEPTH_V2_CONTRACT:
            raise RankAuthorityError(
                "BLOCK_RECEIPT_REQUIRED: block-led /xi requires ASSESSMENT_DEPTH_V2"
            )
        supplied_match = supplied.get("match")
        if not isinstance(supplied_match, dict):
            raise ValueError("c_football.match object required")
        mid = str(authority.get("match_id") or supplied_match.get("match_id") or "")
        if not mid:
            raise RankAuthorityError("BLOCK_RECEIPT_REQUIRED: match_id missing")
        package = authority.get("verified_block_package")
        if not isinstance(package, dict):
            raise RankAuthorityError(
                "BLOCK_RECEIPT_REQUIRED: verified_block_package missing"
            )
        frozen_row, block_row, block_epoch = _validated_block_package(
            package, match_id=mid
        )
        inherited, declared_set = _inherit_frozen_match(
            supplied_match,
            frozen_row,
            authority.get("material_evidence_updates") or [],
            authority_prefix="BLOCK_RECEIPT_REQUIRED",
            forbidden_fields=BLOCK_AUTHORITY_OWNED_FIELDS,
        )
        context = supplied.get("context")
        if not isinstance(context, dict):
            raise ValueError("c_football.context object required")
        inherited_context = dict(context)
        inherited_context.update({
            "block_authority": True,
            "block_priority_policy": BLOCK_PRIORITY_POLICY,
            "block_priority_rank": block_row.get("block_priority_rank"),
            "block_evidence_epoch_id": block_epoch,
            "frozen_board_available": True,
            "frozen_board_certified_burden": block_row.get("supported_line"),
        })
        frozen_g4 = frozen_row.get("g4_research_status")
        if frozen_g4 is not None:
            inherited_context["frozen_board_g4_research_status"] = frozen_g4

        payload = dict(supplied)
        payload["match"] = inherited
        payload["context"] = inherited_context
        return payload, {
            "mode": "BLOCK",
            "match_id": mid,
            "block_priority_policy": BLOCK_PRIORITY_POLICY,
            "block_priority_rank": block_row.get("block_priority_rank"),
            "block_order": list(package["result"].get("block_order") or []),
            "block_evidence_epoch_id": block_epoch,
            "xi_evidence_epoch_id": supplied.get("evidence_epoch_id"),
            "frozen_match_sha256": block_row.get("frozen_match_sha256"),
            "block_input_sha256": package["result"].get("input_sha256"),
            "global_rank_is_selection_authority": False,
            "material_evidence_updates": sorted(declared_set),
            "assessment_depth": depth,
        }
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
        assessment_depth_trace = _validate_assessment_depth(supplied)
        exception_payload = dict(supplied)
        exception_context = dict(exception_payload.get("context") or {})
        exception_context["exception_research_completed"] = True
        exception_context["exception_research_epoch_id"] = research_trace["research_epoch_id"]
        exception_context["exception_upstream_state"] = research_trace["upstream_state"]
        exception_context["exception_revision"] = research_trace["revision"]
        exception_context["exception_flag"] = True
        exception_payload["context"] = exception_context
        return exception_payload, {
            "mode": "EXCEPTION",
            "reference": reference,
            "user_requested_exception": True,
            "rank_state_internal": None,
            "rank_state_display": "EXCEPTION",
            "exception_research": research_trace,
            "assessment_depth": assessment_depth_trace,
        }

    if mode != "RANKED":
        raise RankAuthorityError(
            "XI_AUTHORITY_REQUIRED: authority.mode must be BLOCK, RANKED or EXCEPTION"
        )

    assessment_depth_trace = _validate_assessment_depth(supplied)

    package = authority.get("verified_rank_package")
    if not isinstance(package, dict) or package.get("status") not in VERIFIED_RANK_STATUSES:
        raise RankAuthorityError("RANK_RECEIPT_REQUIRED: verified rank package missing")

    rank = _rank_payload(package)
    policy_lock = rank.get("engine_policy_lock") or package.get("engine_policy_lock")
    pinned_fingerprint = (
        rank.get("engine_policy_fingerprint")
        or package.get("engine_policy_fingerprint")
    )
    assessment_at = _assessment_at_utc(supplied)
    if (
        assessment_at >= POLICY_LOCK_EFFECTIVE_UTC
        and policy_lock != "SLATE_PINNED_V1"
    ):
        raise RankAuthorityError(
            "RANK_POLICY_LOCK_REQUIRED: this /xi assessment is after the "
            "Football C slate-lock activation, but the verified rank receipt "
            "was sealed under the legacy unlocked contract; rerank/reseal the "
            "fixture before routine execution"
        )
    if policy_lock == "SLATE_PINNED_V1":
        if not isinstance(pinned_fingerprint, str) or not pinned_fingerprint.strip():
            raise RankAuthorityError(
                "RANK_RECEIPT_REQUIRED: pinned slate is missing engine policy fingerprint"
            )
        current_fingerprint = _engine_policy_fingerprint()
        if current_fingerprint != pinned_fingerprint:
            raise RankAuthorityError(
                "RANK_ENGINE_POLICY_DRIFT: current Football C policy differs from "
                "the revision that sealed this rank receipt; do not mix policies "
                "inside one slate"
            )
    else:
        current_fingerprint = None
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
    frozen_follow_lane = str(board_row.get("follow_lane") or "").strip()
    if frozen_follow_lane not in {"FOLLOW", "RESERVE", "FOCUS_UNFOLLOWED"}:
        raise RankAuthorityError(
            "RANK_RECEIPT_REQUIRED: ranked FOCUS row is missing a valid frozen follow lane"
        )
    ranked_direct_request = authority.get("ranked_direct_request") is True
    if frozen_follow_lane == "FOCUS_UNFOLLOWED" and not ranked_direct_request:
        raise RankAuthorityError(
            "RANKED_DIRECT_REQUEST_REQUIRED: FOCUS_UNFOLLOWED is qualified but "
            "outside automatic workload capacity; an exact user /xi request must "
            "set ranked_direct_request=true"
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
    inherited_context["official_follow_lane"] = frozen_follow_lane
    if frozen_follow_lane == "FOCUS_UNFOLLOWED":
        inherited_context["step2_authorization"] = "RANKED_DIRECT_REQUEST"
    inherited_context["frozen_board_available"] = True
    inherited_context["frozen_board_certified_burden"] = board_row.get("supported_line")
    inherited_context["rank"] = board_row.get("rank")
    inherited_context["current_rank"] = board_row.get(
        "current_rank", board_row.get("rank")
    )
    inherited_context["slate_rank"] = board_row.get("slate_rank")
    inherited_context["slate_rank_status"] = board_row.get("slate_rank_status")
    inherited_context["rank_scope"] = board_row.get("rank_scope")
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
        "engine_policy_lock": policy_lock,
        "pinned_engine_policy_fingerprint": pinned_fingerprint,
        "current_engine_policy_fingerprint": current_fingerprint,
        "rank": board_row.get("rank"),
        "current_rank": board_row.get("current_rank", board_row.get("rank")),
        "slate_rank": board_row.get("slate_rank"),
        "slate_rank_status": board_row.get("slate_rank_status"),
        "rank_scope": board_row.get("rank_scope"),
        "frozen_board_state": board_row.get("board_state"),
        "frozen_follow_lane": frozen_follow_lane,
        "ranked_direct_request": ranked_direct_request,
        "step2_authorization": inherited_context.get("step2_authorization"),
        "rank_state_internal": "WATCH" if frozen_board_state == "WATCH" else frozen_board_state,
        "rank_state_display": "REVIEW_ONLY" if frozen_board_state == "WATCH" else frozen_board_state,
        "frozen_supported_line": board_row.get("supported_line"),
        "frozen_g4_research_status": frozen_g4,
        "material_evidence_updates": sorted(declared_set),
        "assessment_depth": assessment_depth_trace,
    }
