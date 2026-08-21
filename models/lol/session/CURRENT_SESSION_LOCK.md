# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-21-E1-1151-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-21 11:51 UTC+7`  
**Default expiry:** `2026-08-22 00:00 UTC+7`  
**Authority commit:** `66aebe9c45e0d95721d39b7e3eca443a46472ff7`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

This is the automatic new UTC+7 slate lock required by active governance after the prior `LOL-2026-08-20-E3-2208-UTC7` lock expired at the 2026-08-21 day boundary.

The first 2026-08-21 match context is LCK CL NS vs T1A. The official match-specific starting lineup and user-supplied series pregame prices were saved before this lock at the authority commit.

## Activated authority

This lock freezes analytical/procedural authority at commit:

`66aebe9c45e0d95721d39b7e3eca443a46472ff7`

Canonical analytical model remains **LoL v0.3.58**.

The frozen stack includes the 2026-08-20 draft-reading correction and all retained gates, including:

- mandatory `DIM — Draft Interaction Matrix` before draft edge / draft-derived fallback classification;
- exact roles before DIM;
- PKM / SKM mechanism mapping;
- `TAM — Threat-Answer Matching`;
- `OSG — Objective-Setup Geometry`;
- `DAU — Damage Access & Uptime`;
- `SLI — Side-Lane Independence`;
- `FNF — Frontline Necessity Fit`;
- `CAS — Collapse Asymmetry`;
- `ETS — Execution & Team-Strength modifier`;
- mandatory `AFP — Adversarial Favorite Pass`;
- separate Draft Edge and underdog +kills Stability outputs;
- full UDKC + KPA/KMS/RLD + False-Stable guard;
- UCS downstream of STABLE UDKC;
- FRP for TK Under;
- FCR for Duration Under;
- Lead Decomposition/CFC for live ML;
- FFD/RNE for favorite -kills;
- complete market-family `GATE_SIG[...]` persistence;
- one TAKE per market family per map;
- minimum odds 1.60;
- official betting paused, shadow only.

## NS vs T1A match-specific context

Saved official lineup file:
`models/lol/context/lineups/LCK_CL_2026-08-21_NS_T1A.md`

Starting five:
- NS: Janu / MihawK / SeTab / Lucy / Pleata
- T1A: Haetae / Painter / Guti / Cypher / Cloud

Series pregame prices are context only and are not Map 1 live prices.

## Live execution

Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.

Live ML/KH/TK require two usable live snapshots. Underdog +kills requires DIM/TAM/CAS + complete draft-only UDKC + live preservation + exact signed margin/NKB + UCS. Favorite -kills requires exact RNE + FFD + remaining forced-fight/Structure Substitution checks.

Before every TAKE, every required gate-signature field must be explicit PASS or valid N/A. Missing/FAIL/UNRESOLVED means HOLD/PASS.

## New-chat requirement

A future chat while this lock is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `66aebe9c45e0d95721d39b7e3eca443a46472ff7`;
5. load the analytical/procedural stack from that same commit;
6. load the latest live handoff last as state only;
7. refuse later default-branch analytical edits unless another explicit relock occurs.

If the authority commit cannot be loaded or the model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Circuit-breaker rule

If any TAKE in this E1 epoch is later found to violate an active hard gate, use prohibited live-to-draft proof, omit a required `GATE_SIG[...]` field, or substitute narrative confidence for a required mechanism gate:

- set `Status: CIRCUIT_BREAKER`;
- set `Circuit breaker: ACTIVE`;
- issue no further TAKES until the next valid lock or explicit relock.

A fully canonical bet that simply loses does not trigger the breaker.

## Mid-slate change rule

Normal wins/losses do not change this authority commit. Any analytical/procedural fix committed after this lock is pending for the next lock unless the user explicitly authorizes another immediate relock.
