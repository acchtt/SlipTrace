# Current Live Handoff — KT Rolster vs Dplus KIA — 2026-09-04

**Status:** CLOSED — SERIES COMPLETE / GAME 4 SETTLED / DATA-INTEGRITY FLAG  
**Session lock:** `LOL-2026-09-04-V13-KT-DK-DRAFTONLY-FORCEDCHOICE-Q2-1955-UTC7`  
**Authority commit:** `6018e7706772554d6318c1af4a9548ca4f25cd95`  
**Execution:** `POSTDRAFT-ONLY / FORCED-CHOICE / Q2 QUARANTINE / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## 1. Series closure

- LCK 2026 Season Playoffs — Lower Bracket Round 2 — KT Rolster vs Dplus KIA.
- G1-G2 had no prospective canonical Positions in this chat; no retroactive Positions were created.
- G3: DK won `19-4` in `26:56`; positions `3-1 / +0.40125u`.
- G4: user designated the supplied `31:13` scoreboard as final; DK won `17-10`.
- Series score after G4: **Dplus KIA 3-1 KT Rolster**; series complete.
- G4 map + four canonical Positions are settled in Airtable.
- No further KT-DK Position may be created under this handoff/lock.

## 2. Frozen benchmark used for series

- `B(DK)=+0.355702`
- `B(KT)=-1.465479`
- `GAP(DK-KT)=+1.821180 SD`
- `DK K=+2 / P0=60%`
- `KT K=-2 / P0=40%`
- `TK0=25.45`

Same-series results never changed K/P0/TK0.

## 3. G4 entered draft / board

Entered user draft, TOP / JUNGLE / MID / ADC / SUPPORT:
- DK blue: `Jax / Vi / Annie / Miss Fortune / Neeko`
- KT red: `Gwen / Skarner / Akali / Kalista / Renata`

Board:
- ML: DK `1.650` / KT `2.205`
- KH: DK `-5.5 @1.930` / KT `+5.5 @1.826`
- Duration `31.5`: Over `1.780` / Under `1.968`
- TK `27.5`: Over `1.909` / Under `1.861`

Locked Q2 selections:
1. DK ML @1.650
2. KT +5.5 @1.826
3. Under 31.5 @1.968
4. Over 27.5 @1.909

## 4. G4 settlement

Final user-designated scoreboard:
- winner: **Dplus KIA**
- kills: **DK 17-10 KT**
- duration: **31:13**
- total kills: `27`
- DK kill margin: `+7`

Results:
- DK ML — WIN — `+0.1625u`
- KT +5.5 — LOSS — `-0.2500u`
- Under 31.5 — WIN — `+0.2420u`
- Over 27.5 — LOSS — `-0.2500u`

G4 total: `2W-2L / -0.0955u`; actual exposure `0u`.

## 5. Mandatory data-integrity exception

**Clear draft-input mismatch:** the locked user draft listed DK top **Jax**, but the final scoreboard shows **Siwoo on Renekton**.

Treatment:
- settle the four G4 Positions exactly as entered because map identity, market lines, and final settlement are unambiguous;
- count the Positions in the historical forced-choice ledger/P&L;
- tag G4 as `DATA-INTEGRITY MISMATCH`;
- **exclude G4 from clean draft-mechanism / DIM calibration evidence**;
- do not use the apparent G4 diagnostic `D=DK`, KH distribution, Duration draft scores, or TK draft distribution as clean champion-draft validation evidence;
- this is an implementation/input integrity incident, not evidence for or against a coefficient change.

## 6. Cohort after series

After G4:
- `48 Positions / 12 per family`
- overall `22W-26L / -1.76975u`
- ML `3-9 / -1.7315u`
- KH `5-7 / -0.6505u`
- Duration `9-3 / +1.26175u`
- TK `5-7 / -0.6495u`
- actual exposure `0u`.

Preferred structural checkpoint remains `80 total / 20 per family`, but G4 is flagged contaminated for draft-calibration analysis.

## 7. Next-session requirement

Before any new LoL Position:
1. load canonical bootstrap;
2. observe KT-DK lock is closed;
3. identify the next current match fresh;
4. build a fresh price-independent Gol.gg benchmark;
5. create a fresh Session Authority Lock;
6. load the newest applicable handoff last.

No KT-DK lock reuse.
