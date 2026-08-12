# CURRENT LIVE HANDOFF — LoL — 2026-08-12

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.54.md`
3. retained deltas v0.3.53 through v0.3.26
4. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
5. `models/lol/procedures/LOL_SHADOW_AUTO_RECORD_ADDENDUM_2026-08-12.md`
6. stale-line / item-verification / connected-stack procedures
7. `models/lol/reviews/HLE_BRO_G1_ROLE_WEIGHTED_ECONOMY_REVIEW_2026-08-12.md`
8. aggregate/recent reviews referenced by `CURRENT_MODEL.md`
9. v0.3.25 baseline context/calibration files
10. scoreboard / stake procedures
11. This handoff last

## Active model
**LoL v0.3.54**

GitHub is model authority. Airtable is canonical map/position ledger.

## Operating state
- Official betting paused until explicit restoration.
- Shadow calibration active.
- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Minimum odds: 1.60.
- Same-game multiple shadow bets enabled after live eligibility when independently qualified.
- Pregame/immediate post-draft ML / Kill Handicap / Total Kills TAKEs disabled.
- Kill Handicap is enabled for normal live scanning/TAKEs.
- Duration: no pregame TAKE; no TAKE before 12:00; existing duration gates remain.
- Frozen/expired/stale/greyed/disabled/non-clickable quotes fail closed.
- User `Final`, `final score`, or `X won` is definitive settlement authority.
- Verdict must be output before connector/logging work.

## Shadow execution override — effective 2026-08-12 16:16 UTC+7

**Separate confirmation is no longer required for shadow bets.**

When a verdict is `TAKE` and the exact quoted line is visibly active/executable, fresh, and all normal model/eligibility gates pass, the shadow position is immediately official for calibration and must be logged in Airtable at the stated shadow stake.

This override applies only to shadow calibration while actual exposure is 0u. It does not restore or alter official real-money betting.

Do not auto-record stale/frozen/expired/greyed/disabled lines. Do not backfill old unconfirmed TAKEs from before the effective time.

Authority: `models/lol/procedures/LOL_SHADOW_AUTO_RECORD_ADDENDUM_2026-08-12.md`.

## v0.3.54 mandatory correction — Role-Weighted Economy

When role-level gold is visible, parse:
- `RGV` — role/champion gold vector;
- `GLC` — Gold Leverage Class (`HIGH / MEDIUM / LOW`) by champion function;
- `GCQ` — Gold Concentration Quality.

Do not treat near-even team gold as economic neutrality if distribution is asymmetric. After 30:00 combine with objective terminality (`TEI`). If visible role-level gold is not parsed, ML TAKE is ineligible.

## Current series — LCK 2026 Rounds 3-4
**Nongshim RedForce vs DN SOOPers**

### Game 1 — complete
Final: **NS 20-9 DNS, 25:45**.

Confirmed shadow position:
- `POSTCB-SHADOW-31-P01` Over 31 min @1.860 — **LOSS -0.25u**.

Review flag: at 19:38 NS led 13-6, +4.1k, towers 3-1, dragons 2-1 with no Baron/inhibitor. Duration Over underestimated how quickly NS would convert Baron/structures into a terminal close. Recheck terminality/acceleration before future duration Overs.

### Game 2 — active
Latest synchronized state at **18:18**:
- DNS 11-3 NS
- DNS +4.0k
- towers 1-1
- dragons DNS 2-0 NS
- Baron 0-0
- role-gold edge distributed across DNS Jayce/Pantheon/Ziggs; NS's main positive pocket is mid Locke.

Latest board:
- NS ML 4.837 / DNS ML 1.158
- Duration 32 O1.937 / U1.805 — suspended at snapshot
- Total Kills 31.5 O2.008 / U1.747 — active
- KH NS +14.5 1.936 / DNS -14.5 1.806

Open shadow position:
- `POSTCB-SHADOW-32-P01` **Under 31.5 kills @1.747**, shadow 0.25u, actual 0u, entry 18:18.
- Opposite-side fade benchmark: Over 31.5 @2.008.

Entry thesis: DNS's carry-distributed lead plus poke/siege, return-kill suppression, and potential future fight-window deletion support the Under. Reassess after Baron, inhibitor, major kill burst, or strong NS return-kill sequence.

## Live procedure
1. Pregame/post-draft analysis only.
2. ML / KH / Total Kills require two synchronized live snapshots before TAKE.
3. Duration follows later clock restrictions.
4. Run stale-line freshness gate before every TAKE.
5. Parse visible role-level gold for ML and where material for KH/TK.
6. **A qualified shadow TAKE is auto-recorded immediately; do not ask for confirmation.**
7. Record visible opposite-side fade benchmark when available.
8. Reassess open positions position-blind after material changes.
9. No rescue/martingale/loss chasing.

## Mandatory live response
First visible line:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Keep live explanations brief; full procedure still runs underneath.
