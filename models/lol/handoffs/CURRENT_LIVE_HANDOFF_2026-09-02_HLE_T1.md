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
- Current map: `Game 4`

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

## Games 1-3 summary

### Game 1
T1 Blue: `Jayce / Pantheon / Ryze / Kalista / Renata Glasc`
HLE Red: `Olaf / Lee Sin / Annie / Ashe / Seraphine`
Draft verdict: `SLIGHT HLE`.
Final: `T1 win`, `29:47`, kills `23-17` (`40 total`).
Canonical positions:
1. `HLE ML @1.640` — LOSS `-0.25u`
2. `T1 +5.5 kills @1.860` — WIN `+0.215u`
3. `Under 33 minutes @1.692` — WIN `+0.173u`
4. `Over 29.5 total kills @1.971` — WIN `+0.24275u`
G1 net: `+0.38075u`.

### Game 2
T1 Blue: `Gwen / Qiyana / Anivia / Jhin / Blitzcrank`
HLE Red: `K'Sante / Jarvan IV / Ahri / Yunara / Lulu`
Draft verdict: `SLIGHT HLE`.
Final: `T1 win`, `29:23`, kills `26-6` (`32 total`).
Canonical positions:
1. `HLE ML @1.590` — LOSS `-0.25u`
2. `T1 +5.5 kills @1.959` — WIN `+0.23975u`
3. `Over 32 minutes @1.908` — LOSS `-0.25u`
4. `Under 30.5 total kills @1.880` — LOSS `-0.25u`
G2 net: `-0.51025u`.

### Game 3
HLE Blue: `Camille / Sejuani / Akali / Miss Fortune / Shen`
T1 Red: `Kennen / Maokai / Yone / Kai'Sa / Alistar`
Draft verdict: `SLIGHT T1`.
Final: `HLE win`, `25:41`, kills `18-9` (`27 total`).
Canonical positions:
1. `T1 ML @2.275` — LOSS `-0.25u`
2. `T1 +5.5 kills @2.027` — LOSS `-0.25u`
3. `Under 32 minutes @1.902` — WIN `+0.2255u`
4. `Under 32.5 total kills @2.056` — WIN `+0.264u`
G3 net: `-0.0105u`.

HLE-T1 forced-choice net through G3: `-0.1400u`.

