# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-02 08:00 UTC / 15:00 UTC+7`
- Series score: `T1 2-1 HLE`
- Game 1 winner: `T1`
- Game 2 winner: `T1`
- Game 3 winner: `HLE`
- Current map: `Game 4 prep`

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

## Game 2 final
T1 Blue: `Gwen / Qiyana / Anivia / Jhin / Blitzcrank`
HLE Red: `K'Sante / Jarvan IV / Ahri / Yunara / Lulu`

Price-blind draft verdict: `SLIGHT HLE`.
Final: `T1 win`, `29:23`, kills `26-6` (`32 total`).

Canonical G2 FORCED-CHOICE positions:
1. `HLE ML @1.590` — LOSS `-0.25u`
2. `T1 +5.5 kills @1.959` — WIN `+0.23975u`
3. `Over 32 minutes @1.908` — LOSS `-0.25u`
4. `Under 30.5 total kills @1.880` — LOSS `-0.25u`

G2: `1W-3L`, net `-0.51025u`.
Micro-review: `DRAFT READ ERROR` — HLE front-to-back was overcredited; T1 Blitzcrank/Qiyana/Anivia pick/choke control plus Gwen side-lane pressure produced a much larger clean-cascade branch than projected.

## Game 3 final draft
HLE Blue: `Camille / Sejuani / Akali / Miss Fortune / Shen`
T1 Red: `Kennen / Maokai / Yone / Kai'Sa / Alistar`

Price-blind draft verdict: `SLIGHT T1` (`D=-1` from HLE perspective).
Locked pre-price projections:
- ML: `HLE 50.5% / T1 49.5%`
- `T1 +5.5 cover ≈63%`
- duration `F≈29.5m`
- total kills central `~30.5`

Supplied board:
- ML: `HLE 1.586 / T1 2.275`
- Duration: `Over 32 @1.837 / Under 32 @1.902`
- Total Kills: `Over 32.5 @1.712 / Under 32.5 @2.056`
- Kill Handicap: `HLE -5.5 @1.733 / T1 +5.5 @2.027`

## Game 3 final
User supplied final screenshot:
- Winner: `HLE`
- Duration: `25:41`
- Kills: `HLE 18-9 T1` (`27 total`)
- HLE gold lead: `~9.7k`
- Towers: `8-3`
- Dragons: `4-0`
- Barons: `1-0`
- Inhibitors: `1-0`

### Game 3 FORCED-CHOICE settlement
All `0.25u shadow / 0u actual`:
1. `T1 ML @2.275` — LOSS `-0.25u`
2. `T1 +5.5 kills @2.027` — LOSS `-0.25u`
3. `Under 32 minutes @1.902` — WIN `+0.2255u`
4. `Under 32.5 total kills @2.056` — WIN `+0.264u`

G3: `2W-2L`, net `-0.0105u`.
HLE-T1 series forced-choice net through G3: `-0.1400u`.

Micro-review: `DRAFT READ ERROR` — T1's nominal neutral 5v5 ease was overcredited; HLE's Camille/Sejuani/Shen multi-angle dive, Akali follow-up, and Miss Fortune zone damage produced a stronger decisive-fight branch than projected.

## Fearless consumed through Games 1-3
Unavailable in Game 4:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine / Gwen / Qiyana / Anivia / Jhin / Blitzcrank / K'Sante / Jarvan IV / Ahri / Yunara / Lulu / Camille / Sejuani / Akali / Miss Fortune / Shen / Kennen / Maokai / Yone / Kai'Sa / Alistar`.

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
- Forced-choice checkpoint audit threshold of 10 positions has been exceeded; cohort checkpoint audit is due before making structural model changes.
- No structural model changes have been made; current lock remains frozen.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
