# MODEL RULES — LEAGUE OF LEGENDS v0.3.44

**Status:** Active delta  
**Effective date:** 2026-08-09 16:04 UTC+7  
**Supersedes:** v0.3.43 only where stated

## Purpose

Correct the directional bias exposed in the tracked kill-handicap sample. The handicap engine repeatedly selected the positive-kill side and evaluated the underdog's ability to remain within the cushion more deeply than the favorite's ability to create a wide margin.

At activation, the tracked kill-handicap history contained 12 selections and all 12 were on the `+kills` side. Of the 10 settled positions with known results, the record was 3-7 for **-0.9635u**. One older TH +6.5 result was missing and KT +3.5 vs DK Game 2 was still open. The sample is too small to prove the market family is intrinsically unprofitable, but the 12/12 directional skew is sufficient evidence of a process bias.

This delta makes kill-handicap analysis **side-neutral and distribution-first**. It does not impose a favorite bias and does not require a quota of negative-handicap bets.

All v0.3.43 duration controls and v0.3.42 team-strength/draft controls remain active.

---

## 1. Kill Margin Is the Primary Random Variable

Before evaluating any displayed kill handicap, define a favorite and model the signed final kill margin:

`M = favorite final kills - underdog final kills`

For pregame/0:00, the favorite is the de-vigged map favorite after verified lineup and draft reconciliation. For live snapshots, use the current live map favorite when a synchronized ML market exists; otherwise use the position-blind current map-state favorite.

The handicap line must not determine the projected margin distribution.

Before comparing to a sportsbook handicap, lock a side-neutral final-margin distribution with at least these bins:

- `M <= 0` — underdog wins or does not lose the kill count;
- `M = +1 to +3`;
- `M = +4 to +6`;
- `M = +7 to +9`;
- `M = +10 to +14`;
- `M >= +15`.

Bins may be refined when the line requires it, but they may not be collapsed merely to make a displayed side look attractive.

The probabilities must sum to approximately 100% and must be consistent with the modeled map-win probability, projected total kills, current game state, team-strength gap, draft interaction and cascade structure.

---

## 2. Symmetric Cover Calculation

For a half-kill line `H`:

- `P(underdog +H covers) = P(M < H)`;
- `P(favorite -H covers) = P(M > H)`.

For whole-number lines, account explicitly for push rules if the sportsbook market can push.

Every handicap evaluation must price **both sides from the same locked margin distribution** before selecting either side.

A handicap TAKE is invalid if the model can explain why the selected side covers but cannot explain, with equal depth, why the opposite side fails to cover often enough.

Do not generate separate incompatible distributions for the two sides.

---

## 3. Blind Fair-Margin Lock

Before using the displayed handicap as evidence, internally lock:

1. projected total-kill low / central / high range;
2. fair central favorite kill margin;
3. signed margin-bin distribution;
4. favorite map-win probability range;
5. conditional favorite-win margin distribution;
6. underdog-win/tie branch;
7. uncertainty width.

Only after those are fixed may the sportsbook line `H` and odds be compared to the distribution.

The numerical size of a positive cushion is **not evidence**. Phrases such as "they still need another +7 net kills" are arithmetic descriptions only and cannot support a TAKE without the underlying future-margin distribution.

---

## 4. Favorite Wide-Win Branch Must Be Modeled Explicitly

The favorite's high-margin tail receives the same analytical depth previously given to underdog resilience.

Increase the favorite wide-win branch when supported by matchup-adjusted evidence such as:

- verified team-strength gap;
- stronger early creation or lead conversion;
- simpler/repeatable engage sequence;
- multi-axis target access;
- carry concentration on a hard-to-answer damage source;
- wave/structure control that forces repeated defensive fights;
- objective control and forced face-checks;
- Baron/soul/base access;
- safe chase/cleanup damage;
- serial `pick -> numbers -> objective -> structure -> deeper vision -> second pick` architecture;
- end-game kill inflation from desperate base defense, forced objective contests or terminal chase.

These events are serially dependent. Do not price each future kill as an independent event.

A current small kill margin does not imply a narrow final margin when the favorite has aligned structural and conversion control.

---

## 5. Underdog Resilience Remains Mechanistic

Positive-handicap resilience still requires matchup-adjusted evidence in the retained categories:

1. safe range;
2. disengage/reset;
3. waveclear/base defense;
4. anti-dive/peel;
5. objective-contest access;
6. return-kill reliability.

However, resilience points may only affect the margin distribution after opponent counter-testing under v0.3.42.

Theoretical tools do not automatically convert into a high close-loss probability. The model must identify how those tools reduce the favorite's `+7`, `+10` or `+15` tail in the actual matchup.

---

## 6. Conditional Winner/Margin Consistency

