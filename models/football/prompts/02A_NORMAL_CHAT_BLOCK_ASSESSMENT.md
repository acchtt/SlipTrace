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

Run the whole block through the same goals-first intake logic used by /sweep.
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

Rank only `QUALIFIED_FOR_BLOCK_RANK` and, when useful, the strongest
`RESERVE_SIGNAL` rows.

Use a bounded rank-lite comparison built from the Stage-A evidence:

1. current scoring-route strength;
2. opponent leakage / opening tendency;
3. recent comparable 3+ / 4+ signal;
4. game-state / incentive pressure;
5. endpoint/control risk;
6. observability and XI readiness.

Do not compile a protected O2.50/O3.50 certificate at /block. Do not run the
full Football C XI runtime for every candidate.

Default output is a compact shortlist of **up to three promoted fixtures** plus
the remaining block dispositions. If fewer than three clear the intake floor,
promote fewer. Never fill the shortlist with weak matches just to reach a cap.

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
