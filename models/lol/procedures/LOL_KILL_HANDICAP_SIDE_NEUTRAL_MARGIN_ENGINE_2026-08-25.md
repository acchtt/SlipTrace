# LoL Kill Handicap Side-Neutral Margin Engine — 2026-08-25

**Status:** ACTIVE CANONICAL v0.3.58 IN-PLACE AMENDMENT when included by the active Session Authority Lock  
**Effective:** 2026-08-25 UTC+7  
**Recalibrated:** 2026-08-26 ~17:54 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Scope:** every live Kill Handicap candidate, both positive and negative sides  
**Original authorization:** user instruction “Lock this slate. And adjust the model with your recommendations.”  
**Immediate recalibration authorization:** user instruction “Recalibrate now”  
**Reference reviews:** `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_AND_MARGIN_ENGINE_REVIEW_2026-08-25.md` and `models/lol/reviews/KH_DIRECTIONAL_RECALIBRATION_2026-08-26.md`

This procedure restores the retained v0.3.44 distribution-first Kill Handicap hierarchy as the parent gate and makes later positive/negative handicap mechanisms subordinate validators of the same side-neutral final-margin distribution.

It does not create a favorite quota, does not invert signs mechanically, and does not create a new analytical model version.

---

## 1. Parent rule — predict margin before choosing sign

Before evaluating either displayed Kill Handicap side, construct one **KH_MARGIN_CERT — Kill Handicap Margin Certificate**.

Mandatory order:

`STATE + MKT + TEAM`

`-> KH_MARGIN_CERT`

`-> price both sides from the same locked distribution`

`-> WMS one-cycle + two-cycle stress`

`-> preliminary best side / PASS`

`-> selected-side mechanism validator`

`-> retained uncertainty / calibration buffer`

`-> PRE_TAKE_CERT`

`-> TAKE / HOLD / PASS`

The displayed +H/-H line may not determine the projected distribution. If sign was selected before the distribution was locked:

`SIGN_SELECTED_AFTER_DIST = FAIL -> HOLD/PASS`.

---

## 2. Mandatory KH_MARGIN_CERT

Before using sportsbook handicap size or price as evidence, resolve:

`FAVORITE`

`CURRENT_SIGNED_MARGIN`

`FAVORITE_MAP_WIN_RANGE`

`PROJECTED_TOTAL_KILLS_RANGE`

`FAIR_CENTRAL_FINAL_MARGIN`

`FINAL_MARGIN_BINS`

`CONDITIONAL_FAVORITE_WIN_MARGIN_SHAPE`

`UNDERDOG_WIN_OR_NONPOSITIVE_MARGIN_BRANCH`

`KCV`

`RFI`

`STRUCTURE_MODE`

`FAVORITE_EXPANSION_MECHANISM`

`FAVORITE_MECH_REPEATABILITY = LOW / MATERIAL / HIGH`

`FORCED_CYCLE_DENSITY`

`WIDE_MARGIN_HAZARD`

`UNCERTAINTY_WIDTH`

`DIST_LOCKED_BEFORE_LINE = PASS/FAIL`.

### Required final-margin representation

At minimum retain:

- `M <= 0`
- `M = +1 to +3`
- `M = +4 to +6`
- `M = +7 to +9`
- `M = +10 to +14`
- `M >= +15`

where `M = favorite final kills - underdog final kills`.

Refine bins when the displayed line requires more precision. Probabilities must sum to approximately 100% and remain coherent with map-win probability, total-kill expectation, synchronized live state, team-strength prior, draft interaction, economy concentration, objective schedule, forced-fight density and conversion architecture.

If the distribution is under-specified or internally inconsistent, verdict is HOLD/PASS.

---

## 3. Both-side pricing is mechanical

After `KH_MARGIN_CERT` is locked, and only then, compare the executable handicap prices.

When both sides are available, record:

`DOG_LINE | DOG_ODDS | DOG_BREAK_EVEN | DOG_COVER_RANGE`

`FAV_LINE | FAV_ODDS | FAV_BREAK_EVEN | FAV_COVER_RANGE`

`RETAINED_PHASE_BUFFER`

`DOG_EDGE_AFTER_BUFFER`

`FAV_EDGE_AFTER_BUFFER`

`PRELIMINARY_BEST_SIDE = DOG / FAV / PASS`

`BOTH_SIDES_PRICED = PASS/FAIL`.

The same frozen margin distribution must generate both cover estimates. If only one side is executable, `BOTH_SIDES_PRICED=N/A` is allowed only because the other executable price is genuinely unavailable; distribution neutrality remains mandatory.

For half-kill lines:

