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
    "ACTIVE ROSTER (2026-10-06)",
    "Football C is official; Football C2 is the only shadow challenger",
    "C3 and C4 are retired",
    "Active official model:** Football **C**",
)
require(
    "models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md",
    "Football C3 and Football C4 are retired",
    "C + C2",
    "C+C2 EXCEPTION INCOMPLETE",
    "python xi_portable.py pair --c <c.json> --c2 <c2.json>",
)
require(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "Official model:** Football C",
    "C Action",
    "C2 shadow action",
)
forbid(
    "models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md",
    "Official model:** Football A",
    "Official:** Football A",
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
    "models/football/prompts/xi.md",
    "On **every invocation**",
    "current repository authority",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "Every invocation must reload the current launcher",
)
require(
    "models/football/prompts/05_NORMAL_CHAT_FOOTBALL_C.md",
    "Status:** RETIRED — DO NOT USE FOR NEW PRODUCTION",
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
    'require_c_completion=(model == "c")',
    "DECISION BLOCKED — C2 ROUTE-QUALITY RECHECK MISSING",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_c2_board_does_not_require_c_completion_diagnostics",
    "test_c_board_still_requires_c_completion_diagnostics",
    "test_c2_decision_does_not_require_c_completion_diagnostics",
)
require(
    "models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md",
    "**C2 owns this field independently.**",
    "frozen route-quality ranking for C2",
)

# 4. Retired challengers must not re-enter active execution.
require(
    "models/football/engine/adapter.py",
    'model not in {"c", "c2"}',
    "C3/C4 are retired",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_retired_c3_board_is_rejected",
    "test_retired_c3_decision_is_rejected",
    "test_c3_cannot_reenter_board_runtime",
    "test_c3_cannot_reenter_decision_runtime",
)
require(
    "models/football/engine/board_pair_cli.py",
    'EXPECTED_MODELS = ("c", "c2")',
    "BOARD PAIR FAILED — COMMON EVIDENCE DRIFT",
    "BOARD PAIR FAILED — RANKED ELIGIBLE UNIVERSE MISMATCH",
    "C POLICY FIELD LEAK INTO C2 PAYLOAD",
    "EXECUTED_C_C2_BOARDS",
    "common_evidence_reconciled",
)
require(
    "models/football/engine/tests/test_board_pair.py",
    "test_pair_reconciles_same_common_evidence",
    "test_common_evidence_drift_fails",
    "test_ranked_universe_mismatch_fails",
    "test_c_policy_field_leak_into_c2_fails",
)
require(
    "models/football/engine/decision_pair_cli.py",
    'EXPECTED_MODELS = ("c", "c2")',
    "EXECUTED_C_C2_PAIR",
    "same frozen common evidence epoch",
)

# 4C. Repaired handoffs must be frozen Step-0 authority for /rank.
require(
    "models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md",
    "ACTIVE STEP-0 INPUT AUTHORITY",
    "REPAIRED HANDOFF LOCAL NORMALIZATION: PASS",
    "final_step0_disposition",
    "women_top_flight_disposition_manifest",
    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING",
    "xi_expected",
    "competition_reliability_reason",
    "REPAIRED HANDOFF AUTHORITY: ACCEPTED",
    "structural compatibility",
    "file-local",
    "must not",
    "search the web to re-verify fixture kickoff",
    "REPAIRED HANDOFF CONFLICT — RETURN TO STEP0 REPAIR",
    "REPAIRED HANDOFF INCOMPLETE — STEP0 REPAIR REQUIRED",
)
require(
    "models/football/engine/repaired_handoff_normalize.py",
    "def normalize_repaired_handoff",
    "final_step0_disposition",
    "women_top_flight_disposition_manifest",
    "women_top_flight_raw_count",
    "OPERATIONAL_CONTRACT_FIELDS",
    "_validate_operational_contract",
    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING",
    "REPAIRED HANDOFF LOCAL NORMALIZATION: PASS",
)
require(
    "models/football/engine/tests/test_repaired_handoff_normalize.py",
    "test_final_disposition_wins_and_counts_are_recomputed",
    "test_women_boolean_is_derived_from_manifest_membership",
    "test_missing_operational_reason_fails_closed",
    "test_deferred_fixture_missing_reliability_reason_fails_closed",
    "test_invalid_observability_fails_closed",
    "test_unresolved_women_still_fails_closed",
)
require(
    "models/football/prompts/rank.md",
    "FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md",
    "Do not re-run fixture discovery, kickoff verification, or Step-0 repair in /rank",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "If the attached file is a completed repaired sweep",
    "do not re-verify kickoff/fixture identity on the web",
    "REPAIRED HANDOFF CONFLICT — RETURN TO STEP0 REPAIR",
    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "structurally complete repaired handoff",
    "Do not use /rank to repair Step 0",
)
require(
    "models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md",
    "step0_fixture_universe_frozen = true",
    "capacity_queue_complete = true",
    "repair_status = COMPLETE",
    "HANDOFF INCOMPLETE — STEP0 OPERATIONAL CONTRACT MISSING",
    "competition_reliability_reason",
)

