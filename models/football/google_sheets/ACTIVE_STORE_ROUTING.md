# Football v2 — active Google Sheets routing

**Active store from 2026-10-15:** Google Sheets workbook
`Football v2 — Active Operations`.

Spreadsheet ID:
`1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`

Airtable bases `appbzxqXYf0lKfD4P` and `appWyZJjitSBATXAU` are now
historical read-only. New football writes must never target Airtable.

Machine authority: `ACTIVE_STORE_ROUTING.json`.

## Tabs and immutable keys

- Sweep Runs → Run ID
- Daily Coverage Ledger → Coverage ID
- Decision States → Assessment ID
- Website Picks → Publication Key
- Actual Bets — Current → Bet ID
- Competition Reliability → Competition Key
- Competition Reliability Events → Event ID
- Factor Calibration Observations → Observation ID
- Manual Scores → Score ID
- Circuit Breaker → Breaker ID

Each stage writes/upserts by the first-column immutable key and performs one
independent Google Sheets refetch before claiming persistence.

## /sweep

Unlike the retired Airtable routing split, Sweep Runs is now part of the same
active workbook. The frozen V4 source/receipt artifacts remain the ranking
authority; the sheet is an operational ledger, not a substitute source.

## /rank

Persist each ranked fixture to Daily Coverage Ledger with the exact
`Step1 Engine C Result` JSON, then independently refetch by Coverage ID.

The verified stage status is `V4_RANK_PERSISTENCE_VERIFIED`.

## /xi

Persist one Decision States row per Assessment ID/evidence epoch. Preserve the
exact C result and ordinary Evaluated Line / Evaluated Odds columns when an
observed user screenshot was compared.

## Website Picks and Actual Bets

Only an authorized strict C decision may create a Website Picks row.

WATCH and unresolved WAIT create no exposure. Only a verified user slip may
create/update Actual Bets — Current.

## Migration boundary

The Airtable monthly API quota was already exhausted when this migration
started. Existing Airtable rows are not silently reconstructed. Data available
through frozen receipts/exports can be backfilled to the new workbook with its
original immutable identity and marked as migration history; all new
operations write to Google Sheets immediately.
