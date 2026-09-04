# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** CLOSED — SERIES COMPLETE / G4 BOARD-TRANSCRIPTION CORRECTION APPLIED / RETROSPECTIVE DRAFT CORRECTION SEPARATE  
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

## 5. Separate draft-input correction: Jax -> Renekton

The user-entered G4 draft said DK top **Jax**, while the final scoreboard shows **Siwoo on Renekton**. This champion correction was learned only from the later final scoreboard, so it remains a **retrospective corrected-input draft audit**, distinct from the pre-entry board-transcription correction above.

Corrected actual draft:
- DK: `Renekton / Vi / Annie / Miss Fortune / Neeko`
- KT: `Gwen / Skarner / Akali / Kalista / Renata`

Retrospective DIM with Renekton:
- DK still has deterministic `Vi -> Annie/Neeko -> MF` grouped access and Renekton follow-up/frontline.
- Replacing Jax with Renekton removes the cleaner independent late side-lane/cleanup route and makes DK more reliant on first-contact 5v5 conversion.
- KT retains Skarner/Renata disruption plus Akali/Gwen counter-dive and side pressure.
- corrected diagnostic draft label: **`D=0 / EVEN-STYLE-DEPENDENT`** rather than the original `D=+1 DK`.
- under Q2, `D_PROBABILITY_CONTRIBUTION=0`, so ML remains frozen DK `60%` either way.

Do not use the original Jax-based DIM as clean champion-draft calibration evidence. The corrected Renekton audit may be retained as retrospective mechanism review, but it does not prove what was knowable at entry.

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
