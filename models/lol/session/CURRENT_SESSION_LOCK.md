# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-28-E16-EDG-NIP-1311-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-28 13:11 UTC+7`  
**Scope:** `LPL 2026 Split 3 — Knights' Rivals — EDward Gaming vs Ninjas in Pyjamas — BO5`  
**Authority commit:** `a1039d980cdec8d96f4ffafdfb185c58eabb7c23`  
**Active analytical model:** `LoL v0.3.58 + post-NS-BFX market-priority/execution calibration`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**Post-NS-BFX calibration:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

User instruction on 2026-08-28 UTC+7: **“Lock lpl match.”**

The active match is EDward Gaming vs Ninjas in Pyjamas in the LPL 2026 Split 3 Knights' Rivals BO5. This lock is established before any TAKE-eligible decision for the series.

## Frozen authority

All model-certified analysis and TAKE execution for this EDG–NIP slate must use analytical/procedural files frozen at:

`a1039d980cdec8d96f4ffafdfb185c58eabb7c23`

LoL v0.3.59 and v0.3.60 remain retired/discarded and must not be loaded or blended.

Canonical post-NS-BFX calibration is included in the frozen authority through:

- `models/lol/CURRENT_MODEL.md`
- `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`
- `models/lol/reviews/NS_BFX_2026-08-27_SERIES_CALIBRATION_REVIEW.md`

## Active execution controls

- Market triage at each meaningful synchronized state: `ML -> Kill Handicap -> Total Kills -> Duration`.
- Ordinary live ML may use two causally independent evidence points under the post-NS-BFX calibration; contrary CLEAR/STRONG draft ML still requires full retained LRO.
- HOLD expires on the next meaningful synchronized state / major objective-contact-conversion cycle / material reprice.
- Role-weighted economy, facilitator/carry leverage and mechanism realization outrank raw kill score alone.
- Opportunity decay is active; late terminal-event-sensitive entries require stronger buffers and one-more-fight/one-clean-end boundary bets must PASS.
- TK Over requires at least two distinct observed contact realizations/cycles with recurrence persistence; draft contact inventory + one live event is insufficient.
- KH remains on the full side-neutral distribution / sign-after-distribution / two-live-state stack; KH speed rules are not loosened.
- Same-message user scoreboard + bookmaker screenshots are presumed synchronized unless underlying game state materially contradicts.
- Ignore bookmaker/header/device clock differences alone for synchronization.
- Position-blind reassessment mandatory.
- Exact signed kill-margin arithmetic mandatory.
- Greyed/stale markets non-executable.
- Same-map maximum one accepted TAKE per market family.
- No rescue, martingale, chasing or stake escalation.

## User line-existence confirmation gate — ACTIVE

User standing instruction from 2026-08-27: **“from now on only log the bet when i confirm it still exists.”**

- A visible `TAKE` is an analytical candidate only until the user explicitly confirms that the quoted market/line/odds still exist and are executable.
- Required state: `USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`.
- `PENDING`: no Position record, no W/L, no P/L.
- `CONFIRMED`: may become an accepted shadow Position.
- `FAILED`: no Position exists.
- A materially changed price/line must be reassessed before acceptance.

## Airtable workflow

Retain the user-approved low-latency live workflow:

- do not call Airtable merely to log live frames or TAKE candidates mid-map;
- buffer synchronized evidence during the map;
- only user-confirmed accepted TAKES may become Positions;
- batch-write and exact-verify map/snapshots/confirmed Positions at map end.

## Bootstrap / continuation requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-28-E16-EDG-NIP-1311-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `a1039d980cdec8d96f4ffafdfb185c58eabb7c23`;
5. follow its exact required load order at that same commit;
6. explicitly load `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md` and all pro-play PRE_TAKE extensions at the same commit;
7. load the latest applicable EDG–NIP live handoff last if one exists.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
