# Football Semantic Decision-Basis Contract

**Status:** ACTIVE PROCESS COMPLIANCE CONTROL  
**Model effect:** none — this contract does not add or change predictive thresholds.

## Purpose

Several Football C/C2/C3 inputs are semantic football judgments rather than mechanically observed values. Their booleans/states may change a verdict, so a bare true/false declaration is insufficient for QA.

This contract requires an explicit contemporaneous evidence basis for those judgments. The deterministic engine validates presence and persistence of the basis; it does not invent the football judgment.

## General rule

For every semantic field that can change state, burden, lane, WAIT/PASS/BET, or shadow action:

1. record the exact semantic value;
2. record a non-empty evidence basis from the same evidence epoch;
3. do not infer a favorable value from a missing field;
4. preserve the value+basis pair in machine output / Decision State evidence;
5. never rewrite the earlier basis after result knowledge.

A basis must identify the football reason or evidence checked. Repeating only the field value (for example, "material_veto=false because no veto") is not a sufficient research explanation.

## H2H treatment

Active Football C priority remains:

`CURRENT MECHANISM -> RECENT SAME-VENUE TRANSFERABLE H2H -> RECENT ALL-VENUE TRANSFERABLE H2H -> OLD BACKGROUND`

### "Recent" is priority, not a hidden numeric threshold

Football C currently has no frozen numerical match-count/year cutoff for the word `recent`.

Therefore:
- `recent` orders which H2H evidence should be inspected first;
- it is **not** by itself a hard pass/fail threshold;
- QA must not invent a 3-match/5-match/2-year/etc cutoff inside production;
- any future numerical recency rule is a predictive-rule proposal and requires a separately frozen challenger.

### Allowed H2H effect

H2H never creates a scoring route.

Suppressive H2H may contribute to an existing downgrade/veto only when the research judgment explicitly records:
- why the matchup is transferable to the current teams/context; and
- what current football evidence independently corroborates the same suppressive mechanism.

If transferability or current corroboration cannot be established, record the review as LIMITED / NOT_USABLE / not material as appropriate. Do not turn ambiguous historical scorelines into `material_suppression=true`.

Required fields:
- `h2h_state`;
- `h2h_effect = SUPPRESSIVE / OPEN / MIXED / NOT_MATERIAL / UNAVAILABLE`;
- `h2h_transferability = VERIFIED / LIMITED / NOT_TRANSFERABLE / UNAVAILABLE`;
- `h2h_current_corroboration = VERIFIED / NOT_FOUND / NOT_APPLICABLE / UNKNOWN`;
- `h2h_material_effect = true/false`;
- `h2h_review_status`;
- `h2h_rechecked` at Step 2;
- non-empty `h2h_basis`.

If `h2h_material_effect=true`, the deterministic contract requires all three:
- `h2h_effect=SUPPRESSIVE`;
- `h2h_transferability=VERIFIED`;
- `h2h_current_corroboration=VERIFIED`.

This compiles the already-active "transferable and corroborated" rule; it does not add a new predictive threshold.

Missing/unreliable H2H does not create favorable evidence. It remains unavailable/limited and the decision must rely on the current football evidence permitted by the active model.

## Match-assessment semantic booleans

The following common assessment booleans require a paired basis:

- `carrier_self_fund` -> `carrier_self_fund_basis`;
- `independent_upper_tail` -> `independent_upper_tail_basis`;
- `failure_attacks_route` -> `failure_attacks_route_basis`;
- `material_suppression` -> `material_suppression_basis`.

The basis must identify the route/mechanism evidence used to make the declaration.

These basis fields have zero independent ranking weight. They only make the existing declaration auditable.

## Step-2 context booleans

The following Step-2 decisions require a paired basis:

- `thesis_state = PRESERVED / DEGRADED / BROKEN` -> `thesis_state_basis`;
- `primary_mechanism_intact` -> `primary_mechanism_basis`;
- `wait_reachable` -> `wait_reachability_basis`;
- `wait_requires_negative_info` -> `wait_negative_info_basis`;
- `material_veto` -> `material_veto_basis`.

The basis fields do not change the existing Boolean logic.

### WAIT

`wait_reachable=true` still means the protected target is realistically reachable without expected thesis deterioration under the active Football C rule.

The new basis must state why that is believed at the decision epoch. It does not introduce a new timing/odds threshold.

### Material veto

`material_veto=true/false` remains the current-football synthesis of already-active veto conditions. The basis identifies which concrete mechanism/incentive/XI/H2H evidence creates or rejects the veto.

Do not use `material_veto` as an undocumented catch-all.

## Missing-data behavior

If a required semantic value exists but its basis is absent:

`DECISION BLOCKED — SEMANTIC EVIDENCE BASIS MISSING`

If the underlying evidence is genuinely unavailable, record the appropriate LIMITED / UNAVAILABLE / false-or-unknown state allowed by the authoritative model and explain that in the basis. Do not fabricate support.

## Persistence

Persist the basis in:
- deterministic decision input;
- deterministic decision result where applicable;
- Decision State Evidence Summary and/or dedicated current fields;
- machine appendix.

Frozen Step-1 basis remains historical. A Step-2 basis is a new current evidence epoch and does not overwrite Step 1.

## QA classification

This contract is a `PROCESS COMPLIANCE FIX`.

It does not:
- alter Football C/C2/C3 thresholds;
- create new exposure;
- define a new numerical H2H recency rule;
- change supported-burden policy;
- change price policy.

Any proposal to define new numerical transferability/recency thresholds or to alter how H2H changes burden/exposure is `MODEL CHALLENGER REQUIRED`.
