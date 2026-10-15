# RETIRED — 2026-10-11 Airtable active-base routing

This document records the former Airtable migration. It is no longer active
operational authority.

Effective 2026-10-15, Football v2 active persistence moved to Google Sheets
because the Airtable workspace monthly API quota was exhausted.

Former bases:

- `appbzxqXYf0lKfD4P` — previous active base, now historical read-only
- `appWyZJjitSBATXAU` — older archive, historical read-only

Current routing authority:
`models/football/google_sheets/ACTIVE_STORE_ROUTING.json`.

Do not reconstruct new Airtable writes from the old table/field IDs preserved
in repository history.
