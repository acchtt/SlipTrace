# Football Daily Coverage Ledger — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Daily Coverage Ledger`  
**Table ID:** `tblcl1UAyMqZT6Ub0`  
**Official model:** Football C

This table is the coverage-control and cross-chat bridge for the current football workflow. It records every fixture in the reconciled AiScore slate and preserves the **frozen Work PRE state** for later user-supplied XI/odds review.

---

## 1. Source contract

The fixture universe is AiScore-only.

Recommended source fields:

- `Source 1` = AiScore / AiScore verified handoff;
- `Source 2` = optional research/reference source only;
- `Reconciled = true` means the requested AiScore window itself was fully traversed, normalized, time/date checked, filtered, and accounted for.

Do not write that a multi-source fixture union was built. Other providers may support research but may not establish extra fixtures.

---

## 2. Coverage identity and datetime fields

Use the existing fields to preserve:

- `Coverage ID` — stable unique fixture/slate key;
- `Slate Date`;
- `Match`;
- `Competition`;
- `Kickoff ICT`;
- `Eligibility`;
- `Exclusion Reason`;
- `Reconciled`;
- `Source 1` / `Source 2`;
- `Coverage Status`.

Use `AISCORE:<fixture_id>` as the preferred `Coverage ID` whenever AiScore supplies an ID. Preserve that identity in notes/ID material so the row can be revalidated later. Only when the ID is unavailable may the fallback key use competition + normalized teams + kickoff_utc.

### Airtable timestamp semantics

Airtable/API may return a datetime with a trailing `Z` even when the field is configured to display in `Asia/Ho_Chi_Minh`.

Therefore:

- trailing `Z` always means UTC;
- never display a raw `Z` value as ICT;
- convert UTC to `Asia/Ho_Chi_Minh` exactly once for human-facing schedules;
- derive `Slate Date` from the ICT-converted kickoff, not from the raw UTC date;
- never add +7 to a value already explicitly expressed as ICT.

The field name `Kickoff ICT` describes intended display meaning; it does not change UTC serialization semantics.

Excluded and schedule-integrity-unresolved fixtures remain in the ledger for audit. Do not silently omit them.

---

## 3. Current senior-quality eligibility

Current Football C eligibility is controlled by `CURRENT_MODEL.md`, `00_NORMAL_CHAT_AISCORE_FETCH.md`, the operational-viability gate and the researchability gate.

Hard scope excludes youth/Uxx, academy/junior, reserve/B-team/development, amateur/semi-professional micro, regional/state/provincial and other non-target senior-professional classes as defined by the active Step-0 contract.

**Senior women's domestic top-flight leagues are first-class senior top-flight blocks.** Every visible AiScore fixture in that class must be represented in Daily Coverage, including when its final Step-0 disposition is operational exclusion, researchability exclusion or capacity deferral.

Set `Senior Women's Top Flight = true` on those rows.

Do not apply historical country/league blanket exclusions from archived Football A/v0.2.x overlays to current Football C unless the current Step-0 authority explicitly reinstates them. Gender, audience size or unfamiliarity alone is never an exclusion reason.

Senior first-team continental competitions remain eligible when they otherwise clear current rules.

Every excluded row must carry the exact current exclusion/disposition reason.

---

## 4. Schedule-integrity state

Before a row is treated as a valid current-board fixture, its normalized kickoff must pass `FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`.

If date/time/identity is contradictory, preserve the row for audit but classify it operationally as:

`UNRESOLVED — SCHEDULE INTEGRITY`

A fixture outside the requested corrected ICT window must not receive an active FOCUS/WATCHLIST board role for that slate.

For discovered historical faults, preserve PRE history and append a clear correction label in `Coverage Notes`, such as:

- `TIMEZONE NORMALIZATION FAULT`;
- `SCHEDULE DATE MISMATCH`;
- `STALE UPCOMING STATE`;
- `KICKOFF CHANGE`;
- `FIXTURE IDENTITY / HOME-AWAY MISMATCH`.

Do not silently rewrite history.

---

## 5. Frozen PRE fields

The current official shared coverage state is represented by:

- `Operational Grade`;
- `XI Expected`;
- `Team News Observability`;
- `Competition Reliability State`;
- `Competition Reliability Reason`;
- `Operational Disposition`;
- `Senior Women's Top Flight`;
- `Completion Mode`;
- `Burden Completion Quality`;
- `Continuation Quality`;
- `Opponent Leakage`;
- `Burden Stall Risk`;
- `Same Kickoff Rank`;

