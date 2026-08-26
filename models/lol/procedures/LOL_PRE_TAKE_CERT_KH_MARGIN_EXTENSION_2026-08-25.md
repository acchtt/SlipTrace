# PRE_TAKE_CERT Kill Handicap Margin Extension — 2026-08-25

**Status:** ACTIVE CANONICAL v0.3.58 EXECUTION INTERLOCK when included by the active Session Authority Lock  
**Effective:** 2026-08-25 UTC+7  
**Recalibrated:** 2026-08-26 ~17:54 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Scope:** Kill Handicap family only  
**Parent procedure:** `models/lol/procedures/LOL_KILL_HANDICAP_SIDE_NEUTRAL_MARGIN_ENGINE_2026-08-25.md`  
**Recalibration authorization:** user instruction “Recalibrate now”

This file mechanically extends `LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md` for Kill Handicap only. Where stricter, it supersedes the older validator's KH manifests. All non-KH validator rules remain unchanged.

---

## 1. Common KH parent manifest

For every Kill Handicap candidate, positive or negative, PRE_TAKE must add this common parent manifest before sign-specific validation:

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

`FAVORITE_EXPANSION_MECHANISM`

`FAVORITE_MECH_REPEATABILITY`

`FORCED_CYCLE_DENSITY`

`WIDE_MARGIN_HAZARD`

`DIST_LOCKED_BEFORE_LINE`

`BOTH_SIDES_PRICED_OR_JUSTIFIED_NA`

`WMS_ONE_CYCLE_NET_MARGIN_RANGE`

`WMS_TWO_CYCLE_NET_MARGIN_RANGE`

`WMS_PROBABILITY_CLASS`

`WMS_INTEGRATED_IN_DIST`

`THRESHOLD_CROSSABLE_ONE_CYCLE`

`THRESHOLD_CROSSABLE_TWO_CYCLE`

`SIGN_SELECTED_AFTER_DIST`

`SELECTED_SIDE_COVER_RANGE`

`SELECTED_SIDE_LOWER_BOUND`

`SELECTED_SIDE_BREAK_EVEN`

`APPLICABLE_BUFFER`

`EDGE_AFTER_BUFFER`.

Every categorical field must resolve to an eligible terminal value. Every numeric/range field must be concrete enough to validate the selected line.

Missing or narrative-only margin bins, WMS ranges, cover range, break-even, applicable buffer or lower-bound edge => `CERT_STATE = FAIL`.

---

## 2. Directional calibration state

The following are active prospectively under an authority commit containing this recalibration:

`KH_DIRECTIONAL_CALIBRATION = ACTIVE`

`KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

PRE_TAKE must persist:

`KH_DIR_CAL=ACTIVE`

`KH_DOG_PROBATION=ACTIVE`.

These states are execution controls, not a favorite quota.

---

## 3. Positive Kill Handicap manifest during dog probation

After the common parent manifest passes, a contemplated underdog +kills TAKE must resolve the complete retained positive-handicap sequence:

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

`DOG_CUSHION_CLASS`

`FAVORITE_EXPANSION_MECHANISM`

`UNDERDOG_DIRECT_ANSWER`

`MECHANISM_MATCH`

`MATCHED_SUPPRESSION_EVIDENCE_ID_1`

`MATCHED_SUPPRESSION_EVIDENCE_ID_2`

`DOG_FAILURE_THRESHOLD_CROSSABLE_ONE_CYCLE`

`DOG_FAILURE_THRESHOLD_CROSSABLE_TWO_CYCLE`

`DOG_CYCLE_CROSSABILITY`

`DOG_BASE_BUFFER`

`DOG_CALIBRATION_SURCHARGE_PP`

`DOG_APPLICABLE_BUFFER`

`DOG_TAIL_RECONCILED`

`PRICE`.

### 3.1 Eligible terminal requirements

While `KH_DOG_DIRECTIONAL_PROBATION=ACTIVE`:

- `DOG_CUSHION_CLASS` must equal `LARGE`;
- `MECHANISM_MATCH` must equal `PASS`;
- both matched suppression evidence IDs must be present and represent distinct live expansion-opportunity windows;
- both windows must be pressure-classified `EXPANSION_OPPORTUNITY_SUPPRESSED` or otherwise explicitly prove mechanism-matched suppression;
- the older single-event LAC exception is not eligible;
- `DOG_CYCLE_CROSSABILITY` must equal `PASS`;
- if an ordinary MATERIAL/HIGH WMS branch reaches the dog failure threshold inside one or two compulsory cycles, `DOG_CYCLE_CROSSABILITY=FAIL`;
- `DOG_CALIBRATION_SURCHARGE_PP` must equal `5`;
- `DOG_APPLICABLE_BUFFER = DOG_BASE_BUFFER + 0.05` when probabilities are represented as 0–1, or `+5 percentage points` when represented as percentages;
- selected dog lower-bound cover probability must clear break-even by the full `DOG_APPLICABLE_BUFFER`;
- `DOG_TAIL_RECONCILED=PASS` is mandatory.

`INSUFFICIENT`, `THIN`, or `MATERIAL` cushion during probation => `CERT_STATE=FAIL`.

### 3.2 Mechanism matching

`MECHANISM_MATCH=PASS` requires the underdog answer to directly suppress the favorite's actual repeatable margin-expansion mechanism.

Generic labels are invalid. Examples of invalid substitution:

- counter-engage used as proof against pre-contact poke/pick without observed denial;
- waveclear used as proof against jungle/support pick access;
- side pressure used as proof against objective-choke cleanup;
- scaling used as proof against current target access.

The following cannot satisfy matched suppression by themselves:

- 0-0 towers;
- quiet elapsed time;
- grubs;
- theoretical peel/waveclear/disengage;
- current +H size;
- NKB;
- stable gold without representative favorite pressure.

### 3.3 LAC pressure classes

`LAC_PRESSURE_CLASS` must be one of:

- `EXPANSION_OPPORTUNITY_SUPPRESSED` — positive evidence;
- `NO_EXPANSION_OPPORTUNITY` — neutral;
- `EXPANSION_OPPORTUNITY_CONVERTED` — negative;
- `UNRESOLVED` — fail closed.

During probation, two distinct positive matched windows are mandatory.

---

## 4. Favorite Negative Kill Handicap manifest

After the common parent manifest passes, a contemplated favorite -kills TAKE must resolve:

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

`COVER_BEFORE_CLOSE`

`retained NKB/RFI/KCV controls`

`FAV_TAIL_RECONCILED`

`PRICE`.

`COVER_BEFORE_CLOSE` must be `PASS` for a TAKE and means the favorite can plausibly realize the required margin before terminal structure control causes safe concession or removes fight inventory.

A favorite -H candidate keeps the normal retained phase/uncertainty buffer. The dog +5pp surcharge does not apply.

`COVER_BEFORE_CLOSE` is not a shortcut: FFD/KCV/RFI/role-weighted lead quality, WMS integration, pricing edge and `FAV_TAIL_RECONCILED=PASS` remain mandatory.

---

## 5. Mechanical sign-neutrality and recalibration contradiction scan

The validator must fail the KH certificate if any of the following is true:

1. `DIST_LOCKED_BEFORE_LINE != PASS`;
2. `SIGN_SELECTED_AFTER_DIST != PASS`;
3. separate incompatible margin distributions were used for +H and -H;
4. selected-side lower-bound cover probability does not clear break-even plus `APPLICABLE_BUFFER`;
5. favorite -H mechanism failure was used as positive evidence for dog +H;
6. dog +H mechanism failure was used as positive evidence for favorite -H;
7. NKB/RNE magnitude was treated as probability evidence;
8. a materially probable serial favorite cascade was omitted from WMS or `FINAL_MARGIN_BINS`;
9. `NO_EXPANSION_OPPORTUNITY` was treated as demonstrated dog suppression;
10. displayed handicap size was used to construct or upgrade the distribution;
11. the sign was selected because its mechanism certificate was easier to complete;
12. WMS was labeled LOW despite repeatable favorite mechanism + compulsory contact + no matched suppression, without explicit contrary evidence;
13. selected side is dog and `DOG_CUSHION_CLASS != LARGE` while probation is active;
14. selected side is dog and either matched suppression evidence ID is missing while probation is active;
15. selected side is dog and `MECHANISM_MATCH != PASS`;
16. selected side is dog and an ordinary MATERIAL/HIGH one- or two-cycle WMS branch crosses the failure threshold;
17. selected side is dog and the +5pp calibration surcharge is absent or miscomputed;
18. selected side is favorite and `COVER_BEFORE_CLOSE` is omitted/unresolved;
19. favorite -H was rejected or downgraded solely due late safe-concede narrative without adjudicating `COVER_BEFORE_CLOSE`.

Any one condition => `CONTRADICTIONS` non-empty => `CERT_STATE = FAIL`.

---

## 6. Compact gate signatures

Every qualifying KH TAKE must persist enough of the parent certificate to prove sign-neutral sequencing.

Minimum common block:

`KHMC[DIST=P;BOTH=P/N-A;WMS1=<range>;WMS2=<range>;WMSP=<class>;MECH=<id>;SIGN_AFTER_DIST=P;LB=<x>;BE=<y>;BUF=<z>;EDGE=P;DIRCAL=A]`

For dog +H during probation append at minimum:

`DOGCAL[PROB=A;CUSHION=LARGE;MATCH=P;SUP1=<id>;SUP2=<id>;CYCLE=P;SURCHARGE=5pp;TAIL=P]`

For favorite -H append at minimum:

`FAVCAL[COVER_BEFORE_CLOSE=P;TAIL=P]`.

If required calibration blocks are omitted, treat the TAKE as a mechanical execution failure under the circuit-breaker rules.

---

## 7. Protected-token effect

The word `TAKE` remains protected.

For Kill Handicap, execution order is:

`evidence -> KH_MARGIN_CERT -> both-side pricing -> WMS one/two-cycle stress -> sign selection -> sign-specific mechanisms -> probation calibration when dog -> contradiction scan -> mechanical validator -> final synchronized recheck -> visible verdict`.

Any shortcut forces HOLD/PASS.

---

## 8. Anti-overfit and clearing

The recent 4-12 settled dog sample is audit evidence for execution recalibration, not a direct probability prior. Do not force favorite selections or a directional quota.

`KH_DOG_DIRECTIONAL_PROBATION` may be cleared only by a future explicit aggregate KH review after a meaningful prospective sample. It does not auto-clear from one win, one favorite selection or a short streak.
