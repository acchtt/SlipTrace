# Eredivisie Airtable Decision-State Control

## Base

- Base name: `SlipTrace Eredivisie Decision Control`
- Base ID: `appOKraTcrHSsqJdm`

This base is operational control and calibration storage for the independent Eredivisie model. It is separate from the general-football Airtable base.

## Table 1 — Decision States

- Table ID: `tbloIzJIHAj5xvxrd`
- Purpose: one record per material Eredivisie assessment, including PASS/HOLD/FAIL and NO BET states.
- Hard write lock: a positive shadow selection cannot be emitted unless the corresponding record has `Validator Result = PASS`.

Core fields:

- Assessment ID
- Match
- Season
- Home Team
- Away Team
- Model Version
- Assessment Time
- Minute
- Score
- Reset Epoch
- Assessment Period
- Market Family
- Candidate
- Line
- Odds
- Verdict
- Goal Environment
- Synchronized State
- Reset Resolved
- Competition Utility Verified
- xG Role
- Primary Channels
- Independent Primary Channels
- Favorite/Underdog Gate
- Directional Persistence
- Major Markets Scanned
- Settlement Verified
- Validator Result
- Fail/Hold Reasons
- Evidence Summary

## Table 2 — Shadow Bets

- Table ID: `tblWIbLnXvgGvVoVj`
- Purpose: qualified PASS shadow selections only.

Core fields:

- Shadow ID
- Match
- Season
- Model Version
- Selection
- Line
- Odds
- Stake u
- Entry Minute
- Entry Score
- Result
- Simulated P/L u
- Closing Line
- Closing Odds
- CLV Notes
- Process Validity
- Error Classification
- Review Notes

Do not conflate settlement result with process validity.

## Table 3 — Match Calibration

- Table ID: `tblaplIzm1haJbZ6U`
- Purpose: match-level dataset for the initial 50-match sample and later Eredivisie league-prior estimation.

Core fields:

- Match ID
- Date
- Season
- Round
- Home Team
- Away Team
- Home Promoted
- Away Promoted
- Closing Home AH
- Closing Home AH Odds
- Closing Total
- Closing Over Odds
- HT Score
- FT Score
- Home Goals
- Away Goals
- Red Cards
- Material Assessments
- Shadow Selection
- Closing-Line Captured
- Calibration Notes

## Operational rules

1. Record every material assessment when possible, not only bets.
2. `SHADOW LEAN — DO NOT PLACE` requires a Decision States PASS record first.
3. After PASS, create the corresponding Shadow Bets record with 0.25u simulated stake.
4. At match completion, update match-level calibration and shadow settlement.
5. Capture closing lines where possible to measure CLV.
6. If Airtable is unavailable before a positive candidate, force `NO BET — HOLD — decision-state validation unavailable`.
7. This base does not authorize or record real-money official execution during v0.1 shadow mode.
