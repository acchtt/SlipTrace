# UEFA Youth League Trial Memory

**Status:** ACTIVE MANUAL TRIAL — NON-OFFICIAL  
**Competition:** UEFA Youth League / U19  
**Purpose:** Persistent cross-chat record for UYL-specific observations, trial decisions, results, calibration lessons, and early team flags.  
**Official-model boundary:** U19/youth remains excluded from the normal Football v0.2.50 actionable board unless a later repo change explicitly promotes it.

This file exists so UYL trial knowledge is not trapped inside one chat. When the user explicitly asks to assess, continue, review, audit, or fetch UEFA Youth League / U19 trial matches, load this file in addition to the official stack.

Do not use this file to silently whitelist youth football for the normal production sweep.

---

## 1. Trial decision philosophy

UYL is a separate competition-relative experiment. Do not blindly apply senior-football absolute total thresholds.

Current trial ordering:

`XI / STRUCTURAL VIABILITY -> MARKET GOAL PRIOR -> TEAM-PROFILE REFINEMENT -> LINE SELECTION`

The market goal prior is a ranking/calibration signal, not a standalone reason to bet.

For comparable UYL matches:

- same total line + shorter Over price = stronger market-implied goal environment;
- higher total at a similar Over price = stronger market-implied goal environment;
- a 0.25-higher line with only slightly longer price can still indicate the stronger environment;
- structural research should override the market ordering only when there is a clear XI/route defect, not merely because another team's recent scoreline sample looks more explosive.

This differs intentionally from the official senior model, where price comes much later.

---

## 2. Current UYL burden calibration

Do **not** treat O3.5 as an automatic or universally safe UYL baseline.

Working interpretation:

- O2.5 = very protected / low
- O3.0 = low
- O3.25 = protected
- O3.5 = common but still requires genuine 4-goal support
- O3.75 = demanding enough that market strength matters materially
- O4.0 = high
- O4.25 = high / extreme matchup
- O4.5+ = demanding; requires independently supported extreme environment

Protected lines matter. If a match has strong-but-not-extreme UYL structure, O3.25 may be preferable to O3.5/O3.75 when the price sacrifice is reasonable because exactly 3 goals materially reduces damage.

Never stretch upward merely for a better decimal price.

---

## 3. Repeated market-ranking lesson — 10 Sep 2026

### PSV U19 vs Shakhtar U19 versus Slavia Prague U19 vs Lens U19

Observed prematch/live early market:

- PSV–Shakhtar O3.75 approximately 1.77
- Slavia–Lens O3.75 approximately 1.88

Same line, shorter PSV Over price = market assigned the stronger 4+ goal prior to PSV.

Finals:

- PSV–Shakhtar 2–2 = 4 goals
- Slavia–Lens 2–1 = 3 goals

This does not prove market infallibility, but it is a clean same-slate example where the market ordering was directionally better than the trial's structural ranking.

### Como U19 vs RB Leipzig U19 versus Manchester United U19 vs Sabah U19

The user observed the same directional pattern: the Manchester United match carried the stronger goal-market signal than Como, while the trial research promoted Como too aggressively.

Finals:

- Como–RB Leipzig 0–2 = 2 goals
- Manchester United–Sabah 2–1 = 3 goals

Exact comparative line/price for the Manchester United example should be reverified from the original screenshot before quantitative use, but the qualitative ranking lesson is retained.

**Current conclusion:** UYL public team-form data is noisy enough that the bookmaker total/Over price should receive more weight when ranking otherwise viable matches against each other.

---

## 4. Model-issued UYL trial verdict log

These are **trial verdicts**, not official Football v0.2.50 Website Picks. Do not mix them into official P/L unless the repository later creates an explicit trial accounting contract.

| Match | Trial line | Final | Trial settlement |
|---|---:|---:|---:|
| Sporting CP U19 vs Galatasaray U19 | O3.5 @1.77 | 2–2 | WIN |
| Liverpool U19 vs Atletico Madrid U19 | O3.25 @1.88 | 2–2 | WIN |
| Barcelona U19 vs Feyenoord U19 | O3.25 @1.95 around 70' | user-reported 1–2 | HALF LOSS |
| Fenerbahce U19 vs Roma U19 | O3.5 @1.74 | 0–2 | LOSS |
| Slavia Prague U19 vs Lens U19 | O3.75 @1.88 | 2–1 | LOSS |
| Como U19 vs RB Leipzig U19 | O3.5 @1.88 | 0–2 | LOSS |

### Missed / no-entry case

PSG U19 vs Slovan Bratislava U19 finished 6–1. The trial did not count an executed entry because PSG scored while the verdict was being formed and the market reset. Preserve as a validated missed opportunity / NO BET, not P/L.

### Result-integrity note

For Barcelona U19 vs Feyenoord U19, preserve the user's reported final 1–2 as the trial record unless a later explicit reconciliation is performed. A separate fetched feed previously showed 0–2, so the historical source discrepancy should not be silently overwritten.

Feyenoord also received a red card in that match; red-card timing was not preserved and must not be invented.

---

## 5. Match-specific audit notes

### Slavia Prague U19 vs Lens U19

Final 2–1. User reported many big chances missed.

Audit tag:

`STRUCTURE BROADLY VALIDATED / CONVERSION UNDERPERFORMED`

The loss does not automatically mean the matchup thesis was structurally poor. However, line selection was aggressive: O3.75 required four goals for meaningful success, while a protected O3.25 would have reduced damage at exactly three goals.

### Barcelona U19 vs Feyenoord U19

Live process error occurred: the score column was misread more than once. Future live UYL assessments must explicitly confirm score, minute, cards, and current total before interpreting line movement.

The late O3.25 @1.95 entry illustrated another key point: a line can look low in absolute UYL terms while still requiring two additional goals for a full win. Competition-relative decay alone is not enough; always calculate exact remaining-goal burden.

---

## 6. Early high-scoring / high-event team watch flags

These are **one-slate watch flags only**, not permanent team classifications. Revalidate current season form, XI and market next time.

### Strong individual scoring output observed in the opening slate

- PSG U19 — scored 6
- Club Brugge U19 — scored 5
- Stuttgart U19 — scored 5
- Porto U19 — scored 3
- Real Madrid U19 — scored 3
- Villarreal U19 — scored 3

### High-event opening-slate participants worth early attention

- PSG U19
- Club Brugge U19
- Stuttgart U19
- Porto U19
- Villarreal U19
- Liverpool U19
- Sporting CP U19
- PSV U19

Other teams from the same high-total games may also deserve attention, but no team should be promoted solely from one result.

---

## 7. Future UYL workflow

When a new UYL slate appears:

1. keep it outside the official senior board unless explicitly running the manual trial;
2. identify confirmed XI and basic structural viability;
3. compare the market-implied goal environment across the slate, especially equivalent total lines;
4. use team form/profile to refine rather than dominate cross-match ranking;
5. calculate exact burden at the proposed Asian total;
6. prefer protection when the match is strong but not truly extreme;
7. never chase a line expanded by an early goal;
8. record trial decision, price, final, chance-quality notes if supplied, and any market-ordering lesson back into this file.

The goal of the trial is not to prove that UYL is always high scoring. It is to learn which UYL matches and market states reliably separate ordinary 2–3 goal games from genuine 4+ environments.
