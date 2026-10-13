# Football C + C2 active pair

## Roster

- Football C is official.
- Football C2 is the only active shadow model.
- Football C3 and Football C4 are retired for new execution.

A current assessment is C + C2. A C-only completion is invalid unless the user
explicitly asks for a historical single-model inspection.

## Shared facts, independent policy

Freeze one factual football epoch per fixture.

Shared facts may include fixture identity, current status, routes, carrier,
chance/failure evidence, H2H materiality, tournament state and current team/XI
information.

Model-owned state remains independent.

Football C owns its completion/continuation/leakage/stall diagnostics, supported
line, board state/rank, official lane and action.

Football C2 owns its route-quality state, supported line, board state/rank,
shadow action and optional C2-specific opponent leakage + basis.

Never copy C's supported line, completion/stall diagnostics or leakage grade
into C2.

## Step 1

V4 /rank runs both boards from the same factual epoch and persists exact C/C2
engine JSON. stage.py verify independently refetches those exact results once.

The resulting model_evidence_sha256 is the routine /xi continuity proof.

## Step 2 football assessment

Run independent C and C2 stage=football_assessment payloads.

Successful paired football execution is:

EXECUTED_C_C2_FOOTBALL_ONLY

Odds are not required.

## Observed quote

For a screenshot or other non-executable observation, run the same pure C/C2
quote-policy functions used by strict execution.

The observed result may be ACT/WAIT/PASS but always remains non-executable.

C and C2 may produce different actions because their supported burdens and
model policy are independent.

## WAIT

WAIT requires explicit current model-specific reachability evidence and cannot
require negative football information.

The target/minimum comes from core model policy. WAIT is a plan, not assumed
exposure.

## Strict execution

A strict C/C2 pair requires real current executable-price evidence and the
execution contract.

C may produce an official action. C2 is shadow-only.

Persist/read back the exact strict pair once before publication. Do not execute
the pair a second time in the publication guard.

## Exceptions

A user-requested /xi exception does not require routine board authorization but
still requires independently frozen C and C2 football inputs.

If one model cannot be lawfully executed:

C+C2 EXCEPTION INCOMPLETE — <exact reason>

No retroactive prematch action is allowed after kickoff.

## Accounting

WATCH and unresolved WAIT create no prospective synthetic exposure.

C direct strict BET accounting may use its actual observed quote. A WAIT may be
counted only when reached terms are actually confirmed.

C2 remains shadow accounting only and never creates a Website Pick.

Actual user betting and user P/L remain separate and come only from confirmed
Actual Bets — Current rows.
