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

- **Band A — production-ready professional:** senior top-flight men/women,
  senior continental competition, or another established professional
  competition with current fixture identity and researchability verified.
  Women's domestic top flights explicitly belong here when identity is verified.
- **Band B — professional reserve-observability:** researched professional lower
  divisions / second tiers with adequate current channels.
- **Band C — low-tier caution:** regional, semi-professional, amateur, reserve,
  obscure lower-tier or otherwise weak-observability competitions.

**Band A and Band B compete in one football-first pool.** Band is operational
metadata, not a popularity or prestige ranking bonus. A Band-B fixture must not
be hidden merely because five Band-A fixtures exist. Compare A/B candidates by
the same frozen goal evidence first; use observability only as a late operational
tiebreak when the football evidence is materially tied.

Band C remains constrained. It may enter the visible reserve lane only when it
has both:

1. a materially stronger frozen goal signal than the weakest visible A/B row
   (default: at least **15 priority score points** higher); and
2. verified current researchability plus likely XI/team-news availability.

If either condition fails, keep the Band-C fixture outside the visible board
even when raw 3+/4+ rates are huge. This is an observability safeguard, not a
league-prestige prediction bonus.

Apply **HIGH_4PLUS_RESCUE** to Band-A **or Band-B** `GOAL_REVIEW` /
`RESERVE_SIGNAL` rows when all frozen sweep conditions are true:

- mean 4+ rate >= **0.55**;
- carrier route >= **1.75**;
- low-draw-trap rate <= **0.20**;
- fixture identity/researchability is verified;
- no explicit exclusion or unresolved competition-format blocker applies.

This is display/selection rescue only, never a goal certificate. Do not require
priority_score >=60 and do not convert the frozen sweep lane to GOAL_PRIORITY.

For the common A/B pool compare, in order:

1. current scoring-route strength;
2. opponent leakage / opening tendency;
3. recent comparable **4+ signal**, including HIGH_4PLUS_RESCUE status;
4. recent comparable 3+ signal;
5. game-state / incentive pressure;
6. endpoint/control risk;
7. raw composite priority score;
8. observability and XI readiness only as a late operational tiebreak.

Do not compile a protected O2.50/O3.50 certificate at /block. Do not run the
full Football C XI runtime for every candidate.

Default output is a bounded **two-lane block board with at most 10 rows**:

- **PRIMARY:** the strongest **3 to 5** credible candidates, maximum five;
- **HIGH-SIGNAL RESERVE:** fill from the remaining qualified A/B pool up to a
  maximum **10 total visible rows**. Do not pad when fewer credible rows exist.

Use explicit display states:

- `PROMOTED_FOR_XI` — PRIMARY lightweight selection;
- `HIGH_4PLUS_RESCUE` — A/B review/reserve row admitted by the 4+ rescue;
- `HIGH_SIGNAL_RESERVE` — qualified A/B candidate outside PRIMARY but retained
  visibly because its frozen goal signal remains credible;
- `HIGH_SCORE_RESEARCH_BLOCKED` — strong frozen signal but unresolved
  research/format/identity blocker; zero /xi authority until resolved.

A `HIGH_SCORE_RESEARCH_BLOCKED` row may appear in PRIMARY or reserve according
to its frozen goal signal, but the blocker stays binding. Do not silently replace
it with a weaker ready match merely to make the board all-actionable.

Every completed /block receipt must also freeze an `omission_audit` containing:

- `qualified_for_block_rank_count`;
- `primary_visible_count`;
- `high_signal_reserve_visible_count`;
- `hidden_qualified_count`;
- the strongest hidden **A/B** rows (up to 10) with match id, frozen score,
  3+, 4+, trap, promotion band and `omission_reason`.

For a qualified A/B row hidden only because the 10-row display cap was reached,
the reason must be exactly `DISPLAY_CAP_ONLY`. A qualified A/B row may not
silently disappear from the receipt.

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
