#!/usr/bin/env python3
"""Check that active football execution has one direct runtime path."""

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
            failures.append(f"{rel}: obsolete mechanism remains active: {needle!r}")


require(
    "models/football/engine/xi_portable.py",
    "THIN_SHARED_MODULES",
    "from adapter import ContractError, evaluate_observed_quote",
    "from decision_pair_cli import run_football_pair, run_pair",
    "def self_check",
)
forbid(
    "models/football/engine/xi_portable.py",
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "def run_reconcile_file",
    "def run_accounting_file",
)

require(
    "models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md",
    "thin shared runtime",
    "No transport bootstrap",
    "xi_portable.py xi",
)
forbid(
    "models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md",
    "xi_source_handoff.py",
    "runtime_probe.py",
    "SOURCE_TRANSPORT_BLOCKED",
    "MANDATORY EXECUTION PRECHECK",
)

require(
    "models/football/qa/check_xi_portable_runtime.py",
    "THIN_SHARED_MODULES",
    "embedded-source mechanism returned",
)
require(
    "models/football/qa/check_xi_portable_execution.py",
    "thin /xi runner",
    "deterministic strict pair",
)

if failures:
    print("FOOTBALL RUNTIME CONTRACT FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active /xi execution is one thin runtime over shared C/C2 modules.")
