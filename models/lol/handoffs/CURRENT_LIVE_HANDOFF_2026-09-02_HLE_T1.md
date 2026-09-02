# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Series score: `T1 2-2 HLE`
- Game 1 winner: `T1`
- Game 2 winner: `T1`
- Game 3 winner: `HLE`
- Game 4 winner: `HLE`
- Current map: `Game 5 prep`

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

## Forced-choice checkpoint audit
Canonical review: `models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-02.md`.

Audit enforcement:
1. full DIM required;
2. `D=+/-1` only when at least two independent mechanism advantages survive DIM/AFP; otherwise `D=0 / EVEN-STYLE-DEPENDENT`;
3. full KH signed margin bins and TK total-kill bins before price;
4. persist implied probability, `MODEL_EDGE`, and `FORCED_NEG_EV=YES/NO`;
5. no structural coefficient changes yet.

Checkpoint at 20 canonical forced-choice Positions was `10W-10L / -0.3340u`.

## Game 4 draft and pre-price record
T1 Blue: `Aatrox / Skarner / Orianna / Lucian / Milio`
HLE Red: `Gragas / Xin Zhao / Cassiopeia / Varus / Nautilus`

Fearless legality: `PASS`.

`DIM[ROLES=P; TAM=EVEN; OSG=SLIGHT_HLE; DAU=EVEN; SLI=EVEN; FNF=PASS_BOTH; CAS=EVEN; ETS=SLIGHT_HLE; AFP=P; EDGE=EVEN_STYLE_DEPENDENT]`

Draft certification: `D=0 / EVEN-STYLE-DEPENDENT`.

Pre-price:
- ML: `HLE 55% / T1 45%`.
- KH HLE-minus-T1 bins: `<=-7 14%; -6..-1 31%; 0..+6 27%; +7..+12 18%; +13+ 10%`; `T1 +6.5 cover=72%`.
- Duration: `V=0,Q=0,H=+1,T=0,F=32.0m`.
- TK bins: `<20 8%; 20-24 15%; 25-29 27%; 30-34 28%; 35-39 15%; 40+ 7%`; central `~29.5`.

## Game 4 board / positions
1. `T1 ML @2.188` — model `45.0%`, implied `45.70%`, edge `-0.70pp`, `FORCED_NEG_EV=YES`.
2. `T1 +6.5 kills @1.831` — model `72.0%`, implied `54.62%`, edge `+17.38pp`, `FORCED_NEG_EV=NO`.
3. `Over 32 minutes @1.902` — model `50.0%`, implied `52.58%`, edge `-2.58pp`, `FORCED_NEG_EV=YES`.
4. `Under 31.5 total kills @1.692` — model `61.2%`, implied `59.10%`, edge `+2.10pp`, `FORCED_NEG_EV=NO`.

## Game 4 final
User final screenshot:
- Winner: `HLE`
- Duration: `27:27`
- Kills: `HLE 23-8 T1` (`31 total`)
- HLE gold lead: `~13k`
- Towers: `10-1`
- Dragons: `4-0`
- Barons: `1-0`
- Inhibitors: `1-0`

Settlement, all `0.25u shadow / 0u actual`:
1. `T1 ML @2.188` — LOSS `-0.25u`
2. `T1 +6.5 kills @1.831` — LOSS `-0.25u`
3. `Over 32 minutes @1.902` — LOSS `-0.25u`
4. `Under 31.5 total kills @1.692` — WIN `+0.173u`

G4: `1W-3L`, net `-0.5770u`.
HLE-T1 series forced-choice net through G4: `-0.7170u`.
Forced-choice cohort after G4: `24 Positions`, `11W-13L`, net `-0.9110u`.
By family after G4:
- ML `0-6 / -1.5000u`
- KH `3-3 / -0.0975u`
- Duration `4-2 / +0.3295u`
- Total Kills `4-2 / +0.3570u`

Micro-review: `PROBABILITY/CALIBRATION ERROR` for the KH cascade-risk estimate; the draft itself remained correctly uncertified at `D=0`. Keep forced-negative-EV ML/Duration losses separate from model-positive selections.

Airtable map and all four positions settled at map end.

## Fearless consumed through Games 1-4
Unavailable in Game 5:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine / Gwen / Qiyana / Anivia / Jhin / Blitzcrank / K'Sante / Jarvan IV / Ahri / Yunara / Lulu / Camille / Sejuani / Akali / Miss Fortune / Shen / Kennen / Maokai / Yone / Kai'Sa / Alistar / Aatrox / Skarner / Orianna / Lucian / Milio / Gragas / Xin Zhao / Cassiopeia / Varus / Nautilus`.

## Standing execution rule
- Enabled families: ML / Kill Handicap / Duration / Total Kills.
- Exactly one canonical line per market family; evaluate alternate lines but log one.
- No PASS in forced-choice mode.
- Ignore displayed match clock and all in-map state for prediction.
- Final draft + board is standing authorization.
- `0.25u shadow` per selected market / `0u actual`.
- Airtable only at map end.
- Verdict first; persistence must not delay user-visible picks.

## Audit cadence
- Micro-review every settled map.
- Next checkpoint at `40 canonical forced-choice Positions / 10 samples per family`.
- Current cohort: `24 Positions / 6 samples per family`.
