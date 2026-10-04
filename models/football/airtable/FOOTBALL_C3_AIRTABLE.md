# Football C3 — Airtable Persistence Contract

**Status:** ACTIVE SHADOW PERSISTENCE  
**Base:** `SlipTrace Football Decision Control` (`appWyZJjitSBATXAU`)  
**Official model:** Football C  
**C3 role:** shadow-only burden-funding challenger

C3 fields are comparison metadata only. They must never overwrite Football C or C2 fields and must never create Website Picks.

## 1. Daily Coverage Ledger

Table: `tblcl1UAyMqZT6Ub0`

Dedicated C3 fields:

- `C3 Shadow State` — `fld7pFOSvMsR282rO`
- `C3 Shadow Rank` — `fldK0sE49LvOywO5W`
- `C3 Lane` — `fldHHhXQS74KKEo7I`
- `C3 Supported Line` — `fldNqu0N9eNidTi1C`
- `C3 Second Route Role` — `fldOdZa31wzGcgd9I`
- C3 second-route-role basis — persist in the frozen evidence summary/machine result until a dedicated physical field exists
- `C3 Goal3 Funding` — `fld5o4GIJh88oaw1F`
- `C3 Goal3 Source` — `fld39FLZA4DlTJoxN`
- `C3 Goal3 Basis` — `fld2BwlIyLhlt0wOT`
- `C3 Goal4 Funding State` — `fld5v08kIf9JnhFwL`
- `C3 Goal4 Source` — `fld9tgsrn0DkfOsON`
- `C3 Goal4 Basis` — `fldskRCEGrjAIeuuK`
- `C3 Control Endpoint Risk` — `fldLoLuQH4JEJeHZ6`
- `C3 Control Endpoint Basis` — `fldmakZJi1l7hk14c`
- `C3 Forced Chaos Verified` — `fldkPfgqfrdlKU242`
- C3 forced-chaos basis — persist in the frozen evidence summary/machine result until a dedicated physical field exists
- C3 supported-line basis — persist in the frozen evidence summary/machine result

These fields are frozen at Step 1 before outcome.

Do not write C/C2 values into C3 fields merely because they are similar.

## 2. Decision States

Table: `tblQmUpd5WjBLQ38X`

Dedicated C3 fields:

- `C3 Supported Line` — `fld6avj0tjVcUSZto`
- `C3 Shadow Action` — `fldj1LxIXjVdQQKwL`
- `Current C3 Second Route Role` — `flds0jObsU5QMV4cr`
- Current C3 second-route-role basis — preserve in the Decision State evidence summary / engine result
- `Current C3 Goal3 Funding` — `fldPydLyYTxIh6Yzy`
- `Current C3 Goal3 Source` — `fldSoq3kVRRLHZFsQ`
- `Current C3 Goal3 Basis` — `fldSnl5YyTSBHaK03`
- `Current C3 Goal4 Funding` — `fldfI4SMcRwiZXUpl`
- `Current C3 Goal4 Source` — `fld6GPmAEgYLfZpWc`
- `Current C3 Goal4 Basis` — `fldSEheGWjQoixb0j`
- `Current C3 Control Risk` — `fldJaAFs5pVVq7Oby`
- `Current C3 Control Basis` — `fldjrHHWDhr1hZsSK`
- `Current C3 Forced Chaos Verified` — `fldBKxpdTUGhiIZqU`
- Current C3 forced-chaos basis — preserve in the Decision State evidence summary / engine result

C3 action values:
- `C3-BET — SHADOW`
- `C3-WAIT — SHADOW`
- `C3-PASS — SHADOW`
- `C3-INCOMPLETE`

C3 Decision State data never creates official exposure.

## 3. Sweep Runs

Table: `tblUnGHHe0MVaalDL`

C3 prospective-test fields:

- `C3 Test Board Number` — `fldT9Vs9tQDOlKnbw`
- `C3 Test Board Eligible` — `fld4Y36wOrh9xUUQN`
- `C3 Contamination Reason` — `fldpWdk9rSqq1AJOR`

The first clean **ranked-universe** board frozen after the C3 activation merge is Board 1/5.

Counter eligibility is based on the fixtures that legitimately enter ranking. A prospectively quarantined HOLD/exclusion with no C/C2/C3 output does not by itself contaminate the board.

A contaminated board:
- remains auditable;
- does not advance the counter;
- carries a precise contamination reason.

A missing required competition block or silently omitted eligible fixture is contamination because the ranked universe is incomplete.

## 4. Independence rules

C3 supported line and policy fields must be derived independently.

Never:
- copy C/C2 supported line into C3;
- copy C completion mode/continuation/stall labels into C3 funding fields;
- use C2 rank/state to create C3 rank/state;
- backfill C3 fields after FT;
- publish C3 as a Website Pick.

If the C3 policy block is incomplete:

`C3 COMPARISON INCOMPLETE — BURDEN-FUNDING STATE NOT INDEPENDENTLY FROZEN`

## 5. Current-field semantics

Step 1 fields are immutable historical freeze-time values.

Step 2 `Current C3 ...` fields belong to the current XI/research evidence epoch and may differ prospectively because XI/news changed. They do not overwrite Step-1 C3 fields.

## 6. Audit

Audit C3 separately from C2.

Report:
- C3 Board N/5;
- C vs C3 selection/lane differences;
- C3 two-goal endpoint rate;
- EXCHANGE_ONLY / STATE_DEPENDENT demotions;
- carrier-led cases C3 preserved;
- C3 false negatives.

C3 has no official model P/L.
