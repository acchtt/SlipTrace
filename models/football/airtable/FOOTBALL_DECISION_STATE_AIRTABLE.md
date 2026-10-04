# Football Decision States — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Decision States`  
**Official model:** Football C  
**Shadow comparison models:** Football C2 — SHADOW; Football C3 — SHADOW  
**Current execution authority:** `models/football/CURRENT_MODEL.md` + `models/football/production/FOOTBALL_C.md` + `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` + `models/football/prompts/03_NORMAL_CHAT_LIVE.md`

This table stores material post-board assessment epochs. It must preserve the model/version that actually produced each historical record and must never reinterpret a historical Football A/v0.2.x record as Football C.

## 1. Current authority

For every **new** assessment:

- official model identifier = `Football C`;
- shadow identifiers = `Football C2 — SHADOW` and `Football C3 — SHADOW`;
- only Football C may create official exposure / Website Picks;
- C2 and C3 are comparison-only;
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
- C3 board state/rank/lane, C3 supported burden and frozen funding/control fields when available;
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
- C exposure basis / accounting line / accounting odds;
- WAIT resolution / reconciliation note;
- shadow C2 verdict = `C2-BET — SHADOW / C2-WAIT — SHADOW / C2-PASS — SHADOW`;
- shadow C3 verdict = `C3-BET — SHADOW / C3-WAIT — SHADOW / C3-PASS — SHADOW`;
- evaluated line / odds;
- XI state;
- post-XI research status;
- market-history status / opening total / pre-XI total / current market center / movement / conflict recheck / source note;
- H2H material state;
- tournament incentive applicability + VERIFIED recheck state;
- current route/carrier/failure evidence;
- exact blocker/reason;
- engine C result;
- engine C2 result where valid.

Semantic evidence-basis persistence:
- persist H2H state/effect/transferability/current-corroboration/material-effect plus a non-empty H2H basis whenever H2H is reviewed;
- persist the basis for thesis state, primary-mechanism integrity, WAIT reachability, negative-information dependence and material veto in the current Decision State evidence summary and deterministic result;
- persist common assessment bases for carrier self-funding, independent upper-tail, failure-route attack and material suppression in the current evidence summary / machine result;
- a bare Boolean without its same-epoch basis is an incomplete current Decision State.

Dedicated C/C2/C3 separation fields:
- `C Action`;
- `C Supported Line`;
- `C2 Supported Line`;
- `C2 Shadow Action`;
- `C3 Supported Line`;
- `C3 Shadow Action`;
- current C3 second-route / goal-3 / goal-4 / control fields defined in `FOOTBALL_C3_AIRTABLE.md`;
- `All Model Accounting Result`;
- `Model Accounting Revision`.

The legacy generic `Verdict` field remains historical compatibility only. Do not encode a new Football C action by reusing Football A-era verdict labels.

Burden-completion Step-2 fields:

- `Current Completion Mode`;
- `Current Completion Quality`;
- `Current Continuation Quality`;
- `Current Opponent Leakage`;
- `Current Stall Risk`.

These are current-epoch fields. They do not overwrite frozen Step-1 completion fields in Daily Coverage.

## 5. Separate C, C2 and C3 policy state

Football C, Football C2 and Football C3 share the same underlying football facts but they do **not** share model policy.

Persist separately when available:

- C supported line;
- C2 supported line;
- C board state;
- C2 board state;
- C action;
- C2 shadow action;
- C3 supported line;
- C3 shadow action;
- C3 current funding/control block.

Never copy C's supported burden into C2 or C3 merely to simplify persistence.

If C2's independently frozen supported burden is unavailable:

`C2 COMPARISON INCOMPLETE — SUPPORTED BURDEN NOT INDEPENDENTLY FROZEN`

Do not count that row in confirmatory C-vs-C2 exposure metrics.

If C3's independent burden/funding state is unavailable:

`C3 COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`

Do not count that row in confirmatory C-vs-C3 metrics.

## 6. User-supplied XI + current odds

The user's confirmed XI and current executable odds are the current execution epoch.

