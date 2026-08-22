# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
- Mandatory new-chat bootstrap: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
- Session lock governance: `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
- **LoL v0.3.59 and v0.3.60 are retired/discarded from the active analytical hierarchy.**
- Their files may remain only as historical/audit artifacts. Do not load, blend, or auto-restore them.

User instruction on 2026-08-16 UTC+7: **“Discard newer versions, update this version accordingly.”**

The prior temporary v0.3.58 override is ended. v0.3.58 is the canonical model, not a temporary rollback.

---

## Mandatory session bootstrap / authority-drift guard

Every new chat/session must fetch this `CURRENT_MODEL.md` first, then immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md` before continuing the remaining load order.

Conversation memory, project context, pasted transfer prompts, older handoffs, historical model labels, and prior assistant output never override this file or an active frozen Session Authority Lock.

If live evidence arrives before bootstrap is complete, the only valid visible verdict is:

`MODEL NOT LOADED — HOLD`

No tool call may precede that visible HOLD. Bootstrap then completes and the same synchronized evidence may be reassessed if still valid.

A model/version vocabulary mismatch is a hard tripwire: stop model-certified analysis, reload this file + bootstrap + current session lock, and fail closed until the authority lock passes.

Reference incident review:
`models/lol/reviews/DNS_NS_G3_SESSION_BOOTSTRAP_AND_FRP_EXECUTION_REVIEW_2026-08-18.md`

---

# Canonical v0.3.58 in-place amendments

## 1. Duration Over — Structure Substitution / real stall evidence

Canonical v0.3.58 retains the KRX vs BRO Game 2 correction:

- low kills are not positive Duration stall evidence by themselves;
- 0-0 towers / no first tower / low absolute tower count are neutral state descriptors by default;
- conversion evidence must be classified as `ABSENT CONVERSION` or `FAILED CONVERSION`;
- only actual failed conversion or another clearly observed clock-consuming defense/reset mechanism may support the structure portion of an Over thesis;
- Structure Substitution is mandatory — objective/tower progress can compress clock even while kills remain low;
- Duration Over requires two independent positive clock-consuming mechanisms, with at least one grounded in observed failed conversion or equivalent repeated denial;
- every Duration Over must test the shortest plausible next compulsory fight/objective -> serial structures -> base -> Nexus cascade.

