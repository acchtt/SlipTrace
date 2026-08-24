# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**.
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md` plus the in-place amendments and retained deltas listed below.
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`.
- Mandatory new-chat bootstrap: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
- Session-lock governance: `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`.
- **LoL v0.3.59 and v0.3.60 are retired/discarded from the active analytical hierarchy.** Their files may remain only as historical/audit artifacts. Do not load, blend, or auto-restore them.

User instruction on 2026-08-16 UTC+7: **“Discard newer versions, update this version accordingly.”**

The prior temporary v0.3.58 override is ended. v0.3.58 is the canonical model, not a temporary rollback.

---

## Mandatory session bootstrap / authority-drift guard

Every new chat/session must fetch this `CURRENT_MODEL.md` first, then immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`, then the current Session Authority Lock.

Conversation memory, project context, pasted prompts, older handoffs, historical model labels, and prior assistant output never override this file or an active frozen Session Authority Lock.

If live evidence arrives before bootstrap is complete, the only valid visible verdict is:

`MODEL NOT LOADED — HOLD`

If an active lock exists but its authority commit cannot be matched, use:

`MODEL LOCK MISMATCH — HOLD`

A model/version vocabulary mismatch is a hard tripwire. Retired versions may not be revived because they have higher version numbers.

---

# Canonical v0.3.58 in-place amendments

## 1. Duration Over — Structure Substitution / real stall evidence

Canonical v0.3.58 retains the KRX vs BRO Game 2 correction:

- low kills, low tower count, 0-0 towers, close gold, neutral objectives, and quiet elapsed time are neutral descriptors by default;
- conversion evidence must distinguish `ABSENT CONVERSION` from `FAILED CONVERSION` / equivalent repeated denial;
- only actual failed conversion or another observed clock-consuming defense/reset mechanism may satisfy the mandatory stall component;
- Structure Substitution is mandatory;
- Duration Over requires two independent positive clock-consuming mechanisms, with at least one observed failed-conversion / equivalent-denial mechanism;
- every Over must test the shortest plausible next compulsory fight/objective -> serial structures -> base -> Nexus cascade.

Mandatory / reference:
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
- `models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

## 2. Daily-audit gap fix

Canonical v0.3.58 includes:

- **FRP — Forward Regime Persistence** for every Total Kills Under;
- **FCR — Fast-Close Robustness** for every normal Duration Under;
- **Lead Decomposition + CFC — Compulsory Fight Control** for live Moneyline;
- **SMR — Same-Mechanism Re-certification** when a later same-series TAKE relies on a previously diagnosed failed mechanism.

Reference:
`models/lol/reviews/V0.3.58_CANONICAL_GAP_FIX_2026-08-16.md`

## 3. Underdog +kills — draft fallback and live anti-cascade stack

Canonical v0.3.58 requires:

- separate **KPA — Kill Production Ability** and **KMS — Kill-Margin Suppression**;
- complete draft-only **UDKC — Underdog +Kills Draft Certificate**;
- **RLD — Role-Leverage Decomposition**;
- False-Stable Guard and retained DCR/FF hard-veto controls;
- mandatory **DIM — Draft Interaction Matrix** including exact roles, TAM, OSG, DAU, SLI, FNF, CAS, ETS and AFP;
- `TAM = FAIL/UNRESOLVED` or `CAS = FAIL/UNRESOLVED` forbids `KMS = PASS` and UDKC `STABLE`;
- strict Draft Isolation when exact draft is reconstructed after live start;
- **UCS — Underdog Cushion Sufficiency**, SCNE and exact signed-margin/NKB arithmetic;
- **LAC — Live Anti-Cascade Confirmation** plus explicit live RLD / live preservation;
- live evidence may preserve or downgrade draft proof, never create missing draft proof or upgrade a genuinely FRAGILE/ABSENT fallback.

