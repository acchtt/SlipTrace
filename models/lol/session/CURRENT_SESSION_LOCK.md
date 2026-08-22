# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-22-E1-1438-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-22 14:38 UTC+7`  
**Default expiry:** `2026-08-23 00:00 UTC+7`  
**Authority commit:** `a4d537e2ef06de042397fdab2fa05464c6d242dc`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization / slate transition

This is the normal new UTC+7 slate lock for 2026-08-22. The prior 2026-08-21 lock expired at the slate boundary and is superseded prospectively only; historical verdicts and ledger records are unchanged.

The authority commit includes the 2026-08-22 lineup/odds source fast-path amendment in `LOL_SESSION_BOOTSTRAP.md`. This is a governance/source-efficiency change only; the analytical model remains canonical LoL v0.3.58.

## Frozen authority

All analytical/procedural decisions for this slate use commit:

`a4d537e2ef06de042397fdab2fa05464c6d242dc`

Canonical model remains **LoL v0.3.58**. v0.3.59 and v0.3.60 remain retired/discarded.

Active controls include:

- Draft Interaction Matrix (DIM/TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP);
- UDKC + KPA/KMS/RLD + False-Stable guard;
- UCS for underdog +kills;
- FRP for Total Kills Under;
- FCR for Duration Under;
- Lead Decomposition / CFC for Live ML;
- DPS and LRO for Live ML against a CLEAR/STRONG draft prior;
- complete family-specific `GATE_SIG[...]` persistence;
- one TAKE per market family per map;
- minimum odds 1.60;
- shadow-only execution policy;
- saved-lineup/user-confirmed-lineup + sportsbook-screen fast path with no duplicate web roster/odds lookup unless missing, conflicting, ambiguous, or explicitly requested.

## Live execution

Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.

Live ML/KH/TK require two usable live snapshots. Live ML against a CLEAR/STRONG draft prior requires the LRO three-snapshot/two-cycle certificate.

Underdog +kills requires DIM/TAM/CAS, complete draft-only UDKC, live preservation, exact signed margin/NKB and UCS. Favorite -kills requires exact signed margin, RNE, FFD, remaining forced-fight schedule, Structure Substitution and safe-concede checks.

Before every TAKE, every required gate-signature field must be explicit PASS or valid N/A. Missing/FAIL/UNRESOLVED means HOLD/PASS.

## Source fast path

When saved lineup context and a user-confirmed exact five agree, treat the lineup as confirmed and do not duplicate-check generic roster websites. A readable user sportsbook screenshot is the market authority for displayed odds/lines. External lookup is only for genuine missing/conflicting/ambiguous information, a specific substitution concern, an unshown market, cross-book comparison, or explicit user request.

## New-chat requirement

A future chat while this lock is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `a4d537e2ef06de042397fdab2fa05464c6d242dc`;
5. load the analytical/procedural stack from that same commit;
6. load the latest live handoff last as state only;
7. refuse later default-branch analytical edits unless another explicit relock occurs.

If authority cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Circuit breaker

Circuit breaker is CLEAR at activation. A procedural hard-gate violation, missing required signature, authority mismatch, prohibited live-to-draft proof, skipped market-family hard gate, or contrary-CLEAR/STRONG-draft ML TAKE without the required LRO certificate triggers the procedural circuit breaker and blocks further TAKES until a valid relock.

A fully canonical loss does not trigger the breaker.

## Mid-slate change rule

Normal wins/losses do not change this authority commit. Any further analytical/procedural edit is pending until the next lock unless the user explicitly authorizes another immediate relock.
