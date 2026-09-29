# Football v0.2.52 — Carrier Ceiling + B+ Evidence Hardening

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-12 ICT  
**Base:** Football v0.2.47 CLEAN + active v0.2.49 Two-Sided Priority + v0.2.50 EGE + v0.2.51 Chance-Quality / Market-Confirmation  
**Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW remain unchanged

This patch comes from the Sep 12 Atlante–Pachuca / Tijuana–Querétaro audit. It corrects a relative-ranking error without abandoning Two-Sided Priority:

- Tijuana–Querétaro was promoted from B+ WATCHLIST to an O2.5 LOCK mainly because both nominal routes survived the confirmed XI and the selected line was protected. It finished 0-1.
- Atlante–Pachuca remained B/PASS despite Pachuca retaining a credible self-funded attacking ceiling in the confirmed XI. Pachuca won 0-3 and supplied the full total alone.

The lesson is not that carrier-led matches should replace genuine Tier-A TWO-SIDED matches. The correction is narrower: **nominal two-sidedness must not automatically outrank a materially stronger self-funded carrier, and XI preservation plus line protection cannot by themselves clear a fragile B+ compression case.**

---

## 1. Official decision order

Use:

`STRUCTURAL QUALITY → ROUTE QUALITY PROOF → CARRIER CEILING / CC+ → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → STANDARD/EGE BURDEN → MCE TEST → CURRENT PRICE → LOCK/HOLD`

Frozen PRE remains frozen history. v0.2.52 changes reranking and execution gates prospectively.

---

## 2. Two-sided quality split

A match may no longer receive the full ranking benefit of TWO-SIDED merely because both teams possess a theoretical or lineup-preserved scoring route.

Classify the route state as one of:

