# October 29 00:00–03:00 ICT: Frozen source-vs-rank coverage incident

**Status:** Evidence-backed operational investigation; no prospective odds, G3/G4 certificates, ACT, bets, or production policy changes.

**Evidence:** Read the 28 October 16:10 ICT → 29 October 03:00 ICT sealed bundle `Football-C-rank-20261028-through-0300-verified-published.json`, specifically `source_bundle["source.json"]`, `source_bundle["v4_sweep_ready.json"].source_ledger`, `rank_receipt.board.matches`, and `stage.py`/`goals_first_intake.py`/`league_registry.py`. Source observed at 2026-10-28 09:20 UTC (16:20 ICT). All below are **frozen source statuses**, not a fresh 29 October live-status confirmation. All times ICT on 29 October.

## Exact 00:00–03:00 source accounting

Filter the original 553-row source ledger to `2026-10-28T17:00:00+00:00 <= kickoff_utc <= 2026-10-28T20:00:00+00:00` (00:00–03:00 ICT, inclusive).

| Source intake disposition | Rows | Significance |
|---|---:|---|
| DEFERRED_RESEARCH_BACKLOG | 75 | No validated football-history enrichment; **73 domestic cups**, 2 leagues |
| GOAL_PRIORITY | 19 | Normal Football C research admission |
| GOAL_REVIEW | 5 | Normal Football C research admission |
| WATCH_GOAL_SIGNAL | 15 | Source-screened, no normal Football C research |
| EVIDENCE_LIMITED | 10 | Source history below minimum/other evidence limitation |
| EXCLUDED | 18 | User/scope exclusions; do not automatically lift |
| CONTROL_REVIEW | 1 | Negative-control calibration; not production rank admission |
| **Total** | **143** | Original source rows in this time block |

**Only 24/143 were admitted to normal C research (19 priority, 5 review).** Do not treat 119 non-admissions as model PASS: 75 are unresearched, 15 have only a negative source-goal screen, 10 evidence-limited, 18 explicit exclusions, and 1 negative control.

### Deferred by named competition (all 75)
- Spain Copa del Rey: Round 1: **20**
- Norway NM Cup: Round 3: **12**
- Germany DFB Cup: Round 2: **8**
- Netherlands KNVB Beker: Round 1: **8**
- England Women's League Cup: **7**
- England EFL Cup: Round 4: **4**
- Austria OFB Cup: **3**
- Poland Cup: **3**
- Greece Greece Cup: Group Stage: **2**
- Romania Romanian Cup (Groups B and D): **2**
- Czech Republic Cup: **1**
- Denmark DBU Pokalen: **1**
- Italy Serie C: Group B: **1**
- Switzerland Promotion League: **1**
- Turkiye Cup: Qualification: **1**
- Uruguay Copa Uruguay: **1**

### Concrete source-discovered but never C-assessed examples
| ICT kickoff | Match ID | Frozen fixture | Frozen status |
|---|---|---|---|
| 00:00 | 1889002 | SW Bregenz–FC Salzburg | DEFERRED_RESEARCH_BACKLOG |
| 00:00 | 1894944 | Rosenborg–HamKam | DEFERRED_RESEARCH_BACKLOG |
| 00:00 | 1888385 | Freiburg–Wolfsburg | DEFERRED_RESEARCH_BACKLOG |
| 01:30 | 1882525 | PAOK–AEK Athens | DEFERRED_RESEARCH_BACKLOG |
| 02:00 | 1870279 | Manchester United W–Burnley W | DEFERRED_RESEARCH_BACKLOG |
| 02:00 | 1899135 | MVV Maastricht–Excelsior | DEFERRED_RESEARCH_BACKLOG |
| 02:00 | 1899126 | PEC Zwolle–TOP Oss | DEFERRED_RESEARCH_BACKLOG |
| 02:30 | 1894849 | Manchester City–Brighton | DEFERRED_RESEARCH_BACKLOG |
| 02:45 | 1888389 | Bayern Munich–Magdeburg | DEFERRED_RESEARCH_BACKLOG |
| 02:45 | 1888394 | Bayer Leverkusen–1. FC Nuremberg | DEFERRED_RESEARCH_BACKLOG |
| 02:45 | 1894156 | AFC Bournemouth–Aston Villa | DEFERRED_RESEARCH_BACKLOG |
| 02:45 | 1894155 | Fulham–Crystal Palace | DEFERRED_RESEARCH_BACKLOG |

The names here indicate research priorities, **not** goal predictions, booked bets or XI exceptions.

