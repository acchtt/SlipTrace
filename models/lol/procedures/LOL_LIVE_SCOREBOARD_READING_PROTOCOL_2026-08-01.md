# LoL Live Scoreboard Reading Protocol — 2026-08-01

**Status:** Active immediately  
**Purpose:** Prevent stale-state carryover and missed objective information when reading live or final LoL screenshots.

## 1. Current-frame rule

Every screenshot must be read as a new synchronized state. Do not reuse a prior clock, score, gold, tower count, dragon count, Void Grub count, Baron count, or player state unless it is independently reconciled with the new frame.

If the frame conflicts with an earlier state, the current frame controls and the prior recommendation is `EXPIRED — REASSESSMENT REQUIRED`.

## 2. Mandatory state fingerprint

Before evaluating any market, extract the following from the current frame when visible:

1. Event and map number.
2. Team identity and left/right side.
3. Game clock.
4. Kill score.
5. Team gold and gold difference.
6. Tower score.
7. Dragon score for each team.
8. Void Grub score for each team.
9. Herald, Baron, Elder, soul, or soul-point state.
10. Active major-objective buffs when visible.
11. Player levels, KDA, CS, completed items, meaningful components, and relevant defensive actives.
12. Current market line and odds from the synchronized bookmaker image.

The compact live state line should normally include at least:

`clock | kills | gold | towers | dragons | grubs | Baron/Elder/soul state`

## 3. Objective icons are decision-critical

Dragon and Void Grub icons are mandatory, not optional context.

- Read objective counts separately for each team.
- Distinguish current objective counts from achievement labels such as first blood, first tower, first dragon, or first Baron.
- Distinguish the Void Grub count from dragon icons and other neutral-objective symbols.
- Do not infer the objective score from prior messages when it is visible in the current image.
- If an icon cannot be identified reliably, state `OBJECTIVE STATE UNKNOWN`.

When objective state can materially affect soul timing, forced contests, Baron conversion, duration, kill totals, moneyline, or kill handicap, an unknown objective state blocks an `OFFICIAL BET`.

## 4. Multi-image synchronization

When the user supplies multiple screenshots:

- identify the timestamp on each image;
- use the newest complete state for the verdict;
- use an older image only to fill a field that cannot have changed between timestamps, such as draft identity, unless explicitly reconciled;
- do not combine odds from one timestamp with game state from another without stating the mismatch;
- a material mismatch requires `NO BET — STATE CONFLICT` until synchronized.

## 5. Final-scoreboard reading

For a final scoreboard, record:

- winner;
- final game time;
- final kills;
- final gold;
- final towers;
- final dragons;
- final Void Grubs;
- final Barons and Elder if shown;
- whether the reviewed selection won or lost and by what margin.

Cross-check the team KDA totals against the displayed kill score when player data are visible.

## 6. Verdict-speed integration

The mandatory state fingerprint must not delay the actionable first line.

Use this order:

1. Extract the synchronized fingerprint.
2. Apply hard vetoes and decisive gates.
3. Output `OFFICIAL BET`, `LEAN`, or `NO BET` immediately.
4. Put stake, odds floors, and `Status: not placed` on the next line for an official recommendation.
5. Add only the decisive evidence.
6. Complete the expanded item and market audit afterward when needed.

## 7. Logged correction

The GX vs SK Game 1 final screenshot was initially misread by carrying forward an earlier 32:42 state and omitting dragons and Void Grubs. The corrected final state was:

- SK won at 42:00;
- SK 19-15 GX kills;
- SK 84.5k-79.3k GX gold;
- SK 6-5 GX towers;
- SK 4-2 GX dragons;
- GX 3-0 SK Void Grubs;
- SK 1-0 GX Barons.

This is classified as a state-extraction defect. Future reads must explicitly include dragons and Void Grubs whenever displayed.

## 8. User same-message synchronization override — 2026-08-26

**Status:** Active immediately for this project/user workflow and supersedes Section 4 where conflicting.

When the user supplies a scoreboard screenshot and sportsbook/market screenshot in the **same message**, treat them as a synchronized live evidence bundle by default.

- Do **not** reject or delay certification merely because an in-app sportsbook clock, feed clock, capture clock, device status-bar time, or embedded display time differs from the scoreboard clock.
- For this workflow, bookmaker/header clock differences are not independent evidence of desynchronization.
- The user's same-message pairing is an explicit provenance signal that the screenshots belong to the same decision state.
- Only override that synchronization presumption when there is a **substantive state contradiction** that cannot coexist in one decision state, such as incompatible kill score, tower/objective count, map number, team identity, or the user explicitly says one frame is stale/old/expired.
- When no substantive contradiction exists, immediately run all applicable model gates using the scoreboard as the factual game-state source and the paired sportsbook screenshot as the executable price source.
- Do not spend live-action time requesting same-state confirmation for a same-message pair.

Logged calibration incident: KT Rolster vs HANJIN BRION Game 2 on 2026-08-26. A valid same-message pair was incorrectly held because the sportsbook header/feed time differed from the scoreboard clock; the delay caused BRO +11.5 @1.998 to disappear before execution. Correct handling is to accept the pair as synchronized and decide immediately.