- `P(dog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

For whole-number lines, account explicitly for push rules.

A TAKE requires the lower bound of the selected side's cover range to clear break-even plus the applicable retained buffer.

---

## 4. Non-complementarity of value certification

Hard rules:

- favorite -H FAIL gives zero positive evidence for dog +H;
- dog +H FAIL gives zero positive evidence for favorite -H;
- inability to prove favorite FFD/RNE never creates dog value;
- inability to prove dog KMS/LAC/UCS never creates favorite value;
- both sides may correctly be HOLD/PASS.

No sign inversion shortcut is permitted.

---

## 5. WMS — one-cycle and two-cycle margin stress

Run **WMS — Wide-Margin Stress** before either side is selected for final certification.

Construct the strongest ordinary realistic favorite expansion sequence supported by current evidence:

`next compulsory setup -> first contact -> ordinary cleanup/continuation -> objective/structure transition -> deeper vision/map compression -> next forced entry -> base-defense/terminal exposure where realistic`.

WMS must identify the favorite's actual repeatable margin mechanism, such as hard engage, pre-contact poke/pick, dive/backline access, objective-choke control, siege, side-lane collapse, or another evidence-grounded route. Generic “favorite stronger” language is invalid.

Resolve:

`WMS_BRANCH_DESCRIPTION`

`WMS_ONE_CYCLE_NET_MARGIN_RANGE`

`WMS_TWO_CYCLE_NET_MARGIN_RANGE`

`WMS_PROBABILITY_CLASS = LOW / MATERIAL / HIGH`

`WMS_INTEGRATED_IN_DIST = PASS/FAIL`.

A materially probable serial favorite branch omitted or materially underweighted in `FINAL_MARGIN_BINS` fails the certificate.

### WMS probability floor during directional calibration

If all are true:

1. the favorite has a repeatable evidence-grounded margin-expansion mechanism;
2. current role/economy/objective positioning provides realistic future compulsory contact;
3. the underdog has not demonstrated mechanism-matched suppression of that route;

then WMS may not be labeled `LOW` merely because towers are low, current kill margin is small, or the displayed dog cushion is large. Default classification is at least `MATERIAL` unless contrary live evidence is explicitly identified.

---

## 6. NKB/RNE are arithmetic only

For dog +H, calculate exact failure threshold and NKB. For favorite -H, calculate exact cover threshold and RNE/NKB as applicable.

But:

> “favorite needs another +7/+8/+10 net kills” is a hurdle description, not evidence that the hurdle is unlikely.

Kill margins are serially dependent through fight -> objective -> vision -> next fight -> base-defense sequences. NKB, RNE or a visually deep cushion can never establish value by themselves.

Every KH candidate must additionally answer:

`THRESHOLD_CROSSABLE_ONE_CYCLE = YES / NO / UNRESOLVED`

`THRESHOLD_CROSSABLE_TWO_CYCLE = YES / NO / UNRESOLVED`

using the WMS ranges rather than raw arithmetic alone.

---

## 7. Positive-handicap validator — downstream only

If the preliminary best side is underdog +kills, retain every applicable gate:

`2SNAP | DIM | PDRL/N-A | TAM | CAS | UDKC_STABLE | KPA | KMS | RLD_DRAFT | FALSE_STABLE_INACTIVE | LIVE_RLD | LIVE_PRESERVATION | LAC | UCS | SCNE | SIGNED_MARGIN | EXACT_NKB | PRICE`.

These fields may downgrade or invalidate a preliminary dog edge. They may not create an initial dog edge absent from `KH_MARGIN_CERT`.

After completing the dog validator resolve `DOG_TAIL_RECONCILED = PASS/FAIL`. If mechanism analysis requires a material distribution change, discard the old certificate and rebuild the entire `KH_MARGIN_CERT` before repricing either side.

---

## 8. Pressure-adjusted and mechanism-matched LAC

Before counting a flat or slowly moving favorite margin as positive suppression evidence, classify each representative window:

- `NO_EXPANSION_OPPORTUNITY`
- `EXPANSION_OPPORTUNITY_SUPPRESSED`
- `EXPANSION_OPPORTUNITY_CONVERTED`
- `UNRESOLVED`.

Only `EXPANSION_OPPORTUNITY_SUPPRESSED` is positive LAC evidence.

Every contemplated dog +H must explicitly resolve:

`FAVORITE_EXPANSION_MECHANISM`

`UNDERDOG_DIRECT_ANSWER`

`MECHANISM_MATCH = PASS/FAIL`

`MATCHED_SUPPRESSION_EVIDENCE_ID_1`

`MATCHED_SUPPRESSION_EVIDENCE_ID_2 / N-A only when probation inactive`.

`MECHANISM_MATCH=PASS` means the claimed underdog answer directly suppresses the favorite's actual repeatable margin route under live pressure. Generic defensive inventory does not count.

Examples:

- counter-engage does not automatically answer pre-contact poke/pick;
- waveclear does not automatically answer jungle/support pick access;
- side pressure does not automatically answer objective-choke cleanup;
- scaling does not answer current repeatable target access.

The following remain neutral by themselves: passive farming, elapsed time without fight, 0-0 towers, low kill count, stable gold, grubs, theoretical waveclear/peel/disengage, current cushion, NKB, or ordinary uncontested objective trade.

---

## 9. KH_DOG_DIRECTIONAL_PROBATION — ACTIVE

The 2026-08-26 aggregate review found 4 wins and 12 losses among settled underdog +kills selections in the Aug 19–26 guard era, with the ten most recent KH picks all on the positive side. This is sufficient to activate a prospective execution probation without converting the historical sample into a raw probability model.

`KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

