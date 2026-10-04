# Football Daily Coverage Ledger — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Daily Coverage Ledger`  
**Table ID:** `tblcl1UAyMqZT6Ub0`  
**Official model:** Football C

This table is the coverage-control and frozen-board bridge for the current Football C workflow.

## 1. Source contract

AiScore is the fixture-universe authority.

- `Source 1` = AiScore / verified AiScore handoff;
- other sources may support research only;
- `Reconciled = true` means the requested AiScore window was fully traversed and every visible in-scope senior fixture received a disposition.

Preferred identity:
`Coverage ID = AISCORE:<fixture_id>`

Use a fallback key only when an AiScore ID is genuinely unavailable.

## 2. Time integrity

A trailing `Z` means UTC. Convert to Asia/Ho_Chi_Minh exactly once for display and derive Slate Date from the ICT kickoff.

Preserve schedule/identity faults explicitly:
- `TIMEZONE NORMALIZATION FAULT`;
- `SCHEDULE DATE MISMATCH`;
- `STALE UPCOMING STATE`;
- `KICKOFF CHANGE`;
- `FIXTURE IDENTITY / HOME-AWAY MISMATCH`.

Do not silently rewrite historical frozen state.

## 3. Current Step-0 eligibility

Current eligibility comes only from:
- `CURRENT_MODEL.md`;
- `00_NORMAL_CHAT_AISCORE_FETCH.md`;
- operational viability;
- competition reliability memory;
- researchability;
- women's top-flight coverage contract;
- capacity.

Historical Football A/v0.2.x country/league blanket overlays are **not** current authority.

Senior women's domestic top-flight leagues are first-class senior blocks. Set:
`Senior Women's Top Flight = true`

Every visible fixture in that class requires a row/disposition even when excluded/deferred.

## 4. Frozen Football C board fields

Preserve current official board state exactly.

Dedicated current fields now include:
- `C Board State`;
- `C Rank`;
- `C Supported Line`;
- `C2 Shadow State`;
- `C2 Shadow Rank`;
- `C2 Supported Line`;
- `C3 Shadow State`;
- `C3 Shadow Rank`;
- `C3 Lane`;
- `C3 Supported Line`;
- `C3 Second Route Role`;
- C3 goal-3 / goal-4 / control-endpoint fields defined in `FOOTBALL_C3_AIRTABLE.md`;
- `C4 Shadow State`;
- `C4 Shadow Rank`;
- `C4 Supported Line`;
- C4 structured compiler fields defined in `FOOTBALL_C4_AIRTABLE.md`;
- `C Model Accounting`;
- `C2 Shadow Accounting`;
- `C3 Shadow Accounting`;
- `C4 Shadow Accounting`;
- `Model Accounting Revision`.

Also preserve:
- Common Evidence Basis;
- Step0 Capacity Queue Rank;
- Step1 Replenished;
- Replenishment Wave;
- Replenishment Reason;
- Operational Grade;
- XI Expected;
- Market Observability where available;
- Team News Observability;
- Competition Reliability State / Reason;
- Operational Disposition;
- Senior Women's Top Flight;
- C board state/rank;
- C supported burden and Supported Line Basis;
- C Board State Basis;
- C2 Supported Line Basis and C2 Board State Basis;
- C3 Supported Line Basis;
- Completion Mode;
- Burden Completion Quality;
- Continuation Quality;
- Opponent Leakage;
- Burden Stall Risk;
- Same Kickoff Rank;
- tournament-incentive freeze;
- H2H/failure summary;
- Screened At;
- Frozen PRE Summary / Coverage Notes.

Where the physical Airtable schema still uses legacy columns such as `PRE Grade`, `Board Tier`, or `Structural Type`, use them only as storage aliases for the **actual frozen Football C output**. They do not activate Football A PRE compiler semantics.

C2 shadow fields/notes must be clearly separate:
- C2 state/rank;
- C2 supported burden;
- C2 diagnostics.

C3 shadow fields/notes must also be separate:
- C3 state/rank/lane;
- C3 supported burden;
- second-route role;
- goal-3 / goal-4 funding source and basis;
- control-endpoint risk/basis;
- C3 forced-chaos verification and basis.
- Board Triplet Common-Evidence Reconciliation Status / engine revision where available.

C2/C3/C4 must never overwrite official C fields.

C4 is Step-1-only. C4 persistence belongs in Daily Coverage + Sweep Runs only; do not create C4 Decision States or Website Picks. C4-WATCH may still carry shadow model-accounting JSON/P&L under `FOOTBALL_MODEL_BET_ACCOUNTING.md`; this is not Step-2 exposure.

## 5. Publish = exact copy, never re-screen

Publishing copies the already-frozen Step-0/Step-1 state.

Do not:
- rerank;
- change C state;
- change supported burden;
- reinterpret legacy grade labels;
- rebuild evidence during Airtable publication.

If publisher output conflicts with the frozen board:

`PERSISTENCE SYNC FAULT — FROZEN FOOTBALL C BOARD PRESERVED`

## 6. C / C2 / C3 / C4 policy separation

The underlying football research epoch is shared, but model policy/compilation is separate.

Persist C, C2, C3 and C4 supported burdens independently.

A C2 row without an independently frozen C2 burden is incomplete for C-vs-C2 paired evaluation.

A C3 row without an independently frozen C3 burden/funding block is incomplete for C-vs-C3 paired evaluation.

