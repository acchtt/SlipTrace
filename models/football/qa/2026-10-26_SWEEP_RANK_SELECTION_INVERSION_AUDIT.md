# Football C — /sweep + /rank selection-inversion audit

**Date:** 2026-10-26 ICT  
**Authority:** Football C only  
**Production code audited at:** `36e3be3b4d019a33f185bdbf1bae9531e9d2f804`  
**Target:** `/sweep` admission/research ordering + `/rank` certificate/ranking/FOLLOW selection  
**Explicitly out of scope:** `/xi` execution policy  
**Predictive production changes in this audit:** NONE

## Executive finding

The current failure is primarily an upstream match-selection problem.

The 25 Oct frozen session does **not** support blaming `/xi` for choosing the
wrong matches. `/xi` received a badly separated candidate set from
`/sweep -> /rank`.

The strongest same-session evidence is the morning cohort:

- `/sweep` admitted 12 fixtures; 6/12 later produced 3+ goals.
- 12 source-quantified WATCH fixtures excluded from the active cohort produced
  5/12 3+ goals.
- `/rank` then split its 12 assessed rows into 5 FOCUS/RESERVE and 7 STOP.
- The 5 FOCUS/RESERVE rows produced only **1/5** 3+ goals.
- The 7 STOP rows produced **5/7** 3+ goals.

So the most severe inversion happened **inside /rank after sweep admission**.

Across the two frozen rank cohorts (66 assessed fixture-epochs):

| Rank/lane state | Rows | 3+ goals | Rate |
|---|---:|---:|---:|
| FOLLOW | 11 | 6 | 54.5% |
| RESERVE | 5 | 3 | 60.0% |
| FOCUS_UNFOLLOWED | 33 | 19 | 57.6% |
| STOP | 17 | 11 | 64.7% |

This is one session, not a population estimate. It is nevertheless a valid
failure sample because the states were frozen before outcomes and the audit
joins outcomes only after the selection decisions.

## Frozen cohorts

### Morning

Run: `V4-20261025-0909-20261025-1200-FULLRESEARCH`

- active targets: 24
- sweep eligible targets: 12
- sweep WATCH targets: 12
- rank assessed: 12
- FOCUS/RESERVE: 5
- STOP/REVIEW_ONLY: 7

Rank split:

| Match | Rank state | FT goals |
|---|---|---:|
| Seongnam–Suwon Bluewings | FOLLOW O2.5 | 2 |
| San Diego–Seattle | FOLLOW O2.5 | 4 |
| Nagoya–Yokohama F.M. | FOLLOW O2.5 | 2 |
| Toyama–Sapporo | FOLLOW O2.5 | 1 |
| Oita–Kofu | RESERVE O2.5 | 2 |
| Wollongong–South Hobart | STOP | 2 |
| Sydney Olympic–Bayswater | STOP | 3 |
| Portland–Charlotte | STOP | 5 |
| Albirex Niigata–Vegalta | STOP | 3 |
| AV Alta–Corpus Christi | STOP | 4 |
| Giravanz–Nagano | STOP | 4 |
| Blaublitz Akita–Imabari | STOP | 1 |

### Main slate

Run: `V4-20261025-1323-20261026-0300-SLATEFIX`

The final rerank/presentation surface contains 54 assessed/status-accounted
rows. Excluding the one already-started status-excluded row, the researched
rank surface has 53 football assessments.

Main-slate 3+ reach:

- FOLLOW: 5/7
- RESERVE: 3/4
- QUALIFIED / FOCUS_UNFOLLOWED: 19/33
- REVIEW_ONLY/STOP: 6/9

The main slate is less inverted than the morning board, but it does not restore
meaningful separation between the scarce priority lane and the rejected lane.

## /sweep audit

### Finding S1 — CRITICAL: CONTROL_REVIEW is leaking predictive authority

The 24 Oct coordinated repair says:

> CONTROL_REVIEW itself has no certificate, state, or execution authority.

Current implementation does not enforce that boundary.

`goals_first_intake.py` deliberately chooses up to four rows whose fully
quantified screen state is `WATCH_GOAL_SIGNAL`, changes their lane to
`CONTROL_REVIEW`, and then appends them to `selected` / the rank-eligible
`eligible_queue`.

That means a negative-screen diagnostic control can be passed into Football C
exactly like GOAL_PRIORITY/GOAL_REVIEW and can emerge as production FOCUS,
FOLLOW, RESERVE or QUALIFIED.

In the two frozen cohorts:

