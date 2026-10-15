# /rank — Football V4 C + C2 rank

This is the only active /rank procedure.

## Input authority

Use one native V4 rank handoff containing the matching:

- <run>-v4_sweep_ready.json
- <run>-source.json
- <run>-rank-handoff.json when supplied

The handoff artifact is v4-original-source-attested-receipts.

For /rank newest receipt, resolve that canonical bundle. Do not reconstruct a
sweep receipt from Airtable or from derived ledger rows.

If an older saved source exists only in
models/football/stages_v4/recovery/<run>/source.json, first regenerate the
canonical artifact from that source. Ranking itself does not search historical
Git refs for missing transport files.

## Mandatory original-source replay and full-cohort status

Before football research/C/C2 execution:

1. replay the unchanged original source.json through native V4;
2. require the replayed receipt to match the frozen V4_SWEEP_READY receipt;
3. independently refresh every eligible fixture's kickoff/status;
4. require the refresh to be within the V4 freshness window;
5. reject changed-kickoff/source fixtures;
6. mark already-started fixtures PREMATCH_WINDOW_CLOSED rather than ranking
   them retroactively.

A matching local JSON hash alone is not external provider authenticity; preserve
the actual provider source URLs/timestamps.

The native CLI is:

python models/football/stages_v4/stage.py --output v4_rank.json rank --sweep v4_sweep.json --source source.json --status-refresh status_refresh.json --c c.json --c2 c2.json --unranked unranked.json

## Rank cohort

Rank only the frozen V4 eligible_queue (verified GOAL_PRIORITY cohort).

Research the complete cohort in goal-first order. Do not silently skip an
earlier higher-priority fixture without an explicit allowed evidence/status
reason.

No odds quote is required for Step 1.

## Football research

Freeze one common factual epoch for both models, including:

- fixture identity/status/kickoff;
- recent scoring/allowing evidence;
- home/away scoring routes;
- carrier/chance/failure evidence;
- likely/current team news and XI channels;
- 0-0/1-1 stall/trap evidence;
- H2H only when materially transferable;
- competition format/incentives for cups/tournaments;
- fourth-goal tail evidence when a higher burden needs it;
- the frozen V4 goal-screen priority score, mean 3+ rate, mean 4+ rate and
  0-0/1-1 trap rate from the eligible_queue. These are common source facts and
  must be copied identically into C and C2 inputs.

## Ranking contract

Ranking is price-blind and deterministic. It must compare the quality of each
model's own certified scoring mechanism rather than reward a lower total.

The lexicographic order is:

1. certificate robustness: ROBUST > CONDITIONAL > FRAGILE;
2. highest funded goal certificate: G6 > G5 > G4 > G3 > none;
3. endpoint/control risk;
4. frozen V4 quantitative goal signal;
5. the model's remaining football-mechanism quality factors.

Robustness is compiled only from existing frozen football evidence: route
reliability, independent/two-route or self-funded-carrier structure, current
chance quality, failure resistance, evidence confidence, explicit
route-attacking suppression, and the frozen goal signal. Do not infer
robustness from league identity, bookmaker totals, final scores, or prose
keywords.

A high raw scoreline history alone is insufficient. A row whose current
mechanism dimensions remain broadly MEDIUM stays FRAGILE even when the frozen
3+/4+ rates are high. CONDITIONAL requires a corroborated frozen goal signal,
an independent scoring structure and at least one HIGH current football
dimension (chance quality, route reliability, evidence confidence or
independent-route quality). ROBUST additionally requires either two STRONG
independent routes or HIGH route reliability plus HIGH current chance quality,
including the equivalent HIGH-quality self-funded-carrier shape. This lets
red-card/cup-inflated histories remain low-confidence when the current frozen
mechanism grades did not independently validate the inflation. A fragile
G4/G5 does not automatically outrank a robust or conditional G3.

For C, endpoint/control comparison uses C's own effective stall grade plus the
common frozen 0-0/1-1 trap rate. For C2, endpoint/control comparison uses only
the common frozen trap evidence; C2 must not inherit C's completion,
continuation, opponent-leakage or stall labels.

The quantitative comparator uses the frozen Step-0 priority score, mean 3+
rate, mean 4+ rate and low-draw trap rate. Missing frozen quantitative evidence
ranks below complete evidence at this comparator; it does not create a blocker
or a synthetic positive score.

