# Football V4 — current command entrypoints

**Authority:** `models/football/CURRENT_MODEL.md` and
`models/football/prompts/COMMAND_ALIASES.md` on the current production main.
Football C official, C2 independent shadow. C3/C4 retired.

| Command | Canonical current launcher | Stage |
|---|---|---|
| `/sweep` | `models/football/stages_v4/SWEEP.md` | Current senior fixture discovery and goals-first admission |
| `/rank` | `models/football/stages_v4/RANK.md` | Original-source V4 rank with refreshed full-cohort status, C+C2 |
| `/xi`, `/xi exception` | `models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md` | C+C2 football first, user screenshot as sole market price |
| `/live` | `models/football/prompts/03_NORMAL_CHAT_LIVE.md` | Live football first, original screenshot as limited live price evidence |
| `/audit` | `models/football/prompts/04_WORK_POST_SLATE_AUDIT.md` | Frozen-state audit (V4 intake and C/C2) |
| `/report` | `models/football/prompts/06_NORMAL_CHAT_REPORT.md` | Read-only active Airtable/report and user Actual Bets |

## Mandatory execution boundaries

- V4 /sweep first proves bounded provider-surface completeness: every ICT+UTC date surface touched by the window, all pages, all senior competition blocks, exact fixture-ID union and an independent terminal sentinel. New sources require `source_completeness_manifest` / `DATE_SURFACE_BATCH_V2`; registry filtering before this proof is forbidden. It then creates original `source.json` and a native `V4_SWEEP_READY` receipt. A digest alone is **not** an independent source attestation; use source-attested GitHub Actions artifacts when available.
- V4 /rank replays the unchanged original source, and requires a fresh same-match status/kickoff observation for the **entire eligible cohort** before C and C2 execute. Historical old rank bundles and V1–V3 ZIPs cannot be imported as V4 authority.
- V4 /xi uses independently executed football C/C2 and no mandatory odds; if a user screenshot is supplied, **no external replacement or historical market price search** is permitted. An original screenshot cannot by itself prove an executable market offer. Price verdicts are conditional, not placed bets.
- Live screenshots use their displayed score/minute and original price only, never a prematch priced action after kickoff.
- Current read/write model base: `appbzxqXYf0lKfD4P`. User profit comes only from `Actual Bets — Current`; C2 shadow is not official exposure.
- CI engine success does not prove live provider acquisition or actual betting/execution availability.

## Explicitly retired entrypoints

`prompts/00_NORMAL_CHAT_AISCORE_FETCH.md`, `01_WORK_DAILY_SWEEP.md`,
legacy `prompts/sweep.md`, `prompts/rank.md`, the old V1–V3 CLIs,
`FOOTBALL_SWEEP_RANK_UNIFIED_V3.md`, and the old XI coordinator are historical
references only. Their old "active" flags, caps, venue/odds requirements, or
Football A claims never supersede these V4 launchers.
