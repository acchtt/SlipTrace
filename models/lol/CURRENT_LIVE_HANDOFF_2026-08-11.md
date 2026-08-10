# CURRENT LIVE HANDOFF — LoL — 2026-08-11

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.53.md`
3. retained deltas v0.3.52 through v0.3.26
4. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
5. `models/lol/reviews/AGGREGATE_ANTI_FAVORITE_FADE_BIAS_REVIEW_2026-08-11.md`
6. latest reviews referenced by `CURRENT_MODEL.md`
7. v0.3.25 baseline context/calibration files
8. connected-stack / scoreboard / stake procedures
9. This handoff last

## Active model
**LoL v0.3.53**

GitHub is model authority. Airtable is canonical map/position ledger.

## Operating state
- Official betting paused until explicit restoration.
- Shadow calibration mode active.
- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Minimum odds: 1.60.
- Same-game multiple shadow bets enabled **after live eligibility**.
- Pregame and immediate post-draft ML / Kill Handicap / Total Kills TAKEs disabled.
- Duration: no pregame TAKE; no TAKE before 12:00; existing duration gates remain.
- A wager is recorded only after explicit confirmation of the same executable line.
- User saying `Final`, `final score`, or `X won` is definitive settlement authority.

## Aggregate calibration alarm
Post-circuit-breaker settled positions through `POSTCB-SHADOW-25-P01`:

- record: **10-16**
- net: **-1.5255u**
- recent five confirmed positions: **0-5, -1.25u**
- exact visible opposite-price fade benchmark on those five: approximately **+1.16775u**

Do not blind-fade automatically. Use the fade benchmark as a calibration diagnostic.

## v0.3.53 core corrections

### Two-snapshot eligibility
Before any ML / Kill Handicap / Total Kills TAKE:
- require at least two synchronized live snapshots;
- prefer >=90 seconds separation;
- require exact executable odds;
- require observed mechanism evidence, not draft theory alone.

### MKT + TEAM anchor
Start from current market plus persistent team-strength/execution prior. Fearless Draft does not reset team execution to neutral.

### Anti-favorite guard
Underdog ML/+kills must prove live suppression of the favorite's baseline skill/conversion edge. Attractive theoretical tools are insufficient.

### Mechanism independence
Classify major mechanisms `INDEPENDENT / PARTIALLY COUPLED / COUPLED`. Shared tempo/angle/fog/economy dependencies create correlated failure and widen favorite blowout tails.

### Handicap Buffer Retention
Do not chase a heavily compressed +kills line merely because the underdog temporarily leads. If the thesis is margin survival and most buffer has disappeared, default PASS unless the favorite's wide-margin tail has demonstrably collapsed.

### Structure Substitution
Classify `MARGIN-COMPRESSING / MARGIN-EXPANDING / MIXED`. Structure dominance can force losing defenses and widen kill margins; it is not automatically protective for +kills.

### Total Kills
Retain OKP / FCI / CRR / SRR / BF / CL and add:
- RKS — Return-Kill Suppression
- KPW — Kills Per Realized Window
- structure-driven deletion of future fight windows

High contact availability does not automatically imply high final kills.

### Fade benchmark
For each confirmed shadow TAKE, record visible opposite-side price in notes when available. Benchmark only; do not create a second official shadow position.

### Change control
No ordinary single-map model promotion. Require >=5 settled positions across >=3 maps showing the same mechanism, or an aggregate review. Deterministic correctness bug is the exception.

## Latest completed series — G2 Esports vs Natus Vincere

Series result: **G2 won 2-0**.

### Game 1
G2 blue: Jayce / Xin Zhao / Viktor / Ziggs / Alistar  
NAVI red: K'Sante / Nocturne / Syndra / Ezreal / Shen

Confirmed position:
- `POSTCB-SHADOW-23-P01` NAVI +1.5 kills @1.822 — LOSS -0.25u

Final adjusted score after user scoreboard correction: **G2 14-9 NAVI**, 37:32.

Key review:
- early NAVI catch success was real;
- G2's range/skill/late-control edge persisted;
- handicap buffer was destroyed by taking +1.5 after the earlier +6.5/+7.5 protection compressed;
- NAVI +6.5 would have covered.

### Game 2
G2 blue: Galio / Trundle / Orianna / Varus / Rell  
NAVI red: Rumble / Lee Sin / Cassiopeia / Corki / Leona

Confirmed positions:
- `POSTCB-SHADOW-24-P01` NAVI +7.5 kills @1.931 — LOSS -0.25u
- `POSTCB-SHADOW-25-P01` Over 30.5 kills @1.890 — LOSS -0.25u

Final: **G2 15-7 NAVI**, 30:16, 22 total kills, G2 +9.2k, towers 11-2, dragons 2-2, Baron 1-0, inhibitors 3-0.

Key review:
- NAVI +7.5 lost by 0.5 kill;
- underdog margin resistance was slightly overstated;
- BF/SRR contact availability was badly over-converted into kill volume;
- G2 produced a low-kill structural stomp with strong return-kill suppression and rapid future-window deletion.

## Open positions
**NONE.**

## Next-session protocol
1. Pregame: analysis only.
2. Post-draft: analysis only.
3. Snapshot 1 around 5-7 minutes when available.
4. Snapshot 2 around 8-10 minutes or >=90 seconds later.
5. Only then scan ML / Kill Handicap / Total Kills for TAKE.
6. Multiple same-map shadow TAKEs allowed after eligibility if each qualifies.
7. Record visible opposite-side fade benchmark on every confirmed TAKE.
8. Reassess all open positions position-blind after material changes.
9. No loss chasing; no attempt to recover the recent drawdown in one series.

## Mandatory live response
First visible line on active maps:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Do not delay verdict for GitHub/Airtable work.
