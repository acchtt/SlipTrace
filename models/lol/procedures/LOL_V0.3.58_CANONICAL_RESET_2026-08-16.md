# LoL v0.3.58 Canonical Reset

**Effective:** 2026-08-16 UTC+7  
**Status:** ACTIVE GOVERNANCE  
**User instruction:** "Discard newer versions, update this version accordingly"

## Decision

LoL **v0.3.58 is the canonical active analytical model**.

The prior temporary override is ended. This is no longer a temporary rollback.

`MODEL_RULES_LOL_V0.3.59.md` and `MODEL_RULES_LOL_V0.3.60.md` are **retired from the active analytical hierarchy**. They may remain in the repository only as historical/audit artifacts. They must not be loaded, blended, restored automatically, or used to justify new verdicts.

Historical positions and P/L remain labeled as originally recorded.

## Canonical in-place amendment

The active v0.3.58 file is amended in place with the KRX vs BRO Game 2 Duration correction:

- quiet kill pace is not positive Duration stall evidence by itself;
- 0-0 towers / low tower count are neutral descriptors by default;
- structural evidence must be classified as `ABSENT CONVERSION` or `FAILED CONVERSION`;
- only actual failed conversion / observed clock-consuming defense can support the structure portion of an Over thesis;
- Structure Substitution is mandatory: map progress through objectives/structures can compress clock while kills remain low;
- Duration Over requires two independent positive clock-consuming mechanisms, with at least one grounded in observed failed conversion or equivalent repeated denial;
- every Duration Over must test the shortest next compulsory fight/objective -> structures -> base -> Nexus cascade.

Reference review:
`models/lol/reviews/KRX_BRO_G2_DURATION_STRUCTURE_SUBSTITUTION_REVIEW_2026-08-16.md`

## Active operational governance

The following remain active because they are execution/governance controls or retained pre-v0.3.58 analytical controls:

- shadow only: simulated 0.25u, actual 0u;
- minimum odds 1.60;
- verdict first before connector/logging work on active maps;
- compact visible output still requires full underlying analysis;
- pregame/immediate post-draft ML/KH/TK TAKE disabled;
- live ML/KH/TK require two synchronized snapshots;
- maximum one TAKE per market family per map: ML / Kill Handicap / Total Kills / Duration;
- stale/greyed markets are non-executable;
- position-blind reassessment;
- exact signed kill-margin arithmetic;
- draft-locked underdog +kills fallback certification remains fail-closed;
- no rescue, martingale, chasing, or stake escalation.

## Explicitly retired analytical material

Do not apply v0.3.59/v0.3.60 as model layers. In particular, do not load their files merely because they have higher version numbers.

Only concepts explicitly incorporated into the amended canonical v0.3.58 file are active.

This means later-version-only analytical additions are not active unless the user separately re-authorizes them.

## Recording

New positions are recorded as:

**LoL v0.3.58**

Do not append "temporary override" to new records after this reset.

Do not retroactively relabel historical positions.

## Future changes

Remain on v0.3.58 until the user explicitly requests another model change. Do not auto-promote to v0.3.59, v0.3.60, or a new version because of an individual result.
