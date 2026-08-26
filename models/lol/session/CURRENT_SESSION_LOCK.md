# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`  
**Status:** `CIRCUIT_BREAKER`  
**Effective:** `2026-08-26 14:32 UTC+7`  
**Circuit breaker triggered:** `2026-08-26 ~17:40 UTC+7`  
**Scope:** `LCK 2026 Play-In — KT Rolster vs HANJIN BRION — full BO5 series`  
**Authority commit:** `95af8bcde298772e28f963818a71f0653d602a69`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `SUSPENDED FOR TAKE EXECUTION`  
**Small-H asymmetry calibration:** `ACTIVE AS REVIEW CONTEXT ONLY`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Frozen authority

All analytical/procedural rules remain frozen to:

`95af8bcde298772e28f963818a71f0653d602a69`

The frozen stack includes LoL v0.3.58, DIM, PDRL, PML, KHMC, underdog +kills UDKC/KPA/KMS/RLD/UCS/LAC controls, PRE_TAKE mechanical validation, Duration DOVC, Total Kills FRP, Live ML DPS/LRO, screenshot-sync provenance rules and the map-end Airtable batching override.

LoL v0.3.59 and v0.3.60 remain retired.

## Circuit-breaker trigger

Game 3 KT +9.5 kills @1.982 was emitted at 13:14 with BRO leading 5-2, +3.1k, towers 0-0 and dragons 1-0.

Post-entry audit found a contemporaneous hard-gate violation under the already-active 2026-08-23 underdog +kills execution hardening:

- `LAC — Live Anti-Cascade Confirmation` did not have qualifying observed proof;
- no demonstrated suppression cycle or repeated preservation against BRO's actual favorite margin-expansion mechanism had occurred;
- draft theory (Wukong/Bard/Sivir/Zoe/Yorick reset/return-kill/side-route potential) was substituted for required live anti-cascade evidence;
- BRO's actual mechanism was pre-contact poke/pick/range through Jayce/LeBlanc/Ezreal/Elise, so generic anti-engage/return-kill tools did not directly suppress the favorite route;
- the visible TAKE therefore violated an active hard gate and should have been `HOLD/PASS` before outcome was known.

Final user-authoritative result: BRO 13-3 KT. Historical prediction remains a Loss, -0.25u shadow / 0u actual. Process validity is separately classified invalidated.

Under the frozen governance procedure, this execution failure triggers the procedural circuit breaker.

## Immediate operating consequence

Until the series ends or the user explicitly authorizes an immediate relock/new authority epoch:

- **NO NEW TAKE may be issued in any market family**;
- continue synchronized live analysis, draft reading, HOLD/PASS verdicts and review if useful;
- create no new shadow Positions;
- do not silently activate any default-branch fix inside E14;
- proposed analytical/calibration fixes are `PENDING_NEXT_SLATE` unless the user explicitly authorizes relock now.

## Underdog +kills batch warning

Airtable audit of settled underdog +kills from the Aug 19-26 guard era, including KT +9.5, is 4 wins and 12 losses, excluding voids, for approximately -2.0665u on 4.0u staked (-51.7% ROI).

This is treated as a mechanism-level calibration warning, not isolated variance. Multiple losses were already separately audit-invalidated for false-STABLE, missing draft-lock proof, thin-cushion, or wrong-mechanism KMS/LAC errors.

The recurring failure mode is over-crediting theoretical underdog survival/return-kill tools and arithmetic cushion while underweighting the favorite's actual pre-contact pick/poke/zone/continuation route and the probability of serial objective-cycle margin expansion.

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

Fearless archetype-inventory tracking remains mandatory for Game 4+ analysis.

## Screenshot synchronization

User-supplied same-message scoreboard + bookmaker screenshot pairs are presumed synchronized unless the underlying game state materially contradicts. Bookmaker/header/feed clock differences alone are non-authoritative for synchronization.

## Airtable logging / batching

Standing user-approved map-end batching remains active:

- no Airtable calls merely to log live frames mid-map;
- buffer meaningful states during the map;
- batch-write and exact-verify at map end.

Game 3 has been batch-written and verified, including the settled KT +9.5 Loss.

## Continuation requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-26-E14-KT-BRO-1432-UTC7`;
4. observe `Status = CIRCUIT_BREAKER` and `TAKE SUSPENDED`;
5. re-fetch locked `CURRENT_MODEL.md` at `95af8bcde298772e28f963818a71f0653d602a69` and load the frozen retained stack;
6. load the latest applicable KT-BRO handoff last;
7. continue analysis/HOLD only unless the user explicitly authorizes a relock.

Do not resume TAKE execution merely because a new chat starts or a newer default-branch fix exists.