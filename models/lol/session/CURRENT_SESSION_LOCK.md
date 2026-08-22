# Current LoL Session Lock

**Current Lock ID:** `LOL-2026-08-22-E2-1633-UTC7`  
**Current Status:** `CIRCUIT_BREAKER`  
**Current authority commit:** `a4d537e2ef06de042397fdab2fa05464c6d242dc`  
**Active analytical model:** `LoL v0.3.58`  
**Current actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Current breaker

The current E2 epoch remains in `CIRCUIT_BREAKER` because the DK vs GEN Game 3 `GEN +9.5 kills @1.664` TAKE omitted mandatory `DIM/TAM/CAS` fields under the locked authority. No new TAKEs may be issued under E2. Analysis/HOLD work may continue.

The historical prediction result remains `LOSS / -0.25u shadow / 0u actual`; procedural invalidation does not erase the prediction miss from performance accounting.

## User-authorized next-match lock phase

At **2026-08-22 18:21 UTC+7**, the user explicitly authorized:

**`NEXT LOCK PHASE BEGINS AT THE NEXT MATCH BOUNDARY.`**

Operational meaning:

1. Do **not** clear E2 early. The present circuit breaker stays active until the current match boundary is complete.
2. At the start of the **next match**, create a new lock epoch before any TAKE-eligible live decision.
3. The new epoch clears the prior breaker prospectively; historical invalidations and prediction results remain unchanged.
4. The new authority must include the verified mechanical `PRE_TAKE_CERT` interlock written in commit `e60e5b96d792ad493d24f29c1795607a271b0f32`, or a verified descendant containing the identical rule.
5. The new lock must freeze one exact authority commit and use that commit for `CURRENT_MODEL.md` plus the complete locked analytical/procedural load order.
6. No TAKE may be emitted in the new epoch until the lock itself has been written and fetched back successfully.

This instruction is an explicit relock authorization for the **next match boundary only**. It is not permission for arbitrary later mid-match relocks.

## Mechanical PRE_TAKE_CERT requirement for the next epoch

The next-match authority must contain the verified hard execution interlock in:

`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

Required order for every candidate:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable write -> exact verification`

Before the word `TAKE` may be emitted:

- every common and family-specific required field must exist exactly once;
- every categorical gate must be explicit `PASS` or a specifically permitted `N/A`;
- any `FAIL`, `UNRESOLVED`, `UNKNOWN`, blank, omitted, implied, or narrative-only requirement forces `HOLD/PASS`;
- exact line/odds/state/lock and family arithmetic must be populated where required;
- the assessed state and executable price must belong to the same usable decision window;
- any fight, kill change, objective capture, structure change, or other material live transition expires the certificate and requires a full rebuild from a fresh synchronized state/price pair;
- there is no analyst override for a failed certificate.

Postgame review cannot rewrite a historical losing prediction into a fictional pre-entry HOLD. Track independently:

- `PREDICTION_RESULT = WIN / LOSS / PUSH / VOID`
- `PROCESS_VALIDITY = VALID / INVALIDATED`

Performance accounting may not improve model accuracy by deleting losses merely because a later diagnostic says the analysis could have been different.

## Existing frozen E2 authority

Until the next match boundary, analytical/procedural decisions remain frozen to:

`a4d537e2ef06de042397fdab2fa05464c6d242dc`

Existing controls include DIM/TAM/CAS, UDKC/KMS/RLD/UCS, FRP, FCR, Live ML Lead Decomposition/CFC/LRO, exact family signatures, one TAKE per family per map, minimum odds 1.60, shadow-only execution, and synchronized state/price enforcement.

## New-chat requirement before the next match

A new chat must fetch:

1. default-branch `models/lol/CURRENT_MODEL.md`;
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. this `CURRENT_SESSION_LOCK.md`;
4. the current E2 locked authority if the next match has not begun yet.

When the next match begins, use the explicit authorization above to create the new epoch, verify that its authority contains the `PRE_TAKE_CERT` rule, write the new lock, fetch it back, and only then restore TAKE eligibility.

If authority or lock verification fails, use `MODEL LOCK MISMATCH — HOLD`.