# 4D. Sweep repair must be bounded and reuse persisted state.
require(
    "models/football/procedures/FOOTBALL_SWEEP_REPAIR_MODE.md",
    "ACTIVE BOUNDED REPAIR CONTROL",
    "/sweep repair",
    "at most **2 independent authoritative verification attempts**",
    "Do not open third/fourth/fifth websites",
    "SWEEP REPAIR COMPLETE — READY FOR /RANK",
    "SWEEP REPAIR COMPLETE WITH UNRESOLVED ITEMS — /RANK BLOCKED",
    "fldjFlyBEoQ2N92t9",
    "fld1EptBTr3b4AfIK",
    "fldgTZ1NpMOk4yilt",
    "fld1PLeqyX9fdWSDi",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "/sweep repair [window]",
    "bounded repair path",
    "Do not silently route `/sweep repair` through the normal fresh-sweep discovery loop",
)
require(
    "models/football/prompts/sweep.md",
    "If the preserved user arguments begin with `repair`",
    "FOOTBALL_SWEEP_REPAIR_MODE.md",
)
require(
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md",
    "repair_mode=true",
    "finite repair set",
    "never keep browsing beyond the repair verification budget",
)
require(
    "models/football/procedures/FOOTBALL_AISCORE_SOURCE_ACQUISITION.md",
    "Repair mode must not restart broad acquisition/discovery",
    "BOUNDED_PRODUCTION_DISCOVERY",
    "MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY",
    "global_raw_exact = false",
    "production_scope_complete = false",
    "at least **two independent current discovery surfaces**",
    "Search snippets are allowed **only as discovery seeds** in this mode.",
    "failure to obtain an exact date carrier is not itself SOURCE_BLOCKED",
    "fewer than two independent current discovery source families",
    "source-recovery lease",
    "source_retry_not_before",
    "30 minutes",
    "FootballFixtures.org",
    "SEARCH_LOCATED_FULL_PAGE",
)

# 4D2. Fresh Step-0 sweep execution must be bounded and resumable.
require(
    "models/football/procedures/FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md",
    "ACTIVE STEP-0 RUNTIME CONTROL",
    "football-sweep-checkpoint-v1",
    "SWEEP CHECKPOINT SAVED — /sweep resume",
    "MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK = 6",
    "Resume Cursor",
    "competition-block shared",
    "without dropping source provenance",
    "Discovery Seed Manifest",
    "Do not keep the only copy of a completed block in the assistant's transient context",
)
require(
    "models/football/prompts/sweep.md",
    "FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md",
    "If the preserved user arguments begin with `resume`",
    "do not create a new Run ID",
)
require(
    "models/football/prompts/COMMAND_ALIASES.md",
    "/sweep resume [window|Run ID]",
    "SWEEP CHECKPOINT SAVED — /sweep resume",
)
require(
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md",
    "Checkpointed execution — mandatory",
    "FAST_FINISH_V1",
    "24 logical competition/date blocks per invocation",
    "six-block quota",
    "terminal_unresolved_verification_blocks",
    "competition-block shared",
    "SWEEP CHECKPOINT SAVED — /sweep resume",
)
require(
    "models/football/engine/sweep_checkpoint.py",
    'CHECKPOINT_VERSION = "football-sweep-checkpoint-v1"',
    "MAX_EXTERNAL_VERIFICATION_BLOCKS_PER_CHUNK = 6",
    "FAST_FINISH_VERIFICATION_BLOCKS_PER_INVOCATION = 24",
    "FAST_FINISH_MAX_BLOCK_ATTEMPTS = 2",
    "FAST_FINISH_POLICY = \"FAST_FINISH_V1\"",
    "terminal_unresolved_verification_blocks",
    "SOURCE_RECOVERY_COOLDOWN_MINUTES = 30",
    "RUN_STATUS_BY_SOURCE_STATE",
    "def run_status_for_source_state",
    "def source_retry_decision",
    "def mark_source_blocked",
    "SOURCE_RECOVERY_LEASE_EXPIRED",
    "LEGACY_BLOCKED_CHECKPOINT_NO_RETRY_LEASE",
    "def select_verification_chunk",
    "def advance_after_chunk",
)
require(
    "models/football/engine/tests/test_sweep_checkpoint.py",
    "test_selects_at_most_six_blocks",
    "test_retry_blocks_are_prioritized_on_resume",
    "test_advance_to_reconciliation_when_queue_empty",
    "test_unchanged_blocker_does_not_retry_inside_lease",
    "test_unchanged_blocker_retries_after_lease_expiry",
    "test_changed_fingerprint_retries_immediately",
    "test_legacy_blocked_checkpoint_without_lease_retries_once",
    "test_mark_source_blocked_creates_retry_lease",
    "test_source_state_maps_to_airtable_run_status",
    "test_source_blocked_is_not_a_run_status_value",
)
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "fldtIbv2ppGzwUExs",
    "flduqxh9DOKdV1A06",
    "flduhyM3Thjwj3Bqs",
    "fld8jr7wAWGLhXqXe",
    "fld4h6ZPqTCLBgxQ8",
    "fldBq52mI5JtCz9xf",
    "fld6ZtvrmNrFmff4h",
    "Never write `SOURCE_BLOCKED` into `Run Status`",
)

