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
ACT/WAIT/PASS logic is allowed.

## User screenshot

Use exactly the supplied line/odds. Do not fetch replacement odds.

A materially higher market total may trigger one football-evidence recheck but
cannot create a certificate.

For ranked fixtures, persist the frozen board certified burden into the `/xi`
context. An upward current-certificate change is valid only when new football
evidence is explicitly verified and at least one certificate-relevant field
changed. Market movement, price, or the same preserved lineup/mechanism cannot
authorize an upgrade.

## WAIT

WAIT requires real reachability, an intact mechanism, no negative-information
dependency and no material veto.

A lone screenshot is not directional evidence. Do not create a same-line
micro-WAIT solely because odds might drift.

## Persistence

Persist one C assessment/decision result and independently read it back once.

Retired C2/C3/C4 fields are historical only and are not required for new rows.

## Accounting

WATCH and unresolved WAIT create no exposure. Physical user P/L comes only
from Actual Bets — Current.
