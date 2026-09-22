# Football A — Practical Ceiling Ranking Patch

**Status:** ACTIVE OFFICIAL PATCH  
**Model:** Football A  
**Effective:** 2026-09-22 12:38 ICT onward  
**Basis:** settled rank-separation audit plus actual sportsbook-ledger audit, 2026-09-14 through 2026-09-22 ICT  
**Purpose:** correct repeated PRE ranking inversion where ordinary two-route A2 fixtures outrank lower-grade carrier-led fixtures with a stronger practical path to 3+ total goals.

This patch is prospective. It does not rewrite frozen PRE grades, historical ranks, historical verdicts, settled P/L, or prior shadow/counterfactual outcomes.

---

## 1. Core ranking invariant

`RANK THE MOST RELIABLE PRACTICAL PATH TO THE SUPPORTED TOTAL, NOT THE NUMBER OF NOMINAL SCORING ROUTES.`

Route symmetry remains useful evidence, but it is no longer a primary ranking privilege.

A fixture with two merely usable routes must not automatically rank above a carrier-led fixture when the carrier can credibly self-fund 3+ goals and the opponent's defensive failure/leakage makes that path repeatable.

This is a **ranking patch**, not an odds patch.

- current price does not create or improve Structural Rank;
- a lower bookmaker line does not improve Structural Rank;
- a higher bookmaker line does not improve Structural Rank;
- market data may trigger a separate re-screen under the active market-alignment patch, but it does not become a PRE ranking input.

---

## 2. Structural grades remain intact

This patch does **not** abolish A1 / A2 / B+ / B-PASS grades.

Keep the existing structural definitions and route states:

- A1 remains the maximum structural grade;
- A2 remains the normal grade for qualified PROVEN+SUPPORTED / strong SUPPORTED+SUPPORTED structures;
- B+ remains the normal grade for qualified PROVEN+NOMINAL / SUPPORTED+NOMINAL structures;
- B/PASS remains outside the ranked exposure board unless a fresh structural re-screen legitimately changes the grade.

However:

**Structural grade is no longer a monotonic proxy for Structural Rank.**

A B+ WATCHLIST fixture may rank above an A2 FOCUS fixture when the B+ owns the stronger practical 3+ path.

The structural grade/tier must remain visible so the reason for the cross-grade rank is auditable.

---

## 3. New PRE Structural Rank order

After scope, route proof, failure-mode analysis, supported burden, and strong-negative-veto review, rank fixtures in this order:

1. **PRACTICAL SELF-FUNDED 3+ CEILING**
2. **OPPONENT DEFENSIVE FAILURE / LEAKAGE COMPATIBILITY**
3. **CURRENT CHANCE QUALITY + SCORING URGENCY / REPEATABILITY**
4. **FAILURE-MODE RESISTANCE AT THE SUPPORTED BURDEN**
5. **SECONDARY-ROUTE QUALITY**
6. **ROUTE SYMMETRY / STRUCTURAL GRADE AS A TIE-BREAKER**
7. **SUPPORTED BURDEN FIT**
8. **EVIDENCE CONFIDENCE**

Price is never part of this PRE ranking sequence.

### 3.1 Practical self-funded 3+ ceiling

Give first-order rank credit when one team has a credible independent route to three team goals even if the opponent contributes zero.

Use the existing TRUE CC+ / carrier-ceiling evidence standard where available. In data-poor leagues, a strong substitute may be used only when the evidence is current, repeatable, and mechanism-compatible.

Do not award this flag from one isolated 3+ scoreline.

### 3.1.1 VERIFIED carrier hardener — mandatory

The structural label `CARRIER-LED` by itself receives **no first-order ranking boost**.

Classify every proposed carrier-priority case as exactly one of:

- `PRACTICAL CARRIER CEILING — VERIFIED`
- `PRACTICAL CARRIER CEILING — CANDIDATE`
- `PRACTICAL CARRIER CEILING — UNVERIFIED`

Only **VERIFIED** may receive the first-order self-funded-ceiling rank credit or trigger a cross-grade B+ > A2 inversion.

To mark **VERIFIED**, the evidence must show that the carrier can plausibly fund three team goals **without needing the secondary route**, using a current and repeatable football mechanism. Require the strongest available combination of:

1. **repeatability** — more than one recent demonstration of 3+ team-goal capacity, or one such demonstration plus strong repeated underlying chance creation;
2. **mechanism proof** — chance quality, box access, transition volume, set-piece pressure, territory/second phases, shot quality, or an equivalent route signal consistent with the goals;
3. **independence** — the 3+ path does not depend on the nominal/weak opponent route scoring first or creating an abnormal game state;
4. **opponent compatibility** — the opponent repeatedly permits the same mechanism or has a current defensive failure that materially supports it;
5. **current integrity** — no XI/rotation/tactical change materially damages the carrier mechanism.

In data-poor leagues, score-form substitutes may be used only when the sample is recent, repeated, and reinforced by class-gap, lineup, opponent-leakage, or tactical evidence. A single scoreline, favorite status, market line, or generic goals-against statistic is insufficient.

`CANDIDATE` may improve evidence confidence or monitoring priority but **must not** leapfrog a stronger A2 solely because it is carrier-led.

`UNVERIFIED` receives no carrier-ceiling priority and is ranked on the remaining factors normally.

Persist when applicable:

`PRACTICAL CARRIER CEILING — VERIFIED`

### 3.2 Opponent defensive failure / leakage

A carrier ceiling is materially stronger when the opponent repeatedly permits the exact mechanism the carrier uses:

- central/box access;
- transition exposure;
- repeated high-value chances;
- sustained territory and second-phase pressure;
- set-piece vulnerability;
- repeated multi-goal concessions through the same mechanism;
- inability to slow the match after conceding.

