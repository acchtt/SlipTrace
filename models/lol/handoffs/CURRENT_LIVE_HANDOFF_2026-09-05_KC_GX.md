# Current Live Handoff — Karmine Corp vs GIANTX — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — G1/G2 SETTLED / SERIES 1-1 / GAME 3 POSITIONS LOCKED  
**Session lock:** `LOL-2026-09-05-V13-LEC-KC-GX-DRAFTONLY-FORCEDCHOICE-Q2-1950-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / ML FLOOR 1.45 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

Karmine Corp vs GIANTX — LEC 2026 Summer Playoffs Upper Bracket Round 1, Bo5 Fearless Draft.

- G1 final: **KC won 12-8 in 40:40**.
- G2 final: **GX won 22-12 in 37:42**.
- Series score after G2: **1-1**.
- G1 and G2 map records plus all 8 canonical positions are written to Airtable.
- G3 final draft + exact board were supplied prospectively; four canonical G3 positions are locked below.
- Same-series results do not update frozen `K/P0/TK0`; prior maps may inform only Fearless champion availability.
- User-directed ML floor remains active: selected Moneyline must be `>=1.45`.
- Airtable remains untouched for G3 until the map ends.

## Frozen benchmark

- `B(KC)=+1.625030`
- `B(GX)=-0.241316`
- `GAP(KC-GX)=+1.866346 SD`
- `KC K=+2 / P0=60%`
- `GX K=-2 / P0=40%`
- `TK0=28.50`

## Settled block through Game 2

### Game 1
Locked card and settlement:
1. GX ML @3.522 — **LOSS** — `-0.25000u`
2. GX +8.5 @1.868 — **WIN** — `+0.21700u`
3. Over 32 @1.904 — **WIN** — `+0.22600u`
4. Over 25.5 @1.869 — **LOSS** — `-0.25000u`

**G1: `2W-2L / -0.05700u`.**

### Game 2
Locked card and settlement:
1. GX ML @3.305 — **WIN** — `+0.57625u`
2. GX +8.5 @1.831 — **WIN** — `+0.20775u`
3. Under 32 @1.691 — **LOSS** — `-0.25000u`
4. Over 24.5 @1.735 — **WIN** — `+0.18375u`

**G2: `3W-1L / +0.71775u`.**

KC-GX tracked block through G2: `5W-3L / +0.66075u`.

## Cohort entering Game 3

- `72 Positions / 18 per family`
- overall **`38W-34L / +0.01775u`**
- ML **`5-13 / -1.94150u`**
- KH **`10-8 / +0.18800u`**
- Duration **`13-5 / +1.58650u`**
- TK **`10-8 / +0.18475u`**
- actual exposure `0u`

Preferred checkpoint remains `80 positions / 20 per family`: two more fully recorded maps / eight positions.

## Game 3 final draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

GX blue: `Olaf / Trundle / Viktor / Caitlyn / Bard`  
KC red: `Vayne / Naafiri / Ryze / Yunara / Lulu`

The user's second draft message corrects the earlier omission of Olaf; this five-champion GX draft is source truth.

## Game 3 source-truth board

- ML: KC `1.307` / GX `3.274`
- Duration `32.0`: Over `1.694` / Under `2.083`
- Total Kills `24.5`: Over `1.878` / Under `1.843`
- KH: KC `-8.5 @1.979` / GX `+8.5 @1.770`

Displayed live-state labels are ignored for prediction under postdraft-only mode.

## Game 3 price-blind DIM

GX mechanisms:
- PKM: Bard long-range catch or Trundle pillar displacement creates first contact, Viktor controls the retreat path, Caitlyn traps/range convert, and Olaf supplies front-line chase.
- SKM: Caitlyn/Viktor/Bard objective-zone and siege pressure can win space without committing first; Olaf/Trundle then punish a forced entry or overextension.

KC mechanisms:
- PKM: Naafiri direct access -> Ryze control and Vayne/Yunara focus, with Lulu speed/ult/polymorph protecting the diving or cleanup carry.
- SKM: Vayne/Ryze side-lane and scaling pressure can force split assignments while Yunara/Lulu hold a ranged four-man shell; this route is meaningfully distinct from Naafiri first-contact play.

DIM rows:
- TAM: mixed — GX has pillar/Bard/Viktor disruption; KC has Lulu peel plus Ryze control.
- OSG: GX advantage — Caitlyn traps, Viktor zone and Bard angles give superior choke/structure setup.
- DAU: mixed — Bard/Trundle can manufacture access, while Naafiri gives KC the cleaner single-button forward trigger.
- SLI: KC advantage — Vayne/Ryze create the more credible side-assignment route.
- FNF: GX slight — Olaf/Trundle provide a sturdier front line for Viktor/Caitlyn than KC's comparatively fragile carry-heavy shell.
- CAS: mixed — either side can cascade after the first clean catch, but neither retains a decisive conversion monopoly under adversarial response.
- ETS: KC benchmark advantage remains contextual only and does not set D mechanically.
- AFP: both sides retain two independent mechanisms after adversarial denial; no side clears the threshold for certified directional draft credit.

Diagnostic result: `D=0 / EVEN-STYLE-DEPENDENT`.  
`D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`.

## Game 3 locked forced-choice card

### Moneyline
Frozen Q2 probabilities: KC `60%` / GX `40%`.

- KC @1.307 -> implied `76.51%` -> raw model edge `-16.51pp`; additionally **execution-ineligible** under ML floor `<1.45`.
- GX @3.274 -> implied `30.54%` -> `MODEL_EDGE=+9.46pp`.

Canonical ML: **GX ML @3.274**  
`ML_PRICE_FLOOR=1.45`  
`FORCED_NEG_EV=NO`

### Kill Handicap
Absolute line is `8.5`, so KH may be evaluated independently of ML.

Pre-price signed margin bins:
- KC wins by 10+: `24%`
- KC wins by exactly 9: `5%`
- KC wins by 5-8: `16%`
- KC wins by 1-4: `15%`
- GX wins by 1-4: `16%`
- GX wins by 5-8: `10%`
- GX wins by exactly 9: `4%`
- GX wins by 10+: `10%`

Total KC win mass = `60%`; GX win mass = `40%`.  
GX +8.5 raw cover = `71%`; Q2 capped execution probability = `70%`.  
GX +8.5 @1.770 -> implied `56.50%` -> `MODEL_EDGE=+13.50pp`.

Canonical KH: **GX +8.5 @1.770**  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=0` — Naafiri gives KC direct contact, but both drafts also possess enough peel/zone to deny automatic first-engage conversion.
- `Q=+1` — Viktor/Caitlyn/Bard objective setup plus Ryze/Vayne side assignments can force extra setup and rotation cycles.
- `H=+1` — Lulu/Bard disengage and multiple ranged reset tools create credible non-terminal fight states.
- `T=+1` — both drafts preserve substantial scaling and side-lane value rather than requiring an early terminal path.
- `F=33.75m`.

