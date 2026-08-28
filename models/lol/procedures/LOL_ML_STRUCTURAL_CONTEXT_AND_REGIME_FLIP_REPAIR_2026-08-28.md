# LoL Live ML Structural Context & Regime-Flip Repair — 2026-08-28

**Status:** ACTIVE canonical v0.3.58 in-place amendment when incorporated by `models/lol/CURRENT_MODEL.md` and the active Session Authority Lock  
**Effective:** 2026-08-28 UTC+7  
**Scope:** Live Moneyline; supporting interpretation may inform other families but does not replace their own gates  
**Historical rewrite:** FORBIDDEN  
**User authorization:** “Adjust the model now” after EDG–NIP Game 1 review

## Purpose

Prevent raw tower/structure counts from being upgraded into false live-control evidence and prevent a previously rejected ML thesis from flipping to TAKE without explicit repair of the reason it was rejected.

This is a mechanism clarification, not a generic conservatism increase.

---

## 1. Towers are context by default

Raw tower count, tower differential, tower gold, first tower, or a sequence of uncontested towers is **descriptive context by default**.

A structural advantage may contribute positively to Live ML only when it demonstrably changes forward control.

Classify:

`TOWER_STATE_CLASS = CONTEXT_ONLY / CAUSAL_CONTROL / TERMINAL_CONTROL`

### CONTEXT_ONLY

The structure state mainly describes accumulated gold/map progress but does not materially improve the contemplated side's next-cycle control.

Examples include:

- tower lead obtained through cross-map trades while the opponent still owns the next compulsory objective setup;
- towers taken without meaningful vision-depth, wave-depth, rotation, or base-access consequences;
- a tower differential that does not change who can enter river first, threaten side pressure, force response, or dictate neutral setup;
- tower gold that duplicates the same resource evidence already captured in RL.

`CONTEXT_ONLY` cannot independently satisfy a positive ML evidence point.

### CAUSAL_CONTROL

The structure state creates a specific, forward-looking control advantage relevant to the next compulsory cycles.

At least one concrete mechanism must be identified and usable now:

- deeper safe vision/river entry;
- wave-depth or lane-assignment advantage that creates first move;
- side-lane pressure that forces a real response before the next objective;
- reduced opponent safe-farm/waveclear access;
- a rotation or tempo edge directly created by the missing structure;
- cross-map threat strong enough to alter the opponent's objective choice;
- reliable access to serial structures/base after the next won interaction.

### TERMINAL_CONTROL

The structure state has already created direct base/inhibitor/Nexus access or another clearly terminal conversion branch.

This remains subject to terminal-event sensitivity and price.

---

## 2. Structural Causality Map is mandatory for positive tower evidence

Before towers/structures may be counted as positive Live ML evidence, resolve:

`STRUCTURAL_CAUSALITY = STRUCTURE_CHANGE -> FORWARD_MAP_EFFECT -> NEXT_CYCLE_EFFECT -> COMPOSITION_EXPLOITABILITY`

All four links must be explicit.

If the chain cannot be stated, `TOWER_STATE_CLASS = CONTEXT_ONLY`.

Hard rules:

- raw tower differential is not `CFC_CURRENT`;
- tower gold is not independent from RL when it is already reflected in role/team economy;
- first tower or 3–1 towers cannot by themselves establish regime persistence;
- structures cannot repair a failed objective-control mechanism unless they actually change future objective setup;
- attractive ML price cannot upgrade `CONTEXT_ONLY` into causal evidence.

---

## 3. Objective-Schedule Offset

When the opponent owns a material objective-schedule advantage — especially 3 dragons / Soul point, Soul, Elder access, or a similarly compulsory neutral timer — a tower lead must be tested against that schedule.

Resolve:

`OBJECTIVE_SCHEDULE_OFFSET = PASS / FAIL / N-A`

`PASS` requires a specific reason the structural state changes the next compulsory objective branch, such as:

- first-move/wave control into the objective;
- vision-entry advantage produced by the structure state;
- credible cross-map structure/base threat that makes full contest costly;
- a side-lane assignment that forces a defender and changes numbers/timing;
- direct ability to trade the objective for equivalent or superior terminal progress.

A tower lead that merely coexists with the opponent's Soul-point control is `FAIL` for offset purposes.

`OBJECTIVE_SCHEDULE_OFFSET = FAIL` does not automatically mean the contemplated ML must lose, but the tower state cannot be used as the evidence that overturns the objective-control disadvantage.

---

## 4. Prior-PASS Cause Repair Gate

If the same ML side was previously adjudicated `PASS` in the map, record the decision-critical reason(s):

`PRIOR_PASS_CAUSE = <named mechanism failure(s)>`

A later TAKE on the same side requires:

`PASS_CAUSE_REPAIR = REPAIRED / SUPERSEDED / FAIL / N-A`

### REPAIRED

The exact reason for the prior PASS has materially changed through new live evidence.

Examples:

- failed objective setup becomes repeated first-move/objective control;
- an unusable carry becomes enabled by current items/role leverage and demonstrates access;
- the opponent's easier neutral-fight route is materially degraded by role/economy/position changes;
- a prior one-role lead becomes coherent multi-role control with current CFC confirmation.

