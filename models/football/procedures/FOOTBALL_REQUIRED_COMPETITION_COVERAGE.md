# Football Required Competition Coverage Manifest

**Status:** MANDATORY STEP-0 COVERAGE INVARIANT  
**Purpose:** prevent an entire actionable competition block from disappearing before Work even sees it  
**Version:** `required-competition-manifest-v1`

## 1. Why this exists

Generic rules such as "account for every visible senior block" are insufficient when discovery itself misses a competition.

A protected competition block must therefore be checked explicitly, independently of whether the normal broad discovery pass happened to surface it.

This is a coverage/accounting rule only. It does not promote fixtures into Football C.

## 2. Protected blocks — v1

The required protected block registry currently contains:

- `NED_EERSTE_DIVISIE` — Netherlands Eerste Divisie / Keuken Kampioen Divisie, including Jong/U21/reserve-branded senior participants when they are official league participants.

The registry may be expanded only by a versioned change to this procedure.

## 3. Required status per sweep window

For every protected block, Step 0 must record exactly one:

- `CHECKED_WITH_FIXTURES`
- `CHECKED_NO_IN_WINDOW_FIXTURES`
- `SOURCE_BLOCKED`

`SOURCE_BLOCKED` is unresolved and makes the handoff fail closed.

Do not omit a block because:
- the competition is lower division;
- it contains Jong/U21/reserve-branded official participants;
- it is unfamiliar;
- the normal broad discovery pass did not surface it.

## 4. Fixture accounting

When status is `CHECKED_WITH_FIXTURES`, enumerate every official in-window fixture from that competition block before normal hard-scope / operational / researchability / capacity rules are applied.

Every enumerated fixture must end in one normal Step-0 disposition:
- ADMITTED_TO_C
- HARD_EXCLUDED
- OPERATIONAL_EXCLUDED
- RESEARCHABILITY_EXCLUDED
- OPERATIONAL_CAPACITY_DEFERRED
- UNRESOLVED

Official Jong/U21/reserve-branded clubs participating in the Netherlands Eerste Divisie are **senior league fixtures for coverage purposes**. Do not remove them under generic reserve/youth-name exclusions.

## 5. Persisted manifest

Persist:

`required_competition_manifest_version = required-competition-manifest-v1`

and a block array equivalent to:

```json
[
  {
    "block_id": "NED_EERSTE_DIVISIE",
    "status": "CHECKED_WITH_FIXTURES",
    "fixture_count": 6,
    "fixtures": [
      {
        "match_id": "...",
        "match": "Home - Away",
        "kickoff_ict": "...",
        "disposition": "ADMITTED_TO_C"
      }
    ],
    "note": "..."
  }
]
```

If no fixtures are in the requested window, use `fixture_count=0` and `CHECKED_NO_IN_WINDOW_FIXTURES`.

## 6. Work-readiness gate

Before `work_ready=true`:

- manifest version must be present and current;
- every protected block must be present exactly once;
- no protected block may be `SOURCE_BLOCKED`;
- every CHECKED_WITH_FIXTURES block must list all known in-window official fixtures;
- every listed fixture must have a disposition.

Otherwise:

`HANDOFF INCOMPLETE — REQUIRED COMPETITION COVERAGE GAP`

For Netherlands specifically:

`HANDOFF INCOMPLETE — NETHERLANDS EERSTE DIVISIE COVERAGE GAP`

## 7. Work preflight

`/rank` must reject a Step-0 handoff when:
- the required manifest is absent;
- the manifest version is stale;
- a protected block is missing;
- any block is SOURCE_BLOCKED;
- fixture_count does not match the fixture list;
- a listed fixture lacks a disposition.

Work must not silently reconstruct and rank an incomplete board. Return to Step 0 or explicitly repair the handoff first.

## 8. Audit

Post-slate audit must distinguish:
- required-block discovery miss;
- fixture enumeration miss;
- wrong hard exclusion;
- legitimate operational/researchability/capacity disposition.

A missing required block is board-level coverage contamination for C/C2/C3 confirmatory-board counting.

A correctly discovered fixture that is later excluded for a valid documented reason is not a coverage miss.

## 9. Airtable

Sweep Runs fields:

- `Required Competition Manifest Version` — `fldYxv9Oljrkq4lZf`
- `Required Competition Blocks` — `fldvIsy67dwIvarf2`
- `Required Competition Blocks Complete` — `fldFcVeFIAikCWBj2`

Set `Required Competition Blocks Complete = true` only after this invariant passes.
