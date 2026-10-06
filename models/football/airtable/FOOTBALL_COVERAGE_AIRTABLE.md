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

## 4. Frozen Football C + C2 board fields

Preserve current official/shadow board state exactly.

Current new-board fields include:
- `C Board State`;
- `C Rank`;
- `C Supported Line`;
- `C2 Shadow State`;
- `C2 Shadow Rank`;
- `C2 Supported Line`;
- `C Model Accounting`;
- `C2 Shadow Accounting`;
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
- C supported burden and Supported Line Basis;
- C Board State Basis;
- C2 Supported Line Basis and C2 Board State Basis;
- Completion Mode;
- Burden Completion Quality;
- Continuation Quality;
- Opponent Leakage;
- Burden Stall Risk;
- Same Kickoff Rank;
- tournament-incentive freeze;
- H2H/failure summary;
- Screened At;
- Frozen PRE Summary / Coverage Notes;
- Board Pair Common-Evidence Reconciliation Status / engine revision.

Where the physical Airtable schema still uses legacy columns such as `PRE Grade`, `Board Tier`, or `Structural Type`, use them only as storage aliases for the **actual frozen Football C output**. They do not activate Football A PRE compiler semantics.

C2 shadow fields/notes must remain separate from C:
- C2 state/rank;
- C2 supported burden;
- C2 diagnostics.

Historical C3/C4 columns may remain in the physical Airtable schema and on old rows. They are historical-only compatibility fields:
- do not populate them for new boards;
- do not require them for current publication;
- do not let them overwrite C/C2;
- do not reactivate retired C3/C4 workflow.

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

## 6. C / C2 policy separation

The underlying football research epoch is shared, but model policy is separate.

Persist C and C2 supported burdens independently.

A C2 row without an independently frozen C2 burden is incomplete for C-vs-C2 paired evaluation.

Do not populate C2 supported burden from Football C completion labels or C supported line.

Historical C3/C4 rows remain immutable. Their old fields may stay populated on historical records but are excluded from new/current board completeness.

## 7. Active-model accounting persistence

Dedicated Daily Coverage fields:
- `C Model Accounting` — `fldND2leUXgAq9UQl`
- `C2 Shadow Accounting` — `fldlWroOrJdYF3lHn`
- `Model Accounting Revision` — `fldAt3A1bZW4QSGbF`

Historical compatibility fields retained in Airtable:
- `C3 Shadow Accounting` — `fldEMKp5LzS5IZQpJ`
- `C4 Shadow Accounting` — `fldNvPrq9WTW9118X`

For **new/current** rows, persist exact deterministic C+C2 JSON from `model_bet_accounting.py`.

At Step 1:
- WATCH -> supported line @1.65, 1u;
- non-WATCH -> NONE until a later BET/WAIT exists.

At Step 2, direct BET/WAIT may replace WATCH for that same active model/fixture under the documented precedence.

C2 accounting is shadow-only and does not grant Website Pick / real-exposure authority.

Historical C3/C4 accounting fields may only be read/settled under explicit historical-roster audit mode.

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
- C2 shadow data never replaced C; historical retired-model fields never re-enter current authority.

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

This metadata never promotes a fixture or changes C/C2 predictive state.

## Sweep Runs checkpoint / resume runtime

Fresh Step-0 timeout control is defined by:
`models/football/procedures/FOOTBALL_SWEEP_CHECKPOINT_EXECUTION.md`.

Table:
`Sweep Runs` — `tblUnGHHe0MVaalDL`

Existing runtime fields:
- `Run Status` — `fldm0iEQqUrfsTqKS`
- `Current Stage` — `fldUT0GEsWas15Ljt`
- `Checkpoint Notes` — `fldjaQNJnFYbaPFqd`
- `Resume Cursor` — `fldNjU7wHklM7T0Bf`
- `Retry Queue` — `fldQyCygdjxIfSk5B`
- `Updated At` — `fldTXdSN9d161pHgM`

Bounded-execution fields:
- `Checkpoint Version` — `fldtIbv2ppGzwUExs`
- `Sweep Chunk Number` — `flduqxh9DOKdV1A06`
- `Pending Verification Blocks` — `flduhyM3Thjwj3Bqs`
- `Last Completed Block` — `fld8jr7wAWGLhXqXe`
- `Source Blocker Fingerprint` — `fldFIDTXJNTmazT2Y`
- `Source Last Attempt At` — `fldqs9yD3uZjEC1Yr`
- `Source Retry Not Before` — `fldWkU52dpn2MSb4b`
- `Source Recovery Attempt Count` — `fldpJ92WA877WjYNj`

For a resumable fresh sweep, `Resume Cursor` is the authoritative next stage/block. Normal checkpoints are RUNNING. A BLOCKED row is resumable only when its cursor is `SOURCE_ACQUISITION / SOURCE_BLOCKED` and the source-recovery lease authorizes a new bounded attempt. Do not infer progress from chat history.

Status fields are intentionally different enums:
- `Run Status`: `RUNNING / BLOCKED / COMPLETE` (and any other existing run-level options);
- `Source Acquisition State`: `UNTRIED / ACQUIRED / SOURCE_BLOCKED`.

Required mapping during source acquisition:
- `UNTRIED -> Run Status RUNNING`;
- `ACQUIRED -> Run Status RUNNING`;
- `SOURCE_BLOCKED -> Run Status BLOCKED`.

**Never write `SOURCE_BLOCKED` into `Run Status`.** That value belongs only to `Source Acquisition State` and the structured Resume Cursor.

A chunk boundary is not a coverage failure:
- keep `Run Status = RUNNING`;
- persist the next cursor;
- do not set `work_ready=true`;
- do not emit the canonical ZIP until final reconciliation/packaging passes.

When the source epoch is already `ACQUIRED`, a resume must reuse its source hash/window rather than reacquire the date universe.

When the source epoch is `SOURCE_BLOCKED`, an unchanged blocker fingerprint suppresses only immediate repeat loops. Persist the 30-minute recovery lease; after expiry, or immediately when the fingerprint changes, one new bounded source acquisition pass is allowed. Legacy blocked rows without lease metadata receive one immediate recovery probe.
