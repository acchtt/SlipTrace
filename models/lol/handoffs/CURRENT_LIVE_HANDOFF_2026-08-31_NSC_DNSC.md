# Current Live Handoff — Nongshim Esports Academy vs DN SOOPers Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `Nongshim Esports Academy vs DN SOOPers Challengers`
- Format: `Bo5 Fearless Draft`
- Series score: `NS.C 2-2 DNS.C`
- Game 1 winner: `NS Challengers`
- Game 2 winner: `DNS Challengers`
- Game 3 winner: `NS Challengers`
- Game 4 winner: `DNS Challengers`
- Next map: `Game 5 prep`

## Active authority
- Lock: `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-FORCEDCHOICE`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Forced-choice rule — ACTIVE
For every executable offered enabled market, choose exactly one side for Moneyline, Kill Handicap, Duration, and Total Kills. `PASS` is disabled. Price-blind projections are still locked before odds. Forced-choice positions remain a separate experimental cohort from threshold-qualified selective calibration. Airtable writes occur at map end.

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

## Game 4 — final
User confirmed the supplied 28:56 scoreboard as final.

Winner: `DNS Challengers`
Final duration: `28:56`
Final kills: `DNS 18-7 NS` (`25 total`)
Final towers: `DNS 9-4 NS`
Final dragons: `DNS 4-1 NS`
Final Barons: `DNS 0-1 NS`

Draft:
DNS.C (Blue): Lancer Renekton / DDoiV Sylas / Flip Viktor / Enosh Kai'Sa / Quantum Neeko
NS.C (Red): Janus Gnar / MihawK Maokai / SeTab Yone / Lucy Caitlyn / Pleata Karma

Price-blind draft read was `SLIGHT NS.C` (`D=+1` from NS perspective).

### Game 4 FORCED-CHOICE settlements
1. `NS.EA ML @1.640` — LOSS — `-0.25u`
2. `DNS.C +5.5 kills @1.791` — WIN — `+0.19775u`
3. `Under 32 @1.648` — WIN — `+0.162u`
4. `Over 31.5 total kills @1.602` — LOSS — `-0.25u`

Game 4 forced-choice net: `-0.14025u`
Forced-choice cohort after first 4 positions: `2W-2L / -0.14025u`

Primary micro-review: `PROBABILITY/CALIBRATION ERROR` — Total Kills Over 31.5 missed for a second consecutive accepted TK decision. The model continues to over-weight two-sided kill realization in fast one-sided/cascade outcomes. ML loss is noted, but one map alone does not justify a separate structural draft rewrite.

## Fearless consumed after Games 1-4
Unavailable to either side in Game 5:
`Olaf / Jarvan IV / Orianna / Ashe / Seraphine / Camille / Lee Sin / Galio / Yunara / Lulu / Rumble / Skarner / Tristana / Ezreal / Nautilus / K'Sante / Cho'Gath / Ryze / Lucian / Milio / Yorick / Qiyana / Locke / Kalista / Renata Glasc / Jayce / Trundle / Syndra / Jhin / Alistar / Renekton / Sylas / Viktor / Kai'Sa / Neeko / Gnar / Maokai / Yone / Caitlyn / Karma`

## Game 5 workflow
1. Receive final Game 5 draft/roles plus exact board.
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
