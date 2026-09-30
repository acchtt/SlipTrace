# Football Production Launchers

Every stage reads upstream `models/football/CURRENT_MODEL.md` first.

**Active model: Football C.**

## Canonical stages

1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — build the RESEARCHABLE_SENIOR AiScore fixture ZIP handoff: protected major/international blocks plus ordinary senior fixtures that pass the cheap current-data researchability gate.
2. `01_WORK_DAILY_SWEEP.md` — one common research freeze, then Football C official board + Football C2 shadow board + Python validation.
3. `02_NORMAL_CHAT_XI_ODDS.md` — one common XI/research freeze, then Football C official action + Football C2 shadow action + Python validation.
4. `03_NORMAL_CHAT_LIVE.md` — resolve a predeclared C-WAIT using thesis health.
5. `04_WORK_POST_SLATE_AUDIT.md` — settle/audit Football C and preserve historical model fidelity.

`05_NORMAL_CHAT_FOOTBALL_C.md` is the original shadow-test launcher and is retained for experiment history. It is **not** the production launcher now.

## Simple commands

### Step 0
`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and build the requested ICT-window handoff.`

### Board
`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first. Build the Football C official board and Football C2 shadow board from one common frozen research state, then run Python validation.`

### XI + odds
`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first. Use one common XI/research evidence freeze, issue Football C official and C2 shadow actions, then run Python validation.`

### Live / wait
`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and resolve the existing Football C wait plan from my supplied live state/market.`

### Audit
`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the requested slate.`
