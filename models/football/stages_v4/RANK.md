# /rank — Football V4 single-C rank

This is the only active /rank procedure.

## Input authority

Use one native V4 rank handoff from the
`v4-original-source-attested-receipts` artifact family containing the matching:

- <run>-v4_sweep_ready.json
- <run>-source.json
- <run>-rank-handoff.json when supplied

For /rank newest receipt, resolve that canonical bundle. Do not reconstruct a
sweep receipt from Google Sheets, historical Airtable, or derived ledger rows. The resolver does not search historical
runs to substitute a different source bundle.

## Mandatory original-source replay and full-cohort status

Before Football C execution:

1. replay unchanged source.json through native V4;
2. require the replayed receipt to match V4_SWEEP_READY;
3. refresh every eligible fixture's kickoff/status;
4. require freshness within the V4 bound;
5. reject changed-kickoff/source fixtures;
6. mark already-started fixtures PREMATCH_WINDOW_CLOSED.

The native CLI is:

python models/football/stages_v4/stage.py --output v4_rank.json rank --sweep v4_sweep.json --source source.json --status-refresh status_refresh.json --c c.json --unranked unranked.json

## Rank cohort

Rank only the frozen V4 eligible_queue. Research the complete cohort in
goals-first order. Do not silently skip a higher-priority fixture without an
explicit allowed evidence/status reason.

No odds quote is required at Step 1.

## Football C research

Freeze current factual football evidence including:

- fixture identity/status/kickoff;
- scoring/allowing evidence;
- home/away routes;
- carrier/chance/failure evidence;
- current team/XI information where available;
- endpoint/control risk;
- H2H only when materially transferable;
- tournament format/incentive where applicable;
- fourth/fifth/sixth-goal evidence where higher burden needs it;
- upper-tail transferability grade + basis whenever independent_upper_tail=true;
- frozen V4 priority, mean 3+, mean 4+, and low-draw trap.

C additionally owns completion mode, burden completion, continuation,
opponent leakage and stall risk.

## Ranking contract

Ranking is price-blind and deterministic.

Comparison order:

1. certificate robustness: ROBUST > CONDITIONAL > FRAGILE;
2. highest funded certificate: G6 > G5 > G4 > G3 > none;
3. endpoint/control risk;
4. frozen V4 quantitative goal signal;
5. remaining C football-mechanism quality.

A high raw scoreline history alone is insufficient. Red-card/cup/opponent-level
inflation must not be hidden inside otherwise-HIGH route grades. When C asserts
an independent upper tail, it must freeze:

- upper_tail_transferability = LOW / MEDIUM / HIGH;
- upper_tail_transferability_basis = a prospective explanation of why the
  goal-four-plus evidence does or does not transfer to this matchup.

LOW blocks G4/G5/G6. MEDIUM may fund G4+ when the other deterministic
requirements clear, but the certificate cannot be ROBUST. HIGH preserves the
normal robustness path. The market and the eventual score cannot set this field.

### Comparable-context precedence

Whenever an independent G4+ tail is asserted, also freeze:

- upper_tail_comparable_context_signal = SUPPORTIVE / MIXED / SUPPRESSIVE / UNAVAILABLE;
- upper_tail_comparable_context_basis.

Use the closest available senior context first: same competition/continental
competition, then closely comparable opponent/competition strength, then less
comparable domestic/cup history.

Deterministic precedence:

- SUPPRESSIVE -> effective transferability LOW; G4/G5/G6 blocked;
- MIXED -> effective transferability capped at MEDIUM;
- SUPPORTIVE -> preserve the frozen transferability grade;
- UNAVAILABLE -> preserve a grade only when another current comparable
  mechanism independently supports it. Domestic/cup raw scoring alone cannot
  create HIGH.

Therefore a domestic scoring explosion cannot upgrade a contradictory
continental/same-competition upper-tail sample.

The magnitude of compiled burden is not itself a rank bonus or penalty.

## Availability symmetry

Availability downgrades a certificate only when it attacks an identified
scoring route. Check replacement creators/scorers, opponent scoring routes,
defensive rotation and mixed effects before lowering the total thesis.

## Supplied market disagreement

Step 1 does not fetch odds. A user-supplied contemporaneous market line may
trigger one football-evidence recheck when materially above C's burden, but
the market never enters the ranking key and never manufactures a certificate.

## Supported burden compiler

Production burden is compiled from Football C goal certificates. G4+ also
requires prospectively transferable upper-tail evidence:

- G3 -> O2.50
- G4 -> O3.50
- G5 -> O4.50
- G6 -> O5.50
- no G3 -> none

Asian .75 lines require the next certificate for a full win.

Research-declared supported_line remains audit metadata only.

## Execute board

Run the deterministic Football C board once.

- C is official.
- C2/C3/C4 are retired.
- no price or Website Pick is created by /rank.
- every unranked eligible fixture requires an explicit allowed reason.

## Persist once, read back once

For each ranked fixture persist:

- C state/rank/compiled supported burden;
- C FOLLOW/RESERVE/STOP lane;
- exact Step1 Engine C Result JSON;
- declared line/basis only as audit comparison fields.

Retired C2 fields may remain on historical Airtable rows, but all new rank persistence and independent readback use the Google Sheets `Daily Coverage Ledger` tab.

Then independently refetch once and run:

python models/football/stages_v4/stage.py verify --rank v4_rank.json --readback readback.json

A valid receipt is V4_RANK_PERSISTENCE_VERIFIED with exact C evidence hash,
source replay and current-status verification.

Routine /xi consumes that verified receipt and does not replay
source.json/status_refresh.json again.

## Output

Report run ID, ranked count, explicit unranked reasons, C board,
FOLLOW/RESERVE/STOP, supported burdens and persistence verification.

Never invent prices, lineups, rankings or bets.
