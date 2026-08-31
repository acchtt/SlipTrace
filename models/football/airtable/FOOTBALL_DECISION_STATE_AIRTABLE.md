# Football Airtable Decision-State Control — v0.2.47-R

This document describes the Airtable control plane currently used by Football v1.0.

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

Legacy fields may still exist in the Airtable base. They are not required by the active v0.2.47-R workflow unless explicitly reintroduced later.

---

## Mandatory logging rule

Create a new Decision States record for every material state transition:

`PREMATH FREEZE → XI RERANK → OFFICIAL LINE/PRICE → LIVE VALIDATION → FT SETTLEMENT / PROCESS REVIEW`

Do not overwrite earlier states to make them agree with later information.

Typical `Assessment Period` values:

- `PRE`
- `XI`
- `LIVE`
- `FT`
- `SIM-PRE` for a counterfactual simulation

Use distinct Assessment IDs for distinct material states.

---

## Verdict semantics

Active verdict values:

- `OFFICIAL BET`
- `NO BET — HOLD`

An affirmative final betting selection from the model is automatically an official lock and must be written as `OFFICIAL BET` with the exact line and odds.

A conditional future threshold is not an official bet until the current market actually meets it and the state is reassessed.

`NO BET — HOLD` creates no official exposure.

---

## Model version

All new active records should use:

`v0.2.47-R`

Historical records retain their original model versions. Never rewrite them to the current version.

---

## Evidence Summary

The Evidence Summary should be concise but sufficient to reconstruct why the state existed at that moment. Include the material items applicable to the decision, such as:

- frozen structural band/type;
- carrier route;
- mandatory GF/GA/profile findings;
- confirmed-XI changes;
- chance-quality findings;
- failure modes;
- selected Asian total / protection rationale;
- live substitutions or material events;
- settlement/process lesson.

Do not use result knowledge to rewrite earlier evidence.

---

## Live records

For material live reassessments, record the current score and minute/phase plus the evidence that validated or invalidated the frozen thesis.

Examples of material live states:

- early goal that changes the intended burden-decay entry;
- HT chance-quality review;
- significant substitution cluster;
- red card;
- material line/price change tied to a new decision;
- later live validation/HOLD.

A live HOLD that later finishes Over remains a HOLD. Do not retroactively create an official bet.

---

## Simulations

Counterfactual simulations must be identifiable in Assessment ID / Match / Assessment Period / Candidate text.

They must not be counted in official P/L even if the simulated selection would have won.

---

## Settlement and audit

For standard full-match Asian totals, settlement uses 90 minutes plus stoppage time only unless the market explicitly includes extra time.

When auditing performance:

- collapse multiple PRE/XI/LIVE/FT state rows into the underlying unique official bet;
- do not double-count a bet because it has both lock and settlement records;
- exclude `NO BET — HOLD` states from P/L;
- exclude counterfactual simulations from P/L;
- preserve half-win, push, half-loss, win, and loss settlement semantics.

All audit dates/times are interpreted in `Asia/Ho_Chi_Minh` / ICT unless explicitly stated otherwise.

---

## Authority

Airtable is the current authoritative decision-state history for reconstructing Football v1.0 betting decisions. Search Airtable before reconstructing prior betting history from chat memory or old repository documents.