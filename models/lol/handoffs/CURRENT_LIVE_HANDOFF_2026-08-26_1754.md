# Current Live Handoff — KT Rolster vs HANJIN BRION — 2026-08-26 17:54 UTC+7

## Authority

- Active Lock ID: `LOL-2026-08-26-E14R1-KT-BRO-1754-UTC7`
- Lock status: `ACTIVE`
- Frozen authority commit: `0424b09b9a435411fc1c3fb1dc91c2235f31b7bb`
- Model: `LoL v0.3.58`
- Circuit breaker: `CLEAR — NEW USER-AUTHORIZED AUTHORITY EPOCH`
- PDRL: ACTIVE
- PML: ACTIVE
- KH directional calibration: ACTIVE
- KH dog directional probation: ACTIVE
- Actual exposure: 0u
- Default shadow stake: 0.25u
- Minimum odds: 1.60

The prior E14 epoch triggered a procedural circuit breaker after Game 3 KT +9.5 @1.982 violated the active LAC hard gate. The user then explicitly instructed “Recalibrate now”, authorizing immediate prospective recalibration and relock for the remaining series.

Historical Game 3 position remains a Loss -0.25u shadow / 0u actual. Do not rewrite it.

## Series state

LCK 2026 Play-In — KT Rolster vs HANJIN BRION, BO5.

Series after Game 3: **KT 1-2 BRO**.

Game 4 is next. Side assignment is not yet confirmed in this handoff.

## Completed Fearless depletion entering Game 4

### KT used
- G1: Olaf / Nocturne / Ryze / Miss Fortune / Nautilus
- G2: Ornn / Naafiri / Syndra / Yunara / Lulu
- G3: Yorick / Wukong / Zoe / Sivir / Bard

### BRO used
- G1: Kled / Jarvan IV / Anivia / Lucian / Milio
- G2: Rumble / Vi / Ahri / Kalista / Renata Glasc
- G3: Jayce / Xin Zhao / LeBlanc / Ezreal / Elise

Fearless archetype inventory remains mandatory for Game 4+.

## Game 3 settlement and audit

User-authoritative final: BRO won 13-3.

Logged shadow position:

`KT +9.5 kills @1.982 — 0.25u shadow — LOSS -0.25u — actual 0u`.

Entry state was BRO 5-2 KT, BRO +3.1k, towers 0-0, dragons 1-0. BRO needed +7 additional future net kills to defeat +9.5 and expanded the margin by exactly +7.

Post-entry audit found the TAKE was process-invalid because no qualifying observed LAC suppression cycle existed against BRO's actual Jayce/LeBlanc/Ezreal/Elise pre-contact poke/pick/range mechanism. Draft-theory fallback tools were substituted for live mechanism-matched suppression.

## 2026-08-26 KH recalibration active in E14R1

Reference review:
`models/lol/reviews/KH_DIRECTIONAL_RECALIBRATION_2026-08-26.md`

Updated mandatory procedure paths at frozen authority:

- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

Batch evidence: settled underdog +kills in Aug 19-26 guard era = 4W-12L, -2.0665u on 4.0u stake (-51.7% ROI), excluding voids. Latest ten KH picks were all +kills: 2W-7L-1V.

This is calibration evidence, not a direct probability prior and not a favorite quota.

### Dog +H probation

`KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

Dog +H may TAKE only if all retained gates pass plus:

- `DOG_CUSHION_CLASS=LARGE`; MATERIAL/THIN/INSUFFICIENT are PASS;
- identify favorite actual repeatable expansion mechanism and direct underdog answer;
- `MECHANISM_MATCH=PASS`;
- two distinct mechanism-matched live suppression windows from representative expansion opportunities;
- no single-event LAC exception;
- one-cycle and two-cycle WMS margin ranges;
- if MATERIAL/HIGH WMS can cross failure threshold in one or two compulsory cycles => automatic PASS;
- dog lower-bound cover probability must clear break-even by base retained buffer + 5pp;
- NKB, absolute line size, 0-0 towers, quiet time and theoretical defensive tools are never enough by themselves.

### Favorite -H

Favorite -H retains side-neutral parent pricing and all favorite-tail gates. It is not preferred automatically.

New explicit field: `COVER_BEFORE_CLOSE`, testing whether required margin can be banked before terminal structure control causes safe concession or removes fight inventory. Late safe-concede risk is not an automatic favorite veto if margin can be realized earlier.

## Screenshot synchronization

User-supplied same-message scoreboard + sportsbook screenshot pairs are presumed synchronized unless actual game-state content contradicts.

Ignore bookmaker/header/feed clock differences alone.

## Airtable batching

Standing rule: no Airtable calls merely to log live frames or TAKES mid-map. Buffer during map; batch-write and exact-verify at map end.

Game 3 has already been batch-written and verified.

## Continuation

Bootstrap from GitHub first. Fetch default `CURRENT_MODEL.md`, load `LOL_SESSION_BOOTSTRAP.md`, fetch `CURRENT_SESSION_LOCK.md`, verify E14R1, freeze to authority `0424b09b...`, load the exact retained stack from that commit, and load this handoff last.

If lock/authority mismatch: `MODEL LOCK MISMATCH — HOLD`.
