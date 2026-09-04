# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** ACTIVE SERIES HANDOFF — GAME 3 POSITIONS LOCKED / Q2 VALIDATION  
**Session lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Series / cohort state

- KT Rolster vs Dplus KIA — LCK 2026 Season Playoffs Lower Bracket Round 2, Bo5 Fearless Draft.
- G1-G2 have no prospective canonical Positions in this chat because no final draft + exact board was supplied before those maps; no retroactive Positions may be created.
- Game 3 is the first canonical map under this lock in this chat.
- Same-series outcomes remain quarantined from K/P0 and TK0 and may inform only Fearless champion availability.
- Airtable remains untouched for G3 until map end.

Cohort entering G3:
- `40 Positions / 10 per family`
- `17W-23L / -2.0755u`
- ML `1-9 / -2.0805u`
- KH `4-6 / -0.6225u`
- Duration `7-3 / +0.7770u`
- TK `5-5 / -0.1495u`
- actual exposure `0u`.

## 2. Frozen benchmark

Roster-adjusted pre-series Gol.gg benchmark remains frozen:
- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- `TK0=25.45`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_KT=21;B_CUR_DK=0.174447;B_CUR_KT=-1.458375;B_PREV_DK=0.412956;B_PREV_KT=0.503116;BLEND_DK=0.246000;BLEND_KT=-1.164151;B_DK=0.355702;B_KT=-1.465479;GAP_DK_KT=1.821180;K_DK=+2;K_KT=-2;ROSTER_ADJ_DK=NORMAL70_30;ROSTER_ADJ_KT=ONE_STARTER_85_15;PRICE_USED=N;PLAYOFF_RESULT_USED=N;SAME_SERIES_USED=N]`.

## 3. Game 3 final draft / exact board

User-supplied role order TOP / JUNGLE / MID / ADC / SUPPORT:

KT blue:
- Ambessa
- Cho'Gath
- Syndra
- Varus
- Nautilus

DK red:
- Gnar
- Trundle
- Viktor
- Jhin
- Leona

Board:
- ML: DK `1.746` / KT `2.010`
- Duration 33: Over `1.777` / Under `1.971`
- Total Kills 26.5: Over `2.207` / Under `1.620`
- Kill Handicap: DK `-3.5 @1.888` / KT `+3.5 @1.850`

Displayed in-map clock/state is ignored for prediction by the draft-only lock.

## 4. G3 full price-blind DIM

KT mechanisms:
- `PKM`: Nautilus first access -> Syndra/Cho'Gath chained control + burst -> Varus follow-up -> Ambessa dive/cleanup.
- `SKM`: Varus/Syndra pre-contact pressure plus Cho/Naut choke occupation -> force DK through constrained objective entries -> Ambessa flank/collapse.

DK mechanisms:
- `PKM`: Leona/Jhin catch -> Viktor burst/zone -> Gnar follow-up or flank.
- `SKM`: Trundle pillar + Subjugate degrades Cho/Naut front line -> Viktor/Jhin control the approach -> Gnar converts grouped contact.

Interaction rows:
- `TAM=MIXED`: Trundle R directly punishes KT's heavy front line and DK has several counter-engage tools, but those do not fully answer Nautilus point-and-click access plus Ambessa follow-through.
- `OSG=KT_SLIGHT`: Varus/Syndra range with Cho/Naut choke occupation gives KT the easier first-position objective geometry; Viktor/Jhin/Trundle can still contest entrances.
- `DAU=KT_SLIGHT`: KT has more reliable access onto Jhin/Viktor through Naut/Ambessa; DK's Jhin is less comfortable into Cho/Naut unless Trundle has already stripped the front line.
- `SLI=EVEN`: Gnar and Ambessa each provide credible side pressure; neither route is sufficiently independent to decide the draft.
- `FNF=KT_SLIGHT`: Cho/Naut give KT the simpler sustained front-to-back shell; DK has enough functional front line through Gnar/Trundle/Leona that this is not a large edge.
- `CAS=KT_SLIGHT`: once KT gains vision/control, repeated Naut/Cho entry denial and Ambessa follow-up can make the next compulsory cycle easier; DK retains meaningful anti-cascade via pillar, Viktor zone and Gnar counter-engage.
- `ETS=DK_STRENGTH_PRIOR`: frozen benchmark favors DK materially, but ETS does not reverse the interaction map by fiat.
- `AFP=PASS / KT DIAGNOSTIC EDGE`: DK's strongest counter-route is Trundle shredding KT's front line while Viktor/Jhin kite the forced entry. It is real, but two KT routes survive: direct chained access and pre-objective choke/pick control.

Final diagnostic certification:
`DIM[ROLES=P;PKM_KT=NAUT_ACCESS->SYNDRA_CHO_CC_BURST->VARUS->AMBESSA;SKM_KT=RANGE+CHOKE->OBJECTIVE_ENTRY_FORCE->FLANK;PKM_DK=LEONA_JHIN_CATCH->VIKTOR->GNAR;SKM_DK=TRUNDLE_FRONTLINE_SHRED+PILLAR->VIKTOR_JHIN_CONTROL;TAM=MIXED;OSG=KT_SLIGHT;DAU=KT_SLIGHT;SLI=EVEN;FNF=KT_SLIGHT;CAS=KT_SLIGHT;ETS=DK_STRENGTH;AFP=P;EDGE=KT]`

`D=+1 KT`, but under Q2: `D_DIAGNOSTIC_ONLY=YES / D_PROBABILITY_CONTRIBUTION=0`.

## 5. G3 locked price-blind family projections

### Moneyline
Q2 forced-choice ML uses frozen P0 only:
- DK `60%`
- KT `40%`

### Kill Handicap signed final-margin distribution
DK-perspective bins, locked before line/price:
- DK `+10 or more`: `18%`
- DK `+5 to +9`: `22%`
- DK `+4`: `8%`
- DK `+1 to +3`: `12%`
- KT `+1 to +4`: `18%`
- KT `+5 to +9`: `13%`
- KT `+10 or more`: `9%`

Sums to 100%; DK win mass `60%`, consistent with Q2 ML P0.
- raw DK `-3.5` cover = `48%`
- `KH_CAPPED_PROB=48%` (below 70% cap)
- because `3.5 < 5`, portfolio rule requires KH to align with selected ML team; DK ML therefore forces DK -3.5 rather than opposite-side KT +3.5.

### Duration
Draft-only scoring:
- `V=0`
- `Q=0`
- `H=0`
- `T=-1`

`F = 31.0 + 0.75(-1) = 30.25m`.
At line 33:
- Under `69.25%`
- Over `30.75%`

Acceleration mechanism: both teams have reliable compulsory-contact tools and limited clean reset once first access lands; DK can also convert a caught front line through Trundle shred plus Viktor/Gnar follow-up.

### Total Kills
Frozen `TK0=25.45`.
Pre-price bins:
- `<20`: `12%`
- `20-24`: `23%`
- `25-26`: `15%`
- `27-31`: `27%`
- `32-36`: `15%`
- `37+`: `8%`

Sums to 100%.
At line 26.5:
- Over `50%`
- Under `50%`

Required branch mass:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 22%`
- `TWO_SIDED_BRAWL / REPEATED_CONTACT = 31%`
- remaining `47%` ordinary controlled/contested paths.

