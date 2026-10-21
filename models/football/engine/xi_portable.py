#!/usr/bin/env python3
"""Thin active /xi runner for the single official Football C model.

C2/C3/C4 are retired from new execution. Historical receipts remain immutable
and can still be read for audit, but this runtime has one policy source:
adapter.py/core.py for Football C.

User-facing behavior:
- football assessment never requires odds;
- an observed/user-screenshot quote gets a conditional ACT/BOOK/WAIT/PASS
  comparison through adapter.evaluate_observed_quote(), with no execution
  authority; BOOK is a target order and not exposure until independently filled;
- a genuinely executable current quote uses adapter.run_decision();
- started fixtures keep football analysis but never recreate prematch actions.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import math
from pathlib import Path
import sys
from typing import Any

from adapter import (
    ContractError,
    evaluate_observed_quote,
    run_decision,
    run_football_assessment,
)


MIN_PYTHON = (3, 10)


def self_check() -> dict[str, Any]:
    if sys.version_info[:2] < MIN_PYTHON:
        return {
            "ok": False,
            "status": "XI RUNTIME: FAIL",
            "error": f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required",
        }
    required = (run_football_assessment, run_decision, evaluate_observed_quote)
    if not all(callable(item) for item in required):
        return {
            "ok": False,
            "status": "XI RUNTIME: FAIL",
            "error": "required Football C runtime callables are missing",
        }
    return {
        "ok": True,
        "status": "XI RUNTIME: PASS",
        "active_models": ["c"],
        "retired_models": ["c2", "c3", "c4"],
        "runtime_mode": "THIN_SHARED_MODULES",
        "python_version": ".".join(map(str, sys.version_info[:3])),
        "shared_modules": ["core", "adapter"],
    }


def _load(path: str) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON object required")
    return value


def _time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be an ISO timestamp with timezone")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field} must be an ISO timestamp with timezone") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError(f"{field} must include a timezone")
    return result


def _quote(raw: Any) -> dict[str, float]:
    if not isinstance(raw, dict):
        raise ValueError("screenshot must show exact quote line and odds")
    line, odds = raw.get("line"), raw.get("odds")
    if (
        isinstance(line, bool)
        or not isinstance(line, (int, float))
        or isinstance(odds, bool)
        or not isinstance(odds, (int, float))
        or not math.isfinite(float(line))
        or not math.isfinite(float(odds))
        or float(line) < 0
        or abs(float(line) * 4 - round(float(line) * 4)) > 1e-8
        or float(odds) <= 1
    ):
        raise ValueError("invalid Asian quarter-goal line or decimal odds")
    return {"line": float(line), "odds": float(odds)}


def _require_c(payload: dict[str, Any], stage: str | None = None) -> None:
    if str(payload.get("model", "")).lower() != "c":
        raise ValueError("active /xi accepts Football C only; C2/C3/C4 are retired")
    if stage is not None and payload.get("stage") != stage:
        raise ValueError(f"Football C payload must use stage={stage}")


def assess_user_screenshot(
    screenshot: dict[str, Any],
    c_football: dict[str, Any],
    football_result: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate exact user screenshot as non-executable Football C quote evidence."""

    if screenshot.get("evidence_mode") != "USER_SCREENSHOT_ONLY":
        raise ValueError("screenshot evidence_mode must be USER_SCREENSHOT_ONLY")
    if screenshot.get("source") != "USER_SCREENSHOT":
        raise ValueError("screenshot source must be USER_SCREENSHOT")
    capture_reference = screenshot.get("capture_reference")
    if not isinstance(capture_reference, str) or not capture_reference.strip():
        raise ValueError("original screenshot capture_reference required")

    match_id = football_result["match_id"]
    if screenshot.get("match_id") != match_id:
        raise ValueError("screenshot match_id differs from Football C fixture")

    quote = _quote(screenshot.get("quote"))
    c_ctx = c_football.get("context")
    if not isinstance(c_ctx, dict):
        raise ValueError("Football C context required")
    fixture = c_ctx.get("fixture_status")
    if screenshot.get("fixture_status") != fixture:
        raise ValueError("screenshot fixture status conflicts with Football C evidence")

    assessment_time = _time(c_ctx.get("assessment_at_utc"), "assessment_at_utc")
    captured = screenshot.get("observed_at_utc")
    captured_time = _time(captured, "observed_at_utc") if captured is not None else None
    if captured_time is not None and captured_time > assessment_time:
        raise ValueError("screenshot observation cannot be later than assessment epoch")

    if fixture in {"STARTED", "HALFTIME"}:
        if (
            screenshot.get("score") is None
            or screenshot.get("match_minute") is None
            or screenshot.get("score") != c_ctx.get("score")
            or screenshot.get("match_minute") != c_ctx.get("match_minute")
        ):
            raise ValueError("live screenshot score/minute must match current football epoch")
    elif fixture == "PREMATCH_CONFIRMED":
        if screenshot.get("score") is not None or screenshot.get("match_minute") is not None:
            raise ValueError("prematch screenshot cannot contain live score/minute")

    evidence = {
        "price_evidence_mode": "USER_SCREENSHOT_ONLY",
        "source": "USER_SCREENSHOT",
        "capture_reference": capture_reference,
        "match_id": match_id,
        "bookmaker": screenshot.get("bookmaker"),
        "quote": quote,
        "observed_at_utc": captured,
        "assessment_at_utc": c_ctx.get("assessment_at_utc"),
        "observation_age_seconds": (
            (assessment_time - captured_time).total_seconds()
            if captured_time is not None
            else None
        ),
        "fixture_status": fixture,
        "score": screenshot.get("score"),
        "match_minute": screenshot.get("match_minute"),
        "external_price_searches": 0,
        "replacement_quotes": 0,
    }

    limitations: list[str] = ["SCREENSHOT_NOT_EXECUTION_EVIDENCE"]
    if captured_time is None:
        limitations.append("SCREENSHOT_CAPTURE_TIME_UNKNOWN")
    elif captured_time != assessment_time:
        limitations.append("SCREENSHOT_OBSERVATION_NOT_SAME_AS_ASSESSMENT_EPOCH")
    if fixture != "PREMATCH_CONFIRMED":
        limitations.append("STARTED_FIXTURE_PREMATCH_ACTION_NOT_RECREATED")

    result = evaluate_observed_quote(c_football, quote)
    recheck_required = (
        result.get("action") == "MARKET_DISAGREEMENT_RECHECK_REQUIRED"
    )
    model = {
        "supported_line": result["supported_line"],
        "snapshot_line_relation": result["line_relation"],
        "conditional_action": result["action"],
        "reason": result["reason"],
        "book_target_line": result.get("book_target_line"),
        "book_min_odds": result.get("book_min_odds"),
        "book_target_state": result.get("book_target_state", "NO_BOOK_TARGET"),
        "current_price_clears_book_target": result.get(
            "current_price_clears_book_target", False
        ),
        "book_order_is_exposure": result.get("book_order_is_exposure", False),
        "wait_target_line": result.get("wait_target_line"),
        "wait_min_odds": result.get("wait_min_odds"),
        "wait_reachable": result.get("wait_reachable"),
        "wait_reachability_basis": result.get("wait_reachability_basis"),
        "bridge_used": result.get("bridge_used", False),
        "market_disagreement_recheck_required": result.get(
            "market_disagreement_recheck_required", False
        ),
        "market_disagreement_recheck_completed": result.get(
            "market_disagreement_recheck_completed", True
        ),
        "market_disagreement_gap_goals": result.get(
            "market_disagreement_gap_goals"
        ),
        "market_disagreement_recheck_fields": result.get(
            "market_disagreement_recheck_fields", []
        ),
        "market_disagreement_recheck_evidence_refs": result.get(
            "market_disagreement_recheck_evidence_refs", []
        ),
        "market_disagreement_recheck_basis": result.get(
            "market_disagreement_recheck_basis"
        ),
        "market_disagreement_recheck_missing_fields": result.get(
            "market_disagreement_recheck_missing_fields", []
        ),
        "frozen_board_g4_research_status": result.get(
            "frozen_board_g4_research_status", "LEGACY_UNKNOWN"
        ),
        "certificate_completeness_recheck_required": result.get(
            "certificate_completeness_recheck_required", False
        ),
        "prior_certificate_reclassification_recheck_required": result.get(
            "prior_certificate_reclassification_recheck_required", False
        ),
        "execution_authorized": False,
    }

    if recheck_required:
        limitations.append("MARKET_DISAGREEMENT_RECHECK_REQUIRED")

    return {
        "ok": True,
        "status": (
            "MARKET_DISAGREEMENT_RECHECK_REQUIRED"
            if recheck_required
            else "OBSERVED_QUOTE_EVALUATED"
        ),
        "evidence": evidence,
        "model": model,
        "limitations": limitations,
        "bet_authorized": False,
        "model_bets_created": False,
        "priced_publication_authorized": False,
        "quote_research_required": recheck_required,
        "execution_authorized": False,
    }


