# Football v1.0 — Chat Handoff — 2026-09-03 08:24 ICT

This handoff preserves the live operational state at the end of the current chat so the next chat can continue without resetting model behavior or history.

## 1. Active model / regime

- Official model: **Football v0.2.47-R — PRE-HARDENING**.
- Sep 1 hardened framework remains **INACTIVE** for official selection.
- Do not silently revive:
  - reserve/youth A1 cap;
  - O3.75 exceptional hard gate;
  - A2 O3.5+ prohibition;
  - XI-names-cannot-create-route prohibition;
  - mandatory H2H de-weighting.
- Hardened analysis may appear only as explicitly labelled **SHADOW — HARDENED**, with no effect on shortlist, XI rerank, line choice, or official lock.
- Canonical active files remain:
  1. `models/football/CURRENT_MODEL.md`
  2. `models/football/rules/MODEL_RULES_FOOTBALL_V0.2.47-R.md`
  3. `models/football/procedures/FOOTBALL_BETTING_PROCEDURE.md`
  4. `models/football/airtable/FOOTBALL_DECISION_STATE_AIRTABLE.md`

## 2. Current active calibration added in this chat

### Recent-total / leakage confirmation rule

After Thun–Lausanne finished 0-0, the active model gained a narrow calibration:

- extreme recent high-total runs or repeated defensive leakage may identify a candidate but cannot by themselves complete an A1/A2 proof;
- before top-board promotion or an official lock, require supporting evidence that every scoring route needed by the proposed total is producing repeatable good chances;
- acceptable support includes multi-match big chances, central/box access, box touches, SOT quality, xG/xGOT trends, or stable multi-goal production/concession patterns beyond one anomalous scoreline;
- if a needed secondary route is weak/unproven, reduce priority, choose a more protected line, or HOLD;
- if detailed chance data is unavailable, reduce confidence rather than inventing it.

This is **not** a return to Sep-1 hardening.

GitHub commits that added this calibration earlier in the chat:
- `93cf0a80`
- `a17716ee`
- `3780741c`

## 3. Current cup / competition scope — IMPORTANT CORRECTION

The final corrected active cup scope is:

### INCLUDED / eligible for normal official workflow
- **All English domestic cups**, including:
  - FA Cup
  - EFL / Carabao Cup
- **Germany DFB-Pokal**
- **North American Leagues Cup (MLS / Liga MX)**

### EXCLUDED
- other domestic cups;
- other domestic League Cups (e.g. J.League / Levain Cup, Scottish League Cup, Portuguese League Cup, etc.);
- European / continental cup competitions unless explicitly added later;
- K League remains permanently excluded.

Safeguard: **North American Leagues Cup is a named exception and must not be removed by a generic “League Cup” filter.**

This scope correction supersedes the mistaken temporary rule that excluded every League Cup.

GitHub commits for the corrected cup scope:
- `4ebfef5d`
- `047020ad`
- `4a0aa97b`

Airtable control row:
- `MODEL-CONTROL-20260903-CUP-SCOPE-CORRECTION`
- record `recP3tTuGsL3jkEAi`

## 4. Latest completed official results / audits

### Grasshopper–St. Gallen
- Official lock: **O3.25 @1.79**
- FT: **2-0**
- Settlement: **LOSS -1.00u**
- User later supplied full stats:
  - combined xG **4.03**
  - shots **43**
  - SOT **12**
  - big chances **5**
- Audit: **SOUND / variance-heavy loss**. The Over environment existed; conversion failed. Do not change model because of this result alone.

### Salzburg–Rapid Wien
- Official lock: **O3.25 @1.84**
- FT: **4-1**
- Settlement: **WIN +0.84u**
- A1 thesis validated cleanly.

### Thun–Lausanne
- Official lock: **O3 @1.92**
- FT: **0-0**
- Settlement: **LOSS -1.00u**
- User later supplied full stats:
  - combined xG **2.44**
  - shots **32**
  - SOT **8**
  - big chances **2**
  - Thun xG **1.58**
  - Lausanne xG **0.86**
  - Lausanne **0 big chances**
- Audit: **structural overgrade**. Recent high-total / leakage run was overweighted; this directly produced the new confirmation rule above.

Net across those three: **-1.16u**.

## 5. This morning board / current match states

### Deportes Limache–Ñublense
Frozen board state:
- competition: Chile Primera División
- frozen grade: **A2 Two-Sided — MAIN MORNING FOCUS**
- recent score profile used in freeze:
  - Limache: 3-1 O'Higgins, 1-3 Universidad de Chile, 3-1 Huachipato, 0-3 Everton
  - Ñublense: 2-2 Audax, 2-1 La Calera, 2-1 Universidad Católica, 0-1 Deportes Concepción

