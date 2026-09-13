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
1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — AiScore discovery, time integrity, actionable-senior completeness, cheap scope/league filtering, coverage skeleton, and the **only normal fixture sweep** used to create the Work handoff. Exact enumeration of already-excluded youth/reserve/lower raw blocks is best-effort and does not block Work when actionable coverage is complete.
2. `01_WORK_DAILY_SWEEP.md` — deep price/XI/market-history-blind structural PRE research on the already-pruned handoff; hard-stop only for an **actionable coverage** fault; no second fixture sweep; frozen Airtable publication.
3. `02_NORMAL_CHAT_XI_ODDS.md` — targeted frozen-PRE read, confirmed-XI first pass, mandatory lightweight `OPEN → PRE-XI → POST-XI/current` total-market watch, XI/market conflict check, final XI rerank, goal burden/regime, MCE shadow test, current executable price, Structural Rank + Execution Class, and final material assessment.
4. `03_NORMAL_CHAT_LIVE.md` — targeted live validation, current no-chase/halftime logic, material live-state logging.
5. `04_WORK_POST_SLATE_AUDIT.md` — historical/version-faithful post-slate audit.

## Usage split

To control Work usage:

`NORMAL CHAT ACTIONABLE DISCOVERY/FILTER → WORK DEEP STRUCTURE ONLY → NORMAL CHAT XI + MARKET HISTORY + CURRENT PRICE → NORMAL CHAT LIVE → WORK AUDIT`

The boundary is strict but practical:

- Step 0 must prove `actionable_complete=true` and `work_ready=true` before Work starts.
- `raw_audit_complete=false` is allowed when the only missing exact enumeration belongs to categories already excluded from Work, and those gaps are explicitly recorded as non-blocking.
- If the handoff has a missing/unverified PRIORITY/NORMAL senior block, eligible senior cup/continental block, unresolved senior conditional block, terminal-window fault, or Work-array count mismatch, Work researches **zero fixtures** and returns `HANDOFF INCOMPLETE — ACTIONABLE COVERAGE GAP`.
- Work must never research only a confirmed subset of a genuinely incomplete actionable slate.
- Work must not traverse AiScore again, backfill omitted fixtures, repair non-blocking raw gaps, or spend deep-research usage on opening-odds watch.

The Normal Chat market-history layer is contextual. It may challenge an XI interpretation and support an MCE shadow observation, but under v0.2.54 it cannot create MCE/live-decay official exposure, rewrite frozen PRE, or manufacture unsupported structure/EGE.

## Permanent launchers
Keep these tiny launchers in your normal chats/Work. They reference GitHub and should not need redownloading.

### Step 0 — Normal Chat
`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first and follow the current active model. Execute now for the ICT window I request. Prove actionable_complete/work_ready; exact enumeration of already-excluded raw micro/youth blocks is best-effort.`

### Step 1 — Work High
`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read upstream CURRENT_MODEL.md first, then validate the attached AiScore handoff before any deep research. Stop only for an actionable coverage/scope fault; do not rerun the fixture sweep or repair non-blocking raw-audit gaps.`

### Step 2 — Normal Chat XI + odds
`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first, use my supplied XI/current odds as executable evidence, run the opening-to-prematch market-history watch, then execute immediately.`

### Step 3 — Normal Chat live
`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and use my supplied live state/market. Execute immediately.`

### Step 4 — Work High audit
`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the slate/date I specify from Airtable. Execute immediately.`

## Completeness terminology

For normal production:

- `complete=true` = actionable senior completeness for backward compatibility;
- `actionable_complete=true` = every potentially actionable senior block/fixture in the requested window was accounted for;
- `work_ready=true` = safe to spend Work deep-research usage;
- `raw_audit_complete=false` = exact all-fixture enumeration was not possible, but any gaps are confined to already-excluded categories;
- `raw_count_mode=lower_bound` = discovered raw count is not claimed to be exact.

This split prevents the dynamic AiScore date index from blocking the model merely because excluded youth/lower/reserve fixtures cannot be individually enumerated.

## Version-change rule
When `CURRENT_MODEL.md` moves to a new version, do not edit these launchers merely to change the version number. Update a canonical stage prompt only when the new model changes that stage's workflow boundary or required behavior.

## Authority
Upstream `CURRENT_MODEL.md` and its declared active files outrank stale chat memory, old downloaded packs, locally cached repository copies, and version labels embedded in older historical artifacts.