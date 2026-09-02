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
- Current map: `Game 5`

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

## Games 1-4 settled summary

### Game 1
T1 Blue: `Jayce / Pantheon / Ryze / Kalista / Renata Glasc`
HLE Red: `Olaf / Lee Sin / Annie / Ashe / Seraphine`
Final: `T1 win`, `29:47`, kills `23-17` (`40 total`).
Positions: HLE ML LOSS; T1 +5.5 WIN; Under 33 WIN; Over 29.5 kills WIN.
G1 net: `+0.38075u`.

### Game 2
T1 Blue: `Gwen / Qiyana / Anivia / Jhin / Blitzcrank`
HLE Red: `K'Sante / Jarvan IV / Ahri / Yunara / Lulu`
Final: `T1 win`, `29:23`, kills `26-6` (`32 total`).
Positions: HLE ML LOSS; T1 +5.5 WIN; Over 32 LOSS; Under 30.5 kills LOSS.
G2 net: `-0.51025u`.

### Game 3
HLE Blue: `Camille / Sejuani / Akali / Miss Fortune / Shen`
T1 Red: `Kennen / Maokai / Yone / Kai'Sa / Alistar`
Final: `HLE win`, `25:41`, kills `18-9` (`27 total`).
Positions: T1 ML LOSS; T1 +5.5 LOSS; Under 32 WIN; Under 32.5 kills WIN.
G3 net: `-0.0105u`.

### Game 4
T1 Blue: `Aatrox / Skarner / Orianna / Lucian / Milio`
HLE Red: `Gragas / Xin Zhao / Cassiopeia / Varus / Nautilus`
Draft certification: `D=0 / EVEN-STYLE-DEPENDENT`.
Final: `HLE win`, `27:27`, kills `23-8` (`31 total`).
Positions: T1 ML LOSS; T1 +6.5 LOSS; Over 32 LOSS; Under 31.5 kills WIN.
G4 net: `-0.5770u`.
Micro-review: `PROBABILITY/CALIBRATION ERROR` for the KH cascade-risk estimate; the draft itself remained correctly uncertified at `D=0`.

HLE-T1 series forced-choice net through G4: `-0.7170u`.
Forced-choice cohort after G4: `24 Positions`, `11W-13L`, net `-0.9110u`.
By family after G4:
- ML `0-6 / -1.5000u`
- KH `3-3 / -0.0975u`
- Duration `4-2 / +0.3295u`
- Total Kills `4-2 / +0.3570u`

## Fearless consumed through Games 1-4
Unavailable in Game 5:
`Jayce / Pantheon / Ryze / Kalista / Renata Glasc / Olaf / Lee Sin / Annie / Ashe / Seraphine / Gwen / Qiyana / Anivia / Jhin / Blitzcrank / K'Sante / Jarvan IV / Ahri / Yunara / Lulu / Camille / Sejuani / Akali / Miss Fortune / Shen / Kennen / Maokai / Yone / Kai'Sa / Alistar / Aatrox / Skarner / Orianna / Lucian / Milio / Gragas / Xin Zhao / Cassiopeia / Varus / Nautilus`.

## Game 5 final draft
T1 Blue:
- Top: `Gnar`
- Jungle: `Naafiri`
- Mid: `Lissandra`
- ADC: `Jinx`
- Support: `Bard`

HLE Red:
- Top: `Ambessa`
- Jungle: `Cho'Gath`
- Mid: `Taliyah`
- ADC: `Caitlyn`
- Support: `Karma`

Fearless legality: `PASS`; all ten champions are outside the Games 1-4 consumed pool.
Live-state screenshot was supplied at 1:26, but per active mode all in-map state was ignored for prediction; only final draft and supplied board were used.

## Game 5 price-blind DIM

HLE mechanisms:
- PKM: `Caitlyn/Karma range and priority -> Taliyah zone/terrain denial -> Cho'Gath front control -> objective siege/catch`.
- SKM: `Ambessa side/flank access after HLE wins space, with Taliyah anti-dash punishment controlling T1's counter-entry`.