User sent lineup + odds screenshots just after kickoff.
XI read:
- Limache retained Arturia with Morales / Castro support;
- Ñublense started Molina Canto, Jeraldino, Ovelar;
- chance-quality confirmation was judged sufficient rather than relying only on recent scorelines.

Just-kicked grace applied because it was ~1', 0-0, no material event, no meaningful live evidence.

**OFFICIAL LOCK — Deportes Limache–Ñublense O2.75 @2.00**
- exactly 3 = half win
- 4+ = full win
- O3 @2.31 was rejected as unnecessary extra burden.

Airtable:
- PRE `recVhuFPFteVsb7i8`
- XI `recN5biA2yTjWeMH5`
- LOCK `reczUwNQwyufnFWTN`

At handoff time this bet has **not yet been settled in this chat**.

### Barcelona SC–Independiente del Valle
Morning list originally gave the wrong kickoff as 08:00 ICT. User corrected that the match had already started.

Important integrity correction:
- actual kickoff was **07:00 ICT**;
- the earlier supposed 07:15 “PRE” freeze was actually post-kick and therefore **invalid as a legitimate prematch freeze**;
- preserve the erroneous row for audit history, but do not pretend it was a valid freeze.

Normal workflow verdict:
- **NO BET — HOLD**
- can only be assessed now as **MANUAL LIVE OVERRIDE** if the user explicitly activates it and supplies current stats + live market.

Airtable:
- mistaken PRE row `recV5YtQrCpcyNnn4`
- timing correction `recQaJcmTrdQHZpoG`
- live validation pending row `recpNoh744rAHnguu`

### Real Estelí–San Marcos
- Morning freeze: **B+/A2 Elite Carrier watch — Estelí**
- Secondary only.
- Estelí recent 5-0 win alone must not drive promotion under the new confirmation rule.
- No official lock yet in this chat.
- PRE row `rec7AfzFBWW0ilD86`

## 6. Board/list behavior still active

When user asks “list matches / upcoming / today”:

1. scan full relevant ICT slate;
2. apply competition scope first;
3. use **PRE-HARDENING v0.2.47-R** only;
4. apply the recent-total/leakage confirmation rule where relevant;
5. aggressively shorten to the best 3–5 Over-friendly focus matches;
6. do not omit earlier kickoff blocks;
7. freeze structural grade before XI;
8. confirmed XI is first legitimate rerank gate;
9. choose Asian total only after structure/XI;
10. any affirmative final selection is automatically an **OFFICIAL LOCK**;
11. PASS / HOLD = no bet;
12. never rewrite history after result.

## 7. Live behavior

- Normal live analysis can only validate or invalidate a legitimate frozen prematch thesis.
- It cannot create/promote an unrelated unfrozen match after kickoff.
- Manual live override is allowed only when explicitly activated and must be labelled.
- Competition exclusions still apply to manual live overrides.
- Just-started grace is allowed only at 0-0, no material event, no meaningful live evidence, and market effectively still pre-kick.

## 8. Persistent data / accounting

Airtable remains mandatory for material official states:
- base: **SlipTrace Football Decision Control**
- baseId `appWyZJjitSBATXAU`
- table: **Decision States**
- tableId `tblQmUpd5WjBLQ38X`

Search Airtable first before reconstructing betting history / official P&L.

Historical Aug 1–30 audit remains:
- 32 official locks
- 19 full wins
- 4 half-wins
- 2 pushes
- 7 losses
- **+10.995u**
- ROI **+34.359%**
- Airtable monthly audit `rechAKb830UpuvfQ7`

## 9. Latest unfinished user request — DO THIS FIRST IN NEXT CHAT

Immediately before asking for this handoff, the user said:

**“Reassess na league cups matched”**

Interpret this as: reassess **North American Leagues Cup matches** under the corrected active competition scope.

Important: NA Leagues Cup is now **officially eligible**, not shadow-only. Run a fresh web scan for the relevant/current Leagues Cup slate in ICT, then apply the normal active pre-hardening workflow and aggressively shorten to the best Over-friendly candidates.

## 10. Tone / response style

- compact, operational, table-first;
- no generic betting lectures;
- structural ranking first, price last;
- distinguish screenshot-confirmed vs web-confirmed;
- if user sends lineup/odds screenshots, assess immediately through frozen grade → XI rerank → profile/chance gate → failure mode → line/price → LOCK/HOLD.

This handoff is continuity only. The canonical active model files remain the source of truth for model behavior.
