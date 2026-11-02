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

**Primary production route:** `Normal /block -> Normal /xi -> Normal /live -> Normal /audit`

**Supporting routes:** `Normal /sweep` for full-window source capture and
`Work /rank` for secondary whole-slate comparison/audit.

`/audit deep -> Work` only when normal audit escalates

- **Normal /block (PRIMARY):** resolve the complete requested kickoff block,
  assess every in-scope candidate to equal depth, compare the block
  football-first, and persist each assessment independently. Existing rank is
  secondary metadata only and cannot filter the block.
- **Normal /sweep:** acquire once, research the targeted cohort directly, and
  produce the native V4 handoff. It is now supporting source/intake
  infrastructure rather than the mandatory route into primary assessment.
- **Work /rank (SECONDARY):** source replay, full-cohort status, Football C
  whole-slate research/ranking and verified Google Sheets persistence for
  comparison, website state and audit. It is not the primary assessment gate.
- **Normal /xi:** fast current XI/screenshot interaction; deterministic Football
  C runtime remains the official decision authority.
- **Normal /live:** current-epoch football assessment; no retrospective prematch
  action and no invented live execution authority.
- **Normal /audit:** lightweight targeted diagnosis. It automatically decides
  whether structural escalation is required.
- **Work /audit deep:** only after `DEEP AUDIT REQUIRED`; consume the compact
  handoff for repo-wide/rule/runtime/regression work.

Frozen historical states remain immutable. If this protocol conflicts with
`CURRENT_MODEL.md`, `CURRENT_MODEL.md` wins.
