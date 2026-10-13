# Football v2 — active Airtable routing

Machine-readable authority: ACTIVE_MODEL_ROUTING.json.

## Active base

Football v2 — Active Operations 2026-10-11  
Base: appbzxqXYf0lKfD4P

The previous base appWyZJjitSBATXAU is historical read-only unless an explicit
historical comparison is requested.

Current /rank, /xi, /live, /audit, /report, model QA/accounting and Website
Picks use the active base. /sweep source acquisition remains governed by the
V4 sweep handoff rather than this model router.

## Model authority

- C official only.
- C2 shadow only.
- C3/C4 fields in cloned tables are historical and stay blank for new work.
- Actual Bets — Current is the only user P/L authority.

## Step 1 — Daily Coverage Ledger

For each new V4 ranked fixture persist:

- immutable Coverage ID / Run ID identity;
- C state, rank, supported line and official FOLLOW/RESERVE/STOP lane;
- C2 state, rank and supported line;
- exact Step1 Engine C Result JSON;
- exact Step1 Engine C2 Result JSON.

Current exact engine-result fields:

- Step1 Engine C Result: fldhUWNoyXzXfQJ3C
- Step1 Engine C2 Result: fldq0n2tDlS58goAm

stage.py verify independently refetches these exact fields once and emits
V4_RANK_PERSISTENCE_VERIFIED plus model_evidence_sha256.

Routine /xi consumes that verified receipt. It does not perform another
source/status replay.

## /xi Decision States

Persist one assessment record per assessment epoch.

Always preserve:

- Assessment ID and canonical match identity;
- assessment time / score / minute / evidence epoch;
- exact C football result;
- exact C2 football result;
- C/C2 supported burdens;
- XI/current football notes where applicable.

XI Assessment Execution Status uses these active values:

- EXECUTED_C_C2_FOOTBALL_ONLY
- EXECUTED_C_C2_FOOTBALL_AND_PRICE
- ENGINE_FAILED_AFTER_ATTEMPT

A failed optional price gate after successful football assessment remains
EXECUTED_C_C2_FOOTBALL_ONLY. It is not an engine failure.

### Observed/screenshot quote

Persist the ordinary evaluated line and evaluated odds fields.

Do not encode a second USER_SCREENSHOT_ONLY_JSON receipt in Evidence Summary.
The attachment/capture reference may remain normal evidence text/attachment
metadata.

Observed/screenshot quotes are non-executable evidence and do not create
Website Picks or model exposure.

### Strict executable price

When a strict C+C2 decision pair succeeds, persist the exact strict results
and current quote fields. Independently refetch once before publication.

The final publication gate compares that pair receipt to the readback and
rechecks current quote/fixture/evidence epoch. It does not execute the models
again.

## Website Picks

Only Football C strict official actions may create Website Picks.

C2 never creates a Website Pick.

WATCH and unresolved WAIT do not create synthetic Website Picks/exposure.

## Actual Bets — Current

Only a user-confirmed physical slip may create/update an Actual Bets row.

Do not copy a model action, screenshot comparison, Website Pick, WATCH or WAIT
into Actual Bets automatically.

Formula P/L fields remain table-owned and must not be written directly.

## Write/readback rule

For each stage:

1. resolve the table from ACTIVE_MODEL_ROUTING.json;
2. write/update the intended active-base record;
3. independently refetch that same record by immutable identity;
4. compare required fields once;
5. report PERSISTENCE_UNVERIFIED if the readback cannot be confirmed.

Do not stack multiple independent reconciliation protocols for the same write.
