# J1 League Airtable Decision Control

## Base

- Name: `SlipTrace J1 League Decision Control`
- Base ID: `appJjh5NphXnklhqy`

## Tables

### Decision States
- Table ID: `tblGgAWoilpcAQ0Bm`
- Purpose: one record per material assessment; mandatory hard write before any positive shadow verdict.
- Key fields include assessment/match identity, season, home/away, model version, time/minute/score, reset epoch, assessment period, market family, candidate, line, odds, verdict, goal environment, synchronization/reset/utility checks, xG role, primary channels, independent-channel count, favorite/underdog gate, persistence, market scan, settlement verification, validator result, fail/hold reasons and evidence summary.

### Shadow Bets
- Table ID: `tbljpHcxNaRn6Jzmv`
- Purpose: validator-PASS J1 shadow selections only.
- Key fields include match/model identity, selection/line/odds, simulated stake, entry minute/score, result, simulated P/L, closing line/odds, CLV notes, process validity, error classification and review notes.

### Match Calibration
- Table ID: `tblWRt0GoTsgbL0hQ`
- Purpose: match-level population for the initial 50-match sample and later J1 prior estimation.
- Key fields include date/season/round, teams, promoted status, rest days, midweek cup/AFC flags, closing AH/total, HT/FT score, goals, red cards, assessment count, shadow-selection flag, closing-line capture, travel/weather/congestion notes and calibration notes.

## Write lock

Before `SHADOW LEAN — DO NOT PLACE`:
1. complete the J1 pre-verdict validator;
2. write/update Decision States;
3. require `Validator Result = PASS`;
4. write Shadow Bets with exactly 0.25u simulated stake.

If the Decision States write cannot be completed, do not bypass the control. Output `NO BET — HOLD — decision-state validation unavailable`.

## Record philosophy

Airtable is the operational research/control layer for this child model. Record NO BET decisions to avoid selection bias. Outcome and process validity are separate fields; never rewrite pre-bet reasoning after the result.

## Starting state

- Assessed J1 matches: 0/50
- Qualified shadows: 0
- Official betting: disabled
