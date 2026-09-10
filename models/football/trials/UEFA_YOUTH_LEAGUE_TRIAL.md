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

Important: the opening-round results show that the market prior is useful but not infallible. Do not treat one same-slate price comparison as deterministic evidence.

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

## 3. Correct opening-round results — 8–10 Sep 2026

User-supplied Soccerway results screenshot is the current authoritative reconciliation source for this trial record.

| Date | Match | Final | Total goals |
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

Opening-round aggregate from these 18 reconciled results:

- 70 total goals
- 3.89 goals per match
- Over 2.5: 14/18 (77.8%)
- Over 3.5: 10/18 (55.6%)
- Over 4.5: 7/18 (38.9%)

These league-phase opening results confirm a high overall goal environment, but the distribution remains uneven enough that match selection and line burden still matter.

---

## 4. Market-ranking lessons — evidence is mixed

### PSV U19 vs Shakhtar U19 versus Slavia Prague U19 vs Lens U19

Observed early market:

- PSV–Shakhtar O3.75 approximately 1.77
- Slavia–Lens O3.75 approximately 1.88

Same line, shorter PSV Over price indicated the stronger market-implied 4+ goal prior.

Correct finals:

- PSV–Shakhtar 1–0 = 1 goal
- Slavia–Lens 2–1 = 3 goals

Therefore this comparison **did not validate** the shorter-Over-price ordering in realized goals. Preserve it as a caution that market strength is informative but not deterministic.

### Como U19 vs RB Leipzig U19 versus Manchester United U19 vs Sabah U19

The user observed that Manchester United–Sabah carried the stronger goal-market signal than Como–Leipzig, while the trial's structural research promoted Como too aggressively.

Correct finals:

- Como–RB Leipzig 1–1 = 2 goals
- Manchester United–Sabah 5–0 = 5 goals

This comparison **did** support the market-ordering hypothesis. Exact comparative line/price for Manchester United should be reverified from the original screenshot before quantitative modelling.

**Current conclusion:** use market-implied goal environment as a meaningful UYL ranking input, but require repeated evidence across slates before increasing its weight further.

---

## 5. Model-issued UYL trial verdict log

These are **trial verdicts**, not official Football v0.2.50 Website Picks. Do not mix them into official P/L unless the repository later creates an explicit trial accounting contract.

| Match | Trial line | Final | Trial settlement |
|---|---:|---:|---:|
| Sporting CP U19 vs Galatasaray U19 | O3.5 @1.77 | 2–2 | WIN |
| Liverpool U19 vs Atletico Madrid U19 | O3.25 @1.88 | 2–2 | WIN |
| Barcelona U19 vs Feyenoord U19 | O3.25 @1.95 around 70' | 1–2 | HALF LOSS |
| Fenerbahce U19 vs Roma U19 | O3.5 @1.74 | 2–4 | WIN |
| Slavia Prague U19 vs Lens U19 | O3.75 @1.88 | 2–1 | LOSS |
| Como U19 vs RB Leipzig U19 | O3.5 @1.88 | 1–1 | LOSS |

Flat 1u trial P/L for these six executed verdicts: **-0.11u**.

### Missed / no-entry case

PSG U19 vs Slovan Bratislava U19 finished 6–1. The trial did not count an executed entry because PSG scored while the verdict was being formed and the market reset. Preserve as a validated missed opportunity / NO BET, not P/L.

### Result-integrity note

Earlier third-party result fetching produced multiple incorrect scores. For this opening-round record, the user's Soccerway results screenshot supersedes those fetched values.

Feyenoord received a red card in Barcelona–Feyenoord; red-card timing was not preserved and must not be invented.

---

## 6. Match-specific audit notes

### Slavia Prague U19 vs Lens U19

Final 2–1. User reported many big chances missed.

Audit tag:

`STRUCTURE BROADLY VALIDATED / CONVERSION UNDERPERFORMED`

The loss does not automatically mean the matchup thesis was structurally poor. However, line selection was aggressive: O3.75 required four goals for meaningful success, while a protected O3.25 would have reduced damage at exactly three goals.

### Barcelona U19 vs Feyenoord U19

Final reconciled as 1–2.

Live process error occurred: the score column was misread more than once. Future live UYL assessments must explicitly confirm score, minute, cards, and current total before interpreting line movement.

The late O3.25 @1.95 entry illustrated another key point: a line can look low in absolute UYL terms while still requiring two additional goals for a full win. Competition-relative decay alone is not enough; always calculate exact remaining-goal burden.

### Fenerbahce U19 vs Roma U19

Correct final 2–4. The O3.5 @1.74 trial lock was a full win. Previous 0–2 result was erroneous and must not be reused.

### Como U19 vs RB Leipzig U19

Correct final 1–1. The O3.5 @1.88 trial lock lost. Previous 0–2 result was erroneous; settlement remains a full loss either way, but the scoreline matters for future structural audit.

---

## 7. Early high-scoring / high-event team watch flags

These are **one-round watch flags only**, not permanent team classifications. Revalidate current season form, XI and market next time.

### Strong individual scoring output in opening round

- Bayern U19 — scored 6
- PSG U19 — scored 6
- Club Brugge U19 — scored 5
- Stuttgart U19 — scored 5
- Manchester United U19 — scored 5
- AS Roma U19 — scored 4
- Porto U19 — scored 3
- Real Madrid U19 — scored 3
- Villarreal U19 — scored 3

### High-event opening-round participants worth early attention

- Club Brugge U19 / Aston Villa U19 — 8 total
- Bayern U19 / Bodo/Glimt U19 — 7 total
- PSG U19 / Slovan Bratislava U19 — 7 total
- Fenerbahce U19 / Roma U19 — 6 total
- Dortmund U19 / Villarreal U19 — 5 total
- Stuttgart U19 / Viking U19 — 5 total
- Manchester United U19 / Sabah U19 — 5 total
- Porto U19 / Manchester City U19 — 4 total
- Liverpool U19 / Atletico Madrid U19 — 4 total
- Sporting CP U19 / Galatasaray U19 — 4 total

PSV U19 should **not** be flagged as high-event from this round; PSV–Shakhtar finished 1–0.

---

## 8. Future UYL workflow

When a new UYL slate appears:

1. keep it outside the official senior board unless explicitly running the manual trial;
2. identify confirmed XI and basic structural viability;
3. compare the market-implied goal environment across the slate, especially equivalent total lines;
4. use team form/profile to refine rather than dominate cross-match ranking;
5. calculate exact burden at the proposed Asian total;
6. prefer protection when the match is strong but not truly extreme;
7. never chase a line expanded by an early goal;
8. record trial decision, price, final, chance-quality notes if supplied, and any market-ordering lesson back into this file;
9. prefer user-supplied/competition-source reconciliation for result settlement when third-party feeds conflict.

The goal of the trial is not to prove that UYL is always high scoring. It is to learn which UYL matches and market states reliably separate ordinary 2–3 goal games from genuine 4+ environments.
