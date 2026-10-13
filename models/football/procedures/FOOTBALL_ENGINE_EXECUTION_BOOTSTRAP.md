# Football deterministic engine execution

## Active models

Football C official + Football C2 shadow.

The active engines are core.py + adapter.py, coordinated by
decision_pair_cli.py and the thin xi_portable.py user runner.

## Football-first pair

For /xi, run both stage=football_assessment inputs first. This produces
EXECUTED_C_C2_FOOTBALL_ONLY and requires no odds.

## Observed quote

For a screenshot/observed line, use adapter.evaluate_observed_quote(). It
reuses the core C/C2 quote policy but never authorizes execution.

## Strict price pair

For a real currently executable prematch quote, run both stage=decision inputs.
The strict pair applies the same quote policy plus execution authorization.

A failed optional price gate does not erase a successful football assessment.

## Persistence/publication

Persist and independently refetch once. The final publication guard verifies
that exact strict pair/readback and current quote/fixture/evidence state; it
does not rerun the models.

C3/C4 are never required for new execution.
