# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-09-02 08:00 UTC / 15:00 UTC+7`
- Series score: `0-0`
- Current map: `pre-series / Game 1 prep`

## Active authority
- Lock: `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Circuit breaker: `CLEAR`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Frozen benchmark
Current window: `LCK 2026 Rounds 3-4`; previous: `LCK 2026 Rounds 1-2`; normal 70/30 roster-continuous blend.

- `B_current(HLE)=+0.502`
- `B_current(T1)=-0.178`
- `B_previous(HLE)=+1.135`
- `B_previous(T1)=+0.902`
- `B_raw(HLE)=+0.692`
- `B_raw(T1)=+0.146`
- `B(HLE)=+0.941`
- `B(T1)=+0.199`
- `GAP(HLE-T1)=+0.742 SD`
- `HLE K=+1 / P0=55%`
- `T1 K=-1 / P0=45%`

Current core inputs:
- HLE: 21 games, WR 52.4%, GDM +56, GD@15 +596, towers 6.3-5.4, DRA 48.7%, NASH 49.1%.
- T1: 19 games, WR 42.1%, GDM +5, GD@15 +222, towers 5.7-6.1, DRA 50.3%, NASH 50.9%.

Previous core inputs:
- HLE: 43 games, WR 74.4%, GDM +188, GD@15 +883, towers 7.5-3.7, DRA 54.4%, NASH 71.7%.
- T1: 40 games, WR 75.0%, GDM +139, GD@15 +674, towers 6.9-4.4, DRA 53.9%, NASH 54.2%.

Same-series results and sportsbook prices do not update K/P0.

## Expected current fives
HLE:
- Zeus
- Kanavi
- Zeka
- Gumayusi
- Delight

T1:
- Doran
- Oner
- Faker
- Peyz
- Keria

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
