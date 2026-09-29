# SlipTrace Football Model

This repository is dedicated to the **SlipTrace football model**.

## Active model

**Football C** is the current official production model.

Start here:

`models/football/CURRENT_MODEL.md`

Production specification:

`models/football/production/FOOTBALL_C.md`

Football A is retired from new decisions and retained only for historical audit and rollback.

## Main workflow

- Step 0 fixture handoff: `models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`
- Integrated Football C board: `models/football/prompts/01_WORK_DAILY_SWEEP.md`
- XI + odds decision: `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md`
- Live / WAIT resolution: `models/football/prompts/03_NORMAL_CHAT_LIVE.md`
- Post-slate audit: `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md`

## Football C philosophy

Football C deliberately replaces Football A's large multi-stage gate stack with an integrated flow:

`AISCORE -> SCREEN -> RESEARCH/ASSESS -> RANK -> XI CONFIRM -> BET/WAIT/PASS -> AUDIT`

H2H and fresh post-XI football research remain mandatory where relevant. Market evidence informs the football judgment but does not become an independent veto machine.

## Repository layout

```text
models/football/
├── CURRENT_MODEL.md
├── production/
│   └── FOOTBALL_C.md
├── prompts/
├── airtable/
├── procedures/
├── rules/          # historical Football A/versioned logic
├── challengers/    # historical/prospective experiment artifacts
├── qa/
├── trials/
└── backups/
```

## Validation status

Football C was activated by explicit user directive before completion of its planned five-board shadow test. Do not describe this activation as a statistically validated QA promotion.

## Historical safety

Pre-C production restore branch:

`archive/pre-football-c-active-2026-09-29`

Football A model snapshot:

`models/football/backups/2026-09-29_2038_current_model_snapshot/`

Earlier pre-cleanup repository:

`archive/pre-football-only-2026-09-29`
