# Current Live Handoff — Invictus Gaming vs Team WE — 2026-09-06

**Status:** ACTIVE SERIES HANDOFF — G1/G2/G3 SETTLED / IG LEADS 2-1 / READY FOR G4  
**Session lock:** `LOL-2026-09-06-V13-LPL-IG-WE-DRAFTONLY-FORCEDCHOICE-Q3-1227-UTC7`  
**Authority commit:** `979c955667d63e913cb7eb2ecff915fc1f83920b`  
**Execution:** `POSTDRAFT-ONLY / FOUR-FAMILY SHADOW VALIDATION / Q3 / 0.25u SHADOW PER FAMILY / 0u ACTUAL`

## Frozen series authority

- `B(IG)=+0.797272`
- `B(WE)=-0.938274`
- `GAP(IG-WE)=+1.735546 SD`
- `IG K=+2 / P0=60%`
- `WE K=-2 / P0=40%`
- `TK0=33.40`
- same-series results never update `K/P0/TK0`; prior maps may affect only Fearless champion availability.

Q3 overlay remains active:
- ML: `D_DIAGNOSTIC_ONLY=YES`; `D_PROBABILITY_CONTRIBUTION=0`; P0-only forced-choice probability; ML floor 1.45 is execution eligibility only.
- KH: signed margin bins, explicit 10+ tails, 70% cap; `<5` must align with ML; `±5.5+` may be independent.
- Duration: v1.1 formula / 31.0m anchor unchanged; Over has `OVER_BRANCH_WARNING=YES` and `DURATION_OVER_SHADOW_ONLY=YES`.
- TK: persist separate `ONE_SIDED_FAST_CLOSE / RETURN_KILL_SUPPRESSION` and `LOW_CONTACT_EXTENDED_GAME / LOW_FIGHT_FREQUENCY` branches.
- Airtable writes only at map end; no retroactive positions; actual exposure `0u`.

## Game 1 — SETTLED

Draft:
- IG blue: `Gwen / Nocturne / Syndra / Yunara / Lulu`
- WE red: `K'Sante / Lee Sin / Ryze / Caitlyn / Bard`

Canonical card:
1. `IG ML @1.693`
2. `IG -4.5 kills @1.861`
3. `Over 32 minutes @2.030`
4. `Over 31.5 total kills @2.120`

Final user evidence:
- **IG win**
- kills `18-7`
- duration `23:27`
- total kills `25`

Settlement:
- IG ML — WIN `+0.17325u`
- IG -4.5 — WIN `+0.21525u`
- Over 32 — LOSS `-0.25000u`
- Over 31.5 kills — LOSS `-0.25000u`
- **G1: 2-2 / -0.11150u**

Audit note: very fast one-sided close realized the Q3 fast-close / return-kill-suppression branch. Airtable map + four positions written.

## Game 2 — SETTLED

Draft:
- WE blue: `Galio / Wukong / Akali / Lucian / Milio`
- IG red: `Rumble / Naafiri / Orianna / Xayah / Rakan`

Canonical card:
1. `IG ML @1.598`
2. `WE +5.5 kills @1.961`
3. `Under 31 minutes @1.797`
4. `Over 30.5 total kills @1.771`

Final user evidence:
- **WE win**
- kills `16-7`
- duration `31:30`
- total kills `23`

Settlement:
- IG ML — LOSS `-0.25000u`
- WE +5.5 — WIN `+0.24025u`
- Under 31 — LOSS `-0.25000u`
- Over 30.5 kills — LOSS `-0.25000u`
- **G2: 1-3 / -0.50975u**

Audit note: forced-negative IG ML lost; Under missed by 0:30; TK Over missed with only 23 kills, consistent with low-contact / suppressed fight-frequency risk. Airtable map + four positions written.

## Game 3 — SETTLED

Draft:
- WE blue: `Jayce / Maokai / Corki / Ashe / Camille`
- IG red: `Yorick / Trundle / Twisted Fate / Jhin / Seraphine`

Canonical card:
1. `IG ML @1.653`
2. `WE +5.5 kills @1.820`
3. `Over 31 minutes @1.763`
4. `Over 29.5 total kills @1.708`

Final user evidence:
- **IG win**
- kills `WE 22 - 18 IG`
- duration `33:42`
- total kills `40`

Settlement:
- IG ML — WIN `+0.16325u`
- WE +5.5 — WIN `+0.20500u`
- Over 31 — WIN `+0.19075u`
- Over 29.5 kills — WIN `+0.17700u`
- **G3: 4-0 / +0.73600u**

Important settlement nuance: IG won the map despite WE leading kills 22-18, so WE +5.5 also covered. Airtable map + four positions written.

## Series / Q3 block after G3

Series score: **IG 2-1 WE**.

IG-WE tracked block:
- `7W-5L / +0.11475u`
- shadow stake `3.00u`
- actual exposure `0u`

Cohort after G3:
- `92 positions / 23 per family / 23 maps`
- overall `46W-46L / -1.38275u`
- ML `7-16 / -2.35500u`
- KH `13-10 / +0.34850u`
- Duration `14-9 / +0.77725u`
- TK `12-11 / -0.15350u`

Next preferred structural checkpoint remains `120 positions / 30 per family`.

## Next action

**READY FOR GAME 4 FINAL DRAFT + EXACT BOARD.**

No G4 Position exists yet.