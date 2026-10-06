# Football prompt launchers

Current production roster: **Football C official + Football C2 shadow**.

| Alias | Stage | Typical input |
|---|---|---|
| `/sweep` | Step 0 senior fixture acquisition/intake | time window |
| `/rank` | Step 1 C official + C2 shadow board | Step-0 ZIP/handoff |
| `/xi` | Step 2 C official + C2 shadow XI/odds | XI + odds |
| `/live` | live/WAIT resolution for C + C2 | live state/market |
| `/audit` | post-slate production/model QA | board/date scope |
| `/report` | read-only current state summary | scope |

Always read `CURRENT_MODEL.md` and the current launcher. A copied handoff is historical context, not authority.

## Workflow

1. `00_NORMAL_CHAT_AISCORE_FETCH.md` — acquire/reconcile senior production scope, operational viability, researchability and capacity queue.
2. `01_WORK_DAILY_SWEEP.md` — freeze one common Step-1 evidence epoch, create C official + C2 shadow boards, execute `board_pair_cli.py`, then assign C FOLLOW/RESERVE/STOP and replenish capacity if required.
3. `02_NORMAL_CHAT_XI_ODDS.md` — freeze one current XI/research/market epoch and execute C+C2 atomically through `xi_portable.py pair`.
4. `03_NORMAL_CHAT_LIVE.md` — resolve C official and C2 shadow live/WAIT states from the same live epoch.
5. `04_WORK_POST_SLATE_AUDIT.md` — audit frozen decisions, process integrity, results and active-model accounting.
6. `06_NORMAL_CHAT_REPORT.md` — report already-existing state without rerunning predictive stages.

## Current model visibility

Current /rank, /xi and /live output must show:
- OFFICIAL C;
- SHADOW C2.

C3/C4 are retired from new/current execution. They may appear only in explicitly historical audit/report context when a genuine prospective historical record exists.

If active C2 cannot be lawfully frozen/executed for a current all-model/exception request, show the exact incomplete reason. Do not silently convert the workflow to C-only completion.

## Direct launcher form

Examples:

`Load and execute models/football/prompts/01_WORK_DAILY_SWEEP.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first. Build Football C official and Football C2 shadow boards from one frozen common research state and execute the C+C2 board pair.`

`Load and execute models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first. Freeze one current XI/research evidence epoch and execute Football C + C2 atomically.`

`Load and execute models/football/prompts/03_NORMAL_CHAT_LIVE.md from acchtt/SlipTrace. Read CURRENT_MODEL.md first and resolve the current C/C2 live state from the supplied match state/market.`

## Retired material

Historical C3/C4 specifications/source remain documented under:

`models/football/retired/RETIREMENT_MANIFEST.md`

They are not current launchers or runtime requirements.
