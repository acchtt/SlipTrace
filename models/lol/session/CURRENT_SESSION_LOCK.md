# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-27-E15R1-NS-BFX-G3PLUS-1641-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-27 16:41 UTC+7`  
**Scope:** `LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX — Games 3–5 only`  
**Supersedes:** `LOL-2026-08-27-E15-NS-BFX-1547-UTC7` prospectively from Game 3 onward  
**Authority commit:** `d63d372503f3c14ee058464ee77d041399de22ca`  
**Active analytical model:** `LoL v0.3.58 + E15R1 session speed/decay overlay`  
**Circuit breaker:** `CLEAR`  
**PDRL:** `ACTIVE`  
**PML:** `ACTIVE`  
**KH directional calibration:** `ACTIVE`  
**Small-H asymmetry calibration:** `ACTIVE`  
**E15R1 speed/decay overlay:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

User authorization on 2026-08-27 after Game 2: **“Ok lets do that for the rest of the series.”**

This authorizes the prospective Game-3-through-Game-5 live speed/opportunity-decay recalibration described in:

`models/lol/procedures/LOL_E15R1_LIVE_SPEED_AND_OPPORTUNITY_DECAY_OVERLAY_2026-08-27.md`

Historical Game 1 and Game 2 verdicts, positions and P/L remain frozen and must not be rewritten.

## Frozen authority

All model-certified analysis and TAKE execution from Game 3 onward must use analytical/procedural files frozen at:

`d63d372503f3c14ee058464ee77d041399de22ca`

LoL v0.3.59 and v0.3.60 remain retired and must not be loaded or blended.

## E15R1 execution override

For Games 3–5 only, the hard live `2SNAP` requirement for ML/KH/TK is replaced by **two independent evidence points**.

A certified exact-role professional draft mechanism may count as evidence point 1 when DIM + PDRL + PML pass and the causal mechanism/break condition are explicit. The first meaningful synchronized live snapshot may count as point 2 when it directly confirms that mechanism. No immediate-postdraft TAKE is allowed.

If draft evidence is weak/ambiguous/contradicted, two usable synchronized live snapshots remain the default path.

HOLD is temporary and must resolve on the next meaningful snapshot/objective/contact cycle or material reprice.

Opportunity decay is active:

- preferred causal entry window roughly 8–20 minutes;
- 20–24 minutes normal but terminal-event scan required;
- 24–27 minutes: materially stronger edge plus +3pp late-entry buffer where probability pricing applies;
- >=27 minutes: new TK/Duration presumptive PASS unless exceptional/non-terminal; ML/KH require +5pp buffer and CLEAR non-fragile mechanism.

Mechanism realization may outweigh isolated dragon/tower counters when causally coherent. Lead concentration remains decomposed but a fed role is not automatically discounted if it is the demonstrated conversion engine. Favorite -H may qualify earlier from forward signed-margin distribution rather than waiting for current margin to approach H.

## User line-existence confirmation gate — ACTIVE

User instruction on 2026-08-27: **“from now on only log the bet when i confirm it still exists.”**

This is a hard execution/logging rule and must be carried into successor LoL session locks unless the user explicitly revokes it.

- A visible model verdict `TAKE` is an analytical/execution candidate only until the user explicitly confirms that the quoted market/line/odds still exist and are executable.
- Do **not** create an Airtable `Positions` record merely because a TAKE verdict was issued.
- Do **not** count the candidate in bet history, W/L, or P/L unless the user confirms availability/existence at or after the verdict.
- User confirmation may be concise, e.g. `exists`, `still there`, `taken`, `yes`, or an updated screenshot clearly showing the same executable line/odds; ambiguity fails closed to unconfirmed.
- If the user reports the line moved/disappeared or does not confirm it before the market is no longer executable, record no position. The analytical TAKE may remain in snapshot/audit evidence as an unexecuted candidate, but it is not a bet.
- If the user confirms the market still exists but the price/line has materially changed, reassess the new executable price/line before logging; confirmation of a different market is not confirmation of the original candidate.
- For this series, live Airtable writes remain map-end batched. At map end, only user-confirmed executable TAKES may be written to `Positions`.
- This gate changes execution/logging only. It does not relax or tighten analytical TAKE certification.

Required execution state for every visible TAKE candidate:

`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

Only `CONFIRMED` permits Position logging and P/L settlement.

## Standing controls retained

- Official betting remains paused; shadow only.
- Minimum odds 1.60.
- No pregame/immediate-postdraft ML/KH/TK TAKE.
- Same-message user scoreboard + bookmaker screenshot pairs are presumed synchronized unless underlying game state materially contradicts.
- Ignore bookmaker/header/device clock differences alone for synchronization.
- Position-blind reassessment mandatory.
- Exact signed kill-margin arithmetic mandatory.
- KH side-neutral distribution/sign-after-distribution remains mandatory.
- No automatic underdog +kills selection.
- DOVC / FCR / FRP remain mandatory where applicable.
- Same-map maximum one TAKE per market family.
- Greyed/stale markets non-executable.
- No rescue, martingale, chasing, or stake escalation.
- No Airtable calls merely to log live frames or TAKES mid-map; buffer and batch-write/exact-verify at map end.
- Visible live verdict must be first and compact; deeper checks remain internal.

## Series state at E15R1 activation

Series: `NS 1–1 BFX`.

Game 1: NS won 27–8 in 27:53; no position.

Game 2: BFX won 27–12 in 30:55. Shadow Total Kills OVER 39.5 @2.086 entered at 24:40 lost on final total 39; P/L -0.25u. This remains a valid model loss and is not reclassified.

## Continuation / bootstrap requirement

Every continuation/new chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this `models/lol/session/CURRENT_SESSION_LOCK.md` and verify lock `LOL-2026-08-27-E15R1-NS-BFX-G3PLUS-1641-UTC7`;
4. re-fetch `CURRENT_MODEL.md` at authority commit `d63d372503f3c14ee058464ee77d041399de22ca`;
5. follow its exact required load order at that commit;
6. after the canonical frozen stack, explicitly load `models/lol/procedures/LOL_E15R1_LIVE_SPEED_AND_OPPORTUNITY_DECAY_OVERLAY_2026-08-27.md` at the same authority commit;
7. apply the active `User line-existence confirmation gate` from this mutable lock before any Position logging;
8. load the latest applicable NS-BFX live handoff last.

If the lock/authority cannot be matched, use `MODEL LOCK MISMATCH — HOLD`.
