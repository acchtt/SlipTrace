# Football V4 — current source and rank stages

**Status:** ACTIVE OVERVIEW  
**Detailed authority:** `SWEEP.md`, `RANK.md`, `stage.py`  
**Model:** Football C only

This README is descriptive. It must not redefine the executable V4 contracts.

## Current flow

`/sweep` runs in normal chat and produces a native, attested
`V4_SWEEP_READY` receipt from complete provider date/listing surfaces.

`/rank` runs in ChatGPT Work, consumes that exact receipt plus the unchanged
original source, refreshes the full eligible cohort's fixture status/kickoff,
researches Football C, executes the deterministic C board, persists official
FOCUS rows to Google Sheets, then independently verifies the readback once.

There is no active C2/C3/C4 rank path, paired-model requirement, Airtable
production write, Step0 ZIP, fixed 8/12/15 Work budget, or legacy capacity
replenishment engine.

## Sweep invariants

- acquire complete provider date/listing surfaces before registry/filtering;
- preserve canonical fixture IDs, kickoff, source URL and observation time;
- apply standing user/scope exclusions explicitly;
- use registry lane as research context, not a prediction;
- run the source-backed goals-first research screen;
- retain unresolved research as pending rather than inventing a model PASS;
- no odds or confirmed XI are required for intake.

The source-completeness contract is implemented by
`source_completeness.py` and enforced by `stage.py`.

## Rank invariants

- replay the unchanged original source;
- independently refresh status/kickoff for the whole eligible cohort;
- never create retroactive prematch ranks after kickoff;
- research the complete cohort in frozen goals-first order;
- Football C only;
- WATCH/PASS remain in the frozen research assessment but outside the official
  ranked board;
- every genuine C-FOCUS survives board admission; there is no fixed numeric
  board-size cap;
- unresolved research remains checkpointed/resumable;
- G3-funded C-FOCUS with G4 research INCOMPLETE or EVIDENCE_LIMITED cannot
  finalize on the official board;
- persist official C board rows to Google Sheets and independently verify once.

## G4 completion

The active G4 evidence states and provenance contract are defined by
`../procedures/FOOTBALL_C_G4_EVIDENCE_CONTRACT.md` and enforced by
`engine/adapter.py` plus `stage.py`.

Unavailability is not negative evidence. Incomplete/evidence-limited G4 work
stays unresolved. Completed mixed/rejected/funded states remain distinguishable
for later audit and market-disagreement reinspection.

## Persistence

Active operational store:

`Football v2 — Active Operations`  
Spreadsheet ID:
`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`

The `Daily Coverage Ledger` is the active rank persistence surface.
Historical Airtable rows and retired-model fields are immutable audit material
only.

## Recovery / handoff

When cross-chat execution requires an attested bundle, use the canonical
`v4-original-source-attested-receipts` artifact containing the unchanged
source, native V4 sweep receipt and rank handoff.

Recovery never authorizes retrospective ranking. Current status/kickoff must
still be checked before rank execution.

## Historical material

Older V1–V3, AiScore-only, C+C2, Airtable, ZIP/checkpoint and compact-capacity
instructions elsewhere in the repository are historical unless explicitly
imported by the current authority files above.
