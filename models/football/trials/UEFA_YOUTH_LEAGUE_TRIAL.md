# UEFA Youth League Trial Memory

**Status:** ACTIVE MANUAL TRIAL — NON-OFFICIAL  
**Competition:** UEFA Youth League / U19  
**Last full audit:** 2026-09-10 ICT  
**Official-model boundary:** U19/youth remains excluded from the normal Football v0.2.50 actionable board unless a later repo change explicitly promotes it.

This file is the persistent cross-chat record for UYL-specific results, trial decisions, calibration and audit lessons. When the user explicitly asks to assess, continue, review, audit, or fetch UEFA Youth League / U19 trial matches, load this file in addition to the official stack.

Do not use this file to silently whitelist youth football for the normal production sweep.

---

## 1. Result authority for this trial

For the 2026/27 opening round, the user's Soccerway results screenshot is the reconciled result authority. Earlier third-party web result fetching returned several incorrect scores and must not be reused for settlement or audit.

Correct opening-round results:

| Date | Match | Final | Total |
|---|---|---:|---:|
| 8 Sep | AEK U19 vs LASK U19 | 0–0 | 0 |
| 8 Sep | FC Porto U19 vs Manchester City U19 | 3–1 | 4 |
| 8 Sep | Club Brugge U19 vs Aston Villa U19 | 5–3 | 8 |
| 8 Sep | Lille U19 vs Betis U19 | 0–0 | 0 |
| 8 Sep | Real Madrid U19 vs Inter U19 | 3–0 | 3 |
| 8 Sep | Dortmund U19 vs Villarreal U19 | 2–3 | 5 |
| 9 Sep | Stuttgart U19 vs Viking U19 | 5–0 | 5 |
| 9 Sep | Napoli U19 vs Arsenal U19 | 1–2 | 3 |
| 9 Sep | PSG U19 vs Slovan Bratislava U19 | 6–1 | 7 |
| 9 Sep | Sporting CP U19 vs Galatasaray U19 | 2–2 | 4 |
| 9 Sep | Liverpool U19 vs Atletico Madrid U19 | 2–2 | 4 |
| 10 Sep | Barcelona U19 vs Feyenoord U19 | 1–2 | 3 |
| 10 Sep | Fenerbahce U19 vs AS Roma U19 | 2–4 | 6 |
| 10 Sep | PSV U19 vs Shakhtar Donetsk U19 | 1–0 | 1 |
| 10 Sep | Slavia Prague U19 vs Lens U19 | 2–1 | 3 |
| 10 Sep | Manchester United U19 vs Sabah Baku U19 | 5–0 | 5 |
| 10 Sep | Como U19 vs RB Leipzig U19 | 1–1 | 2 |
| 10 Sep | Bayern U19 vs Bodo/Glimt U19 | 6–1 | 7 |

Opening-round aggregate:

- 18 matches
- 70 goals
- 3.89 goals per match
- Over 2.5: 14/18 = 77.8%
- Over 3.5: 10/18 = 55.6%
- Over 4.5: 7/18 = 38.9%
- exactly 3 goals: 4/18 = 22.2%
- exactly 4 goals: 3/18 = 16.7%
- 5+ goals: 7/18 = 38.9%
- 0–2 goals: 4/18 = 22.2%

**Audit interpretation:** UYL is genuinely high-scoring, but the distribution is highly volatile. The 3.89 average must not be treated as a stable per-match baseline: the same round contained four 0–2 goal matches and seven 5+ goal matches.

---

## 2. Most important opening-round discovery — carrier ceiling

High UYL totals were often created by one dominant attack rather than requiring a perfectly balanced two-sided game.

Opening-round evidence:

- 9/18 matches had at least one team score 3+
- 6/18 matches had at least one team score 4+
- of the 10 matches that reached 4+ total goals, 6 had a team score 4+
- of the 7 matches that reached 5+ total goals, 6 had a team score 4+

The six 4+ individual outputs were Club Brugge 5, Stuttgart 5, PSG 6, Roma 4, Manchester United 5, and Bayern 6.

**Trial conclusion:** for UYL, `CARRIER CEILING` deserves at least equal attention to two-sided structure, especially at O3.75+ burdens. Do not automatically rank a merely balanced two-sided matchup above an elite youth carrier with a credible independent 4+ ceiling.

For a proposed O3.75 or higher line, explicitly ask:

`CAN ONE TEAM PLAUSIBLY SCORE 4 BY ITSELF?`

A strong YES materially improves the case. A NO does not automatically kill the match, but then the two-sided route must be exceptionally strong.

---

## 3. Trial decision order after re-audit

Current UYL trial ordering:

`XI / STRUCTURAL VIABILITY -> ARCHETYPE + CARRIER CEILING -> MARKET GOAL PRIOR -> TEAM-PROFILE REFINEMENT -> SUPPORTED BURDEN -> LINE SELECTION`

