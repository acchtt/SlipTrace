# Football C — 26 October post-repair /xi upstream selection audit

**Decision: FAIL selection and research coverage; no predictive code promoted. Dual-rank and custom-line audit corrected 2026-10-27 ICT.**

**Scope:** October 26 17:12 through October 27 03:00 ICT, eleven identifiable /xi/exception/review matches. Club América, earlier XI assessments, later morning fixtures, and twelve merely ranked/no-/xi fixtures are excluded. End-date crosses midnight. This report distinguishes source-backed C certificates, screenshot decisions, and actual real-money fills. Final scores are outcome overlay, **never prospective input**.

## CORRECTION — analyze TWO distinct /rank processes, not only the last snapshot

User identified two separate ranking processes and confirmed that the bookmaker offers **custom Over totals**. Earlier audit language wrongly counted only final FOLLOW membership as the selection benchmark and treated rejected screenshots as if the user was unable to select another line. This section supersedes those conclusions. The official quotes were not scraped or replaced.

| Metric | First rank, 17:47:18 ICT | Second rank, 22:09:22 ICT |
|---|---:|---:|
| Frozen C-assessed in 22-fixture universe | 9 | 17 |
| Admitted C-FOCUS | 6 | 10 |
| FOLLOW | 6 | 7 |
| Exact FOLLOW certificate clears | **3/6 (50%)** | **1/7 (14.3%)** |
| All admitted FOCUS exact certificate clears | 3/6 | 3/10 |
| Successful FOLLOWs | **Geylang, Rizespor, Galatasaray** | **Galatasaray only** |

At second freeze, successful Rizespor changed **FOLLOW → RESERVE**. Geylang was dropped because kickoff had passed; its **earlier successful FOLLOW stays credited**. New FOLLOW memberships Al Ahli (O3.5, FT 2-1), Kauno (O2.5, FT 0-0), and Al Qadsiah–Al Sadd (O2.5, FT 1-1) all missed. Other first-rank missed certs were Copenhagen (1-1), Örebro (1-0) and PSG–Lyon (2-0, O3.5). The second board also included Biggleswade–Royston **RESERVE O2.5 CLEAR**, Beşiktaş–Başakşehir **RESERVE O2.5 MISS**, and Rizespor **RESERVE CLEAR**.

These are **rank-state process metrics** from all six/ten admitted board rows; don't misrepresent them as /xi-bet results or add the two denominators as independent 16 fixtures. Deduplicated board union is 11 unique fixtures, 4 exact certificate clears (Geylang, Rizespor, Galatasaray, Biggleswade). That union includes rank-only fixtures. Separately, the /xi-linked eight G3-funded fixtures clear 3/8 exact certified burdens across **either** ranking epoch.