# 4D3. Step-1 must consume both exact and bounded Step-0 source scopes.
require(
    "models/football/engine/step0_handoff_cli.py",
    "BOUNDED_PRODUCTION_DISCOVERY",
    "MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY",
    "coverage_mode=FALLBACK_PRODUCTION_SCOPE",
    "global_raw_exact=false",
    "production_scope_complete=true",
    "discovery_seed_manifest",
    "two independent source families",
    "production_universe_count",
    'choices=("export", "rank")',
    "LEGACY_MISSING_DISCOVERY_SEED_MANIFEST",
    "LEGACY_MISSING_BLOCK_EXCLUDED_SUMMARY",
    "direct [...] array",
    "source_family",
)
require(
    "models/football/engine/tests/test_step0_handoff_cli.py",
    "test_bounded_production_handoff_passes",
    "test_bounded_requires_fallback_coverage_mode",
    "test_bounded_requires_production_scope_complete",
    "test_bounded_requires_two_independent_source_families",
    "test_bounded_requires_production_universe_count",
    "test_rank_accepts_transitional_bounded_handoff_without_manifest",
    "test_export_rejects_bounded_handoff_without_manifest",
    "test_rank_accepts_transitional_bounded_handoff_without_block_summary",
    "test_bounded_array_manifest_passes_export_and_rank",
    "test_bounded_array_manifest_accepts_source_family_alias",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "Step-0 source-scope compatibility",
    "source_scope = BOUNDED_PRODUCTION_DISCOVERY",
    "--consumer rank",
    "LEGACY_MISSING_DISCOVERY_SEED_MANIFEST",
    "audit-provenance warnings, not ranking blockers",
    "do not restart source acquisition or demand an exact global raw fixture count in /rank",
    "production_scope_complete=true",
    "global_raw_exact=false",
    "wrapper object vs direct source array",
)
require(
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md",
    "source_scope = EXACT_DATE_UNIVERSE / BOUNDED_PRODUCTION_DISCOVERY",
    "discovery_seed_manifest",
    "--consumer export",
    "source_transport=MULTISOURCE_BOUNDED_PRODUCTION_DISCOVERY",
    "direct `[...]` source-entry array",
)
require(
    "models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md",
    "Step-0 source scope / source transport / coverage mode",
    "restart source acquisition merely because `global_raw_exact=false`",
)

