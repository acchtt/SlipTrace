# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**.
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md` plus all retained v0.3.58 in-place amendments and retained pre-v0.3.59 deltas listed below.
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`.
- Mandatory new-chat bootstrap: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
- Session-lock governance: `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`.
- **LoL v0.3.59 and v0.3.60 remain retired/discarded.** Their files are historical/audit artifacts only and must not be loaded, blended, or revived.

User instruction on 2026-08-16 UTC+7: **“Discard newer versions, update this version accordingly.”** v0.3.58 therefore remains the canonical model.

---

## Mandatory bootstrap / authority drift guard

Every new chat/session must:

1. fetch this `CURRENT_MODEL.md` first from the default branch;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch `models/lol/session/CURRENT_SESSION_LOCK.md` if it exists;
4. if that lock is `ACTIVE`, re-fetch this file and the analytical/procedural stack at the lock's frozen authority commit;
5. follow the exact required load order below;
6. load the latest applicable live handoff last.

Conversation memory, project context, prompts, prior assistant output, historical files and older handoffs never override this file or a valid active frozen lock.

If live evidence arrives before bootstrap is complete, visible verdict:

`MODEL NOT LOADED — HOLD`

If an ACTIVE lock cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

---

# Canonical v0.3.58 in-place amendments

## 1. Duration Over — Structure Substitution / real stall evidence

Retain the KRX vs BRO Game 2 correction and 2026-08-23 DOVC hardening:

- low kills, low tower count, 0-0 towers, close gold, neutral objectives and quiet elapsed time are neutral descriptors by default;
- distinguish `ABSENT CONVERSION` from observed `FAILED CONVERSION` / denial / reset;
- Duration Over needs two independent positive clock-consuming mechanisms, with at least one observed failed-conversion/equivalent mechanism;
- Structure Substitution and shortest plausible compulsory-fight/objective -> serial structures -> base -> Nexus cascade testing are mandatory;
- resolve full DOVC:
  `CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`.

Mandatory:
`models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`

## 2. Daily-audit gap fix

Retain:

- **FRP — Forward Regime Persistence** for every Total Kills Under;
- **FCR — Fast-Close Robustness** for every normal Duration Under;
- **Lead Decomposition + CFC — Compulsory Fight Control** for live Moneyline;
- **SMR — Same-Mechanism Re-certification** when a later same-series TAKE relies on a previously failed mechanism.

## 3. Underdog +kills fallback and anti-cascade stack

Retain the full draft/live hierarchy:

- KPA and KMS separately;
- complete draft-only UDKC;
- RLD, False-Stable Guard, DCR/FF and hard Draft-Collapse veto;
- mandatory DIM with exact roles and retained TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP controls;
- strict Draft Isolation when the exact draft is reconstructed after live start;
- UCS, SCNE and exact signed-margin/NKB arithmetic;
- LAC after draft-only STABLE proof;
- live evidence may preserve or downgrade draft proof, never manufacture missing draft proof.

A kill lead, one dragon, small gold lead, 0-0 towers, theoretical scaling/waveclear/peel, isolated lane economy, grubs, attractive price, or a displayed cushion cannot satisfy LAC by themselves.

