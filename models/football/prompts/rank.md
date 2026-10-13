# /rank — canonical V4 redirect

**ACTIVE:** Read `models/football/CURRENT_MODEL.md`, `models/football/prompts/COMMAND_ALIASES.md` and execute **only**
`models/football/stages_v4/RANK.md` with the original `V4_SWEEP_READY`
receipt and unmodified original `source.json`.

The rank runtime requires original-source replay and a full-cohort,
fresh match-specific kickoff/status observation; run the native CLI with
`--source` and `--status-refresh`. For `/rank newest receipt`, resolve
the matching source automatically before asking the user for any file:
first use the same attestation artifact's `<run>-source.json` +
`<run>-rank-handoff.json`; otherwise use
`models/football/stages_v4/recovery/<run>/source.json` from repository
provenance (including the exact source-producing ref when the handoff names
one). Only after those provenance locations are genuinely absent may the
command report `V4_SOURCE_HANDOFF_MISSING`. Never reconstruct from Airtable
Daily Coverage or from the receipt's derived ledger, and never ask the user
to rerun discovery merely because Work did not initially download the source.
Research goal-qualified fixtures first; C official and C2 shadow are independent.
Persistence remains unverified until independently refetched in active Airtable.
