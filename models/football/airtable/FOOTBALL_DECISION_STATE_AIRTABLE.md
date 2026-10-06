# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Table ID:** `tblQmUpd5WjBLQ38X`  
**Official model:** Football C  
**Only active shadow model:** Football C2 — SHADOW

This table stores material post-board assessment epochs. Historical Football A/C3/C4 rows keep the model/version and fields that actually produced them. Historical compatibility does not reactivate retired models.

## 1. Current authority

For every **new/current** assessment:
- official model = Football C;
- active shadow = Football C2 — SHADOW;
- only C may create official exposure / Website Picks;
- C2 is comparison-only;
- C3/C4 are retired from new/current execution;
- deterministic Python is validation/accounting, not decision authority.

Current semantics come from:
- `CURRENT_MODEL.md`;
- `FOOTBALL_C_C2_ACTIVE_PAIR.md`;
- `02_NORMAL_CHAT_XI_ODDS.md`;
- `03_NORMAL_CHAT_LIVE.md`.

Legacy Football A compilers and retired challenger files may be read only for historical audit fidelity.

## 2. Frozen-board dependency

Before Step 2, resolve the fixture against the exact frozen current board in Daily Coverage.

Preserve:
- canonical fixture identity;
- kickoff;
- C state/rank/lane;
- C supported burden;
- C completion/continuation/stall diagnostics;
- C2 state/rank;
- C2 supported burden;
- operational viability/reliability snapshot;
- tournament-incentive state;
- common frozen evidence epoch.

A later Step-2/live epoch may downgrade or invalidate the current thesis but must never rewrite the frozen Step-1 board.

If persistence conflicts with the original frozen board:

`PERSISTENCE SYNC FAULT — FROZEN FOOTBALL C BOARD PRESERVED`

## 3. Current C + C2 fields

Persist where applicable:
- Assessment ID;
- Match / Competition / canonical fixture ID;
- Model Version;
- Assessment Time;
- Minute / Score / evidence epoch;
- C Action;
- C Supported Line;
- C2 Supported Line;
- C2 Shadow Action;
- evaluated line / odds;
- XI state;
- post-XI research status/note;
- market-history trace;
- H2H material state/basis;
- tournament-incentive applicability + VERIFIED recheck state when required;
- current route/carrier/failure evidence;
- exact reason/blocker;
- Engine Execution Status;
- Engine Source Revision;
- Engine C Result;
- Engine C2 Result;
- Engine Failure Reason when applicable;
- active-model accounting result/revision.

The physical table may still contain C3/C4 columns. For new rows, leave retired-model fields blank unless a migration explicitly documents otherwise.

## 4. Common evidence + model-owned policy

C and C2 share the same current factual evidence epoch.

Shared facts include:
- fixture status;
- XI/personnel;
- route/carrier facts;
- current failure/suppression facts;
- H2H state;
- tournament incentive;
- market-history trace;
- current quote.

Model-owned state remains separate.

Football C owns:
- completion recheck;
- current completion mode/quality;
- continuation;
- opponent leakage;
- stall risk;
- C supported line;
- C action.

Football C2 owns:
- route-quality recheck;
- C2 supported line;
- C2 shadow action.

Never copy C's supported line/action into C2.

If C2 cannot be lawfully frozen or executed from the same current evidence epoch:

`C+C2 EXCEPTION INCOMPLETE — <exact reason>`

A completed C-only active-roster exception is invalid.

## 5. Required current Step-2 evidence

Before a completed current decision:
- `xi_status = CONFIRMED / RELIABLE`;
- `fixture_status = PREMATCH_CONFIRMED`;
- fresh post-XI football research attempted;
- non-empty `post_xi_research_note`;
- market-history attempt;
- H2H recheck;
- tournament-incentive VERIFIED recheck when applicable;
- current quote revalidated;
- C `completion_rechecked = true`;
- C2 `c2_route_quality_rechecked = true`.

A deterministic contract rejection is not a Python/runtime failure.

If the fixture already started, route to live rather than forcing a prematch Decision State.

## 6. Current decision order

Football C:

`FROZEN C BOARD -> AUTHORIZATION -> STATUS/XI -> POST-XI RESEARCH -> MARKET HISTORY -> H2H/TOURNAMENT RECHECK -> C COMPLETION RECHECK -> QUOTE REVALIDATION -> C ACTION -> PERSIST`

Football C2:

`FROZEN C2 BOARD + OWN SUPPORTED LINE -> SAME CURRENT EVIDENCE -> C2 ROUTE-QUALITY RECHECK -> C2 SHADOW ACTION -> PERSIST`

Both active outputs must belong to the same evidence epoch.

## 7. Atomic engine execution

Primary:

`python xi_portable.py pair --c <c.json> --c2 <c2.json>`

Required completed status:

`EXECUTED_C_C2_PAIR`

