# Football A — B/PASS Practical-Ceiling Rescue Patch

**Status:** ACTIVE OFFICIAL PATCH  
**Model:** Football A  
**Effective:** 2026-09-22 19:00 ICT onward  
**Basis:** trailing-7-day B/PASS outcome audit through 2026-09-22 ICT  
**Purpose:** reduce false-negative B/PASS classifications caused by discarding a fixture too early when one route can still self-fund the supported total.

This patch is prospective only. It does not rewrite historical PRE grades, historical ranks, verdicts, exposures, or P/L.

---

## 1. Audit lesson

The trailing-7-day audit found a high raw 3+ incidence among frozen B/PASS fixtures, while several strong current suppression calls still behaved as intended.

Therefore the error is **not** that PASS should disappear.

The error is that Football A sometimes sends a fixture directly to PASS because:

- the second route is NOMINAL / FAILED;
- route symmetry is weak;
- recent scoring is uneven;
- or a generic control/compression concern exists,

without first asking whether one side owns a **verified practical self-funded 3+ path** against a compatible opponent failure.

Core invariant:

`DO NOT FINALIZE PASS SOLELY BECAUSE THE SECOND ROUTE IS WEAK WHEN A VERIFIED CARRIER CAN INDEPENDENTLY FUND THE TOTAL.`

---

## 2. Mandatory PASS Rescue Screen

Before freezing `B / PASS`, run a PASS Rescue Screen whenever **any** of the following is true:

1. at least one route is `PROVEN` or `SUPPORTED`;
2. one side is a plausible carrier / class-gap scorer;
3. the opponent shows repeated defensive leakage compatible with that carrier;
4. the market is not being used, but structural evidence suggests a possible independent 3+ team-goal path;
5. the only reason for PASS would otherwise be weak secondary-route quality or missing route symmetry.

The screen is price-blind at PRE.

Evaluate:

- carrier state: `VERIFIED`, `CANDIDATE`, or `UNVERIFIED`;
- opponent-failure compatibility;
- current chance quality / scoring urgency;
- whether the carrier route survives likely game control;
- whether the failure mode is a real current mechanism or only a generic possibility;
- whether any strong negative veto exists.

Use the carrier definitions in:

`MODEL_RULES_FOOTBALL_A_PRACTICAL_CEILING_RANKING.md`

---

## 3. Rescue outcomes

### 3.1 PASS RESCUE — B+ WATCHLIST

Promote the fixture from provisional PASS to:

`B+ WATCHLIST / CARRIER-LED`

only when all are true:

1. at least one route is PROVEN or SUPPORTED;
2. `PRACTICAL CARRIER CEILING — VERIFIED` clears;
3. the opponent failure is mechanism-compatible, or the carrier's own chance-quality evidence is strong enough to make the 3+ path independent of opponent contribution;
4. no strong current mechanism-compatible negative veto is present;
5. the supported burden can be constructed under existing burden rules.

Persist:

`PASS RESCUE — B+ WATCHLIST — VERIFIED CARRIER`

This is a structural rescue only. It does not create automatic exposure.

The rescued fixture then uses normal B+ execution authority, including the exact-supported protected-line rule.

### 3.2 PASS — CARRIER CANDIDATE / RE-SCREEN ELIGIBLE

If the carrier is only `CANDIDATE` rather than VERIFIED:

- keep `B / PASS`;
- do not rank it on the exposure board;
- persist `PASS — CARRIER CANDIDATE / RE-SCREEN ELIGIBLE`.

A later confirmed XI, material role change, or mandatory high-market conflict re-screen may create a fresh structural epoch. If that fresh football evidence upgrades the carrier to VERIFIED and no veto remains, promotion to B+ is allowed prospectively.

Price alone still cannot create the rescue.

### 3.3 PASS — STRONG SUPPRESSION VETO

Keep PASS when there is a strong current, mechanism-compatible suppression veto, including:

- recent same-venue / matchup suppression that matches the current tactical mechanism;
- repeated control/low-urgency behavior from the likely carrier;
- meaningful carrier XI damage;
- fatigue/rotation that removes the self-funded ceiling;
- current chance-quality collapse;
- structural evidence showing the nominal carrier repeatedly stalls at 1-2 goals against this opponent type.

Persist:

`PASS — STRONG SUPPRESSION VETO`

Historical H2H alone is not enough unless it is recent/relevant and mechanism-compatible.

### 3.4 PASS — NO PRACTICAL CEILING

Keep PASS when:

- neither route reaches SUPPORTED;
- no VERIFIED carrier exists;
- opponent leakage is generic rather than mechanism-compatible;
- chance quality / repeatability is weak;
- or supported burden cannot be constructed.

Persist:

`PASS — NO PRACTICAL 3+ CEILING`

---

## 4. Burden discipline after rescue

A PASS rescue does not justify aggressive burden.

- Construct supported burden using the existing structural burden rules.
- Rescue status by itself never authorizes O3.0+.
- As a default safety cap, a newly rescued B+ should not exceed O2.5 unless the existing model independently proves a higher burden.
- Exact supported B+ execution uses the active B+ Protected-Line patch.
- +0.25 requires `PRACTICAL CARRIER CEILING — VERIFIED` and the active B+ carrier-extension conditions.
- +0.50 or more remains non-automatic.

---

## 5. Ranking treatment

A rescued B+ enters the ranked FOCUS/WATCHLIST board at its true practical rank.

Do not place it automatically at the bottom merely because it originated from a PASS screen.

Apply the active Practical Ceiling Ranking order:

`VERIFIED SELF-FUNDED 3+ CEILING > OPPONENT FAILURE COMPATIBILITY > CHANCE QUALITY / URGENCY > FAILURE RESISTANCE > SECONDARY ROUTE > ROUTE SYMMETRY / GRADE`

A rescued B+ may outrank an ordinary A2 when the practical 3+ path is stronger.

Preserve the B+ grade; do not promote it to A2 merely to justify rank.

---

## 6. Audit requirements

Track separately:

- ordinary B/PASS;
- `PASS — STRONG SUPPRESSION VETO`;
- `PASS — CARRIER CANDIDATE / RE-SCREEN ELIGIBLE`;
- `PASS — NO PRACTICAL 3+ CEILING`;
- `PASS RESCUE — B+ WATCHLIST — VERIFIED CARRIER`.

For rescued B+ fixtures, audit:

- supported-burden result;
- actual execution availability;
- exact-line / +0.25 / above-burden path;
- whether the carrier self-funded 3+;
- whether opponent leakage matched the predicted mechanism.

Do not treat every high-scoring historical PASS as evidence that it should have been rescued.

---

## 7. Authority

This patch is the final Football A authority on whether a provisional B/PASS fixture must receive a practical-ceiling rescue screen before being frozen as PASS.

It does not override:

- scope and league admission;
- route-proof definitions;
- carrier-verification requirements;
- strong negative vetoes;
- supported-burden construction;
- B+ Protected-Line execution;
- decay-first execution;
- market-alignment rules;
- settlement rules.
