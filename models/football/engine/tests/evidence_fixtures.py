"""Explicit synthetic evidence for contract tests; never production facts."""


def attach_g4_evidence(row):
    row['g4_path_evidence'] = {}
    fields = ('g4_carrier_path', 'g4_distributed_path', 'g4_reply_path')
    record = {'basis': 'Synthetic prospective mechanism observation', 'evidence_refs': ['fixture-source-before-kickoff']}
    row['failure_mechanisms'] = {'test-mechanism': {**record, 'kind': 'SCORING_PERSISTENCE', 'affected_paths': list(fields)}}
    for field in fields:
        row['g4_path_evidence'][field] = {**record, 'mechanism_ids': ['test-mechanism'] if row.get(field) == 'FAILED' else []}
    row['grade_evidence'] = {field: {**record, 'mechanism_ids': ['test-mechanism']} for field in (
        'route_reliability', 'continuation_quality', 'burden_stall_risk', 'failure_resistance', 'independent_upper_tail')}
    return row