## 6. G3 canonical forced-choice Positions

1. **Moneyline — DK ML @1.746 — 0.25u shadow / 0u actual**
   - model `60.0%`
   - implied `57.27%`
   - `MODEL_EDGE=+2.73pp`
   - `FORCED_NEG_EV=NO`
   - `D_DIAGNOSTIC_ONLY=YES`.

2. **Kill Handicap — DK -3.5 @1.888 — 0.25u shadow / 0u actual**
   - raw/capped cover `48.0%`
   - implied `52.97%`
   - `MODEL_EDGE=-4.97pp`
   - `FORCED_NEG_EV=YES`
   - selection is mandatory portfolio alignment because absolute KH `<5` and ML side is DK.

3. **Duration — Under 33:00 @1.971 — 0.25u shadow / 0u actual**
   - `F=30.25m`
   - model Under `69.25%`
   - implied `50.74%`
   - `MODEL_EDGE=+18.51pp`
   - `FORCED_NEG_EV=NO`.

4. **Total Kills — Over 26.5 @2.207 — 0.25u shadow / 0u actual**
   - model Over `50.0%`
   - implied `45.31%`
   - `MODEL_EDGE=+4.69pp`
   - `FORCED_NEG_EV=NO`.

G3 shadow total `1.00u`; actual exposure `0u`.

## 7. Settlement discipline

- No G3 live-state reassessment or replacement Position after entry.
- Airtable write is deferred until map end.
- On final result: settle map + exactly these four canonical Positions, run full post-map micro-audit, then update cohort from 40 to 44 Positions.
