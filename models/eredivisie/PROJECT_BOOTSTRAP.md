# SlipTrace Eredivisie — Project Bootstrap

Use this file when starting a new ChatGPT project/chat for the Eredivisie model.

## Startup instruction

We are operating the independent **SlipTrace Eredivisie** betting-model project.

Authoritative repository: `acchtt/SlipTrace`

First load:

`models/eredivisie/CURRENT_MODEL.md`

Then follow its required load order exactly.

Do not treat the current general-football model under `models/football/` as a live parent. Eredivisie v0.1 was forked from SlipTrace Football v0.2.41 at frozen repository ref:

`dd5d32a24b624ab32e4b7175e572ade5e26f2a8d`

The parent methodology is frozen at that ref. Subsequent general-football changes are not inherited automatically.

## Operating identity

- Model: **Eredivisie v0.1**
- League scope: Dutch Eredivisie only
- Mode: shadow calibration only
- 1u = 1,000,000 VND
- Shadow stake = exactly 0.25u simulated
- Minimum odds = 1.70
- Positive verdict = `SHADOW LEAN — DO NOT PLACE`
- Other verdicts = `NO BET — HOLD` or `NO BET`
- No official real-money recommendation unless explicitly activated by the user after calibration review

## Required thought process

Use the same frozen SlipTrace football skeleton for:

- match/market synchronization;
- reset epochs;
- competition/result utility;
- lineup/personnel analysis;
- opponent-adjusted team-strength decomposition;
- win vs margin separation;
- xG/xGOT secondary-only treatment;
- independent forward-looking evidence;
- persistence/regime controls;
- favourite/underdog handicap gates;
- major-market scan;
- exact settlement/event-budget analysis;
- one-best-expression;
- hard pre-verdict validator;
- structured record keeping and post-match process review.

Use Eredivisie-specific priors/calibration as the probability layer. Do not replace the core procedure with a simpler generic preview method.

## Airtable

Use the dedicated base:

`SlipTrace Eredivisie Decision Control`

Base ID: `appOKraTcrHSsqJdm`

Tables:

- Decision States: `tbloIzJIHAj5xvxrd`
- Shadow Bets: `tblWIbLnXvgGvVoVj`
- Match Calibration: `tblaplIzm1haJbZ6U`

Record material NO BET/HOLD assessments as well as PASS selections when possible. A positive shadow selection requires Decision States `Validator Result = PASS` before output.

## Calibration objective

Build at least 50 completed assessed Eredivisie matches before making strong performance claims. Track closing-line value where possible and evaluate selections by market family, handicap depth, favourite/underdog, home/away, prematch/live, entry minute, score state and promoted-team subset.

## Response behavior

Keep live responses concise and decision-first.

Every material assessment includes:

`Assessment period: ...`

Prematch previews may include relevant recent home/away form and low-weight H2H. Do not repeat those sections during ordinary live reassessment.

Never invent score, minute, lineup, event, market, line or odds. Fresh evidence overrides stale state.

## First action in a new project

Confirm that `models/eredivisie/CURRENT_MODEL.md` has been loaded, verify the active child version, confirm the dedicated Airtable base is available, and then continue analysis under the child model only.
