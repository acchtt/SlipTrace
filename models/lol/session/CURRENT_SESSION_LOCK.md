# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-24-E8-BFXY-HLEC-1554-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-24 15:54 UTC+7`  
**Scope:** `LCK CL — BNK FEARX Youth vs Hanwha Life Esports Challengers series`  
**Default expiry:** `BFXY–HLEC series completion or explicit relock; hard stop 2026-08-25 00:00 UTC+7`  
**Authority commit:** `ad6c008e7227d9d16d341bc53b19a2c8a18a9435`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`  
**Minimum accepted odds:** `1.60`

## Authorization

On 2026-08-24 at 15:54 UTC+7 the user explicitly instructed **“Lock next lck cl serie.”**

The next LCK CL Play-In series on the 2026-08-24 slate is **BNK FEARX Youth vs Hanwha Life Esports Challengers**. This E8 epoch supersedes the DNS Challengers vs Kiwoom DRX Challengers lock and does not authorize a model-version change or analytical mutation.

## Frozen authority

All model-certified analysis for this series uses frozen authority commit:

`ad6c008e7227d9d16d341bc53b19a2c8a18a9435`

Canonical model remains **LoL v0.3.58**. v0.3.59 and v0.3.60 remain retired.

The frozen stack includes the active v0.3.58 rules and procedures in `CURRENT_MODEL.md`, including the mandatory mechanical execution validator:

`models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`

No default-branch analytical edit made after this authority commit affects this series unless the user explicitly authorizes another relock.

## Execution integrity

The visible word `TAKE` remains protected. Every candidate must pass the complete applicable PRE_TAKE_CERT mechanical validator with no failed fields, unresolved fields, or contradictions before a TAKE can be emitted.

Core execution controls remain:

- shadow stake `0.25u`; actual exposure `0u`;
- minimum odds `1.60`;
- pregame/immediate-postdraft ML/KH/TK TAKEs disabled;
- live ML/KH/TK require at least two usable synchronized live snapshots;
- one TAKE per market family per map;
- current synchronized sportsbook state/price controls;
- exact signed kill-margin arithmetic for kill handicap;
- position-blind reassessment;
- HOLD/PASS creates no Position;
- during a live map, Airtable writes are deferred until map end; qualified TAKEs, meaningful snapshots, and settlement details are retained in-session and batch-written afterward.

Any skipped mandatory field, ignored contradiction, stale certificate, wrong authority/model, or narrative/price override of a failed gate triggers the procedural circuit breaker.

## Live verdict latency handling

Per the user's 2026-08-24 feedback that a qualified line moved before the verdict arrived, live execution is now strictly **verdict-first**:

- do not call Airtable, GitHub, web, or any other connector in the critical path before emitting the live verdict when the required model/lock context is already loaded;
- complete the PRE_TAKE_CERT internally from the supplied synchronized screenshots and cached locked authority, then immediately emit `TAKE`, `HOLD`, or `PASS` with the exact visible line and stake;
- explanations must be compressed until after the verdict;
- if the quoted price/line is already gone or materially moved before the visible verdict reaches the user, the entry is **latency-invalidated** and must not count as an executable shadow bet or P/L event;
- a latency-invalidated entry is recorded as `Void / Invalidated / 0u` in Airtable at map-end reconciliation and does not consume the market family for subsequent fresh reassessment.

This is an execution-timing control only; it does not change the frozen analytical model or its gates.

## Airtable map-end batching

Per the user's explicit 2026-08-24 instruction **“Ok do it”**, Airtable is removed from the live decision path for the remainder of this lock.

During a live map:

- make **no Airtable read, write, search, create, update, or verification call** merely to log a live frame or TAKE;
- keep the running evidence ledger in-session: meaningful synchronized snapshots, HOLD/PASS states, TAKE entry clock/line/odds/stake, latency invalidations, and any user-supplied corrections;
- live verdict speed takes priority over ledger freshness.

At map end:

- batch-write the meaningful snapshots and any qualified TAKEs;
- record settlement, result, final map state, and any latency-invalidated counterfactual separately from executable P/L;
- perform duplicate protection and exact Airtable verification after the batch write;
- then clear the in-session map buffer only after successful verification.

If the conversation ends before map completion, preserve the buffered evidence in the latest live handoff so the next chat can reconcile Airtable after the map result is known.

## Source-specific state handling

Per the user's standing 2026-08-24 instructions, the scoreboard source's visible **“DELAYED DATA”** and **“FEED NOT UPDATING”** banners are excluded as decision signals. Do not classify a frame as stale solely because either banner appears.

This source-specific exclusion is display-label only. The underlying state must still be internally coherent and synchronized with the relevant live decision window. A real state conflict, impossible progression, materially mismatched clock/state, or other independent evidence of staleness still fails closed.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `ad6c008e7227d9d16d341bc53b19a2c8a18a9435`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. additionally load `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` from the same commit;
7. load the latest applicable live handoff last;
8. verify the authority/model match before model-certified analysis.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
