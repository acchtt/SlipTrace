# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**.
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md` plus all retained v0.3.58 in-place amendments and retained pre-v0.3.59 deltas listed below.
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`.
- Mandatory new-chat bootstrap: `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`.
- Session-lock governance: `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`.
- **LoL v0.3.59 and v0.3.60 remain retired/discarded.** Historical/audit only; never load or blend them into active authority.

User instruction on 2026-08-16 UTC+7: **“Discard newer versions, update this version accordingly.”** v0.3.58 therefore remains canonical.

---

## Mandatory bootstrap / authority drift guard

Every new chat/session must:

1. fetch this `CURRENT_MODEL.md` first from the default branch;
2. immediately load `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch `models/lol/session/CURRENT_SESSION_LOCK.md` if it exists;
4. if that lock is ACTIVE, re-fetch this file and the analytical/procedural stack at the lock's frozen authority commit;
5. follow the exact required load order below;
6. load the latest applicable live handoff last.

Conversation memory, project context, prompts, prior assistant output, historical files and old handoffs never override this file or a valid active frozen lock.

If live evidence arrives before bootstrap completes:

`MODEL NOT LOADED — HOLD`

If an ACTIVE lock cannot be matched:

`MODEL LOCK MISMATCH — HOLD`

---

# Canonical v0.3.58 in-place amendments

## 1. Duration Over — Structure Substitution / real stall evidence

Retain the KRX vs BRO correction and 2026-08-23 DOVC hardening:

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

Retain the complete draft/live hierarchy:

- KPA and KMS separately;
- complete draft-only UDKC;
- RLD, False-Stable Guard, DCR/FF and hard Draft-Collapse veto;
- mandatory DIM with retained TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP controls;
- strict Draft Isolation when exact draft is reconstructed after live start;
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

For a contemplated ML against an original CLEAR/STRONG draft edge, LRO remains mandatory and requires the retained 3SNAP / 2CYCLE / regime persistence / multi-role leverage / `DPS=BROKEN` / `CFC_CURRENT=PASS` / next-cycle stress / DRP stack.

LRO applies to ML only and cannot create or upgrade draft-only underdog +kills proof.

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

## 7. Professional Meta Layer + small-H asymmetry — ACTIVE

User authorization on 2026-08-25 retained prospectively.

### 7.1 Professional Meta Layer (PML)

For pro/semi-pro drafts, PDRL additionally requires PML using professional-relevant evidence rather than solo-queue tiering.

Resolve where available:

- current pro pick/ban priority on the relevant patch/tier;
- blind-pick safety and punishability;
- credible role-flex value;
- pair/trio dependency, especially jungle/support, mid/jungle and bot/support;
- professional functional contribution: lane priority, first move, engage, disengage/reset, front line, waveclear, objective DPS, side pressure, pick threat, backline access, carry protection, terrain/choke control or siege;
- player-specific recent stage fit;
- pocket-pick execution/uncertainty tax;
- Fearless scarcity value.

High pro presence is not standalone proof of draft superiority.

For Fearless Game 2+, maintain archetype inventory, not champion count alone. Track at minimum reliable engage, disengage/reset, front line, lane-priority access, jungle/support coupling, mid/jungle first move, bot stability/carry protection, waveclear, objective DPS, side pressure, pick threat and backline access.

Preferred causal order:

`LANE STATES -> JUNGLE/SUPPORT ACCESS -> FIRST MOVE -> OBJECTIVE SEQUENCE -> TRANSITION QUALITY -> 2/3-ITEM FIGHT SHAPE -> WCSR -> EXECUTION BURDEN -> SERIES-POOL PRESSURE -> PRO ADVERSARIAL PASS`.

Mandatory:
- `models/lol/procedures/LOL_PRO_META_LAYER_2026-08-25.md`
- `models/lol/procedures/LOL_PRO_META_AND_HANDICAP_ASYMMETRY_CALIBRATION_2026-08-25.md`

### 7.2 Small Kill-Handicap asymmetry

The side-neutral KH distribution remains the parent gate.

**Underdog +H:** classify `DOG_CUSHION_CLASS = INSUFFICIENT / THIN / MATERIAL / LARGE` from current state plus the locked one-fight/cascade tail.

- INSUFFICIENT => automatic SKIP.
- THIN => presumptive SKIP; only exceptional UCS + LAC + WMS proof may pass.
- MATERIAL/LARGE => all retained underdog +kills gates still apply.
- no universal numeric cutoff.

**Favorite -H:** a small negative handicap may be an efficient expression of a certified favorite edge when the locked side-neutral distribution and favorite validator support it.

Mandatory:
`models/lol/procedures/LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`

### 7.3 Screenshot synchronization clarification

When the user explicitly confirms paired scoreboard/market screenshots represent the same live state, device/status-bar capture-time differences or capture order do not invalidate synchronization by themselves. Internal game-state contradictions still fail closed.

### 7.4 Recent-series workload

Previous-day play, short turnaround, travel or long-series workload is `PRO_EXEC_CONTEXT`, not a standalone fade/TAKE signal. It may move execution burden only when tied to an observable mechanism.

Mandatory:
`models/lol/procedures/LOL_SCREENSHOT_SYNC_AND_WORKLOAD_CONTEXT_2026-08-25.md`

### 7.5 PRE_TAKE wiring

All applicable TAKES also satisfy:
`models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`.

## 8. Post NS–BFX market priority & execution calibration — ACTIVE

User authorization on 2026-08-27 after the completed NS–BFX series: **“Adjust the model accordingly.”**

This canonicalizes the mechanism-level lessons from the series without rewriting historical verdicts or P/L.

Mandatory:
`models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`

Reference review:
`models/lol/reviews/NS_BFX_2026-08-27_SERIES_CALIBRATION_REVIEW.md`

### 8.1 Market triage — ML first

At every meaningful synchronized live state, evaluate executable families in this order:

`ML -> Kill Handicap -> Total Kills -> Duration`

This is triage priority, not a quota or positive evidence for ML. Do not abandon a clean executable ML merely because a derivative market displays a larger price.

### 8.2 Ordinary live ML — two independent evidence points

For ML aligned with a CLEAR/STRONG draft edge, or where original draft edge is SLIGHT/EVEN/UNCLEAR, ordinary live ML may certify with two causally independent evidence points:

- certified exact-role draft mechanism + first meaningful synchronized live confirmation; or
- two distinct synchronized live states with meaningful transition.

No pregame/immediate-postdraft ML TAKE.

Against an original CLEAR/STRONG contrary draft edge, retained LRO 3SNAP/2CYCLE remains mandatory and is not weakened.

### 8.3 Role-weighted ML state

Raw kill score is descriptive, not dominant. Weight multi-role economy, carry/facilitator leverage, first move, current item/level timings, structure/objective conversion, and whether an advantaged role is the demonstrated conversion engine.

A single dragon/tower may reduce confidence but cannot automatically erase repeated mechanism realization.

### 8.4 HOLD expiry

HOLD expires on the next meaningful synchronized state, major objective/contact/conversion cycle, or material market reprice. Resolve to TAKE or PASS unless the candidate materially changes. Repetitive same-rationale HOLD is prohibited.

### 8.5 Opportunity decay

- approximately 8:00–20:00: preferred causal entry window;
- 20:00–24:00: normal gates + terminal-event scan;
- 24:00–27:00: +3pp late-entry buffer where probability pricing is used;
- >=27:00: new TK/Duration presumptive PASS unless exceptional/non-terminal; ML/KH require +5pp buffer and CLEAR non-fragile mechanism;
- settlement dominated by “one more fight” or “one clean end” must PASS.

Structural phase may override clock when the map is unusually accelerated/undeveloped.

### 8.6 Total Kills Over — stricter recurrence

Draft contact tools are contextual inventory only. No draft + single-live shortcut.

TK Over requires at least two distinct observed contact realizations/cycles, with the second demonstrating persistence or renewed compulsory contact rather than cleanup from the first event. Identify the next live contact source and terminal sensitivity.

Resolve:
`CONTACT_INVENTORY | CONTACT_REALIZATION_1 | CONTACT_REALIZATION_2 | RECURRENCE_PERSISTENCE | NEXT_CONTACT_SOURCE | TERMINAL_SENSITIVITY | PRICE`.

TK Under retains FRP.

### 8.7 KH speed calibration is NOT loosened

KH retains the side-neutral signed final-margin distribution, two usable live-state requirement, sign-after-distribution, WMS, cover-before-close, cushion/asymmetry, and all sign-specific downstream gates. Do not move from unresolved ML into KH simply because the displayed price is larger.

### 8.8 User line-existence confirmation gate

A visible `TAKE` is an analytical candidate until the user confirms the quoted market/line/odds still exist and are executable.

Required execution state:
`USER_LINE_CONFIRMATION = PENDING / CONFIRMED / FAILED`

- PENDING => no Position record, no W/L, no P/L.
- CONFIRMED => may become an accepted shadow Position under active logging/batching governance.
- FAILED => no Position exists.
- materially moved line/price must be reassessed before acceptance.
- unconfirmed TAKE may remain in Snapshot/audit evidence only.

This gate is prospective and must carry into successor LoL session locks unless explicitly revoked by the user.

---

# Active operational governance

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum accepted odds: **1.60**.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Market triage defaults to ML first.
- Ordinary live ML uses the two-independent-evidence path in section 8; contrary CLEAR/STRONG draft ML still requires full LRO.
- Live KH requires two usable synchronized live states plus the complete KHMC/downstream stack.
- TK Over requires two distinct observed contact realizations/cycles; TK Under retains FRP and existing live-state requirements.
- Same-map maximum one accepted TAKE per market family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Every visible TAKE candidate requires complete PRE_TAKE_CERT + contradiction scan + mechanical validator under frozen authority.
- For KH, PRE_TAKE additionally requires KHMC/KH margin extension plus cushion-asymmetry extension.
- DIM is mandatory before certified draft edges when exact draft is available.
- PDRL + PML are mandatory for pro / officially sanctioned semi-pro draft analysis.
- Duration Over requires complete DOVC.
- Total Kills Under requires `FRP = PASS`.
- Duration Under retains FCR.
- Live ML retains Lead Decomposition, CFC, DPS and LRO where applicable.
- Opportunity-decay / terminal-event sensitivity is mandatory.
- HOLD expiry is mandatory.
- No rescue, martingale, chasing, or stake escalation.
- Mechanism gates are not a blanket increase in conservatism: when written gates and pricing buffers genuinely pass, default posture remains TAKE candidate.

## Verdict / execution / logging order

1. visible analytical verdict first;
2. if `TAKE`, set `USER_LINE_CONFIRMATION=PENDING` and ask/await confirmation that the exact quoted market still exists;
3. only `CONFIRMED` creates an accepted Position;
4. log according to active lock batching/immediate governance;
5. exact-verify after write;
6. never claim logged/settled without successful write and verification.

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
- `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`
- `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`, subject to the newer user-confirmation gate above

---

# Session Authority Lock activation rule

A live slate runs against one frozen analytical authority commit.

- Ordinary wins/losses do not silently mutate a locked slate.
- Default-branch edits during an ACTIVE lock remain pending until explicit relock/new epoch unless the lock itself carries a user-authorized mutable execution rule.
- Historical predictions/results/P&L remain under the authority that existed when issued.
- Future locks must freeze a commit containing all amendments intended to authorize TAKES.

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
20. `models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`
21. `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`
22. `models/lol/procedures/LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`
23. `models/lol/procedures/LOL_PRE_TAKE_CERT_AFTERNOON_CALIBRATION_EXTENSION_2026-08-25.md`
24. `models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`
25. `models/lol/procedures/LOL_AIRTABLE_POST_VERDICT_LOGGING_INTEGRITY_2026-08-16.md`
26. retained reviews/procedures relevant to canonical v0.3.58, including the 2026-08-23 session review, 2026-08-25 KH directional review, 2026-08-25 KRXC-BFXY afternoon review, and `models/lol/reviews/NS_BFX_2026-08-27_SERIES_CALIBRATION_REVIEW.md`
27. item-verification suspension
28. v0.3.25 consolidated rules / probation / calibration handbook
29. live fast path and main betting procedure
30. connected-stack procedure and addenda
31. scoreboard protocol
32. shared stake policy
33. latest applicable live handoff last, with CURRENT_MODEL + frozen lock authority winning conflicts

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

---

# Recording

- New accepted positions remain recorded as **LoL v0.3.58**.
- HOLD/PASS creates no Position.
- A visible TAKE with `USER_LINE_CONFIRMATION=PENDING` creates no Position and no P/L.
- Only `USER_LINE_CONFIRMATION=CONFIRMED` permits Position creation.
- If quoted line/price materially changes, reassess before acceptance.
- Missing logs may be repaired only from original evidence, original visible verdict, and explicit execution confirmation where required.
- A visibly issued procedural-error TAKE remains historical and may be audit-labeled; never rewrite it into a fictional pre-entry HOLD.
- Do not create or auto-promote a newer model version from an individual outcome unless the user explicitly requests a version change.