- `TWO-SIDED — QUALITY PROVEN`
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`

### QUALITY PROVEN

Both routes need credible independent scoring evidence. Prefer:

- repeated high-value chance creation;
- repeated scoring-2+ production with credible chance context;
- central/box access and quality SOT/xG/xGOT evidence;
- strong home/away attacking splits against relevant resistance;
- a strong data-poor substitute when detailed chance data is unavailable.

### NOMINAL / WEAK SECONDARY

Use when the second route survives on paper but is supported mainly by:

- lineup presence;
- names/reputation;
- occasional goals;
- generic transition possibility;
- opponent defensive leakage without repeatable attacking creation;
- raw GF/GA that does not establish independent chance quality.

Nominal two-sidedness is still useful, but it does not receive the same ranking premium as a quality-proven two-sided matchup.

---

## 3. CC+ — Carrier Ceiling flag

Add a secondary promotion flag:

`CC+ — CARRIER CEILING`

CC+ identifies a team with a credible independent route to **3+ team goals** even when the opponent contribution route is only moderate or weak.

### CC+ evidence

Require a meaningful combination of:

1. repeated scoring-2+/3+ capacity against relevant opposition;
2. chance-quality evidence or a strong data-poor substitute showing the ceiling is not based only on finishing spikes;
3. enough attacking depth to sustain pressure after the first goal;
4. no dominant opponent suppression profile that clearly caps the carrier;
5. at final XI, preservation of the principal creators/finishers or equivalent senior replacements.

A single 3+ result does not create CC+ retroactively.

### CC+ ranking rule

Two-Sided Tier A remains the primary lane. For comparable non-Tier-A cases:

`QUALITY-PROVEN TWO-SIDED > CC+ ELITE CARRIER > NOMINAL / WEAK-SECONDARY TWO-SIDED > ordinary CARRIER-LED > FRAGILE / OTHER`

A CC+ carrier may outrank a B+ nominal two-sided candidate when the carrier has the stronger self-funded ceiling and better failure-mode resistance.

---

## 4. PRE carrier-ceiling audit gate

Before Work assigns `B / PASS` to a match containing a strong favorite/carrier, explicitly answer:

- Does either team have credible independent 3+ potential?
- Is recent low scoring caused by true chance suppression, or merely by score outcomes / finishing variance / schedule context?
- Is the carrier's ceiling supported by repeatable attacking evidence rather than one anomalous match?

If credible independent 3+ potential exists but XI uncertainty prevents promotion, do **not** silently bury the match. Use:

`CC+ CANDIDATE — XI SENSITIVE`

and keep it eligible for a post-XI carrier review unless another hard structural failure dominates.

This gate is designed to prevent recent-score suppression from automatically erasing a real carrier ceiling.

---

## 5. Narrow post-XI carrier reopen

A frozen B/PASS is still normally non-actionable. Market movement alone still cannot rescue it.

However, a narrow new assessment epoch is allowed under:

`CARRIER REOPEN — XI CONFIRMED`

All must be true:

1. the PRE PASS was **not** a hard structural rejection such as severe chance-quality failure, elite opponent suppression, deep control/format risk, or scope exclusion;
2. PRE already identified a plausible carrier ceiling but downgraded it mainly because of recent-score suppression, contribution weakness, or lineup uncertainty;
3. confirmed XI preserves the carrier's principal creators/finishers or introduces equivalent senior attacking quality;
4. current football evidence still supports an independent 3-goal ceiling;
5. supported execution burden is conservative, normally no higher than O2.5 unless the active model independently supports more;
6. price is evaluated only after the football reopen clears.

This is a football-led XI reopen, not a market rescue.

---

## 6. B+ compression hardening — preservation is neutral

For B+ with an explicit 1-0 / 1-1 / control / weak-secondary / late-goal-dependence failure mode:

- `ATTACKING DEPTH PRESERVED` is **baseline confirmation**, not a positive upgrade;
- a lower/protected Asian total is **execution protection**, not football evidence;
- current price is **not** a positive structural gate.

Therefore **XI preservation + protected line alone can no longer produce an OFFICIAL LOCK**.

Require at least one independent positive gate beyond preservation:

- fresh chance-quality evidence materially stronger than the frozen uncertainty;
- a genuine `XI UPGRADE` rather than mere preservation;
- verified same-source bullish market corroboration that agrees with intact football evidence;
- material opponent defensive weakening that improves the scoring route;
- `CC+` self-funded carrier evidence strong enough to survive the named compression branch.

If none exists:

`B+ PRESERVATION-ONLY HOLD`

This rule would have blocked the Sep 12 Tijuana–Querétaro O2.5 lock.

---

## 7. Same-window relative rerank

When multiple FOCUS/WATCHLIST/eligible carrier-reopen matches overlap, rerank them together after XI and market-history review.

Do not compare only grades. Explicitly compare:

- quality-proven vs nominal two-sidedness;
- self-funded carrier ceiling;
- chance-quality support;
- failure-mode resistance;
- dependence on the weaker team's contribution;
- burden required by the available total.

A nominal B+ two-sided candidate should not outrank a CC+ carrier solely because it has two theoretical routes.

---

## 8. Audit labels added

Use where relevant:

- `TWO-SIDED — QUALITY PROVEN`
- `TWO-SIDED — NOMINAL / WEAK SECONDARY`
- `CC+ — CARRIER CEILING`
- `CC+ CANDIDATE — XI SENSITIVE`
- `CARRIER REOPEN — XI CONFIRMED`
- `B+ PRESERVATION-ONLY HOLD`
- `RELATIVE-RANKING MISS`
- `RECENT-SCORE SUPPRESSION OVERWEIGHTED`

Continue using v0.2.50/v0.2.51 labels where applicable.

---

## 9. What does not change

- Genuine Tier-A TWO-SIDED remains the primary ranking lane.
- Structural quality remains ahead of market price.
- MCE cannot rescue a genuine PASS.
- EGE remains a separate strict regime.
- Price cannot create structure.
- A protected line cannot rescue dual-route XI damage.
- Current executable odds still require the user's supplied market unless external verification is explicitly requested.

---

## 10. Version boundary

Football v0.2.52 is prospective from 2026-09-12 ICT.

The Sep 12 Tijuana–Querétaro official loss remains settled under v0.2.51. Atlante–Pachuca remains a historical PASS with no retrospective P/L. Both are calibration evidence only.