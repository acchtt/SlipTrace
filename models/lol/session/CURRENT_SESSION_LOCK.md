# Current LoL Session Lock

**Lock ID:** `LOL-2026-09-06-V13-LEC-G2-KC-DRAFTONLY-FORCEDCHOICE-Q3-1859-UTC7`  
**Status:** `ACTIVE`  
**Scope:** `LEC 2026 Summer Playoffs — Upper Bracket Final — G2 Esports vs Karmine Corp — Bo5 Fearless Draft`  
**Scheduled start:** `2026-09-06 15:00 UTC / 22:00 UTC+7`  
**Activation:** `2026-09-06 18:59 UTC+7`  
**Current target:** `Game 4 prospectively locked; G1/G2/G3/G4 unsettled in canonical ledger pending explicit map-end evidence`  
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
- KC ML `@1.838`
- KC +3.5 `@1.832`
- Under 33 `@1.748`
- Over 27.5 `@1.897`

Diagnostic: `D=+1 G2`, probability contribution `0pp`.

### Game 3 — UNSETTLED
Source-truth board was labeled Game 3.  
Draft KC blue: Zaahen / Cho'Gath / Syndra / Xayah / Rakan.  
G2: Ambessa / Qiyana / Ryze / Varus / Alistar.

Card:
- KC ML `@1.965`
- KC +3.5 `@1.822`
- Under 33 `@1.711`
- Over 27.5 `@1.792`

Diagnostic: `D=+1 KC`, probability contribution `0pp`.

### Game 4 — UNSETTLED
At the supplied G4 board, the series display shows G2 leading `2-1`; this same-series score is context only and does not update the frozen benchmark.

Draft:
- KC blue: Gnar / Trundle / Sylas / Ashe / Seraphine
- G2: Rumble / Maokai / Tristana / Miss Fortune / Nautilus

Board:
- ML G2 `2.016` / KC `1.741`
- Duration 32: Over `1.833` / Under `1.906`
- Total Kills 27.5: Over `1.919` / Under `1.804`
- KH G2 +3.5 `1.817` / KC -3.5 `1.924`

Canonical card:
- KC ML `@1.741` — model 55%, implied 57.44%, edge `-2.44pp`, `FORCED_NEG_EV=YES`; actual execution `PASS`
- KC -3.5 `@1.924` — raw cover 38%, implied 51.98%, edge `-13.98pp`, `FORCED_NEG_EV=YES`; selected because abs handicap `<5` must align with selected ML
- Under 32 `@1.906` — `V0/Q0/H0/T-1`, `F=30.25m`, model 62.25%, implied 52.47%, edge `+9.78pp`
- Over 27.5 `@1.919` — model 66%, implied 52.11%, edge `+13.89pp`

Full DIM diagnostic: `D=+1 G2`, probability contribution `0pp`.
- G2 PKM: Maokai/Nautilus hard force layers Rumble Equalizer and Miss Fortune Bullet Time, with Tristana cleanup.
- G2 SKM: Nautilus/Maokai pick pressure can create a separate numbers advantage and immediate objective/structure conversion through Tristana.
- KC PKM: Ashe arrow / Trundle pillar / Seraphine control into Sylas follow-up with Gnar flank pressure.
- KC SKM: Ashe-Seraphine kite/disengage plus Trundle disruption can blunt G2's first engage and enable front-to-back recovery.
- Adversarial pass: KC has real anti-engage and stolen-ultimate counterplay, but G2 retains two independent advantages — layered unavoidable initiation and high AoE conversion after first contact. `AFP=PASS_G2_EDGE`.

KH signed-margin bins from KC perspective:
- KC 10+ `16%`
- KC 4-9 `22%`
- KC 1-3 `17%`
- G2 1-3 `16%`
- G2 4-9 `17%`
- G2 10+ `12%`

KC -3.5 raw cover = `38%`. Explicit 10+ tails: KC `16%`, G2 `12%`.

Duration pre-price: `V0/Q0/H0/T-1`, `F=30.25m`.

TK bins:
- `<20`: `6%`
- `20-24`: `10%`
- `25-27`: `18%`
- `28-32`: `28%`
- `33-37`: `22%`
- `38+`: `16%`

Over 27.5 model = `66%`.
Suppression scenario masses:
- `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION = 16%`
- `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY = 5%`

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

**AWAIT EXPLICIT G1/G2/G3/G4 FINAL EVIDENCE OR NEXT FULLY SUPPLIED MAP DRAFT + BOARD.**