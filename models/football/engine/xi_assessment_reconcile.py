#!/usr/bin/env python3
"""Single Google Sheets readback verifier for football-first /xi assessments.

The active /xi path persists the Football C result once and, when an observed
quote was evaluated, persists the normal evaluated line/odds fields. There is
no screenshot-specific serialized Evidence Summary protocol.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ACTIVE_SPREADSHEET_ID = "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM"
DECISION_SHEET = "Decision States"
STATUS_COLUMN = "XI Assessment Execution Status"


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
        or receipt.get("engine_execution_status") != "EXECUTED_C_FOOTBALL_ONLY"
        or receipt.get("model") != "c"
        or receipt.get("model_bets_created") is not False
    ):
        raise XIAssessmentReadbackError(
            "actual Football C football execution required"
        )

    item = receipt.get("result")
    if (
        not isinstance(item, dict)
        or item.get("stage") != "football_assessment_result"
        or item.get("model") != "c"
        or item.get("football_assessment_completed") is not True
        or item.get("bet_authorized") is not False
    ):
        raise XIAssessmentReadbackError(
            "incomplete or fictitious Football C assessment"
        )
    if (
        not isinstance(refetched, dict)
        or refetched.get("spreadsheet_id") != ACTIVE_SPREADSHEET_ID
        or refetched.get("sheet_name") != DECISION_SHEET
        or refetched.get("readback_method")
        != "INDEPENDENT_GOOGLE_SHEETS_REFETCH"
        or not isinstance(refetched.get("row_key"), str)
        or not refetched["row_key"].strip()
        or not isinstance(refetched.get("assessment_id"), str)
        or not refetched["assessment_id"].strip()
        or refetched.get("row_key") != refetched.get("assessment_id")
    ):
        raise XIAssessmentReadbackError(
            "actual active Google Sheets row readback required"
        )

    price = receipt.get("price_check")
    expected_status = (
        "EXECUTED_C_FOOTBALL_AND_PRICE"
        if isinstance(price, dict) and price.get("ok") is True
        else "EXECUTED_C_FOOTBALL_ONLY"
    )
    if (
        refetched.get("xi_status_column") != STATUS_COLUMN
        or refetched.get("xi_assessment_execution_status") != expected_status
    ):
        raise XIAssessmentReadbackError(
            "XI assessment execution status differs from completed /xi result"
        )

    stored = _stored_json(refetched.get("engine_c_result"), "c")
    if stored != item:
        raise XIAssessmentReadbackError(
            "independent saved Football C result differs"
        )
    if refetched.get("match_id") != item.get("match_id"):
        raise XIAssessmentReadbackError(
            "stored match identity differs from Football C engine"
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
        "football_c_verified": True,
        "observed_quote_readback_verified": quote_verified,
        "actual_bet_created": False,
        "row_key": refetched["row_key"],
        "assessment_id": refetched["assessment_id"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify independent Google Sheets readback of /xi assessment"
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