### Separate screen misses (not unresearched)
- AC Milan–Bologna (00:30, 1785364), priority 40, WATCH_GOAL_SIGNAL
- Parma–Udinese (00:30, 1785368), priority 47, WATCH_GOAL_SIGNAL
- Al-Faisaly–Al Taawoun in AFC Champions League Two (01:15, 1873864), priority 46, WATCH_GOAL_SIGNAL
- Genoa–Juventus (02:45, 1785367), priority 43, WATCH_GOAL_SIGNAL
- Aberdeen–Falkirk (02:45, 1792824), priority 42, WATCH_GOAL_SIGNAL

These fixtures *received* a quantified historical goal screen; any rescue must be evidence-backed and review-only until genuine current C research.

## Mechanistic diagnosis

1. **Source acquisition selected a bounded research cohort before full match-history qualification.** The deferred raw fixtures carry `research_cohort_disposition = "DEFERRED_RESEARCH_BACKLOG"`, but no `football_evidence`, verified `researchability_proof` or cup `tournament_format_proof`. `goals_first_intake.py::select` preserves this status instead of promoting missing-history rows automatically. Subsequent `/rank` correctly assesses only `eligible_queue`, so reranking the 34 won't reveal the omitted cups.
2. **Exact cup-name matching misroutes many legitimate cup labels.** `league_registry.py` recognizes `("england","efl cup")`, `("netherlands","knvb beker")`, `("spain","copa del rey")`, and `("germany","dfb pokal")`, but the provider labels contain `Round 4`, `Round 1`, or `DFB Cup: Round 2`. Their normalized names fail exact-match registration and enter generic `DISCOVERY`. This is an independently reproducible registry classification defect, **not** sufficient by itself to fund C admission. Norwegian Cup and English Women's League Cup have no equivalent approved registered alias in that mapping; review scope explicitly rather than silently registering all youth/friendly or excluded cups.
3. **Cheap-filter neutrality becomes research starvation.** The major deferred cup examples have `cheap_filter.priority = "NEUTRAL_RESEARCH"`, reason `NO_ACTIVE_CHEAP_FILTER_PROFILE`. Only 4 priority-research backlog rows across the **entire** slate were selected; the other missing-history rows remain deferred unless explicitly promoted in further source-research batches. `SWEEP.md` permits batches <=30 and further batches of in-scope fixtures; the active cohort's completion is not whole-source research completeness.
4. **UI omission amplifies the problem.** FOCUS-only publishing hides `DEFERRED_RESEARCH_BACKLOG` and `WATCH_GOAL_SIGNAL`; do not translate either to a fictional C-PASS. Show DISCOVERED / SCREENED_OUT / RESEARCH_PENDING / REVIEW / FOCUS / FOLLOW / STOP with unassessed source status prominently labeled.

## Prospective repair proposal (NOT applied to the frozen source)

- **Registry recognition:** canonicalize only specifically approved cup base names with bounded stage suffixes (`Round N`, group stage, quarterfinal, semi-final), and add verified equivalents such as DFB Cup ↔ DFB Pokal. Preserve explicit user-country, league, friendlies, and youth restrictions. Regression test provider strings against exact current CUPS registration.
- **Acquire before screen:** source-backed valid history, researchability status, and fixture-specific cup format/incentive proof should be fetched for each admitted cup research candidate; no invented histories. Include pre-kickoff time remaining and approved competition priority in the *research queue*, without equating cup prestige to goals probability.
- **Expand bounded research in multiple batches:** retain <=30 per batch, continue in-scope priority fixtures in the same complete source receipt. Track `deferred_research_count_by_kickoff_block`, `deferred_priority_competition_count`, `first_C_assessment_before_kickoff`, and `whole_source_research_exhaustive` independently. A successful bounded batch cannot silently imply the entire provider window was screened.
- **Historical safety:** this sealed October 28 source and all prior ranks remain immutable. For matches already started, do not backfill normal prematch authorization; use an explicitly labeled retrospective assessment. For upcoming windows, only a new complete source acquisition with fresh evidence and verified /rank readback may publish an official new board.
- **Validation:** replay the 553 source fixture dispositions (all 143 midnight rows), verify no exclusions or positive C admissions change without evidence, track extra research workload and time-to-kickoff, and hold out additional slates before promoting an operational selection policy.

**Conclusion:** This midnight omission is overwhelmingly a **cup research-coverage problem** (73 deferred cups), worsened by exact-name registry matching and a neutral research-priority queue. It does *not* establish that the omitted matches were winning Over candidates, and it cannot be repaired by reranking the existing 34 only.