**Causal selection inversion in the second rank:** among 7 FOLLOW, 1 cleared exact burden; among 3 RESERVE, 2 cleared. This demonstrates failed *retrospective priority separation on this slate*; investigate the prospective kickoff-protected allocation, not a hindsight-based change to model grades.

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
| Neftchi–Al Ittihad | 1–2 | PASS for visible O3 @2.03, O2.75 @1.77, O2.5 @1.61 | GOAL_PRIORITY, never prematch C-ranked | **Missed potential entry**: O2.5 at 1.61 fully wins; O2.75 at 1.77 half-wins on total 3; O3 pushes. User could select custom line; no actual fill verified. |
| Mohun Bagan–Chennaiyin | 1–0 | PASS Over 2.5 @1.76 | EVIDENCE_LIMITED sweep, no official C rank | Correct avoidance in outcome; independent proof incomplete |
| Rizespor–Trabzonspor | 3–4 | PASS at visible O3 @1.81, O3.25 @2.06, O3.5 @2.28; custom O2.5 also selectable | FIRST FOLLOW, LATER RESERVE, cert O2.5 **CLEAR** | **Missed potential entry and priority demotion**: all three visible O3+ lines fully win at total 7; screenshot capture/actionable window still needs timestamp verification; no fill verified. |
| Al Ahli–Al Gharafa | 2–1 | Conditional BOOK target O3.25 @1.65+ | FOLLOW cert O3.5 **MISS** | O3.25 would be **half-loss**, if filled; G3 reached |
| Kauno Žalgiris–Žalgiris | 0–0 | O2.5 ACT-eligible candidate (final ACT not verified) | FOLLOW cert O2.5 **MISS** | Hypothetical O2.5 full loss; no actual bet inferred |
| Copenhagen–OB | 1–1 | PASS O2.5 @1.50 below minimum | FOLLOW cert O2.5 **MISS** | XI price rejection avoided losing exposure |
| Örebro–Falkenberg | 1–0 | PASS O2.5 @1.82, not execution-authorized | FOLLOW cert O2.5 **MISS** | XI price rejection avoided losing exposure |
| Al Qadsiah–Al Sadd | 1–1 | PASS, ladder below required authority | FOLLOW cert O2.5 **MISS** | XI rejection avoided losing exposure |
| Galatasaray–Fenerbahçe | 2–1 | PASS visible O3.0 @1.74; custom O2.5 or O2.75 selectable according to user bookmaker capability | FIRST & SECOND FOLLOW cert O2.5 **CLEAR** | **Missed potential custom-line entry**: O2.5 would win, O2.75 would half-win; O3.0 would PUSH. Lower-line actual odds and entry availability **not recorded**. |

### Results and denominators — snapshots, not duplicate bets

- **11 /xi-identified fixtures**, 6 reached 3+ final goals, 5 did not. Eight have a frozen G3-funded C-FOCUS at **either** rank: **3/8 exact certificate clears**, versus 5 misses. That is not actual booked P&L.
- **FIRST rank 17:47 ICT**: 6 FOCUS/FOLLOW, 3/6 exact certificate clears. Five of these have /xi evaluations (Geylang, Rizespor, Copenhagen, Örebro, Galatasaray), **3/5** exact clears.
- **SECOND rank 22:09 ICT**: 10 FOCUS, 7 FOLLOW, **1/7 FOLLOW** exact clear. All ten FOCUS **3/10** exact clears. Seven of ten have /xi evaluations (Al Ahli, Rizespor, Kauno, Copenhagen, Örebro, Al Qadsiah, Galatasaray), **2/7** exact clears; later Rizespor is RESERVE, not FOLLOW.
- **11 unique FOCUS fixtures** across the two ranks, with **4/11 exact clears**, including rank-only Biggleswade; do not sum rank-version cohorts as separate opportunities. The first-rank Geylang/Rizespor successful FOLLOW decisions must not be erased by last-rank status.
- **Potential entry outcomes (not confirmed fills)**: Geylang O2.5 conditional target full win; Rizespor visible O3.0 @1.81 / O3.25 @2.06 / O3.5 @2.28 would all fully win; Neftchi visible O2.5 @1.61 full win and O2.75 @1.77 half-win; Galatasaray custom O2.5 would fully win or O2.75 half-win with **unknown lower-line prices**. Galatasaray's visible O3.0 @1.74 alone only pushes. Xorazm's available specific betting line remains unverified.
- Model-positive target outcomes: Al Ahli conditional O3.25 **half-loss** at FT total 3, Kauno ACT-eligible O2.5 **full hypothetical loss** at 0, Geylang BOOK O2.5 **full hypothetical win** at 3. Price, screenshot epoch and bookmaker custom selection can modify executable opportunity; the model's PASS verdict is **not** evidence that booking was impossible.
- All prices are from prior user screenshots, never internet replacement odds. **No user-confirmed stake/fill**, so no realized P&L claimed.


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

### 5. /xi is not the same as upstream selection — actionable lower-line omission

