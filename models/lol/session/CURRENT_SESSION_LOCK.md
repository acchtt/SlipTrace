# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-22-E3-1836-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-22 18:36 UTC+7`  
**Default expiry:** `2026-08-23 00:00 UTC+7`  
**Authority commit:** `7f308824e7e31eaaa56c6d53c115ce6d76651faf`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR — prospectively cleared at next-match boundary under explicit user authorization`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization / match boundary

The user explicitly authorized the next lock phase to begin at the **next match boundary**. The next match is **Kiwoom DRX (KRX) vs DN SOOPers (DNS), Game 1**, observed live at 18:36 UTC+7.

This starts epoch `LOL-2026-08-22-E3-1836-UTC7`. The prior E2 circuit breaker is cleared prospectively only for this new epoch. Historical process invalidations and prediction results remain unchanged.

## Frozen authority

All analytical/procedural decisions for this epoch use frozen authority commit:

`7f308824e7e31eaaa56c6d53c115ce6d76651faf`

Canonical model remains **LoL v0.3.58**. Retired v0.3.59/v0.3.60 material remains inactive.

This authority has been verified to contain the mandatory mechanical `PRE_TAKE_CERT` interlock in:

`models/lol/procedures/LOL_SESSION_AUTHORITY_LOCK_TAKE_SIGNATURE_AND_CIRCUIT_BREAKER_2026-08-20.md`

## Mechanical pre-TAKE interlock — ACTIVE

For every candidate, the required execution order is:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable write -> exact verification`

Before the word `TAKE` may be emitted:

- the exact map, market family, selection, line/odds, evidence state/clock, Lock ID and authority commit must be populated;
- every common and family-specific gate must be present exactly once;
- every categorical gate must be explicit `PASS` or a specifically permitted `N/A`;
- any `FAIL`, `UNRESOLVED`, `UNKNOWN`, blank, omitted, implied or narrative-only field forces `HOLD/PASS`;
- exact arithmetic fields required by the market family must be populated;
- family-use, minimum-odds, model, lock and state/price synchronization checks must pass;
- any material fight, kill, objective, structure or other decision-critical transition before entry expires the certificate completely and requires a fresh synchronized state/price pair plus a full rebuild;
- there is no analyst override for a failed certificate.

A visible TAKE produced without a valid pre-entry certificate is a procedural circuit-breaker trigger.

## Anti-hindsight accounting

Postgame analysis may diagnose a prediction but may not rewrite a historical losing prediction into a fictional pre-entry HOLD.

Track separately:

- `PREDICTION_RESULT = WIN / LOSS / PUSH / VOID`
- `PROCESS_VALIDITY = VALID / INVALIDATED`

Procedural invalidation never deletes a losing prediction from model-performance accounting.

## Active controls

This lock includes the v0.3.58 stack and retained controls, including:

- Draft Interaction Matrix: DIM/TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP;
- UDKC / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable / Draft-Collapse controls;
- UCS and exact signed-margin/NKB handling for underdog +kills;
- FFD/RNE/Structure Substitution/safe-concede controls for favorite -kills;
- FRP for Total Kills Under;
- retained Total Kills Over recurrence/contact framework;
- FCR for Duration Under;
- failed-conversion / Structure Substitution / cascade tests for Duration Over;
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

Live ML/KH/TK require at least two usable live snapshots. A Live ML selection against a CLEAR/STRONG draft prior additionally requires LRO PASS.

Underdog +kills requires complete draft-only DIM + UDKC, live preservation, exact signed margin/NKB and UCS before pricing can qualify.

No martingale, rescue, chasing or stake escalation.

## Current match state at lock creation

Match: `KRX vs DNS — Game 1`.

First observed live state at 4:36:

- KRX 1-0 DNS kills;
- KRX approximately +854 gold;
- towers 0-0;
- dragons 0-0;
- barons 0-0;
- inhibitors 0-0.

Draft/roles visible from the live scoreboard:

- KRX: Frog Olaf / Willer Lee Sin / Ucal Galio / Aiming Lucian / Andil Milio;
- DNS: DuDu Camille / Sharvel Pantheon / Clozer Orianna / deokdam Xayah / Peter Rakan.

This first state is Snapshot 1 only. No odds were supplied with it, so no market is TAKE-eligible from this evidence alone.

## New-chat requirement

A future chat while E3 is active must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `7f308824e7e31eaaa56c6d53c115ce6d76651faf`;
5. load the complete analytical/procedural stack from that same commit;
6. load the latest applicable live handoff last as state only;
7. verify that `PRE_TAKE_CERT` is present in the locked session-authority procedure before any TAKE.

If authority cannot be loaded or model hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`

## Prior breaker history

E1: DK vs GEN Game 2 DK +10.5 was voided for a fight during the decision/entry window; state and price were not synchronized.

E2: DK vs GEN Game 3 GEN +9.5 was audit-invalidated because mandatory DIM/TAM/CAS fields were omitted from the underdog +kills gate signature. Historical prediction result remains Loss / -0.25u shadow / 0u actual.

Neither historical failure is erased by E3. E3 is a fresh prospective lock with the mechanical interlock active.