- use the supplied quote directly;
- do not request a second confirmation;
- do not fabricate missing XI/price;
- perform the mandatory fresh post-XI football research pass and preserve a non-empty post-XI research note in the Decision State evidence summary/machine result;
- perform the mandatory market-history attempt from `FOOTBALL_MARKET_HISTORY_RECHECK.md`;
- perform the mandatory tournament-incentive recheck when applicable;
- revalidate fixture status immediately before prematch decision execution;
- revalidate the user's executable quote immediately before deterministic execution;
- run model-owned current rechecks separately: C completion/continuation, C2 route quality, C3 funding/control;
- issue the Football C official action plus C2/C3 shadow actions from the same factual evidence epoch when the fixture is already being assessed.

If a required final input is missing:

`WAITING FOR USER XI/ODDS — NO OFFICIAL DECISION`

## 7. Current decision order

Football C:

`FROZEN C BOARD -> STEP2 DUE-SET AUTHORIZATION -> IDENTITY/STATUS -> FIRST-PASS XI -> FRESH POST-XI RESEARCH -> MARKET-HISTORY ATTEMPT -> MARKET CONFLICT RECHECK -> TOURNAMENT/H2H RECHECK -> COMPLETION/CONTINUATION RECHECK -> CURRENT QUOTE -> FINAL STATUS/QUOTE REVALIDATION -> C-BET/C-WAIT/C-PASS -> PERSIST -> STEP2 RECONCILIATION`

Football C2:

`FROZEN C2 BOARD + INDEPENDENT C2 SUPPORTED BURDEN -> SAME CURRENT EVIDENCE -> C2 FLOOR/BRIDGE POLICY -> C2-BET/C2-WAIT/C2-PASS — SHADOW -> PERSIST`

Football C3:

`FROZEN C3 BOARD + INDEPENDENT C3 FUNDING/CONTROL STATE -> SAME CURRENT EVIDENCE -> C3 FUNDING RECHECK -> C3-BET/C3-WAIT/C3-PASS — SHADOW -> PERSIST`

The old Football A PRE/EGE/MCE/CC+/OFFICIAL LOCK compiler is not part of this order.

## 8. Price / wait policy

Apply:
- `models/football/procedures/FOOTBALL_MODEL_BET_ACCOUNTING.md`;
- `models/football/procedures/FOOTBALL_WAIT_ASSUMED_EXPOSURE.md`.

C/C2/C3/C4 WATCH accounting is handled separately from operational exposure. A frozen WATCH counts at that model's supported line @1.65, 1u.

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

For accounting, a valid C-WAIT **immediately** becomes `WAIT_ASSUMED` at target line/minimum odds. No later market-reach proof is required.

The model action remains C-WAIT. Only:
- a matching user bet slip -> `WAIT_USER_CONFIRMED / USER_CONFIRMED`; or
- an explicit user statement that the target line never reached -> `WAIT_NOT_REACHED / USER_DECLARED_NOT_REACHED`

may change that accounting state.

## 9. Official exposure semantics

A persisted Football C C-BET is direct official model exposure.

A persisted Football C C-WAIT is assumed official model exposure at its frozen target line/minimum odds unless the user explicitly says that target line never reached.

Exposure basis:
- `DIRECT_BET`;
- `WAIT_ASSUMED`;
- `WAIT_USER_CONFIRMED`;
- `WAIT_NOT_REACHED`;
- `NONE`.

Actual user execution/P&L remains separate and comes only from the user's bet slip.

A matching user slip may reconcile a C-WAIT to exact actual line/odds/stake while preserving the original WAIT target.

If the user explicitly says the target line never reached, the C-WAIT decision remains frozen but official exposure is removed:
`WAIT_NOT_REACHED — USER_DECLARED — NO MODEL EXPOSURE / NO MODEL P&L`

C2/C3 may never create official exposure; their WAITs and WATCHs are shadow model-accounting only. C4-WATCH is also shadow model-accounting despite C4 having no Step-2 action.

Do not count C-PASS as operational official exposure. A prior C-WATCH may still remain countable in the separate model-accounting ledger.

A missing user slip, missing market-history proof, or lack of later mention does not erase a WAIT_ASSUMED model result.

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
2. set `C Exposure Basis = DIRECT_BET`;
3. persist exact quote as C Exposure Line/Odds;
4. publish/reconcile one Website Pick;
5. verify no duplicate official pick.

