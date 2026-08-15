# Football Process Review — Willem II vs NEC Nijmegen — 2026-08-15

**Competition:** Netherlands Eredivisie  
**Audit mode:** Shadow calibration only  
**Model at time of live assessment:** Football v0.2.44  
**Review purpose:** Process correction only; no retrospective shadow promotion

## User correction — primary missed window

The initial review framed the error too heavily around the 45+2 NEC goal and the halftime 0-1 state.

The user corrected the sequence: **around 42' at 0-0, NEC had already increased pressure.** That pre-goal acceleration was the more important missed decision window.

The synchronized live board around that stage showed approximately:

- Over 1.75 @ 1.84;
- Over 2.0 @ 2.20;
- Over 1.5 @ 1.62.

No prospective shadow verdict was issued before the goal.

Therefore the primary error is now classified as:

`LATE — PRE-GOAL PRESSURE INFLECTION NOT CONVERTED TO DECISION`

The halftime issue remains real but secondary.

## Observed sequence

The match remained 0-0 deep into the first half. During the late-first-half interval, NEC's forward pressure increased before scoring at 45+2.

At halftime, the detailed evidence supplied in the screenshots showed NEC had become the materially stronger attacking side, including approximately:

- 68% possession;
- 7 total shots;
- 5 shots on target;
- 2 big chances;
- 20 touches in the opposition box;
- materially stronger final-third occupation and passing control.

xG/xGOT readings were also favorable to NEC, but those remain secondary under the active model.

The synchronized halftime market then showed approximately:

- Over 2.5 @ 1.73;
- Over 2.75 @ 1.99;
- Over 3 @ 2.38.

The model did not issue a shadow Over either before the goal or at halftime.

NEC subsequently extended the score and the user later reported 0-4. Those later goals are useful only for diagnosing the process mistake. They do not retroactively create a winning shadow bet.

## Corrected error classification

Primary error:

`LATE — PRE-GOAL PRESSURE INFLECTION NOT CONVERTED TO DECISION`

Secondary errors:

- `EXCESSIVE CONFIRMATION / WAITING FOR SCOREBOARD VALIDATION`;
- `TRAILER-CHASE DEPENDENCY`;
- `FAILURE TO RECOGNIZE ONE-TEAM / ATTACKER-DRIVEN REMAINING-GOAL SUFFICIENCY`.

Post-goal fallback issue:

`TERMINAL-HALF GOAL — NORMAL POST-GOAL OBSERVATION WINDOW UNAVAILABLE`

## What the model should have asked around 42'

The first relevant question was not:

`Will Willem II chase after conceding?`

There was no trailer yet.

It was:

`Has NEC's current attacking regime accelerated enough that the protected live Over is already the best expression before the first goal?`

That requires interval-delta evidence, not merely cumulative match totals.

If the pre-goal gates cleared, v0.2.44 required immediate verdict-first delivery. Waiting for the first goal would have been a confirmation tax.

## Prospective correction

Football v0.2.46 introduces:

1. a mandatory late-half pressure-acceleration scan from roughly 35' onward;
2. explicit recent-interval comparison rather than cumulative-stat anchoring;
3. `PRESSURE INFLECTION` classification;
4. an `ATTACKER-DRIVEN PRE-GOAL OVER` branch for one-team attacking surges at tied scores;
5. no requirement for a future trailer chase when the protected total can be funded by the attacking team;
6. mandatory adjacent low-total comparison when opponent goal contribution is uncertain;
7. immediate v0.2.44 delivery when the pre-goal gates are complete.

Football v0.2.45 remains active as a secondary fallback after a genuinely terminal goal when no honest post-goal observation window exists.

## Audit integrity

- No retrospective shadow selection is created for Willem II vs NEC.
- No profit is added to shadow P/L.
- The around-42' Over 1.75 state is logged only as a missed synchronized decision state.
- The later 0-4 score does not prove that every similar late-half Over is good value.
- Future cases must satisfy v0.2.46 prospectively at the synchronized pre-goal price.
- If a goal arrives before delivery, the old state is `STATE-CHANGE RACE — NOT COUNTED` and must be repriced.