# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Official model:** Football C  
**Shadow comparison model:** Football C2 — SHADOW  
**Current execution authority:** `models/football/CURRENT_MODEL.md` + `models/football/production/FOOTBALL_C.md` + `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` + `models/football/prompts/03_NORMAL_CHAT_LIVE.md`

This table stores material post-board assessment epochs. It must preserve the model/version that actually produced each historical record and must never reinterpret a historical Football A/v0.2.x record as Football C.

## 1. Current authority

For every **new** assessment:

- official model identifier = `Football C`;
- shadow identifier = `Football C2 — SHADOW`;
- only Football C may create official exposure / Website Picks;
- C2 is comparison-only;
- the Python engine is a validator, not decision authority;
- the current Football C/C2 launcher stack controls semantics.

The following files are **historical Football A compilers only** and are not authority for new Football C decisions:

- `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`;
- `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`;
- old v0.2.x / Football A rule files.

If an old field name remains in Airtable for compatibility, its existence does not activate the old rule that created it.

## 2. Frozen-board dependency

Before Step 2, resolve the fixture against the exact frozen Football C board state in Daily Coverage.

Preserve:
- canonical AiScore identity;
- C board state/rank;
- C supported burden;
- C2 board state/rank and C2 supported burden when available;
- frozen completion mode/quality, continuation, leakage and stall risk;
- operational viability/reliability snapshot;
- tournament-incentive state;
- frozen research epoch.

A later Step-2/live state may downgrade or invalidate the thesis but must never rewrite the frozen Step-1 board.

If Daily Coverage conflicts with the original frozen board artifact:

`PERSISTENCE SYNC FAULT — FROZEN FOOTBALL C BOARD PRESERVED`

## 3. Time / identity

Use `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

- a serialized `Z` timestamp is UTC;
- convert to ICT once for display;
- revalidate near-kickoff fixture status/time;
- a goal/red card/material event creates a new evidence epoch;
- never overwrite the earlier epoch.

## 4. Current Football C material fields

Persist where applicable:

- Assessment ID;
- Match / Competition / canonical AiScore ID;
- Model Version;
- Assessment Time;
- Minute / Score / epoch;
- official C verdict = `C-BET / C-WAIT / C-PASS`;
- shadow C2 verdict = `C2-BET — SHADOW / C2-WAIT — SHADOW / C2-PASS — SHADOW`;
- evaluated line / odds;
- XI state;
- post-XI research status;
- H2H material state;
- tournament incentive applicability + VERIFIED recheck state;
- current route/carrier/failure evidence;
- exact blocker/reason;
- engine C result;
- engine C2 result where valid.

Dedicated C/C2 separation fields:
- `C Action`;
- `C Supported Line`;
- `C2 Supported Line`;
- `C2 Shadow Action`.

The legacy generic `Verdict` field remains historical compatibility only. Do not encode a new Football C action by reusing Football A-era verdict labels.

Burden-completion Step-2 fields:

- `Current Completion Mode`;
- `Current Completion Quality`;
- `Current Continuation Quality`;
- `Current Opponent Leakage`;
- `Current Stall Risk`.

These are current-epoch fields. They do not overwrite frozen Step-1 completion fields in Daily Coverage.

## 5. Separate C and C2 burden state

Football C and Football C2 may share the same underlying football evidence but they do **not** share model policy.

Persist separately when available:

- C supported line;
- C2 supported line;
- C board state;
- C2 board state;
- C action;
- C2 shadow action.

Never copy C's supported burden into C2 merely to simplify persistence.

If C2's independently frozen supported burden is unavailable:

`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`

Do not count that row in confirmatory C-vs-C2 exposure metrics.

## 6. User-supplied XI + current odds

The user's confirmed XI and current executable odds are the current execution epoch.

- use the supplied quote directly;
- do not request a second confirmation;
- do not fabricate missing XI/price;
- perform the mandatory fresh post-XI football research pass;
- perform the mandatory tournament-incentive recheck when applicable;
- recheck completion/continuation/leakage/stall risk;
- issue the Football C official action and C2 shadow action from the same factual evidence epoch.

If a required final input is missing:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

## 7. Current decision order

Football C:

`FROZEN C BOARD -> IDENTITY/STATUS -> CONFIRMED XI -> FRESH POST-XI RESEARCH -> TOURNAMENT/H2H RECHECK -> COMPLETION/CONTINUATION RECHECK -> CURRENT QUOTE -> C-BET/C-WAIT/C-PASS -> PERSIST`

Football C2:

`FROZEN C2 BOARD + INDEPENDENT C2 SUPPORTED BURDEN -> SAME CURRENT EVIDENCE -> C2 FLOOR/BRIDGE POLICY -> C2-BET/C2-WAIT/C2-PASS — SHADOW -> PERSIST`

The old Football A PRE/EGE/MCE/CC+/OFFICIAL LOCK compiler is not part of this order.

## 8. Price / wait policy

Football C current price policy:

- >=1.65 normal acceptable zone;
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material veto;
- <1.60 normally WAIT/PASS;
- higher payout never manufactures a higher supported burden.

Every C-WAIT records:
- target line;
- minimum odds;
- cancellation event;
- thesis-health requirement.

Target reached does not auto-execute.

## 9. Official exposure semantics

Current official exposure exists only from a persisted Football C `C-BET` that is reconciled to Website Picks / user execution.

C2 may never create official exposure.

Do not count these as official P/L:
- C-PASS;
- C-WAIT with no entry;
- C2 shadow;
- counterfactual;
- missed opportunity;
- historical calibration-only states.

User bet slip remains physical execution truth.

## 10. Historical fidelity

Historical Football A/v0.2.x rows retain:
- their original Model Version;
- original verdict labels;
- original fields;
- original settlement semantics.

Do not relabel or recompute them under Football C.

Legacy Airtable columns may remain populated for historical records. For a new Football C record, leave obsolete Football A-only fields blank unless they are reused by an explicitly documented current mapping.

## 11. Persistence transaction

For every new current assessment, persist `C Action` explicitly.

For C-BET:
1. persist Decision State;
2. publish/reconcile one Website Pick;
3. verify no duplicate official pick.

For C-WAIT/C-PASS:
- Decision State only.

For C2:
- Decision State/shadow metadata only;
- never Website Pick.

If Decision State succeeds but official Website Pick fails:

`PERSISTENCE SYNC FAULT`

If canonical identity is conflicting:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`
