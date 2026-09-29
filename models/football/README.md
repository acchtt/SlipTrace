# SlipTrace Football Model

This directory contains the football model, its production workflow, and prospective challenger tests.

## Production

**Official model:** Football A  
**Canonical authority:** `CURRENT_MODEL.md`

Football A remains the only production model. Its active rule/procedure load order is declared in `CURRENT_MODEL.md`; do not infer production state from older rule filenames.

Main production entry points:
- `procedures/FOOTBALL_PRE_DECISION_SPEC.md`
- `procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`
- `procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
- `procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
- `procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md`
- `prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`
- `prompts/01_WORK_DAILY_SWEEP.md`
- `prompts/02_NORMAL_CHAT_XI_ODDS.md`
- `prompts/03_NORMAL_CHAT_LIVE.md`
- `prompts/04_WORK_POST_SLATE_AUDIT.md`

## Prospective challenger

**Football C — SHADOW** is an integrated architecture challenger inspired by the simpler v0.2.47 operating philosophy while preserving lessons learned about XI mechanism, fresh web research, H2H, protected lines and thesis-aware waiting.

Start here:
- `challengers/football-c/FOOTBALL_C_SPEC.md`
- `challengers/football-c/TEST_PROTOCOL.md`
- `prompts/05_NORMAL_CHAT_FOOTBALL_C.md`
- `trials/FOOTBALL_C_VS_A_2026-09-29.md`

Football C is **not** part of Football A's load order and must not create official exposure during the trial.

## Directory map

```text
models/football/
├── CURRENT_MODEL.md
├── challengers/
├── rules/
├── procedures/
├── prompts/
├── airtable/
├── qa/
├── orchestration/
├── session_overrides/
├── trials/
└── backups/
```

## Governance

Permanent model changes follow `procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md`.

Discovery examples may motivate a challenger but do not validate it. Freeze the challenger before prospective outcomes, run it on the same information clock as the champion, preserve non-bets as well as bets, and do not rewrite historical decisions.

## Safety / restore point

The pre-Football-C production stack remains recoverable from Git history and from:

`backups/2026-09-29_2038_current_model_snapshot/`