At line 32.0:
- Over model `62.25%`
- Over @1.694 implied `59.03%`
- `MODEL_EDGE=+3.22pp`

Canonical Duration: **Over 32 @1.694**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=YES`

### Total Kills
Frozen `TK0=28.50`.

Price-blind bins:
- `<20`: `10%`
- `20-24`: `23%`
- `25-29`: `28%`
- `30-34`: `21%`
- `35-39`: `11%`
- `40+`: `7%`

Over 24.5 model = `67%`.  
Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch = `20%` of scenario mass, concentrated below the line. The over branch remains larger because both drafts can generate repeated catches and counter-catches once side assignments collapse around objectives.

Over 24.5 @1.878 -> implied `53.25%` -> `MODEL_EDGE=+13.75pp`.

Canonical TK: **Over 24.5 @1.878**  
`FORCED_NEG_EV=NO`

## Game 3 execution lock

1. **GX ML @3.274** — `0.25u shadow`
2. **GX +8.5 @1.770** — `0.25u shadow`
3. **Over 32 @1.694** — `0.25u shadow`
4. **Over 24.5 @1.878** — `0.25u shadow`

Total G3: `1.00u shadow / 0u actual`.

Do not update predictions from displayed live score/state. Await final G3 result, then write G3 map + four canonical positions to Airtable and run map micro-audit.
