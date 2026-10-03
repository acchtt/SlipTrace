#!/usr/bin/env python3
"""Semantic authority QA for the current Football C production stack."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"missing file: {rel}")
    return path.read_text(encoding="utf-8")


failures: list[str] = []


def require(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle not in text:
            failures.append(f"{rel}: missing required semantic invariant: {needle}")


def forbid(rel: str, *needles: str) -> None:
    text = read(rel)
    for needle in needles:
        if needle in text:
            failures.append(f"{rel}: forbidden active-authority text present: {needle}")


# 1. One production authority.
require(
    "models/football/CURRENT_MODEL.md",
    "Active official model:** Football **C**",
    "retired historical Football A/shadow artifacts",
    "Step-2 fail-closed validator repair",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "Official model:** Football C",
    "Current execution authority:",
    "C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN",
)
forbid(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "Official model:** Football A",
    "Official:** Football A",
    "New Football A material decisions follow only",
    "Current Football A:",
    "Current Football A official states",
)

require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "Official model:** Football C",
    "Historical Football A/v0.2.x country/league blanket overlays are **not** current authority",
    "C2 supported burden",
)
forbid(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "For new Football A decisions",
    "current Step-2 state is compiled by",
    "Japanese domestic leagues, including J1, must not survive",
    "All Finnish domestic league competitions",
)

# 2. Legacy compilers/launcher must fail closed for new work.
for rel in (
    "models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md",
    "models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md",
):
    first = "\n".join(read(rel).splitlines()[:12])
    if "RETIRED FOR NEW FOOTBALL C PRODUCTION" not in first:
        failures.append(f"{rel}: legacy compiler is not visibly retired at file top")

require(
    "models/football/prompts/05_NORMAL_CHAT_FOOTBALL_C.md",
    "Status:** RETIRED — DO NOT USE FOR NEW PRODUCTION",
    "LAUNCHER RETIRED — USE CURRENT FOOTBALL C COMMAND ROUTER",
)

# 3. C2 must have genuinely separate policy plumbing.
require(
    "models/football/engine/core.py",
    "def c2_ranking_key",
    "def rank_assessments_c2",
    "C2 deliberately does NOT inherit Football C's burden-completion-first",
)
require(
    "models/football/engine/adapter.py",
    "rank_assessments_c2",
    'if model == "c"',
    "c2_ranking_key(item)",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "c_supported_line",
    "c2_supported_line",
    "Do **not** freeze one shared",
    "SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN",
)
require(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "independently frozen C2 supported line",
    "Do not reuse C's supported line in the C2 payload",
)
require(
    "models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md",
    "**C2 owns this field independently.**",
    "frozen route-quality ranking for C2",
)
require(
    "models/football/challengers/football-c2/TEST_PROTOCOL.md",
    "HELD AT ZERO",
    "Step-2 fail-closed validator repair",
    "five-board checkpoint restarts at zero",
    "zero Python C2 agreement weight",
)

# 5. Step-2 deterministic validation must fail closed.
require(
    "models/football/engine/schema.json",
    "\"main_failure\"",
    "\"h2h_state\"",
    "\"carrier_self_fund\"",
    "\"failure_attacks_route\"",
    "\"material_suppression\"",
    "\"xi_status\"",
    "\"post_xi_research_status\"",
    "\"h2h_review_status\"",
    "\"h2h_rechecked\"",
    "\"completion_rechecked\"",
    "\"primary_mechanism_intact\"",
)
require(
    "models/football/engine/adapter.py",
    "def _required_bool",
    "DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING",
    "DECISION BLOCKED — H2H RECHECK MISSING",
    "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING",
    "primary_mechanism_intact=_required_bool",
    "_required_bool(obj, \"material_suppression\")",
)
require(
    "models/football/engine/core.py",
    "current burden stall risk is HIGH",
    "current burden-completion quality is LOW",
    "current continuation quality is LOW",
    "primary scoring mechanism not intact",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_missing_xi_status_fails_closed",
    "test_missing_post_xi_research_status_fails_closed",
    "test_h2h_recheck_missing_blocks_decision",
    "test_completion_recheck_missing_blocks_decision",
    "test_missing_suppression_boolean_fails_closed",
    "test_missing_failure_attack_boolean_fails_closed",
    "test_high_current_stall_risk_cannot_bet",
    "test_low_current_completion_cannot_bet",
    "test_low_current_continuation_cannot_bet",
)

# 4. Persistence must have named current C/C2 separation.
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "C supported burden",
    "C2 supported burden",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "C Action",
    "C supported line",
    "C2 supported line",
    "C2 shadow action",
    "legacy generic",
)

if failures:
    print("FOOTBALL AUTHORITY QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — Football C authority and C2 comparison semantics are internally consistent.")
