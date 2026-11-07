# /block — Low-usage sweep + rank hybrid

Effective 2026-11-07 ICT.

Purpose: replace the expensive equal-depth full-block assessment with one
bounded selection pass. /block is a **selection workflow**, not a deep Football
C assessment of every fixture.

The user intent is:

`complete kickoff block -> sweep every fixture cheaply -> rank qualified survivors -> /xi deep-assesses only selected fixtures`

This combines the useful parts of /sweep and /rank without paying the token/
research cost of ASSESSMENT_DEPTH_V3 for every match.

Load:
- `../CURRENT_MODEL.md`
- `COMMAND_ALIASES.md`
- `../stages_v4/SWEEP.md`
- `../stages_v4/RANK.md`
- `02_NORMAL_CHAT_XI_ODDS.md` only when /xi is requested

## 1. Resolve the complete block

Resolve all in-scope, unstarted fixtures in the requested kickoff window before
selection. Started/finished fixtures and explicit user exclusions are removed
with a visible reason.

Do not deep-research every fixture merely because it exists in the block.

## 2. Stage A — lightweight sweep

Run the whole block through the **same active V4 /sweep intake filter policy**.
The only extra precondition is the requested kickoff-block boundary. After that,
reuse the same /sweep inclusion/exclusion rules, user exclusion list,
competition/fixture eligibility, operational-observability gates, source
quality gates and goals-first qualification thresholds. /block must not invent
or loosen a separate filter policy.

For every fixture collect only enough source-backed information to decide
whether it deserves ranking attention:

- fixture identity, kickoff, competition and status;
- operational observability / likely XI availability;
- current competition goal environment;
- recent comparable scoring/conceding signal;
- home/away attack and leakage signal;
- obvious low-output/control warning;
- tournament/incentive state only to the depth needed to avoid a false
  qualification;
- explicit exclusions/blockers.

This stage MUST NOT perform the full ASSESSMENT_DEPTH_V3 manifest, full H2H
study, G4 evidence contract, detailed 0-0/1-1/2-0 failure tree, certificate
compilation or Decision States persistence for every fixture.

Outputs are lightweight dispositions such as:

- `QUALIFIED_FOR_BLOCK_RANK`
- `RESERVE_SIGNAL`
- `SCREENED_OUT`
- `RESEARCH_BLOCKED`

Screening is goals-first. Popularity, league prestige and existing global rank
must not rescue a weak goal signal.

## 3. Stage B — rank the qualified survivors only

Build the display pool from `QUALIFIED_FOR_BLOCK_RANK`, the strongest
`RESERVE_SIGNAL` rows, **and high-score `RESEARCH_BLOCKED` rows**. A blocked row
is displayable when its frozen V4 goal `priority_score >= 60` (the active strong
GOAL_PRIORITY score floor) or its frozen goal screen is already
`DISCOVERY_GOAL_QUALIFIED`. Keep its blocker visible; display inclusion does not
resolve research, format, identity or observability requirements.

Use a bounded rank-lite comparison built from the Stage-A evidence.

**Do not copy the raw /sweep research order into the shortlist.** Sweep priority
is a workload order; block promotion is a separate operational selection step.

First assign every qualified survivor an operational promotion band:

- **Band A — preferred:** senior top-flight men/women, senior continental
  competition, or another established professional competition with current
  fixture identity and researchability channels verified. Women's domestic
  top flights explicitly belong here when identity is verified.
- **Band B — normal:** researched professional lower divisions / second tiers
  with adequate current channels.
- **Band C — low-tier caution:** regional, semi-professional, amateur, reserve,
  obscure lower-tier or otherwise weak-observability competitions.

A Band C fixture may not displace a credible Band A fixture merely because its
raw recent-goal score is extreme. Cross-band promotion from C over A requires
both:

1. a materially stronger frozen goal signal (default: at least **15 priority
   score points** higher); and
2. verified current researchability plus likely XI/team-news availability.

If either condition fails, keep the low-tier fixture as RESERVE even when its
raw 3+/4+ rates are huge. This is an operational reliability rule, not a
league-prestige prediction bonus: a weak Band A goal signal is still screened
out and cannot be rescued by status.