Dedicated fields:
- `Engine Execution Status` — `fldhU9rA7EITaYxuM`
- `Engine Source Revision` — `fld5ZVej5DSbZhPi4`
- `Engine C Result` — `fldUktpv7mWLBzvGh`
- `Engine C2 Result` — `fldpKcoEQ5zqA1knO`
- `Engine Failure Reason` — `fldznzspLsOuIHn2F`

Historical compatibility field:
- `Engine C3 Result` — `fldg9oq2g3PiAe53d`

Do not populate Engine C3 Result for a new current assessment.

Completed current statuses:
- `EXECUTED_C_C2_PAIR`
- `FAILED_AFTER_ATTEMPT`

`FAILED_AFTER_ATTEMPT` requires:
- actual current-turn runtime/repository probes;
- preserved C and C2 structured inputs;
- exact command/setup path;
- exact error.

The old generic:

`ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED`

is invalid for current production.

## 8. C official exposure / WAIT bookkeeping

Dedicated fields:
- `C Exposure Basis` — `fldf6w7o7yi8KPr2G`
- `C Exposure Line` — `fldfRLDGRjvHJ2gML`
- `C Exposure Odds` — `fldbCbFCvLD5KArBA`
- `WAIT Resolution` — `fldhATXMaqVDB4KpO`
- `WAIT Reconciliation Note` — `fldbQgbncu2XIXydA`

Current C exposure bases:
- `DIRECT_BET`;
- `WAIT_ASSUMED`;
- `WAIT_USER_CONFIRMED`;
- `WAIT_NOT_REACHED`;
- `NONE`.

C2 may never create official exposure.

A matching user slip may reconcile C execution to actual line/odds/stake while preserving the frozen model target.

An explicit user statement that the target never reached removes that WAIT exposure layer without rewriting the original C-WAIT decision.

## 9. Active-model accounting

Aggregate fields:
- `All Model Accounting Result` — `fldOEt6DO20U9Yyab`
- `Model Accounting Revision` — `fldIAqPB03Oian4Fw`

The aggregate field name is historical. For **new/current** rows, store the active C+C2 result only:

`ACTIVE_C_C2`

Accounting priority:

`DIRECT BET > COUNTABLE WAIT > WATCH > NONE`

C2 accounting is shadow-only.

Historical C3/C4 settlement must use explicit historical-roster mode and must never be injected into a current C+C2 accounting payload.

## 10. Market-history fields

Dedicated fields:
- `Market History Status` — `fldvt8MMJXSt5C2b6`
- `Market History Open Total` — `fldHF3GBjcPlMV8xD`
- `Market History Pre-XI Total` — `fldVphdjWI21noJe3`
- `Market History Current Center` — `fldBYaxymYIwJZHO5`
- `Market History Movement` — `fldEjQGGA9siB8YzT`
- `Market Conflict Recheck` — `fldvoIAnj9NCFZFuQ`
- `Market History Note` — `fldDPLEXFDLH58Xdu`

These are common evidence for C/C2. Market movement cannot create football structure or exposure authority.

## 11. Website Pick transaction

For C-BET:
1. persist Decision State;
2. set C Exposure Basis = DIRECT_BET;
3. persist exact quote;
4. publish/reconcile one Website Pick;
5. verify no duplicate official pick.

For C-WAIT:
1. persist Decision State;
2. set C Exposure Basis = WAIT_ASSUMED;
3. persist deterministic WAIT target/minimum as exposure line/odds;
4. set WAIT Resolution = ASSUMED_REACHED;
5. publish/reconcile one Website Pick under the current WAIT compatibility contract;
6. verify no duplicate official pick.

For C-PASS:
- persist Decision State with C Exposure Basis = NONE;
- no official Website Pick.

For C2:
- persist shadow metadata/accounting only;
- never Website Pick.

If Decision State succeeds but official Website Pick fails:

`PERSISTENCE SYNC FAULT`

## 12. Live epochs

A goal, red card, major injury, material tactical/mechanism change, or material tournament-incentive change creates a new evidence epoch.

Do not overwrite the prematch/XI epoch.

Persist live advisory changes separately while preserving:
- original frozen plan;
- original WAIT accounting state;
- current score/minute;
- new quote;
- material event basis;
- current C official action;
- current C2 shadow action.

## 13. Historical C3/C4 fidelity

Historical C3/C4 fields may remain populated only on records that genuinely came from those models' active eras.

Do not:
- delete those historical values;
- relabel them as C/C2;
- use FT/current information to backfill missing retired-model states;
- treat retired-model fields as required current columns;
- write new C3/C4 current actions.

Historical retired-model settlement belongs in explicitly historical audit mode.

## 14. Identity / duplicate guard

Use canonical fixture identity.

If two current records disagree materially on fixture identity, kickoff, C state, C2 state, supported burdens, or current exposure:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

Do not resolve by last-write-wins.

## 15. Step-2 session completeness

A persisted Decision State does not prove the session is complete.

Run the session reconciliation contract and require:

`STEP2 RECONCILIATION STATUS: PASS`

Every due FOLLOW / activated RESERVE / user exception must have exactly one disposition.

Silent omission is a workflow failure.
