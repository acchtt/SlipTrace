# Football v2 — Simple /xi assess-and-price procedure

## Principle

Football comes first. Price is optional. Football C is the only active model.

## Football assessment

Freeze the current match epoch and run one Football C assessment. Odds are not
required.

Availability affects the total only when it attacks a named scoring mechanism
after replacements, opponent scoring and defensive rotation are considered.

After kickoff keep football analysis but never create retrospective prematch
exposure.

## Explicit exception integrity

`/xi exception` must start from a fresh, source-backed Football C assessment
epoch. It may not reuse a thin or challenged exception payload and may not jump
straight to a decision-stage request.

When the user disputes an exception assessment, discard that exception epoch and
rebuild the football research before rerunning the deterministic engine. A
reassessment must identify the superseded exception/epoch and use a new evidence
epoch. The same deterministic verdict is allowed only if the **new full research**
independently reaches it; the old verdict itself is not evidence.

A WATCH/PASS upstream state may be reconsidered by explicit exception, but any
promotion to FOCUS requires named changed/reclassified football fields and a
source-backed basis. Market odds cannot supply that promotion.

## One policy path

There is one active price policy:

- adapter.evaluate_observed_quote() for non-executable observed/user-screenshot
  comparison;
- adapter.run_decision() for a genuinely executable current prematch quote.

Both use the same Football C core rules. No wrapper-specific or second-model
ACT/BOOK/PASS logic is allowed.

## User screenshot

Extract exactly the visible screenshot ladder. Do not infer missing prices and
do not fetch replacement odds. Evaluate each visible line through the same C
policy, then select the highest currently supported/executable visible line. A
rejected higher total does not erase a lower supported visible total.

A materially higher market total may trigger one football-evidence recheck but
cannot create a certificate. A G3-only C-FOCUS row may instead receive a
settlement-aware BOOK target without upgrading G4: O2.75 >=1.85 or O3.00
>=1.90 when the deterministic extension-quality gates clear. G3 alone never
authorizes O3.25; O3.50 requires funded G4.

For ranked fixtures, persist the frozen board certified burden into the `/xi`
context. An upward current-certificate change is valid only when new football
evidence is explicitly verified and at least one certificate-relevant field
changed. Market movement, price, or the same preserved lineup/mechanism cannot
authorize an upgrade.

## Conditional BOOK

Active Football C does not expose a normal price WAIT. If an acceptable
line/price is not currently available but the target is prospectively reachable
without negative football information, return BOOK with the exact target line
and minimum odds. BOOK is a conditional target order and remains zero exposure
until an independently confirmed fill.

For an unsupported higher line, a target may move down to the certified burden
only when the gap is <=0.25. A 0.50+ disagreement cannot become a far-lower
target. A lone screenshot is not directional evidence.
## Persistence

Persist one C assessment/decision result and independently read it back once.

Retired C2/C3/C4 fields are historical only and are not required for new rows.

## Accounting

Internal WATCH/REVIEW_ONLY creates no model bet. BOOK creates no exposure until
fill confirmation. Active C emits no user-facing WAIT; historical WAIT records
remain immutable. Physical user P/L comes only from Actual Bets — Current.
