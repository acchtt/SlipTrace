# Football v0.2.51 — Chance-Quality + Market-Confirmation Calibration

**Status:** ACTIVE OFFICIAL PATCH  
**Effective:** 2026-09-11 ICT  
**Base:** Football v0.2.47 CLEAN + active v0.2.49 Two-Sided Priority + v0.2.50 EGE  
**Shadow comparisons:** v0.2.47 CLEAN and v0.2.48-SHADOW remain unchanged

This patch comes from the Sep 10–11 audit. It addresses three specific errors without broadly loosening the model:

1. A1 TWO-SIDED cases were sometimes promoted to O3.0+ without enough proof that both routes repeatedly create high-value chances.
2. Protected totals sometimes rescued an A2/B+ after meaningful XI route damage.
3. A strong same-source opening-to-close total move could correctly challenge an overstated XI downgrade, but the previous workflow could still leave a valid borderline Over permanently stuck on HOLD.

The patch keeps structure first, preserves frozen PRE, and does not allow price alone to manufacture an Over thesis.

---

## 1. Official decision order

Use:

`STRUCTURAL QUALITY → CARRIER CEILING → FAILURE-MODE RESISTANCE → TEAM GF/GA PROFILE → CHANCE QUALITY HARDENING → FIRST-PASS XI → MARKET-HISTORY CONFLICT CHECK → FINAL XI → STANDARD/EGE BURDEN → MARKET-CONFIRMED EDGE TEST → CURRENT PRICE → LOCK/HOLD`

Frozen PRE remains frozen. Market history is still a later-stage calibration layer.

---

## 2. A1 TWO-SIDED O3+ chance-quality hardening

Before an A1 TWO-SIDED fixture can support a **STANDARD burden of O3.0 or higher**, require evidence that both independent routes are not merely nominal.

At least one of the following should be demonstrated for **each route**, using recent/relevant evidence where available:

- repeated big-chance creation;
- repeated central / penalty-area access;
- repeatable high-quality SOT / xG / xGOT production;
- a strong scoring-2+ frequency backed by credible chance-generation context;
- equivalent evidence that the route regularly creates more than low-value volume.

If one route is supported mainly by reputation, possession, raw shot count, occasional high totals, or theoretical transition threat, do **not** call the matchup A1 TWO-SIDED at an O3+ burden without stronger evidence.

Allowed responses:

- downgrade A1 → A2;
- keep A1 but cap STANDARD burden at O2.75;
- reclassify to ELITE CARRIER/CARRIER-LED if one side is doing most of the real work.

This rule is specifically designed to prevent PSV–Shakhtar-type false A1/O3 classifications where the final game produces little or no genuine big-chance quality.

### Data-poor exception

If detailed chance data is unavailable, do not automatically PASS. Use the best available scoring-2+/conceding-2+, home/away, team-style and opponent-quality evidence, but reduce confidence by one step unless the scoring profile is exceptionally stable.

---

## 3. Dual-route XI damage hardening

If confirmed XI materially removes or weakens important creators/finishers on **both sides**, or damages the primary route plus the opponent contribution route, classify:

`DUAL-ROUTE XI DAMAGE`

For A2/B+ cases under this tag:

- a lower protected total **cannot by itself rescue the match**;
- price protection is not enough;
- require a fresh independent football reason that the reduced XI still creates the supported burden;
- otherwise HOLD.

Examples of fresh independent support:

- equivalent senior replacements with proven production;
- a clear shape change that preserves or improves chance generation;
- strong bench/rotation depth that keeps both routes coherent;
- reliable recent evidence that the starting replacements create comparable chances.

Do not confuse this with ordinary rotation.

`ROTATION — ATTACKING DEPTH PRESERVED` remains neutral/near-neutral.

This rule is designed to prevent Shamal–Wakrah-type promotion where both principal finishing routes were reduced and protection was allowed to do too much work.

---

## 4. Market-confirmed edge (MCE) — limited +0.25 exception

The previous hard boundary remains the default: market movement does not create structure or freely raise burden.