# 4E. Step-0 capacity is an initial batch, with deterministic Step-1 replenishment.
require(
    "models/football/procedures/FOOTBALL_CAPACITY_REPLENISHMENT.md",
    "ACTIVE OPERATIONAL CAPACITY CONTROL",
    "15 limit controls **concurrent deep-research workload**",
    "Step0 Capacity Queue Rank",
    "FOLLOW <= 6",
    "RESERVE <= 4",
    "FOLLOW + RESERVE = 10",
    "capacity_replenishment_cli.py",
    "The next candidate is always the lowest remaining Step0 queue rank",
)
require(
    "models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md",
    "complete fixture-level A/B capacity queue first",
    "initial Work batch cap",
    "Step0 Capacity Queue Rank",
    "Kickoff discovery order, source-page order and block arrival order must never decide admission",
    "retained as the Step-1 replenishment queue",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "Deterministic replenishment — mandatory",
    "active_lane_count = FOLLOW + RESERVE",
    "capacity_replenishment_cli.py",
    "Step1 Replenished = true",
    "Replenishment Wave = 1, 2, ...",
    "A STOP/PASS does not permanently consume one of the original 15 research slots",
)
require(
    "models/football/engine/capacity_replenishment.py",
    "MAX_FOLLOW = 6",
    "MAX_RESERVE = 4",
    "def next_replenishment_wave",
    "duplicate Step0 Capacity Queue Rank",
    "REPLENISHMENT_REQUIRED",
)
require(
    "models/football/engine/tests/test_capacity_replenishment.py",
    "test_selects_lowest_queue_ranks_for_vacancies",
    "test_full_active_capacity_selects_none",
    "test_started_candidate_is_skipped_without_jumping_order_bug",
    "test_duplicate_queue_rank_fails",
)
require(
    "models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md",
    "fldUFbfIyiIYcQuVt",
    "fldPUL87XJhpUqYiU",
    "fld5qzOVZdKst3bhK",
    "fldUxHPEnQpGSJVmC",
)

# 4E2. Rank terminal status must distinguish completion from integrity failure.
require(
    "models/football/procedures/FOOTBALL_RANK_TERMINAL_STATUS.md",
    "ACTIVE STEP-1 TERMINAL-STATE CONTROL",
    "RANK COMPLETE — NO RANKED ELIGIBLE FIXTURES",
    "RANK COMPLETE — 0 FOLLOW",
)
require(
    "models/football/engine/rank_terminal_status.py",
    "def rank_terminal_status",
    "COMPLETE_EMPTY_RANKED_UNIVERSE",
    "COMPLETE_ZERO_FOLLOW",
    "REPLENISHMENT_REQUIRED",
    "BLOCKED_INTEGRITY",
)
require(
    "models/football/engine/tests/test_rank_terminal_status.py",
    "test_empty_ranked_universe_with_hold_is_complete_not_blocked",
    "test_zero_follow_ranked_board_is_complete",
    "test_hold_with_deferred_queue_requires_replenishment",
)

# 4F. Required competition coverage must fail closed before Work.
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