- `PRE Grade`;
- `Structural Type`;
- `Board Tier`;
- `Screened At`;
- `XI Status`;
- `Market Status`;
- `Frozen PRE Summary`;
- `Coverage Notes`.

`PRE Grade` and `Board Tier` must reflect the **actual Work structural output**.

The existing comparison fields:

- `v0.2.47 PRE`;
- `v0.2.48 PRE`;

are shadow/comparison fields only. They do not define the official board tier and must not overwrite the official frozen PRE state.

Post-XI v0.2.50 EGE, v0.2.51 MCE, and v0.2.52 carrier-reopen/execution states do not rewrite these frozen PRE fields.

For new Football A decisions, the current Step-2 state is compiled by `FOOTBALL_STEP2_EXECUTION_SPEC.md`. Daily Coverage Ledger remains frozen PRE history only. Current XI mechanism, H2H state, frozen-PRE market alignment, current-PRE execution fit, EGE/carrier/current PRE, upper-tail, execution class and final exposure belong in Decision States / Website Picks, not by mutating frozen PRE.

For every new Step-1 board produced under the compiled PRE authority, `Frozen PRE Summary` / `Coverage Notes` must also preserve a compact `FOOTBALL_PRE_DECISION_SPEC_V1` trace sufficient to reconstruct:

- HOME/AWAY CQ/REP/MECH/CTX states and final route states;
- weaker-route INDEPENDENT/CONDITIONAL state when applicable;
- HOME/AWAY VERIFIED/CANDIDATE/UNVERIFIED carrier states;
- dominant failure mode + severity;
- PASS-rescue result when applicable;
- structural grade + board tier + cap reason;
- supported burden + burden basis/confidence;
- evidence confidence;
- rank-factor summary and cross-grade inversion reason when applicable.

This is frozen PRE history. Later XI/market states may reference it but must not overwrite it.

Under v0.2.52, preserve route-quality and carrier-ceiling context in `Frozen PRE Summary` / `Coverage Notes` where relevant, including:

