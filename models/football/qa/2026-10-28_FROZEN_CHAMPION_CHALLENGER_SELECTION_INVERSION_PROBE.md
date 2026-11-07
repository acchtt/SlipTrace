# Football C — 28 October 2026 frozen champion/challenger selection-inversion probe

**Status: DIAGNOSTIC ONLY — NO PRODUCTION PREDICTIVE CHANGE.** Football C remains the sole production model. This report uses the sealed rank package `Football-C-rank-20261028-through-0300-verified-published.json` and the frozen pre-kickoff source epoch `V4-20261028-1610-20261029-0300-LEAGUEPROOF` (source observed 09:20 UTC, ranking 09:43:08 UTC). HEAD examined: `946480a9e4a2a0a1bf6f69a9177ee0f785601c77`.

The four user-reported FT goal totals are **outcome overlays only**: Kashima–Pohang 3, Gamba–Buriram 2, FC Goa–Hyderabad FC 1, Nasaf–Kuwait SC 1 (winner orientation of the Kuwait shorthand unconfirmed). No final-score data was used to construct any challenger membership, mechanism grade, ranking or threshold. No filled bet or P&L is inferred. The current active Google Sheets `Decision States` and `Actual Bets — Current` match-ID columns were read through all populated rows; these four IDs had no entries on 28 October.

## 1. Frozen source accounting: denominator matters

The full LiveScore source ledger has **553 fixtures**, apportioned exactly:

| Original /sweep intake lane | Count | Meaning |
|---|---:|---|
| CLOSED | 296 | Not an open prematch opportunity within the epoch |
| DEFERRED_RESEARCH_BACKLOG | 131 | Source-discovered, not selected into bounded research |
| EXCLUDED | 34 | User or scope exclusions |
| WATCH_GOAL_SIGNAL | 30 | Terminal historical-goal screen (includes AFC 19:15 omissions and Gamba) |
| EVIDENCE_LIMITED | 24 | Insufficient source-backed history/researchability |
| GOAL_PRIORITY | 24 | Ranked research cohort |
| GOAL_REVIEW | 10 | Ranked research cohort |
| CONTROL_REVIEW | 4 | Source-labeled negative controls; **none in the 34-member eligible_queue** |
| **Total** | **553** | |

The C cohort was **34** (24 GOAL_PRIORITY + 10 GOAL_REVIEW), **33 assessed** and one status-excluded; the assessed slate yielded **16 FOCUS, 17 REVIEW_ONLY**, and the FOCUS split was **7 FOLLOW, 4 RESERVE, 5 FOCUS_UNFOLLOWED**. Completion of this 34-member cohort is not proof of coverage over the other 519 source rows. Distinguish deferred research, terminal watch, status closure, explicit exclusions and review controls rather than calling all of them C-PASS.

The 4 `CONTROL_REVIEW` source rows (not C-ranked) were AC Nagano Parceiro W–Omiya Ardija Ventus W (1814245), Urawa W–Sanfrecce Hiroshima Regina W (1814243), Radnicki Nis–Partizan Beograd (1799115) and Halmstads BK–Malmo FF (1710482). Because controls did not reach C, a full accepted-versus-rejected C replay cannot presently measure their false-negative rates.

The two AFC matches at 19:15 ICT were discovered but not ranked: Viettel–FC Seoul 1873843, `WATCH_GOAL_SIGNAL`, priority 39; Persib Bandung–Melbourne Victory 1885202, `WATCH_GOAL_SIGNAL`, priority 42. This is source-screen filtering rather than absent fixture acquisition. Carry DISCOVERED / SCREENED_OUT and explicit source reasons into website STOP visibility without fabricating a C assessment.

## 2. Mechanism-specific defects visible in current production code