Mandatory:
- `models/lol/procedures/LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
- `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`

## 4. Live Moneyline — Draft Prior Degradation / Live Regime Override

Draft is a prior for live ML, not a permanent veto. Retain DPS, current-state CFC, neutral-fight stress, Lead Decomposition and LRO.

Contrary CLEAR/STRONG draft ML requires three usable snapshots, at least two meaningful contact/objective cycles, regime persistence, multi-role leverage, `DPS=BROKEN`, `CFC_CURRENT=PASS`, next-cycle stress PASS and `DRP=PASS`.

LRO applies to ML only and cannot create/upgrade draft-only underdog +kills proof.

Mandatory:
`models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`

## 5. Professional-play Draft Reading Layer — PDRL

Professional / officially sanctioned semi-professional draft analysis requires **DIM + PDRL**.

Retain competition patch/format, side/selection rights, Fearless/restricted-pool state, lane priority, jungle-support coupling, tempo transitions, objective sequencing, player-specific professional fit, execution burden, WCSR, remaining-series pool pressure, same-series adaptation and pro adversarial pass.

Hard effects:

- Game 2+ Fearless/restricted-pool drafts may not be graded as isolated full-pool drafts;
- solo-queue win/pick rates and generic tier lists cannot upgrade a pro draft edge;
- champion reputation is not player proficiency;
- `more scaling`, `more engage`, `more tanks`, `three winning lanes`, `counterpick`, and `more meta champions` are forbidden standalone conclusions;
- keep `DIM_EDGE`, `PRO_MAP_EDGE`, `PRO_EXEC_EDGE`, `SERIES_DRAFT_EDGE`, and `FINAL_PRO_DRAFT_EDGE` conceptually distinct.

Mandatory:
`models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md`

## 6. Kill Handicap side-neutral margin engine — KHMC

Retain the distribution-first, side-neutral parent gate for both +kills and -kills:

1. define favorite independently of displayed H;
2. build one signed final kill-margin distribution before sign selection;
3. lock `KH_MARGIN_CERT` before displayed line/price is used as evidence;
4. price both executable sides from the same distribution;
5. run WMS so material serial-favorite cascades are represented;
6. select sign only after distribution/pricing are locked;
7. apply sign-specific mechanism stack only downstream;
8. selected-side lower-bound cover probability must clear break-even plus retained phase/uncertainty buffer;
9. NKB/RNE are arithmetic only;
10. failure of one sign is zero positive evidence for the other;
11. distinguish `NO_EXPANSION_OPPORTUNITY` from `EXPANSION_OPPORTUNITY_SUPPRESSED`;
12. `SIGN_SELECTED_AFTER_DIST = PASS` is mandatory.

`KH_DIRECTIONAL_CALIBRATION = ACTIVE` remains a process-neutrality control, not a favorite quota or sign inversion.

Mandatory:
- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`

## 7. 2026-08-25 afternoon professional-meta + KH asymmetry calibration — ACTIVE

User authorization at approximately 20:05 UTC+7 on 2026-08-25: **“Ok implement them now.”**

This explicitly authorizes a prospective canonical v0.3.58 in-place amendment after the KRX.C–BFX.Y slate closed. Historical predictions, positions and P/L are not rewritten.

### 7.1 Professional Meta Layer (PML)

For pro/semi-pro drafts, PDRL now additionally requires a dedicated Professional Meta Layer using professional-relevant evidence rather than solo-queue tiering.

Resolve where available:

- current pro pick/ban priority on the competition patch and relevant competition tier;
- blind-pick safety and punishability;
- credible role-flex value;
- pair/trio dependency, especially jungle/support, mid/jungle and bot/support;
- professional functional contribution: lane priority, first move, engage, disengage/reset, front line, waveclear, objective DPS, side pressure, pick threat, backline access, carry protection, terrain/choke control or siege;
- player-specific recent stage fit;
- pocket-pick execution/uncertainty tax;
- Fearless scarcity value.

High pro presence is not standalone proof of draft superiority; it may reflect flexibility, blind safety, draft compression, ban strategy or role scarcity.

For Fearless Game 2+, maintain **archetype inventory**, not champion count alone. Track at minimum reliable engage, disengage/reset, front line, lane-priority access, jungle/support coupling, mid/jungle first move, bot stability/carry protection, waveclear, objective DPS, side pressure, pick threat and backline access.