- `TWO-SIDED — QUALITY PROVEN`;
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`;
- `CC+ — CARRIER CEILING`;
- `CC+ CANDIDATE — XI SENSITIVE`.

---

## 6. Publish = copy/upsert, not re-screen

The Work structural sweep is the model run that creates the frozen PRE board.

When publishing to Airtable:

1. upsert the same fixture row;
2. copy the frozen Step-0 operational grade/disposition and competition-reliability snapshot exactly;
3. copy the frozen completion mode/quality, continuation quality, opponent leakage, stall risk and same-kickoff rank exactly;
4. copy the Work PRE grade exactly;
5. copy the Work structural type exactly;
6. copy `FOCUS` / `WATCHLIST` / `PASS` / `UNRESOLVED` exactly into `Board Tier` where supported;
7. preserve the Work thesis/failure-mode plus route-quality / CC+ summary in `Frozen PRE Summary` / `Coverage Notes`;
8. set XI/market status to pending/user-supplied as appropriate;
9. preserve canonical kickoff semantics;
10. do **not** run another structural screen during publication.

Forbidden examples:

- Work board = `B+ / WATCHLIST`, publisher independently writes = `B / PASS`;
- raw UTC `10:30Z` is displayed as `10:30 ICT` instead of converted to `17:30 ICT`;
- a Sep 15/16 fixture is copied into a Sep 9 slate because the wrong date representation was trusted.

Those are persistence/schedule failures, not legitimate reranks.

---

## 7. Persistence conflict rule

If the original frozen Work board and Airtable row disagree, classify:

`PERSISTENCE SYNC FAULT — frozen PRE preserved`

Until corrected:

- the original Work PRE artifact remains the thesis authority;
- do not let the conflicting Airtable row auto-PASS or auto-promote the match;
- correct the Airtable record so the bridge again represents the frozen Work state.

Later XI/price/EGE/MCE/carrier-reopen reranks should be logged as later assessment states, not by rewriting what PRE originally was.

---

## 8. Upcoming-schedule reads

The Daily Coverage Ledger is a frozen-board bridge, not sufficient by itself to declare a match upcoming.

When reading it for `next matches` / `upcoming`:

- convert serialized UTC to ICT exactly once;
- resolve current ICT time;
- revalidate near-term AiScore status/time;
- remove LIVE/HT/FT/postponed/cancelled rows from the upcoming display;
- correct stale kickoff data operationally and annotate the correction;
- sort by corrected ICT kickoff.

Do not present an already-live fixture as upcoming simply because its stored timestamp is stale or misconverted.

---

## 9. Coverage reconciliation

Before claiming a board is fully frozen/published, verify:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

Also verify:

- every visible senior women's domestic top-flight fixture has a Daily Coverage row and one explicit Step-0 disposition;
- women's-top-flight raw count reconciles to admitted + operational excluded + researchability excluded + capacity deferred + unresolved;
- every actionable fixture has one PRE state;
- no fixture is duplicated;
- all exclusions have reasons;
- all FOCUS/WATCHLIST candidates are persisted;
- no excluded youth/reserve/lower/small fixture survived;
- the underlying AiScore handoff has `audit.complete = true` and passed cross-midnight/date-page checks;
- every active board fixture passed normalized ICT window/date integrity;
- every strong-carrier B/PASS has a documented CC+ audit result under v0.2.52.

If publication or counts fail:

`COVERAGE INCOMPLETE — board provisional`

---

## 10. Cross-chat bridge

The intended current workflow is:

`AiScore handoff → Work structural sweep through FOOTBALL_PRE_DECISION_SPEC_V1 → Daily Coverage Ledger → Normal Chat XI/odds review through FOOTBALL_STEP2_EXECUTION_SPEC.md → Decision States / Website Picks`

Normal Chat should read the persisted frozen state rather than reconstructing the board from conversational memory.

However, the bridge is only authoritative when it faithfully mirrors the Work artifact **and** its kickoff has passed time/schedule integrity. A demonstrated persistence or schedule conflict triggers the corresponding fault rule above.

---

## 11. Do not overload the coverage table

The Daily Coverage Ledger controls **coverage and frozen PRE**. Material final XI/market/EGE/MCE/carrier-reopen verdicts belong in `Decision States`, and official website LOCK records belong in the appropriate official picks/ledger path.

Do not turn the coverage row into a mutable history that erases earlier PRE state. Competition-level rolling history belongs in `Competition Reliability` / `Competition Reliability Events`; Daily Coverage keeps only the fixture's frozen Step-0 snapshot.

---

## 12. v0.2.53 coverage integrity fields

For prospective v0.2.53 rows, preserve in existing structured fields or `Frozen PRE Summary` / `Coverage Notes`:

- home route state: PROVEN / SUPPORTED / NOMINAL / FAILED;
- away route state: PROVEN / SUPPORTED / NOMINAL / FAILED;
- combined route pair;
- evidence confidence;
- league regime;
- league high-burden gate result where applicable;
- CC+ state and named dominant failure mode.

The publisher must verify that the assigned PRE grade and board tier match the final `FOOTBALL_PRE_DECISION_SPEC.md` compiler trace. Older v0.2.53 caps remain historical inputs to that compiler but are not a separate competing publication authority.

### Duplicate/conflict validator

Before upsert and before any board read:

1. group by canonical AiScore ID;
2. use the fallback key only for rows genuinely missing an AiScore ID;
3. collapse exact duplicates;
4. detect conflicting slate date, kickoff, match orientation, grade, tier, eligibility, or completeness;
5. block active publication until each conflict is resolved.

Required fault label:

`COVERAGE IDENTITY CONFLICT — PUBLICATION BLOCKED`

Do not resolve a conflict through last-write-wins or allow one fixture to occupy two slate dates. Preserve the conflict for audit, correct the canonical record, then publish.

### Historical league overlay note

Historical v0.2.x country/league blanket overlays remain historical audit context only. They are not current Football C eligibility authority. Current Step-0 scope and operational/researchability rules control new boards.

For current Football C, do not silently exclude a senior women's top-flight block because an older overlay targeted a country or domestic-league class.


---

## 13. v0.2.54 structural-rank bridge

For every prospective FOCUS/WATCHLIST row, preserve in existing fields or `Frozen PRE Summary` / `Coverage Notes`:

- same-window Structural Rank position;
- route pair and chance-quality state;
- supported structural burden/range;
- CC+ and dominant-failure-mode state;
- evidence confidence.

Work does not assign final execution class because it is price-blind. Step 2 derives DIRECT LOCK ELIGIBLE / QUALIFIED — WAIT FOR DECAY / STRUCTURAL HOLD / SHADOW ONLY without overwriting frozen PRE rank.

A later price/burden wait must not rewrite FOCUS/WATCHLIST as structural PASS. Final scores and target-burden outcomes for qualified non-exposures belong in Decision States/audit calibration, not official P/L.
