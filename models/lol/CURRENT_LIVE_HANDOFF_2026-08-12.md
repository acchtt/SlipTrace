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
- **Kill Handicap is enabled for live shadow scanning/TAKEs after normal live eligibility as of 2026-08-12 13:26 UTC+7 by explicit user instruction. No special KH suspension remains active.**
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

### Game 2
BRO blue / HLE red.

Draft:
- BRO: Ambessa / Qiyana / Annie / Caitlyn / Bard
- HLE: Gnar / Jarvan IV / Ryze / Varus / Nautilus

Scoreboard timer bug: **displayed timer is +3:00; subtract 3:00 for actual game clock unless user says bug clears.**

Corrected live history:
- baseline displayed 5:09 => actual 2:09, 0-0, BRO +21g, 0-0 towers/objectives.
- S01 displayed 13:39 => actual 10:39, HLE leads 5-1 and +2.3k, towers 0-0, dragons 0-0.
- **S02 correction:** displayed 14:59 => actual 11:59, HLE leads 9-2 and +4.3k, towers 0-0, HLE dragon 1-0. Duration and Total Kills were visibly suspended. Earlier assistant output claiming 17:57 / 9-1 / +6.5k / towers 2-1 and Under 31.5 @2.035 was a state-reading error; no position was confirmed and it is void / NO BET.
- S03 displayed 15:50 => actual 12:50, HLE leads 10-2 and +5.0k, towers 0-0, HLE dragon 1-0. Board: HLE ML 1.049 / BRO 9.345; Duration 29 O1.886/U1.886; Total Kills 30.5 O1.369/U3.032 suspended; KH HLE -17.5 1.604 / BRO +17.5 2.262.

Current G2 verdict at S03:
- KH enabled from this point forward.
- HOLD HLE -17.5 @1.604 / BRO +17.5 @2.262. HLE role-gold advantage is broad and the 18+ kill-margin tail remains live; neither side clears edge threshold confidently.
- No open confirmed G2 positions.

## Next-map/live procedure
1. Pregame: analysis only.
2. Post-draft: analysis only; record MKT/TEAM/draft/TTA/EBG/mechanism coupling.
3. ML / Kill Handicap / Total Kills require normal two-snapshot live eligibility before TAKE.
4. Duration follows existing later clock restrictions.
5. Before every TAKE run stale-line freshness gate.
6. For ML, parse visible role-level gold before verdict; after 30:00 apply TEI.
7. **Kill Handicap is live-enabled:** apply signed kill-margin distribution, NKB, RFI, KCV, Buffer Retention, Structure Substitution, and RWE where relevant.
8. Record visible opposite-side fade benchmark on every confirmed TAKE.
9. Reassess position-blind after material changes.
10. Never grade an unconfirmed recommendation.

## Mandatory live response
First visible line:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Keep live explanations brief; procedure still runs fully underneath.
