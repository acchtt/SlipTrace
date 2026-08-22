# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-22-E5-2100-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-22 21:00 UTC+7`  
**Default expiry:** `2026-08-23 00:00 UTC+7`  
**Authority commit:** `d53a9809df5bead5eb78a283a727a19d9651f474`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization / match boundary

The user explicitly instructed **"Prep for lec first match"** on 2026-08-22 UTC+7 after closing the prior WBG settlement inconsistency. The first scheduled LEC match for 2026-08-22 is **Shifters (SHFT) vs Fnatic (FNC), LEC 2026 Summer Week 5 BO3**.

This starts epoch `LOL-2026-08-22-E5-2100-UTC7` and supersedes E4 prospectively. The relock is a user-authorized match-scope transition, not an outcome-driven analytical mutation. Historical E1-E4 decisions, results, process-validity labels, and P/L remain unchanged.

## Frozen authority

All analytical/procedural decisions for this epoch use frozen authority commit:

`d53a9809df5bead5eb78a283a727a19d9651f474`

Canonical model remains **LoL v0.3.58**. Retired v0.3.59/v0.3.60 material remains inactive.

The frozen authority was checked to contain the mandatory `PRE_TAKE_CERT` interlock in:

`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

## Mechanical pre-TAKE interlock — ACTIVE

For every candidate, the required order remains:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable write -> exact verification`

Before the word `TAKE` may be emitted:

- exact map, market family, selection, line/odds, evidence state/clock, Lock ID and authority commit must be populated;
- all common and family-specific gates must be explicit `PASS` or a specifically permitted `N/A`;
- any `FAIL`, `UNRESOLVED`, `UNKNOWN`, blank, omitted, implied or narrative-only field forces `HOLD/PASS`;
- family-use, minimum-odds, model, lock and state/price synchronization checks must pass;
- required arithmetic fields must be populated exactly;
- a material fight, kill, objective, structure or other decision-critical transition before entry expires the certificate and requires a fresh synchronized state/price pair plus a full rebuild;
- there is no analyst override for a failed certificate.

A visible TAKE without a valid pre-entry certificate is a procedural circuit-breaker trigger.

## Active controls

This lock preserves the frozen v0.3.58 stack and retained controls, including:

- Draft Interaction Matrix: DIM/TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP;
- UDKC / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable / Draft-Collapse controls;
- UCS and exact signed-margin/NKB handling for underdog +kills;
- FFD/RNE/Structure Substitution/safe-concede controls for favorite -kills;
- FRP for Total Kills Under and retained Total Kills Over recurrence/contact framework;
- FCR for Duration Under and failed-conversion / Structure Substitution / cascade tests for Duration Over;
- Lead Decomposition / CFC / neutral-fight stress for Live ML;
- LRO three-snapshot/two-cycle certificate when opposing a CLEAR/STRONG draft prior;
- SMR where a same-series thesis reuses a previously diagnosed failed mechanism;
- one TAKE per market family per map;
- minimum odds `1.60`;
- shadow-only policy: `0.25u` simulated, `0u` actual;
- synchronized state/price enforcement;
- saved-lineup/user-confirmed lineup fast path;
- verdict-first Airtable map/snapshot/position logging with exact verification.

## Live execution

Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.

Live ML/KH/TK require at least two usable synchronized live snapshots. A Live ML selection against a CLEAR/STRONG draft prior additionally requires `LRO = PASS`.

Underdog +kills requires complete draft-only DIM + UDKC, live preservation, exact signed margin/NKB and UCS before pricing can qualify.

No martingale, rescue, chasing or stake escalation.

## Match prep state

Match scope: `SHFT vs FNC — LEC 2026 Summer Week 5 BO3`, beginning Game 1.

Canonical Airtable check at relock time found no 2026-08-22 SHFT-FNC map, snapshot, or position records, so Game 1 begins fresh.

Current Airtable roster records are provisional and must yield to user confirmation or live scoreboard evidence:

- SHFT: Rooster / Sheo / nuc / Paduck / Stend; subs listed Boukada and Trymbi.
- FNC: Soboro / Razork / Vladi / Upset / Lospa.

No pregame draft edge is certified at lock creation. Exact Game 1 draft/roles must be read from user/live evidence before draft-sensitive analysis. Immediate-postdraft ML/KH/TK remain HOLD-only until canonical live snapshot gates are met.

## New-chat requirement

A future chat while E5 is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `d53a9809df5bead5eb78a283a727a19d9651f474`;
5. load the complete analytical/procedural stack from that same commit;
6. load the latest applicable live handoff last as state only;
7. verify `PRE_TAKE_CERT` is present in the locked session-authority procedure before any TAKE.

If authority cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Prior breaker history

E1: DK vs GEN Game 2 DK +10.5 was voided for a fight during the decision/entry window; state and price were not synchronized.

E2: DK vs GEN Game 3 GEN +9.5 was audit-invalidated because mandatory DIM/TAM/CAS fields were omitted from the underdog +kills gate signature. Historical prediction result remains Loss / -0.25u shadow / 0u actual.

E3 and E4 were separate valid match-scope epochs with circuit breaker CLEAR. E5 supersedes E4 prospectively only because the user explicitly requested preparation for the next LEC match.
