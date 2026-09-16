# Football A — High-Market Acceptance Execution Patch

**Status:** ACTIVE OFFICIAL PATCH — FOOTBALL A ONLY  
**Model:** Football A  
**Effective:** 2026-09-16 ICT onward  
**Purpose:** fix the repeated 2–3 day execution failure where structurally strong A1/A2 FOCUS matches are stranded because Football A waits for a lower total that often never appears before scoring begins.

This patch is prospective. It does not alter Model B, rewrite historical frozen PRE states, create retroactive Website Picks, or backfill P/L.

---

## 1. Problem being corrected

Football A has repeatedly identified high-goal environments correctly while failing to participate because the market sits above the independently supported structural ceiling and the model waits for a lower line.

In the strongest matches, that lower line may never appear in a clean state because an early goal arrives first. The result is an execution-layer opportunity-cost problem rather than a broad structural-ranking failure.

This patch does **not** raise the structural ceiling itself. The frozen supported burden remains the football anchor. It creates a separate execution allowance for a narrowly defined high-market state.

`STRUCTURAL CEILING != MAXIMUM EXECUTABLE HIGH-MARKET LINE`

---

## 2. New official lane: HIGH-MARKET ACCEPTANCE (HMA)

A current line above the frozen supported ceiling may become official only when the match is already a strong Football A FOCUS candidate and the excess burden is inside the class-specific acceptance band below.

### 2.1 A1 FOCUS

A clean-XI `A1 FOCUS` may accept:

- up to **+0.25** above the frozen supported ceiling under normal A1 integrity; and
- up to **+0.50** above the frozen supported ceiling only when a strong upper-tail hardener is present.

For the +0.50 band, at least one must clear:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance; or
- `TRUE CC+` / equivalent independent carrier support strong enough to survive one route under-contributing.

### 2.2 A2 FOCUS

A clean-XI `A2 FOCUS` may accept:

- up to **+0.25** above the frozen supported ceiling when the Football A A2 upper-tail gate clears at the actual offered burden.

The A2 +0.25 pass still requires at least one of:

- `4+ TOTAL PATH — QUALITY PROVEN`;
- `TRUE CC+ PATH` with credible support for the additional goal(s); or
- `ELITE TWO-SIDED PATH` with strong chance quality and failure resistance.

### 2.3 A2 FOCUS with exceptional upper-tail proof

An `A2 FOCUS` may accept up to **+0.50** above the frozen supported ceiling only when the case is materially stronger than ordinary A2 and at least one exceptional hardener clears:

- `TRUE CC+` with repeatable independent 3+ team-goal capacity **and** credible 4+ match support;
- `4+ TOTAL PATH — STRONG / REPEATABLE`; or
- a clearly documented `ELITE TWO-SIDED` environment with strong chance quality on both routes and high failure resistance.

Ordinary `PROVEN + SUPPORTED` form evidence is not enough for +0.50.

### 2.4 No automatic extension below FOCUS

The HMA lane is **not available** to:

- `A2 WATCHLIST`;
- `B+ WATCHLIST`;
- `B / PASS`;
- fragile/unresolved structures;
- `A2 FOCUS CAP — FRAGILE SUPPORTED ROUTE` cases that remain WATCHLIST after the cap.

A lower-ranked or weaker match does not gain HMA merely because the market line is convenient.

### 2.5 +0.75 or more remains outside HMA

If the current total is **+0.75 or more above the frozen supported ceiling**, there is no immediate HMA official exposure.

Use a predeclared live-decay plan toward the **nearest Football A-allowed executable band**, not automatically all the way back to the raw structural ceiling.

Examples:

- A1 ceiling O3.0 with strong +0.50 hardener and current O3.75: live-decay target may be O3.5 rather than O3.0.
- A2 FOCUS + TRUE CC+ ceiling O3.0 with current O3.75: live-decay target may be O3.5 if the exceptional +0.50 gate clears.
- Ordinary A2 FOCUS ceiling O3.0 with current O3.75: target remains no higher than O3.25.

---

## 3. HMA is an execution overlay, not a structural upgrade

When HMA is used, persist both numbers:

- **Frozen structural supported ceiling**; and
- **Actual HMA executable line**.

Do not rewrite the structural burden upward after seeing the market.

The market may corroborate a strong environment but may not create A1/A2 quality, CC+, route proof, or upper-tail proof.

Required label:

`HIGH-MARKET ACCEPTANCE — FOOTBALL A`

---

## 4. Prematch execution under HMA

If the actual prematch line is inside the permitted HMA band, price clears the active floor, confirmed XI remains clean enough, and the Football A exposure gate clears, the match may become an official prematch lock immediately.

Do **not** wait for a lower line merely because the HMA line is above the structural ceiling.

Required execution state:

`DIRECT LOCK ELIGIBLE — HIGH-MARKET ACCEPTANCE`

After exposure approval:

`OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE`

Existing Football A priority-inversion rules still apply.

---

## 5. Same-line price decay replaces unrealistic line-decay waiting

When the line is already inside the permitted HMA band but the price is below the hard floor, do not plan around a quarter-line drop.

Use:

`QUALIFIED — EARLY SAME-LINE PRICE PLAN`

Freeze before kickoff:

