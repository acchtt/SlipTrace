# Football C4 Airtable Persistence Contract

**Status:** ACTIVE STEP-1 SHADOW PERSISTENCE  
**Base:** `SlipTrace Football Decision Control` (`appWyZJjitSBATXAU`)  
**Official model:** Football C  
**C4 role:** Step-1-only structured-evidence challenger

C4 fields are comparison metadata only. They must never overwrite C/C2/C3 fields, create Step-2 workload, create Website Picks, or authorize exposure.

## 1. Daily Coverage Ledger

Table: `tblcl1UAyMqZT6Ub0`

Dedicated C4 fields:

- `C4 Shadow State` — `fldLftJ8ven7qffll`
- `C4 Shadow Rank` — `fld0iq4a4VwvB8ItG`
- `C4 Supported Line` — `fldjy4ObqqXKtU9ud`
- `C4 Home Route` — `fldngpvvBR89LKkfB`
- `C4 Away Route` — `fldd4Ktun0iHe70Ba`
- `C4 Carrier` — `fldWAzZopp3eC08Iz`
- `C4 Goal3 Funding` — `fldTxWBQmC0306zuI`
- `C4 Goal4 Funding` — `fldxvpu1CQO6lYL5C`
- `C4 Control Risk` — `fldVGwb1uqHmlyGX3`
- `C4 Structured Evidence` — `fldmP7tAWb2oLXXvy`
- `C4 Compiler Result` — `fldzWguzzVpUkJE2D`
- `C4 Compiler Revision` — `fldKvXHBq2P4nlutL`

Freeze C4 structured evidence and compiler output before outcome knowledge.

`C4 Structured Evidence` should preserve the exact anchor payload or a compact lossless JSON representation.

`C4 Compiler Result` should preserve the exact deterministic C4 result for the fixture.

## 2. Sweep Runs

Table: `tblUnGHHe0MVaalDL`

Prospective-test fields:

- `C4 Test Board Number` — `fldBGuZhpboeMUGtz`
- `C4 Test Board Eligible` — `fld6qcujbINz3vwYK`
- `C4 Contamination Reason` — `fldkzj2yENYGNN18O`

Counter starts at 0/5 at the C4 activation merge.

Advance only when the full ranked eligible universe has complete prospective C4 structured evidence and the compiler reconciles successfully with the frozen C board.

## 3. Persistence order

For a clean Step-1 board:

1. freeze the common Football research epoch;
2. freeze C4 structured anchor payloads before C4 output;
3. complete normal C/C2/C3 board-triplet reconciliation;
4. run the C4 compiler against the frozen C board payload;
5. write C4 per-fixture fields to Daily Coverage;
6. write C4 board eligibility/number to Sweep Runs.

If C4 fails but C/C2/C3 are clean, preserve the normal official board. C4 becomes:

`C4-INCOMPLETE`

and the C4 counter does not advance.

## 4. Independence

Never:
- map Football C route/carrier grades directly into C4 output fields as a substitute for the structured anchors;
- copy C/C2/C3 supported line into C4;
- create a C4 Decision State row;
- create a C4 Website Pick;
- use C4 to authorize `/xi`, `/live`, or real exposure;
- backfill C4 fields after FT.

## 5. Audit

Post-slate audit may compare C4 with C for:
- state/rank inversions;
- supported-line disagreement;
- two-goal endpoints;
- C false-positive/false-negative candidates;
- carrier-led retention;
- deterministic replay reproducibility.

Outcome analysis may append audit conclusions elsewhere, but Step-1 C4 frozen fields remain immutable.
