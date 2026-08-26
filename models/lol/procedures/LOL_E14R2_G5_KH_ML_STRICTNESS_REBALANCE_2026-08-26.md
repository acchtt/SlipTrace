# LoL E14R2 Game 5 — KH / ML Strictness Rebalance — 2026-08-26

**Status:** ACTIVE LOCK-SCOPED PROSPECTIVE OVERLAY only when explicitly included by the active Session Authority Lock  
**Effective:** 2026-08-26 18:53 UTC+7  
**Model version:** unchanged — LoL v0.3.58  
**Scope:** LCK 2026 Play-In — KT Rolster vs HANJIN BRION — Game 5 only  
**Authorization:** user instruction “Apply for g5” after Game 4 strictness review  
**Reference review:** `models/lol/reviews/E14R1_GAME4_STRICTNESS_REVIEW_2026-08-26.md`

This overlay corrects E14R1 over-tightness without reviving the prior underdog +kills selection bias. It supersedes only the conflicting E14R1 lock-scoped probation mechanics described below. All retained v0.3.58 rules, parent KH sign-neutrality, PDRL/PML, 2SNAP, PRE_TAKE_CERT, minimum odds 1.60, exact signed-margin arithmetic, and position-blind reassessment remain active.

---

## 1. What does NOT change

The following remain hard:

- no KH sign may be selected before the side-neutral final-margin distribution is locked;
- both executable KH sides must be priced from the same distribution when available;
- NKB/RNE, displayed cushion, quiet time, 0-0 towers, scaling, waveclear, peel, disengage, side pressure, or attractive odds are not probability evidence by themselves;
- theoretical anti-cascade inventory cannot substitute for live evidence;
- THIN / INSUFFICIENT dog +H remains automatic HOLD/PASS;
- favorite -H remains independently validated and is never preferred by quota;
- global minimum accepted odds remains 1.60;
- no historical E14R1 verdict or result is rewritten.

`KH_DOG_DIRECTIONAL_PROBATION` remains ACTIVE, but with the evidence-compatible rules below.

---

## 2. Screenshot-compatible live suppression evidence

The E14R1 requirement for two video-like mechanism-matched suppression windows is too strict for the actual evidence stream, which is synchronized scoreboard + market screenshots.

For Game 5, define **SST — Snapshot Suppression Transition**.

A transition between two synchronized snapshots may count as live anti-cascade evidence when all are resolved:

`SST_START_STATE`

`SST_END_STATE`

`FAVORITE_EXPANSION_MECHANISM`

`EXPANSION_OPPORTUNITY_PRESENT = YES/NO/UNRESOLVED`

`EXPECTED_ORDINARY_EXPANSION_RANGE`

`OBSERVED_MARGIN_CHANGE`

`OBJECTIVE/STRUCTURE_CHANGE`

`UNDERDOG_DIRECT_ANSWER`

`MECHANISM_MATCH = PASS/FAIL`

`SST_CLASS = COUNTER_EXPANSION / BOUNDED_EXPANSION / SUPPRESSED / CONVERTED / NO_OPPORTUNITY / UNRESOLVED`.

Definitions:

- `COUNTER_EXPANSION`: underdog materially improves signed kill margin during a representative favorite pressure/forced-cycle interval while its direct answer is functionally relevant;
- `BOUNDED_EXPANSION`: favorite gains state but realized kill-margin expansion remains materially below the ordinary WMS branch despite a representative opportunity and the underdog preserves executable return-kill/escape routes;
- `SUPPRESSED`: favorite's representative margin route is directly denied without meaningful margin growth;
- `CONVERTED`: favorite realizes the expected expansion route; negative for dog +H;
- `NO_OPPORTUNITY`: neutral, not positive evidence.

A synchronized screenshot transition is valid evidence. Continuous video is not required.

---

## 3. Dog evidence package — replace rigid two-window rule

For dog +H during Game 5, replace the E14R1 “two distinct matched suppression windows or automatic PASS” rule with:

`DOG_LIVE_EVIDENCE_PACKAGE = PASS` if either route A or route B passes.

### Route A — two matched transitions

