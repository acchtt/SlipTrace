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
        return dict(supplied), {
            "mode": "EXCEPTION",
            "reference": reference.strip(),
            "user_requested_exception": True,
            "rank_state_internal": None,
            "rank_state_display": "EXCEPTION",
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
