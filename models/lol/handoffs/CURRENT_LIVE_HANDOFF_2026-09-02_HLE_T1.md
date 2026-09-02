# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-02 08:00 UTC / 15:00 UTC+7`
- Series score: `0-0`
- Current map: `Game 1`

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

## Game 1 final draft
T1 Blue:
- Jayce
- Pantheon
- Ryze
- Kalista
- Renata Glasc

HLE Red (user typed "geng" for second side; board is HLE vs T1, so interpreted as HLE):
- Olaf
- Lee Sin
- Annie
- Ashe
- Seraphine

## Game 1 price-blind read
Draft verdict: `SLIGHT HLE` (`D=+1` from HLE perspective).

Mechanism:
- HLE has the more reliable layered catch/teamfight chain through Ashe arrow, Annie stun, Seraphine follow-up and Lee Sin displacement, with Olaf difficult for T1's CC-heavy composition to contain once committed.
- T1 has strong early skirmish/tempo through Pantheon + Kalista + Renata, Jayce poke, and Ryze global access, so HLE's edge is slight rather than major.
- T1 lacks a durable conventional frontline, increasing its clean-collapse risk if the first engage is absorbed or turned.

Moneyline before price:
- `P0(HLE)=55%`
- `D=+1`
- `P(HLE)=59.5% / P(T1)=40.5%`

Kill Handicap before price:
- locked approximation: `HLE by 6+ 46% / HLE by 1-5 21% / T1 by 0-5 20% / T1 by 6+ 13%`.
- therefore `T1 +5.5 cover ≈54%`; `HLE -5.5 cover ≈46%`.

Duration before price:
- draft-only score `V=+1, Q=0, H=0, T=+1`
- `F≈30.25m`
- at line 33: `Under ≈69.25% / Over ≈30.75%`.

Total Kills before price:
- baseline centered around high-20s using available LCK team kill/death environments, then adjusted upward for Pantheon/Kalista/Renata early forcing plus Ashe/Annie/Lee catch frequency.
- locked central total-kill expectation `~30.5`.
- line 29.5: `Over ≈57% / Under ≈43%`.
- line 28.5: `Over ≈62% / Under ≈38%`.

## Game 1 supplied board
- ML: `HLE 1.640 / T1 2.171`
- Duration: `Over 33 @2.086 / Under 33 @1.692`
- Total Kills 29.5: `Over @1.971 / Under @1.776`
- Total Kills 28.5: `Over @1.719 / Under @2.047`
- Kill Handicap: `HLE -5.5 @1.877 / T1 +5.5 @1.860`

## Game 1 FORCED-CHOICE positions — OPEN
All `0.25u shadow / 0u actual` under standing authorization.

1. `HLE ML @1.640`
2. `T1 +5.5 kills @1.860`
3. `Under 33 minutes @1.692`
4. `Over 29.5 total kills @1.971`
5. `Over 28.5 total kills @1.719`

Total shadow stake this map: `1.25u`; actual exposure `0u`.

Airtable deferred to map end.

## Fearless tracking
Game 1 consumes after settlement:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine`.

## Audit cadence
- Micro-review every settled map.
- Forced-choice checkpoint audit after 10 forced-choice Positions total.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
