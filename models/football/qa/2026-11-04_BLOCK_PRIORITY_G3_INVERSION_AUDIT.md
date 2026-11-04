# Football C — Block Priority / G3 Inversion Audit

Date: 2026-11-04 ICT  
Status: DISCOVERY AUDIT — not promotion evidence  
Scope: current Football C block selection + G3 execution interaction  
Model of record: Football C only

## Trigger

Repeated user-observed inversion across recent blocks:

- Buriram United–Kashima Antlers: DIRECT /xi ACT O2.5 @ 1.72, FRAGILE DISTRIBUTED G3; user reported 0-0 FT.
- AFC Women block: Nasaf W–Beijing W ranked #1 with funded DISTRIBUTED G3 while East Bengal W–Hwacheon KSPO W ranked #2 with no G3; user later reported KSPO 3-1 while Beijing was 1-1.
- 22:30–23:00 block: Al Rayyan–Al Nahda, Al Wahda–Khaldiya and Rennes–Olympiacos all ranked above Kuwait–Nasaf; user reported all three 0-0 HT while Kuwait–Nasaf was 2-0 HT. HT states are warning evidence only, not settlement evidence.
- Prior Nov 2 pair: Al Sadd–Al Ahli persisted FOCUS / funded DISTRIBUTED G3 and later finished 0-0; Al Wasl persisted WATCH / no G3 and later finished 4-3.

These are discovery cases. They cannot validate a repair.

## Finding 1 — BLOCK_PRIORITY_V1 is circularly gated by the G3 certificate

`block_priority._hard_viability()` assigns:

- tier 3 when `goal3_funded == true` and compiled board is FOCUS;
- tier 2 to structurally viable rows without funded G3.

The priority key is lexicographic and begins with this tier. Therefore any tier-3 funded G3 row beats every tier-2 no-G3 row before activation, leakage, continuation, upper tail, endpoint resistance, chance quality, completion, goal signal, clearability, robustness, depth or mechanism are considered.

This is a selection lock, not a mild preference.

Concrete examples:

### AFC Women
Nasaf W–Beijing:
- hard viability tier 3
- G3 funded DISTRIBUTED
- activation HIGH
- FOCUS

East Bengal W–Hwacheon:
- hard viability tier 2
- G3 not funded
- WATCH

Once those first tuple fields differ, Hwacheon cannot outrank Beijing regardless of later football evidence.

### Kuwait–Nasaf
Kuwait:
- carrier STRONG
- chance HIGH
- goal signal over-2 rate 0.80
- goal signal over-3 rate 0.60
- priority score 62
- but G3 not funded, so hard viability tier 2

All three selected matches were tier 3 because they had funded G3. Kuwait was mathematically locked to the lower lane before its carrier force and goal signal could matter.

This conflicts with the block-comparison design statement that a one-sided carrier may outrank a balanced two-route match when its scoring path is stronger.

## Finding 2 — current-structure verification can bypass the quantitative G3 signal

`c_distributed_goal3_funded()` accepts either:

1. `goal_signal_supports_distributed_goal3()`; OR
2. `c_verified_current_structure_goal3()`.

The verified-current-structure branch requires only:

- `g3_current_structure_verified == true`;
- one STRONG route;
- the reply route at least USABLE;
- carrier at least USABLE.

After that, the remaining execution axes may all be MEDIUM.

This means the bounded-research repair can convert a qualitative STRONG + USABLE + MEDIUM profile into a fully funded G3 even when the frozen rate signal itself is weak.

### Buriram–Kashima
The deterministic result was:
- DISTRIBUTED G3
- FRAGILE
- home USABLE / away STRONG
- carrier USABLE
- route reliability MEDIUM
- chance MEDIUM
- completion MEDIUM
- continuation MEDIUM
- stall MEDIUM
- failure resistance MEDIUM
- current structure verified
- ACT O2.5 @ 1.72

The certificate was therefore created from a broad-MEDIUM profile because the current-structure flag bypassed the ordinary goal-signal requirement.

