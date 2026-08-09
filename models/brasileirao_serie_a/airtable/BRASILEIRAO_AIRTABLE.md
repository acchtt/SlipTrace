# Brazilian Serie A Airtable Control

Dedicated operational base for the independent child model.

## Base

- Name: `SlipTrace Brazilian Serie A Decision Control`
- Base ID: `appsqiBbCMEKKLqgG`

## Tables

### Decision States

Table ID: `tblrTzhQhW6CND7SE`

Purpose: one record per material prematch/live assessment, including NO BET and HOLD states. A positive shadow selection is forbidden unless the corresponding record has `Validator Result = PASS`.

Important fields include:

- Assessment ID, Match, Season, Home Team, Away Team, Model Version
- Assessment Time, Minute, Score, Reset Epoch, Assessment Period
- Market Family, Candidate, Line, Odds, Verdict, Goal Environment
- Synchronized State, Reset Resolved, Competition Utility Verified
- xG Role, Primary Channels, Independent Primary Channels
- Favorite/Underdog Gate, Directional Persistence
- Major Markets Scanned, Settlement Verified
- Validator Result, Fail/Hold Reasons, Evidence Summary

Primary-channel choices additionally include `Serie A Prior` and `Rest/Travel/Congestion`.

### Shadow Bets

Table ID: `tbl8qeAvOeDjvZAr6`

Purpose: qualified shadow selections only.

Track exact selection, line, odds, 0.25u stake, entry state, result, simulated P/L, closing line/odds, CLV, process validity, error classification and review notes.

Outcome and process validity are separate fields.

### Match Calibration

Table ID: `tblYVM3KHohv4oVHL`

Purpose: the match-level 50-match calibration dataset and later league-prior estimation.

Track:

- date, season, round, teams;
- promoted-team flags;
- home/away rest days;
- midweek continental involvement;
- closing AH and total;
- HT/FT score;
- red cards;
- material assessment count;
- shadow-selection flag;
- closing-line capture flag;
- travel/climate/congestion notes;
- calibration notes.

## Write rules

1. Record material assessment states, including NO BET/HOLD, whenever operationally possible.
2. Before any `SHADOW LEAN — DO NOT PLACE`, Decision States must exist with `Validator Result = PASS`.
3. Then create exactly one corresponding primary Shadow Bets record for that selection.
4. Do not create a shadow record for NO BET/HOLD.
5. Match Calibration is one row per assessed Serie A match, updated through completion.
6. Avoid duplicate Assessment IDs, Shadow IDs and Match IDs.
7. Airtable is the child operational/calibration record; it is not permission to write the general football ledger.

## Availability lock

If the dedicated Airtable decision-state write is unavailable, the child model must return:

`NO BET — HOLD — decision-state validation unavailable`

Do not bypass the lock.
