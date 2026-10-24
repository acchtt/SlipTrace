# Football C prospective calibration ledger

**Status:** active, zero selection authority
**Schema:** `football-c-calibration-v1`

Every source-visible prematch fixture receives one record at sweep time. Rank
enriches the same match/epoch identity with compiled state, declared-state
audit metadata, rank/lane, certificates, burden, robustness, split G3/tail
pressure, and direct ACT ceiling. `/xi` adds the exact visible screenshot
ladder, selected evaluated line/price, and ACT/BOOK/PASS decision.

At decision time, final score, goal outcomes, and settlement fields are absent.
After settlement, `calibration_ledger.settle()` appends an immutable settlement
object containing FT score, total goals, G3/G4 reach, certified-burden
settlement, evaluated-line settlement, and ACT settlement where applicable.

The record has `selection_authority=ZERO` and
`automatic_threshold_learning=false`. Production selection code does not read
settlement fields. Exceptions remain separately enumerable through
`exception_flag` but remain inside the universal denominator.

`audit_metrics()` returns the required execution, PASS, screening, ranking,
distribution, and exception metrics. It does not tune or promote thresholds.