Retain:

`P(dog +H covers) = P(dog wins) + P(favorite wins AND M <= H)`

But the favorite-win close/moderate/wide branches must now be derived from the same signed distribution used for the opposite handicap.

Required consistency checks:

- a large favorite map-win probability plus a very high dog-cover probability requires affirmative evidence that favorite wins are usually narrow;
- a strong favorite with simpler execution and high cascade potential must allocate meaningful probability to wide wins;
- an underdog draft with difficult damage access cannot receive full close-loss credit merely for possessing waveclear or engage;
- a favorite-negative handicap is not automatically good merely because the favorite is strong.

The objective is calibrated margin pricing, not directional balance for its own sake.

---

## 7. Live Cascade-Adjusted Margin Hazard

For live handicap evaluation, explicitly score margin-expansion hazard from:

- gold lead and trajectory;
- tower differential and repeatable structure access;
- neutral-objective alignment;
- Baron/Elder/soul state;
- carry concentration and shutdown distribution;
- reliable engage / pick channels;
- defender face-check burden;
- retreating-side return-kill evidence;
- base-defense and terminal-fight exposure.

If the leader has aligned gold + structure/objective pressure + repeatable first contact, widen the favorite high-margin tail even if the current kill margin is small.

When inhibitor/base access is present, positive-handicap analysis must include an explicit **terminal kill inflation** branch. A losing team can concede several additional kills while defending the Nexus even when the map was close for most of its duration.

---

## 8. Side-Neutral Market Scan

When both sides of a kill handicap are displayed, evaluate in this order:

1. locked fair margin distribution;
2. positive-side break-even and edge;
3. negative-side break-even and edge;
4. uncertainty and phase buffer;
5. structural/cascade vetoes;
6. choose the single best qualifying side or PASS/HOLD.

Do not start from the underdog side by default.

If neither side clears its gate from the same distribution, output `PASS/HOLD`.

If both appear to clear because the probability range is too wide or inconsistent, the model is under-specified: widen uncertainty and `PASS/HOLD` rather than selecting one.

---

## 9. Temporary Handicap Calibration Surcharge

The directional skew and 3-7 settled record trigger a temporary high-friction calibration mode for **new kill-handicap entries generated under v0.3.44**.

For the next 20 settled v0.3.44 kill-handicap positions, the lower bound of `P_cover` must clear break-even by:

- **+7pp** pregame / 0:00;
- **+6pp** early live;
- **+5pp** mid/late live.

This is +2pp stricter than the retained v0.3.39 baseline and applies symmetrically to positive and negative handicaps.

Review after 10 settled v0.3.44 handicap positions and again after 20. At review, inspect:

- win/loss and ROI;
- calibration versus estimated probability bands;
- positive vs negative selection share;
- average line magnitude;
- favorite/underdog map-win prior;
- pregame vs live split;
- wide-margin tail calibration.

The surcharge may be removed only by a future explicit model revision.

The already-recorded **KT +3.5 kills @1.935 vs DK Game 2** remains a v0.3.43 entry. It is not retroactively voided or reclassified. Any future position-blind reassessment of that open ticket uses the current v0.3.44 framework.

---

## 10. Directional-Skew Monitor

Track the sign of every new kill-handicap TAKE.

At each 10-position handicap review window:

- if >=80% of selections are on one sign, perform a directional-bias audit before relaxing any calibration controls;
- if >=90% are on one sign **and** settled ROI is negative, keep or strengthen the surcharge and require an explicit process review;
- do not force the next wager to the opposite sign merely to balance counts.

Directional diversity is a diagnostic, not a betting objective.

---

## 11. Mandatory Handicap Output Discipline

Before any kill-handicap recommendation, internally lock:

1. phase classification;
2. current favorite and favorite map-win probability range;
3. current kill margin;
4. projected total-kill low / central / high range;
5. fair central favorite kill margin;
6. side-neutral signed margin bins;
7. conditional favorite-win margin distribution;
8. underdog-win/tie branch;
9. cascade-adjusted wide-margin hazard;
10. matchup-adjusted underdog resilience;
11. both displayed sides' break-even probabilities;
12. both sides' cover ranges from the **same** distribution;
13. applicable v0.3.44 calibration surcharge;
14. structural/cascade veto state;
15. executable line/price status.

Missing a decision-critical element => `PASS` or `HOLD`.

---

## 12. Retained Controls

All v0.3.43 duration controls remain active.

All v0.3.42 verified-team-strength, market-divergence, matchup-adjusted draft, functional-counter, execution-burden and damage-access controls remain active.

All v0.3.41 position-blind reassessment and structural handicap vetoes remain active.

Where this delta conflicts with earlier kill-handicap heuristics, **v0.3.44 controls**.
