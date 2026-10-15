#!/usr/bin/env python3
"""Fail-closed consistency scan for the single active Football C authority."""

from __future__ import annotations

import json
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
            failures.append(f"{rel}: missing active invariant {needle!r}")

def forbid(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle in text:
            failures.append(f"{rel}: overlapping/retired mechanism remains active: {needle!r}")

# Human-facing authority.
require(
    "models/football/CURRENT_MODEL.md",
    "Official and only active model",
    "C2, C3 and C4",
    "There is no active shadow model",
    "models/football/stages_v4/SWEEP.md",
    "models/football/stages_v4/RANK.md",
    "Actual Bets — Current",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "/sweep", "/rank", "/xi", "/live", "/audit", "/report",
    "C2/C3/C4: retired for all new work",
)
require(
    "models/football/stages_v4/RANK.md",
    "single-C rank",
    "Step1 Engine C Result",
    "C2/C3/C4 are retired",
)
forbid(
    "models/football/stages_v4/RANK.md",
    "Step1 Engine C2 Result JSON",
    "Run the deterministic paired C/C2",
    "--c2 c2.json",
)

# Active Python execution surface must be single-model.
require(
    "models/football/engine/adapter.py",
    'ACTIVE_MODEL = "c"',
    "active production model must be 'c'",
)
require(
    "models/football/stages_v4/stage.py",
    "from adapter import run_board",
    '"active_model": "c"',
)
forbid(
    "models/football/stages_v4/stage.py",
    "from board_pair_cli",
    "run_board_pair",
    'STEP1_ENGINE_RESULT_FIELD_IDS["c2"]',
)
require(
    "models/football/engine/xi_portable.py",
    "EXECUTED_C_FOOTBALL_ONLY",
    "EXECUTED_C_DECISION",
    "from adapter import",
)
forbid(
    "models/football/engine/xi_portable.py",
    "decision_pair_cli",
    "run_pair(",
    "run_football_pair(",
    "--c2",
)
require(
    "models/football/engine/step2_queue_guard.py",
    "V4_RANK_PERSISTENCE_VERIFIED",
    "V4 Football C board missing",
)
forbid(
    "models/football/engine/step2_queue_guard.py",
    "C/C2",
    "c2_supported_line",
    "c2_shadow_state",
)
require(
    "models/football/engine/step2_publication_guard.py",
    "football-step2-publication-v3",
    "EXECUTED_C_DECISION",
    "engine_c_result",
)
forbid(
    "models/football/engine/step2_publication_guard.py",
    "EXECUTED_C_C2_PAIR",
    "engine_c2_result",
    "c2_shadow_action",
)

# Routing is machine authority.
routing_path = ROOT / "models/football/google_sheets/ACTIVE_STORE_ROUTING.json"
try:
    routing = json.loads(routing_path.read_text(encoding="utf-8"))
    if routing.get("spreadsheet_id") != "1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM":
        failures.append("ACTIVE_STORE_ROUTING.json: wrong active spreadsheet")
    if routing.get("active_models") != ["c"]:
        failures.append("ACTIVE_STORE_ROUTING.json: active_models must be ['c']")
    if routing.get("retired_models") != ["c2", "c3", "c4"]:
        failures.append("ACTIVE_STORE_ROUTING.json: retired model roster mismatch")
    if routing.get("c_official_only") is not True:
        failures.append("ACTIVE_STORE_ROUTING.json: C official authority missing")
    if routing.get("readback_method") != "INDEPENDENT_GOOGLE_SHEETS_REFETCH":
        failures.append("ACTIVE_STORE_ROUTING.json: wrong readback method")
    legacy = routing.get("legacy_airtable", {})
    if legacy.get("policy") != "HISTORICAL_READ_ONLY_NO_NEW_WRITES":
        failures.append("ACTIVE_STORE_ROUTING.json: Airtable must be historical read-only")
    step1 = routing.get("step1_engine_result", {})
    if step1.get("column_name") != "Step1 Engine C Result":
        failures.append("ACTIVE_STORE_ROUTING.json: Step1 C result column mismatch")
except Exception as exc:
    failures.append(f"ACTIVE_STORE_ROUTING.json unreadable: {exc}")

# Active docs must not create a second model policy.
for rel in (
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md",
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
    "models/football/prompts/06_NORMAL_CHAT_REPORT.md",
):
    forbid(
        rel,
        "C2 shadow",
        "run C and C2",
        "C+C2",
        "C/C2",
    )

# Active production authority must not route new persistence to Airtable.
for rel in (
    "models/football/CURRENT_MODEL.md",
    "models/football/prompts/COMMAND_ALIASES.md",
    "models/football/stages_v4/RANK.md",
    "models/football/stages_v4/stage.py",
    "models/football/engine/xi_assessment_reconcile.py",
):
    forbid(
        rel,
        "INDEPENDENT_AIRTABLE_REFETCH",
        "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK",
        "active_base_id",
    )

# Dormant historical implementation may remain, but no active launcher/workflow
# is allowed to import it.
for rel in (
    "models/football/stages_v4/stage.py",
    "models/football/engine/xi_portable.py",
    "models/football/engine/step2_queue_guard.py",
    "models/football/engine/step2_publication_guard.py",
):
    forbid(rel, "board_pair_cli", "decision_pair_cli")

if failures:
    print("FOOTBALL ACTIVE AUTHORITY FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — one active model authority: V4 + Football C; C2/C3/C4 are historical read-only.")
