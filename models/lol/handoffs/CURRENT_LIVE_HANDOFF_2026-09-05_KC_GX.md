# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 2 POSITIONS LOCKED / G1 SETTLEMENT EVIDENCE PENDING / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.
- G1 final draft + exact board were supplied prospectively and four canonical positions were locked, but no final G1 result/evidence has yet been supplied in chat; do not settle or write G1 retroactively without result evidence.
- G2 final draft + exact board have now been supplied prospectively; four canonical G2 positions are locked below.
- User-directed ML floor remains active: selected ML must be `>=1.45`; sub-1.45 ML is execution-ineligible.
- Same-series results do not update `K/P0/TK0`; prior maps may inform only Fearless champion availability where structurally needed.
- Airtable write occurs only when a map result is supplied and settled.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Game 1 historical open lock

Draft:
- KC blue: `Jayce / Jarvan IV / Anivia / Ashe / Seraphine`
- GX red: `Yorick / Skarner / Cassiopeia / Lucian / Milio`

Board:
- ML KC `1.272` / GX `3.522`
- Duration `32.0`: Over `1.904` / Under `1.835`
- Total Kills `25.5`: Over `1.869` / Under `1.851`
- KH KC `-8.5 @1.869` / GX `+8.5 @1.868`

Locked G1 card:
1. GX ML @3.522
2. GX +8.5 @1.868
3. Over 32 @1.904
4. Over 25.5 @1.869

G1 remains **UNSETTLED — RESULT EVIDENCE NOT YET SUPPLIED**.

## Game 2 final draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

KC blue: `Gnar / Wukong / Akali / Ezreal / Rell`  
GX red: `Ambessa / Sejuani / Orianna / Kai'Sa / Nautilus`

## Game 2 source-truth board

- ML: KC `1.302` / GX `3.305`
- Duration `32.0`: Over `2.088` / Under `1.691`
- Total Kills `24.5`: Over `1.735` / Under `2.004`
- KH: KC `-8.5 @1.908` / GX `+8.5 @1.831`

Displayed live-state labels are ignored for prediction under postdraft-only mode.

## Game 2 price-blind DIM

KC mechanisms:
- PKM: Rell/Wukong/Gnar layered engage -> Akali access -> Ezreal follow-up and cleanup.
- SKM: Ezreal ranged poke plus Akali/Gnar side-angle pressure can soften or displace GX before Wukong/Rell collapse.

GX mechanisms:
- PKM: Sejuani/Nautilus deterministic lock -> Orianna control/Shockwave -> Kai'Sa/Ambessa follow-through.
- SKM: Ambessa side pressure plus Sejuani/Nautilus threat and Orianna zone control can force rotations, with Kai'Sa able to join long-range collapse.

DIM rows:
- TAM: mixed. GX has redundant initiation and counter-lock, while KC has multiple AoE interruption/counter-engage layers.
- OSG: mixed. GX's Sejuani/Nautilus/Orianna package is excellent in chokes; KC offsets with Ezreal poke and Mega Gnar threat.
- DAU: GX slight. Sejuani/Nautilus give more deterministic first-target access, but KC carries high mobility and counter-engage.
- SLI: mixed. Akali and Ambessa both create side-lane pressure; neither side retains a clearly superior independent side route after adversarial response.
- FNF: GX slight from two durable initiators plus Orianna/Kai'Sa stable follow-up; KC can compensate with Gnar/Wukong/Rell layering but is more timing-sensitive.
- CAS: mixed. Either side can cascade rapidly after first successful control chain.
- ETS: KC benchmark advantage is retained only as execution-confidence context and does not set D mechanically.
- AFP: both teams retain at least two viable mechanisms after adversarial denial; the GX front-to-back advantage is not sufficient to certify a full draft-direction edge.

Diagnostic result: `D=0 / EVEN-STYLE-DEPENDENT`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 2 locked forced-choice card

### Moneyline
Frozen Q2 probabilities: KC `60%` / GX `40%`.

- KC @1.302 -> implied `76.80%` -> raw model edge `-16.80pp`; additionally **execution-ineligible** under ML floor `<1.45`.
- GX @3.305 -> implied `30.26%` -> `MODEL_EDGE=+9.74pp`.

Canonical ML: **GX ML @3.305**  
`ML_PRICE_FLOOR=1.45`  
`FORCED_NEG_EV=NO`

### Kill Handicap
Absolute line is `8.5`, so KH may be evaluated independently of ML.

Pre-price signed margin bins:
- KC wins by 10+: `25%`
- KC wins by exactly 9: `5%`
- KC wins by 5-8: `15%`
- KC wins by 1-4: `15%`
- GX wins by 1-4: `16%`
- GX wins by 5-8: `10%`
- GX wins by exactly 9: `4%`
- GX wins by 10+: `10%`

Total KC win mass = `60%`; GX win mass = `40%`, consistent with frozen P0.  
GX +8.5 raw cover = `70%`; Q2 capped execution probability = `70%`.  
GX +8.5 @1.831 -> implied `54.61%` -> `MODEL_EDGE=+15.39pp`.

Canonical KH: **GX +8.5 @1.831**  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=+1` — both drafts have direct, repeatable engage-to-conversion chains with limited need for slow setup once contact is found.
- `Q=0` — no reliable compulsory-cycle stall advantage is certified pre-map.
- `H=0` — ordinary terminal-path depth.
- `T=0` — neither side's scaling/side structure is strong enough to force extra duration credit against the high-contact engage profiles.
- `F=29.50m`.

At line 32.0:
- Under model `67.50%`
- Under @1.691 implied `59.14%`
- `MODEL_EDGE=+8.36pp`

Canonical Duration: **Under 32 @1.691**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=NO`

### Total Kills
Frozen `TK0=28.50`.

Price-blind bins:
- `<20`: `8%`
- `20-24`: `21%`
- `25-29`: `28%`
- `30-34`: `23%`
- `35-39`: `13%`
- `40+`: `7%`

Over 24.5 model = `71%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `18%` of scenario mass, concentrated at 24 or fewer kills. The upper branch remains large because both teams have repeatable initiation plus enough counter-engage and follow-up to create return kills and multi-stage fights.

Over 24.5 @1.735 -> implied `57.64%` -> `MODEL_EDGE=+13.36pp`.

Canonical TK: **Over 24.5 @1.735**  
`FORCED_NEG_EV=NO`

## Game 2 execution lock

1. **GX ML @3.305** — `0.25u shadow`
2. **GX +8.5 @1.831** — `0.25u shadow`
3. **Under 32 @1.691** — `0.25u shadow`
4. **Over 24.5 @1.735** — `0.25u shadow`

Total G2: `1.00u shadow / 0u actual`.

Do not update predictions from displayed live score/state. Await final G2 result, then write G2 map + four canonical positions to Airtable and run map micro-audit. G1 remains separately unsettled until its final evidence is supplied.

## Settled cohort entering KC-GX

Because G1 result has not been supplied, the settled cohort remains:
- `64 Positions / 16 per family`
- `33W-31L / -0.64300u`
- ML `4-12 / -2.26775u`
- KH `8-8 / -0.23675u`
- Duration `12-4 / +1.61050u`
- TK `9-7 / +0.25100u`
- actual exposure `0u`

Open prospectively locked positions in this series: `8` total (G1 four + G2 four). Preferred structural checkpoint remains `80 settled total / 20 per family`.