Two distinct SSTs classified as `COUNTER_EXPANSION`, `BOUNDED_EXPANSION`, or `SUPPRESSED`, each with `MECHANISM_MATCH=PASS`, and neither contradicted by a later dominant `CONVERTED` transition.

### Route B — one strong matched transition + independent state support

One SST classified `COUNTER_EXPANSION` or `SUPPRESSED` with `MECHANISM_MATCH=PASS`, plus all of:

- underdog has independent map-win support from the live ML model rather than handicap cushion logic;
- opposing favorite lead is not broad-and-terminal after lead-quality decomposition;
- underdog retains at least one verified executable direct answer to the favorite's repeatable expansion mechanism;
- no later HIGH-probability converted cascade invalidates the evidence.

`NO_OPPORTUNITY` and theoretical inventory never satisfy either route.

---

## 4. Dog cushion eligibility — MATERIAL may qualify conditionally

For Game 5:

- `INSUFFICIENT` or `THIN` => automatic HOLD/PASS;
- `LARGE` => eligible under retained rules;
- `MATERIAL` => eligible only when **all** of the following pass:
  - `DOG_LIVE_EVIDENCE_PACKAGE = PASS`;
  - `DOG_INDEPENDENT_ML_SUPPORT = PASS`;
  - `MECHANISM_MATCH = PASS`;
  - selected-side lower-bound cover probability clears break-even plus the applicable dog buffer;
  - probability-weighted cycle hazard in Section 5 is not disqualifying.

`DOG_INDEPENDENT_ML_SUPPORT=PASS` requires the map-win model to give the dog meaningful independent win/reversal equity after lead-quality decomposition. It cannot be inferred from the +H price, NKB, or failure of favorite -H.

This change does not make +3.5/+5.5 automatically playable. It only removes the categorical ban when the dog also has credible outright-win equity and observed live resilience.

---

## 5. Replace binary cycle-crossability veto with probability-weighted hazard

E14R1 treated “can an ordinary one/two-cycle branch cross the dog failure threshold?” as an automatic veto. That is too binary because many LoL handicaps are mathematically crossable by a 4-0 or 5-0 fight even when that branch is not probable enough to destroy value.

For Game 5 resolve:

`DOG_FAILURE_THRESHOLD`

`WMS_ONE_CYCLE_NET_MARGIN_RANGE`

`WMS_TWO_CYCLE_NET_MARGIN_RANGE`

`P_CROSS_ONE_CYCLE = LOW / MATERIAL / HIGH`

`P_CROSS_TWO_CYCLE = LOW / MATERIAL / HIGH`

`CROSS_HAZARD_INTEGRATED_IN_DIST = PASS/FAIL`.

Hard consequences:

- `P_CROSS_ONE_CYCLE = HIGH` => automatic HOLD/PASS for dog +H;
- `P_CROSS_TWO_CYCLE = HIGH` with remaining compulsory fight density MATERIAL/HIGH => automatic HOLD/PASS;
- `MATERIAL` cross hazard is not an automatic veto, but must be explicitly represented in the wide-margin tail of `FINAL_MARGIN_BINS` and therefore in the selected-side lower bound;
- if integrating the hazard causes the lower bound to miss break-even plus buffer, PASS;
- raw mathematical crossability without probability classification is not enough to reject the dog.

This preserves wide-margin stress while removing the “any plausible 4-0 fight bans +3.5 forever” failure mode.

---

## 6. Dog calibration buffer for Game 5

Retain a directional surcharge, but make it conditional on cushion/evidence quality:

- `LARGE` dog cushion with Route A evidence package: retained phase buffer **+3 percentage points**;
- `LARGE` dog cushion with Route B evidence package: retained phase buffer **+4 percentage points**;
- `MATERIAL` dog cushion: retained phase buffer **+5 percentage points**.

The surcharge is applied to the selected-side lower-bound pricing test. It is not a central-probability haircut.

This keeps MATERIAL cushions difficult while allowing genuinely demonstrated LARGE cushions to avoid an unnecessary fixed +5pp penalty.

---

## 7. ML/KH lead-concentration decomposition — strengthened

Game 4 showed that a team-level gold lead can be misleading when nearly all of it sits in one role while the other four roles are collectively neutral/behind.

