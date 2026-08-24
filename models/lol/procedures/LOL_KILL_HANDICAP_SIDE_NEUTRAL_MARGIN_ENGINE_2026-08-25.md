# LoL Kill Handicap Side-Neutral Margin Engine — 2026-08-25

**Status:** ACTIVE CANONICAL v0.3.58 IN-PLACE AMENDMENT when included by the active Session Authority Lock  
**Effective:** 2026-08-25 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Scope:** every live Kill Handicap candidate, both positive and negative sides  
**Authorization:** user instruction **“Lock this slate. And adjust the model with your recommendations.”**  
**Reference review:** `models/lol/reviews/KILL_HANDICAP_DIRECTIONAL_BIAS_AND_MARGIN_ENGINE_REVIEW_2026-08-25.md`

This procedure restores the retained v0.3.44 distribution-first Kill Handicap hierarchy as the parent gate and makes later positive/negative handicap mechanisms subordinate validators of the same side-neutral final-margin distribution.

It does **not** create a favorite bias, does not ban underdog +kills, and does not create a new analytical model version.

---

## 1. Parent rule — predict margin before choosing sign

Before evaluating either displayed Kill Handicap side, construct one **KH_MARGIN_CERT — Kill Handicap Margin Certificate**.

The certificate is side-neutral. The displayed +H / -H line may not determine the projected distribution.

Mandatory order:

`STATE + MKT + TEAM`

`-> KH_MARGIN_CERT`

`-> price both sides from the same locked distribution`

`-> wide-margin stress`

`-> preliminary best side / PASS`

`-> side-specific mechanism validator`

`-> retained uncertainty / phase buffer`

`-> PRE_TAKE_CERT`

`-> TAKE / HOLD / PASS`

If the sign was selected before the distribution was locked:

`SIGN_SELECTED_AFTER_DIST = FAIL -> HOLD/PASS`.

---

## 2. Mandatory KH_MARGIN_CERT

Before using the sportsbook handicap as evidence, resolve:

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

`WIDE_MARGIN_HAZARD`

`UNCERTAINTY_WIDTH`

`DIST_LOCKED_BEFORE_LINE = PASS/FAIL`

### Required final-margin representation

At minimum retain the canonical v0.3.44 bins:

- `M <= 0`
- `M = +1 to +3`
- `M = +4 to +6`
- `M = +7 to +9`
- `M = +10 to +14`
- `M >= +15`

where:

`M = favorite final kills - underdog final kills`.

Refine bins when a displayed line requires more precision, but do not create a new incompatible distribution for the opposite side.

The probabilities must sum to approximately 100% and remain coherent with map-win probability, total-kill expectation, live state, team-strength prior, draft interaction, economy concentration, objective schedule and conversion architecture.

If the distribution is under-specified or internally inconsistent, verdict is HOLD/PASS.

---

## 3. Both-side pricing is mechanical

After `KH_MARGIN_CERT` is locked, and only then, compare the displayed handicap/odds.

When both sides are available, record:

`DOG_LINE`

`DOG_ODDS`

`DOG_BREAK_EVEN`

`DOG_COVER_RANGE`

`FAV_LINE`

`FAV_ODDS`

`FAV_BREAK_EVEN`

`FAV_COVER_RANGE`

`RETAINED_PHASE_BUFFER`

`DOG_EDGE_AFTER_BUFFER`

`FAV_EDGE_AFTER_BUFFER`

`PRELIMINARY_BEST_SIDE = DOG / FAV / PASS`

`BOTH_SIDES_PRICED = PASS/FAIL`

The same frozen margin distribution must generate both cover estimates.

If only one side is displayed, still construct the side-neutral distribution. `BOTH_SIDES_PRICED` may be marked `N/A` only because the opposite executable price is genuinely unavailable; absence of the opposite price does not relax `DIST_LOCKED_BEFORE_LINE` or side-neutrality.

### Hard relationship

For half-kill lines:

