# SlipTrace Football Model

This repository is dedicated to the **SlipTrace football model**.

It no longer contains the SlipTrace website or models for other sports. The repository exists for football-model development, execution procedures, QA, launchers, persistence contracts, session overrides, and backups.

## Canonical authority

Always start with:

`models/football/CURRENT_MODEL.md`

That file defines the active Football A stack and the authoritative load order. Do not infer the active model from old commits, archived backups, or chat memory.

## Main entry points

- **Current model:** `models/football/CURRENT_MODEL.md`
- **Prospective challenger:** `models/football/challengers/football-c/FOOTBALL_C_SPEC.md` (shadow-only)
- **Compiled PRE / Step 1:** `models/football/procedures/FOOTBALL_PRE_DECISION_SPEC.md`
- **Compiled XI + odds / Step 2:** `models/football/procedures/FOOTBALL_STEP2_EXECUTION_SPEC.md`
- **Sweep process:** `models/football/procedures/FOOTBALL_MATCH_SWEEP_AND_RESEARCH_PROCEDURE.md`
- **Time integrity:** `models/football/procedures/FOOTBALL_TIME_AND_SCHEDULE_INTEGRITY.md`
- **Betting procedure:** `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
- **Normal-chat launchers / handoffs:** `handoffs/football/`
- **Model QA skill:** `.agents/skills/football-model-qa/SKILL.md`

## Repository layout

```text
.
├── README.md
├── AGENTS.md
├── FOOTBALL_CHAT_PROTOCOL.md
├── .agents/
│   └── skills/football-model-qa/
├── .github/
│   └── workflows/football-step2-research-gate.yml
├── handoffs/
│   └── football/
└── models/
    └── football/
        ├── CURRENT_MODEL.md
        ├── rules/
        ├── procedures/
        ├── prompts/
        ├── airtable/
        ├── challengers/
        ├── qa/
        ├── orchestration/
        ├── session_overrides/
        ├── trials/
        └── backups/
```

## Historical safety

Before this repository was reduced to football-only, a full restore branch was created:

`archive/pre-football-only-2026-09-29`

The current Football A stack was also snapshotted at:

`models/football/backups/2026-09-29_2038_current_model_snapshot/`

Git history remains the source for removed website code and non-football models.

## Scope

This repository is **not a website repository** and has no GitHub Pages application. It is the working source of truth for the football model and its operational workflow.
