# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** ACTIVE SERIES HANDOFF — GAME 4 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Series / cohort state

- KT Rolster vs Dplus KIA — LCK 2026 Season Playoffs Lower Bracket Round 2, Bo5 Fearless Draft.
- G1-G2: no prospective positions; no retroactive creation.
- G3 settled: DK won 19-4 in 26:56; G3 positions 3-1 / +0.40125u.
- Cohort entering G4: `44 Positions / 11 per family / 20W-24L / -1.67425u`.
- Family state: ML `2-9 / -1.8940u`; KH `5-6 / -0.4005u`; Duration `8-3 / +1.01975u`; TK `5-6 / -0.3995u`.
- Actual exposure `0u`.

## Frozen benchmark

- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- `TK0=25.45`
- Same-series results never update K/P0/TK0.

## Game 4 final draft / board

User-supplied role order TOP / JUNGLE / MID / ADC / SUPPORT:

DK blue:
- Jax
- Vi
- Annie
- Miss Fortune
- Neeko

KT red:
- Gwen
- Skarner
- Akali
- Kalista
- Renata

Exact board:
- ML: DK `1.650` / KT `2.205`
- Duration 31.5: Over `1.780` / Under `1.968`
- Total Kills 27.5: Over `1.909` / Under `1.861`
- Kill Handicap: DK `-5.5 @1.930` / KT `+5.5 @1.826`

Displayed match clock/state is ignored by draft-only mode.

## G4 price-blind DIM

DK mechanisms:
- `PKM`: Vi point-and-click access -> Annie/Neeko layered CC -> Miss Fortune Bullet Time -> Jax cleanup.
- `SKM`: Neeko/Annie fog flank or pick -> MF objective-zone conversion, with Jax as a separate side/collapse threat.

KT mechanisms:
- `PKM`: Skarner displacement/pick -> Kalista/Renata follow-up -> Akali/Gwen dive and cleanup.
- `SKM`: Akali/Gwen side/flank pressure -> force split attention -> Skarner/Renata collapse while Kalista controls objective tempo.

Interaction rows:
- `TAM=MIXED`: Renata Bailout and Skarner disruption can blunt a single DK burst sequence, but do not generically answer Vi + layered Annie/Neeko AoE. DK in turn has limited clean peel once Akali/Gwen reach MF after Vi commits.
- `OSG=DK_SLIGHT`: Annie/Neeko/MF create strong choke and fog punishment; Skarner/Renata/Kalista still contest objective setup well.
- `DAU=DK_SLIGHT`: Vi gives DK the most deterministic priority-target access; KT has credible backline access through Skarner/Akali/Gwen but it is more assignment-sensitive.
- `SLI=EVEN`: Jax and Gwen both create real side pressure; neither side route alone invalidates the opposing four-man unit.
- `FNF=EVEN`: neither composition requires a classic front-to-back tank shell to function.
- `CAS=DK_SLIGHT`: a first DK catch can cascade through layered AoE and MF channel; Renata materially reduces but does not erase this branch.
- `ETS=DK_STRENGTH_PRIOR` from frozen benchmark.
- `AFP=PASS / DK DIAGNOSTIC EDGE`: KT's strongest answer is Skarner first contact plus Renata reset into Akali/Gwen counter-dive. Two DK routes still survive: deterministic Vi-led catch/wombo and separate Neeko/Jax flank-side pressure.

Final diagnostic certification:
`DIM[ROLES=P;PKM_DK=VI_ACCESS->ANNIE_NEEKO_CC->MF_ULT->JAX;SKM_DK=FOG_PICK+MF_ZONE+JAX_COLLAPSE;PKM_KT=SKARNER_PICK->KALISTA_RENATA->AKALI_GWEN;SKM_KT=SIDE_FLANK->COLLAPSE;TAM=MIXED;OSG=DK_SLIGHT;DAU=DK_SLIGHT;SLI=EVEN;FNF=EVEN;CAS=DK_SLIGHT;ETS=DK_STRENGTH;AFP=P;EDGE=DK]`

`D=+1 DK`, but Q2 forces `D_DIAGNOSTIC_ONLY=YES / D_PROBABILITY_CONTRIBUTION=0`.

## G4 locked price-blind family projections

### Moneyline
Q2 forced-choice probability remains P0 only:
- DK `60%`
- KT `40%`

### Kill Handicap signed margin distribution
DK-perspective bins:
- DK `+10 or more`: `20%`
- DK `+6 to +9`: `18%`
- DK `+1 to +5`: `22%`
- KT `+1 to +5`: `18%`
- KT `+6 to +9`: `12%`
- KT `+10 or more`: `10%`

Sums to 100%; DK win mass `60%`.
- raw DK `-5.5` cover `38%`
- raw KT `+5.5` cover `62%`
- `KH_CAPPED_PROB=62%`
- line is `±5.5`, so KH may remain independent of ML under portfolio rule.

### Duration
Draft-only scores:
- `V=0 / Q=0 / H=0 / T=-1`
- `F=30.25m`
- at 31.5: Under `58.75%`, Over `41.25%`

Mechanism: both sides have hard compulsory-contact tools and limited clean reset after first access; DK's layered wombo can produce fast conversion, while Renata/Gwen/Akali retain some stall/reversal branches.

### Total Kills
Pre-price bins:
- `<20`: `11%`
- `20-24`: `21%`
- `25-27`: `15%`
- `28-32`: `27%`
- `33-37`: `16%`
- `38+`: `10%`

Sums to 100%.
- Over 27.5 `53%`
- Under 27.5 `47%`

Required branch mass:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 20%`
- `TWO_SIDED_BRAWL / REPEATED_CONTACT = 35%`
- ordinary controlled/contested paths `45%`.

## G4 price pass / canonical positions

1. **Moneyline — DK ML @1.650 — 0.25u shadow / 0u actual**
   - model `60.00%`
   - implied `60.61%`
   - `MODEL_EDGE=-0.61pp`
   - `FORCED_NEG_EV=YES`
   - KT alternative model 40% vs implied 45.35%, so DK is the less-negative forced side.

2. **Kill Handicap — KT +5.5 @1.826 — 0.25u shadow / 0u actual**
   - raw/capped cover `62.00%`
   - implied `54.76%`
   - `MODEL_EDGE=+7.24pp`
   - `FORCED_NEG_EV=NO`
   - `±5.5` is wide enough to remain independent of selected DK ML.

3. **Duration — Under 31.5 @1.968 — 0.25u shadow / 0u actual**
   - `F=30.25m`
   - model Under `58.75%`
   - implied `50.81%`
   - `MODEL_EDGE=+7.94pp`
   - `FORCED_NEG_EV=NO`.

4. **Total Kills — Over 27.5 @1.909 — 0.25u shadow / 0u actual**
   - model Over `53.00%`
   - implied `52.38%`
   - `MODEL_EDGE=+0.62pp`
   - `FORCED_NEG_EV=NO`.

G4 shadow total `1.00u`; actual exposure `0u`.

## Settlement discipline

- No G4 live-state reassessment or replacement position after entry.
- Airtable write deferred until map end.
- On final result: settle map + exactly these four canonical Positions, run full post-map micro-audit, then advance cohort from 44 to 48 Positions.
