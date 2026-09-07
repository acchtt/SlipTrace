# Football Airtable Decision-State Control

This document describes the Airtable decision-state control plane used by Football v1.0.

## Base

- **Base:** `SlipTrace Football Decision Control`
- **Base ID:** `appWyZJjitSBATXAU`

## Decision States table

- **Table:** `Decision States`
- **Table ID:** `tblQmUpd5WjBLQ38X`

Current core field IDs:

| Field | ID |
|---|---|
| Assessment ID | `fldw5PxzbUDRxPTN6` |
| Match | `fldOhDnn8HJx4cv5H` |
| Competition | `fldHMLKkm2qToiZ1O` |
| Model Version | `fldEozpHKiyLBvou9` |
| Assessment Time | `fld3FF6oSQjdYFOAy` |
| Minute | `fldGl8MD1MDJETVyZ` |
| Score | `fldTN65kHAyUj7TyW` |
| Assessment Period | `fldhnnmkvbUvEFH52` |
| Verdict | `fldKHk8vNQMYGx0GU` |
| Candidate | `fld9xNR6kkR8oYISu` |
| Line | `fldLrWtsOoe503UTv` |
| Odds | `fldvslKY49svSlXCx` |
| Evidence Summary | `fldTAwWTDJvfusgj7` |

The separate `Daily Coverage Ledger` is documented in `FOOTBALL_COVERAGE_AIRTABLE.md` and is authoritative for fixture-universe completeness. Decision States is authoritative for model-state history.

---

## Active model versions

New active rows use their actual track version:

- official track: `v0.2.47`
- shadow track: `v0.2.48-SHADOW`

Historical rows keep the version they were created with, including `v0.2.47-R`. Never rewrite historical model-version labels.

---

## Mandatory logging rule

Create a new Decision States record for every material state transition that is worth reconstructing later:

`PRE FREEZE → XI RERANK → FINAL LINE/PRICE → LIVE VALIDATION → FT SETTLEMENT / PROCESS REVIEW`

Do not overwrite earlier states to make them agree with later information.

Typical `Assessment Period` values:

- `PRE`
- `XI`
- `LIVE`
- `FT`
- `SIM-PRE` for counterfactual simulation

Use distinct Assessment IDs for distinct material states and distinct model tracks.

Recommended model suffix in Assessment ID:

- `-V247`
- `-V248S`

---

## Verdict semantics

Current Airtable Verdict choices include:

- `OFFICIAL BET`
- `SHADOW LEAN — DO NOT PLACE`
- `NO BET — HOLD`
- `NO BET`

### Official v0.2.47

User-facing affirmative selection:

`OFFICIAL LOCK — <line> @ <odds>`

Airtable Verdict:

`OFFICIAL BET`

This creates official exposure and must also be written to the official picks control according to the active workflow.

Official HOLD/PASS creates no exposure.

### v0.2.48-SHADOW

User-facing affirmative selection:

`SHADOW LOCK — <line> @ <odds> — DO NOT PLACE`

Airtable Verdict:

`SHADOW LEAN — DO NOT PLACE`

A shadow hold uses Airtable Verdict `NO BET — HOLD` with Model Version `v0.2.48-SHADOW`.

Shadow rows never enter official P/L unless the model is explicitly promoted in the future; historical shadow rows remain shadow even after promotion.

---

## Evidence synchronization

When both tracks evaluate the same match, they must use the same:

- PRE evidence timestamp;
- confirmed XI snapshot;
- score/minute if live;
- Asian-total market snapshot.

Differences between the two records should therefore reflect model logic, not different input states.

If the evidence state differs materially, do not compare the verdicts as a clean model-vs-model test.

---

## Evidence Summary

The Evidence Summary should be concise but sufficient to reconstruct why the state existed at that moment. Include material items such as:

- frozen structural band/type;
- FOCUS/WATCHLIST context when relevant;
- carrier and secondary route;
- mandatory GF/GA/profile findings;
- confirmed-XI changes;
- chance-quality findings;
- failure modes;
- selected Asian total / protection rationale;
- track-specific patch reason for v0.2.48 when it differs;
- live substitutions or material events;
- settlement/process lesson.

Do not use result knowledge to rewrite earlier evidence.

---

## Live records

For material live reassessments, record the current score and minute/phase plus evidence that validated or invalidated the frozen thesis.

Examples:

- early goal that changes intended burden-decay entry;
- HT chance-quality review;
- significant substitution cluster;
- red card;
- material line/price change tied to a new decision;
- later live validation/HOLD.

A live HOLD that later finishes Over remains a HOLD. Do not retroactively create a bet.

The clean v0.2.47 high-scoring-halftime compression fields may be used where relevant.

---

## Simulations

Counterfactual simulations must be identifiable in Assessment ID / Assessment Period / Candidate text.

They must not be counted in official P/L even if the simulated selection would have won.

Keep clean and shadow simulation rows separate.

---

## Settlement and audit

For standard full-match Asian totals, settlement uses 90 minutes plus stoppage time only unless the market explicitly includes extra time.

When auditing performance:

- collapse multiple PRE/XI/LIVE/FT state rows into the underlying unique official bet;
- do not double-count a bet because it has both lock and settlement records;
- exclude official `NO BET — HOLD` states from P/L;
- exclude all v0.2.48-SHADOW rows from official P/L;
- exclude counterfactual simulations from official P/L;
- preserve half-win, push, half-loss, win, and loss settlement semantics.

Shadow performance may be calculated separately for model comparison.

All audit dates/times are interpreted in `Asia/Ho_Chi_Minh` / ICT unless explicitly stated otherwise.

---

## Authority

Use:

- `Daily Coverage Ledger` for fixture coverage, screen status, and FOCUS/WATCHLIST survival;
- `Decision States` for PRE/XI/live model-state reconstruction;
- `Website Picks` for official lock accounting and settlement.

Search Airtable before reconstructing prior betting history from chat memory or archived repository documents.