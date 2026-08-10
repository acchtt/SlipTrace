# CURRENT LIVE HANDOFF — LoL — 2026-08-10

## Load order
1. `models/lol/CURRENT_MODEL.md`
2. `models/lol/rules/MODEL_RULES_LOL_V0.3.50.md`
3. `models/lol/procedures/LOL_LIVE_VERDICT_EXECUTION_CHECKLIST_2026-08-10.md`
4. Latest reviews referenced by `CURRENT_MODEL.md`
5. `models/lol/context/lol-v0.3.25/ACTIVE_RULES_CONSOLIDATED.md`
6. `models/lol/context/lol-v0.3.25/PROBATION_STATUS.md`
7. `models/lol/context/lol-v0.3.25/LIVE_ANALYSIS_CALIBRATION_HANDBOOK.md`
8. This handoff last

## Active model
**LoL v0.3.50**

GitHub is model authority. Airtable is canonical map/position ledger.

## Operating state
- Official betting paused until explicit restoration.
- Shadow mode active.
- Default shadow stake: 0.25u.
- Actual exposure: 0u.
- Minimum odds: 1.60.
- Same-map shadow add-ons enabled when each independently qualifies and joint correlation is priced.
- Duration: no pregame TAKE; no TAKE before 12:00.
- A wager is recorded only after explicit user confirmation of the same executable line.
- If a recommended line disappears before confirmation: NO BET / 0u; never grade hypothetical.
- User saying `Final`, `final score`, or `X won` is definitive settlement authority; trust it over buggy UI labels.

## Mandatory response behavior
First visible line on live maps must immediately be one of:
- `TAKE — [selection] @[odds] — shadow 0.25u; actual 0u.`
- `PASS — [market/selection] @[odds] — 0u.`
- `HOLD — [market/selection] @[odds] — 0u.`

Do not delay verdict for Airtable/GitHub work. Reasoning follows verdict.

For open positions, perform position-blind reassessment and state ACTIVE / DEGRADED / INVALIDATED / CONFIRMED.

## Core model logic retained
### Draft primacy
After draft lock, draft is the most important conditional mechanism layer. Evaluate:
1. reliable first contact
2. hard-CC density
3. CC reliability/range
4. anti-engage/disengage
5. frontline access
6. backline access
7. carry protection
8. damage continuation
9. chase/cleanup
10. re-engage/repeat forcing
11. objective/choke control
12. waveclear/base defense
13. side-lane/global numbers creation
14. execution simplicity

Team strength remains the verified pre-draft baseline. Draft does not erase team-strength uncertainty, but it can materially alter map/market expression.

### Kill handicap
- Build one side-neutral signed favorite kill-margin distribution.
- Price both +H and -H from same distribution.
- Explicitly model favorite blowout tail and underdog margin-survival tools.
- Separate map-win probability from handicap-cover probability.
- Structure Substitution: strong map control can expand towers/objectives without expanding kill margin.
- Kill Conversion Velocity (KCV): HIGH / MEDIUM / LOW-STRUCTURE-SUBSTITUTED from synchronized live snapshots.
- Net-Kill Burden (NKB): calculate additional net kills required to beat the line and compare with remaining high-contact windows.
- Handicap calibration lower-bound surcharge remains: +7pp pregame, +6pp early live, +5pp mid/late.

### Total kills — v0.3.50
Do not equate engage capability with realized combat.

Model separately:
1. OKP — Observed Kill Pace
2. FCI — de-duplicated Forward Contact Inventory; count event windows, not champions
3. CRR — Contact Realization Rate for each window
4. CL — Contact Lethality conditional on contact

Use conceptual arithmetic:
`Expected remaining kills = sum[P(contact_i) * E(kills_i | contact_i)] + residual pick/chase kills`

For each major objective/pressure window explicitly test:
- CONTEST
- CONCEDE
- TRADE
- DELAY

Contest Compulsion only applies when concede/trade/delay become strategically unacceptable or mechanically unavailable. Being behind is not enough.

Threat Deterrence: superior engage/zone/siege can REDUCE realized fights because the opponent gives ground before contact.

For Overs, require evidence the opponent can be forced to enter, not merely punished if they enter.

Quiet-start non-persistence: before 15:00, low kills alone cannot strengthen an Under.

Total Kills lower-bound gates:
- +5pp pregame
- +4pp early live
- +3pp mid/late
- additional v0.3.49/v0.3.50 surcharges where applicable, capped at +9pp total over break-even.

### Total kills vs handicap
Project separately:
- `T = total kills`
- `M = signed kill margin`

Possible branches:
- high T / low M = traded fights
- low T / high M = clean one-sided conversion
- low T / low M = structure-heavy controlled map
- high T / high M = true kill cascade

A +kills handicap can win while an Under loses, and vice versa.

### Same-map add-ons
Do not apply a generic correlation penalty. Estimate branches:
- both win
- A only
- B only
- neither

Each add-on must independently clear its own gate after joint-distribution adjustment. No stake escalation.

### Duration
- No pregame TAKE.
- No TAKE before 12:00.
- Normally require >=2 synchronized snapshots >=90 sec apart from 12:00 onward showing same stall/acceleration mechanism.
- Over requires observed stall; Under requires observed acceleration.
- First tower / Baron / inhibitor / major structure or gold swing is a regime-change event requiring reprice.
- Duration and Total Kills are separate.

## Recent calibration lessons
### FURIA vs Fluxo W7M G2
Confirmed Over 24.5 @1.705 lost; final FURIA 14-3, 32:53, 17 kills.
Lesson: engage tools were double-counted as future fights. FURIA control produced threat deterrence, concession, and structure/objective conversion rather than repeated combat. This produced v0.3.50 CRR/concession update.

### KC vs FNC G2
Under 27.5 @1.955 lost by 0.5 kill; FNC +13.5 @2.122 won.
Lesson: quiet early pace does not imply low future contact. Model Total Kills and kill margin separately; add-on correlation is not binary.

### KT.C vs DNS.C G3 — latest settled map
Draft:
KT.C: Rumble / Wukong / Zeri / Jhin / Karma
DNS.C: Ornn / Naafiri / Ryze / Yunara / Lulu

At 5:48: DNS 1-0, +328g, 0-0 towers/dragons/Baron/inhibitors.
Confirmed: **KT.C +7.5 kills @1.864**, 0.25u shadow.
Final: **KT.C won 13-7 at 31:35**, 20 total kills.
Settlement: **WIN +0.2160u**.
Important correction: KT were the underdogs and won outright by 6 kills. +7.5 therefore covered by 13.5 relative to the spread threshold, not by 1.5.
Unconfirmed/passed totals:
- Under 32.5 @1.777 would have won, but line disappeared before confirmation => NO BET.
- Under 29.5 @1.804 was explicitly PASS and would also have won => NO BET.
Calibration: v0.3.50 low-CRR/concession read was directionally correct; do not weaken safety gates from one unplaced winner.

## Current live state
No open position carried from KT.C-DNS.C G3. Last confirmed position is settled.

## Output discipline
- Exact clock, kills, gold, towers, dragons, Grubs, Baron, inhibitors, and executable odds when visible.
- Never invent missing state.
- User corrections override screenshot bugs.
- Verdict first, concise operational reasoning second.
- On settlement, compute P/L exactly and update Airtable immediately.
