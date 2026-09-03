# Current Live Handoff — Dplus KIA vs BNK FearX — 2026-09-03

**Status:** ACTIVE SERIES HANDOFF — GAME 4 POSITIONS LOCKED / BFX LEADS 2-1 / AIRTABLE DEFERRED TO G4 MAP END  
**Session lock:** `LOL-2026-09-03-V13-DK-BFX-DRAFTONLY-FORCEDCHOICE-1644-UTC7`  
**Authority commit:** `7420942bee48a943a076239d2b9acf074fb833f0`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Current series state

- Dplus KIA (DK) vs BNK FearX (BFX)
- LCK 2026 Season Playoffs — Lower Bracket Round 1
- Bo5 Fearless Draft
- **Series score entering Game 4: BFX 2-1 DK.**
- Same-series results remain quarantined from benchmark construction and never update K/P0.
- G1-G2 had no canonical chat Positions and remain unrecorded prospectively.

## 2. Frozen pre-series benchmark

- `B(DK)=+0.334587`
- `B(BFX)=+0.010432`
- `GAP(DK-BFX)=+0.324155 SD`
- `DK K=0 / P0=50%`
- `BFX K=0 / P0=50%`
- Frozen Total Kills baseline: `TK0=28.4`

`TEAM_BENCH[LEAGUE=LCK2026;CURRENT=R3-4;PREVIOUS=R1-2;G_DK=20;G_BFX=20;B_CUR_DK=0.174447;B_CUR_BFX=0.278708;B_PREV_DK=0.412956;B_PREV_BFX=-0.624751;BLEND_DK=0.246000;BLEND_BFX=0.007670;B_DK=0.334587;B_BFX=0.010432;GAP_DK_BFX=0.324155;K_DK=0;K_BFX=0;ROSTER_ADJ=NORMAL;PRICE_USED=N;SAME_SERIES_USED=N]`

## 3. Game 3 settlement

Final user-supplied result:
- DK win
- final kills `13-12` DK
- total kills `25`
- duration `31:57`

Canonical Game 3 results:
- BFX ML @2.278 — Loss `-0.2500u`
- BFX +5.5 @1.900 — Win `+0.2250u`
- Under 33 @1.847 — Win `+0.21175u`
- Over 27.5 kills @1.928 — Loss `-0.2500u`

Game 3 result: `2W-2L / -0.06325u`.
Airtable map + four Positions were written at map end.

Cohort after G3 settlement:
- `32 canonical Positions / 8 per family`
- `15W-17L`
- shadow P/L `-1.06125u`
- actual exposure `0u`
- checkpoint remains `40 positions / 10 per family` => `2 more fully recorded maps / 8 positions`.

Micro-audit: G3 had `D=0 / EVEN-STYLE-DEPENDENT`; DK winning does not imply a directional DIM classification miss. KH and Duration were correct; ML and Total Kills were wrong. No coefficient change before checkpoint.

## 4. Game 4 final draft and board

User-supplied screenshot resolves roles as:

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

Supplied Game 4 board:
- Moneyline: DK `1.423` / BFX `2.720`
- Duration 32: Over `1.765` / Under `1.985`
- Total Kills 25.5: Over `1.703` / Under `2.070`
- Kill Handicap: DK `-7.5 @1.804` / BFX `+7.5 @1.938`

Displayed `1:49`, kill score, and all other live-state evidence are ignored under the draft-only lock.

## 5. Game 4 full price-blind DIM

DK mechanisms:
- `PKM`: Twisted Fate global/Gold Card creates a first catch -> Naafiri burst/collapse -> Yorick side pressure converts cross-map.
- `SKM`: Yunara + Lulu kite/reset while Yorick occupies side lane and TF threatens cross-map reinforcement.

BFX mechanisms:
- `PKM`: Hecarim engage + Lissandra hard lock -> Rumble Equalizer zone -> Zeri follow/cleanup, with Yuumi attached to the primary entry/carry.
- `SKM`: Hecarim/Lissandra mobility collapses side-map assignments and creates repeated catch windows, then Zeri-Yuumi cleans extended fights.

Interaction rows:
- `TAM=BFX ADV`: Hecarim fear + Lissandra lock + Rumble zone overload DK's mostly single-target/peel-oriented answers. Lulu can disrupt one entry, but DK cannot reliably stop the full engage chain.
- `OSG=BFX ADV`: Rumble Equalizer plus Hecarim/Lissandra entry gives BFX superior direct neutral-objective choke control. DK's best answer is side-map trade rather than symmetric front-door contest.
- `DAU=BFX ADV`: BFX can repeatedly access Yunara/TF/Lulu; DK's Naafiri/TF access onto Zeri-Yuumi must cross Hecarim/Lissandra/Rumble counter-engage and Zeri mobility.
- `SLI=DK SLIGHT`: Yorick + TF is DK's clearest independent side-map route, but BFX Hecarim/Lissandra mobility can collapse that setup and reduce its reliability around objectives.
- `FNF=BFX ADV`: BFX has a more coherent grouped fight shell and repeatable first-entry pattern; DK is more assignment-dependent and lacks a comparable durable front line.
- `CAS=BFX ADV`: one Hecarim/Lissandra connection can chain immediately through Equalizer into Zeri reset pursuit. DK has a pick-cascade route through TF/Naafiri, but it is more target- and assignment-dependent.
- `ETS=EVEN`: frozen benchmark remains K=0 / 50-50 and does not independently break the tie.
- `AFP=PASS / BFX EDGE CERTIFIED`: DK failure path is credible through Yorick split + TF cross-map + Lulu/Yunara kite, but it does not erase both BFX mechanisms: direct grouped engage overload and independent side-collapse/cleanup mobility.

