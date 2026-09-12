# Football Daily Coverage Ledger — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Daily Coverage Ledger`  
**Table ID:** `tblcl1UAyMqZT6Ub0`  
**Official model:** Football v0.2.52

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

The actionable overlay excludes youth/Uxx, academy/junior, reserve/B-team/development, amateur/semi-pro, regional/state/provincial, very small/obscure weak-data competitions, and domestic lower divisions below top flight unless explicitly approved/whitelisted.

All Finnish domestic league competitions at every tier/category are excluded from 2026-09-09 ICT onward. Finnish Cup and UEFA fixtures involving Finnish clubs are not automatically excluded.

Senior first-team continental competitions are **not** generically excluded. UCL, UEL, and UECL are eligible when they otherwise clear the overlay.

A row excluded under the overlay should carry an explicit exclusion reason.

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
2. copy the Work PRE grade exactly;
3. copy the Work structural type exactly;
4. copy `FOCUS` / `WATCHLIST` / `PASS` / `UNRESOLVED` exactly into `Board Tier` where supported;
5. preserve the Work thesis/failure-mode plus route-quality / CC+ summary in `Frozen PRE Summary` / `Coverage Notes`;
6. set XI/market status to pending/user-supplied as appropriate;
7. preserve canonical kickoff semantics;
8. do **not** run another structural screen during publication.

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

- every actionable fixture has one PRE state;
- no fixture is duplicated;
- all exclusions have reasons;
- all FOCUS/WATCHLIST candidates are persisted;
- no excluded youth/reserve/lower/small fixture survived;
- no Finnish domestic league fixture survived the overlay from its effective date;
- the underlying AiScore handoff has `audit.complete = true` and passed cross-midnight/date-page checks;
- every active board fixture passed normalized ICT window/date integrity;
- every strong-carrier B/PASS has a documented CC+ audit result under v0.2.52.

If publication or counts fail:

`COVERAGE INCOMPLETE — board provisional`

---

## 10. Cross-chat bridge

The intended current workflow is:

`AiScore handoff → Work structural sweep + route-quality/CC+ audit → Daily Coverage Ledger → Normal Chat user-supplied XI/odds review → v0.2.52 STANDARD/EGE/MCE/carrier-reopen assessment`

Normal Chat should read the persisted frozen state rather than reconstructing the board from conversational memory.

However, the bridge is only authoritative when it faithfully mirrors the Work artifact **and** its kickoff has passed time/schedule integrity. A demonstrated persistence or schedule conflict triggers the corresponding fault rule above.

---

## 11. Do not overload the coverage table

The Daily Coverage Ledger controls **coverage and frozen PRE**. Material final XI/market/EGE/MCE/carrier-reopen verdicts belong in `Decision States`, and official website LOCK records belong in the appropriate official picks/ledger path.

Do not turn the coverage row into a mutable history that erases earlier PRE state.

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

The publisher must verify that the assigned PRE grade and board tier do not exceed the route-pair cap in `MODEL_RULES_FOOTBALL_V0.2.53.md`.

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

### League overlay

Japanese domestic leagues, including J1, must not survive the active board from 2026-09-12 ICT onward. China Super League O3.0+/MCE candidates must preserve the v0.2.53 home/away-or-CC+ high-burden gate result.