For every live ML and KH distribution in Game 5 resolve:

`TEAM_GOLD_LEAD`

`LARGEST_ROLE_GOLD_EDGE`

`LEAD_CONCENTRATION_RATIO = abs(LARGEST_ROLE_GOLD_EDGE) / abs(TEAM_GOLD_LEAD)` when TEAM_GOLD_LEAD != 0

`NON_CONCENTRATED_NET = TEAM_GOLD_LEAD - signed(LARGEST_ROLE_GOLD_EDGE)`

`LEAD_CONCENTRATION_CLASS = BROAD / MIXED / CONCENTRATED / EXTREME`

`CONCENTRATED_ROLE_CONVERSION_ACCESS = LOW / MATERIAL / HIGH`

`OBJECTIVE_OFFSET`

`COUNTER_EXPANSION_EVIDENCE`

`LEAD_QUALITY_AFTER_CONCENTRATION`.

Guidance:

- `CONCENTRATED`: largest role explains >=60% of team lead;
- `EXTREME`: largest role explains >=90% of team lead or exceeds the total team lead, implying the remaining roles are net behind.

For `CONCENTRATED/EXTREME` leads, downgrade raw lead quality by one band unless the concentrated role has MATERIAL/HIGH direct conversion access into the next compulsory cycles.

Downgrade by an additional band when all are true:

- opposing team has equal/better major-objective control or clearly better next-objective setup;
- opposing team has a valid `COUNTER_EXPANSION` SST;
- concentrated role cannot reliably transfer its lead into the opposing team's demonstrated fight mechanism.

This adjustment applies to both ML win-range construction and KH final-margin bins. It is not an automatic fade of a fed carry; direct conversion access can preserve lead quality.

---

## 8. Independent ML support for a dog handicap

To prevent handicap logic from laundering itself into ML support, resolve the live ML model first.

`DOG_INDEPENDENT_ML_SUPPORT = PASS` only if, after CFC/lead decomposition/concentration adjustment/draft/live execution evidence, the underdog has a non-trivial map-win lower bound that is compatible with the dog handicap's cover thesis.

Examples of valid support:

- underdog has demonstrated counter-expansion and objective control while nominal favorite gold is concentrated;
- underdog's direct engage/answer mechanism has realized successfully in live transitions;
- map state remains structurally reversible and the market favorite's conversion route is answerable.

Invalid support:

- “dog +3.5 also covers many losses”;
- favorite -H failed;
- dog ML odds are large;
- theoretical scaling only.

---

## 9. Game 5 KH PRE_TAKE additions

For any dog +H candidate, Game 5 PRE_TAKE_CERT must append:

`DOG_CUSHION_CLASS`

`DOG_LIVE_EVIDENCE_PACKAGE = PASS/FAIL`

`SST_EVIDENCE_IDS`

`DOG_INDEPENDENT_ML_SUPPORT`

`P_CROSS_ONE_CYCLE`

`P_CROSS_TWO_CYCLE`

`CROSS_HAZARD_INTEGRATED_IN_DIST`

`GAME5_DOG_BUFFER`

`SELECTED_SIDE_LOWER_BOUND`

`EDGE_AFTER_BUFFER`.

For every ML/KH candidate append:

`LEAD_CONCENTRATION_RATIO`

`LEAD_CONCENTRATION_CLASS`

`NON_CONCENTRATED_NET`

`CONCENTRATED_ROLE_CONVERSION_ACCESS`

`LEAD_QUALITY_AFTER_CONCENTRATION`.

Any missing/contradictory required field forces HOLD/PASS.

---

## 10. Supersession statement

For Game 5 only, when the active Session Authority Lock includes this overlay:

- Section 3 replaces the E14R1 requirement for exactly two mechanism-matched suppression windows;
- Section 4 replaces the E14R1 `LARGE-only` dog-cushion eligibility rule;
- Section 5 replaces the E14R1 binary one/two-cycle crossability veto;
- Section 6 replaces the fixed E14R1 +5pp dog surcharge;
- Section 7 strengthens the live ML/KH lead-quality decomposition.

All non-conflicting retained procedures remain mandatory.

No historical Game 1–4 verdict, position or P/L is changed by this prospective overlay.