### SUPERSEDED

A genuinely new causal win mechanism now dominates the next compulsory cycles even though the old mechanism itself was not repaired.

Must record:

`NEW_CAUSAL_THESIS | NEW_EVIDENCE | WHY_OLD_PASS_CAUSE_NO_LONGER_DOMINATES`

The new thesis must be decision-relevant now; it cannot be price, tower count, raw gold, raw kills, or generic scaling language.

### FAIL

The prior PASS cause is still active and no new causal thesis dominates it.

`PASS_CAUSE_REPAIR = FAIL` => same-side ML TAKE forbidden.

This is not a permanent veto. It only prevents a verdict flip without causal explanation.

---

## 5. Regime-Flip Delta

For a same-side verdict transition `PASS -> TAKE`, resolve:

`REGIME_FLIP_DELTA = PASS / FAIL`

`PASS` requires at least one new, causally material state change since the prior PASS that affects forward win probability independently of duplicate scoreboard descriptors.

Valid examples:

- repeated first-move or objective-entry control;
- material carry/facilitator timing change that alters CFC;
- multi-role leverage becoming active across a distinct cycle;
- structural state classified `CAUSAL_CONTROL` or `TERMINAL_CONTROL` with a complete Structural Causality Map;
- opponent's prior winning mechanism becoming unavailable or materially degraded.

Invalid by themselves:

- larger tower differential;
- larger team gold lead with same role distribution;
- market price movement;
- kill score change from one isolated event;
- an objective/tower sequence that does not change the next-cycle control map.

`REGIME_FLIP_DELTA = FAIL` => prior PASS remains PASS for that thesis.

---

## 6. Live ML integration

Add to every Live ML PRE_TAKE_CERT where structures or a prior same-side PASS are material:

`TOWER_STATE_CLASS | STRUCTURAL_CAUSALITY | OBJECTIVE_SCHEDULE_OFFSET | PRIOR_PASS_CAUSE | PASS_CAUSE_REPAIR | REGIME_FLIP_DELTA`

Rules:

- `TOWER_STATE_CLASS=CONTEXT_ONLY` may be recorded but cannot count as an independent positive ML evidence point.
- If tower/structure evidence is not material, `TOWER_STATE_CLASS=N-A` is allowed with reason.
- If no prior same-side PASS exists, `PRIOR_PASS_CAUSE=N-A`, `PASS_CAUSE_REPAIR=N-A`, `REGIME_FLIP_DELTA=N-A`.
- If a prior same-side PASS exists, `PASS_CAUSE_REPAIR` and `REGIME_FLIP_DELTA` are mandatory for a later TAKE.
- Existing Lead Decomposition, DPS, CFC_CURRENT, neutral-fight stress, LRO, SMR, price, opportunity-decay and all governance gates remain intact.

Compact signature:

`ML_STRUCT[TOWER=<CTX/CAUSAL/TERM/NA>;SC=<P/F/NA>;OSO=<P/F/NA>;PPC=<.../NA>;PCR=<R/S/F/NA>;RFD=<P/F/NA>]`

---

## 7. Reference calibration — EDG vs NIP Game 1, 2026-08-28

Contemporaneous sequence:

- 19:18: EDG 4–6 NIP, EDG 2–1 towers, NIP 3–0 dragons. EDG retained broad role economy, but their early-control mechanism had repeatedly failed to control objectives and NIP owned the easier Soul-point 5v5 route. Correct verdict: `PASS — EDG ML`.
- 22:47: EDG 5–7 NIP, EDG 3–1 towers, NIP still 3–0 dragons, EDG broad economy. A later analytical candidate was issued on EDG ML @2.021, largely because the tower/economy state was interpreted as a regime change.
- The quoted EDG ML was never user-confirmed, therefore no Position existed and no P/L is assigned.

Pre-entry diagnostic, independent of the eventual result:

- `PRIOR_PASS_CAUSE`: EDG failed objective-control route + NIP easier compulsory Soul-point 5v5.
- `TOWER_STATE_CLASS`: the 3–1 tower lead lacked demonstrated next-objective control; therefore it should have remained `CONTEXT_ONLY` absent a completed Structural Causality Map.
- `OBJECTIVE_SCHEDULE_OFFSET`: no demonstrated offset to NIP's 3-dragon/Soul-point schedule.
- `PASS_CAUSE_REPAIR`: failed; the exact reason for the 19:18 PASS was still active.
- `REGIME_FLIP_DELTA`: failed; tower count and economy did not demonstrate a repaired CFC/objective mechanism.

Therefore the correct 22:47 analytical verdict under this amendment is `PASS — EDG ML @2.021`.

The final NIP win is not used to prove the gate; it is historical outcome context only.

---

## 8. Anti-overfit guard

This amendment does **not** mean:

- towers never matter;
- objectives always outrank structures;
- a team on Soul point is automatically the ML side;
- a prior PASS can never become TAKE;
- role-weighted economy is downgraded;
- fewer bets are preferred.

It means structural evidence must earn causal weight, and a rejected thesis must show explicit causal repair before being promoted later in the same map.
