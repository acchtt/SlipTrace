# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-21-E2-1229-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-21 12:29 UTC+7`  
**Default expiry:** `2026-08-22 00:00 UTC+7`  
**Authority commit:** `e2feb481ea9c1f62122b34de50cfe1ab01ddd3dc`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

Explicit user authorization was given for an immediate mid-slate relock so the new Live ML draft-prior degradation / regime-override procedure can be used prospectively for Game 2 and later decisions.

The prior `LOL-2026-08-21-E1-1151-UTC7` epoch is superseded for future decisions. Historical Game 1 verdicts and ledger records are not rewritten.

## Activated authority

Frozen analytical authority:

`e2feb481ea9c1f62122b34de50cfe1ab01ddd3dc`

Canonical model remains **LoL v0.3.58**.

This authority includes:

- mandatory Draft Interaction Matrix;
- UDKC + KPA/KMS/RLD + False-Stable guard;
- UCS for underdog +kills;
- FRP for Total Kills Under;
- FCR for Duration Under;
- Lead Decomposition / CFC for Live ML;
- `DPS — Draft Prior State` for Live ML;
- current-state neutral-fight stress using current items, levels, role economy and objective schedule;
- `LRO — Live Regime Override` for Live ML selections opposing a CLEAR/STRONG draft prior;
- contrary-draft LRO requires `3SNAP`, `2CYCLE`, regime persistence, multi-role leverage, `DPS=BROKEN`, `CFC_CURRENT`, next-cycle stress and `DRP` all PASS;
- LRO applies only to ML and cannot create draft proof for another market family;
- complete market-family `GATE_SIG[...]` persistence and `LRO[...]` persistence when applicable;
- one TAKE per market family per map;
- minimum odds 1.60;
- shadow-only execution policy.

Mandatory Live ML procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

Reference review:
`models/lol/reviews/NS_T1A_G1_LIVE_ML_DRAFT_PRIOR_ANCHORING_REVIEW_2026-08-21.md`

## Prospective-only activation

The Game 1 missed-window review remains calibration only and does not create a retrospective position. This E2 authority applies prospectively from this lock forward, including Game 2.

## Live execution

Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.

Live ML/KH/TK require two usable live snapshots. A Live ML selection opposing a CLEAR/STRONG draft prior additionally requires the LRO three-snapshot/two-cycle certificate.

Underdog +kills still requires DIM/TAM/CAS, complete draft-only UDKC, live preservation, exact signed margin/NKB and UCS. Favorite -kills retains exact RNE, FFD and remaining forced-fight/Structure Substitution checks.

Before every TAKE, every required gate-signature field must be explicit PASS or valid N/A. Missing/FAIL/UNRESOLVED means HOLD/PASS.

## New-chat requirement

A future chat while this lock is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `e2feb481ea9c1f62122b34de50cfe1ab01ddd3dc`;
5. load the analytical/procedural stack from that same commit, including the Live ML LRO procedure;
6. load the latest live handoff last as state only;
7. refuse later default-branch analytical edits unless another explicit relock occurs.

If the authority commit cannot be loaded or the model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Circuit breaker

Circuit breaker is CLEAR at E2 activation. A procedural hard-gate violation, missing required signature, authority mismatch, prohibited live-to-draft proof, or contrary-CLEAR/STRONG-draft ML TAKE without the required LRO certificate activates the breaker and blocks further TAKES until a valid relock.

A fully canonical loss does not trigger the breaker.

## Mid-slate change rule

Normal outcomes do not change this authority commit. Any further analytical/procedural edit is pending until the next lock unless the user explicitly authorizes another immediate relock.
