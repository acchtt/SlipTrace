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
`V4_SWEEP_READY` receipt **and its exact source automatically**. The
canonical replay artifact `v4-original-source-attested-receipts` contains
three matching files per run: `<run>-v4_sweep_ready.json`,
`<run>-source.json`, and `<run>-rank-handoff.json`. The handoff manifest
pins the source-file SHA256 and receipt integrity SHA256.

For `/rank newest receipt`, do NOT stop at "receipt found, source missing".
Resolve the source in this order without user intervention:
1. the same attestation artifact's `<run>-source.json`;
2. `models/football/stages_v4/recovery/<run>/source.json` on current main;
3. the exact GitHub source-producing ref/commit identified by the sweep
   provenance, using that same recovery path.

Verify the source bytes against the handoff manifest when present, then run
native source replay. Only when all three provenance locations are genuinely
absent may Work return `V4_SOURCE_HANDOFF_MISSING`. Do not ask the user to
attach a file that already exists in repository or workflow provenance.

If the normal-chat sweep could not run Python, it must save the original
`source.json` in
`models/football/stages_v4/recovery/<V4-run-id>/source.json` on GitHub.
This triggers `.github/workflows/football-v4-replay-attestation.yml`
on push and creates the bundled artifact above. New runs run the real V4
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

## Mandatory original-source replay and fresh status

New V4 rank execution requires the unchanged original \`source.json\` from
the genuine V4 acquisition or original GitHub Actions artifact. The rank
engine replays that source using the source receipt's original UTC epoch
and must reproduce its exact SHA256. A JSON hash is a consistency check,
not a cryptographic third-party source certificate: verify the original
provider source and CI provenance independently.

Refresh **every eligible fixture** on its original fixture URL just
before ranking. Save a \`status_refresh.json\` with
\`schema_version=football-v4-rank-status-refresh-v1\`, original \`run_id\`,
original \`sweep_integrity_sha256\`, \`checked_at_utc\`, and one \`matches[]\`
entry per eligible match containing \`match_id\`, \`source_url\`,
\`kickoff_utc\`, \`fixture_status\`, and \`observed_at_utc\`.
All status evidence must be no older than 10 minutes. A changed kickoff
requires a fresh source epoch; already-started fixtures may not be
ranked prematch. Do not invent a prematch observation.

Research real football evidence for the complete eligible fixture
universe in goal-first priority order: source-backed recent scoring,
home/away scoring routes, current team news, expected XI channels,
competition format/incentives (cups), potential 0–0/1–1 trap and
fourth-goal scoring tail. For C2, independently research current
opponent-specific defensive leakage as a model-owned factor. When a defensible
grade is available, freeze BOTH `c2_opponent_leakage` (LOW/MEDIUM/HIGH) and a
non-empty `c2_opponent_leakage_basis`; never copy C's `opponent_leakage`,
completion, continuation or stall labels. If current C2-specific leakage
evidence is unavailable, omit BOTH fields and the C2 O2.25 leakage certificate
remains unavailable rather than inventing a grade. No price quote is required to complete
football analysis; there is NO implied executable bet without real odds.
Exclude prematch-closed fixtures, never retroactively admit a match.
No random first-eight cap; insufficiently researched fixtures require
clear reasons, not invented C/C2 PASS.

Freeze full C and C2 board input from the SAME actual common evidence.
Use `python models/football/stages_v4/stage.py --output v4_rank.json rank
--sweep v4_sweep.json --source source.json --status-refresh status_refresh.json --c c.json --c2 c2.json --unranked unranked.json`.
The deterministic production model C and C2 execute independently.
Results are **awaiting Airtable persistence** until separately read back and
verified. For every newly ranked fixture write the exact executed model-row
JSON into Daily Coverage `Step1 Engine C Result` and
`Step1 Engine C2 Result`, then independently refetch those exact fields
(field IDs `fldhUWNoyXzXfQJ3C` and `fldq0n2tDlS58goAm`) together with
state/rank/line/lane. `stage.py verify` must compare each stored JSON object
to the sealed C/C2 engine result and emit
`model_evidence_readback_verified=true` plus
`model_evidence_sha256`. A missing or changed model-owned factor—including
C2 leakage evidence—is a persistence failure, not an inferred repair.
The verification receipt must also carry forward `source_replayed`,
`current_fixture_status_checked`, `original_source_sha256` and
`status_refresh_sha256`; routine /xi must receive the unchanged original
source and exact status-refresh payloads and recompute those hashes before
authorization. Store only C official lanes and keep C2 shadow; never invent
prices or website publication.
