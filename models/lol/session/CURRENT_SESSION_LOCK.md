# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-26-E14R1-KT-BRO-1754-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-26 17:54 UTC+7`  
**Scope:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — remainder of BO5 from Game 4`  
**Supersedes:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7` after its procedural circuit breaker  
**Authority commit:** `0424b09b9a435411fc1c3fb1dc91c2235f31b7bb`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR — NEW USER-AUTHORIZED AUTHORITY EPOCH`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**KH dog directional probation:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization and breaker resolution

The prior E14 authority epoch was placed into `CIRCUIT_BREAKER` after Game 3 KT +9.5 @1.982 was found to have violated the already-active LAC hard gate.

At approximately 17:54 UTC+7 on 2026-08-26, after reviewing the recent Kill Handicap sample, the user explicitly instructed:

**“Recalibrate now”**

This instruction authorizes immediate prospective recalibration and an immediate new authority epoch for the remaining KT-BRO series. It does not rewrite any prior position, prediction result or P/L.

The previous Game 3 KT +9.5 remains a historical Loss (-0.25u shadow / 0u actual) with process validity separately invalidated.

## Frozen authority

All model-certified analysis and TAKE execution in E14R1 must use analytical/procedural files frozen at:

`0424b09b9a435411fc1c3fb1dc91c2235f31b7bb`

This commit contains the canonical LoL v0.3.58 retained stack plus the user-authorized 2026-08-26 KH recalibration written in place to the already-mandatory KH procedure paths.

LoL v0.3.59 and v0.3.60 remain retired and must not be loaded or blended.

## 2026-08-26 KH recalibration — active now

Reference audit:

`models/lol/reviews/KH_DIRECTIONAL_RECALIBRATION_2026-08-26.md`

Updated active procedures at this authority commit:

- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

The batch trigger is the Aug 19-26 guard-era underdog +kills sample: 4 wins, 12 losses, -2.0665u on 4.0u settled stake (-51.7% ROI), excluding voids. The latest ten logged KH picks were all positive-handicap selections (2W, 7L, 1 Void).

This batch is calibration evidence only, not a direct empirical probability prior and not a favorite quota.

### Active dog +kills probation

`KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

For underdog +H, all retained gates still apply. In addition:

1. `DOG_CUSHION_CLASS` must be `LARGE`; INSUFFICIENT / THIN / MATERIAL are automatic PASS during probation.
2. Identify `FAVORITE_EXPANSION_MECHANISM`, `UNDERDOG_DIRECT_ANSWER`, and require `MECHANISM_MATCH=PASS`.
3. Require **two distinct mechanism-matched live suppression windows** from representative expansion opportunities; the prior single-event LAC exception is suspended.
4. WMS must quantify ordinary one-cycle and two-cycle margin expansion.
5. If a MATERIAL/HIGH ordinary WMS branch can cross the dog failure threshold inside one or two compulsory cycles, dog +H is automatic PASS.
6. Dog lower-bound cover probability must clear break-even by the retained base phase/uncertainty buffer **plus 5 percentage points**.
7. NKB, line size, 0-0 towers, quiet time, theoretical waveclear/peel/disengage/scaling/side pressure and attractive price cannot substitute for observed matched suppression.

### Favorite -kills recalibration

Favorite -H is not preferred automatically and uses the normal retained buffer.

The favorite validator now explicitly resolves `COVER_BEFORE_CLOSE`: whether the required kill margin can be banked before terminal structure control causes safe concession or removes compulsory fight inventory.

Late safe-concede risk may not automatically veto favorite -H when the required margin can credibly be realized earlier. All retained FFD/KCV/RFI/role-weighted lead quality/WMS/pricing gates remain mandatory.

### Parent sign neutrality remains mandatory

Before either sign can TAKE:

`KH_MARGIN_CERT -> both-side pricing -> WMS one/two-cycle stress -> sign selection -> sign-specific validator -> calibration buffer -> PRE_TAKE_CERT`.

No sign inversion, favorite quota or dog quota is permitted.

## Current series state

Series score after Game 3: `KT 1-2 HANJIN BRION`.

Completed Fearless depletion entering Game 4:

### KT used
- Game 1: Olaf / Nocturne / Ryze / Miss Fortune / Nautilus
- Game 2: Ornn / Naafiri / Syndra / Yunara / Lulu
- Game 3: Yorick / Wukong / Zoe / Sivir / Bard

### BRO used
- Game 1: Kled / Jarvan IV / Anivia / Lucian / Milio
- Game 2: Rumble / Vi / Ahri / Kalista / Renata Glasc
- Game 3: Jayce / Xin Zhao / LeBlanc / Ezreal / Elise

Fearless archetype-inventory tracking remains mandatory for Game 4+.

## Other market families

The E14R1 relock clears the procedural breaker prospectively for all market families, but does not relax any non-KH gate.

- Live ML: retained two-snapshot gate, Lead Decomposition/CFC/DPS and LRO where applicable.
- Total Kills Under: FRP mandatory.
- Total Kills Over: retained recurrence/contact-pressure proof.
- Duration Over: full DOVC mandatory.
- Duration Under: retained FCR/shortest-close-route testing.
- Minimum odds remains 1.60.
- Actual exposure remains 0u; shadow default 0.25u.

## Screenshot synchronization

User-supplied same-message scoreboard + bookmaker screenshot pairs are presumed synchronized unless the underlying game state materially contradicts.

Bookmaker/header/feed clock differences alone are non-authoritative for synchronization.

## Airtable logging / batching

Standing user-approved map-end batching remains active:

- no Airtable calls merely to log live frames or TAKES mid-map;
- buffer meaningful states and entry evidence during the map;
- batch-write and exact-verify at map end.

## Continuation / bootstrap requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-26-E14R1-KT-BRO-1754-UTC7`;
4. verify `Status=ACTIVE`, `Circuit breaker=CLEAR`, `KH directional calibration=ACTIVE`, and `KH dog directional probation=ACTIVE`;
5. re-fetch `CURRENT_MODEL.md` at authority commit `0424b09b9a435411fc1c3fb1dc91c2235f31b7bb`;
6. follow its exact load order at that same frozen commit, including the updated KH engine, small-H calibration and PRE_TAKE KH extension;
7. load the latest applicable KT-BRO live handoff last.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
