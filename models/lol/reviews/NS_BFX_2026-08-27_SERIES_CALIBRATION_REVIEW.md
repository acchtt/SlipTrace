# NS–BFX Series Calibration Review — 2026-08-27

**Series:** LCK 2026 Play-In — Nongshim RedForce vs BNK FEARX  
**Final:** BNK FEARX 3–1 Nongshim RedForce  
**Purpose:** mechanism-level review supporting prospective model calibration only.

## Key observations

1. **Moneyline opportunity leakage**
   - In Game 2, BFX’s live mechanism increasingly realized while usable ML prices still existed, but confirmation burden delayed action until the market largely repriced.
   - In Game 4, ML-first reassessment plus role-weighted state recognized BFX at 13:54 despite a 3–5 kill deficit; BFX were +814g, had first tower, and held multi-role leverage. BFX ML @2.943 was confirmed by the user and won.
   - Lesson: ML should be evaluated before derivatives and may use certified draft mechanism + first meaningful live confirmation on the ordinary path.

2. **TK Over speed was loosened too far**
   - Game 3 O29.5 @1.863 used strong contact inventory plus an early 2–0/dragon realization.
   - Final total was 28 kills.
   - Mechanism lesson: one realized contact sequence does not establish recurrence. TK Over needs at least two distinct observed contact realizations/cycles plus a forward contact source.

3. **Late boundary sensitivity**
   - Game 2 O39.5 @2.086 was entered at 24:40 and lost on 39 total kills.
   - The candidate had become highly sensitive to whether one additional fight occurred before a clean BFX close.
   - Lesson: late TK/Duration need materially higher edge and explicit terminal-event sensitivity; >=27 minutes should be presumptive PASS absent exceptional non-terminal structure.

4. **Raw kills can misdescribe ML state**
   - Game 4 BFX were down 3–5 kills but ahead in gold, first tower, and multiple roles.
   - Role-weighted economy and conversion access were more predictive of the live side than raw kill score.

5. **Objectives are modifiers, not automatic vetoes**
   - Game 2 NS’s dragon ownership reduced BFX confidence but should not have erased repeated BFX first-move/pick realization.

6. **Fearless requires archetype inventory**
   - By Games 3–4 both teams had depleted major engage, mid/jungle, bot-priority and protection options.
   - Remaining functional archetypes and player execution burden mattered more than champion count.

7. **Execution logging must distinguish candidate from position**
   - Fast live lines can disappear before a user can execute.
   - User explicitly required that no bet be logged until they confirm the quoted line still exists.
   - Future ledgers must distinguish analytical TAKE candidate from confirmed accepted Position.

## Prospective calibration

Implemented in:
`models/lol/procedures/LOL_POST_NS_BFX_MARKET_PRIORITY_AND_EXECUTION_CALIBRATION_2026-08-27.md`

Core changes:

- ML-first market triage;
- ordinary live ML two-independent-evidence path;
- retained LRO floor against CLEAR/STRONG contrary draft;
- HOLD expiry;
- canonical opportunity-decay bands;
- stronger role-weighted ML state decomposition;
- TK Over requires two observed contact realizations/cycles;
- KH speed rules are not loosened;
- Fearless archetype inventory emphasized;
- user line-existence confirmation required before Position creation/P&L.

## Historical integrity

No historical verdict, position, settlement or P/L is rewritten by this review.