However, a **limited one-quarter-line exception** is now allowed when the market move resolves a genuine edge case already supported by football evidence.

Tag:

`MCE +0.25 — MARKET-CONFIRMED EDGE`

### Eligibility

All must be true:

1. Frozen PRE is **A2 FOCUS** or **B+ WATCHLIST** and structurally TWO-SIDED.
2. Frozen STANDARD burden is at least **O2.5**.
3. Final XI classification is `ATTACKING DEPTH PRESERVED` or stronger; no meaningful route damage remains.
4. Independent football evidence supports a credible **3-goal ceiling** even if the conservative frozen burden stopped at O2.5.
5. Same-source or normalized market history shows a **BULLISH LINE move of at least +0.25** from OPEN to post-XI/current prematch.
6. The higher line is still only **0.25 above the frozen supported burden**.
7. Current Over price at that higher line is at least **1.75**.
8. No dominant compression/suppression failure mode remains after XI review.

If all eight clear, the model may treat the +0.25 line as an executable edge rather than an automatic HOLD.

### What MCE may not do

MCE may **not**:

- promote B/PASS;
- create TWO-SIDED structure;
- create EGE;
- jump more than +0.25 above frozen burden;
- override DUAL-ROUTE XI DAMAGE;
- override a dominant first-leg/derby/suppression branch;
- use cross-book noise as if it were a continuous market move.

### Pumas calibration example

A frozen B+ TWO-SIDED O2.5 case with preserved attacking XI and a same-source move such as:

`OPEN O2.5 @1.85 → POST-XI O2.75 @1.89`

is no longer automatically discarded solely because O2.75 is one quarter above the frozen burden. If the football evidence independently supports a 3-goal ceiling and the failure mode is not dominant, it may qualify as `MCE +0.25`.

This is a narrow exception, not a general market-following rule.

---

## 5. Market/XI conflict resolution is now mandatory when history exists

When market history is available, do not finalize an XI downgrade until the conflict check is completed.

If first-pass XI says `COHESION / ROUTE DAMAGE` but the same-source total moves +0.25 or more upward, explicitly answer:

- Is the missing player truly irreplaceable?
- Are equivalent senior attackers still starting?
- Did shape remain aggressive?
- Did both scoring routes actually survive?

If yes, reclassify to `ATTACKING DEPTH PRESERVED` and restore the **frozen burden** if appropriate.

The market may correct an overstated XI downgrade. It still may not invent a new structural route.

---

## 6. Failure-mode calibration after Firpo–Olimpia

A named compression failure mode appearing temporarily — for example 0-0 at HT — does not prove the prematch selection was structurally wrong if:

- the selected line was already protected;
- a credible carrier route remained intact;
- the match still had realistic substitution/depth or second-half escalation capacity.

For audit, distinguish:

- `FAILURE MODE TEMPORARILY ACTIVE` from
- `FAILURE MODE DOMINANT / MODEL INVALIDATED`.

Firpo–Olimpia 0-3 is a protected-line/carrier validation, but not a clean TWO-SIDED validation because Firpo failed to score.

Do not use this rule to chase live totals after a quiet half.

---

## 7. Audit labels added

Add where relevant:

- `CQ HARDENED`
- `DUAL-ROUTE XI DAMAGE`
- `MCE +0.25`
- `FAILURE MODE TEMPORARILY ACTIVE`
- `CARRIER VALIDATION — NOT CLEAN TWO-SIDED`

Continue using the v0.2.50 regime labels as well.

---

## 8. Price policy

Unchanged unless MCE applies:

- hard minimum 1.65;
- preferred 1.70+;
- MCE higher-line exception requires 1.75+;
- do not stretch merely for price;
- for normal STANDARD cases, choose burden before current price.

---

## 9. Version boundary

Football v0.2.51 is prospective from 2026-09-11 ICT.

Historical selections remain settled under the version that produced them. Sep 10–11 results are calibration evidence, not retroactive re-grades or P/L rewrites.
