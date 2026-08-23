# LoL PRE_TAKE_CERT Mechanical Validator — 2026-08-23

**Status:** ACTIVE CANONICAL v0.3.58 EXECUTION INTERLOCK  
**Effective:** 2026-08-23 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Authorization:** user instruction **“Do it now”** after diagnosing repeated skipped mandatory gates, including the BFX–NS G1 NS +5.5 kills execution failure.

This procedure adds **no new predictive betting edge**. It hardens execution so an existing mandatory rule cannot be silently skipped, implied, compressed into narrative, or overridden by an attractive price or a persuasive headline state.

---

## 1. Protected-token rule

The visible word `TAKE` is a protected execution token.

Before `TAKE` may be emitted, the analyst must complete an internal structured `PRE_TAKE_CERT` and run the mechanical validator in this file.

Required order:

`evidence -> applicability resolver -> PRE_TAKE_CERT build -> contradiction scan -> mechanical validator -> final synchronized state/price recheck -> visible verdict -> Airtable write -> exact verification`

If the validator does not return `CERT_STATE = PASS`, the visible verdict is **HOLD/PASS**.

Narrative confidence, implied satisfaction, overall-thesis language, price attractiveness, prior wins, or urgency can never substitute for validator PASS.

---

## 2. Applicability resolver is mandatory

Before building the certificate, identify:

- active Session Authority Lock;
- frozen authority commit;
- active model;
- map and market family;
- whether the market is executable and synchronized;
- whether the family is still open on the map;
- whether the two-snapshot gate applies and is satisfied;
- every family-specific and conditional gate that applies to this candidate.

The resolver must produce an explicit `REQUIRED_FIELDS` manifest.

A field may be marked `N/A` only with an explicit rule-grounded reason. `N/A` without a reason is unresolved and fails validation.

The analyst may not start from the displayed line and reason backward into a smaller manifest.

---

## 3. Terminal-value requirement

Every field in `REQUIRED_FIELDS` must have:

1. an explicit terminal value such as `PASS / FAIL / UNRESOLVED`, a required enum, or a concrete numeric value;
2. evidence or a rule-grounded basis;
3. no unresolved contradiction with another mandatory field.

The following do **not** count as resolved fields:

- narrative-only statements;
- “looks fine”, “should hold”, “probably”, or equivalent implication;
- a field silently omitted because another field seemed persuasive;
- a numeric hurdle presented as if it proved the probability of clearing that hurdle;
- a draft theory field reused as live proof;
- a live score descriptor reused as draft proof.

Any required field that is missing, implied, contradictory, `FAIL`, or `UNRESOLVED` forces `CERT_STATE = FAIL`.

---

## 4. Global certificate header

Every candidate PRE_TAKE_CERT must explicitly resolve at least:

`LOCK | AUTHORITY | MODEL | EXEC | SYNC | ODDS | FAMILY | FAMILY_OPEN | POSBLIND | STATE_FRESH | REQUIRED_FIELDS`

Additional global controls apply where defined by canonical rules, including snapshot-count gates, exact arithmetic, stale-market rejection, and state-change expiry.

If `LOCK`, `AUTHORITY`, `MODEL`, `EXEC`, `SYNC`, `ODDS`, `FAMILY_OPEN`, `POSBLIND`, or `STATE_FRESH` fails, no family analysis can rescue the candidate.

---

## 5. Family manifests

The applicability resolver must append the full active family signature from canonical authority. At minimum:

### 5.1 Live Moneyline

Resolve all applicable Live ML controls, including:

`2SNAP | LEAD_DECOMPOSITION | DPS | CFC_CURRENT | NEUTRAL_FIGHT_STRESS | DRP (when applicable) | LRO (when applicable) | PRICE`

A contrary-draft ML candidate may not omit LRO merely because the current live state appears convincing.

### 5.2 Underdog +kills / positive kill handicap

Resolve the complete canonical sequence, without compression:

`2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | UCS | SCNE | SIGNED_MARGIN | EXACT_NKB | PRICE`

Where older canonical wording uses `RLD`, the validator requires two explicit views:

- `RLD_DRAFT` — draft-only role/leverage suppression structure;
- `LIVE_RLD` — current economy/levels/control distribution and whether it preserves or invalidates the draft fallback.

`LIVE_RLD` is an enforcement split of the already-mandatory RLD rule, not a new predictive concept.

For `LIVE_RLD`, explicitly record:

- favorite carry-centered economy concentration;
- underdog multi-role resilience or lack of it;
- favorite repeatable margin-expansion routes currently empowered by economy/levels/control;
- concrete underdog suppression mechanisms that have actually survived live contact;
- whether the live distribution **preserves or downgrades** the draft certificate.

Hard contradiction rule:

> Carry-centered favorite economy plus cleaner grouped control cannot coexist with `LIVE_PRESERVATION = PASS` or `LAC = PASS` unless there is strong observed live suppression of those empowered routes.

If that observed suppression is absent, ambiguous, or contradicted by the current distribution, set `LIVE_RLD = FAIL` and the candidate is HOLD/PASS.

A stable kill margin, 0–0 towers, a large printed cushion, or correct NKB arithmetic cannot override failed `LIVE_RLD`, `KMS`, `LAC`, or `UCS`.

