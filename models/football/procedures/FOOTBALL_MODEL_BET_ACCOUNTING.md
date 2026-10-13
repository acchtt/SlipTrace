# Football model accounting

Model accounting is separate from the user's physical betting ledger.

## Active C/C2 rules

- Direct strict C BET: may be counted from the actual observed executable
  line/odds used by the deterministic decision.
- Direct C2 BET: shadow accounting only, using its actual observed quote.
- WATCH: no exposure.
- unresolved WAIT: no exposure.
- WAIT explicitly reached/confirmed: may be reconciled from the actual
  confirmed reached line/odds.
- PASS: no exposure.

Do not synthesize 1.65 WATCH bets or assume that every WAIT target was reached.

## User P/L

User profit/loss is not model accounting.

Only user-confirmed records in Actual Bets — Current count toward physical
stake, profit or ROI.

A Website Pick, model BET, WATCH, WAIT or C2 shadow action never proves that the
user placed a wager.

## Historical data

Do not rewrite previously frozen historical accounting records. When comparing
them to the current policy, label old synthetic/assumed conventions explicitly
as historical.
