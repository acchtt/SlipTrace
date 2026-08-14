# MODEL RULES — LEAGUE OF LEGENDS v0.3.58

**Status:** Active delta  
**Effective date:** 2026-08-14 UTC+7  
**Supersedes:** v0.3.57 only where stated

## Purpose

Correct a favorite -kills false-PASS pattern revealed by T1 vs DK Game 1: the model recognized terminal pressure but waited for Baron/inhibitor confirmation before sufficiently pricing future kill-margin expansion.

Reference review:
`models/lol/reviews/T1_DK_G1_FAVORITE_HANDICAP_FORCED_FIGHT_DENSITY_REVIEW_2026-08-14.md`

## 1. Baron and inhibitor are NOT mandatory favorite-handicap gates

For **favorite -kills**, existing Baron ownership and existing inhibitor destruction are no longer mandatory prerequisites for a TAKE.

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

## 7. Retained controls

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
- Duration restrictions;
- no rescue/martingale/loss chasing.

Favorite -kills remains independent. A blocked underdog +kills position never automatically implies a favorite -kills TAKE.

Where this delta conflicts with earlier favorite-handicap confirmation language, **v0.3.58 controls**.
