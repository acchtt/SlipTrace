#!/usr/bin/env python3
"""Verify the active /xi thin runner loads only the active Football C path."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "models/football/engine"
RUNNER = ENGINE / "xi_portable.py"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))

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
if result.get("active_models") != ["c"]:
    failures.append("xi runner active_models must be ['c']")
if result.get("retired_models") != ["c2", "c3", "c4"]:
    failures.append("xi runner retired roster mismatch")

text = RUNNER.read_text(encoding="utf-8")
for forbidden in (
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "SOURCES =",
    "exec(compile(",
    "decision_pair_cli",
    "run_football_pair",
    "run_pair(",
    "--c2",
):
    if forbidden in text:
        failures.append(f"overlapping runtime mechanism returned: {forbidden}")

for required in (
    "run_football_assessment",
    "run_decision",
    "evaluate_observed_quote",
):
    if required not in text:
        failures.append(f"missing shared C runtime callable: {required}")

if failures:
    print("XI RUNTIME QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — /xi uses one thin runner over the real Football C modules.")
