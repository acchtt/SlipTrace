# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-22-E2-1633-UTC7`  
**Status:** `CIRCUIT_BREAKER`  
**Effective:** `2026-08-22 16:33 UTC+7`  
**Default expiry:** `2026-08-23 00:00 UTC+7`  
**Authority commit:** `a4d537e2ef06de042397fdab2fa05464c6d242dc`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `ACTIVE — 2026-08-22 17:48 UTC+7; DK vs GEN Game 3 GEN +9.5 underdog +kills TAKE omitted mandatory DIM/TAM/CAS fields and was audit-invalidated`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization / relock

The user explicitly authorized an immediate relock for the ongoing **DK vs GEN Game 2** at **2026-08-22 16:33 UTC+7** after the prior lock entered `CIRCUIT_BREAKER` state.

This started a new lock epoch without changing the analytical authority. The frozen authority remains commit:

`a4d537e2ef06de042397fdab2fa05464c6d242dc`

Canonical model remains **LoL v0.3.58**. No new analytical/procedural amendment was activated by that relock.

The prior **DK +10.5 kills @1.734** position remains historically **INVALIDATED / VOID / 0u P&L** and is not resurrected by the relock.

Because the canonical common TAKE signature requires `FAMILY = no prior TAKE in the same map/market family`, the **Kill Handicap family remained consumed for DK vs GEN Game 2** despite the invalidation.

## Current circuit-breaker state

At **2026-08-22 17:48 UTC+7**, review of **DK vs GEN Game 3** found that the visible **GEN +9.5 kills @1.664** TAKE was issued under this locked authority without the mandatory `DIM`, `TAM`, and `CAS` fields in its persisted underdog +kills gate signature.

The locked procedure explicitly required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD | FALSE_STABLE_INACTIVE | UCS | SIGNED_MARGIN | EXACT_NKB | LIVE_PRESERVATION`

Missing mandatory fields are a hard gate failure and a procedural circuit-breaker trigger. The position has therefore been audit-invalidated in Airtable while preserving its historical **Loss / -0.25u shadow P&L / 0u actual exposure**.

The analytical review also found that GEN's KMS/CAS should not have passed against DK's repeatable Jayce poke/zone -> Maokai/Ahri first-contact -> Lucian/Milio continuation route, especially with DK's live leverage concentrated in the setup roles and a 2-0 dragon lead at entry. A bounded kill margin was incorrectly treated as anti-cascade proof.

Reference review:
`models/lol/reviews/DK_GEN_G3_GEN_PLUSKILLS_DIM_EXECUTION_REVIEW_2026-08-22.md`

**Current operational consequence:** no new TAKEs/positions may be issued under this epoch. Analysis and HOLD logging may continue. TAKE eligibility resumes only at the next valid slate lock or after explicit user authorization to relock now.

## Pending procedural amendment — mechanical pre-TAKE interlock

At **2026-08-22 18:00 UTC+7**, the user explicitly instructed: **"Add the mechanical rule now."**

The default branch procedure:

`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

was amended at commit:

`e60e5b96d792ad493d24f29c1795607a271b0f32`

to add a hard `PRE_TAKE_CERT` execution interlock and anti-hindsight accounting. The new rule requires the complete family certificate to mechanically validate **before** the visible word `TAKE` may be emitted; any missing/failed/unknown field forces HOLD/PASS; any material state change expires the certificate; and postgame review may not rewrite a historical prediction result into a fictional pre-entry HOLD.

Because this epoch's frozen authority remains `a4d537e2ef06de042397fdab2fa05464c6d242dc`, this amendment is **PENDING_NEXT_LOCK** and does not silently alter the current locked stack. The current breaker already prohibits new TAKEs. The mechanical interlock becomes active at the next valid authority lock or an explicit user-authorized relock that includes commit `e60e5b96d792ad493d24f29c1795607a271b0f32` or a descendant containing the same verified rule.

## Frozen authority

All analytical/procedural decisions for this slate continue to reference commit:

`a4d537e2ef06de042397fdab2fa05464c6d242dc`

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

While this lock remains in `CIRCUIT_BREAKER`, model-certified analysis may continue but all new TAKE issuance is suspended.

If explicitly relocked, the following locked rules remain unchanged unless the new relock authority includes a later verified amendment:

Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.

Live ML/KH/TK require two usable live snapshots. Live ML against a CLEAR/STRONG draft prior requires the LRO three-snapshot/two-cycle certificate.

Underdog +kills requires DIM/TAM/CAS, complete draft-only UDKC, live preservation, exact signed margin/NKB and UCS. Favorite -kills requires exact signed margin, RNE, FFD, remaining forced-fight schedule, Structure Substitution and safe-concede checks.

Before every TAKE, every required gate-signature field must be explicit PASS or valid N/A. Missing/FAIL/UNRESOLVED means HOLD/PASS.

A displayed sportsbook market must be executable at the assessed synchronized state/price pair. If a fight or material state change occurs during the decision/entry window, that candidate is not TAKE-eligible from the pre-change assessment.

## Source fast path

When saved lineup context and a user-confirmed exact five agree, treat the lineup as confirmed and do not duplicate-check generic roster websites. A readable user sportsbook screenshot is the market authority for displayed odds/lines. External lookup is only for genuine missing/conflicting/ambiguous information, a specific substitution concern, an unshown market, cross-book comparison, or explicit user request.

## New-chat requirement

A future chat while this lock is active or in circuit-breaker state must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `a4d537e2ef06de042397fdab2fa05464c6d242dc`;
5. load the analytical/procedural stack from that same commit;
6. load the latest live handoff last as state only;
7. refuse later default-branch analytical edits unless another explicit relock occurs.

If authority cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

If this file remains in `CIRCUIT_BREAKER`, visible TAKE status is:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

## Circuit breaker history

### 2026-08-22 16:26 UTC+7 — prior epoch E1

Prior epoch `LOL-2026-08-22-E1-1438-UTC7` triggered the circuit breaker after the Game 2 **DK +10.5 @1.734** TAKE was found to have been issued while a fight occurred during the decision/entry window. The sportsbook price and assessed state were not a clean synchronized pair, so the position was voided for model audit.

The user explicitly authorized epoch E2 at **16:33 UTC+7**. That cleared the breaker prospectively without changing analytical authority.

### 2026-08-22 17:48 UTC+7 — current epoch E2

The Game 3 **GEN +9.5 kills @1.664** TAKE was found to have omitted mandatory `DIM/TAM/CAS` gate fields under an authority commit where those fields were required. The position was additionally found to have a false STABLE KMS/CAS classification against DK's repeatable poke/pick/control route.

This is an execution/hard-gate failure, not a normal model loss. The circuit breaker is therefore active again.

A fully canonical loss does not trigger the breaker.

## Mid-slate change rule

Normal wins/losses do not change this authority commit. No new analytical rule is added from the GEN +9.5 outcome; the existing locked DIM/TAM/CAS rule already covered the failure. The mechanical PRE_TAKE_CERT rule written at 18:00 UTC+7 is a procedural execution safeguard and is explicitly pending the next lock; it does not silently alter the current frozen authority.
