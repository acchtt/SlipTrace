# Football C — Step-2 Market-History Recheck

**Status:** ACTIVE ONLY FOR STRICT NON-SCREENSHOT EXECUTION CONTEXT  
**Model:** Football C only  
**Model effect:** none; market history can trigger football reinspection but cannot create a certificate

## USER_SCREENSHOT_ONLY boundary

When the user supplies odds screenshots for `/xi` or `/xi exception`, the
screenshot is the sole market source for that comparison.

- do not search for replacement/current odds;
- do not search historical bookmaker prices merely to satisfy this procedure;
- preserve the exact supplied line/odds and source reference;
- record the limitation qualitatively when useful;
- do not forge `FOUND`, `PARTIAL` or `UNAVAILABLE_ATTEMPTED`.

Screenshot comparison remains non-executable. Football/XI/incentive research is
separate and still applies.

## Strict executable quote context

For a genuinely executable current prematch quote using an authorized
non-screenshot market source, the strict decision contract may require one
lightweight Asian-total history attempt:

`OPEN -> PRE-XI -> CURRENT PREMATCH`

Persist exactly one supported runtime state:

- `FOUND`
- `PARTIAL`
- `UNAVAILABLE_ATTEMPTED`

Never fabricate snapshots.

When observable, record opening/current center, timestamps/source and movement:

- `UP_0.50_PLUS`
- `UP_0.25`
- `STABLE`
- `DOWN_0.25`
- `DOWN_0.50_PLUS`
- `MIXED`
- `UNCLEAR`

## Football conflict recheck

Market movement may trigger reinspection for late availability, formation/role
changes, goalkeeper/centre-back changes, tactical suppression, tournament
incentive, weather/pitch or source/time mismatch.

Persist the strict runtime conflict state required by the adapter:

- `NOT_REQUIRED`
- `RECHECKED_FOOTBALL_EXPLAINED`
- `RECHECKED_UNEXPLAINED`
- `LIMITED`

Market history may expose missing information. It may not create a route,
upgrade Football C by price, raise supported burden, replace XI/H2H/incentive
research, or override the deterministic certificate.

A lower total is mechanically safer but is not automatically value.
