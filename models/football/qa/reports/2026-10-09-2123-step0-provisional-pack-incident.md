# Oct 9 21:23 ICT sweep — provisional ZIP leaked to Step 01

**Affected run:** `SWEEP-20261009-2123-20261010-0300`  
**Affected board label:** `B-20261009-2123-20261010-0300`  
**Airtable Sweep Runs ID:** `reckpoPu7eJbIrxxY`  
**Source payload hash:** `fnv1a32-3aea7640`  
**Root cause:** producer-side finalization/packaging boundary, **not** a C/C2 evaluation error.

## Independently verified persisted state

- Source run remains `RUNNING / PACKAGING`, chunk 2, 66 source-discovered rows. No verified `COMPLETE` status, finalized Work ZIP filename, or frozen admission counters.
- Daily Coverage has **66 fixture-level records** keyed to this run.
- **10 Netherlands Eerste Divisie fixtures exist in Airtable** and are marked operationally C/excluded. The Sweep Runs required manifest is only a summary (`fixture_count=10`, `operational_excluded_count=10`) with **no `fixtures` array**. The text summary cannot substitute for the ten fixture objects required by Step 01.
- Eight B-grade candidate records exist (Dortmund–Bremen, PSV–Heerenveen, Lens–Lyon, Brann–Viking, Nordsjælland–OB, Galatasaray–Kasımpaşa, Moreirense–Gil Vicente, West Ham–QPR). **All eight have `Operational Disposition=UNRESOLVED`**, with no final `Step0 Capacity Queue Rank` stored. These are not yet Work-admitted.
- A provisional pack was nevertheless given to /rank with `complete=false`, `actionable_complete=false`, `work_ready=false`. Step 01 correctly refused it.
- This was an **unproven export**, not proof that fixtures are unavailable. Do not replace those booleans with true without independent finalization and match eligibility checking.

## Exact finite repair of this run, without a new global sweep

1. Read Sweep Runs `reckpoPu7eJbIrxxY` and the 66 source-epoch Daily Coverage rows again, preserving original Run ID/source hash.
2. Build the required Netherlands manifest from the **ten actual** same-run ledger rows: AiScore canonical match IDs, match names, zoned ICT kickoffs and recorded operational dispositions. Confirm against the KNVB original fixture inventory; do not omit Jong teams or fill missing IDs by guessing.
3. Finish current prematch eligibility/status and XI/Asian-total evidence for the eight B candidates, retaining their prospective grade only where still valid. Freeze admitted ranks 1–8 if and only if all eight clear. Promote their Airtable `Operational Disposition` to `ADMITTED_TO_C` and persist queue rank with read-back. If one fails, correctly exclude it and compact-re-rank the qualifying queue; do not fake eight admissions.
4. Reconcile women's/required/protected coverage, terminal interval, source dates, source hash, raw/production counts, current work readiness and any unresolved identity/time cases. Freeze `required_competition_blocks_complete` only with complete fixture records.
5. Build a new `STEP0_HANDOFF.json` carrying the exact required manifest plus an independently sourced `required_competition_source_fixture_ids` inventory. Run the canonical `--consumer export` validator, followed by the atomic `step0_package_cli.py` using *independent current Airtable read-back* as `sweep_run_proof.json`.
6. Persist ZIP hash/name and mark Sweep Runs `COMPLETE` **only after** ZIP validation. Send **only the final validated ZIP** to Step 01; /rank resumes from that exact handoff, not from the provisional pack.

Do not run C/C2 on the eight candidates before the legal handoff, and do not rewrite frozen official model verdicts. No actual bet is implied.

## Prevention

PR for this incident adds a stricter new fast-handoff required fixture list / source inventory check, a single atomic ZIP packager requiring independently fetched finalization proof, regression tests for false-complete/provisional cases, and a Step 01 repair handoff instruction. Historical COMPLETE sweeps remain unchanged.
