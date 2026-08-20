# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-20-E3-2208-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-20 22:08 UTC+7`  
**Default expiry:** `2026-08-21 00:00 UTC+7`  
**Authority commit:** `c0b06041b8ef59d8d9d932847cc57aa27b1d2577`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

The user explicitly authorized an immediate new session/relock on 2026-08-20 at 22:08 UTC+7 by instructing: `Start new session now`.

This closes the prior E2 circuit-breaker epoch for future TAKE eligibility without altering any historical result, P/L, invalidation, or audit finding.

## Activated authority

This lock freezes analytical/procedural authority at commit:

`c0b06041b8ef59d8d9d932847cc57aa27b1d2577`

The locked authority keeps canonical **LoL v0.3.58** and includes the post-review draft-reading correction:

- mandatory `DIM — Draft Interaction Matrix` before model-certified draft edges / draft-derived fallback classifications;
- exact role resolution before DIM;
- primary/secondary kill-mechanism mapping;
- `TAM — Threat-Answer Matching`;
- `OSG — Objective-Setup Geometry`;
- `DAU — Damage Access & Uptime`;
- `SLI — Side-Lane Independence`;
- `FNF — Frontline Necessity Fit`;
- `CAS — Collapse Asymmetry`;
- `ETS — Execution & Team-Strength modifier`;
- mandatory `AFP — Adversarial Favorite Pass`;
- separate Draft Edge and underdog +kills Stability outputs;
- underdog +kills TAKE signature requires `DIM / TAM / CAS` in addition to UDKC/KMS/RLD/UCS and all retained gates.

Mandatory DIM procedure:
`models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`

## Prior breaker incident retained as history

The prior E2 breaker was triggered by the BLG vs LGD Game 3 `LGD +12.5 kills @2.060` draft-certification error. That position remains historically settled as a Loss with its original P/L and audit-invalidated classification.

Starting E3 does not erase that incident; it only creates the explicitly authorized new authority epoch in which the corrective DIM procedure is now part of the frozen stack.

## New-chat requirement

A future chat while this lock is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `c0b06041b8ef59d8d9d932847cc57aa27b1d2577`;
5. load the locked analytical/procedural stack from that same commit, including DIM;
6. load the latest live handoff last as state only;
7. refuse later default-branch analytical edits unless another explicit relock occurs.

If the authority commit cannot be loaded or the model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Circuit-breaker rule

If any TAKE in this E3 epoch is later found to violate an active hard gate, use draft-only proof incorrectly, omit a required `GATE_SIG[...]` field, or substitute narrative confidence for a required mechanism gate:

- set `Status: CIRCUIT_BREAKER`;
- set `Circuit breaker: ACTIVE`;
- issue no further TAKES until the next valid lock or another explicit user-authorized relock.

A fully canonical bet that simply loses does not trigger the breaker.

## Mid-slate change rule

Normal wins/losses do not change this authority commit. Any analytical/procedural fix committed after this lock is pending for the next lock unless the user explicitly authorizes another immediate relock.
