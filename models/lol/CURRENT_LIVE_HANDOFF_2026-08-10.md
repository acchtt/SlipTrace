# CURRENT LIVE HANDOFF — LoL — 2026-08-10

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.52.md`
3. retained deltas v0.3.51 through v0.3.26
4. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
5. latest reviews referenced by `CURRENT_MODEL.md`
6. v0.3.25 baseline context/calibration files
7. connected-stack / scoreboard / stake procedures
8. This handoff last

## Active model
**LoL v0.3.52**

GitHub is model authority. Airtable is canonical map/position ledger.

## Operating state
- Official betting paused until explicit restoration.
- Shadow mode active.
- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Minimum odds: 1.60.
- Same-map shadow add-ons enabled when each independently qualifies and joint correlation is explicitly priced.
- Duration: no pregame TAKE; no TAKE before 12:00.
- A wager is recorded only after explicit user confirmation of the same executable line.
- If a recommended line disappears before confirmation: NO BET / 0u; never grade hypothetical.
- User saying `Final`, `final score`, or `X won` is definitive settlement authority.

## Mandatory live response
First visible line on active maps:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Do not delay verdict for GitHub/Airtable work.

## Core model logic

### Draft Primacy
After draft lock, compare reliable first contact, CC density/reliability, anti-engage, frontline/backline access, carry protection, damage continuation, chase/cleanup, re-engage, objective/choke control, waveclear/base defense, side-lane/global numbers and execution simplicity.

### v0.3.52 Terminal Threat Overlay
Before post-draft/live ML TAKE, identify each side's strongest 20-25+ minute terminal threat and classify opponent answerability:
- ROBUST
- CONDITIONAL
- UNANSWERED

Also classify Execution Burden Gradient:
- FAVORABLE
- NEUTRAL
- ADVERSE

Classify current lead quality:
- TERMINAL / CLOSING
- NON-TERMINAL

Before 15:00, current-leader ML defaults HOLD/PASS when TTA is UNANSWERED/strongly CONDITIONAL, EBG is ADVERSE, the lead is NON-TERMINAL, and there is no repeated evidence of reliable threat access/suppression.

Live ML lower-bound buffers:
- +5pp early (<15:00)
- +4pp mid (15:00-24:59)
- +3pp late (25:00+)

Add +2pp for CONDITIONAL TTA + ADVERSE EBG; +4pp for UNANSWERED TTA + ADVERSE EBG, capped at +9pp total. Hard veto controls when active.

### Kill Handicap
Use a position-blind signed kill-margin distribution, NKB, RFI, KCV and Structure Substitution. Map dominance is not kill-margin dominance. Price +H and -H symmetrically. An unanswered terminal threat compresses favorite wide-margin tails until disproven.

### Total Kills — v0.3.51 retained
Model separately:
1. OKP — Observed Kill Pace
2. FCI — de-duplicated objective/event Forward Contact Inventory
3. CRR — Contact Realization Rate
4. SRR — Skirmish Recurrence Reserve between formal windows
5. CL — Contact Lethality conditional on contact

Conceptual projection:
`Final kills = current kills + CRR-weighted FCI kills + SRR kills + residual terminal/pick/chase kills`

Before 12:00, an Under cannot be TAKEN mainly from low current kills or a large cushion. Require two synchronized low-contact snapshots >=90 sec apart, repeated LOW-CL realized contact, or an observed near-terminal structure-only branch. One live snapshot + functional repeatable hard access => HOLD/PASS.

Bidirectional Forcing and Threat Deterrence GLOBAL/LOCAL/NONE remain mandatory. HIGH SRR/BF materially raises the high-T / low-M branch.

### Same-map Total Kills + handicap
Project `T` and `M` separately and price all four joint cells. A strong +kills position does not imply an Under.

### Duration
No pregame TAKE; none before 12:00. 12:00-13:59 requires two synchronized snapshots >=90 sec apart showing same observed mechanism. 14:00+ still requires observed stall/acceleration. Reprice after regime changes.

## Latest settled map — LEC SK vs VIT Game 1

Draft:

SK blue — Gnar / Jarvan IV / Ryze / Varus / Shen  
VIT red — Rumble / Pantheon / Viktor / Corki / Bard

Earlier unconfirmed recommendations:
- SK +5.5 kills @1.894 — line moved before confirmation => NO BET.
- SK +3.5 kills @1.751 / @1.758 — not confirmed => NO BET.

Confirmed shadow position:
- **SK ML @1.752**, 0.25u shadow, actual 0u.

Entry at 12:50:
- SK 5-2 VIT;
- SK +1.6k;
- towers 0-0;
- VIT 1-0 dragons;
- Grubs SK 2-1.

Final user-authoritative result: **VIT won**. Latest synchronized grading frame:
- VIT 23-14 SK;
- 32:50;
- towers VIT 9-4 SK;
- dragons VIT 4-0 SK;
- Baron VIT 1-0 SK;
- inhibitors VIT 2-0 SK.

Settlement: **SK ML LOSS -0.25u**.

User correction: **SK threw the game; SK had no answer to Viktor.**

### v0.3.52 correction from Game 1
The early SK lead was real but NON-TERMINAL:
- no tower lead;
- VIT already held first dragon;
- no demonstrated close path;
- Viktor-centered scaling/control threat remained functional;
- SK's answer to Viktor was UNANSWERED / highly CONDITIONAL;
- SK's execution burden became more adverse as the game shifted to organized objective setups.

Correct v0.3.52 read at 12:50: early-live ML hard veto ACTIVE; SK ML @1.752 should have been HOLD/PASS.

Review: `models/lol/reviews/SK_VIT_G1_TERMINAL_THREAT_ANSWERABILITY_REVIEW_2026-08-10.md`.

## Current live state
No open recorded positions. SK vs VIT series continues with **VIT leading 1-0**. Game 2 is next.

## Game 2 operating plan
- Re-run team/draft assessment from scratch under Fearless Draft; do not carry Game 1 draft conclusion mechanically.
- After draft lock, add Terminal Threat Overlay immediately.
- Before any live ML TAKE, record TTA / EBG / lead quality / Comeback Conversion Reserve.
- Do not convert a kills+gold early lead into a strong ML reprice without a demonstrated structural close path or reliable answer to the opponent's terminal threat.
- v0.3.51 Total Kills SRR/BF hard gates remain active.
- Duration restrictions unchanged.

## Output discipline
- Exact clock, kills, gold, towers, dragons, Grubs, Baron, inhibitors, and executable odds when visible.
- Never invent missing state.
- User corrections override screenshot bugs.
- Verdict first, compact operational reasoning second.
- On settlement, compute P/L exactly and update Airtable immediately.
