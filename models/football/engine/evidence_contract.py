"""Evidence completeness and explanations; never modifies predictive grades."""
from collections import defaultdict
from core import (Grade, RouteStrength, CarrierStrength, CompletionMode,
                  c_goal3_funded, c_goal4_funded, c_upper_tail_transferable,
                  c_effective_incentive_grades, certificate_robustness,
                  tournament_incentive_profile)

PATH_FIELDS = ('g4_carrier_path', 'g4_distributed_path', 'g4_reply_path')
GRADE_FIELDS = ('route_reliability', 'continuation_quality', 'burden_stall_risk',
                'failure_resistance', 'independent_upper_tail')
TAIL_FIELDS = ('upper_tail_transferability', 'upper_tail_transferability_basis',
               'upper_tail_comparable_context_signal', 'upper_tail_comparable_context_basis')


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def record_valid(record):
    return (isinstance(record, dict) and nonempty(record.get('basis'))
            and isinstance(record.get('evidence_refs'), list) and bool(record['evidence_refs'])
            and all(nonempty(x) for x in record['evidence_refs']))


def g4_evidence_review(obj, profile):
    """A claimed completed rejection cannot substitute for resolved evidence.

    Legacy files are never mutated. Derived current assessments expose the
    original declaration and normalize unproven completion to pending work.
    """
    declared = profile['g4_research_status']
    gaps, shared = [], defaultdict(list)
    completed = declared in {'G4_RESEARCH_COMPLETE_REJECTED', 'G4_RESEARCH_COMPLETE_MIXED',
                             'G4_RESEARCH_COMPLETE_FUNDED'}
    if completed:
        gaps.extend(k for k in TAIL_FIELDS if not nonempty(obj.get(k)))
        evidence = obj.get('g4_path_evidence') or {}
        mechanisms = obj.get('failure_mechanisms') or {}
        for field in PATH_FIELDS:
            rec = evidence.get(field) if isinstance(evidence, dict) else None
            if not record_valid(rec):
                gaps.append(field + '.evidence')
                continue
            state = profile[field]
            if state == 'UNAVAILABLE':
                gaps.append(field + '.unavailable')
            if state == 'FAILED':
                mids = rec.get('mechanism_ids')
                if not isinstance(mids, list) or not mids:
                    gaps.append(field + '.mechanism_ids')
                else:
                    for mid in mids:
                        mechanism = mechanisms.get(mid) if isinstance(mid, str) and isinstance(mechanisms, dict) else None
                        if not record_valid(mechanism) or not isinstance(mechanism.get('affected_paths'), list) or field not in mechanism['affected_paths']:
                            gaps.append(field + '.unbound_mechanism')
                        elif field == 'g4_carrier_path' and mechanism.get('kind') == 'OPPONENT_REPLY_ONLY':
                            gaps.append(field + '.reply_only_is_not_carrier_failure')
                        else:
                            shared[mid].append(field)
        if profile['g4_continuation_after_g3'] in {'UNAVAILABLE', 'NOT_APPLICABLE'}:
            gaps.append('g4_continuation_after_g3')
        grades = obj.get('grade_evidence') or {}
        for field in GRADE_FIELDS:
            rec = grades.get(field) if isinstance(grades, dict) else None
            if not record_valid(rec):
                gaps.append(field + '.grade_evidence')
                continue
            mids = rec.get('mechanism_ids', [])
            if not isinstance(mids, list):
                gaps.append(field + '.mechanism_ids')
                continue
            for mid in mids:
                if not isinstance(mid, str) or not isinstance(mechanisms, dict) or not record_valid(mechanisms.get(mid)):
                    gaps.append(field + '.unknown_mechanism')
                else:
                    shared[mid].append(field)
            if field == 'burden_stall_risk' and obj.get(field) == 'HIGH' and not mids:
                gaps.append('burden_stall_risk.high_requires_mechanism')
        if declared != 'G4_RESEARCH_COMPLETE_FUNDED' and 'SUPPORTED' in [profile[f] for f in PATH_FIELDS]:
            blockers = obj.get('g4_global_blockers')
            actual = set(g4_diagnostics_from_row(obj).get('failed_conditions', []))
            actual -= {'CARRIER_BRANCH_REQUIREMENTS_NOT_MET', 'DISTRIBUTED_BRANCH_REQUIREMENTS_NOT_MET'}
            if not isinstance(blockers, list) or not blockers or any(
                not record_valid(b) or b.get('condition') not in actual for b in blockers
            ):
                gaps.append('g4_global_blockers')
    status = declared
    if gaps:
        status = ('G4_RESEARCH_EVIDENCE_LIMITED' if all(
            g.endswith('.unavailable') or g == 'g4_continuation_after_g3' for g in gaps
        ) else 'G4_RESEARCH_INCOMPLETE')
    elif declared == 'G4_RESEARCH_COMPLETE_REJECTED' and any(profile[f] == 'MIXED' for f in PATH_FIELDS):
        status = 'G4_RESEARCH_COMPLETE_MIXED'
    dispositions = {'G4_NOT_APPLICABLE': 'NOT_APPLICABLE',
                    'G4_RESEARCH_INCOMPLETE': 'INCOMPLETE',
                    'G4_RESEARCH_EVIDENCE_LIMITED': 'EVIDENCE_LIMITED',
                    'G4_RESEARCH_COMPLETE_REJECTED': 'NEGATIVE',
                    'G4_RESEARCH_COMPLETE_MIXED': 'MIXED',
                    'G4_RESEARCH_COMPLETE_FUNDED': 'FUNDED'}
    return {**profile, 'g4_declared_research_status': declared,
            'g4_research_status': status, 'g4_evidence_disposition': dispositions[status],
            'g4_evidence_gaps': sorted(set(gaps)), 'g4_research_complete': completed and not gaps,
            'g4_path_evidence': obj.get('g4_path_evidence'),
            'grade_evidence': obj.get('grade_evidence'), 'failure_mechanisms': obj.get('failure_mechanisms'),
            'g4_global_blockers': obj.get('g4_global_blockers'),
            'shared_failure_mechanisms': {k: sorted(set(v)) for k, v in shared.items() if len(set(v)) > 1},
            'predictive_grades_changed_by_evidence_contract': False}