def _football_receipt(c_input: dict[str, Any]) -> dict[str, Any]:
    _require_c(c_input, "football_assessment")
    result = run_football_assessment(c_input)
    return {
        "ok": True,
        "engine_execution_status": "EXECUTED_C_FOOTBALL_ONLY",
        "model": "c",
        "quotes_required": False,
        "quote_research_required": False,
        "model_bets_created": False,
        "model_accounting_status": "NONE",
        "result": result,
    }


def _decision_receipt(c_input: dict[str, Any]) -> dict[str, Any]:
    _require_c(c_input, "decision")
    result = run_decision(c_input)
    return {
        "ok": True,
        "engine_execution_status": "EXECUTED_C_DECISION",
        "model": "c",
        "result": result,
    }


def _football_and_optional_price(
    c_input: dict[str, Any],
    *,
    price_c: dict[str, Any] | None,
    screenshot: dict[str, Any] | None,
) -> dict[str, Any]:
    receipt = _football_receipt(c_input)
    if screenshot is not None:
        if price_c is not None:
            raise ValueError(
                "USER_SCREENSHOT_ONLY uses the screenshot quote directly; "
                "separate strict price payload is not used"
            )
        try:
            price = assess_user_screenshot(
                screenshot, c_input, receipt["result"]
            )
            mode = "FOOTBALL_AND_OBSERVED_QUOTE"
        except Exception as exc:
            price = {
                "ok": False,
                "status": ("G4_RESEARCH_REQUIRED" if str(exc).startswith("G4 RESEARCH REQUIRED")
                           else "PRODUCTION_SCOPE_BLOCKED" if str(exc).startswith("PRODUCTION SCOPE BLOCKED")
                           else "OBSERVED_QUOTE_INVALID"),
                "reason": str(exc),
                "execution_authorized": False,
                "bet_authorized": False,
            }
            mode = "FOOTBALL_ASSESSMENT"
        return {
            **receipt,
            "xi_mode": mode,
            "price_check": price,
        }

    if price_c is None:
        return {**receipt, "xi_mode": "FOOTBALL_ASSESSMENT"}

    _require_c(price_c, "decision")
    if (
        price_c.get("match", {}).get("match_id")
        != c_input.get("match", {}).get("match_id")
        or price_c.get("evidence_epoch_id") != c_input.get("evidence_epoch_id")
    ):
        raise ValueError(
            "strict C price decision must match football fixture/evidence epoch"
        )

    if c_input.get("context", {}).get("fixture_status") != "PREMATCH_CONFIRMED":
        return {
            **receipt,
            "xi_mode": "FOOTBALL_ASSESSMENT",
            "price_check": {
                "ok": False,
                "status": "EXECUTABLE_PRICE_NOT_AUTHORIZED",
                "reason": "started fixture; prematch executable-price path closed",
                "execution_authorized": False,
            },
        }

    try:
        priced = _decision_receipt(price_c)
    except Exception as exc:
        return {
            **receipt,
            "xi_mode": "FOOTBALL_ASSESSMENT",
            "price_check": {
                "ok": False,
                "status": "EXECUTABLE_PRICE_NOT_AUTHORIZED",
                "reason": str(exc),
                "execution_authorized": False,
            },
        }
    return {
        **receipt,
        "xi_mode": "FOOTBALL_AND_EXECUTABLE_PRICE_CHECK",
        "price_check": {
            "ok": True,
            "status": "EXECUTABLE_PRICE_DECISION_EXECUTED",
            "receipt": priced,
            "execution_authorized": True,
            "publication_requires_persistence_readback": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Football /xi single-C runtime")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("self-check")

    xi = sub.add_parser("xi")
    xi.add_argument("--c", required=True)
    xi.add_argument("--price-c")
    xi.add_argument("--screenshot-quote")

    decision = sub.add_parser("decision")
    decision.add_argument("--c", required=True)

    football = sub.add_parser("football")
    football.add_argument("--c", required=True)

    args = parser.parse_args()
    try:
        if args.command == "self-check":
            result = self_check()
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0 if result.get("ok") else 2

        c_input = _load(args.c)
        if args.command == "decision":
            result = _decision_receipt(c_input)
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        if args.command == "football":
            result = _football_receipt(c_input)
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0

        if c_input.get("stage") == "decision":
            if args.price_c or args.screenshot_quote:
                raise ValueError("decision-stage input does not accept a second price source")
            result = _decision_receipt(c_input)
            print(json.dumps({
                **result,
                "xi_mode": "STRICT_EXECUTABLE_PRICE_C",
            }, indent=2, sort_keys=True))
            return 0
        if c_input.get("stage") != "football_assessment":
            raise ValueError("/xi expects stage=football_assessment or stage=decision")

        output = _football_and_optional_price(
            c_input,
            price_c=_load(args.price_c) if args.price_c else None,
            screenshot=_load(args.screenshot_quote) if args.screenshot_quote else None,
        )
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0

    except Exception as exc:
        error_type = type(exc).__name__
        contract_types = {"ContractError", "ValueError", "KeyError", "JSONDecodeError"}
        is_contract = error_type in contract_types or isinstance(exc, ContractError)
        print(json.dumps({
            "ok": False,
            "status": (
                "XI ENGINE CONTRACT REJECTED"
                if is_contract
                else "XI RUNTIME: EXECUTION FAILED"
            ),
            "failure_class": (
                "PAYLOAD_OR_MODEL_CONTRACT"
                if is_contract
                else "PYTHON_OR_RUNTIME"
            ),
            "error_type": error_type,
            "error": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
