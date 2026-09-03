# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** ACTIVE SERIES HANDOFF — GAME 5 POSITIONS LOCKED / SERIES 2-2 / 40-POSITION CHECKPOINT AT G5 SETTLEMENT  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Current series / frozen benchmark

- Dplus KIA (DK) vs BNK FearX (BFX), LCK 2026 Season Playoffs Lower Bracket Round 1, Bo5 Fearless Draft.
- Series entering Game 5: `2-2`.
- G1-G2 had no prospective canonical Positions in this chat.
- Same-series results remain quarantined from benchmark construction and may inform only Fearless champion availability.
- `B(DK)=+0.334587`
- `B(BFX)=+0.010432`
- `GAP(DK-BFX)=+0.324155 SD`
- `DK K=0 / P0=50%`
- `BFX K=0 / P0=50%`
- frozen `TK0=28.4`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`

## 2. Settled cohort entering Game 5

Game 3: DK win, `13-12`, `31:57`; canonical result `2W-2L / -0.06325u`.

Game 4: DK win, `16-6`, `22:43`; canonical result `1W-3L / -0.50375u`.

Cohort entering Game 5:
- `36 canonical Positions / 9 per family`
- `16W-20L`
- shadow P/L `-1.5650u`
- actual exposure `0u`
- family records: ML `1-8 / -1.8305u`; KH `4-5 / -0.3725u`; Duration `6-3 / +0.5375u`; TK `5-4 / +0.1005u`.
- Game 5 settlement, if all four settle, triggers the full checkpoint at `40 positions / 10 per family`.

G4 checkpoint evidence retained without coefficient change: BFX `D=+1` and BFX +7.5 `85%` cover were severe misses; Duration Under direction was correct; TK Over missed in a one-sided fast close. Full structural review is deferred until G5 settlement.

## 3. Game 5 final draft and board

User-supplied final role order (TOP / JUNGLE / MID / ADC / SUPPORT):

DK blue:
- Varus TOP
- Kindred JUNGLE
- Taliyah MID
- Ziggs ADC
- Camille SUPPORT

BFX red:
- Kled TOP
- Maokai JUNGLE
- Tristana MID
- Aphelios ADC
- Thresh SUPPORT

Board:
- Moneyline: DK `1.871` / BFX `1.866`
- Duration 32: Over `1.787` / Under `1.958`
- Total Kills 27.5: Over `1.756` / Under `1.997`
- Kill Handicap: DK `-3.5 @1.979` / BFX `+3.5 @1.770`

Any displayed live-state data is ignored for prediction under the draft-only lock.

## 4. Game 5 full price-blind DIM

DK mechanisms:
- `PKM`: Varus Arrow or Camille first access -> Taliyah displacement/zone + Ziggs burst -> Kindred ranged cleanup.
- `SKM`: Varus/Ziggs/Taliyah pre-objective poke and zone control -> Ziggs serial structure conversion, with Kindred R as an anti-cascade reset when BFX forces contact.

BFX mechanisms:
- `PKM`: Kled charge + Maokai R/W + Thresh follow-up forces contact onto DK's ranged core -> Aphelios sustained DPS + Tristana cleanup.
- `SKM`: Kled/Tristana side pressure and mobility create assignment stress -> Maokai/Thresh collapse creates picks away from DK's preferred ranged setup.

Interaction rows:
- `TAM=MIXED`: DK has real anti-engage through Taliyah E, Varus R, Ziggs W and especially Kindred R; BFX can still layer Kled/Maokai/Thresh from multiple timings and force DK to spend those answers.
- `OSG=DK_ADV`: Varus + Ziggs + Taliyah give DK superior pre-contact poke, choke denial and structure conversion when established first; Maokai saplings and BFX engage keep this from being uncontested.
- `DAU=BFX_SLIGHT`: BFX has multiple ways to reach DK's fragile ranged shell; DK can reach Aphelios through Camille/Varus/Taliyah but must cross Maokai/Thresh peel and Kled disruption.
- `SLI=BFX_ADV`: Kled + Tristana give BFX the clearer independent side/assignment pressure route; DK can answer through Taliyah movement and ranged waveclear but has less durable side-lane ownership.
- `FNF=BFX_ADV`: BFX has a materially stronger grouped front-to-back shell through Kled/Maokai/Thresh; DK is highly range- and setup-dependent with little conventional front line.
- `CAS=MIXED`: BFX can cascade from first engage into Tristana/Aphelios cleanup, but Kindred R is a direct anti-cascade layer; DK can also cascade a pick into Ziggs structures.
- `ETS=EVEN`: frozen benchmark is K=0 / 50-50 and does not break the interaction state.
- `AFP=PASS / BFX EDGE CERTIFIED`: DK's strongest failure path for the BFX thesis is first-position objective poke/siege plus Kindred-R reset. It survives and is meaningful, but does not erase two independent BFX mechanisms: forced grouped access and side/assignment collapse.

Final certification:
`DIM[ROLES=P;PKM_DK=VARUS/CAMILLE_CATCH->TALIYAH_ZIGGS_ZONE->KINDRED;SKM_DK=RANGED_POKE/SIEGE+KINDRED_RESET;PKM_BFX=KLED_MAO_THRESH_FORCE->APHELIOS_TRIST_CLEANUP;SKM_BFX=SIDE_ASSIGNMENT_PRESSURE->COLLAPSE;TAM=MIXED;OSG=DK_ADV;DAU=BFX_SLIGHT;SLI=BFX_ADV;FNF=BFX_ADV;CAS=MIXED;ETS=EVEN;AFP=P;EDGE=BFX]`

Post-audit draft edge:
- `D=+1 BFX`
- two independent BFX advantages survive the adversarial pass: grouped front-to-back/forced access and side-assignment collapse.

## 5. Game 5 locked family projections before price pass

### Moneyline
With `P0=50%` and `D=+1 BFX`:
- BFX `54.5%`
- DK `45.5%`

### Kill Handicap signed final-margin distribution
DK-perspective final kill-margin bins, locked before pricing:
- DK `+10 or more`: `8%`
- DK `+5 to +9`: `12%`
- DK `+4`: `6%`
- DK `+1 to +3`: `19.5%`
- BFX `+1 to +4`: `27.5%`
- BFX `+5 to +9`: `15%`
- BFX `+10 or more`: `12%`

Sums to 100%; BFX win probability = `54.5%`, consistent with ML.
Derived cover:
- BFX `+3.5`: `74.0%` by raw bin arithmetic; confidence haircut locks canonical cover at `70.0%` for execution.
- DK `-3.5`: `26.0%` raw.

Portfolio rule: because absolute handicap is `3.5 < 5`, the KH selection must align with the selected ML side. BFX ML therefore requires BFX +3.5.

### Duration
Draft-only t=0 scoring:
- `V=0`
- `Q=0`
- `H=0`
- `T=-1`

`F = 31.0 + 0.75(-1) = 30.25 minutes`.
At line 32:
- `P(OVER)=37.75%`
- `P(UNDER)=62.25%`

Acceleration driver: either BFX forced engage/cascade or DK poke-to-Ziggs structure conversion can compress the terminal path; no demonstrated live stall evidence is used.

### Total Kills
Frozen `TK0=28.4`.
Draft-adjusted total-kill bins, locked before pricing:
- `<20`: `7%`
- `20-24`: `15%`
- `25-27`: `20%`
- `28-32`: `29%`
- `33-37`: `18%`
- `38+`: `11%`

Sums to 100%.
At line 27.5:
- `P(OVER)=58%`
- `P(UNDER)=42%`

Drivers: BFX has multiple compulsory-contact tools; DK has Camille/Varus catch and Kindred R can extend otherwise terminal fights into additional kill exchanges. Counterweight is a possible one-sided fast close suppressing return kills.

## 6. Game 5 canonical forced-choice Positions

Exactly one canonical Position per family:

1. **Moneyline — BFX ML @1.866 — 0.25u shadow / 0u actual**
   - model `54.5%`
   - raw implied `53.59%`
   - `MODEL_EDGE=+0.91pp`
   - `FORCED_NEG_EV=NO`

2. **Kill Handicap — BFX +3.5 @1.770 — 0.25u shadow / 0u actual**
   - locked execution cover `70.0%`
   - raw implied `56.50%`
   - `MODEL_EDGE=+13.50pp`
   - `FORCED_NEG_EV=NO`
   - `<5` handicap aligns with selected BFX ML as required.

3. **Duration — Under 32:00 @1.958 — 0.25u shadow / 0u actual**
   - locked `F=30.25m`
   - model Under `62.25%`
   - raw implied `51.07%`
   - `MODEL_EDGE=+11.18pp`
   - `FORCED_NEG_EV=NO`

4. **Total Kills — Over 27.5 @1.756 — 0.25u shadow / 0u actual**
   - model Over `58.0%`
   - raw implied `56.95%`
   - `MODEL_EDGE=+1.05pp`
   - `FORCED_NEG_EV=NO`

Game 5 shadow total: `1.00u`; actual exposure: `0u`.

## 7. Persistence / settlement rule

- GitHub handoff contains the locked G5 price-blind DIM, family distributions and four canonical selections.
- Airtable is not written at entry; write remains deferred until Game 5 ends.
- No G5 live-state reassessment or replacement position after map start under draft-only execution.
- At Game 5 end: settle map + all four canonical Positions in Airtable, update cohort to 40 / 10 per family, then run the full checkpoint audit before any structural model change or next-session position.
