# Current Live Handoff — Nongshim Esports Academy vs DN SOOPers Challengers — 2026-08-31

**State only — not analytical authority**

## Series
- Competition: `LCK CL 2026 Season`
- Stage: `Playoffs — Upper Round 1`
- Match: `Nongshim Esports Academy vs DN SOOPers Challengers`
- Format: `Bo5 Fearless Draft`
- Scheduled: `2026-08-31 17:30 KST / 15:30 UTC+7`
- Series score: `NS.C 2-1 DNS.C`
- Game 1 winner: `NS Challengers`
- Game 2 winner: `DNS Challengers`
- Game 3 winner: `NS Challengers`
- Next map: `Game 4 prep`

## Active authority
- Lock: `LOL-2026-08-31-V13-NSC-DNSC-DRAFTONLY-1715-UTC7`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY INPUTS / IGNORE DISPLAYED MATCH CLOCK`
- Actual exposure: `0u`
- Shadow stake: `0.25u`
- ML min odds `1.50`, edge `+5.0pp`
- KH / Duration / Total Kills min odds `1.60`, edge `+7.5pp`
- Price cannot create the bet.

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
NS.C:
- Janus — Yorick
- MihawK — Qiyana
- SeTab — Locke
- Lucy — Kalista
- Pleata — Renata Glasc

DNS.C:
- Lancer — Jayce
- DDoiV — Trundle
- Flip — Syndra
- Enosh — Jhin
- Quantum — Alistar

Price-blind draft verdict was `SLIGHT NS.C` (`D=+1` from NS perspective).

### Game 3 settled position
- Position ID: `LCKCL-2026-08-31-NSC-DNSC-G3-TK-O31.5`
- Market: `Total Kills`
- Selection: `Over 31.5 total kills`
- Odds: `1.653`
- Model probability at decision: `~69%`
- Book implied: `60.50%`
- Estimated edge: `~+8.5pp`
- Shadow stake: `0.25u`
- Actual exposure: `0u`
- Result: `LOSS`
- P/L: `-0.25u`

Primary review: `PROBABILITY/CALIBRATION ERROR` — the Total Kills model over-weighted expected two-sided contact/return kills and underweighted a fast one-sided NS clean-cascade branch. Final was only 29 kills despite the high TK0 baseline.

## Fearless consumed after Games 1-3
Unavailable to either side in Game 4:
`Olaf / Jarvan IV / Orianna / Ashe / Seraphine / Camille / Lee Sin / Galio / Yunara / Lulu / Rumble / Skarner / Tristana / Ezreal / Nautilus / K'Sante / Cho'Gath / Ryze / Lucian / Milio / Yorick / Qiyana / Locke / Kalista / Renata Glasc / Jayce / Trundle / Syndra / Jhin / Alistar`

## Game 4 workflow
1. Receive final Game 4 draft/roles plus exact board.
2. Ignore displayed match clock and all live-state stats.
3. Complete price-blind DIM + ML/KH/Duration/TK projections.
4. Compare exact offered lines/odds.
5. Compact verdict first.
6. Exact user confirmation before accepted shadow Position.
7. Airtable only at map end.

## Audit cadence
- Micro-review every settled map.
- Checkpoint audit after 10 accepted postdraft bets total.
- Formal calibration/model audit after 20-30 accepted bets per market family unless procedural bug requires immediate repair.
