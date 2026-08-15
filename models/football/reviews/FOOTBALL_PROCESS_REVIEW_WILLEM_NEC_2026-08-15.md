# Football Process Review — Willem II vs NEC Nijmegen — 2026-08-15

**Competition:** Netherlands Eredivisie  
**Audit mode:** Shadow calibration only  
**Model at time of live assessment:** Football v0.2.44  
**Review purpose:** Process correction only; no retrospective shadow promotion

## Observed sequence

The match remained 0-0 deep into the first half. NEC then scored at 45+2 and led 0-1 at halftime.

The detailed halftime evidence supplied in the live screenshots showed NEC had already built the stronger attacking process before and around the goal, including approximately:

- 68% possession;
- 7 total shots;
- 5 shots on target;
- 2 big chances;
- 20 touches in the opposition box;
- materially stronger final-third occupation and passing control.

xG/xGOT readings were also favorable to NEC, but those remain secondary under the active model.

The synchronized halftime market showed approximately:

- Over 2.5 @ 1.73;
- Over 2.75 @ 1.99;
- Over 3 @ 2.38.

The model did not issue a shadow Over because it remained too dependent on proving Willem II's post-goal chase after NEC's late first-half goal.

NEC subsequently extended the score to 0-2 and then 0-3, and the user later reported 0-4. Those later goals are useful only for diagnosing the process mistake. They do not retroactively create a winning shadow bet.

## Error classification

Primary error:

`EXCESSIVE POST-GOAL CONFIRMATION / TRAILER-CHASE DEPENDENCY`

Secondary error:

`FAILURE TO RECOGNIZE LEADER-DRIVEN REMAINING-GOAL SUFFICIENCY`

Timing context:

`TERMINAL-HALF GOAL — NORMAL POST-GOAL OBSERVATION WINDOW UNAVAILABLE`

## What the model should have asked

The key halftime question was not:

`Will Willem II prove a strong chase before we can consider the Over?`

It was:

`Can NEC plausibly provide the remaining goal budget themselves, and is the synchronized halftime line still priced attractively if Willem contributes little or nothing?`

Given NEC's pre-goal and first-half production, that question was materially more relevant.

## Prospective correction

Football v0.2.45 introduces:

1. a terminal-goal halftime bridge when a late goal leaves too little post-goal live play for the normal v0.2.43 persistence window;
2. carry-forward of strong pre-goal process through the halftime reset when at least three independent primary channels support continuation;
3. explicit `LEADER-DRIVEN OVER` logic;
4. trailer chase classified as ESSENTIAL / HELPFUL / OPTIONAL rather than treated as a universal Over gate;
5. a halftime fast-path when the bridge passes and no material tactical change invalidates the pre-goal regime.

## Audit integrity

- No retrospective shadow selection is created for Willem II vs NEC.
- No profit is added to shadow P/L.
- The later 0-4 state does not prove that every similar halftime Over is good value.
- The correction is retained because the original gate was structurally impossible to satisfy in the available interval and because the leader's own attacking process was already independently strong.
- Future cases must satisfy v0.2.45 prospectively at the synchronized halftime price.