- `P(dog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

For whole-number lines, account explicitly for push rules.

A TAKE requires the **lower bound** of the selected side's cover range to clear break-even by the retained active phase/uncertainty buffer. Central estimate alone is insufficient.

---

## 4. Non-complementarity of value certification

Mandatory hard rules:

- `FAVORITE -H FAIL` supplies **zero positive evidence** for `UNDERDOG +H`;
- `UNDERDOG +H FAIL` supplies **zero positive evidence** for `FAVORITE -H`;
- inability to prove favorite FFD/RNE never creates dog value;
- inability to prove dog KMS/LAC/UCS never creates favorite value;
- both sides may correctly be HOLD/PASS because required edge buffers and uncertainty are not complementary.

No sign inversion shortcut is permitted.

---

## 5. Wide-Margin Stress — mandatory before every KH TAKE

Run **WMS — Wide-Margin Stress** from the favorite's perspective before either side is selected for final certification.

Construct the strongest ordinary realistic serial expansion branch supported by current evidence:

`next compulsory setup`

`-> first contact`

`-> ordinary cleanup / continuation`

`-> objective / structure transition`

`-> deeper vision / map compression`

`-> next forced entry`

`-> base-defense / terminal kill exposure where realistic`.

This must not be a catastrophic miracle branch. It should represent a plausible professional favorite-winning cascade under current draft, role economy, objective schedule, target access and observed fight behavior.

Resolve:

`WMS_BRANCH_DESCRIPTION`

`WMS_NET_MARGIN_RANGE`

`WMS_PROBABILITY_CLASS = LOW / MATERIAL / HIGH`

`WMS_INTEGRATED_IN_DIST = PASS/FAIL`

If a materially probable wide-margin branch is omitted or materially underweighted in `FINAL_MARGIN_BINS`, the certificate fails.

A large NKB cannot override WMS.

---

## 6. NKB/RNE are arithmetic only

Exact signed-margin arithmetic remains mandatory.

For dog +H, calculate exact failure threshold and NKB.

For favorite -H, calculate exact cover threshold and RNE/NKB as applicable.

But:

> “favorite needs another +7 / +8 / +10 net kills” is a hurdle description, not evidence that the hurdle is unlikely.

Kill margins are serially dependent. Multiple kills may arrive through linked fight -> objective -> vision -> next-fight -> base-defense sequences.

`NKB`, `RNE`, or a `DEEP` cushion can never establish value by themselves.

---

## 7. Positive-handicap validator — downstream only

If the preliminary best side is the underdog +kills side, retain every applicable positive-handicap gate:

`2SNAP`

`DIM`

`PDRL` when professional-play draft authority requires it

`TAM`

`CAS`

`UDKC_STABLE`

`KPA`

`KMS`

`RLD_DRAFT`

`FALSE_STABLE_INACTIVE`

`LIVE_RLD`

`LIVE_PRESERVATION`

`LAC`

`UCS`

`SCNE`

`SIGNED_MARGIN`

`EXACT_NKB`

`PRICE`.

These fields test whether the neutral distribution's close-loss / margin-survival mass is mechanically credible.

They may **downgrade or invalidate** the preliminary dog edge. They may not create an initial dog edge that was absent from `KH_MARGIN_CERT`.

### Distribution reconciliation

After completing the dog mechanism validator, explicitly resolve:

`DOG_TAIL_RECONCILED = PASS/FAIL`.

PASS means the side-specific mechanisms are consistent with the already-locked distribution or justify a conservative one-way downgrade of the selected edge.

If mechanism analysis would require rebuilding the distribution materially, discard the old certificate and rebuild `KH_MARGIN_CERT` from zero before re-pricing either side. Do not edit only the dog tail after seeing the line.

---

## 8. Pressure-adjusted LAC interpretation

LAC is strengthened only in interpretation, not replaced.

Before counting a flat or slowly moving favorite kill margin as positive suppression evidence, classify the observed window:

- `NO_EXPANSION_OPPORTUNITY`
- `EXPANSION_OPPORTUNITY_SUPPRESSED`
- `EXPANSION_OPPORTUNITY_CONVERTED`
- `UNRESOLVED`.

Only `EXPANSION_OPPORTUNITY_SUPPRESSED` is positive anti-cascade evidence.

Examples of positive suppression include a representative favorite pressure/contact window where the underdog actually:

- disengages and reforms;
- returns kills and bounds cleanup;
- preserves protected DPS through first contact;
- structurally denies continuation;
- cross-maps in a way that materially deletes the next forced fight;
- or otherwise demonstrates the claimed KMS mechanism under pressure.

The following are `NO_EXPANSION_OPPORTUNITY` or neutral unless tied to real pressured denial:

- passive farming;
- elapsed time with no fight;
- 0-0 towers;
- small kill margin;
- ordinary uncontested objective trade;
- low kill count;
- stable gold without representative contact.

A candidate cannot set `LAC = PASS` by treating absence of opportunity as successful suppression.

---

## 9. Favorite negative-handicap validator — downstream only

If the preliminary best side is favorite -kills, retain every applicable favorite-margin gate:

`2SNAP`

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

`CONTINUATION / CLEANUP ACCESS`

`retained NKB/RFI/KCV checks`

`PRICE`.

These fields test whether the neutral distribution's wide favorite tail is mechanically credible.

They may downgrade or invalidate the preliminary favorite edge. They may not create a favorite edge absent from `KH_MARGIN_CERT`.

After completing the favorite mechanism validator, resolve:

`FAV_TAIL_RECONCILED = PASS/FAIL`.

If material mechanism evidence would require rebuilding the distribution, rebuild the whole certificate and re-price both sides.

---

## 10. Analysis-order neutrality

The Kill Handicap family may not be consumed merely because the analyst inspected +kills first.

Before the first KH TAKE on a map:

`SIGN_SELECTED_AFTER_DIST = PASS`

must certify that:

1. the side-neutral distribution was locked before the displayed side was chosen;
2. both executable sides were priced from that distribution when available;
3. the preliminary best side was determined from price/edge, not from which side's mechanism certificate was easier to complete;
4. the opposite side's mechanism failure was not used as evidence for the selected side.

There is no mandatory elapsed-time delay for positive handicaps. A genuine early +kills edge may still TAKE if this complete process passes.

---

## 11. Directional calibration mode

Canonical ledger review on 2026-08-25 found approximately 97% of settled Kill Handicap selections on the positive side with negative positive-handicap performance.

Therefore:

`KH_DIRECTIONAL_CALIBRATION = ACTIVE`.

While active, every KH PRE_TAKE_CERT must explicitly include:

`KH_MARGIN_CERT`

`DIST_LOCKED_BEFORE_LINE`

`BOTH_SIDES_PRICED / justified N/A`

`WMS`

`SIGN_SELECTED_AFTER_DIST`

`SELECTED_SIDE_LOWER_BOUND`

`SELECTED_SIDE_BREAK_EVEN`

`RETAINED_PHASE_BUFFER`

`EDGE_AFTER_BUFFER`.

Directional calibration is a process control, not a favorite-selection quota.

Do not clear it because one or two favorite bets appear. It may be cleared only by a future explicit aggregate KH review showing that directional selection and calibration have materially normalized.

---

## 12. PRE_TAKE_CERT Kill Handicap parent manifest

Every Kill Handicap candidate, regardless of sign, must first resolve:

`2SNAP | KH_MARGIN_CERT | FAVORITE | CURRENT_SIGNED_MARGIN | MAP_WIN_RANGE | TOTAL_KILLS_RANGE | FAIR_CENTRAL_MARGIN | FINAL_MARGIN_BINS | KCV | RFI | STRUCTURE_MODE | WIDE_MARGIN_HAZARD | DIST_LOCKED_BEFORE_LINE | BOTH_SIDES_PRICED/N-A | WMS | SIGN_SELECTED_AFTER_DIST | SELECTED_SIDE_COVER_RANGE | SELECTED_SIDE_LOWER_BOUND | SELECTED_SIDE_BREAK_EVEN | RETAINED_PHASE_BUFFER | EDGE_AFTER_BUFFER`.

Then append the selected side's existing mechanism-specific manifest from Sections 7 or 9.

Any missing, contradictory, `FAIL`, `UNRESOLVED`, line-anchored, or narrative-only parent field forces:

`PRE_TAKE_CERT = FAIL -> HOLD/PASS`.

---

## 13. Mechanical contradiction rules

For KH, the PRE_TAKE contradiction scan must additionally reject:

- a dog TAKE whose `FINAL_MARGIN_BINS` were built after seeing the dog cushion;
- separate incompatible dog/favorite distributions;
- a dog edge justified by favorite -H FFD failure;
- a favorite edge justified by dog UDKC/LAC/UCS failure;
- `DEEP NKB` used as probability evidence;
- flat-margin history counted as suppression when no expansion opportunity occurred;
- a materially probable serial favorite cascade omitted from WMS or the distribution;
- a selected-side lower bound that does not clear break-even plus retained phase buffer;
- sign selection before distribution lock.

Any one of these forces `CERT_STATE = FAIL`.

---

## 14. Relationship to retained rules

This procedure **augments and, where stricter, supersedes** Kill Handicap execution wording in:

- `MODEL_RULES_LOL_V0.3.44.md` through retained later deltas;
- `MODEL_RULES_LOL_V0.3.48.md`;
- `MODEL_RULES_LOL_V0.3.53.md`;
- `MODEL_RULES_LOL_V0.3.56.md`;
- `MODEL_RULES_LOL_V0.3.57.md`;
- `MODEL_RULES_LOL_V0.3.58.md`;
- `LOL_FALLBACK_FLOOR_CERTIFICATION_2026-08-13.md`;
- `LOL_UNDERDOG_PLUSKILLS_DRAFT_LOCK_GUARD_2026-08-19.md`;
- `LOL_DRAFT_INTERACTION_MATRIX_2026-08-20.md`;
- `LOL_DURATION_OVER_AND_UNDERDOG_PLUSKILLS_EXECUTION_HARDENING_2026-08-23.md`;
- `LOL_PRE_TAKE_CERT_MECHANICAL_VALIDATOR_2026-08-23.md`.

It does not remove any side-specific hard veto. It restores a neutral parent distribution above them.

---

## 15. Anti-overfit guard

This amendment does **not** mean:

- automatically bet favorite -kills;
- prohibit underdog +kills;
- require a 50/50 directional split;
- add a new minimum game clock;
- raise the global 1.60 odds floor;
- treat one loss as proof of a new mechanism;
- rewrite historical predictions;
- discard DIM/PDRL/UDKC/KMS/LAC/UCS/FFD/RNE/KCV/RFI.

It means:

> **Predict the final signed kill margin first. Choose the handicap sign second. Validate the selected tail third.**

If the side-neutral distribution plus all selected-side hard gates and retained buffers genuinely pass, TAKE remains available.