### Rennes–Olympiacos
Pre-XI block signal:
- goal-signal over-3 rate 0.17
- over-2 rate 0.50
- comparable context SUPPRESSIVE
- yet current structure verified allowed DISTRIBUTED G3 and FOCUS.

After confirmed XI, Football C still produced FRAGILE DISTRIBUTED G3 and ACT O2.5 @ 1.75.

## Finding 3 — FRAGILE G3 still has direct ACT authority at O2.5

`c_goal3_execution_floor_authorized()` explicitly preserves direct O2.5 authority for funded G3 even when robustness is FRAGILE, provided endpoint pressure is not HIGH and the ordinary axes are at least MEDIUM.

The code comment explains why this was added:

> a prior replay showed a blanket veto removed 18 ACT-capable fixtures, 14 of which later cleared O2.50.

That repair was designed to recover false negatives. It now creates the opposite failure mode: a qualitative or broad-MEDIUM G3 can be both FOCUS and directly executable at O2.5.

Buriram–Kashima is the clearest settled example.

## Finding 4 — multiple MEDIUM warnings never compound into a G3 hard stop

`c_g3_endpoint_control_pressure()` reserves HIGH for:

- HIGH effective stall;
- a high low-draw trap rate;
- or VERIFIED + corroborated suppressive H2H.

The function explicitly says ordinary MEDIUM completion, continuation, stall and failure grades are merely cautions “regardless of how many coexist.”

Therefore a row can simultaneously have:
- continuation MEDIUM,
- stall MEDIUM,
- completion MEDIUM,
- failure resistance MEDIUM,
- route reliability MEDIUM,

and still remain only MODERATE endpoint pressure.

That is exactly the profile seen in Buriram–Kashima and, substantially, Rennes–Olympiacos.

The model currently has no accumulation rule for several independent medium-risk failure channels.

## Finding 5 — one suppressive exact H2H can hard-veto a high-force carrier

The same endpoint function sets HIGH control pressure when:

- `h2h_effect == SUPPRESSIVE`;
- `h2h_transferability == VERIFIED`;
- `h2h_current_corroboration == VERIFIED`.

There is no minimum H2H sample count in this hard-control condition.

Kuwait–Nasaf was therefore suppressed by the single exact reverse 1-0 despite:
- Kuwait carrier STRONG;
- chance HIGH;
- current goal-signal over-2 rate 0.80;
- current goal-signal over-3 rate 0.60;
- priority score 62;
- very high recent scoring ceiling.

This is an overcorrection in the opposite direction from Finding 2: a single direct low-total comparable can erase strong current carrier evidence.

User-reported 2-0 HT is not final settlement evidence, but it is exactly the prospective failure mode expected from this veto.

## Finding 6 — raw carrier force is not a primary BLOCK_PRIORITY_V1 dimension

The active block key orders:

1. hard viability / G3;
2. activation;
3. leakage;
4. continuation;
5. tail;
6. endpoint;
7. chance;
8. completion;
9. goal signal;
10. clearability;
11. robustness/depth;
12. mechanism.

Raw carrier strength and carrier self-funding are not explicit early dimensions. They only influence the result indirectly through the G3 compiler or a late mechanism classification.

Consequently:

- a no-G3 STRONG carrier cannot rescue itself in block order;
- a funded distributed G3 can outrank a stronger one-sided scoring force;
- exact-match suppression can zero out the certificate before carrier evidence reaches the comparator.

This is the structural reason the user keeps seeing “we selected the neat match, while the raw carrier match scored.”

## Finding 7 — FOCUS is mechanically downstream of G3, so it cannot independently correct G3 mistakes

`compile_c_board_state()` sets every funded G3 to FOCUS.

Then BLOCK_PRIORITY uses FOCUS + funded G3 to create hard viability tier 3.

The chain is therefore circular:

`G3 funded -> FOCUS -> priority tier 3 -> outranks no-G3 rows`

The block layer was intended to provide independent discrimination, but under the current implementation it cannot meaningfully challenge a mistaken G3 certificate.

