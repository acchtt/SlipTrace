#!/usr/bin/env python3
"""Single Airtable readback verifier for football-first /xi assessments.

The active /xi path persists C/C2 football results once and, when an observed
quote was evaluated, persists the normal evaluated line/odds fields. There is
no screenshot-specific serialized Evidence Summary protocol.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ACTIVE_BASE = "appbzxqXYf0lKfD4P"
STATUS_FIELD = "XI Assessment Execution Status"
STATUS_FIELD_ID = "fldkjs6Sykivp0fag"


class XIAssessmentReadbackError(ValueError):
    pass


def _stored_json(value, model: str) -> dict:
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as exc:
            raise XIAssessmentReadbackError(
                f"{model}: malformed stored JSON"
            ) from exc
    if not isinstance(value, dict):
        raise XIAssessmentReadbackError(f"{model}: stored result missing")
    return value


def _normal_quote(receipt: dict) -> dict | None:
    price = receipt.get("price_check")
    if not isinstance(price, dict) or price.get("ok") is not True:
        return None
    evidence = price.get("evidence")
    if not isinstance(evidence, dict):
        return None
    quote = evidence.get("quote")
    if not isinstance(quote, dict):
        return None
    line, odds = quote.get("line"), quote.get("odds")
    if not isinstance(line, (int, float)) or isinstance(line, bool):
        return None
    if not isinstance(odds, (int, float)) or isinstance(odds, bool):
        return None
    return {"line": float(line), "odds": float(odds)}


def verify_football_assessment(receipt: dict, refetched: dict) -> dict:
    if (
        not isinstance(receipt, dict)
        or receipt.get("ok") is not True
        or receipt.get("engine_execution_status")
        != "EXECUTED_C_C2_FOOTBALL_ONLY"
        or receipt.get("models_executed") != ["c", "c2"]
        or receipt.get("model_bets_created") is not False
    ):
        raise XIAssessmentReadbackError(
            "actual paired C+C2 football execution required"
        )

    results = receipt.get("results")
    if not isinstance(results, dict) or set(results) != {"c", "c2"}:
        raise XIAssessmentReadbackError(
            "complete independent C/C2 football results missing"
        )
    if (
        not isinstance(refetched, dict)
        or refetched.get("base_id") != ACTIVE_BASE
        or refetched.get("readback_method") != "INDEPENDENT_AIRTABLE_REFETCH"
        or not isinstance(refetched.get("record_id"), str)
        or not refetched["record_id"].startswith("rec")
        or not isinstance(refetched.get("assessment_id"), str)
        or not refetched["assessment_id"].strip()
    ):
        raise XIAssessmentReadbackError(
            "actual active Airtable record readback required"
        )

    price = receipt.get("price_check")
    expected_status = (
        "EXECUTED_C_C2_FOOTBALL_AND_PRICE"
        if isinstance(price, dict) and price.get("ok") is True
        else "EXECUTED_C_C2_FOOTBALL_ONLY"
    )
    if (
        refetched.get("xi_status_field_id") != STATUS_FIELD_ID
        or refetched.get("xi_assessment_execution_status") != expected_status
    ):
        raise XIAssessmentReadbackError(
            "XI assessment execution status differs from completed /xi result"
        )

    for model in ("c", "c2"):
        item = results[model]
        if (
            item.get("stage") != "football_assessment_result"
            or item.get("model") != model
            or item.get("football_assessment_completed") is not True
            or item.get("bet_authorized") is not False
        ):
            raise XIAssessmentReadbackError(
                f"{model}: incomplete or fictitious football assessment"
            )
        stored = _stored_json(refetched.get(f"engine_{model}_result"), model)
        if stored != item:
            raise XIAssessmentReadbackError(
                f"{model}: independent saved C/C2 result differs"
            )

    if (
        results["c"].get("match_id") != results["c2"].get("match_id")
        or refetched.get("match_id") != results["c"]["match_id"]
    ):
        raise XIAssessmentReadbackError(
            "stored match identity differs from paired engines"
        )

    quote = _normal_quote(receipt)
    quote_verified = False
    if quote is not None:
        if (
            refetched.get("evaluated_line") != quote["line"]
            or refetched.get("evaluated_odds") != quote["odds"]
        ):
            raise XIAssessmentReadbackError(
                "stored evaluated line/odds differ from observed quote"
            )
        quote_verified = True

    return {
        "status": "XI_PERSISTENCE_VERIFIED",
        "football_pair_verified": True,
        "observed_quote_readback_verified": quote_verified,
        "actual_bet_created": False,
        "record_id": refetched["record_id"],
        "assessment_id": refetched["assessment_id"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify independent Airtable readback of /xi assessment"
    )
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--readback", required=True)
    args = parser.parse_args()
    try:
        result = verify_football_assessment(
            json.loads(Path(args.receipt).read_text(encoding="utf-8")),
            json.loads(Path(args.readback).read_text(encoding="utf-8")),
        )
        print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({
            "ok": False,
            "status": "XI PERSISTENCE BLOCKED",
            "reason": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