### 5.3 Favorite negative kill handicap

Resolve exact signed margin and remaining expansion burden plus all active favorite-margin continuation / control gates defined by canonical rules. A large lead alone is not sufficient if the remaining expansion burden is unrealistic or continuation control is unresolved.

### 5.4 Duration Over

Resolve the full DOVC signature:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

No DOVC field may be inferred from “slow game”, low kills, close gold, 0–0 towers, or theoretical waveclear.

### 5.5 Duration Under

Resolve all active Duration Under controls including FCR / shortest-close-route stress and any required current-state conversion evidence. A fast-close thesis that depends on one fragile uninterrupted branch must fail closed.

### 5.6 Total Kills Under

Resolve all active TK Under controls including `FRP = PASS`. Passive quiet or low current kills cannot substitute for forward-regime persistence.

### 5.7 Total Kills Over

Resolve the active recurrence/contact-pressure signature. Current kill pace alone cannot substitute for demonstrated or structurally supported recurrence.

---

## 6. Contradiction scan

After all fields are populated, run a separate contradiction scan before validation.

The scan must answer:

- Does live economy distribution contradict a draft fallback assumption?
- Does current objective/structure control contradict claimed anti-cascade preservation?
- Does a favorite carry or engage role hold enough leverage to empower repeatable expansion routes the underdog has not suppressed?
- Does current state invalidate an earlier snapshot-based mechanism?
- Does the candidate depend on a field that canonical rules explicitly classify as non-evidence?
- Does any downstream live field require a downgrade of an upstream draft certificate?

The scan returns:

`CONTRADICTIONS = []`

or an explicit list.

Any unresolved material contradiction forces `CERT_STATE = FAIL`.

Downstream live evidence may preserve or **downgrade** draft proof. It may never be ignored merely because the draft certificate was previously STABLE.

---

## 7. Mechanical validator output

Immediately before the final state/price recheck, compute:

`REQUIRED_FIELDS`

`RESOLVED_FIELDS`

`FAILED_FIELDS`

`UNRESOLVED_FIELDS`

`CONTRADICTIONS`

`CERT_STATE`

Mechanical rule:

- `CERT_STATE = PASS` only when every required field is resolved in an eligible terminal state, `FAILED_FIELDS = []`, `UNRESOLVED_FIELDS = []`, and `CONTRADICTIONS = []`.
- Otherwise `CERT_STATE = FAIL`.

There is no discretionary override.

If the analyst cannot enumerate the required fields confidently, `CERT_STATE = FAIL`.

---

## 8. Final synchronized recheck

After validator PASS but **before** visible `TAKE`, recheck:

`STATE_FRESH | EXECUTABLE_PRICE | MARKET_ACTIVE | FAMILY_OPEN`

A material state change, odds change that alters eligibility/value, suspension, stale feed, or family closure expires the certificate.

Expired certificate => rebuild from current synchronized evidence. Never reuse a stale PASS.

---

## 9. Circuit-breaker enforcement

Any of the following is a procedural execution failure:

- visible `TAKE` without a complete validator PASS;
- skipped required family field;
- a required field implied only through narrative;
- unresolved contradiction ignored;
- stale certificate reuse;
- wrong authority/model;
- using draft theory as live proof or live evidence as draft proof;
- allowing price or hurdle arithmetic to override a failed mechanism gate.

On detection, immediately trigger:

`TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER`

No further TAKE is allowed under that authority epoch until the execution defect is repaired and a valid authority relock/reset explicitly clears the breaker.

Historical positions remain historical; do not rewrite an issued TAKE as a fictional HOLD.

---

## 10. Post-verdict logging

Verdict-first governance remains unchanged.

For HOLD/PASS:

- log/verify the Snapshot as required;
- create no Position.

For TAKE:

- emit the visible verdict first;
- then create the Snapshot and Position;
- verify exact IDs, selection, odds, stake, entry clock, thesis state, and actual exposure.

The validator must not introduce connector latency before the visible verdict.

---

## 11. Reference failure — BFX vs NS G1, NS +5.5

The historical `NS +5.5 kills @1.869` TAKE remains a real historical loss.

The execution error was not absence of draft/economy rules. Canonical rules already required KMS, RLD, live preservation, LAC, UCS, and exact arithmetic.

The failure was that a stable `BFX +1` kill margin and 0–0 towers were allowed to dominate the decision while BFX had meaningful favorite-side carry leverage and repeatable J4/Rumble/Bard/Ryze/Caitlyn expansion routes.

Under this validator, that candidate could not reach `TAKE` unless `LIVE_RLD`, `KMS`, `LIVE_PRESERVATION`, and `LAC` were all explicitly resolved and contradiction-free. Carry-centered favorite economy with insufficient demonstrated suppression would force HOLD/PASS.

---

## 12. Anti-overfit guard

This file does **not** mean:

- fewer bets for their own sake;
- automatic rejection of underdog +kills;
- a new minimum game clock;
- a new odds floor;
- a mandatory tower lead;
- automatic preference for favorites;
- rewriting outcomes into new rules after every loss.

It means only this:

> Existing canonical requirements must be mechanically enumerated, resolved, contradiction-checked, and validated before `TAKE` can exist.

If every applicable field genuinely passes, the candidate remains TAKE-eligible under the underlying model.