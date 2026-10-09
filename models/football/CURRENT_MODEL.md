# Current Football Model

> **ACTIVE ROSTER (2026-10-06):** Football C is official; Football C2 is the only shadow challenger. C3 and C4 are retired from new/current execution. Historical C3/C4 records remain immutable audit history.

**Active official model:** Football **C**  
**Only active shadow challenger:** Football **C2**  
**Fixture authority:** AiScore primary, with the documented bounded source fallback  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for current football work.

## Command router

Read `models/football/prompts/COMMAND_ALIASES.md`.

- `/sweep` -> `00_NORMAL_CHAT_AISCORE_FETCH.md`
- `/rank` -> `01_WORK_DAILY_SWEEP.md`
- `/xi` -> `02_NORMAL_CHAT_XI_ODDS.md`
- `/live` -> `03_NORMAL_CHAT_LIVE.md`
- `/audit` -> `04_WORK_POST_SLATE_AUDIT.md`
- `/report` -> `06_NORMAL_CHAT_REPORT.md`

Everything after the alias is launcher input. Same-message attachments are launcher inputs.

A handoff is historical context, not current authority. Reload this file and the current launcher before continuing old work.

## Model authority

- Football C is the only model that may create an official Website Pick or official model exposure.
- Football C2 is shadow-only. It may be ranked, executed, persisted and audited, but may never authorize official exposure.
- C3 and C4 are retired for new work. Do not execute them, require them, display them as current tracks, populate new current fields for them, or count them in current forward metrics.
- Historical C3/C4 records remain valid only for the exact epochs in which they were prospectively frozen.
- Python deterministic code validates structured C/C2 inputs and accounting. It is not production decision authority.

The active pair contract is:

`models/football/procedures/FOOTBALL_C_C2_ACTIVE_PAIR.md`

## Active production sequence

`SENIOR DISCOVERY -> SOURCE/IDENTITY INTEGRITY -> OPERATIONAL VIABILITY -> RESEARCHABILITY/CAPACITY -> COMMON STEP-1 EVIDENCE FREEZE -> [C BOARD + C2 SHADOW BOARD] -> C FOLLOW/RESERVE/STOP -> COMMON STEP-2 XI/RESEARCH/MARKET EPOCH -> [C OFFICIAL ACTION + C2 SHADOW ACTION] -> LIVE/WAIT -> AUDIT`

C and C2 share facts, not policy.

## Shared evidence / policy separation

For each fixture and epoch, freeze one factual evidence state before model policy is applied.

Common evidence includes:
- fixture identity/status/kickoff;
- operational viability/reliability state;
- route/carrier evidence;
- chance quality;
- failure/suppression evidence;
- H2H materiality and basis;
- continuation/leakage evidence;
- tournament format/incentive state when applicable;
- current XI/mechanism state;
- current executable quote at Step 2.

Football C owns:
- completion mode;
- burden-completion quality;
- continuation quality;
- opponent leakage;
- burden stall risk;
- C supported line;
- C official board state/rank;
- official FOLLOW/RESERVE/STOP lane;
- C Step-2 action.

Football C2 owns independently:
- C2 supported line;
- C2 route-quality ranking/selection-floor state;
- C2 shadow board state/rank;
- C2 Step-2 shadow action.

Never copy C's supported burden into C2. Never infer missing C2 from C.

## Step 0 — researchable senior intake

Use `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`.

Also apply:
- `FOOTBALL_AISCORE_SOURCE_ACQUISITION.md`;
- `FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`;
- `FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`;
- `FOOTBALL_WOMENS_TOP_FLIGHT_COVERAGE.md`;
- `FOOTBALL_COMPETITION_RELIABILITY_MEMORY.md`;
- `FOOTBALL_OPERATIONAL_VIABILITY_GATE.md`.

Default scope:

`RESEARCHABLE_SENIOR_PRODUCTION`

Step 0 must:
- acquire a valid source scope under the source contract: prefer `EXACT_DATE_UNIVERSE`, otherwise use `BOUNDED_PRODUCTION_DISCOVERY` in FAST_PRODUCTION;
- complete a valid senior production universe under final reconciliation;
- preserve required/protected competition coverage;
- preserve senior women's top-flight accounting;
- apply hard scope exclusions;
- assign current operational viability A/B/C/D;
- apply competition reliability caps/demotion;
- perform cheap researchability screening;
- build the complete deterministic A/B capacity queue;
- admit only the first 15 A/B rows to the initial Work wave;
- preserve overflow A/B rows with immutable Step0 Capacity Queue Rank;
- package a valid `football-step0-handoff-v2` handoff.

