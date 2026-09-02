# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-02 08:00 UTC / 15:00 UTC+7`
- Series score: `T1 2-0 HLE`
- Game 1 winner: `T1`
- Game 2 winner: `T1`
- Current map: `Game 3 prep`

## Active authority
- Lock: `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Circuit breaker: `CLEAR`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Frozen benchmark
- `B(HLE)=+0.941`
- `B(T1)=+0.199`
- `GAP(HLE-T1)=+0.742 SD`
- `HLE K=+1 / P0=55%`
- `T1 K=-1 / P0=45%`

Same-series results and sportsbook prices do not update K/P0.

## Game 1 final
T1 Blue: `Jayce / Pantheon / Ryze / Kalista / Renata Glasc`
HLE Red: `Olaf / Lee Sin / Annie / Ashe / Seraphine`

Price-blind draft verdict: `SLIGHT HLE`.
Final: `T1 win`, `29:47`, kills `23-17` (`40 total`).

Canonical G1 FORCED-CHOICE positions, one line per market family:
1. `HLE ML @1.640` — LOSS `-0.25u`
2. `T1 +5.5 kills @1.860` — WIN `+0.215u`
3. `Under 33 minutes @1.692` — WIN `+0.173u`
4. `Over 29.5 total kills @1.971` — WIN `+0.24275u`

G1: `3W-1L`, net `+0.38075u`.
Micro-review: `DRAFT READ ERROR` — T1 tempo/map-pressure branches were underweighted.

## Game 2 final draft
T1 Blue:
- Gwen
- Qiyana
- Anivia
- Jhin
- Blitzcrank

HLE Red:
- K'Sante
- Jarvan IV
- Ahri
- Yunara
- Lulu

Price-blind draft verdict: `SLIGHT HLE`.
Locked pre-price projections:
- HLE ML `59.5%`
- T1 +5.5 cover `~56%`
- duration `F≈32.75m`
- total kills central `~29`

Supplied board:
- ML: `HLE 1.590 / T1 2.265`
- Duration: `Over 32 @1.908 / Under 32 @1.831`
- Total Kills: `Over 30.5 @1.858 / Under 30.5 @1.880`
- Kill Handicap: `HLE -5.5 @1.787 / T1 +5.5 @1.959`

## Game 2 final
User supplied final screenshot:
- Winner: `T1`
- Displayed final-state clock: `29:23`
- Kills: `T1 26-6 HLE` (`32 total`)
- T1 gold lead: `~15k`
- Towers: `10-0`
- Dragons: `2-1`
- Barons: `1-0`
- Inhibitors: `2-0`

### Game 2 FORCED-CHOICE settlement
All `0.25u shadow / 0u actual`:
1. `HLE ML @1.590` — LOSS `-0.25u`
2. `T1 +5.5 kills @1.959` — WIN `+0.23975u`
3. `Over 32 minutes @1.908` — LOSS `-0.25u`
4. `Under 30.5 total kills @1.880` — LOSS `-0.25u`

G2: `1W-3L`, net `-0.51025u`.
HLE-T1 series forced-choice net through G2: `-0.12950u`.

Micro-review: `DRAFT READ ERROR` — HLE front-to-back was overcredited; T1 Blitzcrank/Qiyana/Anivia pick/choke control plus Gwen side-lane pressure produced a much larger clean-cascade branch than projected.

## Fearless consumed through Games 1-2
Unavailable in Game 3:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine / Gwen / Qiyana / Anivia / Jhin / Blitzcrank / K'Sante / Jarvan IV / Ahri / Yunara / Lulu`.

## Standing execution rule
- Enabled families: ML / Kill Handicap / Duration / Total Kills.
- Exactly one canonical line per market family; if alternate lines exist within the same family, evaluate all but log only the best model-vs-book line.
- No PASS in forced-choice mode.
- Ignore displayed match clock and all in-map state for prediction.
- Final draft + board is standing authorization.
- `0.25u shadow` per selected market / `0u actual`.
- Airtable only at map end.

## Audit cadence
- Micro-review every settled map.
- Forced-choice checkpoint audit threshold of 10 positions has now been exceeded; cohort checkpoint audit is due before making structural model changes.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
