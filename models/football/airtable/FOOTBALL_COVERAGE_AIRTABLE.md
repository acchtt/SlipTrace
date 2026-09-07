# Football Airtable Coverage Control

This document describes the Airtable coverage ledger used by the mandatory Football Coverage Controller.

## Base

- **Base:** `SlipTrace Football Decision Control`
- **Base ID:** `appWyZJjitSBATXAU`

## Daily Coverage Ledger

- **Table:** `Daily Coverage Ledger`
- **Table ID:** `tblcl1UAyMqZT6Ub0`

Core field IDs:

| Field | ID |
|---|---|
| Coverage ID | `fldXPwmYy9MXdZzMm` |
| Slate Date | `fldWiBYqXqsOPIT7Z` |
| Match | `fldQgNmyL30PjV83l` |
| Competition | `fldsgiEy2wA5v1iSB` |
| Kickoff ICT | `fld5X9cTKlEqsorP6` |
| Eligibility | `fldvLheXcmehTQNap` |
| Exclusion Reason | `fldaieUwMkGkuRcVi` |
| Reconciled | `fldFTB5f8pkH762sO` |
| Source 1 | `fldG1yTQLDUlIAOEI` |
| Source 2 | `fldEXkJX1PGkhE4mN` |
| Coverage Status | `fldzK4HbbxfhrnRU1` |
| PRE Grade | `fldWooE7qqMOuXlzP` |
| Structural Type | `fldoabC0JKrzui3TT` |
| Board Tier | `fldp3HdEMHlciCwn9` |
| v0.2.47 PRE | `fld7jfDpoyIU4n8by` |
| v0.2.48 PRE | `fldJJIWyto07rAIpF` |
| Screened At | `fldQDNVrbhBuuIM3K` |
| XI Status | `fld8KQYfTURcgXqoA` |
| Market Status | `fldhiTCVU31YXFBDG` |
| Frozen PRE Summary | `fld7QcWC1ChRALr9A` |
| Coverage Notes | `fldFyiiJry4of6kJV` |

---

## Record identity / upsert

Use one record per fixture per slate date.

Recommended primary key:

`YYYYMMDD-COMPETITION-HOME-AWAY`

When the same fixture is found again through another source or later workflow step, update/upsert the existing row rather than creating a duplicate.

---

## Coverage status semantics

- `PENDING SCREEN` — fixture is in the reconciled universe but has not yet received PRE disposition.
- `SCREENED` — eligible fixture was assessed before/around kickoff.
- `LATE-DISCOVERED BUT SCREENED` — omitted from the initial universe/board but found and screened before kickoff.
- `TRUE MISSED SCREEN` — eligible fixture was not properly assessed before kickoff.
- `EXCLUDED` — fixture was found and explicitly removed by competition scope/hard exclusion.

Excluded rows remain in the ledger so exclusion cannot be confused with omission.

---

## Board tier semantics

- `FOCUS` — primary candidate for XI/market follow-up.
- `WATCHLIST` — still alive and must not be forgotten; may promote after XI/market or when a higher-ranked fixture downgrades.
- `PASS` — structurally rejected for normal follow-up.
- `UNRESOLVED` — data incomplete or reconciliation problem remains.

---

## Dual-model fields

The coverage controller routes the same evidence state to two tracks:

- `v0.2.47 PRE` — official CLEAN track disposition;
- `v0.2.48 PRE` — shadow candidate disposition.

Allowed values are `ADVANCE`, `HOLD`, `PASS`, or `DATA INCOMPLETE`.

The shared `PRE Grade` records the official clean-track structural band for the coverage/ranking workflow. Track-specific full XI/market verdicts belong in `Decision States`, not in this coverage table.

---

## Mandatory write order

For a new daily slate:

1. write/upsert every discovered fixture as soon as the union of fixture sources is built;
2. mark eligibility/exclusion;
3. screen every eligible fixture;
4. update PRE Grade, Structural Type, Board Tier, both model PRE dispositions, Screened At, and Frozen PRE Summary;
5. update XI Status and Market Status when those stages occur;
6. never delete a row because it becomes PASS or excluded.

This table is a coverage ledger, not a picks table.

---

## Coverage reconciliation query

Before claiming a slate is fully screened, counts from this table must satisfy:

`Universe = Eligible + Excluded`

and

`Eligible = Focus + Watchlist + Pass + Unresolved`

with no eligible `PENDING SCREEN` row left unexplained.

---

## Authority

For questions such as `what's next?`, `did we screen this?`, or `what did we miss?`, the Daily Coverage Ledger is the authoritative coverage record for the requested slate. Use the `Decision States` and `Website Picks` tables for model decisions and official P/L; use this table for fixture-universe completeness and ranking survival.