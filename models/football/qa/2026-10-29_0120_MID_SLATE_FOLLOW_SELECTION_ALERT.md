# 29 October 2026 ICT — 01:20 mid-slate Football C portfolio selection alert

**Status: PRELIMINARY/MID-SLATE DIAGNOSTIC ONLY**. This is a separate checkpoint from the October 28 FT retrospective. Do not turn any live/halfway state into final model outcome; no change to production thresholds, FOLLOW allocation, odds authority, bets or frozen receipts.

## Evidence
- Frozen source: `Football-C-rank-20261028-through-0300-verified-published.json`, 16 FOCUS rows, 7 FOLLOW, 4 RESERVE, 5 FOCUS_UNFOLLOWED. Main `946480a9...` at freeze; as of this check main `7e4207b...` includes 53 later XI request/result files and no modifications to core/adapter/sweep/rank selection code relative to the handoff HEAD.
- At **01:20 ICT**, **all 7 FOLLOW** had kickoff <=01:00 and the remaining 9 FOCUS (including higher-ranked alternatives) were RESERVE or FOCUS_UNFOLLOWED. Three completed early FOLLOW outcomes are assessable:
  - ND Beltinci–NK Triglav (1801066), FOLLOW C rank 5 O2.5, independently reported FT **3–4**, G3 **CLEAR**.
  - Nasaf Qarshi–Kuwait SC (1873835), FOLLOW C rank 12 O2.5, user-reported one-goal total, G3 **MISS**. Winner orientation was not initially established; do not assume from shorthand.
  - FC Goa–Hyderabad FC (1900650), FOLLOW C rank 11 O2.5, user-reported FT **0–1**, G3 **MISS**. Third-party source reports an ostensibly associated Goa–SC Delhi 1–1: the provider identity/conflicting opponent/scores require reconciliation; **both one- and two-goal outcomes miss O2.5**.
- This is **1 CLEAR / 3 early certified FOLLOW decisions**; not full-board precision, not final results for the other four already-started FOLLOWs, not actual betting performance. User stake/fills remain unverified and Google Sheets confirmed bets table lists no placements for these match IDs.

## Frozen allocation trace: exact C rank vs FOLLOW selection

The seven FOLLOWs by kickoff:
- **20:00** ND Beltinci–NK Triglav, C rank 5, O2.5 carrier G3 (CLEAR)
- **20:45** Nasaf–Kuwait, C rank 12, O2.5 distributed-only (MISS)
- **21:00** FC Goa–Hyderabad, C rank 11, O2.5 TWO_ROUTE/distributed (MISS)
- **00:00** FC Kosice–DAC, C rank 2, O3.5, outcome **UNRESOLVED at alert**
- **00:30** Venezia–Inter, C rank 1, O2.5, outcome **UNRESOLVED at alert**
- **00:45** Chelsea W–Roma W, C rank 3, O2.5, outcome **UNRESOLVED at alert**
- **01:00** Brommapojkarna–BK Häcken, C rank 6, O2.5, outcome **UNRESOLVED at alert**

Six-plus hours of matches after early FOLLOW allocation are not *automatically* bets. Higher-ranked FOCUS candidates excluded from FOLLOW:
- Spelle-Venhaus–TuS Bersenbrueck, C rank 4, 01:30, RESERVE O2.5
- Celtic–Dundee United, rank 7, 02:45, RESERVE O2.5
- College 1975–Glacis United, rank 8, 03:00, FOCUS_UNFOLLOWED O2.5
- Lyon W–Inter W, rank 9, 03:00, FOCUS_UNFOLLOWED O2.5
- Monza–Napoli, rank 10, 02:45, RESERVE O3.5

This is a verified **workload/chronological FOLLOW allocation vs football-rank conflict**, not proof the substitutes would win. A pure global-rank allocator risks missing earlier /xi deadlines; preserve the existing policy until prospective controls demonstrate net improvement.

## Source-screened AFC evidence (post-FT only, not for retuning)
- Viettel–FC Seoul (1873843), historical WATCH_GOAL_SIGNAL priority 39, no Football C rank, FT **0–5** confirmed by the Asian Football Confederation on Oct 28; would clear O2.5 if quoted, **not a verified fill**. AFC report: https://www.the-afc.com/en/club/afc_champions_league_two.html/news/group-e-the-cong-viettel-fc-vie-x-x-fc-seoul-kor-1
- Persib Bandung–Melbourne Victory (1885202), historical WATCH_GOAL_SIGNAL priority 42, no C rank, FT **2–0**, would miss O2.5. AFC report: https://www.the-afc.com/en/club/afc_champions_league_two.html/news/group-e-persib-bandung-idn-2-0-melbourne-victory-aus
- This is one missed possible high-total outcome versus one correctly excluded below-three-goal outcome. Both must be counted in negative-screen recall, not cherry-picked. It cannot establish net calibration.

## Engine consistency and execution accounting
All 16 FOCUS were assigned MEDIUM failure resistance/protection/stall and opponent leakage, and in all 33 assessed `material_suppression=false` / `failure_attacks_route=false`; these low-variance risk classifications cannot discriminate the narrative sources' third-goal bridge weaknesses. In `core.py::c_distributed_goal3_funded` multi-MEDIUM dimensions can fund G3, and `c_g3_endpoint_control_pressure` compresses them into a single MODERATE. Research collection must prospectively resolve opponent reply, same-competition transfer, 1–1/2–0 stop mechanisms and one-team carrier continuation.
Active Google Sheets `Decision States` has recent XI entries for Kosice, Venezia, Chelsea W and Brommapojkarna (quote actions labeled `OBSERVED_*_NON_EXECUTABLE` or unpriced), while `Actual Bets — Current` shows no corresponding confirmed slips. Do not convert `FOLLOW`, `BOOK` target, or `OBSERVED` into placed bets or ROI. User screenshots remain only odds authority.

## Next operational actions
1. Freeze independent result and kickoff evidence for **all** assessed and screened fixtures when they complete; publish exact Asian settlement by the protected line, never use in-progress scores as FT. Include earliest FOLLOW, RESERVE, FOCUS_UNFOLLOWED, WATCH, DEFERRED, negative controls.
2. Separate **first C assessment before kickoff**, source admission, decision-state XI and independent quote feasibility. In particular, no old 00:00–03:00 started fixture may receive a backdated prematch C rank.
3. A prospective challenger must avoid conflating `FOLLOW` workload allocation with highest predicted goal reliability. Test predeclared alternatives on **identical frozen evidence** across multiple untouched future slates; measure both third-goal false positives and rejected-team-carrier recall, as well as live execution deadline losses.
4. For unstarted fixtures, require the normal independent XI and user-screenshot evidence; do not make automatic or revenge allocations in response to early misses.

**No predictive code merged or promoted**. Keep this mid-slate label open until final results and fixture identities are independently reconciled.
