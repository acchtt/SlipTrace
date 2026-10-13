# Football v2 — Command aliases

## Active router

Only the first slash command routes the message.

| Command | Active authority |
|---|---|
| /sweep [window] | V4 source-backed intake: models/football/stages_v4/SWEEP.md |
| /rank | V4 C/C2 rank: models/football/stages_v4/RANK.md |
| /xi | One C+C2 football assessment with optional observed/executable price check |
| /xi exception | Explicit user-requested fixture assessment outside routine board authority |
| /live | Same C/C2 football assessment using current started-match state |
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

The rank stage itself performs original-source replay and a fresh full-cohort
status check before C/C2 board execution, then independently verifies Airtable
persistence once.

For /rank newest receipt, resolve the matching source from the normal V4
handoff/provenance. Do not ask the user to upload a source that the project
already owns.

Routine Step 2 trusts the resulting verified rank+persistence receipt; it does
not repeat source replay.

## /xi

/xi is one command. The user does not need separate assess/bet commands.

Order:

1. current Football C + C2 football assessment, no odds required;
2. if the user already supplied a screenshot/observed quote, evaluate that
   exact line/odds through the shared C/C2 quote policy;
3. if a genuinely current executable quote and all strict execution evidence
   already exist, run the strict decision pair;
4. persist/read back once when persistence is required.

A user screenshot is the sole price source for that comparison. Do not search
for replacement odds, re-time it, or ask for a new screenshot because
processing took time.

Observed-quote ACT/WAIT/PASS is conditional only. It never authorizes
exposure/publication by itself.

WAIT may be shown only when model-specific research explicitly establishes a
reachable target that does not require negative football information. Do not
invent a reachability rule from market gap alone.

## /xi exception

An explicit exception can assess a STOP/non-board fixture from independently
researched C/C2 evidence. It does not need routine board authorization.

The exception does not authorize retroactive prematch action after kickoff.

## /live

/live uses the same football assessment path as /xi with the actual current
score/minute/material events.

After kickoff:

- keep football analysis;
- discard prematch execution assumptions;
- never recreate a prematch action retrospectively;
- an observed live price is comparison evidence only unless a separately
  implemented live execution policy authorizes it.

There is no standalone kickoff-transition state machine in the active stack.

## /audit

Audit frozen prospective evidence against actual outcomes. Never rewrite
historical decisions. Experimental shadow/probability tools are QA only unless
the user explicitly asks for that analysis.

## /report

Read only from the active operational state. User P/L comes only from
Actual Bets — Current.

## Active model and data boundaries

- Football C: official.
- Football C2: shadow only.
- C3/C4: retired for new work.
- Active model base: appbzxqXYf0lKfD4P.
- Historical base: read-only when explicitly requested.
- C2 never creates a Website Pick.
- WATCH and unresolved WAIT create no synthetic active exposure.
- Actual Bets — Current is the only authority for physical user profit/loss.

## Retired command semantics

Old V1-V3 sweep/resume/repair/ZIP/compact-capacity semantics are historical
only. If an old handoff mentions them, reload this router and use the current
V4/C+C2 command instead of reviving the old workflow.
