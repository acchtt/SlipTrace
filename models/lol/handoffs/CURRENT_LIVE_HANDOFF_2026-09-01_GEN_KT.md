# Current Live Handoff — Gen.G vs KT Rolster — 2026-09-01

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `ROUND2 / Upper Bracket Semifinal`
- Match: `Gen.G vs KT Rolster`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-01 08:00 UTC / 15:00 UTC+7`
- Series score: `0-0`
- Current map: `pre-series / Game 1 prep`

## Active authority
- Lock: `LOL-2026-09-01-V13-GEN-KT-DRAFTONLY-FORCEDCHOICE-1335-UTC7`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Circuit breaker: `CLEAR`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Frozen benchmark
Current window: `LCK 2026 Rounds 3-4`; previous: `LCK 2026 Rounds 1-2`; normal 70/30 roster-continuous blend.

- `B_current(GEN)=+1.044`
- `B_current(KT)=-1.458`
- `B_previous(GEN)=+1.253`
- `B_previous(KT)=+0.503`
- `B_raw(GEN)=+1.107`
- `B_raw(KT)=-0.870`
- `B(GEN)=+1.505`
- `B(KT)=-1.183`
- `GAP(GEN-KT)=+2.688 SD`
- `Gen.G K=+2 / P0=60%`
- `KT Rolster K=-2 / P0=40%`

Current core inputs:
- GEN: 19 games, WR 63.2%, GDM +91, GD@15 +638, towers 6.5-5.3, DRA 55.6%, NASH 48.0%.
- KT: 21 games, WR 38.1%, GDM -167, GD@15 -715, towers 4.5-7.3, DRA 41.7%, NASH 41.7%.

Previous core inputs:
- GEN: 41 games, WR 73.2%, GDM +228, GD@15 +897, towers 7.6-3.8, DRA 64.2%, NASH 72.6%.
- KT: 41 games, WR 63.4%, GDM +46, GD@15 +566, towers 6.5-5.0, DRA 52.6%, NASH 53.8%.

Same-series results and sportsbook prices do not update K/P0. KT's 3-0 Round 1 win over DK is context only and does not replace the frozen benchmark.

## Expected current fives
Gen.G:
- Kiin
- Canyon
- Chovy
- Ruler
- Duro

KT Rolster:
- PerfecT
- Cuzz
- Bdd
- Jiwoo
- Effort

User-supplied draft/scoreboard overrides public roster context if different.

## Forced-choice execution rule
For every executable offered enabled market, choose exactly one side:
- Moneyline
- Kill Handicap
- Duration
- Total Kills

No PASS. Price-blind projections are locked before odds. If both quoted sides are negative EV, choose the less-negative side. A supplied final draft + board is standing authorization for all selected positions. Tag each `FORCED-CHOICE`; 0.25u shadow / 0u actual. Airtable only at map end.

## Game 1 Fearless pool
Empty before Game 1. Track all 10 selected champions after settlement for Game 2.

## Workflow
1. Receive final G1 draft/roles + exact board.
2. Ignore displayed match clock and all live-state stats.
3. Lock draft/DIM, ML probability, KH margin distribution, duration F, TK distribution.
4. Choose one side in every executable offered market.
5. Record positions in handoff immediately; Airtable at map end.

## Audit cadence
- Micro-review every settled map.
- Forced-choice checkpoint audit after 10 forced-choice Positions total.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
