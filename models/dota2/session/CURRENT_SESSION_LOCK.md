# Dota 2 Current Session Authority Lock

**Status:** INACTIVE

No Dota 2 live slate is currently locked.

Before the first TAKE-eligible decision of a slate, update this file with:

- `status: ACTIVE`
- `slate_id`
- `effective_date_utc7`
- frozen `authority_commit`
- active model label
- circuit-breaker state

All analytical/procedural files for an active slate must resolve from the same frozen authority commit. Default-branch edits after lock activation are pending until the next valid lock or an explicit user-authorized relock/new authority epoch.