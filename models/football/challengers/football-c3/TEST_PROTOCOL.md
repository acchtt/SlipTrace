# Football C3 — Prospective Test Protocol

**Status:** ACTIVE PROSPECTIVE SHADOW TEST  
**Champion:** Football C  
**C2 status:** continues its own frozen five-board test independently  
**C3 activation boundary:** merge commit introducing Football C3

## 1. Window

Run C3 for the next **5 complete clean boards** after activation.

C3 Board 1 is the first board fully frozen after the activation commit.

Historical boards have zero confirmatory C3 weight.

## 2. Same evidence

For every admitted fixture:
- same common football facts for C/C2/C3;
- C3 policy fields frozen before C/C2 outcomes are viewed;
- independent C3 supported line;
- no retrospective relabeling.

## 3. Required board output

Persist:
- C official state/rank/lane/line;
- C2 shadow state/rank/line;
- C3 shadow state/rank/lane/line;
- second_route_role;
- goal3 funding/source/basis;
- goal4 funding/source/basis;
- control_endpoint_risk/basis.

## 4. Primary comparison

Primary:
- same-kickoff / same-board selection ordering;
- support settlement at each model's own frozen line;
- two-goal endpoint rate among promoted candidates;
- priority inversion count.

Secondary:
- Step-2 shadow actions on fixtures that receive normal XI/odds assessment;
- false negatives where C3 STOP/PASS and C clears.

## 5. C2 independence

Do not reset, edit, or merge C2 statistics with C3.

C2 continues its current five-board window under its frozen route-quality policy.

C3 gets a separate 1/5 ... 5/5 counter.

## 6. Contamination

A C3 board is contaminated when:
- C3 fields were assigned after outcome knowledge;
- C3 copied C/C2 supported line instead of deriving its own;
- required funding basis is missing;
- common evidence differs materially between models without documentation;
- tournament/identity/XI integrity gates were bypassed.

Contaminated boards do not advance the five-board counter.

## 7. Freeze rule

After C3 Board 1 produces an eligible result:
- do not edit C3 predictive Sections 3–11;
- any predictive change becomes C4.

Plumbing/QA fixes may be made only when they do not change C3 predictive semantics; if they can affect outputs, restart the window.

## 8. Evaluation checkpoint

After 5 clean boards report:
- C vs C3 support-value difference;
- C vs C3 priority inversions;
- C vs C3 two-goal endpoint rate;
- C3 false-negative rate;
- C2 results separately;
- recommendation whether to continue testing, retire C3, or create a further challenger.

No automatic promotion.
