# MODEL RULES — LEAGUE OF LEGENDS v0.3.54

**Status:** Active delta  
**Effective date:** 2026-08-12 UTC+7  
**Supersedes:** v0.3.53 only where stated

## Purpose

Correct a deterministic live-state representation error identified in HLE Challengers vs BRO Challengers Game 1: raw team gold was treated as approximately neutral even though visible role-level gold was materially concentrated on BRO's higher-leverage late-game threats.

Reference review:
`models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`

This update qualifies under the v0.3.53 deterministic-correctness exception. It does **not** create a new one-map directional betting heuristic.

Official betting remains paused. Shadow calibration remains active.

---

## 1. Role-Weighted Economy (RWE) — Mandatory When Visible

For live Moneyline analysis, and for late-game Kill Handicap / Total Kills repricing when economy distribution changes terminal-fight quality, do not reduce economy to total team gold when role-level gold is visible.

Record:

### `RGV` — Role Gold Vector
The visible gold advantage by role/champion pair.

Example representation:
- Top: Team A +X
- Jungle: Team B +Y
- Mid: Team A +Z
- ADC: Team B +W
- Support: Team A +Q

### `GLC` — Gold Leverage Class
Classify each champion's marginal gold leverage in the current game state:

- `HIGH` — primary DPS/scaling carry, terminal side-lane threat, or champion whose extra economy directly increases closing power;
- `MEDIUM` — secondary carry/bruiser or mixed damage/utility;
- `LOW` — primarily engage/tank/utility where extra gold has lower marginal closing value.

GLC is champion/function specific. Do **not** use rigid universal role weights.

### `GCQ` — Gold Concentration Quality
Classify which side has the more valuable distribution of gold after applying GLC.

Possible states:
- `A FAVORED`
- `B FAVORED`
- `NEUTRAL/MIXED`

Raw team-gold parity does not imply economic parity when GCQ is materially asymmetric.

---

## 2. ML Economic-Neutrality Veto

For any live ML TAKE:

- if role-level gold is visible, RGV + GLC + GCQ must be evaluated before the verdict;
- if team gold is near even but GCQ materially favors one side, do **not** describe the state as economically neutral;
- if role-level gold is visible but not parsed, ML TAKE is ineligible and defaults HOLD/PASS;
- if role-level gold is unavailable, do not infer or fabricate it; retain team-gold analysis with an uncertainty penalty.

This rule overrides any earlier shorthand that treats near-even team gold as sufficient evidence of balanced late-game economy.

---

## 3. Terminal Economy Interaction (TEI)

After 30:00, combine RWE with objective terminality.

Classify objective control as:

- `LOW TERMINALITY`
- `MEDIUM TERMINALITY`
- `HIGH TERMINALITY`

HIGH TERMINALITY examples include combinations such as:
- soul / four-dragon control;
- Baron with meaningful map access;
- inhibitor/base exposure;
- multiple stacked terminal objectives.

### TEI hard downgrade
A comeback ML against a side with both:

1. `HIGH TERMINALITY` objective control, and
2. favorable `GCQ` concentrated on HIGH-leverage champions,

must receive a major probability downgrade.

Kill lead, assist count, or superficially near-even team gold cannot independently override this combination.

A TAKE on the comeback side requires observed live proof that the terminal threats are being suppressed, for example:

- Baron expires with negligible conversion;
- soul/dragon control cannot produce map access;
- high-leverage carry is repeatedly denied position/access;
- side-lane pressure is neutralized;
- the supposedly advantaged economy cannot convert across more than one synchronized state.

Without such proof, default PASS/HOLD.

---

## 4. Mandatory Internals Update

Before any live ML TAKE, add these fields to the existing v0.3.53 checklist when role-level data are visible:

1. `RGV`
2. `GLC`
3. `GCQ`
4. objective terminality class
5. `TEI` interaction result

For late-game Kill Handicap and Total Kills, apply the same overlay when economy concentration materially changes expected fight cleanliness, return-kill probability, side-lane pressure, or closing speed.

Missing visible role-level data parsing => HOLD/PASS.

---

## 5. HLE-BRO G1 Reference Error

At the 36:09 HLE ML @5.952 entry:

- HLE led kills 13-7;
- raw gold was close;
- BRO held four dragons and Baron;
- BRO's visible role economy included large advantages on K'Sante and Corki;
- HLE's largest visible advantage was concentrated on Vi, with smaller utility advantages elsewhere.

The model incorrectly compressed this into approximately neutral economy and overestimated HLE's comeback branch.

The corrected interpretation is:

> BRO's objective state was terminal/near-terminal and its gold concentration was more valuable for late-game closing than the raw team-gold number implied.

---

## 6. Retained v0.3.53 Controls

All v0.3.53 controls remain active, including:

- two-snapshot live eligibility;
- stale-line freshness gate;
- MKT + TEAM anchor;
- anti-favorite guard;
- mechanism-independence/shared-failure penalty;
- Handicap Buffer Retention;
- two-sided Structure Substitution;
- Total Kills RKS / KPW / future-window deletion;
- fade benchmark audit;
- same-game shadow calibration;
- position-blind reassessment;
- no rescue/martingale/loss chasing.

Where role-level economy is visible, v0.3.54 RWE/TEI is mandatory and controls over simpler team-gold summaries.

---

## 7. Operating State

- Active model: **LoL v0.3.54**
- Official betting: **PAUSED**
- Shadow mode: ACTIVE
- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/Total Kills TAKE: DISABLED
- Duration restrictions: unchanged
- Same-game multiple shadow positions: ENABLED after eligibility

Where this delta conflicts with v0.3.53 or earlier interpretation, **v0.3.54 controls**.
