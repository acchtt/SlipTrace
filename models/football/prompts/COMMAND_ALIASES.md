# Football v2 — Command aliases

## Active router

Only the first slash command routes the message.

| Command | Active authority |
|---|---|
| /sweep [window] | V4 source-backed intake: models/football/stages_v4/SWEEP.md |
| /rank | V4 Football C rank: models/football/stages_v4/RANK.md |
| /xi | One Football C assessment with optional observed/executable price check |
| /xi exception | Explicit user-requested C assessment outside routine board authority |
| /live | Same Football C assessment using current started-match state |
| /audit | Post-slate audit |
| /report | Read-only current report |

Aliases are case-insensitive. Text after the command is normal launcher input.

## /sweep

Use V4 only. Start from the actual requested/current ICT window and never
retroactively admit already-started fixtures.

The sweep acquires complete provider date surfaces before registry/filtering,
then applies exclusions, research priority and goals-first qualification.

Do not invoke retired V1-V3 checkpoint, repair, ZIP or capacity workflows.

## /rank

Use the newest/explicit native V4_SWEEP_READY receipt.

The rank stage performs original-source replay and a fresh full-cohort status
check before executing the single official Football C board, then independently
verifies Airtable persistence once.

Routine Step 2 trusts the resulting verified C rank+persistence receipt; it
does not repeat source replay.

## /xi

/xi is one command. The user does not need separate assess/bet commands.

Order:

1. current Football C assessment, no odds required;
2. if the user supplied a screenshot/observed quote, evaluate that exact
   line/odds through the shared C quote policy;
3. if a genuinely current executable quote and all strict execution evidence
   exist, run the strict C decision;
4. persist/read back once when persistence is required.

A user screenshot is the sole price source for that comparison. Do not search
for replacement odds, re-time it, or request a new screenshot merely because
processing took time.

Observed-quote ACT/WAIT/PASS is conditional only. It never authorizes
publication/exposure by itself.

WAIT requires an explicitly evidenced reachable target. A lone screenshot does
not prove same-line odds will improve.

## /xi exception

An explicit exception can assess a STOP/non-board fixture from independently
researched Football C evidence. It does not authorize retrospective prematch
action after kickoff.

## /live

/live uses the same Football C assessment with actual current score/minute and
material events. Do not recreate prematch action after kickoff.

## /audit

Audit frozen prospective evidence against actual outcomes. Never rewrite
historical decisions. Retired C2/C3/C4 records are read-only audit material.

## /report

Read only from active operational state. User P/L comes only from
Actual Bets — Current.

## Active model and data boundaries

- Football C: official and only active model.
- C2/C3/C4: retired for all new work.
- Active model base: appbzxqXYf0lKfD4P.
- Historical retired-model fields/receipts remain immutable and read-only.
- WATCH and unresolved WAIT create no synthetic active exposure.
- Actual Bets — Current is the only authority for physical user P/L.

## Retired command/model semantics

Old V1-V3 sweep/resume/repair/ZIP/compact-capacity semantics and all C2/C3/C4
execution paths are historical only. If an old handoff mentions them, reload
this router and use the current V4 + Football C workflow.
