# Football Daily Coverage Ledger — Airtable Contract

**Status:** ACTIVE  
**Base:** `SlipTrace Football Decision Control`  
**Table:** `Daily Coverage Ledger`  
**Table ID:** `tblcl1UAyMqZT6Ub0`  
**Official model:** Football v0.2.49

This table is the coverage-control and cross-chat bridge for the current football workflow. It records every fixture in the reconciled AiScore slate and preserves the **frozen Work PRE state** for later user-supplied XI/odds review.

---

## 1. Source contract

The fixture universe is AiScore-only.

Recommended source fields:

- `Source 1` = AiScore / AiScore verified handoff;
- `Source 2` = optional research/reference source only;
- `Reconciled = true` means the requested AiScore window itself was fully traversed, normalized, filtered, and accounted for.

Do not write that a multi-source fixture union was built. Other providers may support research but may not establish extra fixtures.

---

## 2. Coverage identity fields

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

Excluded fixtures remain in the ledger for audit. Do not silently omit them.

---

## 3. Current senior-quality eligibility

The actionable overlay excludes youth/Uxx, academy/junior, reserve/B-team/development, amateur/semi-pro, regional/state/provincial, very small/obscure weak-data competitions, and domestic lower divisions below top flight unless explicitly approved/whitelisted.

Senior first-team continental competitions are **not** generically excluded. UCL, UEL, and UECL are eligible when they otherwise clear the overlay.

A row excluded under the overlay should carry an explicit exclusion reason.

---

## 4. Frozen PRE fields

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

are shadow/comparison fields only. They do not define the official board tier and must not overwrite the official v0.2.49 frozen PRE state.

---

## 5. Publish = copy/upsert, not re-screen

The Work structural sweep is the model run that creates the frozen PRE board.

When publishing to Airtable:

1. upsert the same fixture row;
2. copy the Work PRE grade exactly;
3. copy the Work structural type exactly;
4. copy `FOCUS` / `WATCHLIST` / `PASS` / `UNRESOLVED` exactly into `Board Tier`;
5. preserve the Work thesis/failure-mode summary in `Frozen PRE Summary` / `Coverage Notes`;
6. set XI/market status to pending/user-supplied as appropriate;
7. do **not** run another structural screen during publication.

Forbidden example:

- Work board = `B+ / WATCHLIST`
- publisher independently writes = `B / PASS`

That is a persistence failure, not a legitimate rerank.

---

## 6. Persistence conflict rule

If the original frozen Work board and Airtable row disagree, classify:

`PERSISTENCE SYNC FAULT — frozen PRE preserved`

Until corrected:

- the original Work PRE artifact remains the thesis authority;
- do not let the conflicting Airtable row auto-PASS or auto-promote the match;
- correct the Airtable record so the bridge again represents the frozen Work state.

Later XI/price reranks should be logged as later assessment states, not by rewriting what PRE originally was.

---

## 7. Coverage reconciliation

Before claiming a board is fully frozen/published, verify:

`Universe = Actionable eligible + Excluded`

`Actionable eligible = Focus + Watchlist + Pass + Unresolved`

Also verify:

- every actionable fixture has one PRE state;
- no fixture is duplicated;
- all exclusions have reasons;
- all FOCUS/WATCHLIST candidates are persisted;
- no excluded youth/reserve/lower/small fixture survived;
- the underlying AiScore handoff has `audit.complete = true` and passed cross-midnight/date-page checks.

If publication or counts fail:

`COVERAGE INCOMPLETE — board provisional`

---

## 8. Cross-chat bridge

The intended current workflow is:

`AiScore handoff → Work structural sweep → Daily Coverage Ledger → Normal Chat user-supplied XI/odds review`

Normal Chat should read the persisted frozen state rather than reconstructing the board from conversational memory.

However, the bridge is only authoritative when it faithfully mirrors the Work artifact. A demonstrated persistence conflict triggers the sync-fault rule above.

---

## 9. Do not overload the coverage table

The Daily Coverage Ledger controls **coverage and frozen PRE**. Material final XI/market verdicts belong in `Decision States`, and official website LOCK records belong in the appropriate official picks/ledger path.

Do not turn the coverage row into a mutable history that erases earlier PRE state.