Generic goals-against alone are supporting evidence, not sufficient proof.

Persist when applicable:

`OPPONENT FAILURE COMPATIBLE — YES`

### 3.3 Chance quality and urgency

Prefer routes that repeatedly generate real scoring pressure over routes inferred mainly from final scores.

Where live/current-state evidence is relevant after PRE freeze, it may validate or damage the route under existing rules; it does not retroactively rewrite PRE rank.

---

## 4. Cross-grade ranking authority

The following cross-grade inversion is now explicitly allowed:

`B+ CARRIER-LED / PROVEN+NOMINAL + VERIFIED SELF-FUNDED 3+ CEILING + COMPATIBLE OPPONENT FAILURE`

may rank above:

`ordinary A2 TWO-SIDED / SUPPORTED+SUPPORTED`

when the A2's advantage is mainly route symmetry and neither route has comparable independent ceiling or failure resistance.

Therefore:

- A2 FOCUS does **not** automatically outrank B+ WATCHLIST;
- two usable routes do **not** automatically outrank one dominant, repeatable route;
- a nominal second route does not materially lower rank when the carrier can independently fund the supported total;
- a weak second route still matters for burden, upper-tail, and execution, but it no longer mechanically buries the fixture in PRE ranking.

### 4.1 A1 treatment

A1 remains the maximum structural class, but A1 is not immune to ranking penalties from:

- strong current suppression;
- mechanism-compatible same-venue H2H suppression;
- chance-quality deterioration;
- realistic control/slowdown failure branches;
- unsupported high burden.

A clean elite A1 normally remains near the top, but the label alone does not guarantee rank #1.

### 4.2 B/PASS treatment

This patch does not promote B/PASS directly into the ranked board.

A PASS can only enter the ranked board after a legitimate fresh structural re-screen under existing rules.

Recent false-negative PASS outcomes are audit evidence, not automatic promotion authority.

---

## 5. Strong negative veto remains authoritative

Practical ceiling cannot override a strong, current, mechanism-compatible veto.

Examples include:

- repeated recent same-venue suppression matching the current control mechanism;
- meaningful XI damage to the carrier route;
- strong current low-urgency/control profile;
- fatigue/rotation that materially lowers the carrier ceiling;
- carrier scoring evidence that is scoreline-only and not supported by route/chance evidence.

A B+ with a strong negative veto must not receive carrier-priority rank merely because it has historical 3+ results.

This preserves the active lesson from the Sep 19–22 suppression audits: suppression is strongest when it is recent, relevant, and mechanism-compatible.

---

## 6. Ranking labels and persistence

For every ranked fixture, preserve the existing:

- Structural Grade;
- Board Tier;
- Structural Type;
- Supported Burden;
- Structural Rank.

Add one of these ranking interpretations in the evidence summary when material:

- `PRACTICAL CEILING PRIORITY — VERIFIED CARRIER`
- `PRACTICAL CEILING PRIORITY — ELITE TWO-SIDED`
- `ORDINARY TWO-SIDED — NO INDEPENDENT 3+ CEILING`
- `RANK CAPPED — STRONG NEGATIVE VETO`

When a B+ outranks an A2, explicitly state why:

`CROSS-GRADE RANK — B+ ABOVE A2 DUE TO STRONGER PRACTICAL 3+ PATH`

Do not change the B+ grade to A2 merely to make the ordering look conventional.

---

## 7. XI and market interaction

PRE Structural Rank is frozen before current odds.

Confirmed XI may rerank only when it materially changes football structure:

- route removed/damaged;
- role/shape change;
- carrier ceiling materially strengthened or weakened;
- opponent resistance materially strengthened or weakened.

Price or line movement alone cannot rerank.

The active market-alignment, decay-first, B+ protected-line, HMA, and exposure rules still govern **execution after ranking**.

---

## 8. Execution remains separate

This patch changes **which matches rank higher**, not which lines are automatically bet.

A high-ranked B+ still uses:

`MODEL_RULES_FOOTBALL_A_BPLUS_PROTECTED_LINE.md`

A high-ranked A2 still uses the active A2 upper-tail, burden, market-alignment, and decay-first rules.

Structural Rank and Exposure Decision remain separate outputs.

---

## 9. Audit requirement

Post-slate audits must now compare:

- A1 FOCUS;
- A2 FOCUS;
- A2 WATCHLIST;
- B+ WATCHLIST;
- B+ with `PRACTICAL CARRIER CEILING — VERIFIED`;
- ordinary A2 TWO-SIDED without independent 3+ ceiling;
- strong-negative-veto subsets;
- B/PASS false negatives separately.

The key diagnostic is whether rank order becomes more monotonic with **supported-burden goal performance**, not whether every carrier-led fixture wins.

Review carrier-priority cases separately from execution price/P&L so ranking and execution errors are not conflated.

---

## 10. Authority

This patch is the final Football A authority on **PRE Structural Rank ordering** where older rules give automatic or near-automatic priority to route symmetry, A2 FOCUS status, or structural grade label.

It overrides conflicting ranking language in:

- `MODEL_RULES_FOOTBALL_V0.2.49.md`;
- `MODEL_RULES_FOOTBALL_V0.2.52.md`;
- `MODEL_RULES_FOOTBALL_V0.2.53.md`;
- `MODEL_RULES_FOOTBALL_V0.2.54.md`;
- `MODEL_RULES_FOOTBALL_A.md`;
- `CURRENT_MODEL.md`.

It does not override fixture scope, route-proof definitions, supported-burden construction, strong-negative-veto rules, B+ protected-line execution, market-alignment, decay-first execution, or official settlement rules.
