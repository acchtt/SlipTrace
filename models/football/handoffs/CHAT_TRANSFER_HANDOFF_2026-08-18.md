# Football Cross-Chat Handoff — 2026-08-18

## Status

- Active model: **Football v0.2.47 — AUDIT MODE**.
- Official football betting remains **PAUSED**.
- Execution remains **SHADOW CALIBRATION ONLY**.
- Ledger writes remain **ON HOLD** until explicit user approval.
- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Normal current audit shadow convention = 0.125u unless a newer explicit instruction supersedes it.
- Directional AH/DNB/ML remains quarantined from official promotion.

## Mandatory active controls

1. Exact score/minute/line/odds synchronization.
2. Full reset after material events.
3. At least two genuinely independent primary forward-looking channels for live candidates.
4. Raw shots/SOT cannot independently satisfy the primary-evidence minimum.
5. Raw SOT is not `Shot Quality/Locations` without location/chance-structure context.
6. One event cluster cannot be relabeled into two independent channels.
7. `Tempo/Persistence` requires comparable score-stable snapshots or a clearly repeated event sequence.
8. xG/xGOT are secondary only.
9. Best-expression / protected-line comparison remains mandatory.
10. For high live totals, evidence strength must match the exact full-win goal burden.
11. For live Unders, conservation/motivation is context only; require affirmative current evidence of actual deceleration or threat suppression.
12. After 3+ HT goals, apply v0.2.47 halftime compression/saturation. First-half openness cannot count as fresh post-HT promotion evidence.

## Latest process reviews

- `models/football/reviews/FOOTBALL_PROCESS_REVIEW_SETTLEMENT_LESSONS_2026-08-18.md`
- `models/football/reviews/FOOTBALL_PROCESS_REVIEW_NOMME_KALJU_EARLY_SOT_EFFICIENCY_2026-08-18.md`
- `models/football/reviews/FOOTBALL_PROCESS_REVIEW_RACING_VILLARREAL_HT_COMPRESSION_2026-08-16.md`

## Recently settled shadow decisions / lessons

### FC Copenhagen vs Debreceni

- Shadow: Under 4 @1.77 at 67:26, score 2-1.
- User-confirmed / recorded FT: **5-1**.
- Settlement: **LOSS**, -0.125u.
- Lesson: aggregate safety and lack of need for goals cannot substitute for evidence of actual attacking deceleration.

### San Diego FC vs Puebla

- Shadow: Over 2.75 @1.85 at 66:31, score 1-1.
- User-confirmed FT: **3-2**.
- Settlement: **FULL WIN**, +0.10625u at 0.125u.
- Lesson: repeated two-sided threat across comparable windows is stronger than isolated efficiency.

### IF Gnistan vs Ilves

- Shadow: Over 3.75 @1.83 at 33:06, score 1-1.
- HT: 2-2.
- User-confirmed FT: **3-2**.
- Settlement: **FULL WIN**, +0.10375u at 0.125u.
- Lesson: the first-half Over was valid, but only one goal arrived after a 2-2 HT. This is supportive evidence for v0.2.47's hard second-half reset; do not chase a new post-HT Over from first-half openness.

### Nõmme United U21 vs Nõmme Kalju U21

- Shadow: Over 4 @1.83 at 10:37, score 0-0.
- User-confirmed FT: **2-0**.
- Outcome: Loss, -0.125u.
- Process validity: **Invalid**.
- Reason: raw SOT cluster double-counted as shot quality + persistence; no independent structural/chance-quality channel; one cumulative early snapshot did not prove persistence.
- Invalid sample stays visible but is excluded from valid edge estimation.

### Austin FC vs FC Dallas

- Shadow: Over 2.25 @1.84 at 17:00, score 0-0.
- FT: 1-2.
- Settlement: **FULL WIN**, +0.105u at 0.125u.

### Vasco da Gama vs Santos

- Shadow: Over 2.25 @1.80 prematch.
- User-confirmed FT: 0-3.
- Settlement: **FULL WIN**, +0.100u at 0.125u.

### Racing Santander vs Villarreal

- Historical v0.2.46 shadow: Over 5.25 @1.88 at 55:51, score 2-2.
- FT: 2-2.
- Settlement: **LOSS**.
- Under v0.2.47 the same state would remain HOLD because second-half conversion quality did not support the two-goal full-win budget.

## Circuit-breaker state

Current v0.2.47 circuit-breaker records include:

- Slot 1 Austin–Dallas: **Won**.
- Slot 2 Gnistan–Ilves: **Won**, process valid.
- Slot 3 Nõmme–Kalju: **Loss, process invalid**; treat as excluded from valid edge evaluation and replace with the next valid counted shadow when operating the audit sequence.

Do not infer that 2-0 valid slots means official betting can resume. Audit exit criteria remain unmet and explicit user approval is still required.

## Tomorrow continuation

User said: **"we continue tomorrow"** on 2026-08-18 ICT.

When the user returns:

1. load `models/football/CURRENT_MODEL.md`;
2. load this handoff;
3. keep Football v0.2.47 — AUDIT MODE;
4. do not bump the version merely because of the newly settled examples;
5. enforce evidence deduplication, persistence proof, Under deceleration proof and HT compression literally;
6. search for / assess the next suitable football match only when requested, prioritizing matches with adequate live-stat depth;
7. keep replies compact and verdict-first during live monitoring.

## Write boundary

Football audit materials remain under `models/football/`. Do not write `/ledger.json` unless the user explicitly lifts the ledger hold.