A/B queue rank is operational only. It must not be based on expected goals, model attractiveness or result knowledge.

### Compact sweep Work research budget — new runs from 2026-10-09 ICT

For new /sweep runs, apply `models/football/procedures/FOOTBALL_COMPACT_SWEEP_WORK_BUDGET.md` as an explicit **prospective operational budget overlay**: `sweep_work_budget_policy=COMPACT_GOAL_ROUTE_V1`, initial Work wave 8 by the full frozen operational A/B rank, routine unique-fixture research ceiling 12, automatic replenish only below 4 active lanes. Source discovery, A/B rank ordering, protected/women/required coverage, hard exclusions and C/C2 decision logic are unchanged. Goal-rate research is context-only, **not** a Step-0 predictive hard filter or automatic league exclusion. Existing RUNNING/frozen/historical sweeps without this policy, including `SWEEP-20261009-1300-20261010-0300` Chunk 12, must retain their legacy 15/refill-to-10 semantics and must not be restarted or rewritten. Keep all A/B overflow as an auditable queue.

### XI + market proof before the Work queue

For new compact intake and explicitly marked resumed unfinished sweeps, apply `FOOTBALL_XI_MARKET_FIRST_INTAKE.md`: **expectation of XI publication**, not confirmed future starting XIs. Verify credible publishing channels and a near-KO recheck; A/YES needs strong evidence for both teams, B/UNCERTAIN may enter conditionally with sources and no routine FOLLOW until /xi validates. Require a current fixture-specific Asian total, news, competition source and identity/time. The raw discovery ledger is not the actionable board. Preserve exact required/protected/women's coverage; exclude/hold actual weak-data cases from Work only. The paused Oct-09 run remains untouched and retains legacy budget on future resume with `XI_MARKET_FIRST_V1` marker.

## Step 1 — Football C official board + Football C2 shadow board

Use `models/football/prompts/01_WORK_DAILY_SWEEP.md`.

For repaired handoffs, first apply:

`models/football/procedures/FOOTBALL_REPAIRED_HANDOFF_AUTHORITY.md`

Step 1 accepts both exact-date and bounded-production Step-0 handoffs after machine validation. A bounded handoff keeps `global_raw_exact=false` and must not trigger raw-universe rediscovery inside /rank.

Do not use /rank to rediscover or repair Step-0 identity/kickoff fields.

Freeze one common Step-1 football evidence epoch, then create:
- Football C official board;
- Football C2 shadow board.

Every ranked fixture requires:
- `common_evidence_basis`;
- C supported line + basis;
- C board state + basis;
- C2 supported line + basis;
- C2 board state + basis.

Run deterministic pair reconciliation:

`python models/football/engine/board_pair_cli.py --c <c.json> --c2 <c2.json>`

Required:
- `EXECUTED_C_C2_BOARDS`;
- `common_evidence_reconciled = true`.

Fail closed on ranked-universe mismatch, common-evidence drift, or C policy leakage into C2.

## Football C selection / clearing-goal funding

FOCUS classification is intentionally broader than FOLLOW certification.

For O2.5/O2.75 and other burdens requiring a third goal, FOLLOW must explicitly fund the clearing goal. A strong carrier plus a merely usable second route is not automatically enough.

Ranking should prioritize:
1. clearing-goal funding;
2. continuation after the first goal;
3. stall/control risk;
4. route/carrier reliability;
5. failure resistance;
6. evidence confidence;
7. burden protection.

Operational capacity does not change predictive rank.

The official lane remains:
- `FOLLOW` — routine Step 2;
- `RESERVE` — conditional;
- `STOP` — no routine Step 2 without explicit exception.

Same-kickoff guard and capacity limits remain:
- maximum routine FOLLOW = 6;
- maximum retained RESERVE = 4;
- maximum two routine FOLLOW fixtures at one exact kickoff minute.

## Step-1 capacity replenishment

The initial 15-fixture Step-0 cap is not a final board-size cap.

If `FOLLOW + RESERVE < 10` after a completed wave and prematch A/B rows remain:
- pull the next deferred rows strictly by ascending Step0 Capacity Queue Rank;
- assess them as the next replenishment wave;
- keep the original queue rank immutable.

Continue until:
1. FOLLOW + RESERVE reaches 10;
2. no prematch A/B deferred row remains; or
3. all remaining deferred rows have left the prematch window.

A STOP/PASS/started row does not permanently consume one of the initial 15 research slots.

## Mandatory deterministic runtime bootstrap