Mandatory procedures:
- `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
- `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`

## 4. Live Moneyline — Draft Prior Degradation & Live Regime Override

Draft remains a prior for Live ML, not a permanent veto.

Mandatory controls include `DPS — Draft Prior State`, current-state CFC, neutral-fight stress, Lead Decomposition and LRO when opposing an original CLEAR/STRONG draft prior.

A contrary-draft LRO requires three usable snapshots, at least two meaningful contact/objective cycles, regime persistence, multi-role leverage, `DPS=BROKEN`, `CFC_CURRENT=PASS`, next-cycle stress PASS and `DRP=PASS`.

LRO applies to ML only and cannot create or upgrade draft-only underdog +kills proof.

Mandatory procedure:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

## 5. 2026-08-23 execution hardening — DOVC + LAC

User instruction on 2026-08-23 UTC+7: **“Adjust accordingly.”**

This authorized an in-place v0.3.58 enforcement amendment and a new authority epoch.

### DOVC

Every Duration Over candidate must resolve:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`.

### LAC

Every underdog +kills candidate, after draft-only DIM + UDKC STABLE, must prove current-regime anti-cascade suppression. A kill lead, one dragon, small gold lead, 0-0 towers, a large cushion, theoretical scaling/waveclear/peel, isolated lane economy, grubs, or attractive price cannot satisfy LAC by themselves.

Mandatory procedure:
`models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`

Reference:
`models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`

## 6. 2026-08-24 professional-play draft reading layer — PDRL

User instruction on 2026-08-24 UTC+7: **“We have to improve our draft reading, especially for proplays only.”**

Professional / officially sanctioned semi-professional draft analysis additionally requires **PDRL** on top of DIM.

PDRL covers competition patch/format, side/selection rights, Fearless/restricted-pool state, lane priority, jungle-support coupling, tempo transitions, projected objective sequencing, player-specific professional fit, execution burden, win-condition state robustness, remaining-series pool pressure, same-series adaptation and a pro adversarial pass.

Hard effects include:

- Game 2+ restricted-pool/Fearless drafts may not be graded as isolated full-pool drafts;
- solo-queue win/pick rates and generic tier lists cannot upgrade a pro draft edge;
- champion reputation is not player proficiency;
- `more scaling`, `more engage`, `more tanks`, `three winning lanes`, and `counterpick` are forbidden standalone pro draft conclusions;
- `DIM_EDGE`, `PRO_MAP_EDGE`, `PRO_EXEC_EDGE`, `SERIES_DRAFT_EDGE`, and `FINAL_PRO_DRAFT_EDGE` remain conceptually separate.

Mandatory procedure:
`models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md`

## 7. 2026-08-25 Kill Handicap side-neutral margin engine — KHMC

User instruction on 2026-08-25 UTC+7: **“Lock this slate. And adjust the model with your recommendations.”**

Canonical v0.3.58 therefore restores the retained v0.3.44 **distribution-first, side-neutral Kill Handicap hierarchy** as the parent gate for both positive and negative handicaps.

The model must:

1. define the favorite independently of the displayed handicap;
2. construct one side-neutral signed final kill-margin distribution before selecting a sign;
3. lock `KH_MARGIN_CERT` before using the displayed line as evidence;
4. price both executable sides from the exact same distribution when both are available;
5. run **WMS — Wide-Margin Stress** so a materially probable serial favorite cascade is represented in the margin distribution;
6. select the preliminary sign only after the distribution and pricing are locked;
7. apply the existing underdog or favorite mechanism stack only as a downstream validator of that selected tail;
8. require the selected side's lower-bound cover probability to clear break-even plus the retained active phase/uncertainty buffer;
9. treat NKB/RNE as arithmetic only, never probability evidence;
10. treat `FAVORITE -H FAIL` as zero positive evidence for `UNDERDOG +H`, and vice versa;
11. distinguish `NO_EXPANSION_OPPORTUNITY` from `EXPANSION_OPPORTUNITY_SUPPRESSED` before allowing flat-margin history to support LAC;
12. prove `SIGN_SELECTED_AFTER_DIST = PASS` before any Kill Handicap TAKE.

Canonical ledger review found approximately 97% of settled KH selections on the positive side with negative positive-handicap performance. Therefore:

`KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

This is a process-neutrality control, not a favorite quota and not a sign inversion.

Mandatory procedures:
- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

Reference review:
`models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_AND_MARGIN_ENGINE_REVIEW_2026-08-25.md`

---

# Active operational governance

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum accepted odds: **1.60**.
- Every new chat/session must complete bootstrap and inherit the active frozen Session Authority Lock.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots; contrary-draft Live ML additionally requires LRO.
- Same-map multiple TAKEs may occur only across different market families; maximum one TAKE per family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Every visible TAKE requires a complete mechanically valid **PRE_TAKE_CERT** under the frozen authority commit.
- For Kill Handicap, PRE_TAKE_CERT additionally requires the complete side-neutral KH parent manifest from the 2026-08-25 margin-engine amendment.
- Draft Interaction Matrix is mandatory before any model-certified draft edge or draft-derived fallback classification when exact draft is available.
- PDRL is mandatory for professional / officially sanctioned semi-professional draft analysis when included by the active lock.
- Duration Over requires complete DOVC.
- Total Kills Under requires `FRP = PASS`.
- Duration Under retains FCR.
- Live ML retains Lead Decomposition, CFC, DPS and LRO where applicable.
- No rescue, martingale, chasing, or stake escalation.
- Mechanism gates are not a blanket increase in conservatism. If all written gates and pricing buffers genuinely pass, default posture remains TAKE.

## Verdict / logging order

The active Session Authority Lock controls whether normal post-verdict Airtable logging or a user-approved map-end batching override is in force.

Never claim `logged` / `settled` without a successful write and exact verification under the applicable lock/procedure.

---

# Mandatory active procedures

- `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`
- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` for pro / officially sanctioned semi-pro draft analysis
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
- `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
- `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
- `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`

---

# Session Authority Lock activation rule

A live slate runs against one frozen authority commit.

- Ordinary wins/losses do not silently mutate the active stack.
- Default-branch edits during an already locked slate remain pending unless the user explicitly authorizes a relock/new authority epoch.
- User authorization on 2026-08-23 activated the DOVC/LAC epoch.
- User authorization on 2026-08-24 activated the PDRL epoch for the current NAVI–FNC series through lock E10.
- User authorization on 2026-08-25 — **“Lock this slate. And adjust the model with your recommendations.”** — explicitly authorizes a new authority epoch for the current slate containing the Kill Handicap side-neutral margin engine and its PRE_TAKE mechanical extension.
- Historical predictions/results/P&L are preserved; postgame review does not rewrite them.

---

# Retired newer analytical versions

Do **not** apply v0.3.59 or v0.3.60 as model layers merely because their version numbers are higher.

Later-version-only concepts remain inactive unless explicitly incorporated into canonical v0.3.58 authority. Historical positions and P/L keep their original labels.

---

# Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
3. current Session Authority Lock from `models/lol/session/CURRENT_SESSION_LOCK.md`; once active, use its frozen `authority_commit` for the remaining analytical/procedural stack
4. re-fetch this `CURRENT_MODEL.md` at the frozen authority commit
5. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
6. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
7. v0.3.57 through v0.3.26 retained rule deltas, excluding retired v0.3.59/v0.3.60
8. mandatory fallback-floor certification procedure, including KPA/KMS + RLD
9. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
10. `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` when professional / officially sanctioned semi-professional
11. `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
12. `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
13. `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
14. `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
15. `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
16. `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`
17. `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`
18. `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
19. `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`
20. retained pre-v0.3.59 reviews/procedures relevant to canonical v0.3.58, including the 2026-08-23 session review and 2026-08-25 KH directional review
21. item-verification suspension
22. v0.3.25 consolidated rules / probation / calibration handbook
23. live fast path and main betting procedure
24. connected-stack procedure and addenda
25. scoreboard protocol
26. shared stake policy
27. latest applicable live handoff last, applying CURRENT_MODEL + frozen lock authority where conflicts exist

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

---

# Recording

- New positions are recorded as **LoL v0.3.58**.
- HOLD/PASS produces no Position.
- TAKE produces the exact shadow Position only after the visible verdict and under the currently active logging/batching governance.
- Missing logs may be repaired only from original evidence and original visible verdict.
- A visibly issued procedural-error TAKE remains historical and may be audit-labeled; do not rewrite it as a fictional pre-entry HOLD.
- Do not create or auto-promote a newer model from an individual outcome unless the user explicitly requests a model change.
