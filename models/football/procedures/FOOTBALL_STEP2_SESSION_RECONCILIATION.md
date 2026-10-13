# Historical Step-2 session reconciliation — retired

The former session-wide Step-2 reconciliation workflow is not part of the
active Football v2 path.

Current /xi uses:

1. one football C+C2 assessment;
2. optional observed-quote comparison or strict C+C2 price pair;
3. one Decision State write/readback;
4. one final publication freshness/readback guard only for strict official
   publication.

The old session queue/outcome reconciliation, kickoff-transition router,
work-ready/terminal Step-1 compatibility path and step2_reconcile CLI are
retired. Git history remains available for historical audit.

Do not load this file as current execution authority.