This is a competition-specific trial ordering and intentionally differs from the official senior model.

### Market goal prior

The market remains useful, but the corrected results show it is not deterministic.

For comparable viable UYL matches:

- same total + shorter Over price = stronger market-implied goal prior;
- higher total at similar price = stronger market-implied goal prior;
- use this to rank close candidates and detect information not visible in noisy public youth data;
- do not allow market strength alone to override a clear XI/route defect;
- do not infer that the shorter-priced Over must realize more goals in one match.

Corrected same-slate examples are mixed:

- PSV–Shakhtar O3.75 ~1.77 vs Slavia–Lens O3.75 ~1.88: PSV had the stronger market prior but finished 1–0 while Slavia finished 2–1. Both stayed under the burden.
- Manchester United–Sabah carried the stronger observed goal-market signal than Como–Leipzig and finished 5–0 vs Como's 1–1. This supports the hypothesis directionally, but the exact Manchester United line/price should be reverified before quantitative modelling.
- Barcelona–Feyenoord carried an extreme O4.5 ~1.78 market yet finished 1–2; the trial's prematch HOLD at that burden was therefore correct.

**Conclusion:** market information should calibrate and break ties; it should not become a standalone selection engine.

---

## 4. Current UYL burden calibration

Do not treat O3.5 as an automatic UYL baseline merely because the competition average is high.

Working interpretation:

- O2.5 = very protected / low
- O3.0 = low
- O3.25 = protected and often useful for strong-but-not-extreme matches
- O3.5 = requires a genuine 4-goal route
- O3.75 = demanding; needs strong market + structure and preferably carrier support
- O4.0 = high
- O4.25 = high / extreme
- O4.5+ = demanding extreme burden; needs independently supported elite carrier/EGE-like conditions

Opening-round empirical break-even prices, using only this 18-match distribution and therefore **not** a forward fair-price model:

- blind O3.25: approximately 1.60
- blind O3.5: approximately 1.80
- blind O3.75: approximately 1.94

These numbers are descriptive only. They show why quarter-line protection mattered in this round and why O3.75 near the high-1.80s can still be demanding despite a 3.89 league average.

**Protected-line rule:** when structure is strong but the 4+ tail is not independently proven, prefer O3.25 over O3.5/O3.75 when the price sacrifice is reasonable. Never stretch upward merely for a prettier decimal price.

---

## 5. Executed UYL trial verdicts

These are trial verdicts only, not official Football v0.2.50 Website Picks.

| Match | Trial line | Final | Settlement |
|---|---:|---:|---:|
| Sporting CP U19 vs Galatasaray U19 | O3.5 @1.77 | 2–2 | WIN |
| Liverpool U19 vs Atletico Madrid U19 | O3.25 @1.88 | 2–2 | WIN |
| Barcelona U19 vs Feyenoord U19 | O3.25 @1.95 around 70' | 1–2 | HALF LOSS |
| Fenerbahce U19 vs Roma U19 | O3.5 @1.74 | 2–4 | WIN |
| Slavia Prague U19 vs Lens U19 | O3.75 @1.88 | 2–1 | LOSS |
| Como U19 vs RB Leipzig U19 | O3.5 @1.88 | 1–1 | LOSS |

Flat 1u P/L: **3W – 2L – 1HL = -0.11u**.

The six selected matches produced 22 goals = 3.67 goals/match. Five of six reached 3+ goals, but only three of six reached 4+.

**Selection audit:** the trial has been better at identifying matches likely to reach the general 3-goal zone than at separating the true 4+ tail. Since most selected lines were 3.25–3.75, that missing 3→4 separation is currently the main weakness.

### Missed/no-entry

PSG U19 vs Slovan Bratislava U19 finished 6–1. No executed entry is counted because PSG scored while the verdict was being formed and the market reset. Keep as a validated missed opportunity / NO BET, not P/L.

---

## 6. Match-by-match audit

### Sporting CP U19 vs Galatasaray U19 — WIN

O3.5 @1.77, final 2–2.

`GOOD TWO-SIDED SELECTION / APPROPRIATE 4-GOAL BURDEN`

Both sides contributed and the line matched the realized route.

### Liverpool U19 vs Atletico Madrid U19 — WIN

O3.25 @1.88, final 2–2.

`GOOD STRUCTURE + GOOD PROTECTION`

This remains the cleanest example of the benefit of O3.25: four goals won fully, while the quarter-line protected the downside if the game had stopped at three.

### Barcelona U19 vs Feyenoord U19 — HALF LOSS

Late O3.25 @1.95 around 70', final 1–2.

`LIVE DECAY SPOT — MARGINAL BURDEN / PROTECTION LIMITED DAMAGE`

The entry was not a goal-expansion chase, but competition-relative decay alone was given too much weight. At entry, with two goals already scored, one more goal still produced a half-loss and two more were required for a full win.

