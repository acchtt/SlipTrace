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

Complete research uses `V4_RANK_PERSISTENCE_VERIFIED`. An assessed board with
unresolved cohort research uses `V4_RANK_PARTIAL_PERSISTENCE_VERIFIED`.
Both verify exact saved board rows; only the former claims completed research
for new coverage-aware receipts. Unresolved fixtures remain in the native rank
checkpoint, never synthetic Daily Coverage selections.

## /xi

Persist one Decision States row per Assessment ID/evidence epoch. Preserve the
exact C result and ordinary Evaluated Line / Evaluated Odds columns when an
observed user screenshot was compared.

## Website Picks and Actual Bets

Only an authorized strict C decision may create a Website Picks row.

WATCH and unresolved WAIT create no exposure. Only a verified user slip may
create/update Actual Bets — Current. Actual Bets — Current is the sole user P/L
authority.

## Migration boundary

The Airtable monthly API quota was already exhausted when this migration
started. Existing Airtable rows are not silently reconstructed. Data available
through frozen receipts/exports can be backfilled to the new workbook with its
original immutable identity and marked as migration history; all new
operations write to Google Sheets immediately.


## Public website projection

The operational workbook remains private. The website never reads the private
workbook directly.

After a verified change to `Daily Coverage Ledger` or `Website Picks`, run
`models/football/google_sheets/public_projection.py` against independently
refetched rows from those two allowlisted tabs and update:

`acchtt/football-v2@main:pages/data/board-feed.json`

Projection schema: `football-v2-public-board-feed-v1`.

Allowed inputs:

- Daily Coverage Ledger
- Website Picks

Explicitly forbidden as projection inputs:

- Decision States
- Actual Bets — Current
- Competition Reliability Events
- Factor Calibration Observations

The builder strips Step1 engine-result JSON and generic Payload JSON even when
those columns exist in the coverage/pick readback.

Website display mapping remains display-only:

- FOLLOW -> FOCUS
- RESERVE -> WATCHLIST
- STOP -> PASS

A projection refresh never creates model authority, a bet, or a persistence
receipt. The Google Sheets verified row remains authoritative.
