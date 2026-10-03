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
    "Shadow challengers:** Football **C2** and Football **C3**",
    "retired historical Football A/shadow artifacts",
    "Step-2 fail-closed validator repair",
    "C3 burden-funding prospective test",
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
    "Do not reuse C's supported line in C2 or C3 payloads",
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

# 4. C3 must be a separate burden-funding shadow policy.
require(
    "models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md",
    "PROSPECTIVE SHADOW CHALLENGER",
    "two plausible scoring routes is descriptive only",
    "BURDEN_CONTRIBUTING",
    "EXCHANGE_ONLY",
    "STATE_DEPENDENT",
    "Who prospectively funds the goal",
    "C3-FOCUS requires LOW control-endpoint risk",
    "C3 has no C2-style market-gap bridge",
    "FOOTBALL C3 — SHADOW ONLY",
)
require(
    "models/football/challengers/football-c3/TEST_PROTOCOL.md",
    "next **5 complete clean boards**",
    "C2 continues its current five-board window",
    "C3 gets a separate 1/5 ... 5/5 counter",
    "Historical boards have zero confirmatory C3 weight",
)
require(
    "models/football/engine/core.py",
    "class C3PolicyAssessment",
    "def c3_ranking_key",
    "def c3_board_state",
    "def c3_shadow_lane",
    "def decide_c3",
    "Two-sidedness has no direct bonus",
)
require(
    "models/football/engine/adapter.py",
    "parse_c3_policy",
    "FOOTBALL_C3_CLEARING_GOAL_FUNDING",
    'model not in {"c", "c2", "c3"}',
    "c3_goal3_funding",
    "c3_control_endpoint_risk",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_c_board_does_not_require_c3_fields",
    "test_c2_board_does_not_require_c3_fields",
    "test_changing_c3_fields_cannot_change_c_ranking",
    "test_c3_board_ignores_two_route_label_without_goal3_funding",
    "test_c3_carrier_led_goal3_can_focus_without_second_route",
)
require(
    "models/football/airtable/FOOTBALL_C3_AIRTABLE.md",
    "C3 role:** shadow-only burden-funding challenger",
    "tblcl1UAyMqZT6Ub0",
    "tblQmUpd5WjBLQ38X",
    "tblUnGHHe0MVaalDL",
    "C3 Test Board Number",
    "C3 COMPARISON INCOMPLETE",
)
forbid(
    "models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md",
    "**Official model:** Football C3",
    "C3 may create Website Picks",
    "C3 may authorize real exposure",
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

# 5. Audit hindsight integrity must be deterministic.
require(
    "models/football/procedures/FOOTBALL_AUDIT_HINDSIGHT_INTEGRITY.md",
    "Three-layer audit record",
    "FROZEN STATE — immutable",
    "OBSERVED OUTCOME — descriptive, not a re-grade",
    "AUDIT DIAGNOSIS — evidence-bounded",
    "MEDIUM-HIGH",
    "RETROSPECTIVE HYPOTHESIS ONLY — DO NOT RE-GRADE HISTORICAL STATE",
    "OFFICIAL C MODEL P&L != ACTUAL USER P&L",
    "FOOTBALL_AUDIT_RECORD",
)
require(
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
    "Audit hindsight integrity — mandatory",
    "FROZEN:",
    "OBSERVED:",
    "DIAGNOSIS:",
    "P&L STATUS:",
    "AUDIT RECORD INVALID — DO NOT FINALIZE DIAGNOSIS",
)
require(
    "models/football/engine/adapter.py",
    "def run_audit_record",
    "AUDIT_DIAGNOSIS_TAGS",
    "official_c_model_pnl must be null when official_c_exposure=false",
    "user_pnl must be null when user_executed=false",
)
require(
    "models/football/engine/cli.py",
    'choices=("board", "decision", "audit")',
    "run_audit_record",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_compound_grade_is_rejected",
    "test_pre_freeze_miss_requires_contemporaneous_note",
    "test_no_official_exposure_cannot_have_model_pnl",
    "test_published_model_exposure_does_not_require_user_bet",
)

# 6. Factor calibration observer must remain non-authoritative.
require(
    "models/football/procedures/FOOTBALL_FACTOR_CALIBRATION_OBSERVER.md",
    "PROSPECTIVE DIAGNOSTIC OBSERVER — ZERO PRODUCTION AUTHORITY",
    "Diagnostic contribution trace",
    "Same-kickoff priority inversion",
    "Ablation replay",
    "OVERWEIGHT CANDIDATE",
    "UNDERWEIGHT CANDIDATE",
    "No silent coefficient tuning inside Football C",
)
require(
    "models/football/airtable/FOOTBALL_FACTOR_CALIBRATION_AIRTABLE.md",
    "tblz2s2KR4BRyAaVo",
    "Outcome fields remain blank before FT",
    "must never be read by",
)
require(
    "models/football/engine/factor_calibration.py",
    "def trace_contributions",
    "def c_ranking_key",
    "def ablated_ranking_key",
    "def factor_bucket_stats",
    "def same_kickoff_ablation",
)
require(
    "models/football/engine/factor_calibration_cli.py",
    "parse_observation",
    "analyze",
)
require(
    "models/football/engine/tests/test_factor_calibration.py",
    "test_trace_score_is_transparent_and_non_market",
    "test_continuation_ablation_can_expose_priority_inversion",
    "test_analyzer_excludes_ineligible_rows_from_buckets",
)
forbid(
    "models/football/engine/core.py",
    "factor_calibration",
)
forbid(
    "models/football/engine/adapter.py",
    "factor_calibration",
)

# 7. Persistence must have named current C/C2/C3 separation.
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "C supported burden",
    "C2 supported burden",
    "C3 Supported Line",
    "C3 Second Route Role",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "C Action",
    "C supported line",
    "C2 supported line",
    "C2 shadow action",
    "C3 Supported Line",
    "C3 Shadow Action",
    "legacy generic",
)

if failures:
    print("FOOTBALL AUTHORITY QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — Football C authority and C2/C3 comparison semantics are internally consistent.")
