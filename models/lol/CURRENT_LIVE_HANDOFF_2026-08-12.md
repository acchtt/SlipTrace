# CURRENT LIVE HANDOFF — LoL — 2026-08-12

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.54.md`
3. retained deltas v0.3.53 through v0.3.26
4. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
5. stale-line / item-verification / connected-stack procedures
6. `models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`
7. aggregate/recent reviews referenced by `CURRENT_MODEL.md`
8. v0.3.25 baseline context/calibration files
9. scoreboard / stake procedures
10. This handoff last

## Active model
**LoL v0.3.54**

GitHub is model authority. Airtable is canonical map/position ledger.

## Operating state
- Official betting paused until explicit restoration.
- Shadow calibration active.
- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Minimum odds: 1.60.
- Same-game multiple shadow bets enabled after live eligibility.
- Pregame/immediate post-draft ML / Kill Handicap / Total Kills TAKEs disabled.
- Duration: no pregame TAKE; no TAKE before 12:00; existing duration gates remain.
- A wager is recorded only after explicit confirmation of the same executable line.
- Frozen/expired/stale quotes fail closed.
- User `Final`, `final score`, or `X won` is definitive settlement authority.
- Verdict must be output before connector/logging work.

## v0.3.54 mandatory correction — Role-Weighted Economy

When role-level gold is visible, live ML analysis must parse:

- `RGV` — role/champion gold vector;
- `GLC` — Gold Leverage Class (`HIGH / MEDIUM / LOW`) by champion function;
- `GCQ` — Gold Concentration Quality.

Do not treat near-even team gold as economic neutrality if gold distribution is materially asymmetric.

After 30:00, combine with objective terminality (`TEI`). A comeback ML against a side with both HIGH-terminal objective control and favorable HIGH-leverage gold concentration receives a major downgrade and defaults PASS/HOLD unless repeated live evidence shows those threats are being suppressed.

If role-level gold is visible but not parsed, ML TAKE is ineligible. If unavailable, do not invent it; add uncertainty.

## Reference map — HLE Challengers vs BRO Challengers G1

Draft:
- HLE: Olaf / Vi / Galio / Ezreal / Shen
- BRO: K'Sante / Lee Sin / Syndra / Corki / Camille

Confirmed positions:
- `POSTCB-SHADOW-29-P01` Over 34 min @1.877 — WIN +0.21925u
- `POSTCB-SHADOW-30-P01` HLE ML @5.952 — LOSS -0.25u

User settlement authority: **BRO won**.

G1 net: **-0.03075u**.

At HLE ML entry 36:09:
- HLE led kills 13-7;
- raw gold was close;
- BRO had 4 dragons + Baron;
- BRO role economy was concentrated on K'Sante/Corki while HLE's largest visible advantage was on Vi.

Error: model over-compressed the economy state to raw team-gold parity and underweighted terminal objective + carry-gold concentration.

## Validation accounting

v0.3.53 validation closed at **3-2, +0.283u** after HLE-BRO G1 settlement.

v0.3.54 begins fresh validation from the next eligible confirmed position. Prior positions remain in Airtable and aggregate/fade reviews remain relevant context.

## Open positions
**NONE.**

## Current series
LCK CL — HLE Challengers vs BRO Challengers.

Game 1 complete: **BRO won**.

Prepare Game 2 from scratch under Fearless Draft, carrying TEAM/execution evidence from Game 1. Side/draft/odds not yet supplied.

## Next-map procedure
1. Pregame: analysis only.
2. Post-draft: analysis only; record MKT/TEAM/draft/TTA/EBG/mechanism coupling.
3. Snapshot 1 around 5-7 minutes when available.
4. Snapshot 2 around 8-10 minutes or >=90 seconds later.
5. Only then scan ML / Kill Handicap / Total Kills for TAKE.
6. Duration follows existing later clock restrictions.
7. Before every TAKE run stale-line freshness gate.
8. For ML, parse visible role-level gold before verdict; after 30:00 apply TEI.
9. Record visible opposite-side fade benchmark on every confirmed TAKE.
10. Reassess position-blind after material changes.

## Mandatory live response
First visible line:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Keep live explanations brief; procedure still runs fully underneath.
