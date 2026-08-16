# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE TEMPORARY OVERRIDE

- Active analytical model: **LoL v0.3.58 (temporary override)**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- Temporary override authority: `models/lol/procedures/LOL_TEMPORARY_MODEL_OVERRIDE_V0.3.58_2026-08-16.md`
- **LoL v0.3.59 and v0.3.60 are temporarily paused for new analytical verdicts.**
- v0.3.60 files/reviews remain preserved for later restoration; no historical P/L is changed.

User instruction on 2026-08-16 UTC+7: **"Temporarily pause latest version, use model v0.3.58".**

## Active operational governance

Operational rules that do not depend on the paused analytical deltas remain active:

- Official betting remains paused; shadow only.
- Default shadow stake: **0.25u**; actual exposure: **0u**.
- Minimum odds: **1.60**.
- Verdict first; no connector/logging work before the visible live verdict.
- Compact output still requires full underlying analysis.
- Pregame/immediate post-draft ML/KH/TK TAKEs remain disabled.
- Live ML/KH/TK retain the two-snapshot eligibility gate.
- Same-map multiple TAKEs may occur across different market families, maximum one TAKE per family: ML / Kill Handicap / Total Kills / Duration.
- Greyed/stale markets are non-executable.
- Position-blind reassessment remains mandatory.
- Exact signed kill-margin arithmetic remains mandatory.
- No rescue, martingale, chasing, or stake escalation.
- Draft-locked underdog +kills fallback certification remains fail-closed because it enforces retained v0.3.57 logic.

## Paused while override is active

Do **not** apply v0.3.59 or v0.3.60 analytical additions to new decisions, including:

- v0.3.59 formal 0-0 tower neutralization / ABSENT-vs-FAILED conversion / LCH additions;
- v0.3.60 FRP;
- v0.3.60 FCR;
- v0.3.60 mandatory RL/SL/OSC/CFC gate;
- v0.3.60 SMR.

Use v0.3.58 and all non-conflicting earlier deltas only.

## Required load order during temporary override

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_TEMPORARY_MODEL_OVERRIDE_V0.3.58_2026-08-16.md`
3. `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
4. v0.3.57 through v0.3.26 rule deltas
5. mandatory fallback-floor certification procedure
6. mandatory live verdict checklist
7. retained pre-v0.3.59 reviews/procedures relevant to v0.3.58
8. item-verification suspension
9. v0.3.25 consolidated rules / probation / calibration handbook
10. live fast path and main betting procedure
11. connected-stack procedure and addenda
12. scoreboard protocol
13. shared stake policy
14. latest live handoff last, applying this override where conflicts exist

Where conflicts exist, **this temporary override controls analytical model selection; v0.3.58 controls analytically; retained operational governance controls execution.**

## Recording

- New positions under this override are recorded as **LoL v0.3.58 (temporary override)**.
- Prior v0.3.59/v0.3.60 positions remain labeled historically as they were.
- Do not create v0.3.61 from individual outcomes while this override is active.

## Restoration

This override remains active until the user explicitly says to restore v0.3.60, resume the latest model, or use another version.
