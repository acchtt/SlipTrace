#!/usr/bin/env python3
"""Independent Airtable readback of quote-free /xi C+C2 assessment.

Caller MUST read actual stored fields separately after writing. The
validator cannot itself attest external Airtable access. Never treats a
football-only assessment as a C-BET, an executable WAIT or a placed bet.
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


def verify_football_assessment(receipt: dict, refetched: dict) -> dict:
    if (not isinstance(receipt, dict)
        or receipt.get("ok") is not True
        or receipt.get("engine_execution_status") != "EXECUTED_C_C2_FOOTBALL_ONLY"
        or receipt.get("models_executed") != ["c","c2"]
        or receipt.get("model_bets_created") is not False):
        raise XIAssessmentReadbackError("actual paired C+C2 football execution required")
    results = receipt.get("results")
    if not isinstance(results, dict) or set(results) != {"c","c2"}:
        raise XIAssessmentReadbackError("complete independent C+C2 football results missing")
    if (not isinstance(refetched, dict)
            or refetched.get("base_id") != ACTIVE_BASE
            or refetched.get("readback_method") != "INDEPENDENT_AIRTABLE_REFETCH"
            or not isinstance(refetched.get("record_id"),str)
            or not refetched["record_id"].startswith("rec")
            or not isinstance(refetched.get("assessment_id"),str)
            or not refetched["assessment_id"].strip()):
        raise XIAssessmentReadbackError("actual active Airtable record readback required")
    price = receipt.get("price_check")
    if price and price.get("ok") is True:
        expected = "EXECUTED_C_C2_FOOTBALL_AND_PRICE"
    elif price:
        expected = "EXECUTED_C_C2_FOOTBALL_PRICE_BLOCKED"
    else:
        expected = "EXECUTED_C_C2_FOOTBALL_ONLY"
    if (refetched.get("xi_status_field_id") != STATUS_FIELD_ID
            or refetched.get("xi_assessment_execution_status") != expected):
        raise XIAssessmentReadbackError("new Airtable execution-status field not independently confirmed")
    for model in ("c","c2"):
        item = results[model]
        if (item.get("stage") != "football_assessment_result"
                or item.get("model") != model
                or item.get("football_assessment_completed") is not True
                or item.get("bet_authorized") is not False):
            raise XIAssessmentReadbackError(f"{model}: incomplete or fictitious football assessment")
        stored = refetched.get(f"engine_{model}_result")
        if isinstance(stored,str):
            try:
                stored=json.loads(stored)
            except json.JSONDecodeError as exc:
                raise XIAssessmentReadbackError(f"{model}: malformed stored JSON") from exc
        if stored != item:
            raise XIAssessmentReadbackError(f"{model}: independent saved C/C2 result differs")
    if (results["c"].get("match_id") != results["c2"].get("match_id")
            or refetched.get("match_id") != results["c"]["match_id"]):
        raise XIAssessmentReadbackError("stored match identity differs from paired engines")
    return {"status":"XI_FOOTBALL_ONLY_PERSISTENCE_VERIFIED",
            "record_id":refetched["record_id"],
            "assessment_id":refetched["assessment_id"],
            "match_id":results["c"]["match_id"],
            "xi_execution_status":expected,
            "football_pair_verified":True,
            "priced_publication_authorized":False,
            "actual_bet_created":False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--receipt",required=True)
    p.add_argument("--readback",required=True)
    args=p.parse_args()
    try:
        result=verify_football_assessment(
            json.loads(Path(args.receipt).read_text(encoding="utf-8")),
            json.loads(Path(args.readback).read_text(encoding="utf-8")))
        print(json.dumps({"ok":True,**result},indent=2,sort_keys=True))
        return 0
    except (OSError,ValueError) as exc:
        print(json.dumps({"ok":False,"status":"XI_FOOTBALL_ONLY_PERSISTENCE_UNVERIFIED",
                          "reason":str(exc)}),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
