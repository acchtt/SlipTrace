# CURRENT LIVE HANDOFF — 2026-08-13

## Active model

**LoL v0.3.55**

GitHub is model/rules authority. Airtable is canonical map/position ledger.

Official betting remains **paused**. Shadow mode is active.

- Default shadow stake: 0.25u
- Actual exposure: 0u
- Minimum odds: 1.60
- Pregame/immediate post-draft ML/KH/TK TAKEs: disabled
- Live ML/KH/TK: two synchronized live snapshots plus all retained gates
- Shadow TAKEs: auto-record after visible verdict when executable and qualified; no confirmation required
- Duration restrictions unchanged

## Mandatory live output behavior

For every active-map screenshot, the first visible line must be the verdict:

- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [selection/market] @[odds] — 0u.`
- `HOLD — [selection/market] @[odds] — 0u.`

Do not delay the visible verdict for Airtable/GitHub/tool work. Logging occurs after the verdict.

## v0.3.55 correction — draft execution is mandatory

v0.3.55 was promoted after KT Challengers vs NS Challengers Game 1 exposed a process-enforcement failure.

Reference review:
`models/lol/reviews/KT_NS_G1_DRAFT_EXECUTION_BURDEN_REVIEW_2026-08-13.md`

Reference rules:
`models/lol/rules/MODEL_RULES_LOL_V0.3.55.md`

Mandatory additions before live ML/KH/TK TAKE:

- complete Draft Function Matrix;
- classify Draft Execution Reliability (DER) for both sides: LOW / MEDIUM / HIGH burden;
- count forcing and survival **shared-failure clusters**, not champion abilities;
- apply objective-schedule x execution-burden interaction;
- for underdog +kills, run Resilience Independence Test (RIT);
- scoreboard parity/two snapshots are not mechanism proof by themselves;
- if favorite has repeatable independent forcing and underdog margin-saving mechanisms are coupled/high-burden with future forced windows remaining, underdog +kills defaults PASS/HOLD until live mechanism proof appears;
- blocking underdog +kills does not automatically make favorite -kills a TAKE.

A user correction to champion identity, role assignment, or draft difficulty triggers a full position-blind Draft Function Matrix + DER + shared-failure rerun, not a cosmetic adjustment.

## Current series — KT Challengers vs NS Challengers

Competition: LCK Challengers League 2026 Rounds 3-4  
Series state: **KT Challengers lead 1-0** after Game 1.

### Game 1 draft

KT.C:
- Olaf
- Vi
- Cassiopeia
- Ashe
- Seraphine

NS.EA:
- Gnar
- Xin Zhao
- Anivia
- Ezreal
- Blitzcrank

Initial support correction: NS support was Blitzcrank, not Nautilus.

### Game 1 shadow position

`LCKCL-2026-08-13-KTC-NS-G1-P01`

- Market: Kill Handicap
- Selection: NS.EA +8.5 kills
- Odds: 1.943
- Shadow stake: 0.25u
- Actual exposure: 0u
- Entry clock: 15:28
- Result: **LOSS -0.25u**
- Thesis: invalidated before settlement, then settled

Entry state:
- KT 3-2 NS;
- NS about +108g;
- towers 0-0;
- KT 2-0 dragons;
- mixed role economy.

The position was a model-process error: NS's draft burden/shared-failure structure was underweighted.

### Game 1 final user-authoritative result

KT Challengers won.

Latest grading frame at 29:50:
- KT 19-5 NS;
- KT +14k gold;
- towers 10-0;
- dragons 4-0;
- Baron 1-0;
- inhibitors 2-0.

Do not infer exact final duration from the 29:50 grading frame unless separately supplied.

## Current shadow validation

After settling NS +8.5:

- Record: **6-6**
- Net: **-0.14850u**
- Open shadow positions: **none**

## Immediate next action

Prepare **KT.C vs NS.EA Game 2** with fresh-map evidence reset.

Do not carry Game 1 scoreboard state into Game 2. Series execution evidence may inform TEAM, but draft remains the primary post-lock mechanism layer.

For Game 2, pay special attention to:

- execution simplicity / DER;
- independent first-contact routes;
- shared-failure clusters;
- objective-setup burden;
- underdog +kills RIT;
- role-weighted economy when visible;
- position-blind reassessment after material state changes.
