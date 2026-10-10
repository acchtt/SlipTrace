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

If the fixture is no longer prematch, **continue the assessment automatically
in this same /xi turn**. Do NOT send the started fixture to the prematch
`xi_portable.py pair` input, and do not stop at a terminal
`DECISION BLOCKED — STEP2 FIXTURE NOT CONFIRMED PREMATCH` response.
First execute:
`python models/football/engine/step2_fixture_transition.py --input <transition.json>`
using independently verified KO/fixture status and current assessment time.
For `STARTED`, `EARLY_LIVE_FAST_PATH` (first 15 minutes) and
`STANDARD_LIVE` (afterward) **both permit continued football assessment**.
They require no second user command and no new Work/sweep handoff.
The 15-minute threshold is a speed-path distinction, **never a hard
assessment cutoff**. This is particularly important when an FOCUS match
is first examined minutes after kickoff.

Immediately follow the `/live` launcher from the saved independent C and
C2 premises:
- Capture score and minute, goal/red-card/major injury/substitution events,
  current tournament incentive when relevant and **fresh in-play quote**
  when available; do not wait for live-stat dashboards.
- Preserve the frozen prematch/XI analysis separately. At 0-0 and with no
  material changes, reuse the *football research* after a rapid verification;
  never reuse a prematch price, status or computed bet authorization.
- If a goal or material event occurred, re-evaluate the thesis and
  clearing-goal burden at the new live score; a goal does not erase the
  obligation to assess, but invalidates old price and funding conclusions.
- Continue immediately with a **qualitative C/C2 football assessment**
  even when current live odds are missing. Label it
  `LIVE QUOTE REQUIRED — NO EXECUTABLE BET` and state the currently
  supportable goal burden; do not invent a quote or C2 result.
- Only a genuinely fresh live quote, current state, independently
  checked C and C2 evidence and the required live integrity checks may
  produce an actionable C live assessment. C2 remains shadow-only.
- In Step-2 reconciliation persist `LIVE_REROUTED` with a reference
  to the **actual** live assessment, not an invented placeholder. Keep
  it open if no live verdict was completed. Do not retrospectively
  re-label the missed prematch opportunity as C-BET/C2-BET.

`PREMATCH_CONFIRMED` *after* independently verified kickoff should
yield `VERIFY_LIVE_STATUS`, not silently authorize a stale PRE quote.
Finished fixtures go to audit only; postponed/cancelled fixtures do not
produce an executable selection.


### Time-critical /xi decision path (C official + C2 shadow)

**No indefinite FOCUS monitoring.** Once a match has been authorized for
Step 2, preassemble its *already frozen* C and C2 supported burdens,
independent goal-three/goal-four funding claims and outstanding football
questions **before** chasing an actionable price. Goal funding is a
football judgment made from source-backed evidence; it must never be
inferred from a low Over line or attractive market odds.

For the first current XI + executable price epoch:

1. Run the mandatory fresh post-XI, market-history **attempt** and
   tournament-incentive checks below as a single bounded research pass.
   A legitimate PARTIAL/UNAVAILABLE_ATTEMPTED market-history state is not
   a reason to re-search indefinitely; preserve the real result.
2. Recheck the C and C2 scoring mechanisms and clearing-goal funding
   *once* against the same current evidence epoch. A prior frozen
   conclusion is not automatically valid after meaningful XI/football
   changes, but unchanged research must not be repeated merely to delay
   a verdict.
3. Immediately execute the pinned portable C+C2 pair and perform the
   existing persistence/read-back/publication guard. Report both
   deterministic actions with current lines/prices and brief mechanisms:
   **ACT** (only C official BET), **WAIT** (explicit reachable total,
   minimum odds, and expiry/event), or **PASS** (specific football/price
   failure). C2 BET is **SHADOW ACT**, never a user bet instruction.
4. If the official C price is unsuitable but C2 meets its price floor,
   **still execute both**; neither model may inherit the other's line
   or goal-three gate. If an essential source/XI/quote is missing,
   issue a precise `INCOMPLETE — NEXT EVIDENCE REQUIRED` or
   `INTEGRITY_BLOCKED` promptly, **not** a football PASS.
5. A WAIT that needs an unlikely future total, negative team news or
   a kickoff-window violation must be a PASS. Never wait for a lower
   line as a substitute for resolving the third-goal hypothesis.

**Timing/accountability:** capture evidence-epoch time and user-visible
decision-delivery time; tag source/runtime/persistence blockers separately
from C/C2 football PASS. Never count an unplaced hypothetical bet as an
actual win, and never backdate a quote after a goal.

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

### New Step-2 prepublication gate — mandatory

After persisting a proposed C+C2 Decision State, but **before publishing a
BET/WAIT/PASS verdict to the user or writing a Website Pick**, read that
Airtable record back independently and run:

`python models/football/engine/step2_publication_guard.py --input <publication_check.json>`

The check requires the original C and C2 frozen input JSON, the unmodified
deterministic pair receipt, the independently retrieved Decision State fields,
the currently active engine revision, and the latest same-fixture evidence
epoch. Store the new epoch in Airtable `C+C2 Evidence Epoch ID` and
record the final `C+C2 Publication Key` only after approval. Build
`previously_published_keys` from current Airtable read-back, not memory.
If a goal, substitution, fixture status or executable quote changes before
publication, set the latest epoch/current quote/status from that update
and fail closed; reassess from the newer epoch.

The serialized engine result stored in Decision States must be normalized
with `supported_line` from **that model's frozen input**, not copied from
the other model. Both independent supported-line fields remain mandatory.

The program validates deterministic receipt/read-back consistency, not
the origin of its own supplied flags. The caller must really re-fetch the
current fixture/quote and stored record, not just assert freshness.
A `STEP2 PUBLICATION ELIGIBLE` result is a prerequisite, **not** evidence
that a bet was placed. Any blocked result means no actionable verdict or
new Website Pick. For live exceptions, preserve the live assessment epoch
and do not republish an obsolete pre-goal quote. Old records are audit-only
and are never retroactively relabeled.

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
