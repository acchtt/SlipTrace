# Football Prompt System

These files are the canonical workflow prompts for the football model.

## Design goal
The chat/Work launcher text should almost never need to change when the model version changes.

Every stage reads `models/football/CURRENT_MODEL.md` first and derives the active official model, active patches, timezone, competition rules, and current load order from the repository at execution time.

Therefore:
- model/rule version changes normally require no launcher update;
- stage/workflow changes require updating only the affected canonical prompt in this directory;
- Airtable ID changes require updating the relevant canonical prompt once;
- old downloaded prompt packs are no longer the source of truth.

## Canonical stages
1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — AiScore universe, time integrity, eligibility, coverage skeleton, Work handoff.
2. `01_WORK_DAILY_SWEEP.md` — deep price/XI-blind structural PRE sweep and frozen Airtable publication.
3. `02_NORMAL_CHAT_XI_ODDS.md` — targeted frozen-PRE read, confirmed-XI rerank, current goal-burden/regime logic, price, final material assessment.
4. `03_NORMAL_CHAT_LIVE.md` — targeted live validation, current no-chase/halftime logic, material live-state logging.
5. `04_WORK_POST_SLATE_AUDIT.md` — historical/version-faithful post-slate audit.

## Permanent launchers
Keep these tiny launchers in your normal chats/Work. They reference GitHub and should not need redownloading.

### Step 0 — Normal Chat
`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and follow the current active model. Execute now for the ICT window I request.`

### Step 1 — Work High
`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first, then run it against the attached AiScore handoff. Execute immediately.`

### Step 2 — Normal Chat XI + odds
`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and use my supplied XI/odds as the current evidence. Execute immediately.`

### Step 3 — Normal Chat live
`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and use my supplied live state/market. Execute immediately.`

### Step 4 — Work High audit
`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the slate/date I specify from Airtable. Execute immediately.`

## Version-change rule
When `CURRENT_MODEL.md` moves to a new version, do not edit these launchers merely to change the version number. Update a canonical stage prompt only when the new model changes that stage's workflow boundary or required behavior.

## Authority
`CURRENT_MODEL.md` and its declared active files outrank stale chat memory, old downloaded packs, and version labels embedded in older historical artifacts.