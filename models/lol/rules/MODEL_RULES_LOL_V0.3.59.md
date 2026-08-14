# MODEL RULES — LEAGUE OF LEGENDS v0.3.59

**Status:** Active delta  
**Effective date:** 2026-08-15 UTC+7  
**Supersedes:** v0.3.58 only where stated

## Purpose

Correct a recurring Duration error in which **0-0 towers / no first tower** was treated as positive stall evidence even when no meaningful structure-conversion attempt had actually been denied.

Reference review:
`models/lol/reviews/DURATION_0_0_TOWER_RECURRENCE_REVIEW_2026-08-15.md`

The user explicitly authorized this narrow revision on 2026-08-15.

All non-Duration v0.3.58 rules remain unchanged.

---

## 1. 0-0 towers is neutral by default

For Duration analysis:

- `0-0 towers`;
- no first tower yet;
- a low absolute tower count;
- no inhibitor yet;

are **state descriptors**, not positive Over evidence by themselves.

They may not satisfy an observed-stall requirement merely because structure conversion has not yet happened.

Do not write or reason:

- “0-0 towers supports the Over”;
- “no structural conversion yet therefore stall”;
- “first tower not taken therefore conversion is unproven”;

unless a real conversion opportunity existed and was demonstrably denied.

Where prior live interpretation allowed 0-0 tower state to function as an implicit Over signal, **v0.3.59 supersedes that interpretation**.

---

## 2. Absent conversion is not failed conversion

Before a Duration Over, classify the structural evidence as one of:

### `ABSENT CONVERSION`

No meaningful opportunity to convert has occurred yet, or no tower has fallen without evidence that a real push/objective/tempo window was denied.

**Effect:** neutral for Over.

### `FAILED CONVERSION`

A team obtained meaningful tempo, objective leverage, numbers advantage, wave access, siege position, Baron/Herald leverage, or a won fight and then **failed to create expected structural/base access because the opponent actually defended, reset, wavecleared, disengaged, cross-mapped or otherwise denied conversion.**

**Effect:** may count as observed stall evidence.

Only **FAILED CONVERSION** can satisfy the structure-related portion of an Over stall thesis.

A scoreboard showing 0-0 towers cannot distinguish these states on its own.

---

## 3. Mandatory Latent Conversion Hazard (LCH) for Duration Over

Before every Duration Over TAKE, classify **Latent Conversion Hazard (LCH)**:

- `LOW`
- `MEDIUM`
- `HIGH`

LCH estimates the probability that the next successful fight/objective sequence can cause a **nonlinear first-break cascade** even if towers are currently 0-0.

Mandatory inputs:

1. dragon count and Soul/Elder proximity;
2. Baron/Herald availability or imminent objective window;
3. grubs and resulting tower pressure where relevant;
4. current gold lead and role-weighted distribution / TEI;
5. lane priority, wave state and realistic siege access;
6. reliable first contact / pick / engage access;
7. defender fallback, waveclear, disengage and reset quality under pressure;
8. side-lane pressure and number of simultaneous defensive assignments;
9. shortest realistic path from the next won fight to first tower, second structure and base access;
10. whether one compulsory objective fight can remove multiple defensive layers.

### LCH = HIGH

Use HIGH when several aligned features make a rapid structure cascade plausible from the **next one or two major windows**, even though little or no structure damage has yet been recorded.

Examples include, but are not limited to:

- 3-0 dragons plus reliable forcing into the Soul fight and weak defender reset;
- strong role-weighted economy plus imminent Baron and multiple lanes already pressured;
- defender draft that can contest once but has poor post-fight waveclear/base defense;
- grubs/siege pressure plus a lead that can turn first tower into serial outer/inner access.

No single signal, including 3-0 dragons, automatically makes LCH HIGH.

---

## 4. Duration Over eligibility correction

Retain the v0.3.45 requirement for at least two independent observed stall mechanisms.

v0.3.59 adds the following hard interpretation rules:

1. **0-0 towers / no first tower cannot count as either stall mechanism.**
2. At least one Over stall mechanism must be based on **observed FAILED CONVERSION** or another clearly observed clock-consuming mechanism, not merely inactivity.
3. If `LCH = HIGH`, a Duration Over is **TAKE-INELIGIBLE** unless:
   - at least one high-leverage conversion opportunity has already been denied **after** LCH became high; and
   - two independent observed stall mechanisms still persist across the required snapshots; and
   - the survival-horizon/dead-zone gates still pass after repricing.