For execution-required `/rank`, `/xi`, and `/audit`, apply:

`models/football/procedures/FOOTBALL_RUNTIME_EXECUTION_BOOTSTRAP.md`

Tool/repository availability is a current-turn observed state.

Required record:

`FOOTBALL_RUNTIME_EXECUTION_RECORD`

The workflow must:
- probe Python;
- probe the current repository authority;
- materialize exact-current source when needed;
- run the stage runtime probe or XI portable self-check;
- attempt the actual deterministic command;
- preserve exact failure evidence.

A missing local checkout or raw container network failure is not repository unavailability while connected repository source remains accessible.

## Step 2 — atomic C+C2 XI/odds execution

Use `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`.

For every authorized normal or exception assessment:
1. freeze one common current XI/research/market/tournament evidence epoch;
2. freeze C model-owned inputs;
3. freeze C2 model-owned inputs independently;
4. persist both frozen inputs;
5. execute both deterministically;
6. persist both outputs;
7. only then publish the completed verdict.

Primary runtime:

`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

Required:

`ENGINE EXECUTION STATUS: EXECUTED_C_C2_PAIR`

If C2 cannot be lawfully frozen/executed:

`C+C2 EXCEPTION INCOMPLETE — <exact reason>`

A C-only completed exception is forbidden.

Mandatory Step-2 evidence includes:
- confirmed/reliable XI;
- fresh post-XI football research;
- market-history attempt;
- H2H recheck;
- tournament-incentive recheck when applicable;
- fixture-status revalidation;
- quote revalidation;
- C completion recheck;
- C2 route-quality recheck.

## Active-model accounting

New/current accounting uses C + C2 only.

Priority per model/fixture:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

WATCH:
- own supported line;
- assumed odds 1.65;
- 1u;
- model-performance accounting only.

WAIT:
- own deterministic target/min odds;
- frozen accounting semantics under `FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

Only C may create official Website Picks/exposure. C2 accounting is shadow-only.

### Actual-user P/L authority — reset 2026-10-08

Canonical actual-user bet ledger: Airtable table `Actual Bets — Current` (`tblF0MSRTuqCWlL8s`).

From 2026-10-08 ICT onward:
- actual-user profit/loss, turnover, ROI and running P/L are calculated from this table only by default;
- do not mix older actual-bet records into current profit unless the user explicitly requests historical combined reporting;
- actual-user execution truth comes only from rows in this table (or a new user slip awaiting persistence);
- Website Picks, Decision States, model WATCH/WAIT accounting and C2 shadow exposure must never be counted as actual-user P/L.

Historical C3/C4 settlement must use explicit historical accounting mode and must never enter a current active-roster payload.

## Live

Use `models/football/prompts/03_NORMAL_CHAT_LIVE.md`.

Current live roster:
- Football C official;
- Football C2 shadow.

No live-stat confirmation gate is required. Assess from score/minute, current quote, frozen thesis and concrete material events. Recompute tournament incentive at each material live epoch when applicable.

C2 never creates official exposure.

## Audit

Use `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`.

Audit all recorded assessed matches, not only Website Picks or LOCK/FOLLOW rows.

Separate:
- frozen state;
- observed result;
- diagnosis;
- official C model P/L;
- C2 shadow model P/L where lawfully countable;
- actual user P/L.

Missing C2 execution in a current all-model/C+C2 exception is a workflow defect, not a C2 PASS.

Never retrospectively reconstruct missing model outputs from FT/current information.

Historical C3/C4 rows may be reported only as historical records from their original frozen epochs.

## Persistence

Current new records must keep C and C2 separate.

Daily Coverage / board persistence:
- C state/rank/line/basis;
- C2 state/rank/line/basis;
- common evidence basis;
- official C lane;
- pair reconciliation status/revision.

Decision States:
- C Action;
- C Supported Line;
- C2 Supported Line;
- C2 Shadow Action;
- Engine Execution Status;
- Engine C Result;
- Engine C2 Result;
- failure reason when applicable;
- current evidence/recheck fields;
- active-model accounting result.

Website Picks:
- Football C official exposure only.

Historical C3/C4 fields may remain in Airtable for immutable history. Do not populate them for new current rows.

## Historical fidelity

Do not rewrite:
- historical C3/C4 board states;
- historical C3/C4 supported lines/actions;
- old engine results;
- old accounting rows;
- old Football A records.

Retired files may remain for audit/history but must not be imported by current runtime or required by current launchers.

## Production principle

Current authority is simple:

**Football C decides official exposure. Football C2 challenges it prospectively. Everything else is historical.**
