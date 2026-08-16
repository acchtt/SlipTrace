# MODEL RULES — LEAGUE OF LEGENDS v0.3.58

**Status:** ACTIVE CANONICAL MODEL  
**Original effective date:** 2026-08-14 UTC+7  
**Canonical amendment date:** 2026-08-16 UTC+7  
**Supersedes:** v0.3.57 only where stated; later v0.3.59/v0.3.60 analytical versions are retired from active use by current governance

## Purpose

v0.3.58 remains the canonical analytical model.

Its original purpose was to correct a favorite -kills false-PASS pattern revealed by T1 vs DK Game 1: the model recognized terminal pressure but waited for Baron/inhibitor confirmation before sufficiently pricing future kill-margin expansion.

Reference review:
`models/lol/reviews/T1_DK_G1_FAVORITE_HANDICAP_FORCED_FIGHT_DENSITY_REVIEW_2026-08-14.md`

On 2026-08-16, the user explicitly retained v0.3.58 as the canonical version, discarded later analytical versions from active use, and authorized an in-place Duration correction after KRX vs BRO Game 2.

Duration amendment reference:
`models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

---

## 1. Baron and inhibitor are NOT mandatory favorite-handicap gates

For **favorite -kills**, existing Baron ownership and existing inhibitor destruction are not mandatory prerequisites for a TAKE.

They remain strong supporting evidence of terminal pressure, but absence of Baron/inhibitor must not by itself force PASS/HOLD.

Where retained rules or prior live interpretation treated Baron/inhibitor as required confirmation before favorite -kills, **v0.3.58 supersedes that interpretation**.

## 2. Mandatory Forced-Fight Density assessment

Before a favorite -kills TAKE, estimate whether the remaining game state creates enough **Forced-Fight Density (FFD)** to expand the signed kill margin before the game ends.

Classify FFD:

- `LOW` — underdog can avoid or safely concede most remaining pressure; favorite can close through structures/objectives without repeated combat;
- `MEDIUM` — some mandatory contest windows exist, but cross-map, waveclear or safe concession can delete several fights;
- `HIGH` — multiple scheduled windows force the underdog into pressured entry/defense and the favorite has reliable access/continuation to convert those windows into kills.

Mandatory inputs:

1. current signed kill margin;
2. **Required Net Expansion (RNE)** — additional net kill margin needed to cover the executable line;
3. role-weighted economy / TEI and lead quality;
4. dragon/Soul schedule;
5. Baron availability or imminent Baron window — ownership is not required;
6. tower/base-pressure schedule;
7. favorite initiation/access reliability and continuation;
8. underdog ability to cross-map, waveclear, disengage, trade objectives, or safely concede;
9. underdog reset/survival quality when forced to enter contested space;
10. Structure Substitution — whether the favorite can end through structures while deleting the very fights needed for the handicap.

## 3. Required Net Expansion must be explicit

For favorite -kills, compute the current signed kill margin and the additional net margin required to cover the line.

Example:

- current margin: favorite +8 kills;
- market: favorite -15.5;
- cover requires final margin >=16;
- `RNE = +8` additional net kills from the decision point.

Do not evaluate a favorite handicap from lead size alone. The question is whether the remaining forced-fight schedule can realistically generate the RNE before terminal state.

## 4. Pre-Baron favorite -kills can qualify

A favorite -kills position may qualify **before Baron or inhibitor** when all retained live-eligibility controls pass and the following are jointly strong:

- two-snapshot live gate satisfied;
- favorite has materially positive economy/role distribution and lead quality;
- FFD = HIGH;
- the underdog has limited low-risk ways to avoid scheduled contests;
- favorite has reliable access/forcing and continuation into those contests;
- RNE is supportable by the expected remaining fight count and signed-margin distribution;
- NKB / RFI / KCV / Structure Substitution do not negate the cover branch;
- exact executable odds are >=1.60.

This is an eligibility path, not an automatic TAKE.

## 5. Anti-overfit guard

Do **not** infer HIGH FFD from any one signal by itself, including:

- 3–0 dragons;
- large gold lead;
- current kill lead;
- favorite TEAM edge;
- strong engage composition;
- imminent Baron;
- one won teamfight.

The scheduled fights must be materially difficult for the underdog to avoid, and the favorite must have a credible mechanism to turn those fights into **net kill-margin expansion**, not merely objective/structure conversion.

## 6. Reference correction — T1 vs DK G1

At 20:27:

- T1 16–8 DK;
- T1 approximately +5.4k gold;
- towers 3–1 T1;
- dragons 3–0 T1;
- Baron 0–0;
- inhibitors 0–0;
- T1 -15.5 kills @1.617.

Current signed margin: `+8`.  
Required final margin: `+16`.  
Required Net Expansion: `+8`.

The 3–0 dragon schedule, imminent Baron schedule, T1's access/continuation, large economy edge and DK's limited ability to avoid future pressured contests created **HIGH FFD** despite no Baron or inhibitor already secured.

Under v0.3.58, assuming the line remained visibly executable, the reference verdict is:

**TAKE — T1 -15.5 kills @1.617 — shadow 0.25u; actual 0u.**

Final: T1 30–11 DK, margin +19.

---

# 7. Canonical Duration amendment — Structure Substitution and real stall evidence

This section is an in-place v0.3.58 correction authorized on 2026-08-16 after the KRX vs BRO Game 2 Over 33 loss.

It supersedes conflicting v0.3.58-and-earlier live interpretation of Duration Over evidence.

## 7.1 Low activity is not positive stall evidence by itself

For Duration analysis, each of the following is **neutral by default**:

- low kill count;
- 0-0 towers;
- no first tower yet;
- low absolute tower count;
- no inhibitor yet;
- quiet elapsed game time.

These describe what has happened, not whether the future clock will be consumed slowly.

Do not reason:

- “few kills therefore Over”;
- “0-0 towers supports Over”;
- “only one tower has fallen therefore the game is stalled”;
- “nothing has happened yet, so the map should run long.”

A Duration Over requires positive evidence that **future conversion is likely to be delayed**, not merely a quiet history.

## 7.2 Mandatory conversion classification

Before every Duration Over, classify structure/conversion evidence as one of:

### `ABSENT CONVERSION`

No meaningful conversion opportunity has occurred, or no meaningful opportunity has been demonstrably denied.

Examples:

- no first tower because neither side has created a real siege/tempo window;
- low tower count while objectives are being traded normally;
- low kills while a team is still converting dragons, towers, waves or map control.

**Effect:** neutral for Over.

### `FAILED CONVERSION`

A team obtained a meaningful fight win, tempo window, objective leverage, numbers advantage, wave access, siege position or map-pressure window and then failed to create expected structural/base progress because the opponent actually defended, reset, wavecleared, disengaged, cross-mapped or otherwise denied conversion.

**Effect:** may count as observed stall evidence.

A scoreboard alone cannot convert `ABSENT` into `FAILED`.

## 7.3 Structure Substitution is mandatory

Duration and Total Kills are separate distributions.

Low kills can coexist with fast map progress when a team converts through:

- dragons;
- Herald/grubs;
- towers;
- lane pressure;
- cross-map trades;
- Baron threat;
- serial structure access.

This is **Structure Substitution**.

If a team is progressing objectives/structures while kills stay low, that is not automatically stall. It can be evidence that the game is advancing **without needing combat**, which can compress the remaining clock.

Therefore low kill pace may not independently satisfy a Duration stall mechanism.

## 7.4 Mandatory Over gate

Before a Duration Over TAKE, all retained Duration timing / persistence / survival-horizon / dead-zone controls still apply, and the following must also be true:

1. At least **two independent positive clock-consuming mechanisms** are observed and relevant to the future game state.
2. At least one mechanism must be based on **observed FAILED CONVERSION** or another clearly observed repeated defense/reset/waveclear mechanism — not mere inactivity.
3. Low kills, 0-0 towers, no first tower, or a low tower count cannot count as either mechanism by themselves.
4. If the evidence is primarily `ABSENT CONVERSION`, verdict is `HOLD/PASS`, never TAKE Over.
5. If objective/structure progress is occurring despite low kills, explicitly test Structure Substitution before calling the map slow.
6. Missing or ambiguous decision-critical conversion evidence is fail-closed: `HOLD/PASS`.

Low Duration bet frequency is acceptable.

## 7.5 Mandatory cascade check

Before every Duration Over, test the shortest realistic path:

`next compulsory fight/objective -> next structure -> serial structures -> base access -> Nexus`

Explicitly ask:

**“What happens if the next compulsory fight is lost?”**

If one realistic fight/objective sequence can create a nonlinear structure cascade materially inside the market survival horizon, the Over must not use a quiet early/midgame as protection.

Objective schedules can consume time, but they can also **compress** the clock by forcing the fight that opens the base.

## 7.6 KRX vs BRO Game 2 reference correction

At 14:52:

- BRO 1-0 KRX kills;
- KRX approximately +860 gold;
- KRX 1-0 towers;
- KRX 1-0 dragons;
- Baron 0-0;
- Over 33 minutes @1.690.

Historical v0.3.58 live verdict:

**TAKE — Over 33 minutes @1.690 — shadow 0.25u; actual 0u.**

Result: LOSS.

Correct v0.3.58 classification after review:

- low kills: descriptor only;
- structural evidence: `ABSENT CONVERSION`, not demonstrated failed conversion;
- KRX already showed Structure Substitution through tower + dragon progress;
- no sufficient observed stall mechanisms;
- one later compulsory objective/fight could still unlock serial conversion.

**Correct verdict: PASS — Over 33 minutes @1.690 — 0u.**

At 17:52 the game still had only one total kill, yet KRX had progressed to 2-0 dragons and 2-1 towers. This confirms the diagnostic point: **low kills did not imply low game-ending velocity.**

---

## 8. Retained controls

All non-conflicting v0.3.57 and earlier controls remain active, including:

- underdog +kills fallback certification and False-Stable Guard;
- v0.3.56 HIGH-DCR + weak-FF hard veto;
- Draft Primacy and position-blind reassessment;
- MKT + TEAM anchoring;
- Role-Weighted Economy / TEI;
- two-snapshot live eligibility for ML/KH/TK;
- side-neutral signed kill-margin distribution;
- NKB / RFI / KCV / Structure Substitution;
- Handicap Buffer Retention;
- Total Kills OKP/FCI/CRR/SRR/BF/CL/RKS/KPW framework;
- stale-line gate;
- same-game correlation decomposition;
- retained Duration timing, persistence, dead-zone, probability-buffer and regime-change restrictions from earlier rules, as modified by Section 7 above;
- no rescue/martingale/loss chasing.

Favorite -kills remains independent. A blocked underdog +kills position never automatically implies a favorite -kills TAKE.

Where this file conflicts with later retired analytical versions, **the current canonical v0.3.58 file controls for new analysis.**
