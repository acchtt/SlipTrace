# LoL Match Prep — 2026-08-21 (UTC+7)

**Status:** PREP CONTEXT ONLY — NON-AUTHORITY  
**Analytical authority:** use the active/new session lock and canonical LoL v0.3.58; this file never overrides `CURRENT_MODEL.md`, bootstrap, or session lock.  
**Draft process:** DIM is mandatory under the next authority lock that includes the 2026-08-20 amendment.  
**Official betting:** paused; shadow only.  

## Slate rule

The current E3 lock expires at the UTC+7 day boundary. Before any TAKE on 2026-08-21, establish a fresh valid session lock from current canonical authority. Pregame/postdraft ML/KH/TK TAKE restrictions and all retained gates remain unchanged.

## Scheduled Tier-1 matches

### LPL — Bo3 Fearless
Official LoL Esports schedule for 2026-08-21:
- TT vs EDG
- AL vs WE
- BLG vs TES

Indicative UTC+7 windows from the official schedule normalization: approximately 14:00 / 16:00 / 18:00. Reconfirm exact start times at match time.

### LCK — Bo3 Fearless
Official schedule:
- BRO vs BNK FEARX
- KT vs T1

Indicative UTC+7 windows: approximately 15:00 / 17:00. Reconfirm exact start times at match time.

### LCP — Bo5
- Team Secret Whales vs GAM Esports, approximately 16:00 UTC+7.

### LEC — Bo3 Fearless
- Team Heretics vs SK Gaming
- NAVI vs Team Vitality

Vietnam-local schedule listings place these around 23:00 UTC+7 and 01:15 on 2026-08-22 respectively. Reconfirm exact start times at match time.

## Preliminary team-strength context — qualitative only

Starting five-player lineups are not yet match-verified, so no numeric TEAM prior is locked here.

### TT vs EDG
- Preliminary edge: TT.
- EDG were 0-10 in the Ascend group in a recent Aug 15 standings snapshot; TT were 3-7.
- Main risk: do not convert EDG weakness into automatic TT -kills. Favorite handicap still needs live FFD/RNE and exact remaining-fight support.
- DIM focus: whether EDG possesses a direct threat-answer and collapse-reset route rather than generic scaling/peel.

### AL vs WE
- Preliminary edge: AL.
- Recent Aug 15 standings had AL 8-2 and WE 6-4.
- Main risk: WE are materially stronger than the bottom Ascend teams; do not treat AL team strength as a draft override.
- DIM focus: objective setup geometry, carry access, and whether WE side-lane/fallback routes are genuinely independent.

### BLG vs TES
- Preliminary class: elite / high-priority, BLG slight team-strength prior only.
- LoL Esports global ranking snapshots place BLG among the very top teams, but TES defeated BLG 2-0 on Aug 7 in this split.
- Main risk: no generic `better team` conclusion. This is a draft-sensitive matchup where pre-contact geometry, side-lane control, and target access can reverse the prior.
- DIM focus: PKM/SKM for both sides; TAM; OSG; FNF (do not penalize low frontline automatically); SLI; CAS; AFP.

### BRO vs BNK FEARX
- Preliminary class: close Rise-group matchup.
- A recent LCK standings snapshot had BRO 8-14 and BFX 7-14, while a current market listing showed BFX favored pre-match. Treat both only as context.
- Main risk: high volatility/throw potential makes generic team-strength claims weak.
- DIM focus: underdog +kills only if TAM/CAS/KMS are genuinely STABLE and later UCS is sufficient. No broad anti-cascade credit.

### KT vs T1
- Preliminary edge: T1, but not a mismatch.
- A recent LCK table had T1 16-6 and KT 15-6; both are Legend-group quality.
- Main risk: do not let T1 name/strength prior substitute for live CFC or draft interaction.
- DIM focus: neutral-fight first contact, protected DPS, side-lane/global pressure, and whether the weaker draft can actually answer the primary kill route.

### TSW vs GAM
- Preliminary edge: TSW.
- Recent Split 3 results: TSW beat CFO 3-0; GAM beat DCG 3-1.
- Bo5 Fearless means champion-pool depletion and later-map draft asymmetry are especially important.
- DIM focus: update mechanism map every game; do not carry a Game 1 draft label into later fearless maps.

### Team Heretics vs SK
- Preliminary class: close lower-table LEC matchup.
- Recent standings context: SK 1-2, TH 1-3; TH recently beat Fnatic 2-1.
- Main risk: low confidence team-strength prior; draft interaction should dominate.

### NAVI vs Vitality
- Preliminary edge: slight NAVI / close.
- Recent standings context had NAVI 2-1 and Vitality 2-2; NAVI previously beat SK 2-1 and lost 0-2 to G2.
- Main risk: avoid overvaluing record in a small fearless sample.

## Mandatory tomorrow workflow

For each exact draft:
1. resolve roles first;
2. complete DIM: PKM/SKM, TAM, OSG, DAU, SLI, FNF, CAS, ETS, AFP;
3. output Draft Edge separately from underdog +kills Stability;
4. if +kills candidate, complete full draft-only UDKC; `TAM` or `CAS` fail/unresolved => KMS cannot pass => UDKC not STABLE;
5. no pregame/immediate-postdraft ML/KH/TK TAKE;
6. live ML/KH/TK require two usable synchronized snapshots;
7. underdog +kills requires STABLE UDKC + live preservation + UCS + exact signed margin/NKB;
8. favorite -kills requires exact RNE + FFD + Structure Substitution checks;
9. every TAKE requires complete `GATE_SIG[...]` and one-per-family check.

## Source notes

Prep built 2026-08-20 UTC+7 from current LoL Esports schedule, recent LCK/LPL/LEC standings/results sources, and LCP playoff schedule. Exact starting lineups, substitutions, side selection, patch, and executable odds must be reverified tomorrow before they are used as decision inputs.
