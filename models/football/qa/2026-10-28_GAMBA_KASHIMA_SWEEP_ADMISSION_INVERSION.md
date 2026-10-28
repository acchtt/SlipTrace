# October 28 — Gamba–Buriram versus Kashima–Pohang intake/exception discrepancy

## Frozen evidence, not postmatch fitting
Sealed original-source receipt: `V4-20261028-1610-20261029-0300-LEAGUEPROOF`, verified published Football C bundle. Source observed **2026-10-28 09:20 UTC (16:20 ICT)**. Both fixtures kicked off **10:00 UTC (17:00 ICT)**.

| | Gamba–Buriram | Kashima–Pohang |
|---|---|---|
| match_id | 1873639 | 1873638 |
| raw LiveScore source fixture | PRESENT | PRESENT |
| registry | CONDITIONAL, AFC Elite East | CONDITIONAL, AFC Elite East |
| source-backed screen priority | 47 | 49 |
| full-historical mean O2.5/3+ | 0.4875 | 0.5500 |
| full-historical mean 4+ | 0.4375 | 0.4000 |
| low-draw trap | 0.125 | 0.150 |
| computed carrier / other route | 1.4625 / 1.45 | 1.90 / 1.00 |
| sweep lane | WATCH_GOAL_SIGNAL | GOAL_REVIEW |
| selected in `eligible_queue` | NO | YES |
| production Football C `goal3_funded` | NOT ASSESSED | false |
| production board | NONE | WATCH / REVIEW_ONLY; no certified Over |

Gamba was in the 553-fixture **source** but not in the 34-member **eligible_queue**. The latest intake routine treats a verified `WATCH_GOAL_SIGNAL` result as a terminal negative screen and does not send it to Football C unless selected into the bounded CONTROL_REVIEW lane. Kashima passed a secondary `NEAR_CUTOFF_CARRIER_SECONDARY_REVIEW` pathway, subsequently received a researched C verdict of WATCH, and was not granted a G3 certificate. The user-reported /xi exceptions: Kashima PASS on screenshot O2.5 @1.82; Gamba better conditional G3 case on screenshot O2.75 @1.94 but no direct ACT; custom O2.5 @1.65+ was a possible conditional target, price not independently filled/verified. These /xi results are **not evidence of an actually placed bet** and are not authority to backfill prematch C rank.

### Precise screening blind spot
The historic screen averages the full validated recent history, up to 10 results per team. Gamba's most recent four: **2-2, 2-1, 2-2, 3-1** (all 3+), with Gamba scoring **2+ in all four**; Buriram's latest four include **2/4 games with 3+ goals**. Gamba also had continental **4-1 and 3-1** pre-match scoring comparators. The long-history combined mean O2.5 is only **0.4875**, and its composite research priority **47** falls below the existing 50 regular review and 49 secondary review priority floors; it also lacks the 1.75 computed carrier-route threshold. Its low 0-0/1-1 trap rate did not help.

Kashima's four newest totals were **5,4,2,1** (only 2/4 were 3+); Pohang's latest four were **4,0,2,3** (2/4 3+). Kashima's historical mean O2.5 0.55, priority 49 and computed route 1.9 admitted it to the near-carrier research lane. Football C then assessed opponent compactness, fatigue, injury, striker availability (Leo Ceara) and a plausible 1-0/2-0 or 1-1 endpoint; WATCH/REVIEW and later /xi PASS are thus **not logically contradictory**.

This demonstrates **selection inversion at the source-history admission boundary**. The earlier PR #201 added research-deadline tracking for the *34 eligible fixtures*, not coverage of the **other 519 source fixtures** (which contain different types of non-eligibility, including screen exclusions). It therefore could not have rescued Gamba from a terminal historic goal-screen rejection.

### Prospective repair: research admission only

The narrow extra `RECENT_4_MATCH_2PLUS_CARRIER_SECOND_ROUTE_REVIEW` path triggers only if:
- Two independently sourced and already validated four-result histories are available;
- one side has **3+/4** recent matches of 3+ *and* **3+/4** recent games scoring 2+;
- the other side has **2+/4** recent matches with 3+;
- the combined source-history 0-0/1-1 trap remains no higher than 0.25;
- timestamp is in a **future** match's prematch window, on or after **2026-10-28 10:05 UTC**, so the October 28 09:20 source remains unchanged.

It produces **`DISCOVERY_GOAL_REVIEW` only**, never `DISCOVERY_GOAL_QUALIFIED`, Football C G3/G4, FOCUS/FOLLOW, an execution verdict or a bookmaker quote.

An isolated review on the frozen 553-fixture source, restricted to terminal WATCH with existing valid four-result evidence, nominated **four** candidates under that prospective criterion (including Gamba). **No outcome-based threshold promotion** or historic receipt rewriting was performed. Multiple future slates should be monitored for selection recall and review workload before any stronger path.

### Status

- Existing verified Oct 28 16:20 ranking is immutable; Gamba kicked off at 17:00 ICT and must **not** be retroactively ranked as prematch.
- Regression controls enforce old-source replay, Kashima unchanged, newly reviewable later prematch cases, no retroactive started-fixture admission and no synthetic betting authority.
- PR changes `discovery_goal_gate.py` and regression tests, not Football C core/adapter scoring or current XI policy.
