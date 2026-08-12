# Football v1.0 — Cross-Chat Transfer Handoff — 2026-08-12

**Repository:** `acchtt/SlipTrace`  
**Canonical namespace:** `models/football/`  
**Active model:** **Football v0.2.43 — AUDIT MODE**  
**Official football betting:** PAUSED  
**Execution mode:** SHADOW CALIBRATION ONLY

## Mandatory startup

Load `models/football/CURRENT_MODEL.md` first and obey its current load order. Newer rule files override older conflicts. Do not rely on the 2026-08-06 handoff for active version, stake policy, or current audit status.

A future chat must preserve these controls:

- 1u = 1,000,000 VND.
- Minimum odds reference = 1.70.
- Official football betting remains paused until audit exit criteria are met and the user explicitly approves resumption.
- Directional AH/DNB/ML selections remain quarantined from official promotion.
- Ledger writes remain on hold until explicitly authorized.
- xG/xGOT are secondary only and may be discarded when provider quality is unreliable.
- Every material assessment must preserve exact score/minute/line/odds synchronization.
- Current audit model and the early-totals benchmark remain separate research arms.

## Strict team-style requirement — v0.2.43

Before every serious match preview, and before the first live recommendation in a match, profile both teams using verifiable current evidence.

For each team include:

- base build-up style;
- main attacking routes;
- tempo;
- defensive block/press;
- transition behaviour;
- chance-generation signature;
- typical behaviour after taking a lead;
- typical behaviour after falling behind;
- expected matchup-specific adaptation;
- confidence level / sample caveat.

Do not use generic labels from reputation alone. Distinguish base style from expected matchup style.

If the style profile cannot be adequately verified, mark `STYLE PROFILE INCOMPLETE` and cap the prematch verdict at `NO BET — HOLD`.

## Strict post-goal requirement

Every goal causes a tactical/state reset. A future chat may not justify a live Over by merely saying the trailing team must chase or the leader will have counters.

After a goal, explicitly assess:

- `Prematch style expectation:`
- `Leader post-goal behaviour:`
- `Trailer post-goal behaviour:`
- `Style deviation:` AS EXPECTED / MORE OPEN THAN EXPECTED / MORE CLOSED THAN EXPECTED / STYLE BREAK-UNRESOLVED
- `Post-goal persistence:`
- `Market implication:`

Normally require two comparable post-goal observations, or one observation plus strong event-level evidence across a meaningful interval, before promoting a new shadow candidate.

For Overs, verify real chase/transition production through actual box access, shots, SOT, set pieces, substitutions, defensive degradation, or independent scoring routes. For Unders, verify actual suppression/sterility rather than elapsed time alone.

## Current audit research direction

Recent directional football performance was poor enough to suspend official execution. The model is testing whether live totals and Asian-total boundary protection provide a more stable edge than directional handicaps.

The early-totals benchmark remains only a research arm. It must evaluate both Over and Under, not create an automatic Over or Under bias.

Recent shadow-total testing produced mixed results; do not treat the small sample as proven edge. Continue prospective tracking without retrospective filtering.

## Future-chat behavior

When the user names a match to preview, do not jump directly to odds or a side. First obtain/verify current competition format, venue, team news/lineups when available, and the two-team style profile required by v0.2.43.

When the user supplies a live screenshot, synchronize the state first, compare actual play with the prematch style expectation, and then scan the market. If a goal occurred since the prior checkpoint, apply the mandatory post-goal reset before any shadow recommendation.

Use only shadow language while audit mode is active: `SHADOW LEAN — DO NOT PLACE`, `BENCHMARK SHADOW — DO NOT PLACE`, `NO BET`, or `NO BET — HOLD`.
