# Football Chat Operating Protocol

**Status:** ACTIVE  
**Canonical model entry point:** `models/football/CURRENT_MODEL.md`  
**Current official model:** Football C only  
**Active operational store:** Google Sheets `Football v2 — Active Operations`
(`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`)

## Authority order

1. `models/football/CURRENT_MODEL.md`
2. `models/football/production/FOOTBALL_C.md`
3. current canonical stage launcher
4. frozen Football C board state in Daily Coverage Ledger
5. Football C Decision States
6. user-supplied current XI/odds/live evidence
7. user bet slip for physical execution truth

Do not load Football A or retired C2/C3/C4 rules into a new production decision.

## Conversation workflow

`Normal /sweep -> Work /rank -> Normal /xi -> Normal /live -> Work /audit`

- **Normal /sweep:** acquire once, research the targeted cohort directly, and
  produce the native V4 handoff. Unfinished upstream research remains a visible
  resumable checkpoint and is not a completed sweep.
- **Work /rank:** source replay, full-cohort status, full Football C research,
  deterministic ranking and verified Google Sheets persistence.
- **Normal /xi:** fast current XI/screenshot interaction; deterministic Football
  C runtime remains the official decision authority.
- **Normal /live:** current-epoch football assessment; no retrospective prematch
  action and no invented live execution authority.
- **Work /audit:** deep cross-board/repo reconciliation and regression work.

Frozen historical states remain immutable. If this protocol conflicts with
`CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.
