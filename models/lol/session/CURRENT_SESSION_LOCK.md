# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-23-E3-HLE-T1-1453-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-23 14:53 UTC+7`  
**Scope:** `LCK — Hanwha Life Esports vs T1 series`  
**Default expiry:** `HLE–T1 series completion or explicit relock; hard stop 2026-08-24 00:00 UTC+7`  
**Authority commit:** `fa9d8d1670d6156103ff6ae61040f7c767323454`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

On 2026-08-23 at 14:53 UTC+7 the user explicitly instructed **“Relock lck match hle vs t1.”**

This supersedes the prior TT–LGD match-scope lock and freezes the HLE vs T1 LCK series under the already-canonical 2026-08-23 v0.3.58 authority. This is a match-scope authority relock only; it does **not** authorize analytical mutation, outcome-driven patching, or a model-version change.

Historical TAKEs, results and P/L remain unchanged.

## Frozen authority

All model-certified analysis for HLE vs T1 uses frozen authority commit:

`fa9d8d1670d6156103ff6ae61040f7c767323454`

Canonical model remains **LoL v0.3.58**. v0.3.59/v0.3.60 remain retired.

The frozen authority includes the 2026-08-23 DOVC/LAC hardening plus all retained v0.3.58 procedures and the Live ML draft-prior degradation / regime-override procedure.

No default-branch analytical edit made after the authority commit may affect this match unless the user explicitly authorizes another relock.

## Mechanical pre-TAKE interlock

Required order:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable write -> exact verification`

Any omitted, implied, unresolved or failed required field forces HOLD/PASS.

A material state or executable-price change before verdict/entry expires the certificate and requires a full rebuild from a fresh synchronized frame.

## Match execution controls

- Shadow only: `0.25u`; actual exposure `0u`.
- Minimum accepted odds: `1.60`.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots.
- One TAKE per market family per map: ML / Kill Handicap / Total Kills / Duration.
- Current synchronized sportsbook state/price controls; stale or greyed markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- Every visible TAKE requires a complete valid PRE_TAKE_CERT before the word TAKE is emitted.
- HOLD/PASS creates no Position; a qualified TAKE creates the exact shadow Position only after the visible verdict and must then be verified in Airtable.

### Live ML

Retain Lead Decomposition, `DPS — Draft Prior State`, `CFC_CURRENT`, current neutral-fight stress and `LRO` where applicable.

Ordinary Live ML remains two-snapshot eligible when aligned with a CLEAR/STRONG draft prior or when the original draft edge was SLIGHT/EVEN/UNCLEAR.

A Live ML TAKE against an original CLEAR/STRONG draft prior requires `LRO = PASS` with the complete contrary-draft regime-override signature. Draft prior may not remain a hidden permanent veto once the strict LRO path is actually satisfied.

### Underdog +kills

Requires complete DIM + draft-only UDKC + KPA/KMS + RLD + False-Stable controls + live preservation + UCS + exact signed-margin/NKB + **LAC = PASS**.

A large numerical cushion, small gold/kill/objective lead, theoretical scaling/waveclear/peel, or attractive price does not by itself prove anti-cascade resistance.

### Duration Over

Requires complete **DOVC**:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

`ABSENT CONVERSION`, low kills, 0-0 towers, close gold, neutral objectives, quiet elapsed time, or theoretical waveclear without demonstrated denial are insufficient.

### Total Kills / Duration Under

- Total Kills Under requires `FRP = PASS`; passive quiet is insufficient.
- Total Kills Over retains recurrence/contact-pressure requirements.
- Duration Under retains FCR and shortest-close-route stress.

## Circuit breaker

Circuit breaker is **CLEAR** at relock creation.

Trigger `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER` for an execution failure such as missing/failed PRE_TAKE_CERT, stale-certificate reuse, wrong authority/model, skipped mandatory family gate, or a TAKE issued under an unresolved hard requirement.

An ordinary valid betting loss does not trigger the circuit breaker and does not authorize a mid-match model change.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `fa9d8d1670d6156103ff6ae61040f7c767323454`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. load the latest live handoff last;
7. verify all applicable PRE_TAKE_CERT / DOVC / LAC / LRO requirements before any TAKE.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
