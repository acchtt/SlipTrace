# Football C — 26 October post-repair /xi upstream selection audit

**Decision: FAIL selection and research coverage; no predictive code promoted.**

**Scope:** October 26 17:12 through October 27 03:00 ICT, eleven identifiable /xi/exception/review matches. Club América, earlier XI assessments, later morning fixtures, and twelve merely ranked/no-/xi fixtures are excluded. End-date crosses midnight. This report distinguishes source-backed C certificates, screenshot decisions, and actual real-money fills. Final scores are outcome overlay, **never prospective input**.

## Grounded source epochs and audit integrity

- Sealed published slate receipt: Football-C-rerank-20261026-through-0300-published-verified.json, including immutable previous_rank_receipt, rank_receipt, source_bundle.sweep_receipt and 22-item coverage manifest.
- First rank (2026-10-26 **17:47:18 ICT**): **9 of 22 assessed**, 13 still evidence-limited. Later rank (**22:09:22 ICT**): **17 assessed**, **5 PREMATCH_WINDOW_CLOSED**, 0 pending, and research_complete=true.
- Cross-receipt union: **19 unique fixtures received prematch C assessments**; 3 **never reached C** before kickoff: Xorazm–Navbahor, Neftchi Fargona–Al Ittihad, Ararat Armenia–Noah. Xorazm (20:30) and Neftchi (20:45) therefore missed the official research deadline; after-start /xi exception cannot repair this.
- These are two different frozen time epochs. Do **not** treat the 22:09 board as what was known before the earlier 18:30 kickoff. Geylang was FIRST FOLLOW and later STATUS_EXCLUDED because it had started; Rizespor changed FIRST FOLLOW → LATER RESERVE.
- The later receipt explicitly has goal_route_proof_policy = **LEGACY_FROZEN_COMPATIBILITY**. PR #200 was merged as opt-in; **its stronger research evidence contract was not enabled** in this session. No new model performance benefit can be attributed to the merge.
- Available Google Sheets Decision States contains only three entries from October 26 UTC: America (explicitly excluded), Neftchi PASS and Mohun PASS. Most other /xi decisions are from conversation-recovered screenshots/verdicts, not complete immutable XI receipts. This limitation is material.

## Eleven /xi evaluations — user session, not entire /rank board

| Match | FT | /xi result from conversation | /rank certificate and outcome | Correct accounting |
|---|---|---|---|---|
| Geylang–Hougang | 3–0 | BOOK target Over 2.5 @1.65+ | First FOLLOW O2.5 **CLEAR** | Target hypothetical win, third goal 90+2; fill unverified |
| Xorazm–Navbahor | 1–2 published; user earlier reported 2–2 | Rejected evidence-limited review | GOAL_REVIEW, never prematch C-ranked | Missed research; outcome 3+ either way; no bookmaker fill |
| Neftchi–Al Ittihad | 1–2 | PASS Over 2.5 @1.61 | GOAL_PRIORITY, never prematch C-ranked | Missed research; quote below typical 1.65 goal; no validated feasible bet |
| Mohun Bagan–Chennaiyin | 1–0 | PASS Over 2.5 @1.76 | EVIDENCE_LIMITED sweep, no official C rank | Correct avoidance in outcome; independent proof incomplete |
| Rizespor–Trabzonspor | 3–4 | PASS O3/O3.25/O3.5 at exception | FIRST FOLLOW, LATER RESERVE, cert O2.5 **CLEAR** | Selection found G3; execution rejected higher burdens; exception timing limits prematch opportunity claims |
| Al Ahli–Al Gharafa | 2–1 | Conditional BOOK target O3.25 @1.65+ | FOLLOW cert O3.5 **MISS** | O3.25 would be **half-loss**, if filled; G3 reached |
| Kauno Žalgiris–Žalgiris | 0–0 | O2.5 ACT-eligible candidate (final ACT not verified) | FOLLOW cert O2.5 **MISS** | Hypothetical O2.5 full loss; no actual bet inferred |
| Copenhagen–OB | 1–1 | PASS O2.5 @1.50 below minimum | FOLLOW cert O2.5 **MISS** | XI price rejection avoided losing exposure |
| Örebro–Falkenberg | 1–0 | PASS O2.5 @1.82, not execution-authorized | FOLLOW cert O2.5 **MISS** | XI price rejection avoided losing exposure |
| Al Qadsiah–Al Sadd | 1–1 | PASS, ladder below required authority | FOLLOW cert O2.5 **MISS** | XI rejection avoided losing exposure |
| Galatasaray–Fenerbahçe | 2–1 | PASS O3.0 @1.74, below @1.90 condition | FOLLOW cert O2.5 **CLEAR** | Quoted O3.0 would **PUSH**, not win |

### Results and denominators

- **11 /xi-identified fixtures:** 6 finished with at least three goals and five with fewer.
- **8 had frozen G3-funded C-FOCUS in the earliest or later ranked epoch** (Geylang, Rizespor, Al Ahli, Kauno, Copenhagen, Örebro, Al Qadsiah, Galatasaray). **4/8 reached three goals**, but **only 3/8 cleared the exact protected certificate** (Geylang, Rizespor, Galatasaray); Al Ahli had O3.5 and finished on three.
- **Seven of those eight were FOLLOW at their last available prematch rank state**; Rizespor became RESERVE. Of the seven FOLLOWs, exact certificate clears were **2/7** (Geylang and Galatasaray), with **5/7 misses**. These are **not actual betting losses or booked win-rate**.
- **/xi execution:** one potential target full win (Geylang), one conditional target half-loss (Al Ahli), one ACT-eligible candidate hypothetical full loss (Kauno, ACT/fill unverified). Remaining eight PASS/evidence-limited reviews; of these four finished 3+, **but not four proven profitable/authorized bets**: Galatasaray O3 pushes; Neftchi's visible 1.61 may be below min, Xorazm price not verified, and Rizespor exception was a started-match/line-mismatch assessment.
- **Actual betting P&L = unknown** in this cohort; do not convert model BOOK/ACT or hypothetical settlement into fills.