While active, a dog +H TAKE is eligible only if all retained rules pass **and** all of the following pass:

### 9.1 Cushion class

`DOG_CUSHION_CLASS` must be `LARGE`.

`INSUFFICIENT`, `THIN`, or `MATERIAL` => HOLD/PASS during probation.

`LARGE` is not defined by absolute H alone. It is conditioned on current signed margin, one-/two-cycle WMS ranges, forced-fight density, structure mode and distribution tail.

### 9.2 Two distinct mechanism-matched suppression windows

The single-event LAC exception is suspended during probation.

Require:

`MATCHED_SUPPRESSION_EVIDENCE_ID_1 = valid`

`MATCHED_SUPPRESSION_EVIDENCE_ID_2 = valid`

from two distinct representative favorite expansion-opportunity windows in the current map.

Both must directly demonstrate the claimed underdog answer against the same favorite expansion mechanism or two independently relevant favorite expansion mechanisms.

### 9.3 Cycle-crossability veto

Resolve:

`DOG_FAILURE_THRESHOLD_CROSSABLE_ONE_CYCLE`

`DOG_FAILURE_THRESHOLD_CROSSABLE_TWO_CYCLE`.

If an ordinary `MATERIAL` or `HIGH` WMS branch reaches or exceeds the dog failure threshold within one or two compulsory cycles:

`DOG_CYCLE_CROSSABILITY = FAIL -> HOLD/PASS`.

This veto cannot be overridden by price, theoretical scaling or NKB size.

### 9.4 Extra dog calibration buffer

During probation:

`DOG_APPLICABLE_BUFFER = RETAINED_PHASE_BUFFER + 5 percentage points`.

The selected dog lower-bound cover probability must clear break-even by this full adjusted buffer.

This is an execution uncertainty surcharge, not a 5-point probability downgrade to the central estimate and not a quota.

### 9.5 No mechanism substitution

`MECHANISM_MATCH=FAIL/UNRESOLVED` => automatic HOLD/PASS.

A dog +H cannot pass by combining several generic defensive tools that do not directly suppress the favorite's actual repeatable expansion route.

---

## 10. Favorite negative-handicap validator — downstream only

If the preliminary best side is favorite -kills, retain:

`2SNAP | SIGNED_MARGIN | COVER_THRESHOLD | RNE | FFD | KCV | RFI | ROLE_WEIGHTED_LEAD_QUALITY | REMAINING_FORCED_FIGHTS | STRUCTURE_SUBSTITUTION | SAFE_CONCEDE_TEST | CONTINUATION_CLEANUP_ACCESS | retained NKB/RFI/KCV controls | PRICE`.

Add:

`COVER_BEFORE_CLOSE = PASS / FAIL / UNRESOLVED`.

This asks whether the favorite can plausibly realize the required kill margin before terminal structure control causes safe concession or ends compulsory fight inventory.

A late safe-concede route is not an automatic favorite -H veto when the required margin can credibly be banked before that phase. Conversely, `COVER_BEFORE_CLOSE=PASS` cannot substitute for FFD/KCV/RFI/role-weighted lead quality or a genuine lower-bound pricing edge.

Favorite -H uses the normal retained phase/uncertainty buffer; the +5pp directional surcharge applies only to dog +H while probation is active.

After completing the favorite validator, resolve `FAV_TAIL_RECONCILED = PASS/FAIL`. If mechanism evidence requires material distribution change, rebuild the full KH_MARGIN_CERT and price both sides again.

---

## 11. Analysis-order neutrality

Before the first KH TAKE on a map, `SIGN_SELECTED_AFTER_DIST = PASS` must certify that:

1. the side-neutral distribution was locked before side selection;
2. both executable sides were priced from that distribution when available;
3. the preliminary best side came from distribution + price, not which sign was easier to justify;
4. opposite-side mechanism failure was not used as positive evidence;
5. the dog probation surcharge and cycle-crossability veto were applied only after neutral sign pricing.

There is no favorite quota and no required directional split.

---

## 12. Directional calibration state

`KH_DIRECTIONAL_CALIBRATION = ACTIVE` and `KH_DOG_DIRECTIONAL_PROBATION = ACTIVE`.

