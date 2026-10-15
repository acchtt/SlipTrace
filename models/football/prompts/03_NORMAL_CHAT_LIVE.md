# /live — current-state Football C assessment

Football C is the only active model.

Use the same C football engine as /xi with:

- actual current score;
- match minute;
- verified goals/reds/injuries/substitutions;
- current tournament/game-state changes;
- frozen prematch/xi thesis as context.

Provider live stats are not required.

After kickoff:

- assess the current football state;
- invalidate prematch execution assumptions;
- never recreate a prematch ACT/WAIT/PASS;
- do not request a new bookmaker quote merely because the game started;
- a user-supplied live quote is comparison evidence only unless a separate
  live-execution policy explicitly authorizes action.

Retired C2/C3/C4 models do not run in /live.
