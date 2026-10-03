# Football Production Launchers

Every stage reads upstream `models/football/CURRENT_MODEL.md` first.

**Active model: Football C.**

## Short commands — preferred

Use these in normal conversation:

| Command | Meaning | Example |
|---|---|---|
| `/sweep` | Step 0 AiScore intake | `/sweep now to 3am` |
| `/rank` | Step 1 Football C/C2 board | attach ZIP, then `/rank` |
| `/xi` | Step 2 XI + odds | attach screenshots, then `/xi` |
| `/live` | live/wait assessment | attach live state, then `/live` |
| `/audit` | post-slate audit | `/audit yesterday` |
| `/report` | read current state without rerunning model stages | `/report next matches` |
| `/help` | show the command cheat sheet | `/help` |

Canonical routing rules live in `COMMAND_ALIASES.md`.

You no longer need to type the long launcher filename for normal use. The explicit filename form remains supported for compatibility.

## Canonical stages

1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — build the RESEARCHABLE_SENIOR AiScore fixture ZIP handoff: protected major/international blocks plus ordinary senior fixtures that pass the cheap current-data researchability gate.
2. `01_WORK_DAILY_SWEEP.md` — one common research freeze, Football C official board + C2 shadow board + Python validation, then a FOLLOW/RESERVE/STOP operational guard (max 6 routine FOLLOW, max 4 RESERVE).
3. `02_NORMAL_CHAT_XI_ODDS.md` — process FOLLOW normally; RESERVE only when activated; STOP only by explicit exception, then run common XI/research and C/C2/Python decisions.
4. `03_NORMAL_CHAT_LIVE.md` — resolve a predeclared C-WAIT using thesis health.
5. `04_WORK_POST_SLATE_AUDIT.md` — settle/audit Football C and preserve historical model fidelity.
6. `06_NORMAL_CHAT_REPORT.md` — report current persisted board/decision/schedule state without rerunning predictive stages.

`05_NORMAL_CHAT_FOOTBALL_C.md` is **hard-retired**. It is retained for experiment history only and must return `LAUNCHER RETIRED — USE CURRENT FOOTBALL C COMMAND ROUTER` if invoked for new production.

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


## Tournament incentive hard gate

Tournament incentive is a hard evidence gate, not an optional annotation.

- Step 1 explicitly declares applicability for every fixture and completes the format/incentive block before C/C2 classification.
- Step 2 rechecks applicable fixtures before any C/C2 action.
- Live recomputes applicable incentive state on every material new epoch.
- Missing incentive evidence blocks the relevant assessment/decision instead of silently defaulting.
