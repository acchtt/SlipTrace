# Football C — G3 mechanism-balance challenger replay, 23–26 October 2026

**Date:** 2026-10-26 ICT  
**Authority:** Football C only  
**Input universe:** nine sealed verified rank packages, 152 frozen assessed match-epochs  
**Outcome rule:** selection is compiled from frozen prematch evidence first; final scores are joined afterward  
**Production predictive code changed:** NO  
**/xi changed:** NO

## Purpose

Test the G3 mechanism-balance proposals after the CONTROL_REVIEW authority repair and the expanded 23–26 October replay.

The production question is whether carrier-led G3 is too easy relative to genuinely two-sided G3, and whether a smaller symmetric funding/ranking change can improve separation without destroying G3 recall.

## Frozen universe

The same nine sealed packages used by the expanded post-repair replay were materialized:

1. Football-C-rank-20261023-1500-2100-rerun-verified.json
2. Football-C-rank-20261023-2100-20261024-0300-verified.json
3. Football-C-rank-20261024-0726-1200-verified.json
4. Football-C-rank-20261024-1046-1200-verified.json
5. Football-C-rank-20261024-1800-0000-verified.json
6. Football-C-rank-20261025-0000-0730-verified.json
7. Football-C-rank-20261025-0909-1200-verified.json
8. Football-C-rank-20261025-MAIN-1500-0300-verified.json
9. Football-C-rank-20261026-0744-1100-verified.json

Total frozen assessed rows: **152**.

The current compiler funds G3 on **100/152** frozen rows.

## Challenger A — symmetric common G3 floor

Common minimum layer, applied before mechanism-specific funding:

- burden completion at least MEDIUM;
- effective continuation at least MEDIUM;
- effective stall no worse than MEDIUM;
- route reliability, chance quality, failure resistance, evidence confidence and burden protection at least MEDIUM;
- no material suppression;
- no route-attacking failure.

Carrier status cannot bypass the layer.

### Structural result

- champion funded G3: 100
- challenger A funded G3: 98
- newly funded: 0
- removed: 2

Removed rows:

| Board | Match | FT | 3+ |
|---|---|---:|---:|
| 24 Oct 18:00–00:00 | West Ham United–Southampton | 2–3 | yes |
| 25 Oct 00:00–07:30 | CF Montréal–Nashville SC | 0–2 | no |

The stricter common floor removes one true positive and one false positive. It does not improve separation enough to justify the recall loss.

**A decision: FAIL promotion.**

## Challenger B — carrier corroboration gate

Layer challenger A with an additional independent current-football corroborator for CARRIER_G3. A carrier must have at least one of:

- HIGH current chance quality;
- HIGH independent-route quality;
- HIGH opponent leakage;
- HIGH failure resistance;
- independently verified expansive tournament pressure.

Step-0 historical-rate support is corroboration only and is not sufficient by itself.

### Structural result

- challenger B funded G3: 85
- champion G3 rows removed: 15
- carrier-funded rows: 81 → 59

The 15 removed champion rows later produced **9/15 matches with 3+ goals**:

- Al-Shabab–Al-Samail — 2–1
- Al Ahli–Al Khaleej — 4–1
- NTV Beleza W–AS Elfen Saitama W — 1–0
- Escorpiones–Sporting FC — 2–4
- Sanfrecce Hiroshima–Shimizu S-Pulse — 4–0
- Jeonnam Dragons–Daegu FC — 2–4
- West Ham United–Southampton — 2–3
- Valencia–Villarreal — 1–2
- CF Montréal–Nashville SC — 0–2
- Alverca–Arouca — 0–1
- Nagoya Grampus–Yokohama F.Marinos — 1–1
- Manchester United–AFC Bournemouth — 0–3
- Genk–Standard Liège — 2–1
- Cheongju–Yongin — 0–2
- AZ Alkmaar–Twente — 0–2

This is a **60% G3 recall loss inside the removed cohort**, including legitimate one-team/carrier and mixed-route winners.

**B decision: HARD FAIL — unacceptable recall collapse.**

## Challenger C — carrier hardening plus relaxed two-sided cliff

Test the carrier common layer together with a genuinely two-sided G3 path that accepts MEDIUM completion/continuation when:

- both current routes are usable;
- one route is STRONG;
- carrier is at least USABLE;
- opponent leakage is at least MEDIUM;
- effective stall is no worse than MEDIUM;
- the common evidence/failure floor is satisfied.

This intentionally does not require every relevant grade to be HIGH.

### Structural result

