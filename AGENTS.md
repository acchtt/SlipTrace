# SlipTrace agent instructions

## Football model work

For tasks under `models/football`, treat
`models/football/CURRENT_MODEL.md` as the execution authority.

When proposing, modifying, promoting, retiring, or evaluating a permanent
football-model rule, use the `football-model-qa` skill at
`.agents/skills/football-model-qa/SKILL.md` and follow
`models/football/procedures/FOOTBALL_MODEL_QA_AND_PROMOTION.md`.

Do not promote permanent rules from anecdotal recent matches or from the same
examples that motivated the rule. Freeze a prospective champion/challenger
experiment first.

Ordinary prematch/live match execution should not load the QA workflow unless
the user is evaluating the model itself; preserve the model's live
verdict-first latency rule.

Never rewrite historical decisions to make them conform to a newer model.