Preferred causal draft order:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST MOVE -> OBJECTIVE SEQUENCE -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> PRO ADVERSARIAL PASS`.

Mandatory:
- `models/lol/procedures/LOL_PRO_META_LAYER_2026-08-25.md`
- `models/lol/procedures/LOL_PRO_META_AND_HANDICAP_ASYMMETRY_CALIBRATION_2026-08-25.md`

### 7.2 Small Kill-Handicap asymmetry

The side-neutral KH distribution remains the parent gate. The new asymmetry is a downstream structural filter, not permission for sign-first analysis.

**Underdog +H:** classify `DOG_CUSHION_CLASS = INSUFFICIENT / THIN / MATERIAL / LARGE` from current state plus the locked one-fight/cascade tail.

- `INSUFFICIENT` => automatic SKIP.
- `THIN` => presumptive SKIP; it may pass only with explicit exceptional UCS + LAC + WMS proof that the normal one-fight/cleanup expansion tail is suppressed. Price alone cannot override.
- `MATERIAL/LARGE` => still must pass all retained underdog +kills gates.
- Do not hard-code a universal numerical cutoff; +1.5/+2.5/+3.5 will often be thin, but state/distribution determines classification.

**Favorite -H:** small absolute negative handicaps are not automatically defective. A small favorite -H may be an efficient expression of a certified favorite edge when the locked side-neutral distribution and favorite downstream validator support the margin.

Mandatory:
`models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`

### 7.3 Screenshot synchronization clarification

When the user explicitly confirms paired scoreboard/market screenshots represent the same live state, device/status-bar capture-time differences or capture order do not by themselves invalidate synchronization. Internal game-state contradictions still fail closed.

This does not waive the two-snapshot requirement for live ML/KH/TK.

### 7.4 Recent-series workload

Previous-day play, short turnaround, travel or long-series workload is `PRO_EXEC_CONTEXT`, not a standalone fade/TAKE signal. It may move execution burden only when tied to an observable mechanism such as preparation compression, roster/substitution constraint, repeated late-series degradation, or verified schedule stress.

Mandatory clarification:
`models/lol/procedures/LOL_SCREENSHOT_SYNC_AND_WORKLOAD_CONTEXT_2026-08-25.md`

### 7.5 Duration Over calibration

The KRX.C–BFX.Y Game 4 result is supporting evidence only. Early objectives without structures do not by themselves prove Over. Use existing DOVC: observed failed conversion/denial/reset and other positive clock-consuming mechanisms remain mandatory. Do not outcome-fit a new standalone heuristic.

Reference review:
`models/lol/reviews/KRXC_BFXY_2026-08-25_AFTERNOON_CALIBRATION_REVIEW.md`

### 7.6 PRE_TAKE mechanical wiring

All applicable TAKES must additionally satisfy:
`models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`.

For pro draft-derived candidates, PML/meta/archetype/player-fit/pocket-tax fields become mandatory where applicable. For underdog +kills, `DOG_CUSHION_CLASS` and one-fight/ML-likeness tests are mandatory. For synchronized screenshot evidence, record internal match or explicit user-confirmed same-state provenance. Generic workload narratives cannot move a TAKE without a mechanism.

---

# Active operational governance

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum accepted odds: **1.60**.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots; contrary-draft Live ML additionally requires LRO.
- Same-map maximum one TAKE per market family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Every visible TAKE requires complete PRE_TAKE_CERT + contradiction scan + mechanical validator under frozen authority.
- For KH, PRE_TAKE additionally requires KHMC/KH margin extension plus the afternoon cushion-asymmetry extension where applicable.
- DIM is mandatory before certified draft edges when exact draft is available.
- PDRL + PML are mandatory for professional / officially sanctioned semi-professional draft analysis under an authority commit containing this amendment.
- Duration Over requires complete DOVC.
- Total Kills Under requires `FRP = PASS`.
- Duration Under retains FCR.
- Live ML retains Lead Decomposition, CFC, DPS and LRO where applicable.
- No rescue, martingale, chasing, or stake escalation.
- Mechanism gates are not a blanket increase in conservatism: if all written gates and pricing buffers genuinely pass, default posture remains TAKE.

## Verdict / logging order

The active Session Authority Lock controls whether ordinary post-verdict Airtable logging or a user-approved map-end batching override is in force.

Never claim `logged` / `settled` without successful write and exact verification.

---

# Mandatory active procedures

- `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`
- `models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`
- `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
- `models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`
- `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
- `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` for pro / officially sanctioned semi-pro play
- `models/lol/procedures/LOL_PRO_META_LAYER_2026-08-25.md` for pro / officially sanctioned semi-pro play
- `models/lol/procedures/LOL_PRO_META_AND_HANDICAP_ASYMMETRY_CALIBRATION_2026-08-25.md`
- `models/lol/procedures/LOL_SCREENSHOT_SYNC_AND_WORKLOAD_CONTEXT_2026-08-25.md`
- `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
- `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
- `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
- `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`

