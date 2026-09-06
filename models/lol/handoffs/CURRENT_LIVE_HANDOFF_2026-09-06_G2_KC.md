# Current Live Handoff — G2 Esports vs Karmine Corp — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — G1/G2/G3/G4 PROSPECTIVELY LOCKED / UNSETTLED  
**Session lock:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u EACH / 0u ACTUAL`

## Match

G2 Esports vs Karmine Corp — LEC 2026 Summer Playoffs Upper Bracket Final, Bo5 Fearless Draft.

Frozen pre-series benchmark remains unchanged:
- `B(G2)=+1.000135`
- `B(KC)=+1.625030`
- `GAP(KC-G2)=+0.624895 SD`
- `KC K=+1 / P0=55%`
- `G2 K=-1 / P0=45%`
- `TK0=30.15 kills`

Same-series outcomes do not update `B/K/P0/TK0`; prior maps may affect only Fearless champion availability. Draft `D` is diagnostic-only and contributes 0pp to ML probability.

## Game 1 — PROSPECTIVE / UNSETTLED
Draft KC blue: Jayce / Vi / Ahri / Caitlyn / Bard.  
G2: K'Sante / Xin Zhao / Viktor / Ezreal / Karma.

Card:
- `KC ML @1.908`
- `KC +3.5 @1.825`
- `Under 33 @1.817`
- `Under 27.5 @1.739`

Diagnostic draft: `D=+1 KC`, contribution `0pp`.

## Game 2 — PROSPECTIVE / UNSETTLED
Draft G2 blue: Camille / Jarvan IV / Galio / Yunara / Lulu.  
KC: Olaf / Lee Sin / Orianna / Lucian / Milio.

Card:
- `KC ML @1.838`
- `KC +3.5 @1.832`
- `Under 33 @1.748`
- `Over 27.5 @1.897`

Diagnostic draft: `D=+1 G2`, contribution `0pp`.

## Game 3 — PROSPECTIVE / UNSETTLED
The source-truth sportsbook board was explicitly labeled Game 3.

Draft KC blue: Zaahen / Cho'Gath / Syndra / Xayah / Rakan.  
G2: Ambessa / Qiyana / Ryze / Varus / Alistar.

Card:
- `KC ML @1.965`
- `KC +3.5 @1.822`
- `Under 33 @1.711`
- `Over 27.5 @1.792`

Diagnostic draft: `D=+1 KC`, contribution `0pp`.

## Game 4 — PROSPECTIVE / UNSETTLED
The supplied G4 screen shows G2 leading the series `2-1`. This same-series score is context only; it does not modify the frozen benchmark or prior.

Draft:
- KC blue: Gnar / Trundle / Sylas / Ashe / Seraphine
- G2: Rumble / Maokai / Tristana / Miss Fortune / Nautilus

Board:
- ML G2 `2.016` / KC `1.741`
- Duration 32: Over `1.833` / Under `1.906`
- Total Kills 27.5: Over `1.919` / Under `1.804`
- KH G2 +3.5 `1.817` / KC -3.5 `1.924`

Canonical card:
- `KC ML @1.741`
- `KC -3.5 @1.924`
- `Under 32 @1.906`
- `Over 27.5 @1.919`
- `0.25u each / 1.00u total shadow / 0u actual`

Model/price:
- KC ML model `55%` vs implied `57.44%` => `-2.44pp`, `FORCED_NEG_EV=YES`; actual execution `PASS`
- KC -3.5 raw cover `38%` vs implied `51.98%` => `-13.98pp`, `FORCED_NEG_EV=YES`; abs handicap `<5` therefore aligned with selected ML side
- Under 32: `V0/Q0/H0/T-1`, `F=30.25m`, model `62.25%` vs implied `52.47%` => `+9.78pp`
- Over 27.5 model `66%` vs implied `52.11%` => `+13.89pp`

Full DIM diagnostic: `D=+1 G2`, contribution `0pp`.
- G2 PKM: Maokai/Nautilus engage layers Rumble Equalizer + Miss Fortune Bullet Time, with Tristana cleanup.
- G2 SKM: Maokai/Nautilus pick pressure can create numbers and immediate objective/structure conversion through Tristana.
- KC PKM: Ashe arrow / Trundle pillar / Seraphine control into Sylas follow-up with Gnar flank.
- KC SKM: Ashe-Seraphine kite/disengage plus Trundle disruption can blunt the first engage and create a front-to-back recovery route.
- Adversarial pass: KC retains real anti-engage and stolen-ultimate counterplay, but G2 still has two independent surviving advantages: layered initiation and high AoE conversion. `AFP=PASS_G2_EDGE`.

KH signed margin bins from KC perspective:
- KC 10+ `16%`
- KC 4-9 `22%`
- KC 1-3 `17%`
- G2 1-3 `16%`
- G2 4-9 `17%`
- G2 10+ `12%`

KC -3.5 cover = `38%`. Explicit 10+ tails: KC `16%`, G2 `12%`.

Duration pre-price: `V0/Q0/H0/T-1`, `F=30.25m`.

TK bins: `<20 6% / 20-24 10% / 25-27 18% / 28-32 28% / 33-37 22% / 38+ 16%`; Over 27.5 model `66%`. Suppression: fast-close return-kill suppression `16%`; low-contact extended-game `5%`.

## Cohort entering G2-KC

- `96 settled positions / 24 per family / 24 settled maps`
- overall `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

No G2-KC Airtable write occurs until explicit map-end final evidence. G1/G2/G3/G4 remain unsettled in the canonical ledger.

## Next action

**AWAIT EXPLICIT G1/G2/G3/G4 FINAL EVIDENCE OR NEXT FULLY SUPPLIED MAP DRAFT + BOARD.**