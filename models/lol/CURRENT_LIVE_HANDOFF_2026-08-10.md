# CURRENT LIVE HANDOFF — LoL — 2026-08-10

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.51.md`
3. retained deltas v0.3.50 through v0.3.26
4. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
5. latest reviews referenced by `CURRENT_MODEL.md`
6. v0.3.25 baseline context/calibration files
7. connected-stack / scoreboard / stake procedures
8. This handoff last

## Active model
**LoL v0.3.51**

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

### Kill Handicap
Use a position-blind signed kill-margin distribution, NKB, RFI, KCV and Structure Substitution. Map dominance is not kill-margin dominance. Price +H and -H symmetrically.

### Total Kills — v0.3.51
Model separately:
1. OKP — Observed Kill Pace
2. FCI — de-duplicated objective/event Forward Contact Inventory
3. CRR — Contact Realization Rate
4. SRR — Skirmish Recurrence Reserve between formal windows
5. CL — Contact Lethality conditional on contact

Conceptual projection:
`Final kills = current kills + CRR-weighted FCI kills + SRR kills + residual terminal/pick/chase kills`

#### Hard pre-12:00 Under gate
Before 12:00, an Under cannot be TAKEN mainly from low current kills or a large cushion.
Require one of:
- two synchronized live snapshots >=90 sec apart showing low OKP and stable/declining contact pressure;
- repeated contact already demonstrating LOW CL through functioning disengage/peel/reset;
- an observed near-terminal structure-only branch removing future contact windows.

One live snapshot + functional repeatable hard access => HOLD/PASS.

#### SRR
Classify LOW / MEDIUM / HIGH from vision/jungle collisions, lane-transition catches, side collapses, roam contact, post-reset re-engage and repeatable neutral picks. Do not count engage champions as independent fights.

#### Bidirectional Forcing
If both teams can independently start meaningful contact without a voluntary objective-choke entry, BF is ACTIVE. Raise SRR/high-total branch unless live evidence suppresses it.

#### Threat Deterrence
Classify GLOBAL / LOCAL / NONE. Poke/zone control is only LOCAL if the opponent can bypass it through flank, fog, dash, displacement, point-click engage or transition timing.

#### Under cushion stress test
Calculate current kills, max additional kills that still win, kills required to lose, remaining time range and whether repeated 2-4 kill skirmishes plus objective/base fights can plausibly cross the line.

### Same-map Total Kills + handicap
Project `T` and `M` separately and price all four joint cells. HIGH SRR/BF materially raises the high-T / low-M branch; a strong +kills position does not imply an Under.

### Duration
No pregame TAKE; none before 12:00. 12:00-13:59 requires two synchronized snapshots >=90 sec apart showing same observed mechanism. 14:00+ still requires observed stall/acceleration. Reprice after regime changes.

## Latest settled series — HLE.C vs GGA

### Game 1
Confirmed shadow: **GGA +9.5 kills @1.802**, 0.25u.
Final: GGA won 23-14 at 34:12.
Settlement: **WIN +0.2005u**.

### Game 2
Draft:
GGA blue — Jayce / Skarner / Syndra / Varus / Leona
HLE.C — Yorick / Lee Sin / Annie / Jhin / Alistar

Confirmed standalone shadow positions:
1. **GGA +7.5 kills @2.082**, 0.25u — WIN +0.2705u.
2. **Under 33.5 kills @1.690**, 0.25u — LOSS -0.25u.

Final: GGA won 20-15 at 30:30, 35 total kills.
Net Game 2 shadow P/L: **+0.0205u**.

User settlement note: many skirmishes occurred.

### v0.3.51 correction from Game 2
The Under was a process/model error:
- early confirmation hard gate should have failed;
- SRR was HIGH;
- Bidirectional Forcing was active;
- Threat Deterrence was only LOCAL;
- high-T / low-M branch was underweighted.

Review: `models/lol/reviews/HLE_GGA_G2_UNDER_SKIRMISH_RECURRENCE_REVIEW_2026-08-10.md`.

## Current live state
No open positions. HLE.C-GGA series is complete 2-0 GGA.

## Next target
LEC 2026 Summer Week 3: **SK Gaming vs Team Vitality**, scheduled 2026-08-10 15:00 UTC / 17:00 CEST / 22:00 ICT, Bo3 Fearless Draft.

Expected current rosters pending lobby confirmation:

SK: Wunder / Skeanz / SlowQ / Jopa / Mikyx
VIT: Naak Nako / Lyncas / FIESTA / Carzzy / Fleshy

Pre-draft process:
- Treat roster/lobby confirmation as mandatory.
- Team-strength prior favors VIT but do not convert it into a kill-margin edge before draft.
- Re-run Draft Primacy from scratch each game because Fearless Draft changes available mechanisms across the series.
- v0.3.51 early Under gate is active immediately.
- If both drafts have reliable independent contact starters, mark BF and SRR before any Total Kills verdict.

## Output discipline
- Exact clock, kills, gold, towers, dragons, Grubs, Baron, inhibitors, and executable odds when visible.
- Never invent missing state.
- User corrections override screenshot bugs.
- Verdict first, compact operational reasoning second.
- On settlement, compute P/L exactly and update Airtable immediately.
