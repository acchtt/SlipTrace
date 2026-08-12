# CURRENT LIVE HANDOFF — LoL — 2026-08-12

Updated through **20:37 UTC+7** after BLG–JDG Game 1 settlement.

## Purpose
This file is the continuation handoff for the next chat. It preserves the operational logic, user-facing workflow, model state, active series state, execution corrections, and decision-rationale summaries needed to continue without reconstructing the long chat.

It does **not** attempt to preserve private scratchpad/hidden chain-of-thought verbatim. Preserve and apply the explicit rules, state, mechanisms, corrections, and rationale capsules below.

## Required load order
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
11. **This handoff last**

Where conflict exists, the shadow auto-record addendum and this handoff control the current shadow workflow.

## Active model / authority
- **LoL v0.3.54**.
- GitHub = model/rules authority.
- Airtable = canonical map/snapshot/position ledger.
- Official betting remains paused until explicit restoration.
- Shadow calibration active.
- Actual exposure remains **0u**.

## User-facing operating style — mandatory
- **Verdict first.** Logging/connectors must never delay the visible live verdict.
- Keep live output brief, but run the full procedure underneath.
- First visible line on an active map should be exactly one of:
  - `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
  - `PASS — [market/selection] @[odds] — 0u.`
  - `HOLD — [market/selection] @[odds] — 0u.`
- User explicitly complained that verdicts sometimes took too long. Optimize latency: parse screenshot → verdict → only then ledger work.
- User corrections about LIVE/FINAL, timer bugs, stale/unavailable lines, or scoreboard display bugs are authoritative execution evidence.
- User `Final`, `final score`, or `X won` is definitive settlement authority when grading data are sufficient.

## Shadow execution override — effective 2026-08-12 16:16 UTC+7
**Separate confirmation is no longer required for shadow bets.**

When the model says TAKE and the exact quoted line is visibly active/executable, fresh, and eligible, the shadow position becomes official for calibration immediately and should be logged at the stated stake.

- Default shadow stake: **0.25u**.
- Minimum odds: **1.60**.
- Actual exposure: **0u**.
- Do not auto-record stale/frozen/expired/greyed/disabled/non-clickable lines.
- If the user later says a line was unavailable at the proposed entry, **scratch the position entirely**: NO BET / 0u / no validation count / no P&L.
- Do not backfill old recommendations that were never executable.
- Record visible opposite-side price as a fade benchmark when practical, but not as a second position.

## Core live eligibility
- Pregame and immediate post-draft ML / Kill Handicap / Total Kills TAKEs are disabled; analysis only.
- ML / Kill Handicap / Total Kills require at least **2 synchronized live snapshots**, preferably >=90 sec apart, before TAKE.
- Duration: live-only; no TAKE before **12:00**.
- Duration 12:00–13:59 requires two synchronized snapshots >=90 sec apart showing the same mechanism; 14:00+ still requires observed stall/acceleration.
- Same-map multiple shadow bets are allowed after eligibility if each independently qualifies. Do not force bets for sample size.
- No rescue, martingale, or loss chasing.

## Mandatory stale / executable-line gate
Before every TAKE:
- Compare candidate line/price to immediately prior sportsbook state.
- Exact frozen line+price across material map movement is suspect stale.
- If adjacent markets reprice while one stays frozen, fail closed unless clearly active/fresh.
- Greyed/disabled/frozen/expired/non-clickable = **NO BET / 0u**.
- A displayed quote can be visually present but not executable.
- User identification of a frozen/unavailable line is definitive for execution grading.

## Scoreboard parsing / visual gotchas
- Do not infer gold-lead side from a bare plus sign. Use scoreboard side color / arrow direction / team-side orientation.
- Role-gold rows must be parsed per matchup: identify which side the arrow/colored number favors, then build the role-gold vector.
- Tracker pages have repeatedly shown **`Final` while the game is actually LIVE**. If user says LIVE, treat the state as LIVE and ignore the bad tracker status.
- If user flags a timer offset/bug, use the corrected timer for that map; do not generalize the offset to unrelated sources/maps.
- Never overwrite a user-supplied scoreboard correction with automated display assumptions.

# v0.3.54 mandatory mechanism — Role-Weighted Economy
When role-level gold is visible, parse and use:
- `RGV` — role/champion gold vector;
- `GLC` — Gold Leverage Class (`HIGH / MEDIUM / LOW`) by current champion function;
- `GCQ` — Gold Concentration Quality.

Do not treat near-even team gold as economic neutrality when role distribution is asymmetric.

If role-level gold is visible but not parsed, live ML TAKE is ineligible.

After 30:00 combine RWE with objective terminality (`TEI`). High-terminal objective access + high-leverage carry concentration materially suppress comeback tails.

## How to use role gold in practice
- Broad small leads across 4–5 roles = distributed control, but still distinguish **terminal** from **non-terminal** control.
- Large gold concentrated on high-leverage mid/ADC/carry champions can matter more than similar total gold on utility/low-leverage pockets.
- A temporary underdog lead can justify ML/+kills only if it proves the favorite baseline execution edge is actually being suppressed.
- Reassess position-blind after material changes. Early favorite suppression can decay rapidly if role-gold distribution flips.

# Retained v0.3.53 logic that matters most live

## MKT + TEAM anchor
Start from current market plus persistent team-strength/execution prior. Draft does not reset TEAM to neutral.

## Anti-favorite guard
Before underdog ML/+kills against a clear favorite, require observed evidence that the favorite's baseline skill/conversion edge is suppressed. One kill, one objective, or one fed lane is insufficient.

## Mechanism independence / shared-failure penalty
Do not double-count multiple tools that depend on the same engage angle, fog state, tempo, or first-spell success.

## Handicap Buffer Retention
If thesis = underdog can lose but keep margin bounded, do not chase a compressed +kills line just because the underdog temporarily leads. Preserve buffer unless repeated evidence proves the wide-margin tail has collapsed.

## Structure Substitution
Structure control can:
- compress kill margin if favorite closes without fighting, or
- expand kill margin if base/structure pressure forces repeated losing defenses.
Classify the actual map mechanism rather than assuming one direction.

## Total Kills
Retain OKP / FCI / CRR / SRR / BF / CL plus:
- `RKS` Return-Kill Suppression;
- `KPW` Kills Per Realized Window;
- future fight-window deletion from Baron/structures/inhibitors.

High contact availability does not automatically imply high final kills.

### Critical totals correction from NS–DK G2
Early low kill pace alone is not enough for an Under. **0 towers + close gold + hard engage** can extend the duration tail and preserve repeated late objective-fight windows. Every kill Under needs a duration/escalation coupling check.

# Same-day model lessons to retain

## HLE Challengers vs BRO Challengers G1 — role-weighted economy bug
The earlier raw-gold summary underweighted BRO's large economy advantages on K'Sante/Corki plus four dragons/Baron while HLE's positive pocket sat more on utility-side resources. This drove v0.3.54. Always parse visible role gold.

## DK vs KT G2 — early suppression can decay
Draft:
- DK blue: K'Sante / Vi / Taliyah / Sivir / Bard
- KT red: Jayce / Naafiri / Annie / Ziggs / Nautilus

Early live:
- 6:31 KT led 2–0, about +1.1k, with role gold favoring KT across all five rows. `KT +3.5 @1.869` was taken.
- 10:31 KT led 4–0, about +1.6k, with KT still ahead in top/mid/ADC/support and only DK jungle positive. `KT ML @1.719` was taken.
- By 24:22, kills were 8–7 KT but DK led about +2.6k, with high-leverage role gold shifted strongly to DK mid/ADC/support. `Over 25.5 kills @1.607` was taken.
Final: **DK 17–11 KT at 33:52**.
Settlement:
- KT +3.5 @1.869 — LOSS -0.25u
- KT ML @1.719 — LOSS -0.25u
- Over 25.5 @1.607 — WIN +0.15175u
Map net: **-0.34825u**.
Lesson: early underdog suppression can be real yet temporary; role-gold concentration on favorite high-leverage carries must trigger a strong position-blind downgrade. Totals can remain independently valid after side thesis flips.

## BLG vs JDG G1 — buffer retention + execution integrity
Pregame series market:
- BLG 1.318 / JDG 3.317; de-vig roughly BLG 71.6% / JDG 28.4%.
- TEAM anchor = BLG strong favorite.
- BLG top starter confirmed by user as **Flandre**.

G1 draft:
- JDG blue: Rumble / Jarvan IV / Viktor / Jhin / Nautilus
- BLG red: Ambessa / Xin Zhao / Syndra / Ezreal / Karma

Post-draft read: BLG slight draft edge, roughly 64–66%, aligned with favorite market. JDG had cleaner 5v5 wombo/engage; BLG had range, pick, skirmish flexibility and kiting.

Live snapshots:
- 5:48: 0–0 kills, 0–0 objectives. BLG held small role-gold leads across all five roles. HOLD.
- 8:12: 0–0 kills, BLG 1–0 dragon, 0–0 towers. BLG still had only small distributed role-gold leads; no terminality. Market widened to JDG +9.5 @2.035. **TAKE JDG +9.5 @2.035, shadow 0.25u.**
- ~18:49 live state despite tracker falsely showing Final: BLG 13–5, 3–0 towers, 3–0 dragons, distributed gold across all five roles. No add-on.
- 25:01: BLG 20–14, 5–1 towers, 3–1 dragons, no Baron. A proposed `JDG +11.5 @2.066` looked attractive on buffer-retention logic, but the user later confirmed the line was **unavailable**. It has been deleted from Airtable and must never be graded or counted.

Final G1: **BLG 28–20 JDG at 30:46**.
Valid shadow settlement:
- `JDG +9.5 @2.035` — **WIN +0.25875u**.
- `JDG +11.5 @2.066` — **SCRATCH / NO BET / 0u / no validation count**.

Important inference: BLG dominated the map, yet JDG generated enough return kills for the final margin to finish at 8. This supports wide-buffer retention when the underdog's fight package keeps producing kills, but only if the line is actually executable.

# Current active series — BLG vs JDG, LPL 2026 Split 3
- Series score: **BLG leads 1–0**.
- Game 1 final: BLG 28–20 JDG, 30:46.
- **No open shadow positions.**
- Next map: **Game 2 pending**.

Expected current cores for this series based on observed G1 / user correction:
- BLG: Flandre / XUN / knight / Viper / ON
- JDG: Xiaoxu / JunJia / HongQ / GALA / Vampire

For Game 2:
- TEAM prior remains **BLG strong favorite**, but JDG's G1 ability to generate 20 kills despite losing should modestly strengthen JDG's kill-buffer floor, not its outright ML prior.
- Do not overreact to G1 final margin alone. Wait for blue side, draft, opening map odds.
- If JDG gets early live advantage, require **distributed role-gold + objective/structure evidence** before underdog ML.
- For JDG +kills, preserve a genuinely wide buffer when the map remains non-terminal and JDG's engage/wombo is producing return kills; do not chase compressed buffers.
- If BLG has distributed high-leverage economy + structure/dragon terminality, widen blowout tails and downgrade JDG handicap survival.

# Current validation / accounting
- Official betting paused; official probation remains as stated in `CURRENT_MODEL.md`.
- Shadow actual exposure = **0u**.
- Corrected **v0.3.54 validation after scratching unavailable JDG +11.5**: **4–5, -0.38925u**.
- Do not count unavailable/stale/scratched lines in record, P&L, or validation sample.

# Airtable notes
Base: `SlipTrace LoL Live Tracker` (`appcx61bVBssnwvVd`).
Canonical tables:
- Maps `tblQMpvXFmXEhAGpv`
- Snapshots `tbl8ykMwApuBvldwE`
- Positions `tblPwnKFAsj1suaLv`

Do not invent restricted single-select values. If schema/options are not loaded, omit nonessential select fields rather than guessing.

The erroneous JDG +11.5 position created from G1 has been **deleted** after user correction that the line was unavailable.

# Next-chat startup command
Continue the League of Legends live-betting project from GitHub repository `acchtt/SlipTrace`.

Load the required order above, ending with `models/lol/CURRENT_LIVE_HANDOFF_2026-08-12.md`.

Active model: **LoL v0.3.54**.
Current series: **BLG vs JDG, BLG leads 1–0, Game 2 pending**.
No open shadow positions.
Shadow TAKEs auto-record immediately when executable; no confirmation required.
Verdict first; logging after.
