# DK vs GEN Game 3 — GEN +9.5 Kills Execution Review — 2026-08-22

**Status:** AUDIT REVIEW  
**Model authority:** LoL v0.3.58  
**Locked authority commit at entry:** `a4d537e2ef06de042397fdab2fa05464c6d242dc`  
**Map:** `LCK-2026-08-22-DK-GEN-G3`  
**Position:** `LCK-2026-08-22-DK-GEN-G3-KH-GEN+9.5-1349`

## Entry and result

Entry at 13:49:

- DK 5-3 GEN;
- DK approximately +2.6k gold;
- towers 1-1;
- dragons DK 2-0;
- GEN +9.5 kills @1.664;
- signed favorite margin `M = DK - GEN = +2`;
- GEN +9.5 loses at DK final margin `+10`;
- exact `NKB = 10 - 2 = 8`, DEEP.

Final: DK 19-7 GEN, final DK kill margin +12. Historical result remains LOSS, -0.25u shadow P/L, 0u actual exposure.

## Procedural finding — hard failure

The locked underdog +kills TAKE signature required:

`LOCK | MODEL | EXEC | ODDS | FAMILY | POSBLIND | 2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD | FALSE_STABLE_INACTIVE | UCS | SIGNED_MARGIN | EXACT_NKB | LIVE_PRESERVATION`

The Airtable position's recorded `GATE_SIG[...]` omitted **DIM, TAM, and CAS** entirely.

Under the active Session Authority Lock procedure, a missing required gate-signature field means the market is not TAKE-eligible. An underdog +kills TAKE under an authority commit containing DIM without resolved `DIM/TAM/CAS` is a circuit-breaker trigger.

Therefore the position is **AUDIT INVALIDATED**. Correct retrospective verdict: **HOLD/PASS**.

This is not a new rule and does not change the model. The required gate already existed in the locked authority.

## Analytical finding — UDKC/KMS should also have failed

Even apart from the missing signature fields, the draft interaction was misclassified.

Draft:

- DK: Jayce / Maokai / Ahri / Lucian / Milio
- GEN: Gragas / Wukong / Syndra / Kalista / Renata

DK's repeatable primary route was not generic committed dive. It was:

`Jayce pre-contact poke/zone -> Maokai/Ahri first-contact or pick -> Lucian/Milio ranged continuation -> objective/structure control`

GEN's credited protection was too generic:

- Renata and Wukong are stronger answers to committed contact/continuation than to pre-contact Jayce poke plus Ahri/Maokai pick geometry;
- Gragas can disrupt an engage but does not by itself neutralize DK's ranged setup;
- Kalista's damage access is shorter and more entry-dependent, forcing GEN to operate inside DK's controlled objective space.

The correct DIM interpretation is:

- `TAM = FAIL/UNRESOLVED` for GEN suppression of DK's primary repeatable route;
- `OSG = DK advantage`;
- `DAU = DK advantage from neutral setup`;
- `CAS = FAIL` for GEN because an ordinary DK advantage makes the next objective-entry cycle easier for DK and forces GEN back through the same poke/pick geometry;
- therefore `KMS = FAIL` and UDKC cannot be STABLE.

## Live-preservation finding

At 13:49 the live state should have downgraded, not preserved, GEN's fallback:

- DK held approximately +2.6k;
- DK led dragons 2-0;
- meaningful economy/control leverage was concentrated in Jayce, Maokai, and Ahri — the exact roles driving DK's setup and first-contact mechanisms.

The entry note treated the kill margin moving only from roughly DK +1 to DK +2 as observed anti-cascade proof. That is insufficient. A bounded scoreboard margin is a descriptor, not proof that the underdog has actually suppressed the favorite's repeatable net-margin expansion route.

`RLD/LIVE_PRESERVATION` should therefore have been downgraded.

## Cushion finding

The arithmetic itself was correct: NKB=8 was DEEP. The error was treating a deep cushion as compatible with a failed mechanism certificate.

A DEEP NKB never overrides failed `TAM/CAS/KMS`. Once GEN's suppression route fails, the handicap is ineligible regardless of the nominal cushion.

From entry to final, DK's margin expanded from +2 to +12, a further +10 net kills, crossing the +10 failure threshold. This is consistent with the repeated-control-route concern; it is not evidence for a new rule by itself.

## Classification

- Result: **LOSS**
- P/L: **-0.25u shadow**, **0u actual**
- Thesis state: **INVALIDATED**
- Correct retrospective verdict: **HOLD/PASS**
- Primary error: **missing mandatory DIM/TAM/CAS gate signature plus false STABLE KMS/CAS classification**
- Model change required: **NO**
- New rule required: **NO**
- Circuit breaker: **YES**, because an active hard gate was skipped/omitted.

## Required operational response

1. Preserve historical Loss and -0.25u P/L.
2. Mark the position Invalidated in Airtable.
3. Mark the map review complete with the execution error recorded.
4. Set `CURRENT_SESSION_LOCK.md` to `CIRCUIT_BREAKER` until the next valid slate lock or explicit user-authorized relock.
5. Do not amend v0.3.58 from this result. The locked DIM/TAM/CAS rule already covers the failure.