Reference:
`models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

## 2. Daily-audit gap fix

Canonical v0.3.58 includes:

- **FRP — Forward Regime Persistence** for every Total Kills Under;
- **FCR — Fast-Close Robustness** / one-disruption stress test for every normal Duration Under;
- **Lead Decomposition + CFC — Compulsory Fight Control** for every live Moneyline;
- **SMR — Same-Mechanism Re-certification** when a later same-series TAKE relies on a previously diagnosed failed mechanism.

Reference:
`models/lol/reviews/V0.3.58_CANONICAL_GAP_FIX_2026-08-16.md`

## 3. Underdog +kills — KPA/KMS, RLD, UDKC, DIM

Canonical v0.3.58 requires:

- **KPA — Kill Production Ability** and **KMS — Kill-Margin Suppression** as separate tests;
- `STABLE` fallback only when both pass with FER/PDC/PST/ARI and retained fallback-floor controls;
- **RLD — Role-Leverage Decomposition** so isolated top-side economy/grubs are not treated as generic grouped-fight resistance;
- False-Stable Guard when favorite repeatable range/zone/siege/continuation overwhelms the underdog's claimed reset path;
- complete draft-only **UDKC — Underdog +Kills Draft Certificate**;
- strict Draft-Isolation reconstruction when the exact draft is first recovered after live play has begun;
- mandatory **DIM — Draft Interaction Matrix** with exact roles, TAM, OSG, DAU, SLI, FNF, CAS, ETS and AFP before draft-derived fallback certification;
- `TAM = FAIL/UNRESOLVED` or `CAS = FAIL/UNRESOLVED` forbids `KMS = PASS` and UDKC `STABLE`.

Mandatory procedures:
- `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`

References:
- `models/lol/reviews/KC_GX_G1_UNDERDOG_KILLS_FALSE_STABLE_REVIEW_2026-08-18.md`
- `models/lol/reviews/DNS_BRO_G1_UNDERDOG_KILLS_ROLE_LEVERAGE_AND_DURATION_EXECUTION_REVIEW_2026-08-19.md`
- `models/lol/reviews/DNS_BRO_G2_UNDERDOG_PLUSKILLS_DRAFT_LOCK_EXECUTION_REVIEW_2026-08-19.md`
- `models/lol/reviews/UDKC_DRAFT_ISOLATION_AMENDMENT_2026-08-20.md`
- `models/lol/reviews/BLG_LGD_G3_DRAFT_INTERACTION_REVIEW_2026-08-20.md`

## 4. Live Moneyline — Draft Prior Degradation & Live Regime Override

Draft remains a prior for Live ML, not a permanent veto.

Mandatory controls:

- classify `DPS — Draft Prior State` as `INTACT / DEGRADED / BROKEN`;
- current-state neutral-fight stress uses current levels/items/role economy/objective schedule;
- ordinary Live ML remains two-snapshot eligible when aligned with a CLEAR/STRONG draft prior or when the original draft edge was SLIGHT/EVEN/UNCLEAR;
- an ML TAKE against a CLEAR/STRONG draft prior requires `LRO = PASS`;
- contrary-draft LRO requires three usable snapshots, at least two meaningful contact/objective cycles, regime persistence, multi-role leverage, `DPS=BROKEN`, `CFC_CURRENT=PASS`, next-cycle stress PASS and `DRP=PASS`;
- LRO applies to ML only and cannot create or upgrade draft-only underdog +kills proof.

Mandatory procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

Reference:
`models/lol/reviews/NS_T1A_G1_LIVE_ML_DRAFT_PRIOR_ANCHORING_REVIEW_2026-08-21.md`

## 5. 2026-08-23 execution hardening — DOVC + LAC

User instruction on 2026-08-23 UTC+7 after the FNC–SHFT / SK–MKOI review: **“Adjust accordingly.”**

This explicitly authorizes an in-place v0.3.58 enforcement amendment and a new authority epoch. No newer analytical version is authorized.

### DOVC — Duration Over Verification Certificate

Every Duration Over candidate must explicitly resolve:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

Hard effects:

- `ABSENT CONVERSION` or `UNRESOLVED` => HOLD/PASS;
- theoretical waveclear/peel/disengage cannot substitute for observed delay under real pressure;
- 0-0 towers, low towers, low kills, close gold, neutral dragons and quiet elapsed time cannot count as positive clock mechanisms;
- the actual failed-conversion / repeated-denial live window must be identified;
- missing or narrative-only DOVC fields fail PRE_TAKE_CERT mechanically.

### LAC — Live Anti-Cascade Confirmation for underdog +kills

After draft-only DIM + UDKC `STABLE`, every underdog +kills candidate must also prove `LAC = PASS` from the current live regime.

LAC asks whether the underdog has **demonstrated** suppression of repeated favorite net kill-margin expansion, rather than merely owning a numerical cushion.

A kill lead, one dragon, small gold lead, 0-0 towers, a large +kills buffer, theoretical scaling/waveclear/peel, isolated lane economy, grubs, or attractive price cannot by themselves satisfy LAC.

When the favorite has repeatable engage/pick/zone/siege/continuation and the underdog has only shallow non-structural live leverage with no demonstrated reset/return-kill/denial cycle, `LAC = FAIL/UNRESOLVED` and the +kills candidate is HOLD.

Mandatory procedure:
`models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`

Reference review:
`models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`

This amendment does **not** add a new conservative gate to Live ML. It hardens only the identified failure mechanisms.

---

# Active operational governance

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum accepted odds: **1.60**.
- Every new chat/session must complete bootstrap and inherit the active frozen Session Authority Lock.
- Verdict first; no Airtable logging, web research, or nonessential connector work before the visible live verdict.
- Immediately after every valid visible live verdict, Airtable map/snapshot logging is mandatory and the expected record must be verified.
- HOLD/PASS create no Position. Qualified executable TAKE creates the exact shadow Position only after the visible verdict.
- Never claim `logged` / `settled` without a successful write and exact verification.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots; contrary-draft Live ML additionally requires LRO.
- Same-map multiple TAKEs may occur only across different market families; maximum one TAKE per family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Every visible TAKE requires a complete mechanically valid **PRE_TAKE_CERT** under the frozen authority commit.
- Draft Interaction Matrix is mandatory before any model-certified draft edge or draft-derived fallback classification when exact draft is available.
- Underdog +kills requires complete DIM + draft-only UDKC + KPA/KMS + RLD + False-Stable checks + live preservation + **LAC** + UCS + exact signed-margin/NKB.
- Live evidence cannot create missing draft proof or upgrade a genuinely FRAGILE/ABSENT draft fallback.
- Duration Over requires complete **DOVC**; state descriptors or theoretical waveclear are not observed stall proof.
- Total Kills Under is never TAKE-eligible unless `FRP = PASS`; passive quiet alone is insufficient.
- Duration Under retains FCR.
- Live ML retains Lead Decomposition, CFC, Draft Prior State and LRO where applicable.
- No rescue, martingale, chasing, or stake escalation.
- These mechanism gates are not a blanket increase in conservatism. If all written gates pass, default posture remains TAKE.

Mandatory active procedures:
- `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
- `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
- `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`

---

# Session Authority Lock activation rule

A live slate runs against one frozen authority commit.

- Ordinary wins/losses do not silently mutate the active stack.
- Default-branch edits during an already locked slate are pending unless the user explicitly authorizes an immediate relock/new epoch.
- The user instruction **“Adjust accordingly”** on 2026-08-23 UTC+7 is explicit authorization for the DOVC/LAC amendment to enter the new 2026-08-23 authority epoch.
- Historical predictions/results/P&L are preserved; postgame review does not rewrite them.

---

# Retired newer analytical versions

Do **not** apply v0.3.59 or v0.3.60 as model layers merely because their version numbers are higher.

Later-version-only concepts remain inactive unless explicitly incorporated into canonical v0.3.58 authority. Historical positions and P/L keep their original labels.

---

# Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
3. current Session Authority Lock from `models/lol/session/CURRENT_SESSION_LOCK.md`; once active, use its frozen `authority_commit` for the remaining stack
4. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
5. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
6. v0.3.57 through v0.3.26 rule deltas
7. mandatory fallback-floor certification procedure, including active KPA/KMS + RLD amendments
8. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
9. `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
10. `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
11. `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
12. mandatory live verdict checklist + `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
13. `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`
14. retained pre-v0.3.59 reviews/procedures relevant to v0.3.58, plus explicit v0.3.58 amendment reviews including `models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`
15. item-verification suspension
16. v0.3.25 consolidated rules / probation / calibration handbook
17. live fast path and main betting procedure
18. connected-stack procedure and addenda
19. scoreboard protocol
20. shared stake policy
21. latest live handoff last, applying CURRENT_MODEL + frozen lock authority where conflicts exist

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

---

# Recording

- New positions are recorded as **LoL v0.3.58**.
- Every valid live verdict must be followed by Airtable snapshot write + verification.
- HOLD/PASS produce no position record; TAKE produces the exact shadow position after the verdict when executable.
- Missing logs may be repaired only from original evidence and original visible verdict.
- A visibly issued procedural-error TAKE remains historical and may be audit-labeled; do not rewrite it as a fictional pre-entry HOLD.
- Do not create or auto-promote a newer model from an individual outcome unless the user explicitly requests a model change.
