# Temporary LoL Model Override — v0.3.58

**Effective:** 2026-08-16 UTC+7  
**Status:** ACTIVE TEMPORARY OVERRIDE  
**User instruction:** "Temporarily pause latest version, use model v0.3.58"

## Scope

For all new live analysis and shadow selections until the user explicitly restores or changes the model:

- **Active analytical model = LoL v0.3.58.**
- `MODEL_RULES_LOL_V0.3.59.md` and `MODEL_RULES_LOL_V0.3.60.md` are **paused analytically** and must not be applied to new verdicts.
- Historical positions and diagnostic reviews remain unchanged and preserved.
- This is a temporary rollback, not deletion or repudiation of v0.3.59/v0.3.60.

## What remains active

Operational/governance controls remain in force unless they analytically depend on v0.3.59/v0.3.60:

- shadow-only execution: simulated 0.25u, actual 0u;
- minimum odds 1.60;
- verdict-first workflow;
- mandatory full underlying analysis despite compact output;
- two-snapshot live eligibility for ML/KH/TK;
- pregame/immediate post-draft ML/KH/TK TAKE disabled;
- one TAKE maximum per market family per map;
- stale/greyed market non-executability;
- position-blind reassessment;
- exact signed kill-margin arithmetic;
- no rescue/martingale/loss chasing;
- draft-locked underdog +kills fallback certification remains fail-closed because it enforces retained v0.3.57 logic rather than adding a later analytical model delta.

## Paused analytical additions

Do not apply the following while this override is active:

### v0.3.59
- 0-0 tower neutralization as a formal new Duration rule;
- ABSENT vs FAILED conversion formalization;
- LCH framework and its new Duration Over veto structure.

### v0.3.60
- Forward Regime Persistence (FRP);
- Fast-Close Robustness (FCR);
- mandatory RL/SL/OSC/CFC ML decomposition as a v0.3.60 gate;
- Same-Mechanism Re-certification (SMR).

Ordinary retained v0.3.58-and-earlier concepts such as team/market anchoring, draft primacy, role-weighted economy, terminal threat, OKP/FCI/CRR, FFD/RNE, Structure Substitution, NKB/RFI/KCV, and fallback certification continue to apply.

## Recording

- New selections taken under this override must be recorded as **model v0.3.58 (temporary override)**.
- Do not retroactively relabel prior v0.3.59/v0.3.60 positions.
- Do not create v0.3.61 while this temporary override is active unless the user explicitly asks for a new revision.

## Restoration

The override ends only on explicit user instruction to restore v0.3.60, use another version, or resume the latest model.
