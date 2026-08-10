# SK Gaming vs Team Vitality Game 1 — Terminal Threat Answerability Review

**Date:** 2026-08-10  
**Model at entry:** LoL v0.3.51  
**Market:** SK moneyline @1.752  
**Shadow stake:** 0.25u  
**Result:** LOSS (-0.25u)

## Draft

SK Gaming: Gnar / Jarvan IV / Ryze / Varus / Shen  
Team Vitality: Rumble / Pantheon / Viktor / Corki / Bard

## Entry state

At 12:50:

- SK 5-2 VIT;
- SK +1.6k gold;
- towers 0-0;
- VIT 1-0 dragons;
- Grubs SK 2-1 VIT;
- no Baron / inhibitors.

Confirmed shadow position: **SK ML @1.752**, 0.25u.

The live read upgraded SK because the draft's early forcing package was functioning and the economic lead was distributed through multiple roles.

## Final

User declared final with VIT winning. Latest synchronized grading frame:

- VIT 23-14 SK;
- 32:50;
- towers VIT 9-4 SK;
- dragons VIT 4-0 SK;
- Baron VIT 1-0 SK;
- inhibitors VIT 2-0 SK.

## User correction

The user characterized the result as **SK throwing the game and having no answer to Viktor**.

That is the key model-learning signal. The early SK advantage was real; the central error was not simply that the early scoreboard was misread. The model over-converted a real but non-terminal lead into a strong ML probability without pricing how the matchup changed if VIT reached organized mid/late objective setups.

## Primary model error

### 1. No explicit Terminal Threat Answerability test

Viktor represented VIT's principal terminal control threat. As the game progressed, VIT's Rumble / Viktor / Corki zone-and-damage shell became easier to execute in prepared objective spaces.

SK had initiation, but much of it was conditional:

- Jarvan and Gnar needed usable entry angles;
- Shen amplified the first commit but did not solve target access by itself;
- Varus and Ryze did not reliably remove Viktor from protected front-to-back setups;
- if SK's first engage failed or entered through controlled terrain, VIT retained strong damage continuation and counter-control.

The model credited SK for reliable early forcing but did not separately ask whether SK possessed a **repeatable, opponent-tested answer to VIT's strongest 25+ minute threat**.

### 2. Execution Burden Gradient was ignored

At 12:50, SK's composition was easier to execute because it could create picks and global numbers before VIT fully controlled terrain.

As time advanced:

- SK's initiation became more angle-dependent;
- VIT's front-to-back/choke execution became simpler;
- a single failed SK engage could expose the whole composition to Viktor/Rumble/Corki damage;
- VIT needed less creativity to win a standard objective setup than SK needed to break one.

The model treated execution simplicity as a static draft feature instead of a **time-varying gradient**.

### 3. Lead quality was overstated

The 5-2 / +1.6k state looked strong, but it was still structurally non-terminal:

- 0-0 towers;
- VIT already held the first dragon;
- SK had no demonstrated base access or accelerated tower conversion;
- the key VIT scaling/control threat was not materially suppressed.

Kills plus distributed gold were therefore insufficient evidence that SK could close before VIT's preferred game state arrived.

### 4. Comeback branch was underweighted

The live ML tree should have contained a large branch in which:

1. SK fail to convert the early lead into towers/objective acceleration;
2. VIT stabilize lanes and reach grouped setups;
3. Viktor/Rumble/Corki control narrows SK's engage angles;
4. one failed or forced SK engage flips a major objective;
5. VIT convert the objective into structural control and a decisive map state.

This branch was not given enough probability at entry.

## Corrected read under v0.3.52

At 12:50:

- SK early forcing: functioning;
- SK lead quality: **NON-TERMINAL**;
- VIT terminal threat: **Viktor-centered control/scaling shell**;
- SK Terminal Threat Answerability: **UNANSWERED / at best highly CONDITIONAL**;
- Execution Burden Gradient: **ADVERSE for SK** as the map moved toward 20-25+ minutes;
- structural acceleration: insufficient;
- leader ML upgrade: capped / vetoed until either Viktor was materially suppressed, SK demonstrated repeatable access onto the terminal threat, or the lead converted into a real close path.

Correct verdict on SK ML @1.752: **HOLD/PASS**, not TAKE.

## Model changes required

1. Add mandatory **Terminal Threat Answerability (TTA)** before post-draft and live ML TAKEs.
2. Add **Execution Burden Gradient (EBG)** to distinguish early versus late execution simplicity.
3. Split early lead into **terminal** versus **non-terminal** lead quality using structures/objectives/close path, not kills and gold alone.
4. Add a hard early-live ML veto when the leader has an unanswered terminal threat, adverse EBG, and only a non-terminal lead.
5. Re-run TTA after first tower, major objective acceleration, a material role-gold suppression of the terminal threat, repeated demonstrated access onto that threat, or a major state swing.
6. Apply the same terminal-threat logic to wide favorite kill-handicap tails: an unanswered scaling/control threat is both map-saving and margin-saving until proven otherwise.

This review is calibration for v0.3.52 and does not retroactively change the settled LOSS.