4. If the evidence is only `ABSENT CONVERSION`, verdict is `HOLD/PASS`, never TAKE Over.

This is intentionally high-friction. Low Duration bet frequency is acceptable.

---

## 5. Pre-first-tower cascade check

The nonlinear conversion check must occur **before** the first tower falls.

For every Over, estimate the shortest realistic chain:

`next forced fight/objective -> first tower -> vision depth -> second structure -> base access -> Nexus`

If that plausible chain fits materially inside the market survival horizon, the Over cannot use 0-0 towers as protection.

The model must explicitly ask:

**“What happens if the next compulsory fight is lost?”**

not only:

**“What has failed to happen so far?”**

---

## 6. Objective schedule can compress clock

For Duration, a scheduled objective window does not automatically imply more game time because another fight must occur.

Soul, Elder and Baron windows can instead **compress** the map by forcing a fight whose winner gains immediate structure/base access.

Therefore:

- 3-0 dragons is not a generic Over signal;
- “another dragon fight remains” is not automatically clock-positive;
- if one side has reliable access and the loser has weak post-fight defense, the objective schedule increases LCH.

This is separate from favorite-handicap FFD. A forced fight can be good for a kill handicap while simultaneously being bad for a Duration Over because the same fight can end the map quickly.

---

## 7. Under symmetry guard

Do not flip the old bias into an automatic Under bias.

`0-0 towers`, HIGH LCH, 3-0 dragons, a large gold lead or strong engage **do not by themselves qualify a Duration Under**.

The v0.3.45 Under requirement remains:

- observed acceleration;
- at least two independent acceleration mechanisms except the retained terminal-state exception;
- two-snapshot persistence where required;
- survival-horizon and dead-zone clearance.

v0.3.59 changes Over interpretation, not the standard for Under qualification.

---

## 8. VIT vs GIANTX Game 3 reference correction

At 17:53:

- VIT 3-5 GX kills;
- GX approximately +2.2k economy;
- towers 0-0;
- VIT dragons 3-0;
- Over 32 minutes @1.675.

The historical v0.3.58 verdict was:

**TAKE — Over 32 min @1.675 — shadow 0.25u; actual 0u.**

Final at 27:21:

- VIT 14-6 GX;
- VIT approximately +8.5k;
- towers 8-3;
- dragons 4-0;
- Baron 1-0;
- inhibitor 1-0.

Under v0.3.59, the reference state is **not an Over TAKE** merely because towers were 0-0.

The correct classification is:

- tower evidence: `ABSENT CONVERSION`, not proven failed conversion;
- Soul-point schedule: material pre-break compression risk;
- LCH: elevated and potentially HIGH depending on synchronized wave/access evidence;
- without demonstrated failed conversion after that high-leverage state, Over should be `HOLD/PASS`.

This is a diagnostic reference only. Historical P/L remains unchanged.

---

## 9. Mandatory Duration checklist addition

Before any Duration Over TAKE, internally lock all retained v0.3.45 items plus:

1. tower count treated as descriptor, not direction;
2. conversion classification: `ABSENT` or `FAILED`;
3. exact observed failed-conversion mechanism;
4. LCH LOW/MEDIUM/HIGH;
5. next compulsory objective window;
6. shortest pre-break fight-to-Nexus cascade;
7. whether the Over survives the `LCH = HIGH` block;
8. confirmation that 0-0 towers was not counted as a stall mechanism.

Missing or ambiguous decision-critical evidence => `PASS/HOLD`.

---

## 10. Retained controls

All non-conflicting v0.3.58 and earlier controls remain active, including:

- favorite -kills FFD / RNE correction;
- v0.3.57 fallback-floor certification and False-Stable Guard;
- v0.3.56 hard underdog +kills veto;
- Draft Primacy and position-blind reassessment;
- MKT + TEAM anchoring;
- Role-Weighted Economy / TEI;
- two-snapshot live eligibility for ML/KH/TK;
- signed kill-margin distribution;
- NKB / RFI / KCV / Structure Substitution;
- Total Kills OKP/FCI/CRR/SRR/BF/CL/RKS/KPW;
- stale-line gate;
- same-game correlation decomposition;
- all v0.3.45 Duration timing, persistence, dead-zone, probability-buffer and regime-change restrictions;
- no rescue/martingale/loss chasing.

Where this delta conflicts with earlier Duration interpretation, **v0.3.59 controls**.
