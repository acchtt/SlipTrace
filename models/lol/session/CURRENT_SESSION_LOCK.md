# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-20-E2-2100-UTC7`  
**Status:** `CIRCUIT_BREAKER`  
**Effective:** `2026-08-20 21:00 UTC+7`  
**Default expiry:** `2026-08-21 00:00 UTC+7`  
**Authority commit:** `7098780fb503477483fda68fa10bfc910c49eb3b`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `ACTIVE`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

This lock epoch was explicitly authorized by the user on 2026-08-20 UTC+7 after the chat-transition execution-drift review.

The locked authority includes:

- frozen per-slate authority commit;
- mandatory market-family TAKE gate signatures;
- procedural circuit breaker;
- durable-fix write/fetch verification;
- UCS — Underdog Cushion Sufficiency downstream of UDKC.

## Circuit-breaker incident — BLG vs LGD Game 3

The breaker is now ACTIVE because the historical `LGD +12.5 kills @2.060` TAKE was subsequently reviewed as a draft-certification execution error under the already-active v0.3.58 KMS / False-Stable requirements.

The original UDKC credited Maokai + Renata as broad anti-cascade protection and Yorick as an independent side-lane suppression route without adequately matching those tools against BLG's repeatable `poke -> zone -> pick -> Pantheon follow-up` kill mechanism.

The locked fallback procedure already required explicit testing of favorite range/zone control, first-contact reliability, objective-entry control, repeated punishment routes, and the False-Stable Guard. Therefore this is not classified merely as a normal losing result: `KMS = PASS` / UDKC `STABLE` was too permissive under the locked authority.

Required state:

- `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`
- no further positions in this lock epoch;
- analysis/HOLD logging may continue;
- historical result/P&L remains unchanged;
- resume only at the next valid slate lock or after explicit user authorization to relock now.

Reference review committed after the lock:
`models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`

## Pending next-slate amendment

The default branch now contains a stronger Draft Interaction Matrix (`DIM`) amendment, but it is **not active inside this frozen authority commit**.

Pending files include:

- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- default-branch `models/lol/CURRENT_MODEL.md` amendment requiring DIM in the load order;
- default-branch session TAKE-signature amendment requiring `DIM / TAM / CAS` for underdog +kills.

These changes must be included in the next valid authority lock before being described as active for live TAKE decisions.

## New-chat requirement

A future chat while this lock is still the applicable slate lock must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. recognize `Status: CIRCUIT_BREAKER` and issue no new TAKES;
5. re-fetch `CURRENT_MODEL.md` at authority commit `7098780fb503477483fda68fa10bfc910c49eb3b` for any model-certified analysis of the frozen slate;
6. not silently activate newer default-branch analytical edits.

If the authority commit cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Mid-slate change rule

Normal wins/losses do not change this authority commit.

Any review/fix committed after this lock is `PENDING_NEXT_SLATE` unless the user explicitly authorizes another immediate relock.
