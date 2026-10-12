# /rank — Football V4 independent C and C2 board

This is the only current /rank launcher. Do not load old V1–V3 Work
launchers or resurrect their halted CLI.

## Critical: cross-chat receipt handoff — current /rank authority

**Do not reconstruct a V4 sweep JSON from Airtable Daily Coverage.** A
self-consistent `V4_SWEEP_DERIVED_UNATTESTED` hash is NOT sufficient.
The V4 rank function will reject it immediately with
`V4_ATTESTATION_REQUIRED`. Do NOT edit the status string or
SHA256 to fabricate an official completion. This is NOT a request
for another discovery sweep.

Work chat must retrieve the original **source-attested**
`V4_SWEEP_READY` receipt. If the normal-chat sweep could not run
Python, it must first save the original `source.json` in
`models/football/stages_v4/recovery/<V4-run-id>/source.json` on GitHub.
This triggers `.github/workflows/football-v4-replay-attestation.yml`
on push and creates a downloadable **GitHub Actions artifact** named
`v4-original-source-attested-receipts`. New runs run the real V4
sweep algorithm with the actual runner UTC clock. Old derived snapshots
are replayed through the SAME real stage at their original checked UTC
instant and compared field-for-field against the original derived
document, rather than trusting its self-hash.

**Recovery of `V4-20261012-003037-0600`:** the real-engine replay
succeeded on GitHub Actions run `38163249319`.
Download the artifact from
`https://github.com/acchtt/SlipTrace/actions/runs/38163249319`.
Use ONLY `V4-20261012-003037-0600-v4_sweep_ready.json` with
`integrity_sha256=9a8a64afc2bd512fa14f6ab65ec921f7a6f49d911d2ac600ced68837c8c2467e`.
The file attests the 00:36 ICT source snapshot: 12 raw, 5 eligible,
2 researchability pending and 5 excluded. It does NOT attest whether
a match remains prematch at the current Work execution time.

Work must independently refresh match-specific actual kickoff/status
**before researching C/C2**. Any fixture already started is
`PREMATCH_WINDOW_CLOSED` in unranked reasons, not a retrospective
board. Source/frozen match IDs, original kickoff and now-current prematch
status must agree. Verify which of the originally five are still
ahead of kickoff; do not silently add the five excluded Brazil fixtures
or promote the two pending conditional leagues without real evidence.

If no verified artifact can be retrieved from GitHub, return an
immediate `V4_ATTESTATION_REQUIRED` blocker with the run ID and
artifact link. Do not spend 8 minutes refetching 12 Airtable rows
and reproducing the same invalid `V4_SWEEP_READY` error.

## Goals-first rank intake authority

**Do not rank a V4 snapshot merely because it contains registered leagues.**
The current `eligible_queue` is the immutable goal-qualified shortlist:
`GOAL_PRIORITY` from actual recent team scoring evidence for ALL leagues,
including registered and unregistered. Read `goal_selection_policy` and
`goal_screen_manifest.priority_profile=GOAL_SIGNAL_FIRST_V1`. The full
`goal_research_queue` contains legitimate fixtures whose recent scoring
or league channel data still needs research. These are NOT C PASS.

When Work receives a V4 receipt with few/no goal-qualified fixtures but a
nonempty `goal_research_queue`, research recent finished scorelines for the
promising pending fixtures (goal signal first, not alphabetical league order).
Create a **new** currently observed provider source snapshot with the same
verified fixture identities, kickoffs, scores and fresh statuses, then run
native V4 sweep for that new source epoch to obtain its own genuine
`V4_SWEEP_READY` receipt. This is targeted evidence enrichment, not a
worldwide discovery restart and never a change to the old receipt.
If source evidence cannot be confirmed before KO, leave pending and report
it explicitly. Do not promote missing form by league reputation or
fabricated rates. Evaluate genuine C official and C2 shadow only on the
new verified `eligible_queue`, independent Airtable readback as before.

Read `README.md`, the official C and independent C2 engine
specifications and the latest source receipt from V4 /sweep.
Research all DISCOVERY-qualified fixtures together with registered A/B fixtures. The `discovery_watchlist` identifies unregistered official competitions with source-backed goal signals but missing current researchability, recent team scoring evidence, or required cup-format proof. They are **not** model PASS and must not silently vanish. Do not add pending discovery fixtures to the official model cohort until a NEW original-source V4 sweep verifies their qualifying evidence; never edit a sealed receipt. Source scoring heuristics only decide eligibility for research, not guaranteed 3+/4+ goals or a bet.

Research real football evidence for the complete eligible fixture
universe in goal-first priority order: source-backed recent scoring,
home/away scoring routes, current team news, expected XI channels,
competition format/incentives (cups), potential 0–0/1–1 trap and
fourth-goal scoring tail. No price quote is required to complete
football analysis; there is NO implied executable bet without real odds.
Exclude prematch-closed fixtures, never retroactively admit a match.
No random first-eight cap; insufficiently researched fixtures require
clear reasons, not invented C/C2 PASS.

Freeze full C and C2 board input from the SAME actual common evidence.
Use `python models/football/stages_v4/stage.py --output v4_rank.json rank
--sweep v4_sweep.json --c c.json --c2 c2.json --unranked unranked.json`.
The deterministic production model C and C2 execute independently.
Results are **awaiting Airtable persistence** until separately
read back and verified. Store only C official lanes and keep C2
shadow; never invent bets, prices or website publication.
