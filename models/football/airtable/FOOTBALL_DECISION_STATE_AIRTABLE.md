# FOOTBALL AIRTABLE DECISION-STATE CONTROL

Effective with Football v0.2.40; strengthened by Football v0.2.41 and Football v0.2.47.

This document records the canonical operational Airtable control plane for football decision-state validation.

## Base

- Base name: `SlipTrace Football Decision Control`
- Base ID: `appWyZJjitSBATXAU`
- Purpose: enforce structured football decision-state logging and circuit-breaker/audit tracking.

This Airtable base is **not** the authoritative financial ledger. `/ledger.json` remains authoritative for official betting accounting when ledger writes are explicitly authorized.

## Table 1 — Decision States

- Table ID: `tblQmUpd5WjBLQ38X`
- Primary field: `Assessment ID` — `fldw5PxzbUDRxPTN6`

Important field IDs:

- Match — `fldOhDnn8HJx4cv5H`
- Competition — `fldHMLKkm2qToiZ1O`
- Model Version — `fldEozpHKiyLBvou9`
- Assessment Time — `fld3FF6oSQjdYFOAy`
- Minute — `fldGl8MD1MDJETVyZ`
- Score — `fldTN65kHAyUj7TyW`
- Reset Epoch — `fldbPsoX2ZxywShf0`
- Assessment Period — `fldhnnmkvbUvEFH52`
- Verdict — `fldKHk8vNQMYGx0GU`
- Candidate — `fld9xNR6kkR8oYISu`
- Line — `fldLrWtsOoe503UTv`
- Odds — `fldvslKY49svSlXCx`
- Goal Environment — `fldDyMTJlF5gPX1RO`
- Synchronized State — `fldXbAUPmgQkOZdaX`
- Reset Resolved — `fldJR1gsmr6g7zncK`
- Competition Format Verified — `fld2sc8z4Fh5gL7Op`
- Win Draw Margin Utility Verified — `fldXAYNAW0LS8sUF1`
- Margin Incentive Propagated — `fldU7zDQfsrNz7ynX`
- xG Role — `fldulLHGJxfWKrJj9`
- Primary Channels — `fld6Rcz1ryT2TsfMu`
- Independent Primary Channels — `fldGz8gbcyuPUqZWD`
- Favorite Fade Gate — `fldZhL6NWpiNCwQCS`
- Directional Persistence — `fldz2otbFIu7Dr8OE`
- Underdog Suppression Evidence Count — `fldFvGzM6hi1FNWFk`
- Favorite First-Goal Branch — `fld3Oq1Fb4FBYJD2R`
- Major Markets Scanned — `fldoWuPOW46IuEhlF`
- Circuit Breaker Mode — `fldnMIgdPKLcXc64W`
- Validator Result — `fldCuQ8rqNrmhgpld`
- Fail Reasons — `fldlkav9gyDQI7jKb`
- Evidence Summary — `fldTAwWTDJvfusgj7`

### v0.2.47 halftime-compression fields

- HT Goals — `fldwssNwjgGXOcmtE`
- HT Saturation Gate — `fldcdRGbFGhlRqzlY`
- Conversion Quality Gate — `fldv1u9Hd3eMwckYa`
- Second-Half Hazard — `fldrRCpTPn0tQjYCy`
- Remaining Goal Budget — `fldkiqxcL1YRjJNZ6`

Allowed `HT Saturation Gate` values:

- `Not Applicable`
- `Moderate`
- `Strong`

Allowed `Conversion Quality Gate` values:

- `Not Applicable`
- `Pass`
- `Unresolved`
- `Fail`

Allowed `Second-Half Hazard` values:

- `Not Applicable`
- `Re-accelerating`
- `Persistent but Unproven`
- `Compressing`
- `Unresolved`

### Operational rule

Create one record for every material prematch assessment and material live reassessment that could produce a side, total, derivative or shadow selection.

