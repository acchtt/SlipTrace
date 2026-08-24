# PRE_TAKE_CERT Kill Handicap Margin Extension — 2026-08-25

**Status:** ACTIVE CANONICAL v0.3.58 EXECUTION INTERLOCK when included by the active Session Authority Lock  
**Effective:** 2026-08-25 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Scope:** Kill Handicap family only  
**Parent procedure:** `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`

This file mechanically extends `LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` for Kill Handicap only.

Where this file is stricter, it supersedes the older validator's Sections 5.2 and 5.3. All non-KH validator rules remain unchanged.

---

## 1. Applicability

For every Kill Handicap candidate, positive or negative, the PRE_TAKE applicability resolver must add a common parent manifest **before** the sign-specific manifest.

Required common parent fields:

`2SNAP`

`KH_MARGIN_CERT`

`FAVORITE`

`CURRENT_SIGNED_MARGIN`

`MAP_WIN_RANGE`

`TOTAL_KILLS_RANGE`

`FAIR_CENTRAL_MARGIN`

`FINAL_MARGIN_BINS`

`KCV`

`RFI`

`STRUCTURE_MODE`

`WIDE_MARGIN_HAZARD`

`DIST_LOCKED_BEFORE_LINE`

`BOTH_SIDES_PRICED_OR_JUSTIFIED_NA`

`WMS`

`SIGN_SELECTED_AFTER_DIST`

`SELECTED_SIDE_COVER_RANGE`

`SELECTED_SIDE_LOWER_BOUND`

`SELECTED_SIDE_BREAK_EVEN`

`RETAINED_PHASE_BUFFER`

`EDGE_AFTER_BUFFER`

Every categorical field must resolve to an eligible terminal value. Every numeric/range field must be populated concretely enough to validate the selected line.

Missing or narrative-only margin bins, cover range, break-even, buffer or lower-bound edge => `CERT_STATE = FAIL`.

---

## 2. Positive Kill Handicap extension

After the common parent manifest passes, a contemplated underdog +kills TAKE must additionally resolve the complete active positive-handicap sequence:

`DIM`

`PDRL/N-A`

`TAM`

`CAS`

`UDKC_STABLE`

`KPA`

`KMS`

`RLD_DRAFT`

`FALSE_STABLE_INACTIVE`

`LIVE_PRESERVATION`

`LIVE_RLD`

`LAC`

`LAC_PRESSURE_CLASS`

`UCS`

`SCNE`

`SIGNED_MARGIN`

`FAILURE_THRESHOLD`

`EXACT_NKB`

`DOG_TAIL_RECONCILED`

`PRICE`.

`LAC_PRESSURE_CLASS` must be one of:

- `EXPANSION_OPPORTUNITY_SUPPRESSED` — eligible positive LAC evidence;
- `NO_EXPANSION_OPPORTUNITY` — neutral, cannot establish LAC;
- `EXPANSION_OPPORTUNITY_CONVERTED` — negative evidence;
- `UNRESOLVED` — fail closed.

A flat margin classified `NO_EXPANSION_OPPORTUNITY` cannot coexist with `LAC=PASS` unless separate representative pressure-adjusted suppression evidence exists and is explicitly identified.

`DOG_TAIL_RECONCILED=PASS` means the positive-side mechanisms are consistent with the locked distribution. If mechanism evidence requires a material distribution change, the entire KH_MARGIN_CERT expires and must be rebuilt before either side is re-priced.

---

## 3. Favorite Negative Kill Handicap extension

After the common parent manifest passes, a contemplated favorite -kills TAKE must additionally resolve:

`SIGNED_MARGIN`

`COVER_THRESHOLD`

`RNE`

`FFD`

`KCV`

`RFI`

`ROLE_WEIGHTED_LEAD_QUALITY`

`REMAINING_FORCED_FIGHTS`

`STRUCTURE_SUBSTITUTION`

`SAFE_CONCEDE_TEST`

`CONTINUATION_CLEANUP_ACCESS`

`retained NKB/RFI/KCV controls`

`FAV_TAIL_RECONCILED`

`PRICE`.

`FAV_TAIL_RECONCILED=PASS` means the favorite-side mechanisms are consistent with the locked distribution. If mechanism evidence requires a material distribution change, rebuild the full KH_MARGIN_CERT and price both sides again.

---

## 4. Mechanical sign-neutrality checks

The validator must fail the KH certificate if any of the following is true:

1. `DIST_LOCKED_BEFORE_LINE != PASS`;
2. `SIGN_SELECTED_AFTER_DIST != PASS`;
3. the analyst used separate incompatible margin distributions for +H and -H;
4. the selected side's lower-bound cover probability does not clear break-even plus the retained phase buffer;
5. favorite -H mechanism failure was used as positive evidence for dog +H;
6. dog +H mechanism failure was used as positive evidence for favorite -H;
7. a large `NKB` / `RNE` was treated as probability evidence;
8. a materially probable favorite serial cascade was omitted from `WMS` or `FINAL_MARGIN_BINS`;
9. `NO_EXPANSION_OPPORTUNITY` was treated as demonstrated dog suppression;
10. the displayed handicap size was used to construct or upgrade the distribution;
11. the preliminary sign was selected because its mechanism certificate was easier to complete rather than because the common distribution + price produced the best edge.

Any one condition => `CONTRADICTIONS` non-empty => `CERT_STATE = FAIL`.

---

## 5. Directional calibration state

While the 2026-08-25 directional review remains uncleared:

`KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

The PRE_TAKE_CERT must explicitly persist:

`KH_DIR_CAL=ACTIVE`

and cannot compress or omit the common margin manifest.

This state does not require or prefer a favorite bet. It enforces process neutrality only.

---

## 6. Compact gate signature

A qualifying Kill Handicap TAKE must persist enough of the parent certificate to prove the sign-neutral sequence occurred.

Minimum compact parent block:

`KHMC[DIST=P;BOTH=P/N-A;WMS=P;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

Then append the existing sign-specific `GATE_SIG[...]` fields.

If the persisted signature omits the parent block, treat the TAKE as a mechanical execution failure under the normal circuit-breaker rules.

---

## 7. Protected-token effect

The word `TAKE` remains protected.

For Kill Handicap, the execution order is now:

`evidence -> KH_MARGIN_CERT -> both-side pricing -> WMS -> sign selection -> sign-specific mechanisms -> contradiction scan -> mechanical validator -> final synchronized recheck -> visible verdict`.

Any shortcut forces HOLD/PASS.
