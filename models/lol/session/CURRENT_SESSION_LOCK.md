# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-28-E17-BRO-BFX-1530-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-28 15:30 UTC+7`  
**Scope:** `LCK 2026 Play-In — HANJIN BRION vs BNK FEARX — BO5 Fearless — final Play-In decider`  
**Authority commit:** `dbbc0cd2a92ba0292db3702a975cfdc72c9c867e`  
**Active analytical model:** `LoL v0.3.58 + post-NS-BFX calibration + ML structural-context/regime-flip repair`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Post-NS-BFX calibration:** `ACTIVE`  
**ML structural context / regime-flip repair:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

User instruction on 2026-08-28 UTC+7: **“Lock and preview lck match at 15:00.”**

The scheduled 15:00 UTC+7 LCK match is HANJIN BRION vs BNK FEARX, the BO5 Fearless final Play-In decider for the remaining playoff berth.

This lock is prospective from 15:30 UTC+7, when the user issued the lock instruction. Any game action before lock establishment is historical context only and cannot be backfilled into a TAKE.

## Prior slate closure

The prior EDG–NIP slate is closed. NIP won the series 3–0. No quoted TAKE candidate in that series was user-confirmed as still executable, so no accepted Position was created and series shadow P/L is 0u.

## Frozen authority

All model-certified analysis and TAKE execution for BRO–BFX must use analytical/procedural files frozen at:

`dbbc0cd2a92ba0292db3702a975cfdc72c9c867e`

LoL v0.3.59 and v0.3.60 remain retired/discarded and must not be loaded or blended.

The frozen authority includes:

- `models/lol/CURRENT_MODEL.md`;
- `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`;
- `models/lol/procedures/LOL_ML_STRUCTURAL_CONTEXT_AND_REGIME_FLIP_REPAIR_2026-08-28.md`;
- all mandatory pro-play / PRE_TAKE / KH / TK / Duration procedures listed by locked `CURRENT_MODEL.md`.

## Active execution controls

- Market triage at each meaningful synchronized state: `ML -> Kill Handicap -> Total Kills -> Duration`.
- Ordinary live ML may use two causally independent evidence points; contrary CLEAR/STRONG draft ML still requires full retained LRO.
- Raw tower count/differential is context by default. Positive structural ML evidence requires a complete structural-causality chain into forward control.
- Same-side `PASS -> TAKE` requires explicit prior-pass cause repair/supersession plus a causal regime-flip delta.
- HOLD expires on the next meaningful synchronized state / major objective-contact-conversion cycle / material reprice.
- Role-weighted economy and mechanism realization outrank raw kill score, but resource advantage does not substitute for CFC/objective control.
- Opportunity decay is active; late terminal-event-sensitive entries require stronger buffers and one-more-fight/one-clean-end boundary bets must PASS.
- TK Over requires at least two distinct observed contact realizations/cycles with recurrence persistence.
- KH remains on the full side-neutral distribution / sign-after-distribution / two-live-state stack.
- Same-message user scoreboard + bookmaker screenshots are presumed synchronized unless underlying game state materially contradicts.
- Ignore bookmaker/header/device clock differences alone for synchronization.
- Position-blind reassessment mandatory.
- Exact signed kill-margin arithmetic mandatory.
- Greyed/stale markets non-executable.
- Same-map maximum one accepted TAKE per market family.
- No rescue, martingale, chasing or stake escalation.

## User line-existence confirmation gate — ACTIVE

User standing instruction: **“from now on only log the bet when i confirm it still exists.”**

- A visible `TAKE` is an analytical candidate only until the user explicitly confirms the exact quoted market/line/odds still exist and are executable.
- Required state: `USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`.
- `PENDING`: no Position record, no W/L, no P/L.
- `CONFIRMED`: may become an accepted shadow Position.
- `FAILED`: no Position exists.
- A materially changed price/line must be reassessed before acceptance.

## Airtable workflow

- do not call Airtable merely to log live frames or TAKE candidates mid-map;
- buffer synchronized evidence during the map;
- only user-confirmed accepted TAKES may become Positions;
- batch-write and exact-verify map/snapshots/confirmed Positions at map end.

## Series context to retain

BRO entered this decider after losing 2–3 to KT on 2026-08-26. BFX entered after defeating NS 3–1 on 2026-08-27. Recent regular-season head-to-head results are context only and do not override current draft/live evidence.

For Fearless Game 2+, maintain exact used-champion and functional-archetype inventory for both teams. Do not infer depletion from champion count alone.

## Bootstrap / continuation requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-28-E17-BRO-BFX-1530-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `dbbc0cd2a92ba0292db3702a975cfdc72c9c867e`;
5. follow its exact required load order at that same commit;
6. explicitly load `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md` and `models/lol/procedures/LOL_ML_STRUCTURAL_CONTEXT_AND_REGIME_FLIP_REPAIR_2026-08-28.md`;
7. apply the user line-existence confirmation gate before any Position creation;
8. load the latest applicable BRO–BFX live handoff last if one exists.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
