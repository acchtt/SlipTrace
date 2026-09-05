# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** CLOSED — SERIES COMPLETE / G4 BOARD-TRANSCRIPTION CORRECTION APPLIED / RENEKTON REASSESSMENT NO PICK CHANGE  
**Session lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Series closure

- LCK 2026 Season Playoffs — Lower Bracket Round 2 — KT Rolster vs Dplus KIA.
- G1-G2 had no prospective canonical Positions in this chat; no retroactive Positions were created.
- G3: DK won `19-4` in `26:56`; positions `3-1 / +0.40125u`.
- G4 final: DK won `17-10` in `31:13`.
- Series final: **Dplus KIA 3-1 KT Rolster**.
- KT-DK lock remains closed; no further Position may be created under it.

## 2. Frozen benchmark used for series

- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- `TK0=25.45`

Same-series results never changed K/P0/TK0.

## 3. G4 source-truth board correction

The pre-entry sportsbook screenshot was readable and existed before the G4 card. The assistant transcribed all four families incorrectly. Source-truth board:

- ML: **DK `1.719` / KT `2.047`**
- Duration `33.0`: **Over `1.869` / Under `1.869`**
- Total Kills `26.5`: **Over `2.086` / Under `1.692`**
- Kill Handicap: **DK `-4.5 @1.932` / KT `+4.5 @1.810`**

This is an operator transcription correction, not retroactive market creation, because the exact screenshot was supplied before the card.

Under the frozen Q2 rules, the corrected canonical card is:
1. **DK ML @1.719**
2. **DK -4.5 @1.932** — mandatory `<5` alignment with DK ML
3. **Under 33 @1.869**
4. **Over 26.5 @2.086**

Corrected price notes:
- DK ML: model `60%`, implied `58.17%`, `MODEL_EDGE=+1.83pp`, `FORCED_NEG_EV=NO`.
- DK -4.5: corrected-input cover estimate `42%`, implied `51.76%`, `MODEL_EDGE=-9.76pp`, `FORCED_NEG_EV=YES`; selected because `<5` KH must align with ML.
- Under 33: frozen `F=30.25m`, model `69.25%`, implied `53.50%`, `MODEL_EDGE=+15.75pp`, `FORCED_NEG_EV=NO`.
- Over 26.5: corrected-input estimate about `58%`, implied `47.94%`, `MODEL_EDGE≈+10.06pp`, `FORCED_NEG_EV=NO`.

## 4. G4 corrected settlement

Final result: DK `17-10`, duration `31:13`, total kills `27`, DK kill margin `+7`.

Corrected source-truth card settlement:
- DK ML @1.719 — **WIN** — `+0.17975u`
- DK -4.5 @1.932 — **WIN** — `+0.23300u`
- Under 33 @1.869 — **WIN** — `+0.21725u`
- Over 26.5 @2.086 — **WIN** — `+0.27150u`

**G4 corrected: `4W-0L / +0.90150u`; actual exposure `0u`.**

Airtable Positions were updated in place to these source-truth lines/results. No duplicate Positions were created.

## 5. Top-lane correction and reassessment: Jax -> Renekton

The entered G4 draft said DK top **Jax**, while the final scoreboard showed **Siwoo on Renekton**. Reassessment was completed using the actual draft:
- DK: `Renekton / Vi / Annie / Miss Fortune / Neeko`
- KT: `Gwen / Skarner / Akali / Kalista / Renata`.

Reassessed interaction read:
- DK retains deterministic `Vi -> Annie/Neeko -> MF` grouped access with Renekton follow-up/frontline.
- Replacing Jax with Renekton removes the cleaner independent late side-lane/cleanup route and shifts the diagnostic DIM from `D=+1 DK` to **`D=0 / EVEN-STYLE-DEPENDENT`**.
- Under Q2, `D_PROBABILITY_CONTRIBUTION=0`, so ML remains frozen DK `60%`.
- The corrected source-truth canonical selections remain exactly **DK ML / DK -4.5 / Under 33 / Over 26.5**.

Because the full corrected-draft reassessment leaves all four canonical selections unchanged, **no `DATA-INTEGRITY MISMATCH` tag applies to G4**. Retain the Jax->Renekton note only as a neutral retrospective input correction and use the Renekton-based DIM, not the obsolete Jax-based DIM, for any later draft-mechanism review.

## 6. Corrected cohort after series

After replacing the operator-misread G4 board with source truth:
- `48 Positions / 12 per family`
- overall **`24W-24L / -0.77275u`**
- ML **`3-9 / -1.71425u`**
- KH **`6-6 / -0.16750u`**
- Duration **`9-3 / +1.23700u`**
- TK **`6-6 / -0.12800u`**
- actual exposure `0u`.

Preferred structural checkpoint remains `80 total / 20 per family`.

## 7. Next-session requirement

Before any new LoL Position:
1. load canonical bootstrap;
2. observe KT-DK lock is closed;
3. identify the next current match fresh;
4. build a fresh price-independent Gol.gg benchmark;
5. create a fresh Session Authority Lock;
6. load the newest applicable handoff last.

No KT-DK lock reuse.
