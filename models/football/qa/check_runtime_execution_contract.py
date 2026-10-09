#!/usr/bin/env python3
"""Enforce current-turn execution plumbing for the active Football C+C2 roster."""

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
            failures.append(f"{rel}: forbidden retired/fallback invariant present: {needle}")


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
    "xi_source_handoff.py",
    "XI SOURCE HANDOFF: PASS",
    "SOURCE_TRANSPORT_BLOCKED",
    "xi_portable.py pair",
    "xi_portable.py accounting",
    "runtime_probe.py --stage <rank|xi|audit>",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
    "Do not write \"Python unavailable\" before a real probe fails.",
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
    "decision_pair_cli.py",
)

require(
    "models/football/engine/xi_portable.py",
    "XI PORTABLE RUNTIME: PASS",
    "SOURCE_BLOB_SHA",
    "def self_check",
    "def run_pair_files",
    "def run_reconcile_file",
    "def run_accounting_file",
    "EXECUTED_C_C2_PAIR",
    "active_models",
)
forbid(
    "models/football/engine/xi_portable.py",
    "def run_triplet_files",
    "decision_triplet_cli",
    "EXECUTED_ALL_THREE",
)

require(
    "models/football/engine/xi_source_handoff.py",
    "def git_blob_sha",
    "def stage_source",
    "os.replace",
    "XI SOURCE HANDOFF: PASS",
    "XI SOURCE HANDOFF: FAIL",
    "source blob mismatch",
)

require(
    "models/football/engine/decision_pair_cli.py",
    'EXPECTED_MODELS = ("c", "c2")',
    "def run_pair",
    "EXECUTED_C_C2_PAIR",
    "same frozen common evidence epoch",
)

require(
    "models/football/qa/check_xi_portable_runtime.py",
    "XI PORTABLE QA FAIL",
    "self_check",
    "stale embedded source",
)

require(
    "models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md",
    "Active models:** Football C official + Football C2 shadow",
    "python xi_portable.py pair --c <c.json> --c2 <c2.json>",
    "ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR",
    "decision_pair_cli.py",
    "C3/C4 are never required for new Step-2 completion",
)
forbid(
    "models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md",
    "EXECUTED_ALL_THREE",
    "xi_portable.py triplet",
)

for rel in (
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
):
    require(rel, "FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md")

for rel in (
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
):
    forbid(rel, "ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED")

require(
    "models/football/CURRENT_MODEL.md",
    "Mandatory deterministic runtime bootstrap",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
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

print("PASS — active C+C2 runtime requires current-turn probes and atomic pair execution.")
