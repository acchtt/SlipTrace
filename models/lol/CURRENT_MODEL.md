# Current League of Legends Model

**Canonical namespace:** `models/lol/`

## ACTIVE MODEL

- Active analytical model: **LoL v0.3.58**
- Active rules: `models/lol/rules/MODEL_RULES_LOL_V0.3.58.md`
- Canonical reset authority: `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
- **LoL v0.3.59 and v0.3.60 are retired/discarded from the active analytical hierarchy.**
- Their files may remain only as historical/audit artifacts. Do not load, blend, or auto-restore them.

User instruction on 2026-08-16 UTC+7: **"Discard newer versions, update this version accordingly".**

The prior temporary v0.3.58 override is ended. v0.3.58 is now the canonical model, not a temporary rollback.

## Canonical v0.3.58 Duration amendment

The active v0.3.58 file now includes the KRX vs BRO Game 2 correction:

- low kills are not positive Duration stall evidence by themselves;
- 0-0 towers / no first tower / low absolute tower count are neutral state descriptors by default;
- conversion evidence must be classified as `ABSENT CONVERSION` or `FAILED CONVERSION`;
- only actual failed conversion or another clearly observed clock-consuming defense/reset mechanism may support the structure portion of an Over thesis;
- Structure Substitution is mandatory — objective/tower progress can compress clock even while kills remain low;
- a Duration Over requires two independent positive clock-consuming mechanisms, with at least one grounded in observed failed conversion or equivalent repeated denial;
- every Duration Over must test the shortest plausible next compulsory fight/objective -> serial structures -> base -> Nexus cascade.

Reference review:
`models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

## Active operational governance

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
- Draft-locked underdog +kills fallback certification remains fail-closed.
- No rescue, martingale, chasing, or stake escalation.

## Retired newer analytical versions

Do **not** apply v0.3.59 or v0.3.60 to new analytical verdicts merely because their version numbers are higher.

Later-version-only concepts are inactive unless they have been explicitly incorporated into the amended v0.3.58 file or the user separately re-authorizes them.

Historical positions and P/L remain unchanged and keep their original model labels.

## Required load order

1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/procedures/LOL_V0.3.58_CANONICAL_RESET_2026-08-16.md`
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
14. latest live handoff last, applying this CURRENT_MODEL authority where conflicts exist

**Do not load v0.3.59 or v0.3.60 rule files in the active stack.**

## Recording

- New positions are recorded as **LoL v0.3.58**.
- Do not append `temporary override` to new records.
- Prior v0.3.59/v0.3.60 positions remain labeled historically as they were.
- Do not create or auto-promote a newer model from an individual outcome unless the user explicitly requests another model change.
