# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-28-E16R1-EDG-NIP-G2PLUS-1405-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-28 14:05 UTC+7`  
**Scope:** `LPL 2026 Split 3 — EDward Gaming vs Ninjas in Pyjamas — Games 2–5 only`  
**Supersedes:** `LOL-2026-08-28-E16-EDG-NIP-1311-UTC7` prospectively from Game 2 onward  
**Authority commit:** `4668363454de564fa01d75d3d822fd8154c11f13`  
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

Initial series lock was authorized by the user on 2026-08-28 with: **“Lock lpl match.”**

After Game 1, the user explicitly authorized an immediate analytical adjustment/relock with: **“Adjust the model now.”**

This permits the structural-context and same-map regime-flip repair amendment to become active prospectively for Games 2–5 rather than waiting for the next slate.

Historical Game 1 evidence and verdicts remain under the prior E16 authority and are not rewritten.

## Game 1 historical state

NIP won Game 1, final **22–7** kills.

Final supplied scoreboard state included:

- towers NIP 10–4 EDG;
- dragons NIP 4–1 EDG;
- Barons NIP 2–0 EDG;
- inhibitors NIP 2–0 EDG.

Two EDG ML analytical TAKE candidates were visible during Game 1, including EDG ML @2.441 and later EDG ML @2.021. Neither quoted line was user-confirmed as still executable, therefore neither became a Position and neither contributes W/L or P/L.

The @2.021 candidate is retained as analytical audit evidence. The model correction does not rewrite it into a fictional historical pre-entry PASS; it establishes the prospective correct gate for future decisions.

## Frozen authority

All model-certified analysis and TAKE execution from Game 2 onward must use analytical/procedural files frozen at:

`4668363454de564fa01d75d3d822fd8154c11f13`

LoL v0.3.59 and v0.3.60 remain retired/discarded and must not be loaded or blended.

The frozen authority includes:

- `models/lol/CURRENT_MODEL.md`;
- `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`;
- `models/lol/procedures/LOL_ML_STRUCTURAL_CONTEXT_AND_REGIME_FLIP_REPAIR_2026-08-28.md`;
- `models/lol/reviews/EDG_NIP_G1_ML_STRUCTURAL_CONTEXT_REVIEW_2026-08-28.md`;
- all mandatory pro-play / PRE_TAKE / KH / TK / Duration procedures listed by locked `CURRENT_MODEL.md`.

## New ML structural-context gate — ACTIVE

For Live ML:

- raw tower count, tower differential, first tower and tower gold are context by default;
- towers become positive evidence only when a complete Structural Causality Map demonstrates a forward map-control effect;
- classify `TOWER_STATE_CLASS = CONTEXT_ONLY / CAUSAL_CONTROL / TERMINAL_CONTROL / N-A`;
- `CONTEXT_ONLY` cannot independently satisfy ML evidence count, CFC_CURRENT, regime persistence, DPS break, or a regime flip;
- when the opponent owns a material compulsory objective schedule such as 3 dragons / Soul point, resolve `OBJECTIVE_SCHEDULE_OFFSET`; a tower lead that merely coexists with that schedule does not repair the objective-control deficit.

Required structural chain when positive tower evidence is used:

`STRUCTURE_CHANGE -> FORWARD_MAP_EFFECT -> NEXT_CYCLE_EFFECT -> COMPOSITION_EXPLOITABILITY`

## Same-side PASS -> TAKE repair gate — ACTIVE

If an ML side was previously PASS in the same map, a later TAKE on that same side must record the exact `PRIOR_PASS_CAUSE` and resolve:

`PASS_CAUSE_REPAIR = REPAIRED / SUPERSEDED`

plus:

`REGIME_FLIP_DELTA = PASS`.

- `REPAIRED`: the exact earlier rejection mechanism materially changed.
- `SUPERSEDED`: a genuinely new causal thesis now dominates the next compulsory cycles, with explicit new evidence and explanation of why the old PASS cause no longer dominates.
- tower differential, duplicated gold, kill score or price movement cannot by themselves satisfy repair/supersession.
- `FAIL / UNRESOLVED` blocks TAKE.

For applicable ML PRE_TAKE evidence persist:

`ML_STRUCT[TOWER=...;SC=...;OSO=...;PPC=...;PCR=...;RFD=...]`

## Standing execution controls

- Market triage at each meaningful synchronized state: `ML -> Kill Handicap -> Total Kills -> Duration`.
- Ordinary live ML may use two causally independent evidence points under the post-NS-BFX calibration; contrary CLEAR/STRONG draft ML still requires full retained LRO.
- HOLD expires on the next meaningful synchronized state / major objective-contact-conversion cycle / material reprice.
- Role-weighted economy, facilitator/carry leverage and mechanism realization outrank raw kill score alone, but resource advantage does not substitute for CFC/objective control.
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
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-28-E16R1-EDG-NIP-G2PLUS-1405-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `4668363454de564fa01d75d3d822fd8154c11f13`;
5. follow its exact required load order at that same commit;
6. explicitly load `models/lol/procedures/LOL_ML_STRUCTURAL_CONTEXT_AND_REGIME_FLIP_REPAIR_2026-08-28.md` and `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md` at the same commit;
7. apply the user line-existence confirmation gate before any Position creation;
8. load the latest applicable EDG–NIP live handoff last if one exists.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
