#!/usr/bin/env python3
"""Check that active football execution has one direct Football C runtime path."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
failures: list[str] = []

def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        failures.append(f"{rel}: missing")
        return ""
    return path.read_text(encoding="utf-8")

def require(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle not in text:
            failures.append(f"{rel}: missing {needle!r}")

def forbid(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle in text:
            failures.append(f"{rel}: obsolete/overlapping mechanism remains active: {needle!r}")

require(
    "models/football/engine/xi_portable.py",
    "THIN_SHARED_MODULES",
    "run_football_assessment",
    "run_decision",
    "evaluate_observed_quote",
    "def self_check",
)
forbid(
    "models/football/engine/xi_portable.py",
    "decision_pair_cli",
    "run_football_pair",
    "run_pair",
    "--c2",
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "def run_reconcile_file",
    "def run_accounting_file",
)

require(
    "models/football/qa/check_xi_portable_runtime.py",
    "THIN_SHARED_MODULES",
    'active_models") != ["c"]',
)
require(
    "models/football/qa/check_xi_portable_execution.py",
    "single-C /xi runner",
    "EXECUTED_C_DECISION",
    "EXECUTED_C_FOOTBALL_ONLY",
)

if failures:
    print("FOOTBALL RUNTIME CONTRACT FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active /xi execution is one thin runtime over Football C shared modules.")