Every KH PRE_TAKE_CERT must explicitly include:

`KH_MARGIN_CERT`

`DIST_LOCKED_BEFORE_LINE`

`BOTH_SIDES_PRICED / justified N/A`

`WMS_ONE_CYCLE`

`WMS_TWO_CYCLE`

`FAVORITE_EXPANSION_MECHANISM`

`FAVORITE_MECH_REPEATABILITY`

`SIGN_SELECTED_AFTER_DIST`

`SELECTED_SIDE_LOWER_BOUND`

`SELECTED_SIDE_BREAK_EVEN`

`APPLICABLE_BUFFER`

`EDGE_AFTER_BUFFER`.

If selected side is dog +H, also require the full probation manifest in Section 9.

Directional calibration and dog probation may be cleared only by a future explicit aggregate KH review. One win, one favorite selection or one short run does not clear either state.

---

## 13. PRE_TAKE_CERT parent manifest

Every KH candidate must first resolve:

`2SNAP | KH_MARGIN_CERT | FAVORITE | CURRENT_SIGNED_MARGIN | MAP_WIN_RANGE | TOTAL_KILLS_RANGE | FAIR_CENTRAL_MARGIN | FINAL_MARGIN_BINS | KCV | RFI | STRUCTURE_MODE | FAVORITE_EXPANSION_MECHANISM | FAVORITE_MECH_REPEATABILITY | FORCED_CYCLE_DENSITY | WIDE_MARGIN_HAZARD | DIST_LOCKED_BEFORE_LINE | BOTH_SIDES_PRICED/N-A | WMS_ONE_CYCLE | WMS_TWO_CYCLE | WMS_PROBABILITY_CLASS | THRESHOLD_CROSSABLE_ONE_CYCLE | THRESHOLD_CROSSABLE_TWO_CYCLE | SIGN_SELECTED_AFTER_DIST | SELECTED_SIDE_COVER_RANGE | SELECTED_SIDE_LOWER_BOUND | SELECTED_SIDE_BREAK_EVEN | APPLICABLE_BUFFER | EDGE_AFTER_BUFFER`.

Then append the selected side's mechanism-specific manifest.

Any missing, contradictory, FAIL, UNRESOLVED, line-anchored, or narrative-only field forces:

`PRE_TAKE_CERT = FAIL -> HOLD/PASS`.

---

## 14. Mechanical contradiction rules

The KH contradiction scan must reject:

- margin bins built after seeing the desired sign/cushion;
- separate incompatible dog/favorite distributions;
- dog value inferred from favorite validator failure or vice versa;
- DEEP NKB/RNE used as probability evidence;
- flat-margin history counted as suppression when no expansion opportunity occurred;
- a materially probable serial favorite cascade omitted from WMS or margin bins;
- a selected-side lower bound that fails break-even plus applicable buffer;
- sign selection before distribution lock;
- WMS labeled LOW despite repeatable favorite mechanism + compulsory contact + no matched suppression, without explicit contrary evidence;
- dog `MECHANISM_MATCH` missing/failed;
- during probation, fewer than two valid matched suppression windows;
- during probation, `DOG_CUSHION_CLASS` other than LARGE;
- during probation, a MATERIAL/HIGH one- or two-cycle WMS branch that crosses the dog failure threshold;
- during probation, failure to add the +5pp dog calibration surcharge;
- favorite -H rejected solely because of late safe-concede risk without adjudicating `COVER_BEFORE_CLOSE`.

Any one forces `CERT_STATE = FAIL`.

---

## 15. Relationship to retained rules

This procedure augments and, where stricter, supersedes KH execution wording in retained v0.3.44+ rules and procedures, including:

- `MODEL_RULES_LOL_V0.3.58.md`;
- `LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`;
- `LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`;
- `LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`;
- `LOL_UNDERDOG_CUSHION_SUFFICIENCY_2026-08-20.md`;
- `LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`;
- `LOL_KH_SMALL_HANDICAP_ASYMMETRY_2026-08-25.md`;
- `LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`;
- `LOL_PRE_TAKE_CERT_KH_MARGIN_EXTENSION_2026-08-25.md`.

Where older LAC wording allows a single favorable event, Section 9.2 is stricter while dog directional probation is active.

---

## 16. Anti-overfit guard

This recalibration does not mean:

- automatically bet favorite -kills;
- require a favorite/dog quota;
- make the recent 4-12 sample a direct cover-probability prior;
- add a minimum game clock;
- raise the global 1.60 odds floor;
- rewrite historical predictions;
- discard DIM/PDRL/UDKC/KMS/LAC/UCS/FFD/RNE/KCV/RFI.

It means:

> Predict the signed final margin first. Stress whether ordinary favorite cycles can cross the line. Select sign second. For dog +H, require observed mechanism-matched suppression rather than theoretical survivability.
