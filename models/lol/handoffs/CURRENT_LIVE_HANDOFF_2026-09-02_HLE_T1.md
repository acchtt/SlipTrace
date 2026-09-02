# Current Live Handoff — Hanwha Life Esports vs T1 — 2026-09-02

**State only — not analytical authority**

## Series final
- Competition: `LCK 2026 Season Playoffs`
- Stage: `Upper Bracket Round 2`
- Match: `Hanwha Life Esports vs T1`
- Format: `Bo5 Fearless Draft`
- Final series score: `HLE 3-2 T1`
- Winners by map: `G1 T1 / G2 T1 / G3 HLE / G4 HLE / G5 HLE`
- Series status: `COMPLETE`

## Active authority used
- Lock: `LOL-2026-09-02-V13-HLE-T1-DRAFTONLY-FORCEDCHOICE-1459-UTC7`
- Authority commit: `3e11a3a2b94a710dbc2d9ef16d88c3ac4ea0335c`
- Mode: `POSTDRAFT-ONLY / IGNORE DISPLAYED CLOCK / FORCE ONE SIDE PER OFFERED MARKET`
- Actual exposure: `0u`
- Shadow stake: `0.25u per market`

## Frozen benchmark
- `B(HLE)=+0.941`
- `B(T1)=+0.199`
- `GAP(HLE-T1)=+0.742 SD`
- `HLE K=+1 / P0=55%`
- `T1 K=-1 / P0=45%`

Same-series results and sportsbook prices did not update K/P0.

## Checkpoint-audit enforcement
Canonical review: `models/lol/reviews/LOL_FORCED_CHOICE_CHECKPOINT_AUDIT_2026-09-02.md`.

For post-audit maps:
1. full DIM required;
2. `D=+/-1` only when at least two independent mechanism advantages survive DIM/AFP; otherwise `D=0 / EVEN-STYLE-DEPENDENT`;
3. full KH signed margin bins and TK total-kill bins before price;
4. persist implied probability, `MODEL_EDGE`, and `FORCED_NEG_EV=YES/NO`;
5. no structural coefficient changes yet.

## Game 5 final draft
T1 Blue: `Gnar / Naafiri / Lissandra / Jinx / Bard`
HLE Red: `Ambessa / Cho'Gath / Taliyah / Caitlyn / Karma`
Fearless legality: `PASS`.

`DIM[ROLES=P; TAM=SLIGHT_HLE; OSG=HLE; DAU=SLIGHT_HLE; SLI=EVEN; FNF=HLE; CAS=EVEN; ETS=SLIGHT_HLE; AFP=P; EDGE=SLIGHT_HLE]`

Draft certification: `D=+1 HLE / SLIGHT HLE`.

Pre-price records:
- ML: `P0(HLE)=55%`, `P(HLE)=59.5% / T1 40.5%`.
- KH HLE-minus-T1 bins: `<=-5 17%; -4..0 24%; +1..+4 19%; +5..+9 23%; +10+ 17%`; `T1 +4.5 cover=60%`.
- Duration: `V=0,Q=0,H=+1,T=+1,F=32.75m`; `Over32=55.25%`.
- TK bins: `<20 6%; 20-24 13%; 25-29 25%; 30-34 29%; 35-39 18%; 40+ 9%`; `Over30.5≈50.2%`.

## Game 5 board / canonical positions
1. `HLE ML @1.678` — model `59.5%`, implied `59.59%`, edge `-0.09pp`, `FORCED_NEG_EV=YES`.
2. `T1 +4.5 kills @1.936` — model `60.0%`, implied `51.65%`, edge `+8.35pp`, `FORCED_NEG_EV=NO`.
3. `Over 32 minutes @1.869` — model `55.25%`, implied `53.50%`, edge `+1.75pp`, `FORCED_NEG_EV=NO`.
4. `Over 30.5 total kills @1.974` — model `50.2%`, implied `50.66%`, edge `-0.46pp`, `FORCED_NEG_EV=YES`.

## Game 5 final
User supplied final screenshot:
- Winner: `HLE`
- Duration: `28:01`
- Kills: `HLE 22-9 T1` (`31 total`)
- HLE gold lead: `~7.2k`
- Towers: `6-2`
- Dragons: `4-0`
- Barons: `1-0`
- Inhibitors: `1-0`

Settlement, all `0.25u shadow / 0u actual`:
1. `HLE ML @1.678` — WIN `+0.1695u`
2. `T1 +4.5 kills @1.936` — LOSS `-0.25u`
3. `Over 32 minutes @1.869` — LOSS `-0.25u`
4. `Over 30.5 total kills @1.974` — WIN `+0.2435u`

G5: `2W-2L`, net `-0.0870u`.
HLE-T1 series forced-choice net: `-0.8040u`.

The stricter post-audit DIM correctly certified HLE in G5. The two model-positive misses were KH and Duration; do not infer a structural change from one map, but retain the HLE clean-cascade branch for the next checkpoint review.

Airtable map and all four canonical positions were settled at map end.

## Forced-choice cohort after series
- `28 Positions / 7 samples per family`
- `13W-15L`
- Shadow P/L: `-0.9980u`
- Actual exposure: `0u`

By family:
- ML `1-6 / -1.3305u`
- KH `3-4 / -0.3475u`
- Duration `4-3 / +0.0795u`
- Total Kills `5-2 / +0.6005u`

## Next audit cadence
- Next checkpoint at `40 canonical forced-choice Positions / 10 samples per family`.
- Need `3 more maps / 12 more positions` to reach that checkpoint.
- No structural coefficient change is authorized yet.