---

# Session Authority Lock activation rule

A live slate runs against one frozen analytical authority commit.

- Ordinary wins/losses do not silently mutate a locked slate.
- Default-branch analytical edits during an ACTIVE lock remain pending until explicit relock/new epoch.
- Historical predictions/results/P&L are preserved under the authority that existed when issued.
- User authorization on 2026-08-25 at approximately 20:05 UTC+7 explicitly activates the afternoon PML / KH asymmetry / synchronization / workload calibration prospectively after the completed KRX.C–BFX.Y slate.
- The completed E13 KRX.C–BFX.Y lock must not be retroactively relocked onto this amendment.
- Future locks must freeze a commit that contains this amendment before these new controls may authorize a TAKE.

---

# Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`
3. `models/lol/session/CURRENT_SESSION_LOCK.md` if it exists; if ACTIVE, freeze to its authority commit
4. re-fetch `CURRENT_MODEL.md` at frozen authority commit when a lock is ACTIVE
5. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
6. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
7. retained v0.3.57 through v0.3.26 rule deltas, excluding retired v0.3.59/v0.3.60
8. fallback-floor certification including KPA/KMS + RLD
9. `models/lol/procedures/LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`
10. `models/lol/procedures/LOL_PRO_PLAY_DRAFT_READING_LAYER_2026-08-24.md` when pro/semi-pro
11. `models/lol/procedures/LOL_PRO_META_LAYER_2026-08-25.md` when pro/semi-pro
12. `models/lol/procedures/LOL_PRO_META_AND_HANDICAP_ASYMMETRY_CALIBRATION_2026-08-25.md`
13. `models/lol/procedures/LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`
14. `models/lol/procedures/LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`
15. `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
16. `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`
17. `models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`
18. `models/lol/procedures/LOL_LIVE_ML_DRAFT_PRIOR_DEGRADATION_AND_REGIME_OVERRIDE_2026-08-21.md`
19. `models/lol/procedures/LOL_SCREENSHOT_SYNC_AND_WORKLOAD_CONTEXT_2026-08-25.md`
20. `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`
21. `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`
22. `models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`
23. `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
24. `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`
25. retained reviews/procedures relevant to canonical v0.3.58, including the 2026-08-23 session review, 2026-08-25 KH directional review and 2026-08-25 KRXC-BFXY afternoon calibration review
26. item-verification suspension
27. v0.3.25 consolidated rules / probation / calibration handbook
28. live fast path and main betting procedure
29. connected-stack procedure and addenda
30. scoreboard protocol
31. shared stake policy
32. latest applicable live handoff last, with CURRENT_MODEL + frozen lock authority winning conflicts

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

---

# Recording

- New positions remain recorded as **LoL v0.3.58**.
- HOLD/PASS creates no Position.
- TAKE creates the exact shadow Position only after the visible verdict under active logging/batching governance.
- Missing logs may be repaired only from original evidence and original visible verdict.
- A visibly issued procedural-error TAKE remains historical and may be audit-labeled; never rewrite it into a fictional pre-entry HOLD.
- Do not create or auto-promote a newer model version from an individual outcome unless the user explicitly requests a version change.
