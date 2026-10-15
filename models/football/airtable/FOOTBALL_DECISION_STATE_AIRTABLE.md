# Football Decision State — current Airtable contract

Active base: appbzxqXYf0lKfD4P.

Football C is the only active model. Existing C2/C3/C4 fields are historical
read-only compatibility fields and are not required for new records.

## One assessment epoch

For each new /xi assessment persist:

- Assessment ID and canonical match identity;
- evidence epoch / assessment timestamp;
- current fixture status, score/minute where applicable;
- exact Football C football result JSON;
- C supported burden and current football notes;
- evaluated line/odds when an observed quote was compared;
- strict C decision result when a genuinely executable prematch decision ran.

Active XI Assessment Execution Status values:

- EXECUTED_C_FOOTBALL_ONLY
- EXECUTED_C_FOOTBALL_AND_PRICE
- ENGINE_FAILED_AFTER_ATTEMPT

A failed optional price check after successful football assessment remains
EXECUTED_C_FOOTBALL_ONLY.

## Screenshot quote

Persist ordinary evaluated line and evaluated odds. The screenshot/capture
reference may remain normal evidence metadata.

A screenshot comparison is non-executable and never creates a Website Pick or
model exposure.

## Strict decision

A strict prematch decision requires real current execution evidence. Persist
the exact C result, then independently refetch once before publication.

The final publication guard compares that C result with the readback and checks
quote/fixture/evidence freshness. It does not rerun the model.

## Retired fields

Do not write new C2/C3/C4 states/actions/results. Existing values remain
immutable historical evidence and may be read for audit only.

## Exposure

WATCH and unresolved WAIT create no model exposure.

Only a strict C BET or a confirmed reached WAIT may enter C model accounting.
Only a user-confirmed physical slip may enter Actual Bets — Current.