| Intake lane | Rows | 3+ goals | Rate | Mean goals |
|---|---:|---:|---:|---:|
| GOAL_PRIORITY | 44 | 28 | 63.6% | 3.27 |
| GOAL_REVIEW | 14 | 9 | 64.3% | 2.57 |
| CONTROL_REVIEW | 8 | 2 | 25.0% | 2.50 |

The eight CONTROL_REVIEW rows were:

| Match | Frozen screen | Rank result | FT goals |
|---|---|---|---:|
| Nagoya–Yokohama F.M. | priority 44 / O2 0.55 | FOLLOW O2.5 | 2 |
| Blaublitz–Imabari | 44 / 0.55 | STOP | 1 |
| Oita–Kofu | 46 / 0.55 | RESERVE O2.5 | 2 |
| Toyama–Sapporo | 41 / 0.45 | FOLLOW O2.5 | 1 |
| Chindia–Olimpia | 42 / 0.45 | FOLLOW O2.5 | 5 |
| Midtjylland–Lyngby | 49 / 0.45 | QUALIFIED O2.5 | 5 |
| Helsingborg–Ljungskile | 36 / 0.35 | STOP | 2 |
| AZ–Twente | 48 / 0.50 | QUALIFIED O2.5 | 2 |

Six of eight negative-screen controls were promoted to a funded FOCUS
certificate; only two of those eight fixtures produced 3+ goals.

This is not a hindsight threshold argument. It is an authority-contract bug:
a calibration/control lane explicitly documented as zero-authority is currently
allowed to become production selection.

**Required repair:** keep CONTROL_REVIEW research and calibration, but remove it
from production rank eligibility. Its frozen assessment may be recorded in the
calibration ledger, but it must not create a production certificate, priority
lane, or /xi workload.

### Finding S2 — MEDIUM-HIGH: sweep discrimination is weak but not the primary inversion

The morning positive admission set produced 6/12 3+ outcomes versus 5/12 among
the source-quantified WATCH set.

That is weak separation, but it is materially less severe than the subsequent
rank split of 1/5 selected versus 5/7 STOP.

The gate remains a recent-scoreline research screen and should remain an
admission/workload signal rather than final Football C truth.

No GOAL_PRIORITY/GOAL_REVIEW numeric threshold is changed by this audit.

## /rank audit

### Finding R1 — CRITICAL: asymmetric G3 certification structurally favors carrier rows

Current `c_carrier_goal3_funded()` funds G3 when a STRONG self-funded carrier
has mostly MEDIUM supporting grades. It does **not** require:

- Step-0 goal-signal corroboration;
- burden-completion grade;
- continuation grade;
- stall-risk ceiling;
- opponent-leakage support.

By contrast, `c_two_route_goal3_funded()` requires HIGH burden completion and
HIGH continuation, while `c_distributed_goal3_funded()` requires a stricter
Step-0 goal-signal predicate plus two-sided current structure and stall control.

The sweep/rank thresholds are therefore asymmetric:

- sweep ROUTE_SCORE admission can occur at mean O2 >= 0.55;
- distributed G3 route-score corroboration requires mean O2 >= 0.65 and
  low-draw trap <= 0.20;
- carrier G3 has no equivalent Step-0 corroboration requirement.

This creates a funnel in which a weak/negative historical screen can still
become G3 if a carrier is labeled self-funded, while credible two-sided rows can
remain certificate-less.

Morning examples:

- Toyama–Sapporo: negative CONTROL_REVIEW, priority 41, mean O2 0.45,
  carrier G3 -> FOLLOW O2.5 -> 0-1.
- Nagoya–Yokohama: negative CONTROL_REVIEW, priority 44, mean O2 0.55,
  carrier G3 -> FOLLOW O2.5 -> 1-1.
- Portland–Charlotte: positive goal admission with strong two-sided score
  history, no funded G3 -> STOP -> 3-2.
- Albirex–Vegalta: positive goal admission, two strong current routes but no
  funded G3 -> STOP -> 2-1.
- Sydney Olympic–Bayswater: positive goal admission, two-sided/MIXED current
  structure but no funded G3 -> STOP -> 1-2.

Across 65 football-assessed rows:

| Compiled G3 mechanism | Rows | 3+ goals | Rate |
|---|---:|---:|---:|
| CARRIER | 46 | 27 | 58.7% |
| LEAKAGE | 3 | 1 | 33.3% |
| NONE | 16 | 11 | 68.8% |

This does **not** prove carrier should be removed or that NONE should be promoted
wholesale. It does prove that the current mechanism split failed to provide
positive separation on this frozen failure sample.

Historical replay already showed that broad distributed G3 can contain valuable
rows. Therefore the safe response is a frozen challenger, not a one-board
threshold relaxation/tightening.

