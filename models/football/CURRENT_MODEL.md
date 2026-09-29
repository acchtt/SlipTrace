# Current Football Model

**Active official model:** Football **C**  
**Effective:** 2026-09-29 ICT  
**Activation type:** explicit user-directed production activation before completion of the planned C shadow holdout  
**Previous official model:** Football A — historical/rollback only  
**Fixture authority:** AiScore  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for all new football work.

## Active production load order

Load only:

1. `models/football/CURRENT_MODEL.md`
2. `models/football/production/FOOTBALL_C.md`
3. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
4. `models/football/airtable/FOOTBALL_COVERAGE_AIRTABLE.md`
5. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`
6. the stage launcher being executed from `models/football/prompts/`

Do **not** load Football A's versioned rules, PRE compiler, Step-2 compiler, HMA/decay/carrier patches, or old session overrides into a new Football C decision unless an audit explicitly asks to reconstruct an old Football A state.

## Current production sequence

`STEP 0 AISCORE HANDOFF -> FOOTBALL C INTEGRATED BOARD -> XI + ODDS ONE-PASS CONFIRMATION -> C-BET / C-WAIT / C-PASS -> WAIT RESOLUTION IF NEEDED -> SETTLEMENT/AUDIT`

### Step 0
Use:
`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

It owns fixture discovery, scope/time integrity and the canonical ZIP handoff.

### Board / Step 1
Use:
`models/football/prompts/01_WORK_DAILY_SWEEP.md`

It now runs Football C's integrated screening/research/ranking. It does **not** run Football A's PRE compiler.

### XI + odds / Step 2
Use:
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

It runs one integrated Football C confirmation pass with mandatory fresh post-XI football web research, H2H/matchup context and the user-supplied executable price.

### Live
Use:
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Normal live use resolves a predeclared C-WAIT and explicitly distinguishes price decay from thesis decay.

### Audit
Use:
`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

Audit the model/version that actually produced each historical decision.

## Football C invariants

- integrated end-to-end football judgment;
- H2H mandatory when usable;
- fresh post-XI public-web football research mandatory before final prematch C-BET;
- market evidence informs but does not independently create/veto football structure;
- supported burden chosen before price;
- no higher burden merely for better odds;
- >=1.65 normal price zone;
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material football veto;
- WAIT requires a healthy realistic path, not merely a numerical future target;
- target reached never auto-executes: thesis health must still be positive;
- actual bet slips are physical execution truth;
- historical Football A decisions remain immutable.

## Validation status

Football C was originally frozen as challenger `FC-C-20260929-INTEGRATED-01`, but the user explicitly promoted it before the planned five-board shadow checkpoint.

Therefore:
- Football C is active production;
- it is **not** described as prospectively validated;
- continue tracking its first boards closely;
- any later rule change should be versioned/prospectively frozen rather than silently editing historical C logic.

## Rollback

Pre-C production state:
`archive/pre-football-c-active-2026-09-29`

Football A snapshot:
`models/football/backups/2026-09-29_2038_current_model_snapshot/`
