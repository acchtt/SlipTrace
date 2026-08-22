# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-23-E1-0205-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-23 02:05 UTC+7`  
**Default expiry:** `2026-08-24 00:00 UTC+7`  
**Authority commit:** `fa9d8d1670d6156103ff6ae61040f7c767323454`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

After reviewing the FNC–SHFT / SK–MKOI session, the user explicitly instructed **“Adjust accordingly.”** on 2026-08-23 UTC+7.

That instruction authorizes:

1. the narrow in-place v0.3.58 DOVC/LAC enforcement amendment;
2. a new Session Authority Lock epoch for the 2026-08-23 slate.

This is an explicit user-authorized relock, not a silent outcome-driven mutation. Historical TAKEs, results and P/L remain unchanged.

## Frozen authority

All model-certified analysis in this epoch uses frozen authority commit:

`fa9d8d1670d6156103ff6ae61040f7c767323454`

Canonical model remains **LoL v0.3.58**. v0.3.59/v0.3.60 remain retired.

The frozen authority includes:

- `models/lol/reviews/LEC_FNC_SHFT_SK_MKOI_SESSION_REVIEW_2026-08-23.md`
- `models/lol/procedures/LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`
- updated `models/lol/CURRENT_MODEL.md` manifest and load order.

## Mechanical pre-TAKE interlock

The required order remains:

`evidence -> PRE_TAKE_CERT build -> mechanical validation -> visible verdict -> Airtable write -> exact verification`

Any omitted, implied, unresolved or failed required field forces HOLD/PASS.

A material state or executable-price change before verdict/entry expires the certificate and requires a full rebuild from a fresh synchronized frame.

## New active hardening

### Duration Over — DOVC

Every Duration Over candidate must explicitly pass:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

`ABSENT CONVERSION`, theoretical waveclear without demonstrated denial, quiet elapsed time, low kills, 0-0 towers, close gold or neutral objectives cannot certify an Over.

### Underdog +kills — LAC

After complete DIM + draft-only UDKC `STABLE`, live preservation and UCS, underdog +kills also requires `LAC = PASS`.

LAC must be based on demonstrated current-regime suppression of repeated favorite net kill-margin expansion. A kill lead, one dragon, small gold edge, 0-0 towers, a large +kills buffer, theoretical scaling/waveclear/peel or attractive odds cannot substitute.

## Preserved controls

All retained v0.3.58 controls remain active, including:

- DIM/TAM/OSG/DAU/SLI/FNF/CAS/ETS/AFP;
- UDKC / FER / PDC / PST / ARI / KPA / KMS / RLD / False-Stable;
- UCS and exact signed-margin/NKB handling;
- FFD/RNE/Structure Substitution/safe-concede for favorite -kills;
- FRP for Total Kills Under;
- retained Total Kills Over recurrence/contact framework;
- FCR for Duration Under;
- Lead Decomposition / CFC / neutral-fight stress for Live ML;
- LRO when opposing a CLEAR/STRONG draft prior;
- SMR for repeated failed mechanisms;
- one TAKE per family per map;
- minimum odds `1.60`;
- shadow-only `0.25u`, actual `0u`;
- synchronized state/price enforcement;
- verdict-first Airtable logging and exact verification.

No broad additional conservatism is authorized for Live ML.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `fa9d8d1670d6156103ff6ae61040f7c767323454`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. load the latest live handoff last;
7. verify PRE_TAKE_CERT, DOVC and LAC requirements are present before issuing any applicable TAKE.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
