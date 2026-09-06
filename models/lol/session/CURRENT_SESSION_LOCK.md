# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Final — G2 Esports vs Karmine Corp — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 15:00 UTC / 22:00 UTC+7`  
**Activation:** `2026-09-06 18:59 UTC+7`  
**Current target:** `Game 2 prospectively locked; G1/G2 unsettled`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Active analytical model:** `LoL v1.3 — benchmark-aware core + lock-scoped Draft-Only Forced-Choice Validation Block Q3`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / 0.25u EACH / 0u ACTUAL`

## Authority boundary

Canonical `models/lol/CURRENT_MODEL.md` remains unchanged. Q3 forced-choice overlay is active prospectively for this series.

Frozen pre-series benchmark:
- `B(G2)=+1.000135`
- `B(KC)=+1.625030`
- `GAP(KC-G2)=+0.624895 SD`
- `KC K=+1 / P0=55%`
- `G2 K=-1 / P0=45%`
- `TK0=30.15 kills`

No sportsbook price or same-series result alters `B/K/P0/TK0`; prior maps may affect only Fearless champion availability.

Q3 controls remain:
- `D_DIAGNOSTIC_ONLY=YES`, `D_PROBABILITY_CONTRIBUTION=0`;
- ML floor `1.45` is execution eligibility only;
- KH requires full signed margin bins, explicit 10+ tails, 70% reporting cap; abs handicap `<5` aligns with selected ML;
- Duration v1.1 formula and 31m anchor unchanged; selected Over is shadow-only;
- TK persists explicit fast-close suppression and low-contact extended-game branches;
- exactly one ML/KH/Duration/TK shadow position per fully supplied map; `0.25u each / 0u actual`;
- Airtable only at map end; no retroactive positions; displayed live state ignored for draft-only prediction.

## Prospective positions

### Game 1 — UNSETTLED
Draft KC blue: Jayce / Vi / Ahri / Caitlyn / Bard.  
G2: K'Sante / Xin Zhao / Viktor / Ezreal / Karma.

Card:
- KC ML `@1.908`
- KC +3.5 `@1.825`
- Under 33 `@1.817`
- Under 27.5 kills `@1.739`

Diagnostic: `D=+1 KC`, probability contribution `0pp`.

### Game 2 — UNSETTLED
Draft G2 blue: Camille / Jarvan IV / Galio / Yunara / Lulu.  
KC: Olaf / Lee Sin / Orianna / Lucian / Milio.

Board:
- G2 ML `1.901` / KC ML `1.838`
- Duration 33: O `2.007` / U `1.748`
- TK 27.5: O `1.897` / U `1.825`
- KH G2 -3.5 `1.906` / KC +3.5 `1.832`

Card:
- KC ML `@1.838` — model 55%, implied 54.41%, edge `+0.59pp`
- KC +3.5 `@1.832` — raw/model 69%, implied 54.59%, edge `+14.41pp`
- Under 33 `@1.748` — `V0/Q0/H0/T-1`, `F=30.25m`, model 69.25%, implied 57.21%, edge `+12.04pp`
- Over 27.5 `@1.897` — model 65%, implied 52.71%, edge `+12.29pp`

Diagnostic draft: `D=+1 G2`, probability contribution `0pp`.

KH signed-margin bins from G2 perspective: G2 10+ `13%`, G2 4-9 `18%`, G2 1-3 `14%`, KC 1-3 `15%`, KC 4-9 `19%`, KC 10+ `21%`.

TK bins: `<20 8% / 20-24 11% / 25-27 16% / 28-32 27% / 33-37 21% / 38+ 17%`.  
Fast-close suppression `17%`; low-contact extended-game branch `8%`.

## Settled cohort entering G2-KC

- `96 positions / 24 per family / 24 settled maps`
- `47W-49L / -1.84875u`
- ML `7-17 / -2.60500u`
- KH `13-11 / +0.09850u`
- Duration `14-10 / +0.52725u`
- TK `13-11 / +0.13050u`
- actual exposure `0u`

Preferred structural checkpoint: `120 settled positions / 30 per family`.

## Historical outstanding state

- T1-DK G3 settled; no T1-DK G4 position existed at switch.
- IG-WE G4 remains prospectively locked but unsettled in its historical handoff.

## Next action

**AWAIT EXPLICIT G1/G2 FINAL EVIDENCE OR NEXT FULLY SUPPLIED MAP DRAFT + BOARD.**