Final certification:
`DIM[ROLES=P;PKM_DK=TF_CATCH->NAAFIRI_COLLAPSE;SKM_DK=YORICK_SIDE+YUNARA_LULU_KITE;PKM_BFX=HEC_LISS_ENGAGE->RUMBLE_ZONE->ZERI_CLEANUP;SKM_BFX=SIDE_COLLAPSE+RESET_CARRY;TAM=BFX_ADV;OSG=BFX_ADV;DAU=BFX_ADV;SLI=DK_SLIGHT;FNF=BFX_ADV;CAS=BFX_ADV;ETS=EVEN;AFP=P;EDGE=BFX]`

Post-audit draft edge:
- `D=+1 BFX`.
- At least two independent BFX mechanism advantages survive adversarial failure-path review.

## 6. Game 4 locked family projections before price pass

### Moneyline
With `P0(BFX)=50%` and `D=+1 BFX`:
- BFX `54.5%`
- DK `45.5%`

### Kill Handicap signed final-margin distribution
DK-perspective final kill-margin bins, locked before pricing:
- DK `+10 or more`: `7%`
- DK `+8 to +9`: `8%`
- DK `+1 to +7`: `30.5%`
- BFX `+1 to +7`: `26.5%`
- BFX `+8 to +9`: `12%`
- BFX `+10 or more`: `16%`

Sums to 100%; BFX win probability = `54.5%`, consistent with ML.
Derived cover:
- BFX `+7.5`: `85.0%`
- DK `-7.5`: `15.0%`

Because absolute handicap is `7.5`, KH may remain independent under the portfolio-coherence rule.

### Duration
Draft-only t=0 scoring:
- `V=0`
- `Q=0`
- `H=0`
- `T=0`

`F=31.0 minutes`.
At line 32:
- `P(OVER)=43.0%`
- `P(UNDER)=57.0%`

### Total Kills
Frozen `TK0=28.4`.
Draft-adjusted bins:
- `<20`: `6%`
- `20-25`: `32%`
- `26-30`: `30%`
- `31-35`: `19%`
- `36+`: `13%`

Sums to 100%.
At line 25.5:
- `P(OVER)=62%`
- `P(UNDER)=38%`

Drivers: BFX has repeated forced-contact inventory through Hecarim/Lissandra/Rumble and Zeri reset pursuit; DK has TF/Naafiri catch and side-collapse routes. Counterweight is DK's Yorick side-map plan, which can reduce direct 5v5 frequency.

## 7. Game 4 canonical forced-choice Positions

Exactly one canonical Position per family:

1. **Moneyline — BFX ML @2.720 — 0.25u shadow / 0u actual**
   - model `54.5%`
   - raw implied `36.76%`
   - `MODEL_EDGE=+17.74pp`
   - `FORCED_NEG_EV=NO`

2. **Kill Handicap — BFX +7.5 @1.938 — 0.25u shadow / 0u actual**
   - model cover `85.0%`
   - raw implied `51.60%`
   - `MODEL_EDGE=+33.40pp`
   - `FORCED_NEG_EV=NO`

3. **Duration — Under 32:00 @1.985 — 0.25u shadow / 0u actual**
   - locked `F=31.0m`
   - model Under `57.0%`
   - raw implied `50.38%`
   - `MODEL_EDGE=+6.62pp`
   - `FORCED_NEG_EV=NO`

4. **Total Kills — Over 25.5 @1.703 — 0.25u shadow / 0u actual**
   - model Over `62.0%`
   - raw implied `58.72%`
   - `MODEL_EDGE=+3.28pp`
   - `FORCED_NEG_EV=NO`

Game 4 shadow total: `1.00u`; actual exposure: `0u`.

## 8. Persistence / settlement rule

- GitHub handoff contains G3 settlement state plus the locked G4 pre-price analytical record and four selected positions.
- Airtable is **not** written for G4 at entry; write is deferred until Game 4 ends.
- At G4 map end, settle the map and all four canonical Positions in one Airtable batch, then run the full micro-audit and update cohort state.
- No live-state reassessment or new G4 prediction is permitted after map start under this draft-only execution mode.
