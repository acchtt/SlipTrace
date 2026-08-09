# Duration Market Rebuild Review — 2026-08-09

## Scope

Review the full tracked Duration sample available in Airtable before LoL v0.3.45 activation.

Known settled record: **1-5, -1.03425u**.

| Position | Result | Known final / evidence | Process finding |
|---|---|---|---|
| Over 29 minutes | Loss | 28:24 | Structure acceleration underweighted. |
| Over 34 minutes | Win | 36:57 | Observed Baron-expiry/stall evidence supported the thesis. |
| Under 31 minutes | Loss | Exact final clock unavailable | Draft-only acceleration thesis; insufficient observed duration evidence. |
| Over 32 minutes | Loss | 31:02 | Early no-tower state overweighted despite six kills by 7:45 and engage inventory. |
| Over 32 minutes | Loss | 30:43 | 0-0 kills, 0-0 towers and near-even gold were treated as separate stall signals although they were correlated quiet-state descriptors. |
| Over 33 minutes | Loss | Finished below 33 | At 16:00 KT led 5-3 and +2.1k with 0-0 towers; latent conversion and first-break cascade risk were underweighted. |

## Main findings

### 1. Quiet-state double counting

Low kills, 0-0 towers, even gold, split dragons and no Baron were repeatedly counted as multiple reasons for a long map. They are frequently correlated outcomes of one uneventful opening and do not independently forecast future structural conversion.

### 2. Nonlinear first-break risk

The model projected current pace too linearly. First tower, Herald, Baron or one successful pick can change the map regime by opening side lanes, deeper vision, objective control and serial structure access.

### 3. Betting inside timing uncertainty

Three duration losses missed by approximately 36, 58 and 77 seconds. This indicates the process was willing to bet near the center of its own plausible closing-time distribution rather than demanding separation between the market line and the model's forecast.

### 4. Draft theory overuse

Draft can identify possible stall or acceleration mechanisms but does not prove they will function on the current map. The Under 31 loss was a clear example of a draft-only duration thesis.

### 5. Observed stall was more useful than theoretical stall

The only duration win, Over 34, was supported by observed Baron-expiry and stall evidence. This is qualitatively stronger than theoretical waveclear, disengage, scaling or simply having no towers down.

### 6. Total Kills and Duration were partially conflated

Fight frequency and game length are not interchangeable. Total Kills depends on fight inventory and kill generation; Duration depends on structural conversion efficiency and clock survival after fights.

## Corrective action

LoL v0.3.45 makes Duration live-only, imposes a 12:00 minimum entry time, requires temporally persistent observed stall/acceleration evidence, collapses correlated quiet-state signals, adds a two-minute forecast dead zone, forces repricing after structural regime changes, and raises probability buffers while the market family is in rebuild mode.

Rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.45.md`.