For C-WAIT:
1. persist Decision State;
2. set `C Exposure Basis = WAIT_ASSUMED`;
3. persist deterministic WAIT target/minimum as C Exposure Line/Odds;
4. set `WAIT Resolution = ASSUMED_REACHED`;
5. publish/reconcile one Website Pick immediately;
6. verify no duplicate official pick.

For C-PASS:
- Decision State only with `C Exposure Basis = NONE`.

Later reconciliation of a C-WAIT is allowed only from a matching user slip or explicit user statement that the target line never reached.

For C2/C3:
- Decision State/shadow metadata only;
- never Website Pick.

If Decision State succeeds but official Website Pick fails:

`PERSISTENCE SYNC FAULT`

If canonical identity is conflicting:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`


## 11A. WAIT exposure accounting fields

Dedicated Decision State fields:
- `C Exposure Basis` — `fldf6w7o7yi8KPr2G`
- `C Exposure Line` — `fldfRLDGRjvHJ2gML`
- `C Exposure Odds` — `fldbCbFCvLD5KArBA`
- `WAIT Resolution` — `fldhATXMaqVDB4KpO`
- `WAIT Reconciliation Note` — `fldbQgbncu2XIXydA`

These fields control legacy C operational WAIT bookkeeping only. They do not overwrite `C Action` or the frozen model target.

## 11B. All-model accounting fields

- `All Model Accounting Result` — `fldOEt6DO20U9Yyab`
- `Model Accounting Revision` — `fldIAqPB03Oian4Fw`

Persist the exact C/C2/C3/C4 accounting result after Step-2 reconciliation. The accounting result uses `DIRECT BET > COUNTABLE WAIT > WATCH > NONE`.

## 12. Market-history fields

Dedicated Decision State fields:
- `Market History Status` — `fldvt8MMJXSt5C2b6`
- `Market History Open Total` — `fldHF3GBjcPlMV8xD`
- `Market History Pre-XI Total` — `fldVphdjWI21noJe3`
- `Market History Current Center` — `fldBYaxymYIwJZHO5`
- `Market History Movement` — `fldEjQGGA9siB8YzT`
- `Market Conflict Recheck` — `fldvoIAnj9NCFZFuQ`
- `Market History Note` — `fldDPLEXFDLH58Xdu`

These fields are common evidence for C/C2/C3. They do not grant exposure authority.


## 13. Deterministic engine execution fields

Dedicated Decision State fields:
- `Engine Execution Status` — `fldhU9rA7EITaYxuM`
- `Engine Source Revision` — `fld5ZVej5DSbZhPi4`
- `Engine C Result` — `fldUktpv7mWLBzvGh`
- `Engine C2 Result` — `fldpKcoEQ5zqA1knO`
- `Engine C3 Result` — `fldg9oq2g3PiAe53d`
- `Engine Failure Reason` — `fldznzspLsOuIHn2F`

Every completed Step-2 Decision State must persist one execution status:
- `EXECUTED_ALL_THREE`
- `FAILED_AFTER_ATTEMPT`

The serialized engine result/evidence summary must also preserve:
- `fixture_status`;
- `h2h_state`;
- `h2h_effect`;
- `h2h_transferability`;
- `h2h_current_corroboration`;
- `h2h_material_effect`;
- `h2h_basis`;
- `thesis_state_basis`;
- `primary_mechanism_basis`;
- `wait_reachability_basis`;
- `wait_negative_info_basis`;
- `material_veto_basis`;
- `carrier_self_fund_basis`;
- `independent_upper_tail_basis`;
- `failure_attacks_route_basis`;
- `material_suppression_basis`;
- `quote_revalidated`;
- `post_xi_research_note`;
- C `completion_rechecked` or shadow-owned `c2_route_quality_rechecked` / `c3_funding_rechecked`;
- official `official_follow_lane` and `step2_authorization`.

Step-2 session completeness is separately validated by `FOOTBALL_STEP2_SESSION_RECONCILIATION.md`; a persisted Decision State does not by itself prove that every due fixture was handled.

`FAILED_AFTER_ATTEMPT` requires a non-empty exact technical reason and preserved structured C/C2/C3 inputs.

No-local-checkout / GitHub-only source access is not a failure reason. Follow `FOOTBALL_ENGINE_EXECUTION_BOOTSTRAP.md` and materialize/setup the current engine first.

The old generic `ENGINE NOT EXECUTED — STRUCTURED INPUT PRESERVED` state is not valid for current production.
