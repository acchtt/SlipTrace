#!/usr/bin/env python3
"""Thin active /xi runner for Football C official + C2 shadow.

The former generated self-contained source bundle duplicated core.py, adapter.py,
reconciliation and accounting inside this file. The active runtime now imports
those checked-out modules directly. The transport artifact ships this file
beside its real dependencies, so there is one source of truth for C/C2 policy.

User-facing behavior:
- football assessment never requires odds;
- an observed/screenshot quote gets a model ACT/WAIT/PASS comparison through
  adapter.evaluate_observed_quote(), with no execution authority;
- a genuinely executable current quote uses the strict decision pair;
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

from adapter import ContractError, evaluate_observed_quote
from decision_pair_cli import run_football_pair, run_pair


MIN_PYTHON = (3, 10)


def self_check() -> dict[str, Any]:
    if sys.version_info[:2] < MIN_PYTHON:
        return {
            "ok": False,
            "status": "XI RUNTIME: FAIL",
            "error": f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required",
        }
    required = (run_football_pair, run_pair, evaluate_observed_quote)
    if not all(callable(item) for item in required):
        return {
            "ok": False,
            "status": "XI RUNTIME: FAIL",
            "error": "required C/C2 runtime callables are missing",
        }
    return {
        "ok": True,
        "status": "XI RUNTIME: PASS",
        "active_models": ["c", "c2"],
        "runtime_mode": "THIN_SHARED_MODULES",
        "python_version": ".".join(map(str, sys.version_info[:3])),
        "shared_modules": ["core", "adapter", "decision_pair_cli"],
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


def run_football_pair_files(c: str, c2: str) -> dict[str, Any]:
    return run_football_pair(_load(c), _load(c2))


def run_pair_files(c: str, c2: str) -> dict[str, Any]:
    return run_pair(_load(c), _load(c2))


def assess_user_screenshot(
    screenshot: dict[str, Any],
    c_football: dict[str, Any],
    c2_football: dict[str, Any],
    football: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate the exact user screenshot as non-executable quote evidence."""

    if screenshot.get("evidence_mode") != "USER_SCREENSHOT_ONLY":
        raise ValueError("screenshot evidence_mode must be USER_SCREENSHOT_ONLY")
    if screenshot.get("source") != "USER_SCREENSHOT":
        raise ValueError("screenshot source must be USER_SCREENSHOT")
    capture_reference = screenshot.get("capture_reference")
    if not isinstance(capture_reference, str) or not capture_reference.strip():
        raise ValueError("original screenshot capture_reference required")

    match_id = football["results"]["c"]["match_id"]
    if screenshot.get("match_id") != match_id:
        raise ValueError("screenshot match_id differs from C/C2 football fixture")
    if football["results"]["c2"]["match_id"] != match_id:
        raise ValueError("C/C2 football fixture mismatch")

    quote = _quote(screenshot.get("quote"))
    c_ctx = c_football.get("context")
    c2_ctx = c2_football.get("context")
    if not isinstance(c_ctx, dict) or not isinstance(c2_ctx, dict):
        raise ValueError("C/C2 football contexts required")
    fixture = c_ctx.get("fixture_status")
    if c2_ctx.get("fixture_status") != fixture or screenshot.get("fixture_status") != fixture:
        raise ValueError("screenshot fixture status conflicts with C/C2 football evidence")

    assessment_time = _time(c_ctx.get("assessment_at_utc"), "assessment_at_utc")
    if _time(c2_ctx.get("assessment_at_utc"), "assessment_at_utc") != assessment_time:
        raise ValueError("C/C2 assessment times differ")
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

    model_results = {
        "c": evaluate_observed_quote(c_football, quote),
        "c2": evaluate_observed_quote(c2_football, quote),
    }
    models = {}
    for model, result in model_results.items():
        models[model] = {
            "supported_line": result["supported_line"],
            "snapshot_line_relation": result["line_relation"],
            "conditional_action": result["action"],
            "reason": result["reason"],
            "wait_target_line": result.get("wait_target_line"),
            "wait_min_odds": result.get("wait_min_odds"),
            "wait_reachable": result.get("wait_reachable"),
            "wait_reachability_basis": result.get("wait_reachability_basis"),
            "bridge_used": result.get("bridge_used", False),
            "execution_authorized": False,
        }

    return {
        "ok": True,
        "status": "OBSERVED_QUOTE_EVALUATED",
        "evidence": evidence,
        "models": models,
        "limitations": limitations,
        "bet_authorized": False,
        "model_bets_created": False,
        "priced_publication_authorized": False,
        "quote_research_required": False,
        "execution_authorized": False,
    }


