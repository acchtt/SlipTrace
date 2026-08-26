# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-26-E14R2-KT-BRO-G5-1853-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-26 18:53 UTC+7`  
**Scope:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — Game 5 decider only`  
**Supersedes:** `LOL-2026-08-26-E14R1-KT-BRO-1754-UTC7` prospectively for Game 5  
**Authority commit:** `a095385d721ffdcd62e77d6053ab241b5a8b5cdb`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR — USER-AUTHORIZED G5 REBALANCE`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**KH dog directional probation:** `ACTIVE — E14R2 REBALANCED`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

After Game 4, the user stated that the model appeared too strict because multiple live opportunities produced zero TAKES. The Game 4 strictness review found mixed evidence: several passes were correct, but the E14R1 dog-probation mechanics and lead-concentration handling were over-restrictive for the screenshot-driven evidence stream.

The user then explicitly instructed:

**“Apply for g5”**

This authorizes a new prospective Game 5 authority epoch. It does not rewrite Games 1–4, any historical TAKE/HOLD/PASS, or any P/L.

## Frozen authority

All model-certified analysis and TAKE execution in E14R2 must use analytical/procedural files frozen at:

`a095385d721ffdcd62e77d6053ab241b5a8b5cdb`

LoL v0.3.59 and v0.3.60 remain retired and must not be loaded or blended.

## Mandatory E14R2 overlay

After loading the exact frozen `CURRENT_MODEL.md` stack, explicitly load:

`models/lol/procedures/LOL_E14R2_G5_KH_ML_STRICTNESS_REBALANCE_2026-08-26.md`

This overlay is Game-5-only and supersedes conflicting E14R1 lock-scoped strictness mechanics while retaining the global v0.3.58 model.

Reference review:

`models/lol/reviews/E14R1_GAME4_STRICTNESS_REVIEW_2026-08-26.md`

### Active Game 5 KH changes

1. `KH_DOG_DIRECTIONAL_PROBATION` remains ACTIVE.
2. `INSUFFICIENT/THIN` dog +H remains automatic HOLD/PASS.
3. `MATERIAL` dog +H may qualify only with independent ML support, a passing screenshot-compatible live evidence package, mechanism match, probability-weighted cycle hazard, and full lower-bound pricing clearance.
4. `LARGE` dog +H remains eligible under retained rules.
5. Synchronized snapshot transitions may establish `COUNTER_EXPANSION`, `BOUNDED_EXPANSION`, or `SUPPRESSED` live evidence; continuous video is not required.
6. The rigid “exactly two matched suppression windows” rule is replaced by the overlay evidence package.
7. Raw one/two-cycle threshold crossability is no longer an automatic veto. `P_CROSS_ONE_CYCLE` and `P_CROSS_TWO_CYCLE` must be probability-classified and integrated into final-margin bins.
8. HIGH one-cycle cross hazard, or HIGH two-cycle hazard with MATERIAL/HIGH remaining forced-cycle density, remains automatic HOLD/PASS for dog +H.
9. Dog surcharge becomes evidence/cushion conditional: +3pp / +4pp for LARGE depending on evidence route, +5pp for MATERIAL.
10. NKB, theoretical tools, cushion size, quiet time, and price remain non-evidence by themselves.

### Active Game 5 ML/KH lead-concentration changes

Every live ML/KH distribution must resolve:

`TEAM_GOLD_LEAD | LARGEST_ROLE_GOLD_EDGE | LEAD_CONCENTRATION_RATIO | NON_CONCENTRATED_NET | LEAD_CONCENTRATION_CLASS | CONCENTRATED_ROLE_CONVERSION_ACCESS | OBJECTIVE_OFFSET | COUNTER_EXPANSION_EVIDENCE | LEAD_QUALITY_AFTER_CONCENTRATION`.

Concentrated/extreme leads are discounted unless the concentrated role has real near-term conversion access. Opposing objective control plus demonstrated counter-expansion can justify an additional lead-quality downgrade.

This applies symmetrically to both teams and both KH signs.

## What remains unchanged

- KH parent sign neutrality remains mandatory.
- `KH_MARGIN_CERT -> both-side pricing -> WMS -> sign selection -> sign-specific validator -> calibration buffer -> PRE_TAKE_CERT` remains the required order.
- No favorite quota, dog quota, or sign inversion shortcut.
- Live ML retains 2SNAP, Lead Decomposition/CFC/DPS/PML/LRO where applicable.
- Total Kills Under retains FRP.
- Total Kills Over retains recurrence/contact-pressure proof.
- Duration Over retains full DOVC.
- Duration Under retains FCR/shortest-close-route testing.
- Minimum accepted odds remains 1.60.
- Actual exposure remains 0u; default shadow stake remains 0.25u.

## Current series state

Series after Game 4: `KT 2-2 HANJIN BRION`.

Game 4 final user-authoritative supplied state: `33:28 | KT 17-8 BRO | KT +6.7k | towers 7-3 | dragons 3-2 | Baron 1-0 | inhibitors 1-0`.

No Game 4 shadow position existed; P/L 0u.

## Completed Fearless depletion entering Game 5

### KT used
- Game 1: Olaf / Nocturne / Ryze / Miss Fortune / Nautilus
- Game 2: Ornn / Naafiri / Syndra / Yunara / Lulu
- Game 3: Yorick / Wukong / Zoe / Sivir / Bard
- Game 4: Ambessa / Lee Sin / Lissandra / Ashe / Seraphine

### BRO used
- Game 1: Kled / Jarvan IV / Anivia / Lucian / Milio
- Game 2: Rumble / Vi / Ahri / Kalista / Renata Glasc
- Game 3: Jayce / Xin Zhao / LeBlanc / Ezreal / Elise
- Game 4: Gnar / Pantheon / Locke / Jhin / Camille

Fearless archetype-inventory tracking is mandatory for Game 5.

## Game 4 review facts that must not be lost

- Several Game 4 passes were correct; zero TAKEs alone is not proof that the entire model was too strict.
- BRO -3.5 at 18:28 and 21:58 would have lost.
- displayed Total Kills Overs would have lost with 25 final kills.
- BRO ML 1.598 at 11:48 was below floor and ultimately lost.
- key possible over-filtered windows were KT +3.5 and KT ML around 18:28/21:58.
- at 9:18 and 11:48 the correct dragon state was BRO 0-KT 1; prior live commentary that gave BRO the first dragon was a reading error and must not propagate.

## Screenshot synchronization

User-supplied same-message scoreboard + bookmaker screenshot pairs are presumed synchronized unless the underlying game state materially contradicts.

Bookmaker/header/feed clock differences alone are non-authoritative for synchronization.

## Airtable logging / batching

Standing user-approved map-end batching remains active:

- no Airtable calls merely to log live frames or TAKES mid-map;
- buffer meaningful states and entry evidence during Game 5;
- batch-write and exact-verify at map end.

## Continuation / bootstrap requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-26-E14R2-KT-BRO-G5-1853-UTC7`;
4. verify `Status=ACTIVE`, `Circuit breaker=CLEAR`, `KH directional calibration=ACTIVE`, and `KH dog directional probation=ACTIVE — E14R2 REBALANCED`;
5. re-fetch `CURRENT_MODEL.md` at authority commit `a095385d721ffdcd62e77d6053ab241b5a8b5cdb`;
6. follow its exact load order at that frozen commit;
7. explicitly load `models/lol/procedures/LOL_E14R2_G5_KH_ML_STRICTNESS_REBALANCE_2026-08-26.md` after the frozen core stack;
8. load the latest applicable KT-BRO live handoff last.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
