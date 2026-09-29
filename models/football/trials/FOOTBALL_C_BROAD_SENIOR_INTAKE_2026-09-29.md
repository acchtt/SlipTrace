# Football C Broad-Senior Intake Trial

**Status:** ACTIVE PROCEDURE TRIAL  
**Started:** 2026-09-29 ICT  
**Model:** Football C

## Change

Replace legacy narrow-core Step-0 filtering with complete broad-senior intake before Football C screening.

## Hypothesis

The old Step-0 prefilter can create false negatives by removing reasonable senior fixtures before Football C sees them.

Broad intake should improve coverage without simply inflating the betting board because C still independently C-PASSes weak fixtures.

## Frozen intake rule

- enumerate every reasonable senior first-team fixture in the requested AiScore window;
- apply only hard non-production/identity/time exclusions;
- send every survivor to Football C;
- persist every C-PASS/WATCH/FOCUS result.

Do not reintroduce PRIORITY/NORMAL/CONDITIONAL, LOW-GOAL, country-wide, professional-lower-division or small-cup exclusions at Step 0.

## Measurement

For each new board:

`RAW SENIOR -> HARD EXCLUDED -> ADMITTED TO C -> C-PASS -> C-WATCH -> C-FOCUS -> C-BET/C-WAIT`

After FT inspect high-scoring C-PASS false negatives, low-scoring C-FOCUS false positives, missing senior fixtures, C-BET/C-WAIT settlement, board size/followability and processing time.

## Discovery example

The user's 20:00 Africa Cup of Nations qualification block on 2026-09-29 motivated this change. It is discovery evidence only and does not count as prospective validation.

## Rollback

`archive/pre-football-c-broad-senior-intake-2026-09-29`