A C4 row without complete structured evidence anchors and deterministic compiler output is incomplete for C-vs-C4 paired evaluation. C4 incompleteness does not invalidate an otherwise clean official C/C2/C3 board, but it makes that board ineligible for the C4 0/5 counter.

Do not populate C3 fields from Football C completion labels or C2 route-quality output. Do not populate C4 compiled fields by copying C/C2/C3 semantic grades.

## 7. All-model accounting persistence

Dedicated Daily Coverage fields:
- `C Model Accounting` — `fldND2leUXgAq9UQl`
- `C2 Shadow Accounting` — `fldlWroOrJdYF3lHn`
- `C3 Shadow Accounting` — `fldEMKp5LzS5IZQpJ`
- `C4 Shadow Accounting` — `fldNvPrq9WTW9118X`
- `Model Accounting Revision` — `fldAt3A1bZW4QSGbF`

Persist exact deterministic JSON from `model_bet_accounting.py`.

At Step 1:
- WATCH -> supported line @1.65, 1u;
- non-WATCH -> NONE until a later BET/WAIT exists.

At Step 2, direct BET/WAIT may replace WATCH for that same model/fixture under the documented precedence.

These fields are model-performance accounting and do not grant Website Pick / real-exposure authority to C2/C3/C4.

## 8. Capacity queue / replenishment persistence

Dedicated Daily Coverage fields:
- `Step0 Capacity Queue Rank` — `fldUFbfIyiIYcQuVt`
- `Step1 Replenished` — `fldPUL87XJhpUqYiU`
- `Replenishment Wave` — `fld5qzOVZdKst3bhK`
- `Replenishment Reason` — `fldUxHPEnQpGSJVmC`

Every Step-0 A/B fixture must receive a unique positive queue rank across the sweep before initial admission.

Initial ranks 1–15 are admitted to the first Work wave. Rank 16+ rows remain `OPERATIONAL_CAPACITY_DEFERRED` until Step 1 either replenishes them or the prematch window closes.

When Step 1 pulls a deferred fixture:
- keep its original Step0 queue rank immutable;
- set `Step1 Replenished = true`;
- set `Replenishment Wave`;
- record the reason;
- do not rewrite original discovery/operational evidence.

A capacity-deferred row is therefore a queued eligible candidate, not a permanent negative model verdict.

## 9. Women's top-flight reconciliation

For every sweep, Daily Coverage plus Sweep Runs must support:

`women_top_flight_raw_count = admitted + operational_excluded + researchability_excluded + capacity_deferred + unresolved`

Every manifest fixture has a Daily Coverage disposition.

Missing block/row:

`HANDOFF INCOMPLETE — WOMEN TOP-FLIGHT COVERAGE GAP`

## 10. Coverage reconciliation

Before declaring board publication complete:

`RAW SENIOR = HARD EXCLUDED + OPERATIONAL EXCLUDED + RESEARCHABILITY EXCLUDED + CAPACITY DEFERRED + ADMITTED + UNRESOLVED`

Also verify:
- no duplicate canonical AiScore ID;
- every admitted fixture has one C board state;
- every exclusion/defer has a reason;
- every active fixture lies inside the corrected ICT window;
- no unresolved schedule identity is treated as active;
- women's-top-flight counts reconcile;
- C2/C3/C4 shadow data never replaced C.

If these fail:

`COVERAGE INCOMPLETE — BOARD PROVISIONAL`

## 11. Upcoming reads

Daily Coverage is frozen history, not sufficient by itself to prove a fixture is currently upcoming.

For `/report next matches`:
- convert time correctly;
- revalidate near-term status/time;
- remove LIVE/HT/FT/postponed/cancelled from upcoming;
- annotate material schedule corrections.

## 12. Historical fields

Legacy v0.2.x / Football A columns and old row content remain valid historical records.

For new Football C boards:
- do not populate old EGE/MCE/CC+/Football A execution fields as authority;
- do not use old PRE compiler rules;
- do not use old league overlays;
- do not reinterpret old historical rows.

Historical fidelity is preserved by Model Version and Git history, not by keeping obsolete authority active in this contract.

## 13. Cross-chat bridge

Current workflow:

`/sweep -> Football C /rank -> Daily Coverage -> /xi -> Decision States / Website Picks -> /live -> /audit`

Normal Chat reads the frozen Football C state; it does not reconstruct an old Football A PRE state.

## 14. Duplicate/conflict validator

Group by canonical AiScore ID.

If two active rows disagree on date, kickoff, orientation, C state, supported burden, eligibility or completeness:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

Do not resolve by last-write-wins.


## Required competition coverage manifest

Sweep Runs must persist the protected Step-0 block check defined by:
`models/football/procedures/FOOTBALL_REQUIRED_COMPETITION_COVERAGE.md`.

Fields:
- `Required Competition Manifest Version` — `fldYxv9Oljrkq4lZf`
- `Required Competition Blocks` — `fldvIsy67dwIvarf2`
- `Required Competition Blocks Complete` — `fldFcVeFIAikCWBj2`

Current version:
`required-competition-manifest-v1`

Current protected block:
- `NED_EERSTE_DIVISIE`

Set completion true only when every protected block is explicitly checked and resolved.

`SOURCE_BLOCKED`, a missing block, count/list mismatch, or missing fixture disposition means the sweep is not work-ready.

This metadata never promotes a fixture or changes C/C2/C3 predictive state.