- **Neftchi** was not frozen in either C ranking before kickoff, but the screenshot already offered **O2.75 @1.77** (half-win on FT 1-2) and **O2.5 @1.61** (full win). The old audit dismissed O2.5 as below a common price floor while ignoring a visible higher-priced quarter line. This was a real *candidate price option*, not a verified executed bet.
- **Rizespor** was FIRST FOLLOW O2.5, then demoted to later RESERVE despite its retained G3. /xi PASS on screenshot O3 @1.81, O3.25 @2.06 and O3.5 @2.28; all would have fully won on the final seven goals. User also reports custom O2.5 available. Quote timestamp / match progress must still be respected; do not invent prematch availability or assert that every line remained open after goals.
- **Galatasaray** was FOLLOW twice and cleared protected O2.5. /xi considered O3.0 @1.74 (would push); the user's bookmaker supports choosing **custom O2.5/O2.75** that would win/half-win if quoted, although those exact prices are not in the record. Calling this PASS a correctly avoided nonwinner was wrong.
- This is **selection/entry opportunity loss**, not evidence that three realized winning bets were placed. Galatasaray screenshot O3 is a push; lower lines are unpriced. Rizespor custom O2.5 is not the sole alternative because screenshot O3+ were already winners. Neftchi O2.75 is an observable half-win without replacement prices.
- **Copenhagen, Örebro and Al Qadsiah** were FOLLOW G3 misses correctly passed by /xi on the user quotes. Keep the distinction that /xi avoided executing bad ranked picks. Geylang won only on 90+2 goal; keep time-to-goal fragility.
- **Xorazm** earlier user 2–2 vs published 1–2 remains a source discrepancy; both have 3+ total goals. Do not infer undocumented entry prices from this.

### 6. Current FOLLOW allocator is kickoff-protected, not pure cross-slate merit

The production `adapter.py::_allocate_c_follow_lanes` first nominates one CLEARABILITY candidate **per kickoff block**; these primary nominations are allocated in **kickoff order** up to MAX_FOLLOW, with remaining capacity going to secondary nominees. This scheme is intended to protect timing and avoid earlier global ranking regressions, but is not equivalent to always selecting the strongest G3 forecasts across the whole slate. The two frozen ranks expose the allocation effect: Rizespor was demoted after more late fixtures were researched, while new FOLLOW burden failures were admitted. This is a **prospective prioritization test target**, not proof to reintroduce the previously failed global allocator.


## Controlled repair programme — NOT promoted

1. Replay and publish BOTH rank versions per slate, including FOLLOW→RESERVE and STATUS_EXCLUDED transitions; instrument every sweep-eligible fixture's *prematch* decision deadline and first-C-assessment timestamp. Include closed-before-research missed count in rank publication; keep status fail-closed and one shared full slate universe.
2. Prospectively turn on the opt-in independent fact-level goal-route research contract in a parallel trial, for FOCUS *and* PASS / EVIDENCE_LIMITED controls. Explicit scoring carrier, opponent reply, two-goal endpoint, context/tournament incentives, and fourth-goal bridge, frozen before kickoff.
3. Run champion versus challenger on **identical frozen prematch evidence**, keeping genuine winning-match recall across all eligible candidates, certificate settlement, false G3/G4, first goal and quote availability. Exclude post-kickoff retrospective exception from claims of prematch execution feasibility.
4. Alter live predictive gates or ranking priorities **only after** multi-day holdout demonstrates improvement in both reach and burden precision. PR #199's failed challenger must remain unmerged.
5. Keep /xi screenshot-only prices and **custom bookmaker lines**, execution-only; evaluate the *best reachable user-supported burden/odds pair* and settlement-specific O2.5/O2.75/O3.0/O3.25 options before PASS. No replacement web odds; do not demand a screenshot line exactly match a custom line. BOOK is not filled exposure.

**Release gate:** source-completeness instrumentation and a prospectively replayed independent-route challenger required. Current champion **FAIL on this audited XI cohort**; **no predictive code changes from this report**.
