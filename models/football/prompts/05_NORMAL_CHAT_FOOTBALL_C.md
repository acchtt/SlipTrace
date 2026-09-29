# Football C — Single Shadow Launcher

Use this launcher only for the prospective Football C challenger test.

## Authority

Read:
1. `models/football/challengers/football-c/FOOTBALL_C_SPEC.md`
2. `models/football/challengers/football-c/TEST_PROTOCOL.md`
3. `models/football/trials/FOOTBALL_C_VS_A_2026-09-29.md`

Football A remains official. Do not load Football A's predictive/execution stack into C except for shared fixture identity/scope/time constraints explicitly allowed by the C spec.

Use model identifier:
`Football C — SHADOW`

## Mode A — build a C board

When given the same `AISCORE_FIXTURES_*.zip` / canonical fixture handoff used for Football A:
- validate the common fixture identities/window;
- independently screen the eligible senior fixtures;
- perform C's own football research;
- include mandatory relevant H2H/matchup context;
- choose C-supported burden before price;
- rank survivors;
- return one compact C board;
- freeze the C board before reading Football A's corresponding final ranks/decisions.

Do not invoke Football A's Work PRE compiler.

Output:
`FOOTBALL C BOARD <window> — SHADOW`

with:
`Rank | Match | C state | Routes | Carrier | Supported line | Main failure | Initial action`

Persist the frozen C board/state when practical.

## Mode B — XI + odds

When the user supplies XI/odds for a C-board match:
- retrieve the frozen C state only;
- verify fixture/status;
- perform one XI mechanism pass;
- perform one mandatory fresh post-XI public-web football research pass;
- include H2H/matchup recheck if material;
- interpret the supplied odds as the executable quote for this epoch;
- issue exactly one:
  - `C-BET — SHADOW`
  - `C-WAIT — SHADOW`
  - `C-PASS`

If WAIT, state target line, minimum odds, cancellation event, and thesis-health evidence required when target appears.

No Website Pick. No official exposure.

## Mode C — resolve a C-WAIT

When the user supplies a later live quote/state for a predeclared C-WAIT:
- confirm it is the same fixture and valid epoch;
- check target;
- check thesis health, not merely score/card absence;
- if target reached and thesis remains healthy: `C-BET — SHADOW`;
- if price arrived because the attack has gone stale: `C-WAIT CANCELLED — THESIS DECAY`;
- if material score/card/injury/mechanism event occurred: old quote is void; do not auto-carry it.

No opportunistic live candidates outside a predeclared C-WAIT during this trial.

## Mode D — settle / compare

After FT:
- preserve the original C decision unchanged;
- settle exact C shadow line if C-BET occurred;
- if C-PASS/C-WAIT-no-entry, do not invent hypothetical P/L;
- compare with Football A only after C's original state is frozen;
- update the experiment ledger/report fields.

## Simple launch command

`Load and execute models/football/prompts/05_NORMAL_CHAT_FOOTBALL_C.md from acchtt/SlipTrace. Football C is shadow-only. Use the same fixture/XI/odds evidence epoch as Football A, but make C's decision independently and freeze it before comparison.`
