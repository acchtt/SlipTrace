# Current Live Handoff — Nongshim Esports Academy vs DN SOOPers Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `Nongshim Esports Academy vs DN SOOPers Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `NS.C 2-1 DNS.C`
- Game 1 winner: `NS Challengers`
- Game 2 winner: `DNS Challengers`
- Game 3 winner: `NS Challengers`
- Next map: `Game 4 prep`

## Active authority
- Lock: `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-FORCEDCHOICE`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Forced-choice rule — ACTIVE prospectively
User instruction: `take all available markets, no more pass`.

For every executable offered enabled market:
- Moneyline: choose one side;
- Kill Handicap: choose one side;
- Duration: choose Over or Under;
- Total Kills: choose Over or Under.

`PASS` is disabled. Old minimum-odds, edge, and selected-side thesis gates remain diagnostic metadata only, not execution vetoes. Price-blind projections are still locked before odds. After odds are seen, choose the better model-vs-book side; if both sides are negative EV, choose the less-negative side.

Standing authorization: a supplied board is enough to record all forced-choice shadow positions; no extra per-line confirmation required. Tag these positions `FORCED-CHOICE`. Keep them separate from threshold-qualified selective TAKE calibration. Airtable only at map end.

If a market lacks a clear two-sided executable quote or settlement semantics are unclear, use execution-data HOLD until clarified; do not substitute a model PASS.

## Frozen benchmark
- `B_current(NS)=+0.317`
- `B_current(DNS)=-0.690`
- `B_previous(NS)=+0.733`
- `B_previous(DNS)=+0.495`
- normal 70/30 roster-continuous blend
- `B_raw(NS)=+0.442`
- `B_raw(DNS)=-0.334`
- final `B(NS)=+0.550`
- final `B(DNS)=-0.417`
- `GAP(NS-DNS)=+0.967 SD`
- `NS.C K=+1 / P0=55%`
- `DNS.C K=-1 / P0=45%`

Same-series results/prices do not update K/P0.

## Game 1 — final
Winner: `NS Challengers`
Final duration: `26:37`
Final kills: `NS 26-5 DNS`
Final towers: `9-1`
Final dragons: `2-1`
Final Barons: `1-0`
Final inhibitors: `1-0`

Draft:
NS.C: Janus Olaf / MihawK Jarvan IV / SeTab Orianna / Lucy Ashe / Pleata Seraphine
DNS.C: Lancer Camille / DDoiV Lee Sin / Flip Galio / Enosh Yunara / Quantum Lulu

## Game 2
Winner: `DNS Challengers`.
Final duration/final detailed scoreboard not supplied. A screenshot at 38:33 while live showed DNS leading 23-21 kills; do not treat those live values as final settlement values.

Draft:
DNS.C: Lancer Rumble / DDoiV Skarner / Flip Tristana / Enosh Ezreal / Quantum Nautilus
NS.C: Janus K'Sante / MihawK Cho'Gath / SeTab Ryze / Lucy Lucian / Pleata Milio

## Game 3 — final
Winner: `NS Challengers`
Final duration: `24:49`
Final kills: `NS 22-7 DNS` (`29 total`)
Final towers: `10-2`
Final dragons: `3-0`
Final Barons: `1-0`
Final inhibitors: `2-0`

Draft:
NS.C: Janus Yorick / MihawK Qiyana / SeTab Locke / Lucy Kalista / Pleata Renata Glasc
DNS.C: Lancer Jayce / DDoiV Trundle / Flip Syndra / Enosh Jhin / Quantum Alistar

### Game 3 settled position — pre-forced-choice cohort
- `Over 31.5 total kills @1.653`
- 0.25u shadow / 0u actual
- Result: `LOSS`
- P/L: `-0.25u`
- Primary review: `PROBABILITY/CALIBRATION ERROR`

## Fearless consumed after Games 1-3
Unavailable to either side in Game 4:
`Olaf / Jarvan IV / Orianna / Ashe / Seraphine / Camille / Lee Sin / Galio / Yunara / Lulu / Rumble / Skarner / Tristana / Ezreal / Nautilus / K'Sante / Cho'Gath / Ryze / Lucian / Milio / Yorick / Qiyana / Locke / Kalista / Renata Glasc / Jayce / Trundle / Syndra / Jhin / Alistar`

## Game 4 workflow
1. Receive final Game 4 draft/roles plus exact board.
2. Ignore displayed match clock and all live-state stats.
3. Lock price-blind ML probability, KH margin distribution, duration F, and TK distribution.
4. Compare both sides of every offered enabled market.
5. Choose exactly one side for each executable offered market — no PASS.
6. Record all selected sides as `FORCED-CHOICE`, 0.25u shadow each / 0u actual, without additional confirmation.
7. Airtable only at map end.

## Audit cadence
- Micro-review every settled map.
- Forced-choice checkpoint audit after 10 forced-choice Positions total.
- Keep forced-choice cohort separate from old threshold-qualified selective calibration.