Before the normal within-band ordering, apply one narrow **HIGH_4PLUS_RESCUE**
to Band-A fixtures only. A `GOAL_REVIEW` / `RESERVE_SIGNAL` row enters the
five-match promotion comparison when all frozen sweep conditions are true:

- mean 4+ rate >= **0.55**;
- carrier route >= **1.75**;
- low-draw-trap rate <= **0.20**;
- fixture identity/researchability is verified;
- no explicit exclusion or unresolved competition-format blocker applies.

This is a promotion rescue, not a goal certificate and not an automatic top-five
slot. It exists specifically to prevent the composite-score threshold from
burying a top-flight fixture whose upper-tail sample is already strong. Do not
require priority_score >=60 for this rescue, and do not convert the row to
GOAL_PRIORITY in the frozen sweep receipt.

For rescued rows, compare the **4+ rate before the raw priority score**. A
rescued row may outrank a non-rescued same-band candidate when its upper-tail
signal is materially stronger, even if its composite score is lower. Never
use league status alone to trigger the rescue.

Within the same promotion band compare:

1. current scoring-route strength;
2. opponent leakage / opening tendency;
3. recent comparable **4+ signal**, including HIGH_4PLUS_RESCUE status;
4. recent comparable 3+ signal;
5. game-state / incentive pressure;
6. endpoint/control risk;
7. observability and XI readiness;
8. raw composite priority score as a later tiebreak, not a threshold cliff.

Do not compile a protected O2.50/O3.50 certificate at /block. Do not run the
full Football C XI runtime for every candidate.

Default output is a compact **five-match block board**. Fill up to five slots
from the strongest rankable candidates plus eligible high-score blocked rows.
Use explicit display states:

- `PROMOTED_FOR_XI` — lightweight block selection cleared;
- `HIGH_4PLUS_RESCUE` — Band-A review/reserve row admitted to promotion
  comparison by the 4+ >=55%, carrier >=1.75, trap <=20% rescue;
- `RESERVE_SIGNAL` — qualified but below the promoted priority;
- `HIGH_SCORE_RESEARCH_BLOCKED` — frozen score >=60 / GOAL_PRIORITY-quality,
  but unresolved research/format/identity/observability blocks normal promotion.

A `HIGH_SCORE_RESEARCH_BLOCKED` row may appear inside the five-match board when
its frozen signal is stronger than lower displayed reserves, but it has **zero
/xi authority until the named blocker is resolved**. Do not silently replace it
with a weaker ready match merely to keep the board all-actionable. If fewer than
five credible/high-score rows exist, show fewer; never pad with weak matches.

## 4. Relationship to /xi

A new lightweight /block receipt is selection metadata only. It does NOT itself
authorize ACT/BOOK/PASS and does NOT substitute for the full Football C
assessment.

When the user sends `/xi` for a block-selected fixture:

1. perform the full market-independent ASSESSMENT_DEPTH_V3 Football C research
   for that fixture only;
2. use confirmed XI/availability if supplied;
3. compile G3/G4 and supported burden;
4. evaluate only the user's supplied screenshot quote when present;
5. persist Decision States and independently read back before publishing a
   priced verdict.

If no compatible historical full BLOCK/RANKED authority exists, the selected
fixture uses the normal exact-user DIRECT /xi path. This is intentional: deep
research is deferred until /xi instead of being duplicated across the block.

## 5. Usage invariant

The principal cost-saving invariant is:

**Never run full Football C deep assessment on every fixture just to select the
best few.**

/block should be materially cheaper than running /xi candidate-by-candidate or
running a full whole-slate /rank. Reuse current sweep/source snapshots whenever
possible and avoid re-researching resolved fixture facts.

## 6. Odds

/block does not search bookmaker odds and does not publish ACT/BOOK/PASS.
A user screenshot remains the sole odds authority for later /xi evaluation.

## 7. Historical compatibility

Historical `football-block-runtime-v1` full-assessment receipts remain
readable and may retain their old authority. They are not the default for new
/block calls after this change.

The old rule requiring every new block fixture to reach ASSESSMENT_DEPTH_V3
before comparison is retired.
