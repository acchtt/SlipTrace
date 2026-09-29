# Football Production Launchers

Every stage reads upstream `models/football/CURRENT_MODEL.md` first.

**Active model: Football C.**

## Canonical stages

1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — build the canonical AiScore fixture ZIP handoff.
2. `01_WORK_DAILY_SWEEP.md` — Football C integrated screening, research and ranking.
3. `02_NORMAL_CHAT_XI_ODDS.md` — Football C XI + mandatory fresh post-XI web research + H2H + current odds decision.
4. `03_NORMAL_CHAT_LIVE.md` — resolve a predeclared C-WAIT using thesis health.
5. `04_WORK_POST_SLATE_AUDIT.md` — settle/audit Football C and preserve historical model fidelity.

`05_NORMAL_CHAT_FOOTBALL_C.md` is the original shadow-test launcher and is retained for experiment history. It is **not** the production launcher now.

## Simple commands

### Step 0
`Load and execute models/football/prompts/00_NORMAL_CHAT_AISCORE_FETCH.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and build the requested ICT-window handoff.`

### Board
`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and build the Football C board from the attached AISCORE_FIXTURES_*.zip.`

### XI + odds
`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and assess my supplied XI/current odds with Football C.`

### Live / wait
`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and resolve the existing Football C wait plan from my supplied live state/market.`

### Audit
`Load and execute models/football/prompts/04_WORK_POST_SLATE_AUDIT.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and audit the requested slate.`