def _football_and_optional_price(
    c_input: dict[str, Any],
    c2_input: dict[str, Any],
    *,
    price_c: dict[str, Any] | None,
    price_c2: dict[str, Any] | None,
    screenshot: dict[str, Any] | None,
) -> dict[str, Any]:
    football = run_football_pair(c_input, c2_input)
    if screenshot is not None:
        if price_c is not None or price_c2 is not None:
            raise ValueError(
                "USER_SCREENSHOT_ONLY uses the screenshot quote directly; "
                "separate priced-decision payloads are not used"
            )
        try:
            price = assess_user_screenshot(
                screenshot, c_input, c2_input, football
            )
            mode = "FOOTBALL_AND_OBSERVED_QUOTE"
        except Exception as exc:
            price = {
                "ok": False,
                "status": "OBSERVED_QUOTE_INVALID",
                "reason": str(exc),
                "execution_authorized": False,
                "bet_authorized": False,
            }
            mode = "FOOTBALL_ASSESSMENT"
        return {
            "ok": True,
            "xi_mode": mode,
            **football,
            "price_check": price,
        }

    if price_c is None and price_c2 is None:
        return {"ok": True, "xi_mode": "FOOTBALL_ASSESSMENT", **football}
    if price_c is None or price_c2 is None:
        raise ValueError("both C and C2 strict price inputs are required")

    # Strict executable-price decisions are separate from observed-quote
    # comparison and retain all adapter execution guards. Failure of the price
    # gate never erases the already-completed football assessment.
    try:
        priced = run_pair(price_c, price_c2)
    except Exception as exc:
        return {
            "ok": True,
            "xi_mode": "FOOTBALL_ASSESSMENT",
            **football,
            "price_check": {
                "ok": False,
                "status": "EXECUTABLE_PRICE_NOT_AUTHORIZED",
                "reason": str(exc),
                "execution_authorized": False,
            },
        }
    return {
        "ok": True,
        "xi_mode": "FOOTBALL_AND_EXECUTABLE_PRICE_CHECK",
        **football,
        "price_check": {
            "ok": True,
            "status": "EXECUTABLE_PRICE_DECISION_EXECUTED",
            "receipt": priced,
            "execution_authorized": True,
            "publication_requires_persistence_readback": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Football /xi C+C2 runtime"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("self-check")

    xi = sub.add_parser("xi")
    xi.add_argument("--c", required=True)
    xi.add_argument("--c2", required=True)
    xi.add_argument("--price-c")
    xi.add_argument("--price-c2")
    xi.add_argument("--screenshot-quote")

    pair = sub.add_parser("pair")
    pair.add_argument("--c", required=True)
    pair.add_argument("--c2", required=True)

    football_pair = sub.add_parser("football-pair")
    football_pair.add_argument("--c", required=True)
    football_pair.add_argument("--c2", required=True)

    args = parser.parse_args()
    try:
        if args.command == "self-check":
            result = self_check()
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0 if result.get("ok") else 2

        if args.command == "pair":
            result = run_pair_files(args.c, args.c2)
            print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
            return 0

        if args.command == "football-pair":
            result = run_football_pair_files(args.c, args.c2)
            print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
            return 0

        c_input, c2_input = _load(args.c), _load(args.c2)
        if c_input.get("stage") != c2_input.get("stage"):
            raise ValueError("C+C2 must use the same /xi stage")
        if c_input.get("stage") == "decision":
            if args.price_c or args.price_c2 or args.screenshot_quote:
                raise ValueError("decision-stage pair does not accept a second price source")
            result = run_pair(c_input, c2_input)
            print(json.dumps({
                "ok": True,
                "xi_mode": "STRICT_EXECUTABLE_PRICE_PAIR",
                **result,
            }, indent=2, sort_keys=True))
            return 0
        if c_input.get("stage") != "football_assessment":
            raise ValueError("/xi expects stage=football_assessment or stage=decision")

        output = _football_and_optional_price(
            c_input,
            c2_input,
            price_c=_load(args.price_c) if args.price_c else None,
            price_c2=_load(args.price_c2) if args.price_c2 else None,
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
