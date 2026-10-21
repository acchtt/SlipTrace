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

## One quote policy

There is one active price policy:

- adapter.evaluate_observed_quote() for non-executable observed/user-screenshot
  comparison;
- adapter.run_decision() for a genuinely executable current prematch quote.

Both use the same Football C core rules. No wrapper-specific or second-model
ACT/BOOK/PASS logic is allowed.

## User screenshot

Use exactly the supplied line/odds. Do not fetch replacement odds.

A materially higher market total may trigger one football-evidence recheck but
cannot create a certificate. A G3-only C-FOCUS row may instead receive a
settlement-aware BOOK target without upgrading G4: O2.75 >=1.85, O3.00 >=1.90,
or O3.25 >=2.00 when the deterministic extension-quality gates clear. O3.50
still requires funded G4.

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