def g4_diagnostics_from_row(obj):
    # Delayed import avoids the adapter's module initialization cycle.
    from adapter import parse_assessment
    return g4_diagnostics(parse_assessment(obj))


def g4_diagnostics(a):
    """Explain existing vetoes, with actual compiler funding authoritative."""
    continuation, stall = c_effective_incentive_grades(a)
    strong_pair = a.home_route == a.away_route == RouteStrength.STRONG and a.independent_route_quality == Grade.HIGH
    suppressive = tournament_incentive_profile(a)['tail_bias'] == 'SUPPRESSIVE'
    failed = []
    for name, ok in (
        ('G3_REQUIRED', c_goal3_funded(a)),
        ('INDEPENDENT_TRANSFERABLE_TAIL_REQUIRED', c_upper_tail_transferable(a)),
        ('STALL_AT_MOST_MEDIUM', stall <= Grade.MEDIUM),
        ('NO_MATERIAL_SUPPRESSION', suppressive or not a.material_suppression),
        ('NO_ROUTE_DESTROYING_FAILURE', suppressive or not a.failure_attacks_route),
    ):
        if not ok:
            failed.append(name)
    carrier = (a.carrier == CarrierStrength.STRONG and a.carrier_self_fund
               and (a.route_reliability == Grade.HIGH or strong_pair)
               and a.chance_quality >= Grade.MEDIUM and a.failure_resistance >= Grade.MEDIUM
               and a.evidence_confidence >= Grade.MEDIUM and a.burden_completion_quality >= Grade.MEDIUM
               and continuation >= Grade.MEDIUM)
    distributed = (a.completion_mode in {CompletionMode.TWO_SIDED, CompletionMode.MIXED}
                   and min(a.home_route, a.away_route) >= RouteStrength.USABLE
                   and max(a.home_route, a.away_route) == RouteStrength.STRONG
                   and a.independent_route_quality == Grade.HIGH and a.route_reliability == Grade.HIGH
                   and a.chance_quality >= Grade.MEDIUM and (strong_pair or a.failure_resistance == Grade.HIGH)
                   and a.burden_completion_quality == Grade.HIGH and continuation == Grade.HIGH)
    if suppressive:
        carrier = (a.carrier == CarrierStrength.STRONG and a.carrier_self_fund
                   and a.route_reliability == Grade.HIGH and a.chance_quality == Grade.HIGH
                   and a.failure_resistance == Grade.HIGH and a.evidence_confidence == Grade.HIGH
                   and continuation >= Grade.MEDIUM)
        distributed = False
    if not carrier:
        failed.append('CARRIER_BRANCH_REQUIREMENTS_NOT_MET')
    if not distributed:
        failed.append('DISTRIBUTED_BRANCH_REQUIREMENTS_NOT_MET')
    return {'goal4_funded': c_goal4_funded(a), 'failed_conditions': failed,
            'carrier_branch_quality_met': carrier, 'distributed_branch_quality_met': distributed,
            'tournament_tail_bias': tournament_incentive_profile(a)['tail_bias'],
            'certificate_robustness': ('FRAGILE', 'CONDITIONAL', 'ROBUST')[certificate_robustness(a, 'c')],
            'explanation_only': True}