- `engine/core.py::c_distributed_goal3_funded` accepts a distributed 2+1/1+2 certificate with `MEDIUM` reliability, failure resistance, protection, stall/continuation, and opponent leakage when other route and source-rate clauses pass. The historical-source gate is corroboration, not an independent current reply mechanism.
- `engine/core.py::c_g3_endpoint_control_pressure` combines many MEDIUM cautions using `or`; HIGH requires effective stall HIGH, source low-draw trap >= 0.25, or a specially verified suppressive H2H. Multiple independent MEDIUM countermechanisms still collapse to one MODERATE class. This is a **mechanical aggregation fact**, not proof that a blanket multi-MEDIUM hard veto would predict well.
- Across **all 16 FOCUS**, `failure_resistance`, `burden_protection`, `burden_stall_risk`, and `opponent_leakage` are identically `MEDIUM`. Across all 33 assessed fixtures, `failure_attacks_route` and `material_suppression` are always false. This greatly limits rank discrimination precisely where narrative `main_failure` reports opponent compactness, transferred-competition control, short-season sample, scorer concentration and travel.
- `engine/core.py::follow_priority_profile` computes a workload floor (not calibrated third-goal probability). For FC Goa and Nasaf–Kuwait, `follow_clearability_score=45` despite the former TWO_ROUTE+distributed and the latter distributed-only; both have MEDIUM failure/reliability/stall/protection and HIGH chance quality. Identical scores cannot be construed as equal objective probabilities.
- The `SHADOW_GOAL_PATH_AND_ENDPOINT_STRESS_V1` emitted **16/16** `G3_COMPARABLE_CONTEXT_TRANSFER_REVIEW` warnings for FOCUS and did not change any certificate. Its trigger examines `upper_tail_comparable_context_signal` (a G4-tail field), not a distinct, independently proven G3 reply bridge. Because all positives are flagged, the warning cannot itself order the positive cohort. Do not blanket-block on this flag.

## 3. Case comparisons (prematch features, then separately outcomes)

| Match ID | Frozen intake / C outcome | Prior evidence and limitation | Postmatch outcome overlay |
|---|---|---|---|
| **1873638** Kashima–Pohang | GOAL_REVIEW priority 49; C WATCH, no G3; /xi PASS visible O2.5 @1.82 | Long-history combined 3+ = 0.55, screen computed route 1.90/1.00; **current** C home/away USABLE, no independently certified self-funding carrier, injury/fatigue/compact-block counterevidence in `main_failure` | 3–0; O2.5 would win if placed, **not** evidence the frozen negative was irrational when evaluated |
| **1873639** Gamba–Buriram | WATCH_GOAL_SIGNAL priority 47, not C-ranked; user exception conditional G3 only | Long-history combined 3+ = 0.4875, recent Gamba latest four had 2+ scored each. The later PR #202 offers only future GOAL_REVIEW rescue. No frozen normal C record exists. | 1–1; both conditional O2.5 and visible O2.75 would lose; no bet documented |
| **1900650** Goa–Hyderabad FC | GOAL_PRIORITY 77, C FOCUS/FOLLOW O2.5, TWO_ROUTE plus DISTRIBUTED | HIGH completion/continuation and chance, but MEDIUM route/reliability/failure/stall; Chiki scored four of five season goals, lone 1–0 H2H, travel/recent competition mixing. `carrier_self_fund=false`. Frozen identity remains Goa–Hyderabad despite conflicting Delhi research text. | 0–1; G3 certificate MISS |
| **1873835** Nasaf–Kuwait | GOAL_PRIORITY 67, C FOCUS/FOLLOW O2.5, DISTRIBUTED only | HIGH chance but MEDIUM completion/continuation/reliability/failure/stall, no self-funded carrier, prior continental 0–0 and non-transferable high domestic Kuwait goals documented in `main_failure`. | One goal total (Kuwait shorthand 1–0, winning side unverified); G3 certificate MISS |

Important distinction: the historical `goal_screen.carrier_route` is a screening statistic, **not** an independently proven current one-team three-goal carrier. Raising Kashima's production carrier grade based on the 3–0 FT would leak outcome information.

## 4. Frozen champion versus two read-only challengers

**Champion:** Seven FOLLOW rows allocated by `adapter.py::_allocate_c_follow_lanes`. The allocator nominates one `CLEARABILITY` primary per exact kickoff block and fills primary nominations chronologically before secondary candidates. All seven October 28 FOLLOWs were first-block `CLEARABILITY` nominees; the FOLLOW capacity was exhausted by the 01:00 ICT block. This makes FOLLOW a **time-distributed workload allocation**, not the seven best C ranks.

**Challenger A (deterministic, shadow only):** Pick the seven FOCUS / operational-grade-A fixtures with the lowest existing frozen C `rank` (tie-break kickoff, match ID), without any new grade, quote or outcome. Retains **5/7** champion choices. Swaps out:
- Nasaf–Kuwait, frozen rank 12, distributed O2.5, clearability 45;
- Goa–Hyderabad, frozen rank 11, two-route O2.5, clearability 45.

