# Football V4 — current command entrypoints

**Authority:** `models/football/CURRENT_MODEL.md` and
`models/football/prompts/COMMAND_ALIASES.md`.

**Official model:** Football C only. C2/C3/C4 are retired and audit-only.

| Command | Canonical launcher | Surface |
|---|---|---|
| `/sweep` | `models/football/stages_v4/SWEEP.md` | **Normal chat** |
| `/rank` | `models/football/stages_v4/RANK.md` | **ChatGPT Work** |
| `/xi`, `/xi exception` | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` | **Normal chat** |
| `/live` | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` | **Normal chat** |
| `/audit` | `models/football/prompts/04_NORMAL_CHAT_AUDIT.md` | **Normal chat** |
| `/audit deep` | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` | **ChatGPT Work; escalation only** |
| `/report` | `models/football/prompts/06_NORMAL_CHAT_REPORT.md` | **Normal chat** |

Normal `/sweep` first obtains a canonical source-only bundle and status
`SOURCE_READY_FOR_RESEARCH`, then finishes targeted upstream research and emits
the same native V4 handoff consumed by Work `/rank`. If local acquisition is
unavailable, the dedicated `football-v4-normal-source.yml` backend performs
source acquisition only. A RESEARCH_PENDING checkpoint is not a completed
sweep, and manual fixture research cannot replace the source gate.

Normal `/xi` is an interaction surface only: official ACT/WAIT/PASS remains
owned by the deterministic Football C runtime. When direct execution is
unavailable, use the on-demand GitHub XI request/result bridge and consume its
persisted result in the same turn. Do not return ANALYSIS_ONLY merely because
local Python is unavailable.

Normal `/live` uses current-epoch Football C assessment. A live priced action
exists only where a promoted deterministic live policy explicitly authorizes it.

Normal `/audit` is the default audit route and should inspect only the relevant
frozen evidence. The user does not need to choose a deep mode. If a repeated or
structural implementation defect requires repository-wide inspection or tests,
normal audit emits `DEEP AUDIT REQUIRED` plus a compact handoff for Work
`/audit deep`.

Google Sheets `Football v2 — Active Operations`
(`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`) is the active store.
User physical P/L comes only from `Actual Bets — Current`.

Legacy Work sweep, V1–V3 ZIP/checkpoint flows, Football A execution, Airtable
production routing, and C2/C3/C4 production routes are historical only.
