# Football v2 — active Airtable routing

Machine-readable authority: ACTIVE_MODEL_ROUTING.json.

## Active base

Football v2 — Active Operations 2026-10-11
Base: appbzxqXYf0lKfD4P

The previous base appWyZJjitSBATXAU is historical read-only.

## Model authority

- Football C is the only active model.
- C2/C3/C4 are retired and their existing fields are historical read-only.
- Actual Bets — Current is the only user P/L authority.

## Step 1 — Daily Coverage Ledger

For each new V4 ranked fixture persist:

- immutable Coverage ID / Run ID;
- C state, rank, supported burden and official FOLLOW/RESERVE/STOP lane;
- exact Step1 Engine C Result JSON.

Current active engine-result field:

- Step1 Engine C Result: fldhUWNoyXzXfQJ3C

The existing Step1 Engine C2 Result field
(fldq0n2tDlS58goAm) remains only for frozen historical rows and must not be
required or written by new /rank operations.

stage.py verify independently refetches the C fields once and emits
V4_RANK_PERSISTENCE_VERIFIED plus the exact C evidence hash.

## /xi Decision States

Persist one assessment record per evidence epoch.

Always preserve:

- Assessment ID and canonical match identity;
- assessment time / score / minute / evidence epoch;
- exact C football result;
- C supported burden;
- evaluated line/odds when a user-supplied observed quote was compared.

XI Assessment Execution Status active values:

- EXECUTED_C_FOOTBALL_ONLY
- EXECUTED_C_FOOTBALL_AND_PRICE
- ENGINE_FAILED_AFTER_ATTEMPT

A failed optional price check after a successful football assessment remains
EXECUTED_C_FOOTBALL_ONLY.

Retired C2 Decision State fields remain historical only.

## Strict executable price

When a strict C decision succeeds, persist the exact C result and quote fields.
Independently refetch once before publication.

The publication gate compares that C decision receipt to the readback and
rechecks current quote/fixture/evidence epoch. It does not execute C again.

## Website Picks and Actual Bets

Only an authorized Football C strict action may create a Website Pick.

WATCH and unresolved WAIT do not create synthetic exposure.

Only a user-confirmed physical slip may create/update Actual Bets — Current.

## Write/readback rule

For each active stage:

1. resolve the table from ACTIVE_MODEL_ROUTING.json;
2. write/update the intended active-base record;
3. independently refetch by immutable identity;
4. compare required C fields once;
5. report PERSISTENCE_UNVERIFIED if readback cannot be confirmed.
