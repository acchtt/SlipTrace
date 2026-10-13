#!/usr/bin/env python3
"""Active-authority consistency check for Football v2.

This intentionally checks only the production stack:
V4 sweep/rank, Football C official + C2 shadow, one /xi assessment path,
one Airtable routing manifest, and Actual Bets as user-P/L authority.

Retired V1-V3 code and experimental QA may remain in Git history or dormant
files, but production launchers/CI must not depend on them.
"""

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
            failures.append(f"{rel}: obsolete/duplicate mechanism present {needle!r}")


# Command authority
require(
    "models/football/CURRENT_MODEL.md",
    "ACTIVE STACK",
    "Football C",
    "Football C2",
    "models/football/stages_v4/SWEEP.md",
    "models/football/stages_v4/RANK.md",
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "Actual Bets — Current",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "/sweep",
    "/rank",
    "/xi",
    "/live",
    "/audit",
    "/report",
    "V4",
)
forbid(
    "models/football/prompts/COMMAND_ALIASES.md",
    "work_ready",
    "Step0 ZIP",
    "rank reassess",
)

# V4 intake/rank
require(
    "models/football/stages_v4/SWEEP.md",
    "DATE_SURFACE_BATCH_V2",
    "GOALS-FIRST",
    "USER_AFRICA_DOMESTIC_EXCLUSION",
    "UEFA Youth League",
)
require(
    "models/football/stages_v4/stage.py",
    "verify_rank_source_and_status",
    "V4_RANK_EXECUTED_AWAITING_AIRTABLE_READBACK",
    "V4_RANK_PERSISTENCE_VERIFIED",
    "model_evidence_readback_verified",
)
require(
    "models/football/stages_v4/RANK.md",
    "original-source replay",
    "full-cohort",
    "Step1 Engine C Result",
    "Step1 Engine C2 Result",
)

# One Step2 authorization chain, no second source replay.
require(
    "models/football/engine/step2_queue_guard.py",
    'football-step2-queue-v2',
    "V4_RANK_PERSISTENCE_VERIFIED",
    "model_evidence_sha256",
    "EXCEPTION_ONLY",
)
forbid(
    "models/football/engine/step2_queue_guard.py",
    "work_ready",
    "TERMINAL_COMPLETE",
    "v4_original_source",
    "v4_status_refresh",
    "validate_v4_queue_authority",
)

# One model quote policy + separate execution authorization.
require(
    "models/football/engine/core.py",
    "class ModelQuoteContext",
    "def evaluate_c_quote",
    "def evaluate_c2_quote",
    "def decide_c",
    "def decide_c2",
)
require(
    "models/football/engine/adapter.py",
    "def evaluate_observed_quote",
    "def run_football_assessment",
    "def run_decision",
    "reachable WAIT requires",
)
require(
    "models/football/engine/xi_portable.py",
    "THIN_SHARED_MODULES",
    "OBSERVED_QUOTE_EVALUATED",
    "EXECUTABLE_PRICE_DECISION_EXECUTED",
)
forbid(
    "models/football/engine/xi_portable.py",
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "MAX_ASSESSMENT_LIVE_DECAY_GAP",
    "ASSESSMENT_WAIT_IS_PREDECLARED_DECAY_PLAN",
)

# Screenshot is normal observed quote evidence, not a parallel persistence protocol.
require(
    "models/football/engine/xi_assessment_reconcile.py",
    "evaluated_line",
    "evaluated_odds",
    "XI_PERSISTENCE_VERIFIED",
)
forbid(
    "models/football/engine/xi_assessment_reconcile.py",
    "USER_SCREENSHOT_ONLY_JSON=",
    "EVIDENCE_SUMMARY_FIELD_ID",
    "screenshot_evidence_summary_line",
)

# Strict publication is one exact pair + one readback, no second execution/reconcile.
require(
    "models/football/engine/step2_publication_guard.py",
    "football-step2-publication-v2",
    "pair_receipt",
    "decision_state_snapshot",
    "readback_verified",
)
forbid(
    "models/football/engine/step2_publication_guard.py",
    "run_pair(",
    "step2_reconcile",
)

# No synthetic active accounting.
forbid(
    "models/football/engine/model_bet_accounting.py",
    "WATCH_ASSUMED",
    "SHADOW_WATCH_ASSUMED",
    "WAIT_ASSUMED",
    "SHADOW_WAIT_ASSUMED",
)
require(
    "models/football/engine/model_bet_accounting.py",
    "WAIT_USER_CONFIRMED",
    "WATCH is classification only",
)

# Airtable has one machine-readable active routing authority.
routing_path = ROOT / "models/football/airtable/ACTIVE_MODEL_ROUTING.json"
try:
    routing = json.loads(routing_path.read_text(encoding="utf-8"))
    if routing.get("base_id") != "appbzxqXYf0lKfD4P":
        failures.append("ACTIVE_MODEL_ROUTING.json: wrong active base")
    if routing.get("c_official_only") is not True:
        failures.append("ACTIVE_MODEL_ROUTING.json: C official authority missing")
    if routing.get("c2_shadow_only") is not True:
        failures.append("ACTIVE_MODEL_ROUTING.json: C2 shadow authority missing")
except Exception as exc:
    failures.append(f"ACTIVE_MODEL_ROUTING.json unreadable: {exc}")

# Current docs must describe the simplified path rather than resurrecting wrappers.
for rel in (
    "models/football/CURRENT_MODEL.md",
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "models/football/procedures/FOOTBALL_SIMPLE_ASSESS_AND_BET.md",
):
    forbid(
        rel,
        "xi_v4_queue.py",
        "step2_reconcile.py",
        "step2_fixture_transition.py",
        "WAIT_ASSUMED",
        "WATCH_ASSUMED",
        "MAX_ASSESSMENT_LIVE_DECAY_GAP",
        "ASSESSMENT_WAIT_IS_PREDECLARED_DECAY_PLAN",
    )

# Production CI must not execute retired V1-V3 mechanics.
workflow = ".github/workflows/football-step2-research-gate.yml"
forbid(
    workflow,
    "sweep_checkpoint.py",
    "capacity_replenishment.py",
    "rank_terminal_status.py",
    "repaired_handoff_normalize.py",
    "step0_handoff_cli.py",
    "xi_source_handoff.py",
    "step2_reconcile.py",
)
require(
    workflow,
    "check_post_xi_research_gate.py",
    "check_authority_consistency.py",
    "check_runtime_execution_contract.py",
    "check_xi_portable_runtime.py",
)

if failures:
    print("FOOTBALL ACTIVE AUTHORITY FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — simplified active authority: V4 + C/C2 + one quote policy + one persistence/publication chain.")
