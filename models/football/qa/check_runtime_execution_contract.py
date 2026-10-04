#!/usr/bin/env python3
"""Enforce the football runtime availability/execution contract."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]

failures: list[str] = []


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        failures.append(f"{rel}: missing file")
        return ""
    return path.read_text(encoding="utf-8")


def require(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle not in text:
            failures.append(f"{rel}: missing runtime invariant: {needle}")


def forbid(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle in text:
            failures.append(f"{rel}: forbidden runtime fallback present: {needle}")


COMMON = "models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md"

require(
    COMMON,
    "MANDATORY EXECUTION PRECHECK",
    "Do not infer tool or repository unavailability from environment shape.",
    "PYTHON PROBE: PASS",
    "REPOSITORY PROBE: PASS",
    "CONTAINER NETWORK UNAVAILABLE — NOT REPOSITORY UNAVAILABLE",
    "XI PORTABLE RUNTIME: PASS",
    "xi_portable.py self-check",
    "xi_portable.py triplet",
    "runtime_probe.py --stage <rank|xi|audit>",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
    "Do not write \"Python unavailable\" before a real probe fails.",
    "Do not write \"GitHub unavailable\" unless the actual GitHub connector/source call itself failed",
    "ENGINE EXECUTION FAILED — ATTEMPTED — <exact reason>",
)

require(
    "models/football/engine/runtime_probe.py",
    'STAGE_FILES = {',
    '"rank": (',
    '"xi": (',
    '"audit": (',
    "def probe_stage",
    "RUNTIME SOURCE PROBE: PASS",
    "RUNTIME SOURCE PROBE: FAIL",
)

require(
    "models/football/engine/xi_portable.py",
    "XI PORTABLE RUNTIME: PASS",
    "SOURCE_BLOB_SHA",
    "def self_check",
    "def run_triplet_files",
    "def run_reconcile_file",
    "def run_accounting_file",
    "model_bet_accounting",
)
require(
    "models/football/qa/check_xi_portable_runtime.py",
    "XI PORTABLE QA FAIL",
    "self_check",
    "stale embedded source",
)
require(
    "models/football/engine/tests/test_runtime_probe.py",
    "test_current_repo_runtime_probe_passes_all_stages",
    "test_rank_manifest_contains_both_board_engines",
    "test_xi_manifest_contains_triplet_and_reconciliation",
    "test_audit_manifest_contains_factor_calibration",
    "test_all_stages_include_model_accounting",
)

for rel in (
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
):
    require(rel, "FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md")

forbid(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "If runtime execution is unavailable:",
    "ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED",
)
forbid(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED",
)
forbid(
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
    "ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED",
)

require(
    "models/football/CURRENT_MODEL.md",
    "Mandatory deterministic runtime bootstrap",
    "Tool/repository availability is a **current-turn observed state**",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
    "network failure is not a valid \"GitHub unavailable\" reason",
)

require(
    "models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md",
    "Common runtime precheck:",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
    "xi_portable.py self-check",
    "xi_portable.py triplet",
    "portable bundle itself fails self-check",
    "raw-network failure while GitHub connector source remains accessible",
)

require(
    "models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md",
    "Runtime availability is also never inherited from a handoff.",
    "Re-probe the current turn before making any availability claim.",
)

if failures:
    print("FOOTBALL RUNTIME CONTRACT FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — football runtime availability claims require current-turn probes and execution evidence.")
