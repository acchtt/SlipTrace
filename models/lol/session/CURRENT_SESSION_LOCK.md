# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-24-E7-DNSC-KRXC-1336-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-24 13:36 UTC+7`  
**Scope:** `LCK CL — DNS Challengers vs Kiwoom DRX Challengers series`  
**Default expiry:** `DNSC–KRXC series completion or explicit relock; hard stop 2026-08-25 00:00 UTC+7`  
**Authority commit:** `4c16955f8779e972ecee80dbd6127c70162b138a`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`

## Authorization

On 2026-08-24 at 13:36 UTC+7 the user explicitly instructed **“Relock this match.”**

The prior BFX–NS authority epoch expired at the UTC+7 slate boundary. This establishes a new authority epoch for the active DNS Challengers vs Kiwoom DRX Challengers LCK CL series. It does not authorize a model-version change or analytical mutation.

## Frozen authority

All model-certified analysis for this series uses frozen authority commit:

`4c16955f8779e972ecee80dbd6127c70162b138a`

Canonical model remains **LoL v0.3.58**. v0.3.59 and v0.3.60 remain retired.

The frozen stack includes the active v0.3.58 rules and procedures in `CURRENT_MODEL.md`, plus the mandatory mechanical execution validator:

`models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`

No default-branch analytical edit made after this authority commit affects this series unless the user explicitly authorizes another relock.

## Execution integrity

All model-certified live decisions must follow the frozen authority and the mechanical validator. Any missing required field, unresolved contradiction, stale decision state, authority mismatch, or skipped mandatory mechanism fails closed.

The procedural circuit breaker triggers on execution failure; an ordinary model outcome does not itself trigger it.

## Source-specific state handling

Per the user's explicit 2026-08-24 instruction, the scoreboard source's visible **“DELAYED DATA”** banner is excluded as a decision signal for this series. Do not classify a frame as stale solely because that banner appears.

The underlying state must still be internally coherent and synchronized with the relevant live decision window. A real state conflict, impossible progression, materially mismatched clock/state, or other independent evidence of staleness still fails closed.

The already logged 11:42 and 16:02 Game 2 frames remain usable historical live evidence after this relock if coherent. Any new live decision must use a fresh current state and be fully revalidated under this E7 lock.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `4c16955f8779e972ecee80dbd6127c70162b138a`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. additionally load `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` from the same commit;
7. load the latest applicable live handoff last;
8. verify the authority/model match before model-certified analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
