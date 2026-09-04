# KT vs DK Game 4 — Corrected Draft Reassessment — 2026-09-04

**Status:** RETROSPECTIVE / NON-CANONICAL FOR SETTLEMENT / DATA-INTEGRITY REVIEW  
**Series:** LCK 2026 Season Playoffs — KT Rolster vs Dplus KIA — Game 4  
**Historical lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7` (closed)  
**Purpose:** recompute the pre-price draft-only projections using the corrected DK top champion **Renekton** instead of the erroneously entered **Jax**.  
**Hard rule:** do not rewrite the historical Position ledger, odds, stake, result, or P/L. This file is calibration/audit evidence only.

## Corrected final draft

DK blue, TOP/JG/MID/ADC/SUP:
- Renekton
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

Historical locked board retained for counterfactual comparison:
- ML: DK `1.650` / KT `2.205`
- KH: DK `-5.5 @1.930` / KT `+5.5 @1.826`
- Duration `31.5`: Over `1.780` / Under `1.968`
- Total Kills `27.5`: Over `1.909` / Under `1.861`

Frozen series benchmark remains unchanged:
- DK `P0=60%`
- KT `P0=40%`
- `TK0=25.45`
- Q2: `D_DIAGNOSTIC_ONLY=YES / D_PROBABILITY_CONTRIBUTION=0`.

## Corrected DIM

DK primary route:
- `Vi access -> Annie/Neeko layered CC -> Miss Fortune Bullet Time -> Renekton follow-up/frontline conversion`.

DK secondary route:
- `Renekton/Neeko flank or Annie pick -> short-range collapse -> MF zone/cleanup`.
- Unlike Jax, Renekton does **not** provide the same independent late side-lane/cleanup route into Gwen; the second route overlaps materially with DK's main committed engage geometry.

KT primary route:
- `Skarner displacement -> Kalista/Renata follow-up -> Akali/Gwen dive and cleanup`.

KT secondary route:
- `Gwen/Akali side-flank pressure -> split attention -> Skarner/Renata collapse around compulsory objective contact`.

Interaction rows:
- `TAM=MIXED`: Renata Bailout and Skarner disruption can blunt DK's first burst; DK still has deterministic Vi/Annie/Neeko access. DK has limited peel if Akali/Gwen reach MF after Vi commits.
- `OSG=DK_SLIGHT`: Annie/Neeko/MF remain strong choke/fog tools, but Kalista/Renata/Skarner contest objective setup well.
- `DAU=EVEN_TO_DK_SLIGHT`: DK has easier first target access; KT has better continuing melee backline access if the first burst does not decide the fight.
- `SLI=KT_SLIGHT`: Gwen is the more credible independent late side-lane threat against Renekton; replacing Jax removes DK's previous independent side-pressure argument.
- `FNF=DK_SLIGHT`: Renekton materially improves DK's immediate front-line occupancy and follow-up compared with Jax.
- `CAS=MIXED`: DK can cascade hard from one successful wombo, but Renata plus Gwen/Akali return-kill potential gives KT more real margin suppression than the erroneous Jax read credited.
- `ETS=DK_STRENGTH_PRIOR` from frozen benchmark.
- `AFP=NO CLEAR TWO-ROUTE DK CERTIFICATION`: DK's first wombo route is strong, but if Renata/Skarner disrupt that sequence, the corrected Renekton composition lacks the same independent Jax side/cleanup route.

Corrected diagnostic conclusion:
`D=0 / EVEN-STYLE-DEPENDENT`.

Q2 consequence: none for ML probability because draft contribution is quarantined at 0pp.

## Corrected price-blind family projections

### Moneyline
Unchanged by corrected draft under Q2:
- DK `60%`
- KT `40%`

At the historical board:
- DK @1.650 implied `60.61%`
- `MODEL_EDGE=-0.61pp`
- canonical forced side remains **DK ML** as the less-negative binary side.

### Kill Handicap
Corrected DK-perspective signed margin bins:
- DK `+10 or more`: `18%`
- DK `+6 to +9`: `18%`
- DK `+1 to +5`: `24%`
- KT `+1 to +5`: `20%`
- KT `+6 to +9`: `11%`
- KT `+10 or more`: `9%`

Sums to 100%; DK win mass remains 60%.
- DK `-5.5` raw cover = `36%`
- KT `+5.5` raw cover = `64%`
- `KH_CAPPED_PROB=64%`

At KT +5.5 @1.826 implied `54.76%`:
- `MODEL_EDGE=+9.24pp`
- canonical KH remains **KT +5.5**.

Interpretation: Renekton improves DK's grouped first-contact reliability, but removes the independent Jax late side/cleanup route; Renata/Gwen/Akali preserve meaningful return-kill and margin-compression branches.

### Duration
Corrected draft-only duration scores remain:
- `V=0 / Q=0 / H=0 / T=-1`
- `F=30.25m`

Reason: Renekton is more front-loaded than Jax, but draft theory alone is not enough to justify a `T=-2` strong-terminal-acceleration classification under the frozen Duration core.

At line 31.5:
- Under `58.75%`
- Under @1.968 implied `50.81%`
- `MODEL_EDGE=+7.94pp`
- canonical Duration remains **Under 31.5**.

### Total Kills
Corrected bins:
- `<20`: `11%`
- `20-24`: `20%`
- `25-27`: `14%`
- `28-32`: `29%`
- `33-37`: `17%`
- `38+`: `9%`

At 27.5:
- Over `55%`
- Under `45%`

Required branch allocation:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 21%`
- `TWO_SIDED_BRAWL / REPEATED_CONTACT = 38%`
- ordinary controlled/contested paths `41%`.

At Over 27.5 @1.909 implied `52.38%`:
- `MODEL_EDGE=+2.62pp`
- canonical TK remains **Over 27.5**.

## Corrected counterfactual pick set

Using the corrected Renekton draft but the exact same historical board, the four canonical forced-choice sides remain:
1. **DK ML @1.650**
2. **KT +5.5 @1.826**
3. **Under 31.5 @1.968**
4. **Over 27.5 @1.909**

Therefore the historical settlement would still be `2W-2L / -0.0955u` on the supplied final result DK 17-10 in 31:13, but this reassessment does **not** rewrite the ledger.

## Audit conclusion

The champion correction changes the draft diagnosis materially even though it does not change the four selected sides:
- diagnostic `D`: **DK +1 -> 0 / EVEN-STYLE-DEPENDENT**;
- KT +5.5 becomes somewhat stronger structurally because DK loses Jax's independent late side/cleanup mechanism;
- Under 31.5 is unchanged;
- Over 27.5 becomes slightly stronger from more front-loaded grouped contact, while still carrying substantial one-sided-fast-close suppression risk.

Keep historical G4 tagged `DATA-INTEGRITY MISMATCH`; use this corrected review, not the erroneous Jax DIM, for any future qualitative draft-audit reference.
