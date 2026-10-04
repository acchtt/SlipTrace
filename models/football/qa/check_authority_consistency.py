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
    'require_c_completion=(model == "c")',
)
require(
    "models/football/engine/core.py",
    "FOOTBALL C COMPLETION DIAGNOSTICS MISSING",
    "def require_c_completion",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_c2_board_does_not_require_c_completion_diagnostics",
    "test_c3_board_does_not_require_c_completion_diagnostics",
    "test_c_board_still_requires_c_completion_diagnostics",
    "test_c2_decision_does_not_require_c_completion_diagnostics",
    "test_c3_decision_does_not_require_c_completion_diagnostics",
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
    "next **5 complete clean ranked boards**",
    "C2 continues its current five-board window",
    "C3 gets a separate 1/5 ... 5/5 counter",
    "ranked eligible universe",
    "one isolated HOLD does not hold back an otherwise complete board",
    "missing Netherlands Eerste Divisie block",
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
    "ranked-universe",
    "prospectively quarantined HOLD/exclusion",
    "C3 COMPARISON INCOMPLETE",
)
forbid(
    "models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md",
    "**Official model:** Football C3",
    "C3 may create Website Picks",
    "C3 may authorize real exposure",
)

# 4A. Step-1 board comparison must reconcile the common evidence epoch.
require(
    "models/football/procedures/FOOTBALL_STEP1_BOARD_RECONCILIATION.md",
    "ACTIVE PROCESS COMPLIANCE CONTROL",
    "COMMON EVIDENCE RECONCILED",
    "BOARD TRIPLET FAILED — COMMON EVIDENCE DRIFT",
    "BOARD TRIPLET FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH",
    "supported_line_basis",
    "board_state_basis",
)
require(
    "models/football/engine/board_triplet_cli.py",
    "EXPECTED_MODELS = (\"c\", \"c2\", \"c3\")",
    "MODEL_OWNED_FIELDS",
    "COMMON EVIDENCE DRIFT",
    "RANKED ELIGIBLE UNIVERSE MISMATCH",
    "C POLICY FIELD LEAK INTO SHADOW PAYLOAD",
    "C3 POLICY FIELD LEAK INTO C/C2 PAYLOAD",
    "EXECUTED_ALL_THREE_BOARDS",
    "common_evidence_reconciled",
)
require(
    "models/football/engine/tests/test_board_triplet.py",
    "test_triplet_reconciles_same_common_evidence",
    "test_common_evidence_drift_fails",
    "test_ranked_universe_mismatch_fails",
    "test_c_policy_field_leak_into_c2_fails",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "board_triplet_cli.py",
    "common_evidence_basis",
    "supported_line_basis",
    "board_state_basis",
    "common_evidence_reconciled = true",
)
require(
    "models/football/engine/schema.json",
    "\"common_evidence_basis\"",
    "\"supported_line_basis\"",
    "\"board_state_basis\"",
    "\"c3_second_route_role_basis\"",
    "\"c3_forced_chaos_basis\"",
)
require(
    "models/football/engine/adapter.py",
    "common_evidence_basis=_string",
    "supported_line_basis=_string",
    "board_state_basis = _string",
    "c3_second_route_role_basis",
    "c3_forced_chaos_basis",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_board_requires_common_evidence_basis",
    "test_board_requires_supported_line_basis",
    "test_c_and_c2_require_board_state_basis",
)
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "Common Evidence Basis",
    "Supported Line Basis",
    "C Board State Basis",
    "Board Triplet Common-Evidence Reconciliation Status",
)

# 4B. Required competition coverage must fail closed before Work.
require(
    "models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md",
    "MANDATORY STEP-0 COVERAGE INVARIANT",
    "required-competition-manifest-v1",
    "NED_EERSTE_DIVISIE",
    "CHECKED_WITH_FIXTURES",
    "CHECKED_NO_IN_WINDOW_FIXTURES",
    "SOURCE_BLOCKED",
    "HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP",
)
require(
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md",
    "Required competition-block manifest — mandatory",
    "NED_EERSTE_DIVISIE",
    "Required Competition Blocks Complete = true",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "Required competition coverage preflight — fail closed",
    "HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP",
    "HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP",
)
require(
    "models/football/engine/coverage_manifest.py",
    'REQUIRED_BLOCKS = ("NED_EERSTE_DIVISIE",)',
    "SOURCE_BLOCKED",
    "required_blocks_complete",
)
require(
    "models/football/engine/tests/test_coverage_manifest.py",
    "test_missing_eerste_block_fails_closed",
    "test_source_blocked_fails_closed",
    "test_count_mismatch_fails_closed",
)
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "Required Competition Manifest Version",
    "Required Competition Blocks Complete",
)

