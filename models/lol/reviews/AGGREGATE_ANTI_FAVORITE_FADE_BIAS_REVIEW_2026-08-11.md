# AGGREGATE ANTI-FAVORITE / FADE-BENCHMARK REVIEW — 2026-08-11

## Scope

This review is triggered by the completed SK-VIT and G2-NAVI LEC series cluster and the broader post-circuit-breaker shadow ledger.

Official betting remains paused. All positions reviewed here were shadow only, 0.25u each, actual exposure 0u.

## Aggregate evidence

Post-circuit-breaker settled shadow positions through `POSTCB-SHADOW-25-P01`:

- Record: **10-16**
- Net: **-1.5255u**
- Stakes: 6.50u
- ROI: approximately **-23.47%**

Most recent five confirmed positions:

1. SK ML @1.752 vs VIT — LOSS
2. SK +6.5 kills @1.814 vs VIT — LOSS
3. NAVI +1.5 kills @1.822 vs G2 — LOSS
4. NAVI +7.5 kills @1.931 vs G2 — LOSS
5. Over 30.5 kills @1.890, G2-NAVI G2 — LOSS

Model result over those five: **0-5, -1.25u**.

At the exact opposite prices visible at entry, a 0.25u fade benchmark would have returned approximately:

- VIT ML @2.042: +0.2605u
- VIT -6.5 @1.964: +0.2410u
- G2 -1.5 @1.956: +0.2390u
- G2 -7.5 @1.844: +0.2110u
- Under 30.5 @1.865: +0.21625u

Fade benchmark total: **+1.16775u**.

This does not prove that blind fading is a durable strategy, but it is strong evidence of a current directional/calibration bias that must be treated as a model-governance failure rather than ordinary variance.

## Primary failure 1 — Systematic anti-favorite / underdog-resilience bias

The model repeatedly identified theoretical underdog tools and converted them into excessive probability shifts away from the market/team-strength favorite.

Examples:

- SK vs VIT G2: SK's Skarner/Nocturne/TF/Orianna/Kai'Sa control/catch package was treated as enough to materially compress VIT's wide-margin tail. VIT won 24-7.
- NAVI vs G2 G1: early NAVI catch success caused the model to move from a buffered +kills thesis to NAVI +1.5 despite G2's superior range/skill shell. Final adjusted margin was G2 +5; NAVI +6.5 would have covered while +1.5 lost.
- NAVI vs G2 G2: NAVI +7.5 was priced as resilient to G2's map control. G2 finished +8 kills and covered by 0.5.

The correction is not "always bet favorites." The correction is that **team-strength and market priors cannot be reset to neutral merely because an underdog draft has visible tools.**

## Primary failure 2 — Tool-count fallacy / correlated mechanism failure

The model has been treating several champion-level answers as if they were independent survival mechanisms.

In practice, many tools share the same dependencies:

- same tempo state;
- same engage angle;
- same jungle/support access;
- same ability to enter fog/chokes;
- same economy threshold;
- same first-spell success.

When the underdog loses tempo or map control, multiple supposed answers fail together. This is correlated mechanism failure, not diversification.

Future draft/live analysis must classify each major mechanism as `INDEPENDENT`, `PARTIALLY COUPLED`, or `COUPLED` and apply a shared-failure penalty to comeback and +kills-survival branches.

## Primary failure 3 — Team skill / series execution prior was underweighted

Fearless Draft resets champion availability and mechanisms. It does **not** reset:

- player skill;
- lane reliability;
- objective setup quality;
- range management;
- vision discipline;
- engage timing;
- ability to convert a lead;
- ability to avoid low-value fights.

VIT and G2 repeatedly showed superior execution across different drafts. The model allowed fresh-draft narratives to overpower this persistent team-level prior.

Same-series maps must therefore update a persistent execution prior rather than starting each draft from a near-neutral state.

## Primary failure 4 — Handicap buffer destruction

NAVI-G2 G1 exposed a line-selection error.

The original post-draft NAVI +7.5 line represented the actual thesis: NAVI could lose the map but keep the kill margin bounded.

After early NAVI success, the market compressed to +1.5. The model took +1.5 because NAVI's mechanism appeared to be functioning. That decision discarded most of the protection precisely when the favorite's latent range/skill edge still existed.

Final adjusted score: G2 14-9 NAVI. NAVI +6.5 would have cashed; +1.5 lost.

Future rule: **temporary underdog success does not justify sacrificing handicap buffer unless repeated live evidence also shows the favorite's collapse tail has materially disappeared. If the protective line has compressed too far, PASS.**

## Primary failure 5 — BF/SRR was confused with kill volume

G2-NAVI G2 draft had many engage/contact tools, leading to Over 30.5 @1.890.

Final: G2 15-7 NAVI, 22 total kills, while G2 simultaneously achieved a large structural stomp.

The missing branch was:

- high contact availability;
- strong-team clean or low-return-kill wins;
- rapid structure conversion;
- shrinking number of future fight windows.

Therefore BF/SRR must not directly raise total kills without modeling:

1. kills per realized contact window;
2. loser return-kill share;
3. whether the stronger team can end the sequence through towers/Baron/inhibitors rather than another fight;
4. how structure acceleration deletes future windows.

## Primary failure 6 — Structure Substitution was one-directional

The model often treated structure conversion as automatically compressing favorite kill-margin tails.

That is incomplete. In a strong team-skill or range-control mismatch, structure pressure can also **force** the weaker team into losing defenses, creating both structures and kills.

Structure Substitution must become two-sided:

- `MARGIN-COMPRESSING` when the favorite can safely take map progress without extra combat;
- `MARGIN-EXPANDING` when map pressure forces repeated low-quality defense or base fights;
- `NEUTRAL/MIXED` when both branches remain live.

## Governance failure — too-fast model promotion

Recent revisions were promoted after single-map explanations. That creates narrative overfit.

Future model promotion requires one of:

- an aggregate sample of at least **5 settled positions across at least 3 maps** showing the same error mechanism; or
- a deterministic correctness bug that is logically independent of outcome.

Single-map findings may enter probationary notes but may not immediately create strong new confidence.

## Required operating correction

Effective next session:

1. **No pregame or immediate post-draft TAKE in ML, Kill Handicap, or Total Kills.** Draft is analysis only.
2. Require **two synchronized live snapshots at least ~90 seconds apart** before any ML/KH/Total Kills TAKE.
3. Same-game multiple shadow bets remain enabled after eligibility; correlated positions are grouped for calibration.
4. Every TAKE must record the visible opposite-side price as a **fade benchmark** when available.
5. The market/team-strength prior is the starting anchor; draft may modify it but may not erase it.
6. Underdog tools must receive a mechanism-independence/shared-failure test.
7. Buffered +kills lines must pass a buffer-retention test; a heavily compressed line is not an automatic replacement.
8. Total Kills must explicitly model return-kill suppression and structure-driven deletion of future fight windows.
9. Official betting remains paused; no stake escalation.

## Conclusion

The current issue is not merely that several close bets lost. The model has a detectable **anti-favorite calibration bias**, a **correlated-tool overcount**, and a **contact-to-kill conversion error**. These must be corrected at the process layer before the next series rather than patched champion by champion.
