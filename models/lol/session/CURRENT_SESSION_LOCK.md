# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-27-E15-NS-BFX-1547-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-27 15:47 UTC+7`  
**Scope:** `LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — full BO5 from Game 1 onward`  
**Supersedes:** `LOL-2026-08-26-E14R2-KT-BRO-G5-1853-UTC7` by new UTC+7 slate boundary  
**Authority commit:** `7ac5aa001194406da96ad63c5bbabcfc78496940`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization / slate boundary

This is a new UTC+7 calendar-day slate, so the prior KT-BRO Game-5-only lock is not applicable. Under the active session-governance rule, the Aug-27 LCK slate is frozen prospectively to the current fully bootstrapped authority before any TAKE-eligible decision.

## Frozen authority

All model-certified analysis and TAKE execution for this slate must use analytical/procedural files frozen at:

`7ac5aa001194406da96ad63c5bbabcfc78496940`

LoL v0.3.59 and v0.3.60 remain retired and must not be loaded or blended.

## Standing execution controls

- Official betting remains paused; shadow only.
- Pregame/immediate-postdraft ML/KH/TK TAKEs disabled.
- Live ML/KH/TK require two usable synchronized live snapshots.
- Same-message user scoreboard + bookmaker screenshot pairs are presumed synchronized unless underlying game state materially contradicts.
- Ignore bookmaker/header/device clock differences alone for synchronization.
- No Airtable calls merely to log live frames or TAKES mid-map; buffer during a map and batch-write/exact-verify at map end.
- Position-blind reassessment remains mandatory.
- Exact signed kill-margin arithmetic remains mandatory.
- PDRL + PML are mandatory for this professional Fearless series.
- Fearless archetype inventory must carry forward game to game.

## Series state at lock creation

User has supplied Game 1 final:

`27:53 | NS 27-8 BFX | towers NS 9-2 | dragons NS 3-1 | Baron NS 1-0 | inhibitors NS 1-0`

Game 1 draft from the supplied final scoreboard:

- BFX: Jayce / Lee Sin / Galio / Caitlyn / Bard
- NS: Camille / Jarvan IV / Orianna / Jhin / Shen

No Game 1 shadow position was issued in this chat. Historical Game 1 position count therefore remains 0 unless original contemporaneous evidence elsewhere proves otherwise.

## Continuation / bootstrap requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-27-E15-NS-BFX-1547-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `7ac5aa001194406da96ad63c5bbabcfc78496940`;
5. follow its exact required load order at that commit;
6. load the latest applicable NS-BFX live handoff last.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
