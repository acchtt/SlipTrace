# RETIRED — Airtable active routing

Airtable stopped being the active Football v2 persistence store on
**2026-10-15** after the workspace monthly API quota was exhausted.

Both Airtable bases are historical read-only:

- `appbzxqXYf0lKfD4P`
- `appWyZJjitSBATXAU`

Do not perform new /sweep, /rank, /xi, /live, Website Picks or Actual Bets
writes/readbacks through Airtable.

Current authority:

- `models/football/google_sheets/ACTIVE_STORE_ROUTING.json`
- Google Sheets workbook `Football v2 — Active Operations`
- spreadsheet ID `1ojWKj5aT3VEJUyX3NSbAOZNTaUM0Mb8I8e4lvFy7kGM`

Historical Airtable rows remain immutable audit material.