# 5. New-chat handoff freshness must preserve current three-track authority.
require(
    "models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md",
    "MANDATORY ROUTER PRECHECK",
    "historical state snapshot",
    "HANDOFF AUTHORITY STALE — CURRENT MODEL/LAUNCHER RELOADED",
    "OFFICIAL C",
    "SHADOW C2",
    "SHADOW C3",
    "may never be silently absent",
)
require(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "Mandatory three-track visibility",
    "SHADOW C2: UNAVAILABLE — NO PROSPECTIVE C2 FREEZE",
    "SHADOW C3: UNAVAILABLE — BOARD PREDATES C3 / NO PROSPECTIVE C3 FREEZE",
)
require(
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
    "Mandatory three-track visibility",
    "Never omit a shadow row",
    "No live-stat gate",
    "Assess the live match **regardless of provider live stats**",
    "positive live-stat confirmation is not required",
    "Do not ask the user for live-stat screenshots before assessing",
)
forbid(
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
    "Require contemporaneous attacking-quality evidence",
    "require at least one live attacking-quality indicator",
)
require(
    "models/football/production/FOOTBALL_C.md",
    "Do **not** require positive live-stat confirmation",
    "Live assessment proceeds regardless of provider live stats",
)
require(
    "models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md",
    "Do not require a live attacking-quality indicator",
)
require(
    "models/football/challengers/football-c3/FOOTBALL_C3_SPEC.md",
    "C3 live resolution does not require shots, xG, big chances",
)

# 5. Step-2 market history must be attempted and explicit.
require(
    "models/football/procedures/FOOTBALL_MARKET_HISTORY_RECHECK.md",
    "MANDATORY STEP-2 EVIDENCE BLOCK",
    "OPEN -> PRE-XI -> POST-XI / CURRENT PREMATCH",
    "MARKET HISTORY FOUND",
    "MARKET HISTORY PARTIAL",
    "MARKET HISTORY UNAVAILABLE — ATTEMPTED",
    "Market history is a reinspection trigger, not a model",
)
require(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "MANDATORY MARKET-HISTORY ATTEMPT",
    "market_history_status = FOUND / PARTIAL / UNAVAILABLE_ATTEMPTED",
    "MARKET HISTORY status + OPEN / PRE-XI / CURRENT trace",
)
require(
    "models/football/engine/adapter.py",
    "market_history_status",
    "market_history_movement",
    "market_history_conflict_recheck",
    "market_history_note",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_missing_market_history_status_fails_closed",
    "test_unavailable_market_history_can_continue_after_attempt",
)

# 5. Completed Step-2 decisions must attempt deterministic execution.
require(
    "models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md",
    "MANDATORY STEP-2 EXECUTION PRECHECK",
    "Lack of an already-existing local repository checkout is **not** engine unavailability",
    "decision_triplet_cli.py",
    "ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>",
    "ENGINE EXECUTION STATUS: EXECUTED_ALL_THREE",
)
require(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "Engine execution is **mandatory** for a completed Step-2 decision",
    "decision_triplet_cli.py",
    "A missing local checkout is **not** engine unavailability",
    "ENGINE EXECUTION STATUS: EXECUTED_ALL_THREE",
    "ENGINE EXECUTION STATUS: FAILED_AFTER_ATTEMPT — <exact technical reason>",
    "generic fallback `ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED` is forbidden",
)
forbid(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "If execution is unavailable:",
)
require(
    "models/football/engine/decision_triplet_cli.py",
    "EXPECTED_MODELS = (\"c\", \"c2\", \"c3\")",
    "EXECUTED_ALL_THREE",
    "triplet payload mismatch",
    "official_follow_lane",
    "step2_authorization",
    "must share the same official_follow_lane and step2_authorization",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_triplet_executes_all_three_models",
    "test_triplet_rejects_model_mismatch",
    "test_triplet_rejects_non_decision_stage",
)
require(
    "models/football/procedures/FOOTBALL_STEP2_SESSION_RECONCILIATION.md",
    "mandatory Step-2 completeness guard",
    "every `FOLLOW` fixture whose XI/odds decision window is open",
    "STEP2 RECONCILIATION FAILED — SILENT OMISSION",
    "quote_revalidated = true",
    "c2_route_quality_rechecked = true",
    "c3_funding_rechecked = true",
)
require(
    "models/football/engine/step2_reconcile.py",
    "def reconcile_step2",
    "SILENT OMISSION",
    "OUTCOME WITHOUT AUTHORIZATION",
    "LIVE_REROUTED",
)
require(
    "models/football/engine/tests/test_step2_reconcile.py",
    "test_missing_follow_is_a_hard_failure",
    "test_outcome_without_authorization_is_a_hard_failure",
    "test_routine_follow_requires_follow_lane",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "Engine Execution Status",
    "Engine Source Revision",
    "Engine C Result",
    "Engine C2 Result",
    "Engine C3 Result",
    "Engine Failure Reason",
)