# 5. New-chat handoff freshness must preserve current C+C2 authority.
require(
    "models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md",
    "MANDATORY ROUTER PRECHECK",
    "historical state snapshot",
    "HANDOFF AUTHORITY STALE — CURRENT MODEL/LAUNCHER RELOADED",
    "OFFICIAL C",
    "SHADOW C2",
    "C3 and C4 are retired",
    "\"all models\" means the active roster: C + C2",
)
require(
    "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "ACTIVE ROSTER OVERRIDE",
    "python xi_portable.py pair --c <c.json> --c2 <c2.json>",
)
require(
    "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
    "ACTIVE ROSTER (2026-10-06)",
    "No live-stat gate",
    "Assess the live match **regardless of provider live stats**",
    "positive live-stat confirmation is not required",
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

# 4G. Execution-required stages must probe current runtime/repository state.
require(
    "models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md",
    "MANDATORY EXECUTION PRECHECK",
    "PYTHON PROBE: PASS",
    "REPOSITORY PROBE: PASS",
    "CONTAINER NETWORK UNAVAILABLE — NOT REPOSITORY UNAVAILABLE",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
    "XI PORTABLE RUNTIME: PASS",
    "xi_portable.py self-check",
    "runtime_probe.py --stage <rank|xi|audit>",
)
require(
    "models/football/engine/runtime_probe.py",
    "STAGE_FILES",
    "def probe_stage",
    "RUNTIME SOURCE PROBE: PASS",
)
require(
    "models/football/prompts/01_WORK_DAILY_SWEEP.md",
    "FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
)
require(
    "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
    "FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md",
    "FOOTBALL_RUNTIME_EXECUTION_RECORD",
)

# 5. Completed Step-2 decisions must execute the active pair atomically.
require(
    "models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md",
    "MANDATORY STEP-2 EXECUTION PRECHECK",
    "Active models:** Football C official + Football C2 shadow",
    "xi_portable.py self-check",
    "xi_portable.py pair --c <c.json> --c2 <c2.json>",
    "decision_pair_cli.py",
    "ENGINE EXECUTION FAILED — ATTEMPTED — <exact technical reason>",
    "ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR",
)
require(
    "models/football/engine/xi_portable.py",
    "def run_pair_files",
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
    "models/football/engine/tests/test_adapter.py",
    "test_pair_executes_both_active_models",
    "test_pair_rejects_model_mismatch",
    "test_pair_rejects_non_decision_stage",
    "test_pair_rejects_mixed_common_evidence_epoch",
)
require(
    "models/football/procedures/FOOTBALL_STEP2_SESSION_RECONCILIATION.md",
    "mandatory Step-2 completeness guard",
    "every `FOLLOW` fixture whose XI/odds decision window is open",
    "STEP2 RECONCILIATION FAILED — SILENT OMISSION",
    "quote_revalidated = true",
    "c2_route_quality_rechecked = true",
)

# 5. Step-2 deterministic validation must fail closed.
require(
    "models/football/engine/schema.json",
    "\"official_follow_lane\"",
    "\"step2_authorization\"",
    "\"xi_status\"",
    "\"post_xi_research_status\"",
    "\"fixture_status\"",
    "\"quote_revalidated\"",
    "\"h2h_rechecked\"",
    "\"completion_rechecked\"",
    "\"c2_route_quality_rechecked\"",
    "\"primary_mechanism_intact\"",
)
require(
    "models/football/engine/adapter.py",
    "def _required_bool",
    "DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING",
    "DECISION BLOCKED — H2H RECHECK MISSING",
    "DECISION BLOCKED — BURDEN-COMPLETION RECHECK MISSING",
    "DECISION BLOCKED — C2 ROUTE-QUALITY RECHECK MISSING",
    "DECISION BLOCKED — STEP2 FIXTURE NOT CONFIRMED PREMATCH",
    "DECISION BLOCKED — CURRENT QUOTE NOT REVALIDATED",
)
require(
    "models/football/engine/tests/test_adapter.py",
    "test_missing_step2_lane_fails_closed",
    "test_stop_lane_without_exception_is_blocked",
    "test_stop_lane_user_exception_can_reopen",
    "test_missing_xi_status_fails_closed",
    "test_missing_post_xi_research_status_fails_closed",
    "test_non_prematch_fixture_blocks_step2",
    "test_quote_must_be_revalidated_before_decision",
    "test_c2_requires_own_route_quality_recheck",
)

# 5. Active accounting is C+C2; historical retired-model settlement is explicit.
require(
    "models/football/engine/model_bet_accounting.py",
    'ACTIVE_MODELS = ("c", "c2")',
    'HISTORICAL_MODELS = ("c", "c2", "c3", "c4")',
    "historical_roster",
    "active accounting permits C/C2 only",
    "ACTIVE_C_C2",
    "HISTORICAL_C_C2_C3_C4",
)
require(
    "models/football/engine/tests/test_model_bet_accounting.py",
    "test_active_fixture_output_requires_c_and_c2_only",
    "test_active_fixture_output_rejects_retired_rows",
    "test_historical_roster_can_still_be_settled_explicitly",
)
require(
    "models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md",
    "New model accounting includes C and C2 only",
    "Historical C3/C4 accounting is retained as historical data",
)

# 6. Audit hindsight integrity must be deterministic.
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
    "WAIT_ASSUMED exposure line/odds must equal frozen WAIT target/minimum",
    "WAIT_USER_CONFIRMED requires user_executed=true",
    "WAIT_NOT_REACHED requires official_c_exposure=false",
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
    "test_wait_assumed_counts_as_official_model_exposure",
    "test_wait_not_reached_requires_user_declared_no_exposure",
)

# 7. Factor calibration observer must remain non-authoritative.
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

# 8. Persistence must keep active C/C2 fields distinct.
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
)
require(
    "models/football/procedures/FOOTBALL_SEMANTIC_DECISION_BASIS.md",
    "ACTIVE PROCESS COMPLIANCE CONTROL",
    "H2H never creates a scoring route",
    "carrier_self_fund_basis",
    "primary_mechanism_basis",
)

if failures:
    print("FOOTBALL AUTHORITY QA FAIL")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS — Football C official + C2 shadow production authority is internally consistent.")