## Fearless consumed through Games 1-3
Unavailable in Game 4:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine / Gwen / Qiyana / Anivia / Jhin / Blitzcrank / K'Sante / Jarvan IV / Ahri / Yunara / Lulu / Camille / Sejuani / Akali / Miss Fortune / Shen / Kennen / Maokai / Yone / Kai'Sa / Alistar`.

## Forced-choice checkpoint audit — COMPLETE 2026-09-02
Canonical review: `models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-02.md`.

Canonical forced-choice sample through G3:
- `20 Positions / 5 maps / 5 samples per family`
- overall `10W-10L`, `-0.3340u` on `5.00u` shadow stake, ROI `-6.68%`
- ML `0-5 / -1.2500u`
- KH `3-2 / +0.1525u`
- Duration `4-1 / +0.5795u`
- Total Kills `3-2 / +0.1840u`

Audit enforcement for new maps:
1. full DIM required;
2. `D=+/-1` only when at least two independent mechanism advantages survive DIM/AFP; otherwise `D=0 / EVEN-STYLE-DEPENDENT`;
3. full KH signed margin bins and TK total-kill bins before price;
4. store raw implied probability, selected-side `MODEL_EDGE`, and `FORCED_NEG_EV=YES/NO` after price;
5. no structural coefficient changes yet.

## Game 4 final draft
T1 Blue:
- Top: `Aatrox`
- Jungle: `Skarner`
- Mid: `Orianna`
- ADC: `Lucian`
- Support: `Milio`

HLE Red:
- Top: `Gragas`
- Jungle: `Xin Zhao`
- Mid: `Cassiopeia`
- ADC: `Varus`
- Support: `Nautilus`

Fearless legality: `PASS`; all ten champions are outside the Games 1-3 consumed pool.

## Game 4 price-blind DIM

HLE mechanisms:
- PKM: `Varus poke/root or Nautilus catch -> Xin Zhao/Gragas collapse -> Cassiopeia sustained zone/DPS`.
- SKM: `Gragas flank/displacement plus Cassiopeia choke control to force a front-to-back objective fight`.

T1 mechanisms:
- PKM: `Skarner catch/drag -> Orianna control/burst -> Aatrox follow-up and Lucian burst`.
- SKM: `Lucian+Milio ranged pressure with Orianna zone; Aatrox flank/side pressure`.

`DIM[ROLES=P; TAM=EVEN; OSG=SLIGHT_HLE; DAU=EVEN; SLI=EVEN; FNF=PASS_BOTH; CAS=EVEN; ETS=SLIGHT_HLE; AFP=P; EDGE=EVEN_STYLE_DEPENDENT]`

Interaction notes:
- HLE has strong pre-contact objective geometry from Varus range, Cassiopeia choke denial and Nautilus threat.
- T1 directly answers committed HLE catch with Milio cleanse/reset, Skarner counter-entry, Orianna zone and a durable Aatrox front.
- HLE directly answers T1's forward access with Gragas displacement, Xin Zhao ultimate, Cassiopeia Miasma and Nautilus hard CC.
- T1's Aatrox side route is not independent enough to certify a draft edge because Gragas can neutralize/waveclear and HLE can contest through ranged objective setup.
- AFP finds a repeatable route for each side but also a direct answer for each; fewer than two independent uncompensated advantages survive.

Draft certification: `D=0 / EVEN-STYLE-DEPENDENT`.

### Moneyline pre-price
- `P0(HLE)=55%`
- `D=0`
- `P(HLE)=55% / P(T1)=45%`

### Kill Handicap pre-price signed HLE-minus-T1 final kill-margin distribution
- `<= -7`: `14%`
- `-6 to -1`: `31%`
- `0 to +6`: `27%`
- `+7 to +12`: `18%`
- `+13 or more`: `10%`

Derived at `HLE -6.5 / T1 +6.5`:
- `P(T1 +6.5 cover)=72%`
- `P(HLE -6.5 cover)=28%`

### Duration pre-price
Draft-only clock scoring:
- `V=0`
- `Q=0`
- `H=+1`
- `T=0`
- `F=32.0m`

Mechanism: both sides have reliable waveclear/reset and durable objective-fight structures, creating meaningful terminal path depth rather than a certified fast-close profile.

At line `32`:
- `P(Over 32)=50%`
- `P(Under 32)=50%`

### Total Kills pre-price
Gol.gg current-window environments used pre-series:
- HLE: `13.9 kills/game + 16.9 deaths/game = 30.8`
- T1: `14.7 + 12.3 = 27.0`
- `TK0=28.9`

Draft-adjusted total-kill bins:
- `<20`: `8%`
- `20-24`: `15%`
- `25-29`: `27%`
- `30-34`: `28%`
- `35-39`: `15%`
- `40+`: `7%`

Approximate central expectation: `~29.5`.
Using uniform interpolation inside the `30-34` bin:
- at `31.5`: `Under ≈61.2% / Over ≈38.8%`
- at `30.5`: `Under ≈55.6% / Over ≈44.4%`

## Game 4 supplied board and forced-choice selections

Board:
- ML: `HLE 1.631 / T1 2.188`
- Duration: `Over 32 @1.902 / Under 32 @1.837`
- Total Kills: `Over 31.5 @2.086 / Under 31.5 @1.692`; alternate `Over 30.5 @1.971 / Under 30.5 @1.776`
- Kill Handicap: `HLE -6.5 @1.908 / T1 +6.5 @1.831`

Exactly one canonical line per family:
1. `T1 ML @2.188` — model `45.0%`, implied `45.70%`, `MODEL_EDGE=-0.70pp`, `FORCED_NEG_EV=YES`.
2. `T1 +6.5 kills @1.831` — model `72.0%`, implied `54.62%`, `MODEL_EDGE=+17.38pp`, `FORCED_NEG_EV=NO`.
3. `Over 32 minutes @1.902` — model `50.0%`, implied `52.58%`, `MODEL_EDGE=-2.58pp`, `FORCED_NEG_EV=YES`; selected over Under because the locked clock is exactly 32.0 and Over is the less-negative side at the supplied prices.
4. `Under 31.5 total kills @1.692` — model `61.2%`, implied `59.10%`, `MODEL_EDGE=+2.10pp`, `FORCED_NEG_EV=NO`; this is the canonical TK line versus the weaker 30.5 alternatives.

All positions: `0.25u shadow / 0u actual`.
Total Game 4 shadow stake: `1.00u`.
Airtable deferred until map end.

## Standing execution rule
- Enabled families: ML / Kill Handicap / Duration / Total Kills.
- Exactly one canonical line per market family; if alternate lines exist within the same family, evaluate all but log only the best model-vs-book line.
- No PASS in forced-choice mode.
- Ignore displayed match clock and all in-map state for prediction.
- Final draft + board is standing authorization.
- `0.25u shadow` per selected market / `0u actual`.
- Airtable only at map end.
- Persist full post-audit distributions and forced-negative-EV flag before settlement.

## Audit cadence
- Micro-review every settled map.
- Next checkpoint at `40 canonical forced-choice Positions / 10 samples per family`.
- No structural model changes have been made; current lock remains frozen.
