# DK vs KT Game 1 — Duration Review — 2026-08-09

## Position

- Market: Game 1 duration Over 33 minutes
- Odds: 2.020
- Stake: 0.25u shadow
- Actual exposure: 0u
- Entry clock: 16:00
- Entry state: KT 5-3 DK, KT +2.1k gold, towers 0-0, dragons 1-1, no Baron/inhibitors
- Result: LOSS, -0.25u shadow

## Draft

KT: Olaf / Pantheon / Ryze / Ezreal / Nautilus  
DK: Ambessa / Vi / Taliyah / Lucian / Milio

## What the model did

The model treated 0-0 towers, split dragons and DK's theoretical Taliyah/Milio defensive tools as strong evidence that the map could extend beyond 33:00. It estimated the Over at roughly 59-66% versus a 49.5% break-even probability.

## What was wrong

### 1. Towerlessness was mistaken for stall

At 16:00, turret plates had already expired. A 0-0 tower state did not mean KT was unable to convert structures; it only meant the first break had not occurred yet.

The first structural break was highly elastic because KT had enough collapse and pick tools to turn one winning sequence into multiple towers and objective access.

### 2. Remaining survival horizon was not modeled directly

Over 33 at 16:00 required the game to survive roughly 17 more minutes. The analysis discussed whether the game looked slow but did not explicitly price the probability of surviving that full horizon.

### 3. KT's latent conversion architecture was underweighted

Pantheon + Nautilus supplied reliable first contact. Pantheon + Ryze supplied fast numbers creation and collapse. Ezreal/Ryze supplied safe follow-up pressure. Olaf reduced the reliability of conventional control as a stopping mechanism.

KT therefore had multiple independent ways to convert one successful sequence into kills, objectives and structures even before they had taken a tower.

### 4. DK's defensive tools were theoretical, not demonstrated

Taliyah waveclear and Milio protection were credited before repeated successful stall cycles had been observed. The model should have required evidence that those tools were actually preventing conversion.

### 5. Model-market divergence was unsupported

The model central estimate exceeded market break-even by more than 9 percentage points without three independent synchronized reasons, including observed stall evidence. That disagreement should have triggered shrinkage/fail-closed behavior.

## Later state

By 28:29 KT had reached approximately:

- +11k gold;
- 14-4 kills;
- 8-3 towers;
- 3-1 dragons;
- 1 Baron;
- 1 inhibitor.

The map demonstrated exactly the missing first-break/cascade branch.

## Correction

Promote LoL model to v0.3.43 with:

- remaining-survival-horizon duration math;
- structural absence = neutral, not stall;
- Latent Conversion Potential score;
- observed stall evidence requirement;
- first-break elasticity rule;
- duration market-divergence sanity gate;
- phase-aware duration probability buffers;
- high-friction Over veto when a leader has enough latent conversion and the line requires a long remaining survival horizon.

Under v0.3.43, the 16:00 Over 33 @2.020 is a PASS/HOLD.
