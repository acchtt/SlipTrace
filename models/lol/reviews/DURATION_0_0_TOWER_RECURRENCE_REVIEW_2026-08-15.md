# Duration 0-0 Tower Recurrence Review — 2026-08-15

## Scope

Review the recurring Duration error in which **0-0 towers / no first tower** was repeatedly treated as positive stall evidence for an Over.

This is a recurrence of the failure already identified in the 2026-08-09 Duration Market Rebuild Review, not a new isolated map error.

Reference prior review:
`models/lol/reviews/DURATION_MARKET_REBUILD_REVIEW_2026-08-09.md`

## Audit sample

Airtable positions where **0-0 towers was explicitly part of the entry-state Duration thesis** produced the following settled sample:

- 8 positions
- Record: **3-5**
- Net: **-0.47575u**

Examples include:

| Position | Entry state / thesis | Result |
|---|---|---|
| CB-05-P01 — Over 32 @1.868 | 7:45, 3-3 kills, 0-0 towers; “no structural conversion” | LOSS |
| CB-08-P01 — Over 32 @1.803 | 12:31, 0-0 kills, 0-0 towers; quiet descriptors treated as stall | LOSS |
| POSTCB-SHADOW-08-P01 — Over 33 @2.020 | 16:00, KT 5-3, +2.1k, 0-0 towers | LOSS |
| POSTCB-SHADOW-26-P01 — Over 32 @1.643 | 16:38, 2-2 kills, 0-0 towers, KRX 2-0 dragons | WIN |
| POSTCB-SHADOW-27-P01 — Over 33 @2.612 | 12:39, 1-1 kills, 0-0 towers, NS 2-0 dragons | WIN |
| LCK-2026-08-13-HLE-GEN-G1-P01 — Over 33 @1.842 | 15:48, 7 kills, 0-0 towers, lead compression + repeated stall | WIN |
| LPL-2026-08-13-BLG-TT-G1-P01 — Over 32 @1.888 | 11:17, 3 kills, 0-0 towers; slow conversion certified | LOSS |
| LEC-2026-08-15-VIT-GX-G3-P01 — Over 32 @1.675 | 17:53, 8 kills, 0-0 towers, VIT 3-0 dragons while GX led kills/economy | LOSS |

The mixed results matter: **0-0 towers is not useless information, but it is not directional evidence by itself.** The wins had additional actual stall mechanisms. The losses repeatedly promoted “nothing has fallen yet” into “future conversion will remain slow.”

## VIT vs GIANTX Game 3 recurrence

Entry at 17:53:

- VIT 3-5 GX kills;
- GX approximately +2.2k economy;
- towers 0-0;
- VIT dragons 3-0;
- Over 32 minutes @1.675;
- shadow stake 0.25u; actual 0u.

The model described the state as strong stall/dead-zone evidence because no towers had fallen.

Final at 27:21:

- VIT 14-6 GX;
- VIT approximately +8.5k;
- towers 8-3;
- dragons 4-0;
- Baron 1-0;
- inhibitor 1-0.

Over 32 lost by 4:39.

### Process error

The state had **absent conversion**, not demonstrated **failed conversion**.

No tower had fallen, but the map already contained a compressed high-leverage objective schedule: VIT was 3-0 dragons and the next dragon represented Soul pressure. GX also had a draft/state that could lose multiple structures after one failed compulsory fight.

The 0-0 tower count was a **lagging event count**. It did not measure the probability that the next successful fight would cascade through first tower, vision, further structures and base access.

## Root cause

The model kept conflating:

- **No structure has fallen yet**

with:

- **Teams have repeatedly tried and failed to convert tempo into structures.**

Only the second is genuine observed stall evidence.

The v0.3.45 rule already warned against correlated quiet-state counting, but live execution still allowed “0-0 towers” and “no structural conversion” language to function as an implicit positive Over signal.

## Corrective principle

**Tower count is a state descriptor, not a conversion-efficiency measurement.**

For Duration:

- `0-0 towers` is neutral by default;
- absent conversion is neutral;
- failed conversion can support Over only when a meaningful opportunity existed and was actually denied;
- pre-break cascade risk must be priced before the first tower falls;
- 3-0 dragon / Soul pressure can compress the next compulsory fight window and increase nonlinear conversion hazard even while towers remain 0-0.

## Authorized action

The user explicitly authorized a narrow model revision on 2026-08-15.

Promote **LoL v0.3.59** with a Duration-only correction:

1. neutralize 0-0 tower count as standalone Over evidence;
2. distinguish absent conversion from observed failed conversion;
3. add mandatory Latent Conversion Hazard assessment before Duration Over;
4. add a pre-first-tower cascade check;
5. preserve v0.3.45 observed-stall/acceleration requirements and all v0.3.58 non-Duration rules.

No historical P/L is changed.
