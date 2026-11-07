# 2026-10-29 — Football C /sweep + /rank full-selection audit (Oct 28–29 slate)

**Disposition: VERIFIED STRUCTURAL FAULTS + OBSERVED ONE-SLATE INVERSION.** Audit only. Main, active Google Sheets, user bets, active receipts and execution policies untouched. Football C only. Dates ICT unless stated. No post-result feature edits.

## 1. Evidence authority and denominator

- Sealed immutable source and ranks: `Football-C-rank-20261028-through-0300-verified-published.json`, source epoch `V4-20261028-1610-20261029-0300-LEAGUEPROOF`, source observed Oct 28 16:20 ICT, rank stamped Oct 28 16:43:08 ICT. Freeze original model inputs, grade, certificate, kickoff and lane **before** outcome overlay.
- 553 source-fixture rows; 34 admitted source-eligible, 33 completed Football C research assessments; 16 funded FOCUS certificates, 17 WATCH/STOP. 7 FOLLOW, 4 RESERVE, 5 FOCUS_UNFOLLOWED. One of 34 no C assessment because status exclusion. Reported `research_complete=true` pertains to the **34 admitted**, **not** all 553 source rows.
- Full-source intake: CLOSED 296, DEFERRED_RESEARCH_BACKLOG 131, EXCLUDED 34, WATCH_GOAL_SIGNAL 30, EVIDENCE_LIMITED 24, GOAL_PRIORITY 24, GOAL_REVIEW 10, CONTROL_REVIEW 4. The four negative-control fixtures were not admitted to normal C ranking.
- Fixed outcome overlay was obtained **after** candidate membership and ranking were frozen. Explicit distinct 90-minute FT evidence for 27/33 C-assessed, with six unresolved below. This is not an independent predictive holdout.

## 2. Certified burden reconciliation (only backed lines)

| Lane | N | FT verified | Cleared own C supported line | Missed | FT unknown/conflict |
|---|---:|---:|---:|---:|---:|
| FOLLOW | 7 | 7 | **1** | **6** | 0 |
| RESERVE | 4 | 3 | **3** | 0 | 1 |
| FOCUS_UNFOLLOWED | 5 | 3 | **2** | 1 | 2 |
| All FOCUS | 16 | 13 | **6** | **7** | 3 |
| WATCH/STOP, hypothetical O2.5 diagnostic only | 17 | 14 | **10** with FT >=3 | 4 with FT <=2 | 3 |

For WATCH rows, 3+ goals is **not** an official G3 prediction or wager. For FOCUS O3.5 is tested at *four* goals. Actual placed bets and sportsbook quotes are separate.