Future rule: after roughly 60', do not promote a UYL Over merely because the line has decayed into a visually low number. Require current live chance-quality/territory evidence and calculate exact remaining-goal burden before LOCK.

Also preserve the process fault: the score column was misread more than once. Future live UYL review must confirm `SCORE / MINUTE / CARDS / CURRENT TOTAL / PRICE` before analysis.

### Fenerbahce U19 vs Roma U19 — WIN

O3.5 @1.74, final 2–4.

`GOOD CARRIER-LED SELECTION / MARKET + ROUTE ALIGNED`

Roma produced four themselves and Fener contributed two. This is a strong example of why UYL carrier ceiling must not be subordinated automatically to two-sided labels.

### Slavia Prague U19 vs Lens U19 — LOSS

O3.75 @1.88, final 2–1. User reported many big chances missed.

`STRUCTURE BROADLY VALIDATED / CONVERSION UNDERPERFORMED / LINE TOO AGGRESSIVE`

The chance route apparently survived, so this is not a pure structural miss. But O3.75 exposed the trial to a full loss at exactly three goals. A protected O3.25 would have reduced settlement damage if available at an acceptable price.

### Como U19 vs RB Leipzig U19 — LOSS

O3.5 @1.88, final 1–1.

`RANKING / MATCH-SELECTION MISS`

The trial promoted Como too aggressively from noisy recent youth form and matchup research. The user observed that Manchester United–Sabah carried the stronger goal-market signal; United then finished 5–0 while Como finished 1–1.

This is the clearest opening-round example that public youth-form research should refine rather than dominate cross-match ranking.

---

## 7. What the audit changes

### A. High average does not justify high burden by itself

3.89 goals/match is real, but the round was highly dispersed. Do not turn the league average into a universal O3.5 or O3.75 permission slip.

### B. Separate 3+ detection from 4+ detection

Current trial screening is reasonably good at finding 3-goal environments but not yet good enough at isolating the 4+ tail. Before O3.5+, require an explicit 4+ mechanism rather than generic youth volatility.

### C. Carrier ceiling becomes a first-class UYL signal

For O3.75+ in particular, a credible independent 4+ team ceiling is highly valuable. Elite carrier routes may outrank merely balanced two-sided games.

### D. Market prior stays important but secondary to viable mechanism

Use it to compare close matches and expose hidden information. Do not elevate it into a deterministic rule after one round.

### E. Downweight tiny recent-form samples

Recent 4–2, 5–3, 7–1 type youth scores are useful context but are too noisy to dominate ranking. Team form should confirm a route, not manufacture one.

### F. Late live entries need live evidence

After 60', line decay is not enough. Require current chance quality plus exact remaining-goal burden.

### G. Result integrity is part of the model process

For settlement/audit, prefer user-supplied Soccerway or competition-source reconciliation when web feeds conflict. Do not let an unverified result overwrite the trial record.

---

## 8. Early team watch flags

These are one-round watch flags, not permanent classifications. Revalidate current form, XI and market next time.

### Individual 4+ carrier outputs

- Bayern U19 — 6
- PSG U19 — 6
- Club Brugge U19 — 5
- Stuttgart U19 — 5
- Manchester United U19 — 5
- AS Roma U19 — 4

### Other useful 3+ outputs

- Porto U19 — 3
- Real Madrid U19 — 3
- Villarreal U19 — 3

### High-event opening-round fixtures

- Club Brugge / Aston Villa — 8 total
- Bayern / Bodo/Glimt — 7
- PSG / Slovan Bratislava — 7
- Fenerbahce / Roma — 6
- Dortmund / Villarreal — 5
- Stuttgart / Viking — 5
- Manchester United / Sabah — 5
- Porto / Manchester City — 4
- Liverpool / Atletico Madrid — 4
- Sporting CP / Galatasaray — 4

PSV U19 is **not** a high-event flag from this round; PSV–Shakhtar finished 1–0.

---

## 9. Future UYL workflow

For the next UYL slate:

1. keep the competition outside the official senior board unless explicitly running this trial;
2. confirm fixture/result identity carefully;
3. inspect XI and basic structural viability;
4. classify `TWO-SIDED`, `ELITE CARRIER`, `CARRIER-LED`, or `FRAGILE`;
5. explicitly assess independent 4+ carrier ceiling when considering O3.75+;
6. compare market goal priors across otherwise viable matches;
7. use recent team form as refinement, not dominant ranking evidence;
8. set a supported burden before choosing price;
9. prefer O3.25 protection for strong-but-not-extreme profiles when price remains usable;
10. require a genuine 4-goal mechanism for O3.5 and stronger evidence again for O3.75+;
11. after 60' live, require current chance-quality evidence plus exact remaining-goal burden;
12. never chase early-goal line expansion;
13. record final, settlement, chance-quality notes and market-ordering lessons back into this file.

The trial objective is to identify which UYL matches reliably reach the 4+ tail, not merely to observe that the competition is high scoring overall.
