# J1 League Fork Manifest

## Identity

- Child model: **J1 League v0.1**
- Namespace: `models/j1_league/`
- Parent model: SlipTrace Football v0.2.41
- Frozen parent repository ref: `9090f5bcb7bc0d8a67a1c308766801c9d40fd03a`
- Fork mode: independent child after creation

## Fork rule

The J1 model inherits the parent football decision-process skeleton at the frozen ref. It does **not** continuously inherit future changes under `models/football/`.

A future parent rule may enter the J1 model only after:
1. explicit review for J1 relevance;
2. conflict analysis against J1-specific rules/data;
3. a documented child-model version change.

This prevents changes learned from unrelated competitions from silently contaminating the J1 experiment.

## Inherited methodology

At the frozen ref, inherit the complete Football v0.2.41 loading chain, including the organized loading guide, retained legacy baseline, main procedure/addendum, v0.2.5 through v0.2.41 rule layers, hard pre-verdict validator, and decision-state discipline.

Core controls retained include:
- state synchronization;
- reset epochs;
- competition/result utility;
- lineup and personnel decomposition;
- opponent-adjusted attack/defense assessment;
- win/draw/margin separation;
- xG/xGOT secondary-only role;
- independent primary evidence channels and correlation control;
- persistence and regime classification;
- deep-favorite/protected-underdog gates;
- exact AH and total settlement;
- full major-market scan;
- one-best-expression;
- pre-verdict validation and write lock;
- post-match process/error review.

## J1-specific ownership

The child owns its own priors and learned rules for:
- home advantage and venue/stadium effects;
- home/away scoring/conceding profiles;
- handicap-band performance;
- draw and clean-sheet tendencies;
- favorite multi-goal margin rates;
- underdog margin suppression;
- total-goal distributions;
- live scoring hazard by minute/score state;
- promoted teams;
- domestic travel and rest asymmetry;
- summer heat/humidity and weather effects;
- Emperor's Cup / J.League Cup / AFC congestion and rotation;
- club tactical profiles;
- market movement and CLV.

## Dataset boundary

Calibration population: J1 League matches only.

Do not blend J2, J3, Emperor's Cup, J.League Cup, AFC competitions, friendlies, youth/reserve or national-team matches into J1 calibration. Those may be contextual evidence only and must be labelled as such.

## Execution boundary

The child starts in shadow-only calibration mode. No real-money official betting is enabled by this fork.

## Starting state

- Assessed matches: 0/50
- Qualified shadows: 0
- Official betting: disabled
