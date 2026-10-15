#!/usr/bin/env python3
"""Production invariants for the single active Football C stack."""

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
            failures.append(f"{rel}: forbidden active mechanism {needle!r}")

require(
    "models/football/stages_v4/stage.py",
    "V4_SOURCE_REPLAY_REQUIRED",
    "V4_STATUS_REFRESH_INCOMPLETE",
    '"active_model": "c"',
    '"retired_models": ["c2", "c3", "c4"]',
    "V4_RANK_PERSISTENCE_VERIFIED",
    "from adapter import run_board",
)
forbid(
    "models/football/stages_v4/stage.py",
    "run_board_pair",
    "--c2",
    "c2_shadow_only",
)

require(
    "models/football/engine/adapter.py",
    'ACTIVE_MODEL = "c"',
    "def _active_model",
    "def evaluate_observed_quote",
    "def run_decision",
)
require(
    "models/football/engine/xi_portable.py",
    "THIN_SHARED_MODULES",
    'active_models": ["c"]',
    "EXECUTED_C_FOOTBALL_ONLY",
    "EXECUTED_C_DECISION",
    "FOOTBALL_AND_OBSERVED_QUOTE",
)
forbid(
    "models/football/engine/xi_portable.py",
    "decision_pair_cli",
    "run_football_pair",
    "run_pair",
    "--c2",
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
)

require(
    "models/football/engine/step2_publication_guard.py",
    "football-step2-publication-v3",
    "decision_receipt",
    "engine_c_result",
    "readback_verified",
)
forbid(
    "models/football/engine/step2_publication_guard.py",
    "pair_receipt",
    "engine_c2_result",
    "c2_shadow_action",
)

forbid(
    "models/football/engine/model_bet_accounting.py",
    "WATCH_ASSUMED",
    "SHADOW_WATCH_ASSUMED",
    "WAIT_ASSUMED",
    "SHADOW_WAIT_ASSUMED",
)
require(
    "models/football/engine/model_bet_accounting.py",
    'ACTIVE_MODELS = ("c",)',
    "WAIT_USER_CONFIRMED",
    "WATCH is classification only",
)

if failures:
    print("ACTIVE FOOTBALL STACK REGRESSION")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active stack is V4 + Football C only; retired models have no execution dependency.")
