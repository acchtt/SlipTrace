# Current Live Handoff — Gen.G vs Hanwha Life Esports — 2026-09-05

**Status:** ACTIVE SERIES HANDOFF — GAME 2 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-05-V13-GEN-HLE-DRAFTONLY-FORCEDCHOICE-Q2-1306-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series state

- Gen.G vs Hanwha Life Esports — LCK 2026 Season Playoffs Upper Bracket Final, Bo5 Fearless Draft.
- G1 had no prospective canonical Position in this chat; do not create retroactive G1 Positions.
- G2 final draft + exact board were supplied prospectively and four canonical forced-choice Positions are locked.
- No Airtable write until G2 ends.
- Same-series results never update K/P0/TK0; only Fearless champion availability may carry forward.

## Frozen benchmark

- `B(GEN)=+1.467332`
- `B(HLE)=+0.931313`
- `GAP(GEN-HLE)=+0.536019 SD`
- `GEN K=+1 / P0=55%`
- `HLE K=-1 / P0=45%`
- `TK0=26.95`
- benchmark windows: completed LCK 2026 Rounds 3-4 + Rounds 1-2; no playoff result or sportsbook price used.

## Game 2 draft

Role order TOP / JUNGLE / MID / ADC / SUPPORT.

GEN blue:
- Rumble
- Jarvan IV
- Locke
- Jhin
- Shen

HLE red:
- Ambessa
- Qiyana
- Syndra
- Caitlyn
- Bard

Locke is treated as the mid-lane champion named by the user; exact role is resolved.

## Game 2 source-truth board

- Moneyline: GEN `1.678` / HLE `2.109`
- Duration `32.0`: Over `1.756` / Under `1.996`
- Total Kills `26.5`: Over `2.026` / Under `1.734`
- Kill Handicap: GEN `-3.5 @1.753` / HLE `+3.5 @2.001`

## Game 2 price-blind draft audit

Diagnostic DIM only; Q2 sets `D_PROBABILITY_CONTRIBUTION=0` for forced-choice ML.

Mechanisms:
- GEN PKM: Jarvan engage/terrain confinement -> Shen reinforcement -> Rumble choke damage -> Locke/Jhin cleanup.
- GEN SKM: ranged catch/finish through Jhin plus Locke follow-up around isolated targets and objective entries.
- HLE PKM: Syndra/Bard pick and zone -> Caitlyn trap/range control -> Qiyana/Ambessa collapse.
- HLE SKM: long-range objective setup with Caitlyn/Syndra/Bard creating forced entry angles for Qiyana terrain burst and Ambessa follow-through.

DIM rows:
- TAM: mixed; Shen can directly blunt HLE dive/burst on one target, while Bard/Syndra can disrupt GEN's committed engage.
- OSG: slight HLE due Caitlyn/Syndra/Bard pre-contact space plus Qiyana terrain leverage; GEN Equalizer/Jarvan remains dangerous in chokes.
- DAU: mixed/slight HLE at range, GEN stronger once hard contact is achieved.
- SLI: no certified independent decisive side-lane mechanism.
- FNF: both compositions can function without classic tank front-to-back; GEN has more deterministic first-contact body access through Jarvan/Shen.
- CAS: both have clean-cascade branches; neither side receives reliable margin-suppression certification.
- ETS: GEN benchmark strength modestly higher, but team strength does not alter diagnostic draft sign.
- AFP: each side retains a second route after first mechanism denial; no two-independent-mechanism superiority survives strongly enough for nonzero D.

`D=0 / EVEN-STYLE-DEPENDENT`  
`D_DIAGNOSTIC_ONLY=YES`  
`D_PROBABILITY_CONTRIBUTION=0`

## Game 2 locked forced-choice card

### Moneyline
Frozen probability:
- GEN `55%`
- HLE `45%`

Price comparison:
- GEN @1.678 -> implied `59.59%` -> edge `-4.59pp`
- HLE @2.109 -> implied `47.42%` -> edge `-2.42pp`

Canonical ML: **HLE ML @2.109**  
`MODEL_EDGE=-2.42pp`  
`FORCED_NEG_EV=YES`

### Kill Handicap
Portfolio rule applies because absolute handicap is `<5`; KH must align with selected HLE ML.

Pre-price signed margin bins:
- HLE wins by 10+: `10%`
- HLE wins by 5-9: `12%`
- HLE wins by 1-4: `23%`
- GEN wins by 1-3: `17%`
- GEN wins by 4-9: `23%`
- GEN wins by 10+: `15%`

HLE +3.5 raw cover = `62%`; capped execution probability = `62%` (below 70% cap).  
HLE +3.5 @2.001 -> implied `49.98%` -> `MODEL_EDGE=+12.02pp`.  
Canonical KH: **HLE +3.5 @2.001**  
`FORCED_NEG_EV=NO`

### Duration
Draft-only scores:
- `V=0`
- `Q=0`
- `H=0`
- `T=-1`
- `F=30.25m`

At line 32.0:
- Under model `62.25%`
- Under @1.996 implied `50.10%`
- `MODEL_EDGE=+12.15pp`

Canonical Duration: **Under 32 @1.996**  
`FORCED_NEG_EV=NO`  
`OVER_BRANCH_WARNING=NO`

### Total Kills
Frozen `TK0=26.95`.

Pre-price bins:
- `<20`: `9%`
- `20-24`: `20%`
- `25-26`: `17%`
- `27-31`: `28%`
- `32-36`: `16%`
- `37+`: `10%`

Explicit `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` branch: `23%` of total scenario mass, concentrated primarily below 27 total kills; separate two-sided-brawl continuation keeps upper-tail mass meaningful.

Over 26.5 model = `54%`; Over @2.026 implied `49.36%`; `MODEL_EDGE=+4.64pp`.

Canonical TK: **Over 26.5 @2.026**  
`FORCED_NEG_EV=NO`

## Game 2 execution lock

Four canonical Positions, standing authorization from supplied final draft + exact board:
1. HLE ML @2.109 — 0.25u shadow
2. HLE +3.5 @2.001 — 0.25u shadow
3. Under 32 @1.996 — 0.25u shadow
4. Over 26.5 @2.026 — 0.25u shadow

Total: `1.00u shadow / 0u actual`.

Do not update from live score/state. Await final map result, then write map + four Positions to Airtable and run map micro-audit.

## Cohort entering G2

- `48 Positions / 12 per family`
- `24W-24L / -0.77275u`
- ML `3-9 / -1.71425u`
- KH `6-6 / -0.16750u`
- Duration `9-3 / +1.23700u`
- TK `6-6 / -0.12800u`
- actual exposure `0u`

Next preferred checkpoint: `80 total / 20 per family`.
