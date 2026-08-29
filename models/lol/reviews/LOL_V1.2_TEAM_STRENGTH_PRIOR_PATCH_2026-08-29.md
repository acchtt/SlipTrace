# LoL v1.2 Team-Strength Prior Patch — 2026-08-29

## 1. Trigger

During T1 vs BNK FEARX Game 2, the user asked whether team strength had been considered. Review showed that v1.1 did not contain any persistent team-strength layer: every map started from 50% before draft/live variables.

That is a clear mechanical architecture defect for professional Moneyline estimation, because draft quality and current live state are not substitutes for persistent team quality.

The user then explicitly authorized an immediate patch.

No accepted v1.1 Moneyline Position existed, so the ML validation sample is not contaminated by the transition.

---

# 2. Repair chosen

Add one compact series-frozen team-strength variable:

`K=-2,-1,0,+1,+2`

with baseline:

`P0=50%+10*K pp`

Then preserve the existing v1.1 draft/live state score:

`S=1.0*D_eff+1.5*R+1.5*X+1.25*O+1.0*T`

and use:

`P=clamp(P0+3*S pp,15%,85%)`.

This retains the simple v1.x architecture: one new discrete prior, no regression tree, no sportsbook-derived seed and no legacy certificate stack.

---

# 3. Why `K` is separate from draft

`K` answers: how strong are these teams relative to each other before this series and independent of this map's composition?

`D` answers: which exact draft has the better map-specific mechanism?

Combining the two inside one draft label would hide causal information and make a slight composition edge carry too much team-reputation burden.

---

# 4. Anti-price contamination

`K` must be assigned from evidence available before Game 1 and may not use sportsbook odds.

For mid-series v1.2 activation, earlier maps from the same series are also prohibited from choosing `K`.

Book price may only be read after `K/P0`, draft/live state and final probability are locked.

---

# 5. T1 vs BNK FEARX prospective series prior

For Game 3 onward, reconstructing only from evidence available before Game 1:

From BNK FEARX perspective:

`K=-1`

Therefore:

`P0(BFX)=40%`
`P0(T1)=60%`

Rationale: T1 entered the playoff bracket without needing the late Play-In path and had a stronger established top-level competitive baseline, while BFX had enough recent official wins and Play-In success that the gap should be meaningful but not classified as the maximum `K=-2` mismatch.

This `K` is frozen for the remainder of the series unless an actual roster/availability change occurs. Game 1 and Game 2 results do not modify it.

---

# 6. Post-design sanity checks — not validation observations

These are historical process checks only and do not count as v1.2 samples.

### Game 1 11:32 window

v1.1 BFX state score had `S=-5.0` and produced 35% from a neutral 50% baseline, creating a BFX @4.960 candidate.

With prospective series strength `K=-1`, `P0(BFX)=40%`:

`P(BFX)=40%-15%=25%`.

At 4.960, raw implied was about 20.16%, so edge would have been about `+4.84pp`, below the +5.0pp ML threshold -> PASS rather than TAKE CANDIDATE.

### Game 2 ~10:05 window

v1.1 state score was `S=+3.0` for BFX.

With `P0(BFX)=40%`:

`P(BFX)=49%`.

The executable BFX price around 1.997 implied about 50.1%, so v1.2 would PASS.

These checks show the repair addresses the identified neutral-baseline failure without changing the existing live-state weights. They are not accepted-position calibration evidence and are not permission to tune further from two maps.

---

# 7. Duration boundary

Duration v1.1 is unchanged by this patch. Team strength must not be inserted into Duration automatically; game length is handled through the independent Duration state model.

---

# 8. Validation boundary

Game 1 and Game 2 remain v1.1 historical evidence.

v1.2 applies prospectively only after a new authority commit and fresh Session Authority Lock activate the complete stack.
