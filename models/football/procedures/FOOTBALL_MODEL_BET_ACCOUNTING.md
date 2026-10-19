# Football model accounting

## Active rule

Football C is the only active model-accounting roster.

- direct C BET: use exact observed line/odds;
- C BOOK order creation: no exposure;
- confirmed C BOOK fill: exposure only when the actual filled line equals the
  frozen BOOK target and filled odds meet/exceed the frozen BOOK minimum;
- unresolved C WAIT: no exposure;
- reached WAIT: exposure only when reached terms are actually confirmed;
- WATCH/PASS: no exposure.

C2/C3/C4 accounting is historical read-only and may be processed only through
an explicitly historical audit path.

A Website Pick, model BET/BOOK/WATCH/WAIT or retired shadow action never
proves that the user physically executed a bet. A BOOK is only a target order
until its fill is independently confirmed. Actual Bets — Current is the sole
user P/L authority.