## Root-cause findings — frozen evidence and current source logic

### 1. Research deadline defect: hard evidence
The research-complete bit flips to true when the remaining five candidates have CLOSED, including three **never C-assessed**. This is correct fixture-status closure but a misleading **selection-coverage quality metric**. Xorazm GOAL_REVIEW and Neftchi GOAL_PRIORITY reached kickoff before a current C model rank, even though they were in the frozen eligible 22. The window was not fully researched in a usable prematch sense.

**Required test:** for all eligible match IDs retain first eligibility, first frozen C assessment and kickoff timestamps; explicitly measure **never-assessed-before-kickoff** separately from terminal closure. Priority must respect near-kickoff deadlines without discarding registered competitions or secretly splitting the board.

### 2. Carrier-G3 FOCUS is under-discriminating: hard structural finding
The production C carrier G3 compiler in models/football/engine/core.py accepts STRONG self-funded carrier plus only MEDIUM minimum route reliability, failure resistance, confidence and burden protection. The board compiler then maps *every* funded G3 directly to FOCUS. The October 26 losers Kauno (0–0), Copenhagen (1–1) and Örebro (1–0) all received STRONG carrier / MEDIUM reliability / MEDIUM failure / MEDIUM completion profiles and protected O2.5 despite documented opponent control, fatigue or absent-scorer counterevidence.

The endpoint-control function compresses simultaneous MEDIUM completion/continuation/stall/failure risks into a single MODERATE flag via OR; HIGH is reserved for explicit verified hard controls. This preserves recall but can give a weak multi-risk G3 the same executable floor as a sturdier one. **Do not apply a blanket all-MEDIUM PASS**: earlier frozen replays showed it deleted many winning 3+ fixtures.

**Required test:** prospective independent carrier/finisher and opponent leakage proof plus 0–0/1–1/2–0 failure scenarios; test whether control pressure ought to be mechanism-specific. Use separate facts, not a recycling of last-seven scoreline citations.

### 3. Comparable competition suppression insufficient: concrete Al Sadd case
Al Qadsiah–Al Sadd entered GOAL_PRIORITY on combined historical goal rates (mean 3+ 0.7944, mean 4+ 0.6389, low draw trap 0.05) and got distributed G3 even though the frozen main failure explicitly cited Al Sadd's **two blank continental outings** and Al Qadsiah's closest continental 2–1 and 1–1 comparators. Tournament stage/incentive *was* verified; it was the **scoring-route transfer** into a continental clash that remained uncertain. FT 1–1 confirmed risk but must not retroactively change original evidence grades.

**Required test:** for independently funded distributed 2+1, source a competition-comparable reply route and conversion/continuation evidence, not only an aggregate historical goal-rate.

### 4. Goal-four overreach: concrete Al Ahli case
Al Ahli had G4 O3.5 funded on MEDIUM upper-tail transferability with documented contrary continental 1–1 and opponent 0–0. It finished 2–1, clearing G3 but **missing G4**; proposed O3.25 would half-lose at three. Neither the fourth-goal certificate nor the price target should be lowered after FT without a prospective fourth-goal bridge.

**Required test:** isolated G4-after-G3 source proof; explicitly grade fourth-goal continuation/score-control and settlement-aware target against actual user screenshot, without importing replacement bookmaker odds.

### 5. /xi is not the same as upstream selection: avoid false inversion
- Geylang G3 only cleared with a stoppage-time third goal: credit as certified clear, flag **completion latency**, but do not invent a guaranteed 1.65 early fill.
- Rizespor G3 was already funded upstream and even initially FOLLOW; PASS concerned visible **higher** O3+ lines in an exception with match-state information. It is a tail/entry disagreement, not a missed /sweep G3.
- Galatasaray's ranked O2.5 clear is **not** proof the offered O3.0 @1.74 would win: it pushes.
- Copenhagen, Örebro and Al Qadsiah had poor ranking certificates but XI **PASS avoided** losses. Neftchi's O2.5 @1.61 was PASS with no G3 certificate; line arithmetic alone does not prove admissible bookmaker value.
- Xorazm's published 1–2 conflicts with an earlier user 2–2; both cross three total goals. Preserve both readings for source reconciliation, without conflating the match with another fixture.

## Controlled repair programme — NOT promoted

1. Instrument every sweep-eligible fixture's *prematch* decision deadline and first-C-assessment timestamp. Include closed-before-research missed count in rank publication; keep status fail-closed and one shared full slate universe.
2. Prospectively turn on the opt-in independent fact-level goal-route research contract in a parallel trial, for FOCUS *and* PASS / EVIDENCE_LIMITED controls. Explicit scoring carrier, opponent reply, two-goal endpoint, context/tournament incentives, and fourth-goal bridge, frozen before kickoff.
3. Run champion versus challenger on **identical frozen prematch evidence**, keeping genuine winning-match recall across all eligible candidates, certificate settlement, false G3/G4, first goal and quote availability. Exclude post-kickoff retrospective exception from claims of prematch execution feasibility.
4. Alter live predictive gates or ranking priorities **only after** multi-day holdout demonstrates improvement in both reach and burden precision. PR #199's failed challenger must remain unmerged.
5. Keep /xi screenshot-only prices and custom lines, execution-only; BOOK is not filled exposure.

**Release gate:** source-completeness instrumentation and a prospectively replayed independent-route challenger required. Current champion **FAIL on this audited XI cohort**; **no predictive code changes from this report**.
