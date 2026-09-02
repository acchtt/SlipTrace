# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-02 08:00 UTC / 15:00 UTC+7`
- Current map: `Game 2`
- Current screenshot indicates `T1 leads 1-0`; exact Game 1 final settlement details are not fully supplied, so keep G1 duration settlement pending.

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
T1 Blue: `Jayce / Pantheon / Ryze / Kalista / Renata Glasc`

HLE Red: `Olaf / Lee Sin / Annie / Ashe / Seraphine`

Game 1 price-blind draft verdict: `SLIGHT HLE` (`D=+1` from HLE perspective).

### Game 1 FORCED-CHOICE positions — settlement not fully completed
All `0.25u shadow / 0u actual`:
1. `HLE ML @1.640`
2. `T1 +5.5 kills @1.860`
3. `Under 33 minutes @1.692`
4. `Over 29.5 total kills @1.971`
5. `Over 28.5 total kills @1.719`

The Game 2 board screenshot appears to show T1 leading the series 1-0 and prior-game kill totals consistent with HLE 17 / T1 23, but exact Game 1 duration was not supplied; do not fabricate the missing settlement field.

## Fearless consumed after Game 1
Unavailable in Game 2:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine`.

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

All ten champions are outside the Game 1 consumed pool.

## Game 2 price-blind read
Draft verdict: `SLIGHT HLE` (`D=+1` from HLE perspective).

Mechanism:
- HLE has the cleaner front-to-back structure through K'Sante + Jarvan IV, with Ahri pick access and Yunara/Lulu as the protected sustained-damage core.
- T1 has dangerous pick/choke control through Blitzcrank + Qiyana + Anivia and strong side-lane scaling through Gwen, but Jhin provides less sustained tank damage into HLE's front line and the composition is more execution/pick dependent.
- Anivia can materially disrupt Jarvan engage and T1 can win through catches before setup, so HLE's edge is slight rather than major.

Moneyline before price:
- `P0(HLE)=55%`
- `D=+1`
- `P(HLE)=59.5% / P(T1)=40.5%`

Kill Handicap before price:
- locked approximation: `HLE by 6+ ~44% / HLE by 1-5 ~23% / T1 by 0-5 ~22% / T1 by 6+ ~11%`.
- therefore `T1 +5.5 cover ~56%`; `HLE -5.5 cover ~44%`.

Duration before price:
- draft-only score `V=0, Q=+1, H=0, T=+1`
- `F≈32.75m`
- at line 32: `Over ≈55.25% / Under ≈44.75%`.

Total Kills before price:
- baseline remains high-20s, but Anivia waveclear/control and HLE's durable front line suppress pure two-sided brawl realization despite Blitz/Qiyana/Ahri pick access.
- locked central total-kill expectation `~29`.
- at line 30.5: `Under ≈58% / Over ≈42%`.

## Game 2 supplied board
- ML: `HLE 1.590 / T1 2.265`
- Duration: `Over 32 @1.908 / Under 32 @1.831`
- Total Kills: `Over 30.5 @1.858 / Under 30.5 @1.880`
- Kill Handicap: `HLE -5.5 @1.787 / T1 +5.5 @1.959`

## Game 2 FORCED-CHOICE positions — OPEN
All `0.25u shadow / 0u actual` under standing authorization.

1. `HLE ML @1.590`
2. `T1 +5.5 kills @1.959`
3. `Over 32 minutes @1.908`
4. `Under 30.5 total kills @1.880`

Total Game 2 shadow stake: `1.00u`; actual exposure `0u`.

Airtable deferred to map end.

## Audit cadence
- Micro-review every settled map.
- Forced-choice checkpoint audit after 10 forced-choice Positions total.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