Replacements are:
- Spelle-Venhaus–TuS Bersenbrueck, rank 4, carrier O2.5, clearability 45;
- Celtic–Dundee United, rank 7, carrier O2.5, clearability 36.

The two removed fixtures are **known** G3 misses, but the two added fixtures have **no FT labels in this probe**. This is not a demonstrated gain in accuracy. A global ranking allocator also risks neglecting earlier kickoff /xi deadlines, and earlier experiments found global allocation regressions. **Do not deploy it based on October 28.**

**Challenger B (source-proof diagnostic; NOT A VETO):** Flag a funded FOCUS for independent comparable-competition reply-bridge recheck when `carrier_self_fund=false` plus `MEDIUM` route reliability, failure resistance, burden protection and opponent leakage. This flags **5/16** FOCUS: FC Goa (1900650), Nasaf–Kuwait (1873835), Bayern W–Real Madrid W (1887690), Al Khalidiyah–Al-Wahda (1873836), London Lions–Ware (1859839). It leaves current certificates, rankings and XI unchanged. None of these five should be automatically PASSed: their complete forward outcomes are not available and a similar prior all-MEDIUM rule discarded winning games.

Kashima and Gamba remain unchanged under both shadow challengers; this is a necessary negative-control finding. No simple reallocation or hard multi-MEDIUM veto can currently claim to solve missed one-team carriers.

## 5. Evidence-backed next challenger: new source-level G3 bridge, not new outcome-tuned threshold

Define and prospectively freeze **separate evidence objects** for:

1. **ONE_TEAM_G3:** 3-goal team supply, named current suppliers/finishers, feasible substitutions, opponent match-specific leakage, and a 2–0 continuation test. Do not identify a strong carrier just from four recent 2-goal games or one 3–0 FT.
2. **DISTRIBUTED_G3:** independent 2+1 / 1+2 contribution proof by each side in *comparable current competition*; direct opponent reply route rather than a high aggregate 3+ rate; credible 1–0/1–1 stall breaks; availability and travel effects.
3. **CONTEXT_TRANSFER:** same-competition evidence hierarchy, domestic-to-continental transfer uncertainty, match format/incentives, GD/draw utility, rivalry and fatigue. A G4 upper-tail transfer flag cannot stand in for G3 context proof.
4. **G4_AFTER_G3:** independent fourth-goal continuation and precise Asian-line settlement; never upgrade a funded G3 just because the historical O3.5 rate is high.

Every field must distinguish `VERIFIED_SUPPORT`, `VERIFIED_COUNTEREVIDENCE`, `UNKNOWN` and `NOT_APPLICABLE` and carry timestamped source refs. `UNKNOWN` must not silently become neutral. Freeze these **for FOCUS, REVIEW, negative screen controls and admitted review rescues**, then compare to the untouched champion on identical prematch availability and evidence. Start with shadow outputs, not an overnight threshold/score patch.

## 6. Release gate and exact denominators

- **Source recall:** all 553 source fixtures stratified by CLOSED / EXCLUDED / EVIDENCE_LIMITED / DEFERRED / WATCH / admitted; compare candidate-specific research admission and the first full C assessment **before kickoff**, not simply sealed research_complete.
- **Predictive precision and reach:** every assessed or sampled negative control, separate G3 O2.5 from G4 O3.5 and O2.75/O3.0/O3.25 Asian full/half/push/loss settlement. Record first goal, 1–0/1–1/2–0 stalls, scorer concentration, and same-competition bridge validity.
- **Selection opportunity:** compare two rank epochs rather than erasing earlier FOLLOW; compare FOLLOW vs RESERVE vs STOP under the same frozen period. Preserve actual quote epoch and custom-line feasibility; no internet odds.
- **Unseen slates and rollback:** freeze challenger definition in advance, run multiple independent future slates with both positives and negatives, examine confidence intervals and false-positive / false-negative tradeoffs, and promote only if recall and burden precision improve without major missed winning carriers or late /xi outcomes.

**Decision: Do not merge a predictive scoring rule or FOLLOW allocation change from these observations.** PR #201 and #202 remain preserved. PR #202 is an intake research-recall repair only and does not predict G3 winners. Current diagnostics pinpoint *why* the allocator and G3 compiler can favor failing fixtures, but no statistically supported replacement has yet been established.