T1 mechanisms:
- PKM: `Bard pick/portal or Lissandra access -> Naafiri/Gnar collapse -> Jinx reset/chase`.
- SKM: `Gnar flank/terrain engage plus Bard ultimate to bypass HLE's front line and reach Caitlyn/Taliyah`.

`DIM[ROLES=P; TAM=SLIGHT_HLE; OSG=HLE; DAU=SLIGHT_HLE; SLI=EVEN; FNF=HLE; CAS=EVEN; ETS=SLIGHT_HLE; AFP=P; EDGE=SLIGHT_HLE]`

Interaction notes:
- HLE has a clear pre-contact objective-setup advantage from Caitlyn traps/range, Karma pressure and Taliyah terrain control.
- HLE has direct answers to T1's primary access: Taliyah anti-dash field, Cho'Gath CC/frontline and Karma spacing tools materially complicate Naafiri/Lissandra/Gnar entry.
- T1 still has a real alternative route through Bard ultimate/portal and Gnar flank, so the edge is not clear/strong.
- At least two independent HLE advantages survive AFP: objective setup geometry and threat-answer/damage-access fit.

Draft certification: `D=+1 HLE / SLIGHT HLE`.

### Moneyline pre-price
- `P0(HLE)=55%`
- `D=+1`
- `P(HLE)=59.5% / P(T1)=40.5%`

### Kill Handicap pre-price signed HLE-minus-T1 final kill-margin distribution
- `<= -5`: `17%`
- `-4 to 0`: `24%`
- `+1 to +4`: `19%`
- `+5 to +9`: `23%`
- `+10 or more`: `17%`

Derived at `HLE -4.5 / T1 +4.5`:
- `P(T1 +4.5 cover)=60%`
- `P(HLE -4.5 cover)=40%`

Rationale: HLE owns stronger setup but T1 retains multiple independent return-kill/pick routes through Bard, Lissandra and Jinx resets, preventing a stable wide HLE margin certificate.

### Duration pre-price
Draft-only clock scoring:
- `V=0`
- `Q=0`
- `H=+1`
- `T=+1`
- `F=32.75m`

Mechanism: HLE can siege rather than overforce, while T1 has Jinx/Lissandra waveclear and Bard reset tools; both compositions can extend neutral cycles if first access fails.

At line `32`:
- `P(Over 32)=55.25%`
- `P(Under 32)=44.75%`

### Total Kills pre-price
Primary baseline remains `TK0=28.9` from the frozen current-window HLE/T1 environments used in this series.

Draft-adjusted total-kill bins:
- `<20`: `6%`
- `20-24`: `13%`
- `25-29`: `25%`
- `30-34`: `29%`
- `35-39`: `18%`
- `40+`: `9%`

At `30.5`, using uniform interpolation within the 30-34 bin:
- `P(Over 30.5)≈50.2%`
- `P(Under 30.5)≈49.8%`

## Game 5 supplied board and forced-choice selections

Board:
- ML: `HLE 1.678 / T1 2.109`
- Duration: `Over 32 @1.869 / Under 32 @1.869`
- Total Kills: `Over 30.5 @1.974 / Under 30.5 @1.774`
- Kill Handicap: `HLE -4.5 @1.806 / T1 +4.5 @1.936`

Exactly one canonical line per family:
1. `HLE ML @1.678` — model `59.5%`, implied `59.59%`, `MODEL_EDGE≈-0.09pp`, `FORCED_NEG_EV=YES`.
2. `T1 +4.5 kills @1.936` — model `60.0%`, implied `51.65%`, `MODEL_EDGE≈+8.35pp`, `FORCED_NEG_EV=NO`.
3. `Over 32 minutes @1.869` — model `55.25%`, implied `53.50%`, `MODEL_EDGE≈+1.75pp`, `FORCED_NEG_EV=NO`.
4. `Over 30.5 total kills @1.974` — model `50.2%`, implied `50.66%`, `MODEL_EDGE≈-0.46pp`, `FORCED_NEG_EV=YES`.

All positions: `0.25u shadow / 0u actual`.
Total Game 5 shadow stake: `1.00u`.
Airtable deferred until map end.

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
- Current cohort before G5 settlement: `24 settled Positions / 6 samples per family` plus `4 open G5 Positions`.
