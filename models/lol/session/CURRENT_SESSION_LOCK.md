# Current LoL Session Lock

**Lock ID:** `LOL-2026-08-23-E6-BFX-NS-1804-UTC7`  
**Status:** `ACTIVE`  
**Effective:** `2026-08-23 18:04 UTC+7`  
**Scope:** `LCK — BNK FEARX vs Nongshim RedForce series`  
**Default expiry:** `BFX–NS series completion or explicit relock; hard stop 2026-08-24 00:00 UTC+7`  
**Authority commit:** `7fbaf380b78b595c6b36a5a6ab5e6e9101c5760b`  
**Active analytical model:** `LoL v0.3.58`  
**Circuit breaker:** `CLEAR — reset only after validator repair + explicit user authorization`  
**Actual exposure policy:** `0u`  
**Default shadow stake:** `0.25u`

## Authorization

On 2026-08-23 at 18:04 UTC+7 the user explicitly instructed **“Do it now”** after asking why mandatory model rules kept being skipped.

This instruction explicitly authorizes an immediate execution-hardening authority epoch and relock of the still-active BFX–NS series.

The prior E5 authority epoch is superseded. The historical NS +5.5 kills @1.869 TAKE remains a real historical loss and is not rewritten.

The E5 procedural breaker is treated as having tripped when review established that mandatory KMS/RLD/live-preservation/LAC enforcement had been skipped/compressed before that TAKE. E6 clears the breaker only because:

1. the execution defect has been documented;
2. a mechanical PRE_TAKE_CERT validator has been added;
3. the user explicitly authorized immediate repair/relock.

This is an in-place **execution-governance hardening** of canonical LoL v0.3.58. It does not create v0.3.59/v0.3.60 and does not add a new predictive betting edge.

## Frozen authority

All model-certified analysis for the remainder of BFX vs NS uses frozen authority commit:

`7fbaf380b78b595c6b36a5a6ab5e6e9101c5760b`

Canonical model remains **LoL v0.3.58**. v0.3.59/v0.3.60 remain retired.

The frozen authority includes all prior v0.3.58 controls plus:

- DOVC / LAC hardening;
- Live ML draft-prior degradation / regime override;
- **mandatory mechanical PRE_TAKE_CERT validator:**
  `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`;
- reference review:
  `models/lol/reviews/BFX_NS_G1_PRE_TAKE_CERT_EXECUTION_FAILURE_REVIEW_2026-08-23.md`.

No default-branch analytical edit made after this authority commit may affect this match unless the user explicitly authorizes another relock.

## Protected TAKE interlock

The visible word `TAKE` is now a protected execution token.

Required order:

`evidence -> applicability resolver -> PRE_TAKE_CERT build -> contradiction scan -> mechanical validation -> final synchronized state/price recheck -> visible verdict -> Airtable write -> exact verification`

A candidate may reach `TAKE` only when the mechanical validator returns:

- every applicable required field explicitly resolved;
- `FAILED_FIELDS = []`;
- `UNRESOLVED_FIELDS = []`;
- `CONTRADICTIONS = []`;
- `CERT_STATE = PASS`.

Any omitted, implied, narrative-only, unresolved, contradictory, or failed mandatory field forces HOLD/PASS.

A material state or executable-price change before verdict expires the certificate and requires a full rebuild from fresh synchronized evidence.

## Match execution controls

- Shadow only: `0.25u`; actual exposure `0u`.
- Minimum accepted odds: `1.60`.
- Pregame/immediate-postdraft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK require at least two usable synchronized live snapshots.
- One TAKE per market family per map: ML / Kill Handicap / Total Kills / Duration.
- Current synchronized sportsbook state/price controls; stale or greyed markets are non-executable.
- Position-blind reassessment is mandatory.
- Exact signed kill-margin arithmetic is mandatory.
- HOLD/PASS creates no Position; a qualified TAKE creates the exact shadow Position only after the visible verdict and must then be verified in Airtable.
- No price, cushion size, arithmetic hurdle, prior win/loss, or narrative confidence may override a failed mandatory mechanism gate.

