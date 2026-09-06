# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Final — G2 Esports vs Karmine Corp — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 15:00 UTC / 22:00 UTC+7`  
**Activation:** `2026-09-06 18:59 UTC+7`  
**Current target:** `Game 3 prospectively locked; G1/G2/G3 unsettled`  
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

Card:
- KC ML `@1.838` — model 55%, implied 54.41%, edge `+0.59pp`
- KC +3.5 `@1.832` — raw/model 69%, implied 54.59%, edge `+14.41pp`
- Under 33 `@1.748` — `V0/Q0/H0/T-1`, `F=30.25m`, model 69.25%, implied 57.21%, edge `+12.04pp`
- Over 27.5 `@1.897` — model 65%, implied 52.71%, edge `+12.29pp`

Diagnostic draft: `D=+1 G2`, probability contribution `0pp`.

### Game 3 — UNSETTLED
**Source-truth board label:** sportsbook screenshot says `Ván 3` / Game 3. User text said `game 4`; because the board itself is explicitly Game 3 and no separate G4 board was supplied, this position is canonically recorded as **Game 3** unless the user later corrects the source.

Draft:
- KC blue: Zaahen / Cho'Gath / Syndra / Xayah / Rakan
- G2: Ambessa / Qiyana / Ryze / Varus / Alistar

Board:
- ML G2 `1.782` / KC `1.965`
- Duration 33: Over `2.058` / Under `1.711`
- Total Kills 27.5: Over `1.792` / Under `1.933`
- KH G2 -3.5 `1.917` / KC +3.5 `1.822`

Canonical card:
- KC ML `@1.965` — model 55%, implied 50.89%, edge `+4.11pp`, `FORCED_NEG_EV=NO`
- KC +3.5 `@1.822` — raw/model 70% (Q3 cap binds), implied 54.88%, edge `+15.12pp`
- Under 33 `@1.711` — `V0/Q0/H0/T-1`, `F=30.25m`, model 69.25%, implied 58.45%, edge `+10.80pp`
- Over 27.5 `@1.792` — model 65%, implied 55.80%, edge `+9.20pp`

Full DIM diagnostic: `D=+1 KC`, probability contribution `0pp`.
- KC mechanism 1: Rakan/Cho'Gath/Syndra force-and-catch into Xayah cleanup.
- KC mechanism 2: Xayah self-peel plus Cho'Gath/Syndra control gives a separate anti-dive front-to-back route into G2's Ambessa/Qiyana/Alistar access.
- G2 mechanism 1: Alistar/Qiyana/Ambessa hard force with Varus/Ryze follow-through.
- G2 mechanism 2: Ryze side/collapse pressure with Varus ranged setup.
- Adversarial pass: G2 has real engage and side routes, but KC retains two independent surviving advantages: anti-dive/front-to-back resilience and pick/control layering. `AFP=PASS_KC_EDGE`.

KH signed-margin bins from KC perspective:
- KC by 10+: `19%`
- KC by 4-9: `19%`
- KC by 1-3: `17%`
- G2 by 1-3: `15%`
- G2 by 4-9: `17%`
- G2 by 10+: `13%`

Thus KC +3.5 raw cover = `70%`; Q3 reporting cap = `70%`. Explicit 10+ clean-cascade tails: KC `19%`, G2 `13%`.

TK pre-price bins:
- `<20`: `6%`
- `20-24`: `11%`
- `25-27`: `18%`
- `28-32`: `29%`
- `33-37`: `22%`
- `38+`: `14%`

Over 27.5 model = `65%`.
Suppression scenario masses:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 15%`
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY = 8%`

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

**AWAIT EXPLICIT G1/G2/G3 FINAL EVIDENCE OR NEXT FULLY SUPPLIED MAP DRAFT + BOARD.**