- champion funded G3: 100
- challenger C funded G3: 104
- newly funded: 6
- removed: 2

Changed rows and outcomes:

| Board | Match | Champion | Challenger C | FT | 3+ |
|---|---|---|---|---:|---:|
| 24 Oct 18:00–00:00 | West Ham United–Southampton | G3 | no G3 | 2–3 | yes |
| 25 Oct 00:00–07:30 | CF Montréal–Nashville SC | G3 | no G3 | 0–2 | no |
| 25 Oct 00:00–07:30 | Vitória–Athletico Paranaense | no G3 | G3 | 1–1 | no |
| 25 Oct 09:09–12:00 | Sydney Olympic–Bayswater City | no G3 | G3 | 1–2 | yes |
| 25 Oct 09:09–12:00 | Albirex Niigata–Vegalta Sendai | no G3 | G3 | 2–1 | yes |
| 25 Oct 09:09–12:00 | Blaublitz Akita–FC Imabari | no G3 | G3 | 1–0 | no |
| 25 Oct main | CS Afumați–Steaua București | no G3 | G3 | 1–3 | yes |
| 25 Oct main | Hibernian–Celtic | no G3 | G3 | 1–2 | yes |

The six recovered rows reach 3+ in **4/6**. The two removed rows reach 3+ in **1/2**.

Net movement across the changed cohort:

- +4 recovered G3 winners;
- +2 newly admitted G3 misses;
- -1 old G3 miss;
- -1 old G3 winner;
- net: **+3 true positives, +1 false positive**.

That is directionally better, but the positive recovery occurs only on the 25 October boards. The only non-25-Oct changed fixture is West Ham–Southampton on 24 October, and that change is a false negative.

The handoff promotion gate explicitly prohibits promotion when improvement exists only on 25 October.

**C decision: FAIL promotion gate despite promising Oct-25 recovery. Keep as challenger only.**

## Challenger D — mechanism identity later in the ranking key

Structural ordering tested:

1. funded G3;
2. execution robustness;
3. endpoint/stall control;
4. completion + continuation;
5. current chance / route quality;
6. clearability;
7. certificate depth;
8. mechanism identity as a late tie-breaker.

This was not promoted independently because its funding prerequisite failed.

The important diagnostic is that it **does not solve the Oct-25 O4.5 problem**. Barcelona–Real Madrid, Freiburg–Bayern and Sparta Rotterdam–Ajax remain extremely strong on the earlier robustness/completion/current-route dimensions, so simply moving CARRIER later does not stop their O4.5 burden from ranking highly.

**D decision: NO independent promotion. Ranking order cannot compensate for an over-certified burden.**

## Burden diagnostic

The expanded replay already showed the critical separation:

- Barcelona–Real Madrid — reasonable G3 match, O4.5 failed at 1–2;
- Freiburg–Bayern — 4 goals, O4.5 failed at 1–3;
- Sparta Rotterdam–Ajax — 3 goals, O4.5 failed at 1–2.

These are not equivalent to a bad goal-match selection. They are burden errors.

Therefore future replay/reporting must preserve two independent axes:

1. **selection correctness** — should the match receive goal-match priority?
2. **burden correctness** — what is the highest independently justified total?

A ranking change must not use certificate depth as a substitute for match quality, and a burden repair must not be fitted from final scores.

## Final promotion decision

No new G3/ranking predictive change clears the 23–26 October promotion gate.

- Champion: retain for G3 funding.
- Challenger A: reject.
- Challenger B: reject hard; recall collapse.
- Challenger C: keep in challenger status; promising but Oct-25-local and regresses West Ham–Southampton.
- Challenger D: do not promote independently.
- /xi: untouched.

The strongest proven production result from the expanded replay remains the CONTROL_REVIEW zero-authority repair.

Separately, the already-promoted global-clearability FOLLOW allocator failed the expanded predictive replay: it improved semantic quality scores but reduced exact certificate clears. Under the handoff freeze, this challenger replay does **not** alter that allocator in production; its rollback/hold remains the next rank-policy action to resolve explicitly.

## Primary diagnosis

Football C still exhibits selection inversion because the remaining problem is not one scalar threshold:

- CARRIER_G3 is structurally easier to fund than two-sided mechanisms;
- a naive carrier corroboration gate destroys too much legitimate recall;
- relaxing the two-sided cliff recovers useful matches, but the current sample does not yet prove the change outside 25 October;
- ranking cannot repair a certificate that is itself too deep;
- selection quality and supported burden must therefore be calibrated separately.

**No outcome-fitted production threshold has been introduced.**
