#!/usr/bin/env python3
"""Production invariants for the simplified active Football C+C2 stack."""

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
    '"source_replayed": True',
    '"current_fixture_status_checked": True',
    "V4_RANK_PERSISTENCE_VERIFIED",
)
require(
    "models/football/engine/step2_queue_guard.py",
    'VERSION = "football-step2-queue-v2"',
    '"V4_ROUTINE", "EXCEPTION_ONLY"',
    "model_evidence_readback_verified",
    "source_replayed",
    "current_fixture_status_checked",
)
forbid(
    "models/football/engine/step2_queue_guard.py",
    '"ROUTINE"',
    "work_ready",
    "TERMINAL_COMPLETE",
    "validate_v4_queue_authority",
    "v4_original_source",
    "v4_status_refresh",
)
require(
    "models/football/engine/core.py",
    "class ModelQuoteContext",
    "def evaluate_c_quote",
    "def evaluate_c2_quote",
    "def model_wait_target",
)
require(
    "models/football/engine/adapter.py",
    "def evaluate_observed_quote",
    "def run_decision",
    "wait_reachable=true",
    "model_accounting_status",
)
require(
    "models/football/engine/xi_portable.py",
    "THIN_SHARED_MODULES",
    "evaluate_observed_quote",
    "FOOTBALL_AND_OBSERVED_QUOTE",
    "FOOTBALL_AND_EXECUTABLE_PRICE_CHECK",
)
forbid(
    "models/football/engine/xi_portable.py",
    "SOURCE_BLOB_SHA",
    "_restore_pinned_sources",
    "ASSESSMENT_WAIT_IS_PREDECLARED_DECAY_PLAN",
    "MAX_ASSESSMENT_LIVE_DECAY_GAP",
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
    "WAIT_USER_CONFIRMED",
    "WATCH is classification only",
)
require(
    "models/football/engine/step2_publication_guard.py",
    'football-step2-publication-v2',
    "pair_receipt",
    "decision_state_snapshot",
    "readback_verified",
)
forbid(
    "models/football/engine/step2_publication_guard.py",
    "run_pair(",
    "step2_reconcile",
)
for rel in (
    "models/football/engine/core.py",
    "models/football/engine/adapter.py",
    "models/football/engine/schema.json",
):
    forbid(rel, "decide_c3", "rank_assessments_c3", '"c3"')

if failures:
    print("ACTIVE FOOTBALL STACK REGRESSION")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — active stack is V4 + C official/C2 shadow with one quote policy and no synthetic WAIT/WATCH exposure.")
