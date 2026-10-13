#!/usr/bin/env python3
"""Verify the active /xi thin runner loads the real shared C/C2 modules."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "models/football/engine/xi_portable.py"

spec = importlib.util.spec_from_file_location("xi_runtime_guarded", RUNNER)
if spec is None or spec.loader is None:
    raise SystemExit("XI RUNTIME QA FAIL — unable to load runner")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

failures: list[str] = []
result = module.self_check()
if not result.get("ok"):
    failures.append(f"self-check failed: {result}")
if result.get("runtime_mode") != "THIN_SHARED_MODULES":
    failures.append("xi runner is not using THIN_SHARED_MODULES")

text = RUNNER.read_text(encoding="utf-8")
for forbidden in (
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "SOURCES =",
    "exec(compile(",
):
    if forbidden in text:
        failures.append(f"embedded-source mechanism returned: {forbidden}")

for required in (
    "from adapter import ContractError, evaluate_observed_quote",
    "from decision_pair_cli import run_football_pair, run_pair",
):
    if required not in text:
        failures.append(f"missing shared-module import: {required}")

if failures:
    print("XI RUNTIME QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — /xi uses one thin runner over the real C/C2 modules.")
