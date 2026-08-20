# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-20-E2-2100-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-20 21:00 UTC+7`  
**Default expiry:** `2026-08-21 00:00 UTC+7`  
**Authority commit:** `7098780fb503477483fda68fa10bfc910c49eb3b`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

This is an explicit relock/new epoch authorized by the user on 2026-08-20 UTC+7 after the chat-transition execution-drift review.

The relock activates the governance corrections already present at the authority commit, including:

- frozen per-slate authority commit;
- mandatory market-family TAKE gate signatures;
- procedural circuit breaker;
- durable-fix write/fetch verification;
- UCS — Underdog Cushion Sufficiency downstream of UDKC.

## New-chat requirement

A future chat on this active slate must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `7098780fb503477483fda68fa10bfc910c49eb3b`;
5. load the analytical/procedural stack from that same commit;
6. refuse to let newer default-branch analytical edits silently affect this slate.

If the authority commit cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Circuit-breaker rule

If any TAKE in this lock epoch is later found to have violated an active hard gate or lacked its mandatory complete `GATE_SIG[...]`, update this lock to:

- `Status: CIRCUIT_BREAKER`
- `Circuit breaker: ACTIVE`

and issue no further TAKES until the next valid lock or explicit user authorization to relock.

A fully canonical losing bet does not trigger the breaker.

## Mid-slate change rule

Normal wins/losses do not change this authority commit.

Any review/fix committed after this lock is `PENDING_NEXT_SLATE` unless the user explicitly authorizes another immediate relock.