- **FOLLOW misses (6):** Venezia–Inter 0–2 on O2.5; Košice–DAC 0–1 on O3.5; Chelsea W–Roma W 2–0 on O2.5; Brommapojkarna–Häcken 0–0 on O2.5; FC Goa–**Sporting Club Delhi** 1–1 on O2.5 (receipt's old `Hyderabad FC` display alias); Nasaf–Kuwait SC 0–1 on O2.5.
- **FOLLOW clear (1):** Beltinci–Triglav 3–4 on O2.5.
- **RESERVE clears (3):** Celtic–Dundee United 2–2 O2.5, Monza–Napoli 1–4 O3.5, Bayern W–Real Madrid W 2–2 O2.5.
- **UNFOLLOWED clears (2):** Lyon W–Inter W 6–0 O2.5, Al Khalidiyah–Al Wahda 1–2 O2.5. **UNFOLLOWED miss (1):** Forest Green–Eastleigh 2–0 O2.5.
- **Unresolved (6):** Spelle–Bersenbrück, College 1975–Glacis, London Lions–Ware, Aylesbury–Hertford, Shifnal–Atherton, Vargas Torres–22 de Julio. Spelle sources directly disagree on final (2–0 at 90+3 versus 4–0 marked FT) and is **excluded** from deterministic scoring until reconciled. Source snapshots for the others were incomplete.

### External score references (retrospective only)
- Serie A Venezia 0–2, Monza 1–4: https://www.soccerway.com/match/inter-Iw7eKK25/venezia-MkPmVv50/?mid=QRMD8Ai3 ; https://sscnapoli.it/match-report-monza-napoli-1-4/
- UEFA women 2–0 Chelsea/Roma, 2–2 Bayern/Real, 6–0 Lyon/Inter, 5–1 Servette/Leuven: https://www.uefa.com/womenschampionsleague/news/02a9-2184a4a3a3d8-3d2bf80e5c0e-1000--women-s-champions-league-2026-27-league-phase-fixtures-and-/
- Celtic 2–2: https://www.celticfc.com/news/2026/october/28/celts-held-to-draw-against-dundee-united-at-paradise/
- Nasaf 0–1: https://www.the-afc.com/en/club/afc_champions_league_two.html/news/group-a-pfc-nasaf-uzb-0-1-kuwait-sc-kuw
- Al Khalidiyah 1–2: https://www.the-afc.com/en/club/afc_champions_league_two.html/news/group-a-al-khaldiya-sc-bhr-1-2-al-wahda-fc-uae
- Goa–Sporting Club Delhi 1–1: https://www.indiansuperleague.com/news/fc-goa-snatch-stoppage-time-draw-against-sporting-club-delhi
- Kashima–Pohang 3–0: https://www.the-afc.com/en/club/afc_champions_league_elite.html/news/md3-kashima-antlers-jpn-3-0-fc-pohang-steelers-kor
- Spelle conflict: https://www.soccerpunter.com/h2h/Spelle-Venhaus-vs-Bersenbrueck/4909/4927/ vs https://www.advancescores.com/match-schedule/spelle-venhaus-vs-bersenbruck-1588982

## 3. Quantitative evidence of selection inversion — descriptive, not forecasting

Within the 13 FT-verified FOCUS fixtures, pairwise concordance (ROC AUC for binary **clearing own supported line**):
- `follow_clearability_score`: **0.3690**;
- `follow_priority_score`: **0.4286**;
- original lower-is-better slate C rank: **0.3571**;
- historical `goal_signal_priority_score`: **0.3690**.

0.5 represents chance-level concordance. All four are below 0.5 in this *small, selected single slate*. These are not calibrated probabilities, confidence intervals or a validated predictive model.

Mechanism grouping among FT-verified FOCUS:
- CARRIER: **3 clears / 8 verified**, 2 unresolved;
- DISTRIBUTED: **2/3**, 1 unresolved;
- TWO_ROUTE: **1/2**.
- Two C-certified G4/O3.5: Košice failed, Monza cleared, **1/2**.

The popular proposed blanket `MEDIUM` or distributed-only veto is **unsupported**: Bayern and Al Khalidiyah both cleared despite distributed G3, while several CARRIER certificates failed. A prior replay found that a broad veto would suppress numerous successful historical G3s. These outcomes motivate a better *independent third-goal bridge*, not a uniform threshold increase.

### Same-evidence counterfactual — shadow only
**Pre-registered before the completed Oct 29 results:** select the seven lowest C-rank FOCUS fixtures (operational grade A), not kickoff-first FOLLOW. Overlap 5/7; removes Goa and Nasaf, adds Spelle and Celtic. On currently verified outcomes: **2 clears / 6 verified** (Celtic + Beltinci), **4 misses**, Spelle unresolved/conflicting. Champion 1/7. This shadow is **not evidence that global rank is good or profitable**, and it ignores execution timing. It does demonstrate that simply reversing FOLLOW capacity cannot fix the underlying C ranking.

## 4. Confirmed structural /sweep defects

1. **Research admission starved by provider-first bounded cohort.** The midnight interval **00:00–03:00 ICT inclusive** contains 154 discovered rows, 26 normal C admissions, 81 deferred **including 79 senior domestic cups**. This includes Liverpool–Chelsea 03:00, Manchester City–Brighton 02:30, KNVB ties, Bayern–Magdeburg, etc. None received native C assessment; do not label as C PASS or infer they'd win.
2. **Exact league_registry cup alias mismatch.** A name `EFL Cup: Round 4`, `DFB Cup: Round 2`, `KNVB Beker: Round 1` misses exact normalized registered cup strings and falls into generic discovery. `goals_first_intake.py` leaves `research_cohort_disposition=DEFERRED_RESEARCH_BACKLOG` sources unresearched; `/rank` cannot recover them from existing 34.
3. **Research completeness overinterpreted.** `rank_receipt.research_complete=true` is accurate only for 34 admitted; 131 unresearched source rows still exist. User-facing board must distinguish `research_complete_admitted` from `whole_source_research_exhaustive`. This is not a source-list incompleteness claim: all 553 source fixtures were registered.

## 5. Confirmed structural Football C ranking discrimination defects

1. **All four key risk axes are MEDIUM for 16/16 FOCUS:** frozen `failure_resistance`, `burden_protection`, `burden_stall_risk`, `opponent_leakage`. All 16 have `failure_attacks_route=false` and `material_suppression=false`; **16/16** receive `G3_COMPARABLE_CONTEXT_TRANSFER_REVIEW` from shadow. This uniform profile can certify risk but **does not distinguish relative reliability**.
2. In `core.py::c_g3_endpoint_control_pressure`, multiple MEDIUM cautions collapse to one `MODERATE` result via `or`. This is intentionally non-vetoing; it removes count/severity of interacting football risks from FOLLOW discrimination. The shadow `goal_burden_shadow.py` currently fires a G3 label based on a G4-ish `upper_tail_comparable_context_signal`, yielding 16/16 FOCUS identical warning and zero triage value.
3. High-profile actual misses were **already anticipated in frozen prose**, but prose did not become a discriminating proof: Chelsea W's recent UEFA 1–0/0–0 and Roma 0–0/0–6, Venezia's 2–0 control and poor home finishing, Brommapojkarna facing Häcken's four clean sheets, and Nasaf against a Kuwait scorer whose 6/7-goal data were from domestic rather than comparable continental fixtures. These are concrete source-based test cases for future structured G3 route/reply proof, **not a hindsight license to toggle today’s grades**.
4. `follow_priority_profile` produces **relative, deterministic workload points**, not calibrated `P(goals > line)`. Original #1 Venezia scored clearability 64 but had 0–2; #2 Košice clearability 48 and certified G4/O3.5 despite a 0–1. No demonstrated probabilistic ranking separation for the protected burden.
5. `adapter.py::_allocate_c_follow_lanes` takes chronological one-per-kickoff primary before strongest global secondary. The **seven FOLLOW capacity slots were full by 01:00 ICT**. Later higher-ranked FOCUS rows (#4 Spelle, #7 Celtic, #9 Lyon, #10 Monza) were RESERVE or FOCUS_UNFOLLOWED, not FOLLOW. Since global C rank also inverted, **allocation-only repair is inadequate**.

## 6. Immediate controlled repair contract (NOT automatically applied)

**P0 source coverage and identity**
- Preserve user exclusions/friendlies and national league identity. Add explicit bounded, source-verified cup canonical aliases + round/group-stage stripping **only** for approved senior competitive cups. Require cup format/incentives evidence per fixture.
- Build **multiple sequential <=30 researched-fixture batches** against one sealed source epoch; prioritize previously unresearched in-scope fixtures by time-to-kickoff and goal-research viability. Do not use league prestige as a positive G3 gate.
- Display `DEFERRED`, `SCREENED_OUT`, `EVIDENCE_LIMITED`, and negative controls separately; source-to-rank coverage denominators by kickoff block must be visible. Add exact canonical opponent alias reconciliation (e.g. `Hyderabad FC` -> `Sporting Club Delhi`) with original provider ID and source evidence, not unproven string replacement.

**P1 independent G3 mechanism proof (shadow first)**
- For all FOCUS, REVIEW and specifically rejected high-potential controls, collect source-backed **comparable-context carrier 3+ capacity**, **repeatable opponent 1-goal reply**, specific 2+1 / 1+2 completion, **0–0 / 1–1 / 2–0 stall endpoint**, and opponent-specific score-state continuation. Separate G3 comparator from G4 tail transferability.
- Encode per-axis independent evidence references, freshness, caveats and contradiction resolution instead of repeating all-MEDIUM grades; preserve unconfirmed as UNVERIFIED, not automatically HIGH or LOW. Preserve one-team funded O2.5 where defensible.
- Test two-route conditional risk prospectively; **never implement blanket multi-MEDIUM veto** without proof. Run a distinct, verified G4 path audit before O3.5/O4+ issuance.

**P2 portfolio and opportunity**
- Treat published `FOLLOW` as an execution workload budget, not a probability rank. Evaluate kickoff-safe quotas, protected later-block capacity, and global top-rank shadows on **same frozen inputs and certified burden**. No outcome-trained immediate switch.
- For already-started matches, do not retroactively grant prematch rank; exceptional XI assessment remains its own authority.
- Respect screenshot-only odds and confirmed slips. Google Sheets remains active; Airtable historical read-only; no `BOOK` event or exposure without verified user fill.

**P3 regression and promotion gate**
- Reproduce current 553->34->33->16->7 exactly before changing any policy. Enforce no retro mutation of Oct 28 source, certificate, outcomes or previous repairs (PR 201/202).
- Replay earlier untouched Oct 23–27 negative controls and selection-inversion sessions; reserve later truly unseen slates for prospective challenger. Compare **G3 false positives, omitted 3+ recall, supported-line clear rate, kickoff feasibility, research latency**, false veto counts and coverage denominator.
- Promotion requires improved *both* precision/recall and operational timeliness without gaming unsupported odds or excluding difficult known losses.

## Audit verdict
**FAIL — upstream selection and portfolio ranking reliability, with a separately CONFIRMED source-research coverage deficit.** The 1/7 certified FOLLOW outcome and sub-0.5 in-sample ordering AUC justify urgent controlled repair, but this single slate does **not** validate any specific replacement weighting or threshold. Keep main unchanged pending prospective repair and regression.
