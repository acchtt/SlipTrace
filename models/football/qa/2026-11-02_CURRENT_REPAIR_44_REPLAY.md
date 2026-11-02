# 2026-11-02 Current-Repair Replay — Recent 44 Matches

## Scope

Same-information replay of the exact 44 frozen Decision States fixtures used by
the earlier 2 November audit. No outcome fields, bookmaker results or post-match
facts were read by the replay engine.

- Production base: `cd2d51bcf2fa426d6af8eb9797f40502e2cd02dc`
- Audit branch: `audit/replay-44-current-repair-20261102`
- Replay harness commit: `7b9e76f24089f36d9304a5965b66666d8a297253`
- GitHub Actions run: `41403851133` — SUCCESS
- Frozen fixtures: **44**
- Historical assessment batches: **24**

## Current-core preflight

The deterministic core by itself still compiles the same qualification boundary:

- Original: **29 FOCUS / 15 WATCH**
- Current core: **29 FOCUS / 15 WATCH**
- FOCUS/WATCH state changes: **0**

So the latest repair is not a hidden threshold retune. Its effect is in the new
research-completeness/discrimination gates.

## G3_BORDERLINE_DISCRIMINATION_V2

Six historical WATCH rows are now stopped as `G3_BORDERLINE_RESEARCH_PENDING`
instead of being allowed to finalize from generic MEDIUM evidence:

| Fixture | Frozen state | FT outcome overlay | 3+ |
|---|---|---:|---|
| Alacranes de Durango–Atlético Morelia | WATCH | 3–1 | HIT |
| Monterrey–Tijuana | WATCH | 3–3 | HIT |
| Colorado Rapids–Chicago Fire | WATCH | 2–4 | HIT |
| Cheongju FC–Paju Citizens | WATCH | 1–2 | HIT |
| Persib Bandung–Isenmulang Kalteng | WATCH | 4–0 | HIT |
| Portland Timbers–Houston Dynamo | WATCH | 2–1 | HIT |

Outcome overlay was joined only after the same-information replay completed.

- 3+ among the six checkpointed borderline rows: **6/6**
- 4+ among the six: **4/6**

This is the strongest positive result of the repair: the new gate catches the
specific false-negative class the first rank-only repair could not see. It does
not auto-promote these fixtures; it forces a bounded source-backed second pass.

## G4 contract drift

Three frozen rows contain a historical `G4_RESEARCH_COMPLETE_FUNDED` declaration
that the current deterministic core no longer funds at G4:

- Manchester City–Brighton — current depth G3; FT 0–1
- Young Boys–FC Zürich — current depth G3; FT 3–5
- CF América–Toluca — current depth G3; FT 2–2

These rows are non-finalizable without evidence reconciliation. The outcome
overlay is mixed: the downgrade would have protected against Manchester City,
but Young Boys and América still reached 4+.

## BLOCK_DISCRIMINATION_V2

After removing the six borderline-pending rows and the three G4-contract-drift
rows, current block discrimination identifies:

- **9** kickoff blocks requiring equal-depth comparison
- **33** fixtures checkpointed as `BLOCK_COMPARISON_PENDING`

The frozen historical payloads predate the required `block_comparison` objects,
so none of those nine blocks can legitimately finalize under the repaired policy
without the new same-depth football comparison.

Examples include:

- Yongin–Seoul E-Land / Mito–Sanfrecce / Kashima–Cerezo / NTV Beleza W–Omiya W
- Werder Bremen–Hoffenheim / Fredrikstad–Rosenborg / Feyenoord–Fortuna
- Bayern–Dortmund / Tottenham–Crystal Palace / Heerenveen–NEC
- Necaxa W–Santos W / Yokohama F.Marinos–Kawasaki / Cerezo W–Elfen W
- Cruz Azul–León / LAFC–Minnesota

## Finalization impact

Across all three current-repair checkpoint classes:

- Unique fixtures checkpointed: **42/44**
- Finalizable from the old frozen evidence without new research: **2/44**
- The two surviving rows are Selangor–Star City and Chelsea–Manchester United.

This is intentionally fail-closed. It demonstrates that the latest repair blocks
the old compressed evidence from flowing straight into rank, but it also means a
historical same-information replay cannot honestly produce a new completed board
for 42 fixtures without performing the bounded re-research required by the new
contracts.

## Comparison with the first replay

The first repair changed only ordering:

- state changes: **0**
- rank movements: **9**
- review challengers: **0**
- changed-block #1 at 3+: **3/4**
- changed-block #1 at 4+: **2/4**

The current repair reaches the layer the first replay missed. It detects six
borderline false negatives — all six later reached 3+ — and prevents 33 nearby
candidates from being ranked without explicit same-depth block comparison.

The full settled cohort had **30/44** fixtures reach 3+.

## Conclusion

The latest repair materially addresses the diagnosed information-loss failure,
but this replay is a **checkpoint validation**, not proof that the final repaired
ranking is already better. The next valid step is to complete the bounded
selection rechecks and block comparisons using the frozen prematch source epoch,
then rerun the 44 to obtain a fully finalizable repaired board.