The research-declared supported line and the magnitude of the compiled burden
are never direct ranking bonuses. Certificate depth is the only burden-related
ranking concept.

### Availability / rotation symmetry

Availability news may downgrade a certificate only when the missing player(s)
attack an identified scoring mechanism. Record that through the existing
route-specific failure/suppression evidence and basis.

Do not convert generic attacking absences or rotation into automatic total
suppression. Recheck whether:

- alternative creators/scorers preserve the certified route;
- the opponent retains an independent scoring route;
- defensive rotation increases opponent leakage;
- mixed attacking and defensive changes offset rather than uniformly suppress.

Low XI robustness remains a later mechanism-quality comparator when the scoring
route itself is preserved. It must not erase a stronger certified mechanism by
itself.

### Supplied market disagreement is a research trigger only

Step 1 does not fetch odds. If the user has already supplied a valid,
contemporaneous screenshot/frozen quote and its total is materially above the
compiled certified burden, use the disagreement only to recheck the original
football evidence before finalizing research:

1. inspect missing scoring routes and continuation assumptions;
2. recompute G3/G4/G5/G6 from football evidence;
3. record why the discrepancy remains or why the football certificate changed.

Never search for a replacement quote, infer a missing price, pass the quote
into the ranking key, or let the market manufacture a goal certificate. If no
valid supplied quote exists, ranking completes normally.

## Supported burden compiler

Do not choose the production supported line manually.

The research payload may retain its former `supported_line` and basis only as
an audit declaration. The engine compiles the authoritative burden from frozen
goal certificates using exact Asian full-win settlement semantics:

- G3 -> O2.50 maximum fully-funded burden;
- G4 -> O3.50;
- G5 -> O4.50;
- G6 -> O5.50;
- no G3 -> no certified burden.

A .75 line requires the next certificate because landing on the adjacent
integer is only a half win: O2.75 requires G4, O3.75 requires G5, O4.75
requires G6.

G3 can be certified independently by a carrier route, a distributed 2+1/1+2
route, or matchup-specific leakage. Distributed G3 requires the frozen V4 goal
screen to corroborate the route; league identity or market totals never create
a certificate.

### C-owned inputs

Research/freeze C completion mode, burden completion, continuation, opponent
leakage and stall risk independently.

### C2-owned inputs

Research/freeze C2 route-quality policy independently.

For the active C2 O2.25 leakage calibration, when current opponent-specific
leakage evidence is defensible, supply BOTH:

- c2_opponent_leakage
- c2_opponent_leakage_basis

Never copy C's opponent_leakage, completion, continuation or stall labels.
If the C2-specific evidence is unavailable, omit both and let the certificate
fail closed.

## Execute boards

Run the deterministic paired C/C2 board engine once.

- C = official.
- C2 = shadow only.
- shared facts do not mean shared policy.
- no price or Website Pick is created at /rank.

Every unranked eligible fixture must have an explicit allowed reason rather
than an invented C/C2 PASS.

## Persist once, read back once

Write the ranked cohort to the active Daily Coverage Ledger.

For every ranked fixture persist:

- C state/rank/deterministically compiled supported burden;
- C official FOLLOW/RESERVE/STOP lane;
- C2 state/rank/deterministically compiled supported burden;
- the research-declared line/basis only as audit comparison fields;
- exact Step1 Engine C Result JSON;
- exact Step1 Engine C2 Result JSON.

Then independently refetch once and run:

python models/football/stages_v4/stage.py verify --rank v4_rank.json --readback readback.json

A valid result is V4_RANK_PERSISTENCE_VERIFIED and includes:

- ranked count;
- C2 shadow-only authority;
- source_replayed=true;
- current_fixture_status_checked=true;
- original_source_sha256;
- status_refresh_sha256;
- model_evidence_readback_verified=true;
- model_evidence_sha256.

That verified rank+persistence chain is sufficient routine /xi provenance.
Step 2 does not replay source.json/status_refresh.json again.

## Output

Report:

- run ID;
- ranked count;
- unranked reasons;
- C official board;
- C2 shadow board;
- FOLLOW/RESERVE/STOP;
- supported lines;
- persistence verification status/hash.

Never invent prices, lineups, rankings or bets.
