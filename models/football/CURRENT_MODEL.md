# Current Football Model

**Active official model:** Football **C**  
**Effective:** 2026-09-29 ICT  
**Previous official model:** Football A — historical/rollback only  
**Fixture authority:** AiScore  
**Operational timezone:** Asia/Ho_Chi_Minh (ICT, UTC+7)

This file is the canonical entry point for all new football work.

## Active load order

1. `models/football/CURRENT_MODEL.md`
2. `models/football/production/FOOTBALL_C.md`
3. `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
4. football Airtable contracts
5. the current stage launcher under `models/football/prompts/`

Do not load Football A's versioned rules, PRE compiler, Step-2 compiler, HMA/decay/carrier patches, or old session overrides into new Football C decisions.

## Production sequence

`BROAD SENIOR AISCORE HANDOFF -> C INTEGRATED SCREEN/RESEARCH/RANK -> XI+ODDS ONE-PASS CONFIRMATION -> C-BET/C-WAIT/C-PASS -> WAIT RESOLUTION -> AUDIT`

### Step 0
`models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`

Default intake is **BROAD_SENIOR_PRODUCTION**.

All reasonable senior first-team fixtures in the requested AiScore window are sent to Football C after **hard scope/identity/time exclusions only**.

Legacy NARROW_CORE, PRIORITY/NORMAL/CONDITIONAL, LOW-GOAL, Finland/Japan, professional-lower-division, and small-cup prefilters are not allowed to remove an otherwise reasonable senior fixture before Football C sees it.

### Step 1
`models/football/prompts/01_WORK_DAILY_SWEEP.md`

Football C itself screens every admitted fixture and records C-PASS / C-WATCH / C-FOCUS.

### Step 2
`models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`

One integrated XI/odds confirmation with mandatory fresh post-XI football web research and relevant H2H/matchup context.

### Live
`models/football/prompts/03_NORMAL_CHAT_LIVE.md`

Resolve predeclared C-WAIT with target + thesis-health check.

### Audit
`models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

Audit full funnel and preserve the model/version that actually produced each historical decision.

## Football C invariants

- Step 0 broad senior intake; football-quality screening belongs to C.
- No fixed board-size target.
- H2H mandatory when usable.
- Fresh post-XI public-web football research mandatory before final prematch C-BET.
- Market evidence informs but does not independently create/veto football structure.
- Supported burden chosen before price.
- No higher burden merely for better odds.
- >=1.65 normal price zone.
- 1.60–1.64 soft zone only for top-ranked C-FOCUS at/below supported burden with no material football veto.
- WAIT requires a healthy realistic path.
- Target reached never auto-executes; thesis health must still be positive.
- Actual bet slips are physical execution truth.
- Historical Football A decisions remain immutable.

## Validation status

Football C is active by explicit user direction before completion of its original planned shadow holdout.

The broad-senior intake change is being tried prospectively. Track the full funnel rather than judging it from one prior Africa block.

## Rollback

Pre-C:
`archive/pre-football-c-active-2026-09-29`

Pre-broad-intake C:
`archive/pre-football-c-broad-senior-intake-2026-09-29`


## Deterministic engine status

`models/football/engine/` is the active **shadow validation layer** for Football C/C2.

It does not replace semantic football research. Research must first freeze structured judgments (routes, carrier, chance quality, suppression, supported burden, XI/thesis state). The engine then applies deterministic ranking/execution/settlement rules.

Until explicitly promoted:
- text Football C remains production authority;
- C2 remains a shadow challenger where declared;
- engine outputs are shadow validation;
- text/code disagreement must be preserved and reported, never silently reconciled.
