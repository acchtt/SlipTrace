# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** ACTIVE SERIES HANDOFF — GAME 4 SETTLED / SERIES 2-2 / GAME 5 NEXT / 40-POSITION CHECKPOINT ONE MAP AWAY  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Current series state

- Dplus KIA (DK) vs BNK FearX (BFX)
- LCK 2026 Season Playoffs — Lower Bracket Round 1
- Bo5 Fearless Draft
- G1-G2 had no prospective canonical Positions in this chat and remain unrecorded.
- G3: DK win.
- G4: DK win.
- **Series score entering Game 5: DK 2-2 BFX.**
- Same-series results remain quarantined from benchmark construction and never update K/P0.
- Same-series maps may inform only structurally required Fearless champion availability.

## 2. Frozen pre-series benchmark

- `B(DK)=+0.334587`
- `B(BFX)=+0.010432`
- `GAP(DK-BFX)=+0.324155 SD`
- `DK K=0 / P0=50%`
- `BFX K=0 / P0=50%`
- frozen Total Kills baseline: `TK0=28.4`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`

## 3. Game 3 settlement

Final:
- DK win
- kills `13-12` DK
- total kills `25`
- duration `31:57`

Canonical results:
- BFX ML @2.278 — Loss `-0.2500u`
- BFX +5.5 @1.900 — Win `+0.2250u`
- Under 33 @1.847 — Win `+0.21175u`
- Over 27.5 kills @1.928 — Loss `-0.2500u`

G3: `2W-2L / -0.06325u`.
Airtable map + four positions written at map end.

Micro-audit: `D=0 / EVEN-STYLE-DEPENDENT`; no directional DIM miss. KH and Duration correct; ML and TK wrong. No coefficient change before checkpoint.

## 4. Game 4 final draft / locked analytics

BFX:
- Clear — Rumble TOP
- Raptor — Hecarim JUNGLE
- VicLa — Lissandra MID
- Taeyoon — Zeri ADC
- Kellin — Yuumi SUPPORT

DK:
- Siwoo — Yorick TOP
- Lucid — Naafiri JUNGLE
- ShowMaker — Twisted Fate MID
- Smash — Yunara ADC
- Career — Lulu SUPPORT

Board:
- ML: DK `1.423` / BFX `2.720`
- Duration 32: Over `1.765` / Under `1.985`
- TK 25.5: Over `1.703` / Under `2.070`
- KH: DK `-7.5 @1.804` / BFX `+7.5 @1.938`

Price-blind DIM certification:
`DIM[ROLES=P;PKM_DK=TF_CATCH->NAAFIRI_COLLAPSE;SKM_DK=YORICK_SIDE+YUNARA_LULU_KITE;PKM_BFX=HEC_LISS_ENGAGE->RUMBLE_ZONE->ZERI_CLEANUP;SKM_BFX=SIDE_COLLAPSE+RESET_CARRY;TAM=BFX_ADV;OSG=BFX_ADV;DAU=BFX_ADV;SLI=DK_SLIGHT;FNF=BFX_ADV;CAS=BFX_ADV;ETS=EVEN;AFP=P;EDGE=BFX]`

- `D=+1 BFX`
- ML projection: BFX `54.5%`
- KH cover projection: BFX +7.5 `85.0%`
- Duration: `V=0,Q=0,H=0,T=0,F=31.0m`; Under 32 `57.0%`
- TK bins implied Over 25.5 `62.0%`

Canonical G4 positions:
- BFX ML @2.720 — `MODEL_EDGE=+17.74pp`, `FORCED_NEG_EV=NO`
- BFX +7.5 @1.938 — `MODEL_EDGE=+33.40pp`, `FORCED_NEG_EV=NO`
- Under 32 @1.985 — `MODEL_EDGE=+6.62pp`, `FORCED_NEG_EV=NO`
- Over 25.5 @1.703 — `MODEL_EDGE=+3.28pp`, `FORCED_NEG_EV=NO`

## 5. Game 4 settlement

User-supplied final screenshot:
- **DK win**
- duration `22:43`
- kills `16-6` DK
- total kills `22`
- towers `6-2` DK
- dragons `2-0` DK
- barons `1-0` DK
- inhibitors `1-0` DK

Canonical results:
- BFX ML @2.720 — Loss `-0.2500u`
- BFX +7.5 @1.938 — Loss `-0.2500u`
- Under 32 @1.985 — Win `+0.24625u`
- Over 25.5 @1.703 — Loss `-0.2500u`

G4 result: `1W-3L / -0.50375u`.
Airtable map + four Positions written at map end.

### G4 micro-audit

- **Moneyline/DIM:** directional miss. BFX `D=+1` failed; DK won decisively. The certified BFX mechanisms did not materialize strongly enough to overcome DK's side/catch/kite route. Do not change DIM coefficients or certification thresholds yet; preserve this as checkpoint evidence.
- **Kill Handicap:** severe distribution miss. Model assigned BFX +7.5 cover `85%`; actual BFX margin was `-10`. This must be inspected at the 40-position audit for excessive confidence/tail compression and interaction with D certification.
- **Duration:** correct. Neutral `F=31.0m` selected Under 32; final was much faster at `22:43`. Direction correct but magnitude under-modeled; do not retune from one map.
- **Total Kills:** miss. Model Over 25.5 `62%`; final `22`. Review whether forced-contact inventory was overweighted relative to one-sided fast-close suppression of return kills.
- **Governance:** no structural coefficient change before checkpoint unless implementation bug is discovered. No bug identified from settlement alone.

## 6. Forced-choice cohort after Game 4

Total:
- `36 canonical Positions`
- `9 per family`
- `16W-20L`
- shadow P/L `-1.5650u`
- actual exposure `0u`

By family:
- ML `1-8 / -1.8305u`
- KH `4-5 / -0.3725u`
- Duration `6-3 / +0.5375u`
- Total Kills `5-4 / +0.1005u`

Checkpoint:
- target `40 positions / 10 per family`
- **one more fully recorded map / 4 positions needed**
- Game 5 settlement, if all four canonical families execute, triggers the full 40-position checkpoint audit.

## 7. Standing Game 5 workflow

When final G5 draft + exact board are supplied:
1. keep frozen benchmark `K=0 / P0=50-50 / TK0=28.4`;
2. use G1-G4 only for Fearless champion availability, never as strength evidence;
3. lock full price-blind `PKM / SKM / TAM / OSG / DAU / SLI / FNF / CAS / ETS / AFP` before D;
4. certify `D=+1/-1` only with at least two independent surviving mechanisms; otherwise `D=0 / EVEN-STYLE-DEPENDENT`;
5. lock full signed KH margin distribution before price;
6. KH rule: handicap `<5` must align with selected ML; `±5.5` or wider may be independent;
7. lock Duration `V/Q/H/T/F` and full TK bins before price;
8. exactly one ML/KH/Duration/TK canonical forced choice, `0.25u shadow / 0u actual` each;
9. tag all selections `MODEL_EDGE` and `FORCED_NEG_EV`;
10. Airtable only at map end; after G5 settlement run the full 40-position checkpoint audit before any structural model change.