**Required next step:** build a same-information G3-balance challenger that
tests symmetric corroboration / current-route requirements for carrier and
two-sided mechanisms across multiple sealed boards. Do not promote it from this
one session.

### Finding R2 — HIGH: mechanism class is too early in the official rank key

Current `ranking_key()` begins with:

1. G3 execution-floor authorization;
2. G3 mechanism rank;
3. follow clearability;
4. certificate robustness;
5. certificate depth;
6. endpoint control;
7. continuation/completion;
8. Step-0 goal signal;
9. remaining football grades.

And `c_goal3_mechanism_rank()` assigns:

- CARRIER = 4
- TWO_ROUTE = 3
- LEAKAGE = 2
- DISTRIBUTED = 1
- NONE = 0

Thus, after execution-floor eligibility, carrier identity can dominate
robustness, endpoint control and goal-signal corroboration.

This compounds R1.

The existing clearability challenger was checked on this session and does **not**
materially improve top-N outcome separation. It therefore still fails the
promotion gate.

**Required next step:** do not simply promote the existing clearability
challenger. Build the G3-balance challenger first and replay both mechanism
funding and rank ordering together.

### Finding R3 — HIGH: FOLLOW allocator has an earliest-kickoff capacity bias

`_allocate_c_follow_lanes()` first chooses one clearability nominee from each
exact kickoff block, then sorts these primary nominees by:

1. `kickoff_ict` ascending;
2. clearability;
3. rank;

and stops when `MAX_FOLLOW` is reached.

So the global FOLLOW cap can be consumed by earlier kickoff blocks before later
higher-clearability primary candidates are compared.

On the main slate this allowed early rows such as:

- Chindia clearability 31 -> FOLLOW;
- Fortuna clearability 33 -> FOLLOW;
- Norrby clearability 34 -> FOLLOW;
- Genk clearability 34 -> FOLLOW;

while later rows such as Basel (68), Sparta (60), Freiburg (60), Barcelona
(60), Molde (58) and Liverpool (57) did not receive FOLLOW.

A same-information counterfactual that simply chooses the strongest primary
clearability nominees globally still produced 5/7 3+ outcomes on this slate,
the same as the current earliest-first seven. Therefore this is a real semantic
allocator defect, but **not proven to be the cause of yesterday's losses**.

**Required repair:** remove accidental earliest-kickoff precedence from the
global quality comparison. If temporal coverage is desired, encode it explicitly
as a diversity constraint rather than using kickoff time as the leading sort
key.

## Why /xi is not the audit target

The frozen failures occur before market execution:

- many losing/low-goal rows were already promoted to funded FOCUS;
- many eventual 3+ rows were already STOP/REVIEW_ONLY;
- FOLLOW scarcity was allocated upstream.

Changing `/xi` could reduce exposure, but it would not repair the wrong match
selection. This audit therefore makes no /xi recommendation and changes no
execution policy.

## Repair classification

### Safe authority/semantics repairs

These do not fit predictive thresholds to outcomes:

1. **CONTROL_REVIEW zero-authority enforcement**
   - research/calibration only;
   - excluded from production rank input;
   - still persisted for audit denominator.

2. **FOLLOW global-cap ordering repair**
   - remove kickoff-first truncation;
   - keep exact-kickoff diversity as an explicit bounded constraint.

### Requires frozen challenger + multi-board replay

3. **G3 mechanism balance**
   - test carrier versus distributed/two-route symmetry;
   - preserve useful carrier rows;
   - recover credible two-sided rows;
   - no threshold promotion from the 25 Oct outcomes alone.

4. **Official rank-key ordering**
   - evaluate only after the mechanism challenger exists;
   - do not promote the existing clearability-only challenger from this sample.

## Acceptance criteria for the next repair

A repair may be promoted only if a same-information replay across multiple
sealed boards shows:

- no CONTROL_REVIEW row can create production selection authority;
- no loss of source/accounting completeness;
- materially improved FOCUS/STOP or top-N G3 separation;
- supported-burden reach does not collapse;
- useful distributed/two-sided recall is preserved;
- no outcome, odds or post-kickoff information enters selection;
- /xi behavior remains unchanged.

## Audit decision

**UPSTREAM SELECTION REPAIR REQUIRED.**

Primary defect location: **/rank**.

Secondary defect location: **/sweep CONTROL_REVIEW authority boundary**.

Do not respond by tightening ACT or rewriting /xi. The correct next repair is
to restore the sweep/rank authority boundary first, then replay a balanced G3
selection challenger before modifying predictive certificate thresholds.