## Tournament incentive is not the root cause in these cases

Recent audited rows generally resolved tournament incentive as MIXED rather than EXPANSIVE. The current failures are therefore not primarily caused by an incentive boost.

The larger defects are:
- G3 certificate admission;
- hard block-priority tiering;
- lack of cumulative medium-risk penalty;
- single-H2H hard suppression;
- insufficient independent carrier rescue.

## Root-cause summary

The repeated inversion is produced by two opposite overcorrections that now coexist:

### False-positive lane
Previous false-negative repairs made the model permissive toward:
- verified current STRONG + USABLE route structure;
- broad MEDIUM completion/continuation/stall profiles;
- FRAGILE G3 direct O2.5 execution.

This creates FOCUS/ACT on structurally neat but weakly protected matches.

### False-negative lane
The model simultaneously remains aggressive at suppressing:
- one-sided carrier matches;
- rows with one verified suppressive H2H;
- no-G3 rows before raw carrier/goal-signal evidence can influence block order.

This removes explosive matches from focus.

The two lanes together create the observed selection inversion.

## Immediate safety recommendation — quarantine only

Because discovery is not validation, do not permanently retune thresholds from these matches.

A risk-tightening quarantine is permissible under the QA policy:

1. **FRAGILE DISTRIBUTED quarantine**
   - A FRAGILE DISTRIBUTED G3 with G4 unfunded should not create direct ACT at O2.5 when at least three of completion, continuation, stall, failure resistance and route reliability are only MEDIUM.
   - Keep football assessment visible, but exposure = zero / REVIEW until prospective validation.

2. **Current-structure bypass quarantine**
   - `g3_current_structure_verified` alone should not bypass the frozen goal-signal path for direct exposure when no genuinely HIGH predictive dimension exists.
   - This is tightening only.

These would have blocked the Buriram direct ACT and the Rennes direct ACT without creating any new exposure.

## Shadow challengers — do not promote yet

### Challenger A — BLOCK_PRIORITY_V2 carrier-rescue
Remove “funded G3 vs no G3” as the first absolute ordering split.

Use a common structural viability tier first, then compare:
- activation;
- raw carrier/self-funding force;
- current chance quality;
- goal signal;
- continuation/completion;
- endpoint risk;
- then certificate/accessibility.

A no-G3 row may rise in shadow ranking but may not create exposure unless Football C separately certifies a burden.

### Challenger B — single-H2H suppression cap
A single suppressive exact H2H cannot by itself produce HIGH endpoint control.

Require either:
- at least two transferable direct meetings; or
- one direct meeting plus independent current suppressive corroboration from the present competition/current structures.

This would be tested in shadow because it can expand the candidate set.

### Challenger C — cumulative medium-risk control
Add a prospective risk accumulator for funded G3:
- continuation MEDIUM;
- completion MEDIUM;
- stall MEDIUM;
- failure resistance MEDIUM;
- route reliability MEDIUM;
- reply only USABLE;
- no carrier self-fund.

Several simultaneous cautions should be able to downgrade exposure even when no single axis is HIGH risk.

## Governance result

**Current model diagnosis: CONFIRMED ARCHITECTURAL SELECTION INVERSION RISK.**

This is a discovery diagnosis, not proof of any repair.

**Permanent repair status: NOT YET PROMOTABLE.**

Recommended governance:
- ship the FRAGILE DISTRIBUTED / broad-MEDIUM exposure quarantine as a safety tightening if immediate protection is desired;
- run BLOCK_PRIORITY_V2 carrier-rescue and H2H-cap logic in shadow;
- use all current inversion matches as discovery-only and exclude them from prospective promotion statistics.

## Exact next action

1. Freeze a prospective challenger contract.
2. Apply only the safety quarantine to official exposure.
3. Run champion vs:
   - V2 carrier-rescue block order;
   - single-H2H cap;
   - cumulative-medium control
   on identical future blocks.
4. Require at least 40 eligible decisions / 20 settled exposure differences before any provisional performance claim.
