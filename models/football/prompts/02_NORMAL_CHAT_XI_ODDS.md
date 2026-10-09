# 02 — Normal Chat: Football C Official + C2 Shadow XI/Odds

> **ACTIVE ROSTER OVERRIDE (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired for new/current execution.

**Command alias:** `/xi`

Read before execution:
- `models/football/procedures/FOOTBALL_HANDOFF_FRESHNESS_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`
- `models/football/CURRENT_MODEL.md`
- `models/football/production/FOOTBALL_C.md`
- `models/football/challengers/football-c2/FOOTBALL_C2_SPEC.md`
- `models/football/procedures/FOOTBALL_TOURNAMENT_INCENTIVE_INTEGRITY.md`
- `models/football/procedures/FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`
- `models/football/procedures/FOOTBALL_BURDEN_COMPLETION_SELECTION.md`
- `models/football/procedures/FOOTBALL_MARKET_HISTORY_RECHECK.md`
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`
- `models/football/procedures/FOOTBALL_STEP2_SESSION_RECONCILIATION.md`
- `models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`
- `models/football/procedures/FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md`

Only Football C may create official exposure. C2 is shadow-only and may never create a Website Pick or real exposure.

## 1. Step-2 authorization

Retrieve the frozen official Football C lane before research:

- `FOLLOW` — routine Step-2 processing is authorized.
- `RESERVE` — process only when explicitly activated or when FOLLOW capacity collapses.
- `STOP` — do not run routine Step 2 unless the user explicitly declares an exception.

For every current session derive and freeze the due set using `models/football/engine/step2_queue_guard.py` under `FOOTBALL_STEP2_SESSION_RECONCILIATION.md`:
- all FOLLOW fixtures whose XI/odds window is open;
- activated RESERVE fixtures (explicitly account for missing XI/odds, too);
- every user-declared exception with explicit authorization.

Routine execution requires a **COMPLETE** packaged Step-0 source and a terminal reconciled C+C2 Step-1 board. `RUNNING` sweeps and provisional screen rows are not routine FOLLOW authority. When that gate fails, run only `EXCEPTION_ONLY` for explicitly user-authorized fixtures if applicable, preserving C+C2 evidence requirements. Keep the full `not_due` manifest as a negative-space audit.

A WATCH/STOP fixture does not reopen merely because market price improves.

## 2. Frozen board retrieval

For each supplied fixture retrieve:
- fixture identity and kickoff;
- frozen operational viability/reliability fields;
- Football C state/rank/lane and independently frozen C supported line;
- Football C completion mode, completion quality, continuation, opponent leakage and stall risk;
- Football C2 state/rank and independently frozen C2 supported line;
- common frozen Step-1 evidence and semantic basis fields.

If C2 was not prospectively frozen, do not manufacture it from C. For a user-declared exception, the assessment is not complete until a lawful C2 input can be frozen from the same current evidence epoch.

If C2 supported burden was not independently frozen where required:

`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`

For an active-roster exception, persist:

`C+C2 EXCEPTION INCOMPLETE — <exact reason>`

rather than presenting a completed C-only verdict.

### Step 0 day-ahead XI expectation versus Step 2 actual XI

The prospective Step-0 gate `FOOTBALL_XI_MARKET_FIRST_INTAKE.md` validates **whether usable starting-XI information is likely to be published near kickoff**, not whether starters were confirmed at the initial all-day sweep. A conditional B/`xi_expected=UNCERTAIN` can therefore have a valid Work research record and remain RESERVE/conditional; do not back-propagate Step-2 confirmation requirements into Step 0. At the scheduled `xi_recheck_due_utc` (typically 75 minutes before kickoff), /xi must acquire reliable current XI and executable odds. If current XI is still unavailable, maintain the existing `DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING` or wait behavior; **no official wager based only on XI expectation**.

## 3. Current evidence epoch

Use the user's confirmed/reliable XI and current executable Asian-total quote as the Step-2 epoch.

Required current evidence includes:
- `xi_status = CONFIRMED / RELIABLE / UNAVAILABLE`;
- current fixture status;
- current quote and `quote_revalidated = true`;
- one fresh fixture-specific post-XI football research pass;
- non-empty `post_xi_research_note`;
- H2H recheck/basis;
- tournament-incentive recheck when applicable;
- market-history attempt;
- model-specific policy rechecks.

Odds/history lookup does **not** satisfy the football-research gate.

If XI is unavailable:
`DECISION BLOCKED — CONFIRMED/RELIABLE XI MISSING`

If the fixture is no longer prematch, do not force a prematch decision. Persist/reroute according to Step-2 reconciliation.

## 4. MANDATORY FRESH POST-XI FOOTBALL WEB RESEARCH

After XI confirmation, run one fresh fixture-specific football research pass before freezing the decision payloads.

Check material current information that can alter:
- route viability;
- carrier self-funding;
- finishing/service continuity;
- opponent leakage;
- continuation after the first goal;
- failure/stall mechanisms;
- tactical/personnel integrity;
- tournament incentive.

Persist:
- `post_xi_research_status = FOUND / LIMITED / UNAVAILABLE_ATTEMPTED`;
- `post_xi_research_note`.

A failed search after a real attempt may be LIMITED/UNAVAILABLE_ATTEMPTED. It must not be silently treated as FOUND.

## 5. MANDATORY MARKET-HISTORY ATTEMPT

Attempt to establish:
`OPEN -> PRE-XI -> POST-XI / CURRENT`

Persist:
- `market_history_status = FOUND / PARTIAL / UNAVAILABLE_ATTEMPTED`;
- market-history movement;
- conflict-recheck status;
- explanatory note.

Report the `MARKET HISTORY status + OPEN / PRE-XI / CURRENT trace`.

Market history is a reinspection trigger, not a model. Price movement never creates a scoring route and cannot override football evidence.

## 6. Tournament-incentive recheck

When `tournament_incentive_required=true`, re-establish before the decision:
- competition format/stage;
- aggregate/table/qualification state;
- draw utility;
- margin/GD/tiebreak relevance;
- simultaneous-result effects.

Required:
- `tournament_incentive_rechecked = true`;
- `tournament_incentive_recheck_status = VERIFIED`.

Otherwise:

`DECISION BLOCKED — TOURNAMENT INCENTIVE RECHECK MISSING`

or

`DECISION BLOCKED — TOURNAMENT INCENTIVE UNRESOLVED`

A user exception does not waive this integrity gate.

## 7. Model-specific current rechecks

Freeze one common factual epoch, then independently apply each active model.

### Football C official

Set `completion_rechecked = true` only after rechecking:
- completion mode;
- current burden-completion quality;
- current continuation quality;
- current opponent leakage;
- current stall risk;
- clearing-goal funding at the supported burden;
- current main failure.

A frozen FOLLOW lane does not force C-BET. If the current mechanism degrades materially, C may WAIT/PASS.

### Football C2 shadow

Set `c2_route_quality_rechecked = true` only after independently rechecking C2's route-quality policy.

Do not reuse C's supported line in C2. C2 owns its supported burden independently.

C2 may return BET/WAIT/PASS for shadow comparison only.

## 8. Atomic deterministic execution

Engine execution is **mandatory** for a completed Step-2 decision.

Before execution, perform `FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md` for stage=`xi` and record the `FOOTBALL_RUNTIME_EXECUTION_RECORD`.

Primary runtime:

1. fetch exact-current `models/football/engine/xi_portable.py`;
2. run `python xi_portable.py self-check`;
3. require `XI PORTABLE RUNTIME: PASS`;
4. freeze `FOOTBALL_ENGINE_C_DECISION_INPUT`;
5. freeze `FOOTBALL_ENGINE_C2_DECISION_INPUT`;
6. run:

`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

Required:

`ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR`

The pair must share the same frozen common evidence epoch. A deterministic payload/contract rejection is not a Python error.

Multi-file fallback is allowed only when the exact-current portable bundle itself fails self-check, using `decision_pair_cli.py` as defined in `FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md`.

The legacy generic no-execution fallback is forbidden.

If execution genuinely fails after a real setup attempt:

`ENGINE EXECUTION STATUS: FAILED_AFTER_ATTEMPT — <exact technical reason>`

If text/code disagree:

`ENGINE DISAGREEMENT — PRESERVE BOTH`

## 9. Price/action policy

Use the model's independently frozen supported burden and the current revalidated quote.

For Football C:
- C-BET only when deterministic/current football requirements clear;
- C-WAIT only when the target is healthy and realistically reachable;
- C-PASS when the mechanism/burden/price path does not clear.

For C2:
- produce the independent shadow action using C2 policy;
- never create official exposure.

WAIT accounting follows `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

## 10. Persistence — fail closed

A completed current assessment must persist together:
- C Action;
- C supported line;
- C result payload;
- C2 Shadow Action;
- C2 supported line;
- C2 result payload;
- Engine Execution Status;
- Engine Source Revision;
- Engine C Result;
- Engine C2 Result;
- Engine Failure Reason when applicable;
- current WAIT/accounting fields.

Do not mark the assessment complete when C2 execution/persistence is missing.

## 11. Active-model accounting

Build one accounting payload containing C and C2 only and run:

`python xi_portable.py accounting --input <model_accounting.json>`

Priority remains:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

A Step-2 PASS does not erase a prospectively frozen WATCH accounting entry.

Historical C3/C4 accounting is audit-only and must use the explicit historical accounting mode; it is never part of a new current Step-2 payload.

## 12. Session reconciliation

At the end of the session, freeze a **v2** `football-step2-reconcile-v2` payload from the due set. Before classifying any match as `DECISION_STATE_PERSISTED`, independently read back its Airtable Decision State record and verify that C/C2 actions, both supported lines, engine revision/status, and both serialized engine results are actually stored. Set `decision_state_snapshot` from that post-write read-back, including the Airtable record ID and original due `match_id`. Do not copy the proposed write payload into the snapshot.

Every other disposition requires an explicit blocker reason; `LIVE_REROUTED` requires a concrete live-handoff reference, and `ENGINE_FAILED_AFTER_ATTEMPT` requires the exact failure reason. Incomplete or provisional records are never `DECISION_STATE_PERSISTED`.

Run:

`python xi_portable.py reconcile --input <step2_reconcile.json>`

Do not call the current session complete unless:

`STEP2 RECONCILIATION STATUS: PASS`

and `verified_decision_count = persisted_decision_count`. A v1 reconciliation pass is historical replay only and cannot authorize current-session completion. Every due fixture must have exactly one traceable disposition. Silent omission is a process failure.

**Then audit against the original frozen queue** with
`python models/football/engine/step2_queue_audit.py --input <step2_queue_audit.json>`
using the saved queue receipt and the same v2 reconciliation input.
A reconciliation PASS proves accounting, not necessarily that every case
is closed. Report `STEP2 ACCOUNTED WITH OPEN FOLLOW_UPS` whenever any
XI/odds wait, status/integrity block, runtime failure, or live reroute
remains unresolved. Only `STEP2 SESSION COMPLETE` with
`all_due_completed=true` is a completed session.

## 13. User-facing output

For each assessed fixture show:
- Match / kickoff
- C frozen state/rank/lane/line
- C2 frozen state/rank/line
- XI status
- fresh football-research status
- market-history status
- current quote
- C official action + reason
- C2 shadow action + reason
- engine pair status
- any WAIT target/min odds
- exact blocker if incomplete

Do not show C3/C4 as current tracks. Historical C3/C4 information belongs only in an explicitly historical audit.