- the accepted HMA line;
- the minimum acceptable price;
- the structural ceiling;
- HMA excess burden (`+0.25` or `+0.50`);
- the upper-tail hardener that permits the band;
- cancellation triggers.

If the **same line** clears the price floor during the early scoreless window, it may become official without waiting for a lower total.

---

## 6. Early scoreless execution window

For a predeclared HMA same-line price plan, Football A may use an early scoreless window of approximately **0'–12'**.

During this window:

- the frozen PRE structure and confirmed XI remain the primary authority;
- live statistics are **veto/context**, not a mandatory promotion requirement;
- ordinary 0-0 clock decay may improve price on the same line;
- the model must execute promptly when the predeclared line/price trigger appears and all gates remain clear.

The early HMA trigger expires or requires a fresh state-integrity reassessment after:

- any goal;
- red card;
- major attacking injury;
- obvious tactical collapse or route damage;
- other material state change.

Do not chase a goal-driven line expansion.

This window is an execution tool, not a requirement to wait. If the prematch HMA line already clears the floor and exposure gate, take the prematch decision immediately.

---

## 7. Relationship to LIVE DECAY PLAN

The Football A live-decay patch remains active, but this patch changes the target selection order.

When the current prematch line is above the raw structural ceiling:

1. test whether it is already inside the HMA band;
2. if yes and price/exposure gates clear, execute prematch;
3. if yes but only price blocks, use `QUALIFIED — EARLY SAME-LINE PRICE PLAN`;
4. if outside HMA, use `QUALIFIED — LIVE DECAY PLAN` toward the **nearest allowed HMA boundary** that the match independently qualifies for;
5. do not automatically wait all the way to the raw structural ceiling.

Thus Football A no longer treats the structural ceiling as the only possible executable target in strong high-market FOCUS matches.

---

## 8. Price policy

HMA does not change the active price floor:

- hard minimum decimal odds: **1.65**;
- preferred: **1.70+**.

Price cannot compensate for missing structural or upper-tail proof.

Do not accept +0.50 merely because the odds are attractive.

---

## 9. Relationship to the old +0.25 shadow acceptance band

This patch does **not** declare the old generic `HIGH-SCORING +0.25 ACCEPTANCE BAND — SHADOW ONLY` sample released.

Instead, HMA is a new, narrower **Football A-only official lane** with explicit structural-class and upper-tail gates.

Therefore:

- historical +0.25 shadows remain historical shadows;
- Model B remains unchanged;
- generic +0.25 acceptance outside the HMA conditions remains shadow-only;
- A2 WATCHLIST and B+ do not inherit this official lane;
- HMA official results must be audited separately from the legacy +0.25 shadow sample.

---

## 10. Priority-inversion interaction

HMA strengthens, rather than removes, the Football A priority-inversion principle.

A higher-ranked clean A1/A2 FOCUS match inside its valid HMA band should no longer be treated as unavailable merely because its raw structural line is lower.

Before exposing a weaker lower-ranked candidate, first test whether the higher-ranked match is now executable under HMA.

A materially weaker lower-ranked candidate must not displace a higher-ranked valid HMA candidate solely because it offers a lower nominal total.

---

## 11. Required persistence

For every HMA review persist:

- `Model Version = Football A`;
- Structural Rank;
- board tier;
- frozen structural supported burden / ceiling;
- actual market line and price;
- HMA excess burden: `+0.25 / +0.50 / OUTSIDE BAND`;
- HMA eligibility: `PASS / FAIL / NOT APPLICABLE`;
- upper-tail hardener used;
- confirmed-XI integrity;
- priority-inversion state;
- execution path: `PREMATCH HMA / EARLY SAME-LINE PRICE / LIVE DECAY TO HMA BOUNDARY / NO HMA`;
- Exposure Decision;
- exact blocker if no exposure.

For early same-line price plans also persist:

- predeclared HMA line;
- minimum price;
- first timestamp the same line clears the floor;
- score/minute at trigger;
- state integrity;
- final execution decision.

---

## 12. Audit separation

Post-slate Football A audit must report separately:

- normal protected-line official locks;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE` at +0.25;
- `OFFICIAL LOCK — HIGH-MARKET ACCEPTANCE` at +0.50;
- HMA early same-line price locks;
- HMA candidates outside the band that used live decay;
- HMA candidates whose trigger was invalidated by an early goal/state change;
- A2 WATCHLIST/B+ cases correctly denied HMA;
- legacy +0.25 shadow observations;
- ordinary live-decay plans and official live-decay locks.

Track outcome at both:

- the frozen structural target; and
- the actual HMA line taken.

This is required so the model can distinguish structural accuracy from execution-burden calibration.

---

## 13. Authority

This patch applies to **Football A only**.

It overrides earlier Football A / v0.2.55 / live-decay wording only where those rules:

- forced a strong A1/A2 FOCUS candidate to wait for the raw structural ceiling despite a valid HMA line being available;
- kept the generic +0.25 quarantine from allowing the narrower HMA official lane defined here; or
- targeted live decay all the way back to the structural ceiling when a nearer HMA boundary was independently qualified.

It does **not** alter Model B, structural ranking rules, the fragile SUPPORTED-route A2 FOCUS guard, the hard price floor, confirmed-XI requirements, priority-inversion guard, opportunistic-live quarantine, or settlement accounting.