# 5. Step-2 deterministic validation must fail closed.
require(
    "models/football/engine/schema.json",
    "\"official_follow_lane\"",
    "\"step2_authorization\"",
    "\"thesis_state_basis\"",
    "\"main_failure\"",
    "\"h2h_state\"",
    "\"h2h_effect\"",
    "\"h2h_transferability\"",
    "\"h2h_current_corroboration\"",
    "\"h2h_material_effect\"",
    "\"h2h_basis\"",
    "\"carrier_self_fund\"",
    "\"carrier_self_fund_basis\"",
    "\"independent_upper_tail_basis\"",
    "\"failure_attacks_route\"",
    "\"failure_attacks_route_basis\"",
    "\"material_suppression\"",
    "\"material_suppression_basis\"",
    "\"xi_status\"",
    "\"post_xi_research_status\"",
    "\"post_xi_research_note\"",
    "\"fixture_status\"",
    "\"quote_revalidated\"",
    "\"h2h_review_status\"",
    "\"h2h_rechecked\"",
    "\"h2h_basis\"",
    "\"primary_mechanism_basis\"",
    "\"wait_reachability_basis\"",
    "\"wait_negative_info_basis\"",
    "\"material_veto_basis\"",
    "\"completion_rechecked\"",
    "\"c2_route_quality_rechecked\"",
    "\"c3_funding_rechecked\"",
    "\"primary_mechanism_intact\"",
)
require(
    "models/football/engine/adapter.py",
    "def _required_bool",
    "official_follow_lane",
    "step2_authorization",
    "DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING",
    "DECISION BLOCKED — H2H RECHECK MISSING",
    "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING",
    "DECISION BLOCKED — C2 ROUTE-QUALITY RECHECK MISSING",
    "DECISION BLOCKED — C3 FUNDING RECHECK MISSING",
    "DECISION BLOCKED — STEP2 FIXTURE NOT CONFIRMED PREMATCH",
    "DECISION BLOCKED — CURRENT QUOTE NOT REVALIDATED",
    "post_xi_research_note",
    "validate_h2h_semantics",
    "H2H MATERIAL EFFECT BLOCKED",
    "h2h_effect",
    "h2h_transferability",
    "h2h_current_corroboration",
    "h2h_material_effect",
    "h2h_basis",
    "thesis_state_basis",
    "thesis_state_basis",
    "primary_mechanism_basis",
    "wait_reachability_basis",
    "wait_negative_info_basis",
    "material_veto_basis",
    "failure_attacks_route_basis",
    "material_suppression_basis",
    "primary_mechanism_intact=_required_bool",
    "_required_bool(obj, \"material_suppression\")",
)
require(
    "models/football/engine/core.py",
    "class Step2Authorization",
    "DECISION BLOCKED — STEP2 AUTHORIZATION/LANE MISMATCH",
    "current burden stall risk is HIGH",
    "current burden-completion quality is LOW",
    "current continuation quality is LOW",
    "primary scoring mechanism not intact",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_missing_step2_lane_fails_closed",
    "test_stop_lane_without_exception_is_blocked",
    "test_stop_lane_user_exception_can_reopen",
    "test_missing_xi_status_fails_closed",
    "test_missing_post_xi_research_status_fails_closed",
    "test_post_xi_research_note_is_required",
    "test_material_h2h_effect_requires_verified_transferability_and_corroboration",
    "test_material_h2h_effect_requires_current_corroboration",
    "test_missing_h2h_basis_fails_closed",
    "test_missing_thesis_state_basis_fails_closed",
    "test_missing_primary_mechanism_basis_fails_closed",
    "test_missing_wait_basis_fails_closed",
    "test_missing_material_veto_basis_fails_closed",
    "test_missing_assessment_boolean_basis_fails_closed",
    "test_non_prematch_fixture_blocks_step2",
    "test_quote_must_be_revalidated_before_decision",
    "test_c2_requires_own_route_quality_recheck",
    "test_c3_requires_own_funding_recheck",
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
    "models/football/procedures/FOOTBALL_SEMANTIC_DECISION_BASIS.md",
    "ACTIVE PROCESS COMPLIANCE CONTROL",
    "\"Recent\" is priority, not a hidden numeric threshold",
    "H2H never creates a scoring route",
    "carrier_self_fund_basis",
    "primary_mechanism_basis",
    "MODEL CHALLENGER REQUIRED",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "h2h_basis",
    "primary_mechanism_basis",
    "wait_reachability_basis",
    "material_veto_basis",
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
