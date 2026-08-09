# Kill-Handicap Directional Bias Review — 2026-08-09

**Model transition:** v0.3.43 -> v0.3.44  
**Trigger:** user observed persistent positive-handicap bias.

## Tracked sample at review

The Airtable tracker contained 12 kill-handicap selections and **all 12 were on the positive-kill side**.

Known settled kill-handicap results:

- WE +14.5 @1.966 — WIN +0.2415u
- BRO +6.5 @2.056 — WIN +0.2640u
- SHFT +3.5 @1.886 — LOSS -0.25u
- GX +3.5 @1.781 — LOSS -0.25u
- SHFT +10.5 @1.835 — LOSS -0.25u
- TH +7.5 @1.940 — LOSS -0.25u
- EDG +10.5 @1.810 — LOSS -0.25u
- NAVI +5.5 @1.886 — LOSS -0.25u
- SK +7.5 @2.124 — WIN +0.2810u
- LNG +9.5 @1.970 — LOSS -0.25u

Known settled record: **3-7**.  
Known settled P/L: **-0.9635u** on 2.5u staked, approximately **-38.5% ROI**.

Data exceptions:

- TH +6.5 @1.818 had no populated settlement result in Airtable at review time.
- KT +3.5 @1.935 vs DK Game 2 was open and remains a v0.3.43 entry.
- LNG +9.5 was still marked Open in Airtable despite the synchronized final IG 26-13 LNG result; canonical grading is LOSS -0.25u.

## Diagnosis

The issue is a **process asymmetry**, not proof that positive handicaps are inherently bad.

The previous engine repeatedly began from the question, "How can the underdog stay within +H?" It then credited range, waveclear, disengage, scaling, return-kill access and the numerical size of the cushion. The opposite event — the favorite winning by a large kill margin — did not receive equal branch depth.

This created four failure modes:

1. **Cushion anchoring:** +7.5/+9.5/+10.5 visually looked safe before a fair margin distribution was constructed.
2. **Linear-margin thinking:** current kill margin plus exact future net kills required was treated as probabilistic evidence, despite cascades making future margin expansion path-dependent.
3. **Underdog-tool overcounting:** theoretical defensive tools were converted too readily into close-loss probability.
4. **Favorite-tail underpricing:** structural control, carry concentration, repeatable engage, objective routing and terminal base-defense kills were not fully priced into wide favorite wins.

The 12/12 positive-side selection share is a stronger diagnostic of directional process bias than the small-sample 3-7 record alone.

## Corrective action

v0.3.44 makes kill handicap pricing side-neutral:

- model signed favorite kill margin before comparing with the book line;
- use one common margin distribution for both +H and -H prices;
- explicitly model wide favorite-win tails;
- retain matchup-adjusted underdog resilience, but only as a modifier to the same distribution;
- add live cascade/terminal-kill inflation hazard;
- apply a temporary +2pp calibration surcharge to all new handicap TAKE gates for the next 20 settled v0.3.44 handicap entries;
- audit directional selection share after 10 and 20 new settled entries.

The correction does **not** force favorite handicaps. A healthy model may still select more positive than negative lines if the same side-neutral distribution supports them.

## Grandfathered open entry

KT +3.5 kills @1.935 vs DK Game 2 was recorded before v0.3.44 activation and remains a valid v0.3.43 shadow position. It is not retroactively voided or regraded. Future position-blind reassessment uses current v0.3.44 logic.