No `SHADOW LEAN — DO NOT PLACE`, `LEAN`, or `OFFICIAL BET` may be emitted unless its corresponding record has `Validator Result = PASS`.

If a material reset is unresolved, write the state with `Goal Environment = Unresolved`, `Reset Resolved = false`, and `Validator Result = HOLD`.

If xG/xGOT is creating the thesis rather than corroborating it, write `xG Role = Violation` and `Validator Result = FAIL`.

For a prematch protected-underdog candidate against a material/deep favourite under v0.2.41:

- `Underdog Suppression Evidence Count` must be at least 2;
- `Favorite First-Goal Branch` must be `Pass`;
- `Margin Incentive Propagated` must be checked whenever competition tiebreak/order or other incentives materially affect margin utility;
- failure of any applicable condition forces `Validator Result = FAIL`.

### v0.2.47 enforcement

For any serious post-halftime Over assessment after **3+ first-half goals**:

1. write the actual `HT Goals` count;
2. set `HT Saturation Gate = Moderate` for exactly 3 HT goals or `Strong` for 4+ HT goals;
3. evaluate only fresh second-half evidence for the new Over promotion; first-half activity is context only;
4. write `Conversion Quality Gate` based on a fresh second-half conversion-quality channel;
5. write `Second-Half Hazard` as `Re-accelerating`, `Persistent but Unproven`, `Compressing`, or `Unresolved`;
6. write the exact settlement burden in `Remaining Goal Budget`;
7. `Persistent but Unproven`, `Unresolved`, or `Conversion Quality Gate = Unresolved/Fail` cannot coexist with `Validator Result = PASS` for a post-HT Over;
8. if the candidate needs two or more additional goals for a full win, the Evidence Summary must explain the credible second-half multi-goal route.

For matches with 0-2 HT goals, use `HT Saturation Gate = Not Applicable` unless a later rule specifically requires otherwise.

Historical v0.2.46 decisions are not rewritten merely because v0.2.47 would classify them differently. New fields may be used in a separate process-audit record, but the original historical verdict/line/odds/model version must remain unchanged.

## Table 2 — Circuit Breaker

- Table ID: `tblcJfh8zbNyzjArK`
- Primary field: `Slot ID` — `fld8QjDiNTQgrE8iC`

Important field IDs:

- Slot Number — `fldk3s3hh2OzwKR1g`
- Match — `fldfDzaLuNDi9UoCx`
- Model Version — `fldXcmz2W2t42WWXj`
- Shadow Selection — `fldqEOUnlSGZLJti0`
- Odds — `fldPF85cFFuBmih2P`
- Stake u — `fldhNX2MtZR0DYl9e`
- Assessment State — `fldSGNw00ApLJfQbQ`
- Result — `fldiR1pc3UxnwEqwy`
- Simulated P/L u — `fld5HmlT5PGsBxH9Z`
- Process Validity — `flduZGz2TZLRO7zQy`
- Counted — `fldaWRKCIc4aPzWCh`
- Review Notes — `fld2FQz6SYfLR4PwB`
- Completed At — `fldXrWAM4P6wKQwmp`

### Circuit-breaker workflow

1. A match does not enter this table merely because it was analyzed.
2. It enters only when the hard validator returns `PASS` and a normal executable LEAN would otherwise exist.
3. During a circuit-breaker phase, record the candidate as `SHADOW LEAN — DO NOT PLACE` using the active model's stake convention.
4. Exactly one primary counted shadow selection may count per match unless an explicit later audit protocol says otherwise.
5. After verified settlement, update result, simulated P/L, process validity, review notes and completion time.
6. `NO BET` and `NO BET — HOLD` do not consume a slot.
7. Official betting remains paused until the active audit exit criteria are met and the user explicitly restores it.

## Current operating state

- Official football betting: paused.
- Execution: shadow calibration only.
- Ledger writes: unauthorized / on hold.
- Active model: Football v0.2.47 — AUDIT MODE.