### Live ML

The validator must resolve all applicable ML controls including:

`2SNAP | LEAD_DECOMPOSITION | DPS | CFC_CURRENT | NEUTRAL_FIGHT_STRESS | DRP (if applicable) | LRO (if applicable) | PRICE`

Ordinary Live ML remains two-snapshot eligible when aligned with a CLEAR/STRONG draft prior or when the original draft edge was SLIGHT/EVEN/UNCLEAR.

A Live ML TAKE against an original CLEAR/STRONG draft prior requires `LRO = PASS` with the complete contrary-draft regime-override signature.

### Underdog +kills

The validator must resolve the full sequence without compression:

`2SNAP | DIM | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_PRESERVATION | LIVE_RLD | LAC | UCS | SCNE | SIGNED_MARGIN | EXACT_NKB | PRICE`

`LIVE_RLD` is a mechanical split of the already-existing RLD requirement and must explicitly inspect current economy/levels/control distribution.

Hard contradiction rule:

> Carry-centered favorite economy plus cleaner grouped control cannot coexist with `LIVE_PRESERVATION = PASS` or `LAC = PASS` unless strong observed live suppression of those empowered favorite routes is demonstrated.

Stable kill margin, 0–0 towers, a large +kills buffer, theoretical scaling/waveclear/peel, or correct NKB arithmetic cannot override failed KMS/RLD/LAC/UCS.

### Favorite negative kill handicap

Resolve exact signed margin, remaining net-kill expansion burden, current continuation/control state, and all active family gates before price.

### Duration Over

Requires complete **DOVC**:

`CONVERSION_CLASS | POSITIVE_CLOCK_MECH_1 | POSITIVE_CLOCK_MECH_2 | FAILED_CONVERSION_OR_EQUIVALENT | OBSERVED_STALL_EVIDENCE_ID | CLOCK_CAUSALITY | STRUCTURE_SUBSTITUTION | SHORTEST_CASCADE_TEST | SURVIVAL_HORIZON | PRICE`

`ABSENT CONVERSION`, low kills, 0–0 towers, close gold, neutral objectives, quiet elapsed time, or theoretical waveclear without demonstrated denial are insufficient.

### Total Kills / Duration Under

- Total Kills Under requires `FRP = PASS`; passive quiet is insufficient.
- Total Kills Over retains recurrence/contact-pressure requirements.
- Duration Under retains FCR and shortest-close-route stress.

## Circuit breaker

Trigger `TAKE SUSPENDED — PROCEDURAL CIRCUIT BREAKER` immediately for any execution failure including:

- visible TAKE without validator PASS;
- skipped mandatory field;
- narrative-only implied PASS;
- ignored contradiction;
- stale-certificate reuse;
- wrong authority/model;
- draft theory used as live proof or live evidence used as draft proof;
- price/arithmetic overriding a failed gate.

No further TAKE is permitted under that authority epoch until the defect is repaired and an explicitly authorized relock/reset clears the breaker.

An ordinary valid betting loss does not itself trigger the breaker.

## New-chat requirement

While this lock is active, a future chat must:

1. fetch default-branch `models/lol/CURRENT_MODEL.md` first;
2. fetch `models/lol/procedures/LOL_SESSION_BOOTSTRAP.md`;
3. fetch this lock;
4. re-fetch `CURRENT_MODEL.md` at authority commit `7fbaf380b78b595c6b36a5a6ab5e6e9101c5760b`;
5. load the complete stack in the locked CURRENT_MODEL order from that same commit;
6. additionally load `models/lol/procedures/LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` from the same commit as a **lock-specific mandatory execution interlock**, even if an older CURRENT_MODEL load-order listing does not yet enumerate it;
7. load the latest live handoff last;
8. verify the complete applicability manifest and mechanical PRE_TAKE_CERT before any visible TAKE.

If authority cannot be loaded or hierarchy mismatches, use:

`MODEL LOCK MISMATCH — HOLD`
