# Football Prompt System

These files are the canonical workflow prompts for the football model.

## Design goal
The chat/Work launcher text should almost never need to change when the model version changes.

Every stage reads the upstream/default-branch `models/football/CURRENT_MODEL.md` first and derives the active official model, active patches, timezone, competition rules, and current load order from the repository at execution time.

If a locally cached repository copy disagrees with upstream, upstream wins immediately. A stale cache must not cause a run on old rules.

Therefore:
- model/rule version changes normally require no launcher update;
- stage/workflow changes require updating only the affected canonical prompt in this directory;
- Airtable ID changes require updating the relevant canonical prompt once;
- old downloaded prompt packs and stale local caches are no longer the source of truth.

## Canonical stages
1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — AiScore universe, time integrity, eligibility, cheap scope/league filtering, coverage skeleton, and the **only normal fixture sweep** used to create the Work handoff. A normal Work handoff is exported only when `complete:true` and `work_ready:true`.
2. `01_WORK_DAILY_SWEEP.md` — deep price/XI/market-history-blind structural PRE research on the already-pruned handoff; **hard-stop before research if Step 0 is incomplete**; no second fixture sweep; frozen Airtable publication.
3. `02_NORMAL_CHAT_XI_ODDS.md` — targeted frozen-PRE read, confirmed-XI first pass, mandatory lightweight `OPEN → PRE-XI → POST-XI/current` total-market watch, XI/market conflict check, final XI rerank, goal burden/regime/MCE where eligible, current executable price, and final material assessment.
4. `03_NORMAL_CHAT_LIVE.md` — targeted live validation, current no-chase/halftime logic, material live-state logging.
5. `04_WORK_POST_SLATE_AUDIT.md` — historical/version-faithful post-slate audit.

## Usage split

To control Work usage:

`NORMAL CHAT COMPLETE DISCOVERY/FILTER → WORK DEEP STRUCTURE ONLY → NORMAL CHAT XI + MARKET HISTORY + CURRENT PRICE → NORMAL CHAT LIVE → WORK AUDIT`

The boundary is strict:

- Step 0 must finish coverage and reconciliation first.
- If the handoff says `complete:false`, `work_ready:false`, `Reconciled=false`, traversal incomplete, or has a scope/count fault, Work researches **zero fixtures** and returns `HANDOFF INCOMPLETE — RERUN NORMAL CHAT STEP 0` (or `HANDOFF SCOPE FAULT`).
- Work must never research only the confirmed subset of an incomplete slate.
- Work must not traverse AiScore again, backfill omitted fixtures, or spend deep-research usage on opening-odds watch.

The Normal Chat market-history layer is contextual. It may challenge an XI interpretation and, under the active model, may support a narrowly defined MCE exception, but it cannot rewrite frozen PRE or manufacture unsupported structure/EGE.

## Permanent launchers
Keep these tiny launchers in your normal chats/Work. They reference GitHub and should not need redownloading.

### Step 0 — Normal Chat
`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first and follow the current active model. Execute now for the ICT window I request. Do not export a Work handoff unless complete=true and work_ready=true.`

### Step 1 — Work High
`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first, then validate the attached AiScore handoff before any deep research. If it is not complete=true and work_ready=true, stop immediately and send it back to Normal Chat Step 0. Do not run another fixture sweep.`

### Step 2 — Normal Chat XI + odds
`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first, use my supplied XI/current odds as executable evidence, run the opening-to-prematch market-history watch, then execute immediately.`

### Step 3 — Normal Chat live
`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and use my supplied live state/market. Execute immediately.`

### Step 4 — Work High audit
`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the slate/date I specify from Airtable. Execute immediately.`

## Version-change rule
When `CURRENT_MODEL.md` moves to a new version, do not edit these launchers merely to change the version number. Update a canonical stage prompt only when the new model changes that stage's workflow boundary or required behavior.

## Authority
Upstream `CURRENT_MODEL.md` and its declared active files outrank stale chat memory, old downloaded packs, locally cached repository copies, and version labels embedded in older historical artifacts.