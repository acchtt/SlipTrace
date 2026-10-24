"""Research coverage and recovery regressions; no network or predictive changes."""
import copy
import json
import unittest

from test_stage import snapshot, sweep, NOW, model_input, fresh_status, fixture
from stage import rank, verify_rank, StageError

AT = '2026-10-11T16:05:00Z'
LATER = '2026-10-11T16:07:00Z'


def c_input(mid='m1'):
    data = model_input(mid)
    data['authority_commit'] = 'c-authority-for-test'
    return data


def make_unfunded_watch(row):
    row.update(
        board_state='C-WATCH',
        board_state_basis='Current evidence does not fund G3',
        home_route='WEAK', away_route='WEAK', carrier='NONE',
        carrier_self_fund=False,
        carrier_self_fund_basis='No current self-funded carrier',
        independent_upper_tail=False,
        independent_upper_tail_basis='No independent upper-tail route',
        route_reliability='LOW', independent_route_quality='LOW',
        chance_quality='LOW', failure_resistance='LOW',
        burden_protection='LOW', burden_completion_quality='LOW',
        continuation_quality='LOW', opponent_leakage='LOW',
    )
    return row


def gap(mid='m2'):
    return {
        'reason': 'RESEARCH_EVIDENCE_MISSING', 'match_id': mid,
        'missing_fields': ['away_route'],
        'attempts': [{
            'source_url': 'https://club.example.org/preview/' + mid,
            'checked_at_utc': AT, 'fields_checked': ['away_route'],
            'finding': f'{mid}: current away preview has no service/chance mechanism evidence.',
        }],
        'next_action': 'Check the latest away league match report for chance creation.',
    }


def execute(c=None, reasons=None, *, previous=None, status=None, at=AT):
    source = snapshot()
    receipt = sweep(source, now=NOW)
    return rank(receipt, c if c is not None else c_input(),
                reasons if reasons is not None else {'m2': 'RESEARCH_EVIDENCE_MISSING'},
                now=at, original_source=source,
                status_refresh=status or fresh_status(receipt, now=at),
                previous_rank=previous)


def readback(result):
    return {
        'spreadsheet_id': result['active_spreadsheet_id'],
        'sheet_name': result['active_sheet'],
        'method': 'INDEPENDENT_GOOGLE_SHEETS_REFETCH',
        'run_id': result['run_id'],
        'rank_integrity_sha256': result['integrity_sha256'],
        'sweep_integrity_sha256': result['sweep_integrity_sha256'],
        'readback_at_utc': LATER,
        'ranked_rows': [{
            'match_id': row['match_id'],
            'coverage_id': result['run_id'] + '|' + row['match_id'],
            'follow_lane': row['follow_lane'], 'c_rank': row['rank'],
            'c_board_state': 'C-' + row['board_state'],
            'c_supported_line': row['supported_line'],
            'step1_engine_c_result': json.dumps(row),
            'step1_engine_c_result_column': 'Step1 Engine C Result',
        } for row in result['board']['matches']],
    }


class RankResearchTests(unittest.TestCase):
    def test_39_fixture_incident_reports_24_pending_and_5_closed(self):
        source = snapshot([fixture(f"m{i}", ko=("2026-10-11T16:03:00Z" if i < 5
                                                 else "2026-10-11T17:00:00Z"))
                           for i in range(39)])
        receipt = sweep(source, now=NOW)
        data = c_input()
        data['matches'] = []
        for i in range(5, 15):
            row = c_input(f"m{i}")['matches'][0]
            if i >= 7:
                make_unfunded_watch(row)
            data['matches'].append(row)
        reasons = {f"m{i}": ('PREMATCH_WINDOW_CLOSED' if i < 5
                              else 'RESEARCH_EVIDENCE_MISSING')
                   for i in range(39) if i < 5 or i >= 15}
        statuses = fresh_status(receipt, now=AT)
        for row in statuses['matches']:
            if int(row['match_id'][1:]) < 5:
                row['fixture_status'] = 'STARTED'
        result = rank(receipt, data, reasons, now=AT, original_source=source,
                      status_refresh=statuses)
        coverage = result['research_coverage']
        self.assertEqual((coverage['full_queue_count'], coverage['assessed_count'],
                          coverage['pending_count'], coverage['status_excluded_count']),
                         (39, 10, 24, 5))
        self.assertEqual((result['ranked_count'], result['watch_count']), (2, 8))
        self.assertEqual(len(result['coverage_manifest']), 39)
        self.assertEqual(len(result['resume_queue']), 24)
        self.assertEqual(verify_rank(readback(result), result)['status'],
                         'V4_RANK_PARTIAL_PERSISTENCE_VERIFIED')

    def test_generic_missing_is_pending_not_completed_or_pass(self):
        result = execute()
        coverage = result['research_coverage']
        self.assertEqual(coverage['status'], 'INCOMPLETE')
        self.assertEqual((coverage['assessed_count'], coverage['pending_count']), (1, 1))
        self.assertEqual(coverage['assessed_open_fraction'], .5)
        self.assertFalse(result['research_complete'])
        self.assertEqual(result['pass_count'], 0)
        self.assertEqual(len(result['coverage_manifest']), 2)
        self.assertEqual(result['resume_queue'][0]['match_id'], 'm2')
        self.assertIn('goal_screen', result['resume_queue'][0])
        expected = c_input()
        expected['matches'][0].update(country='England', competition='Premier League', competition_kind='DOMESTIC_LEAGUE')
        self.assertEqual(result['frozen_model_input'], expected)
        persisted = verify_rank(readback(result), result)
        self.assertEqual(persisted['status'], 'V4_RANK_PARTIAL_PERSISTENCE_VERIFIED')
        self.assertEqual(persisted['research_coverage'], coverage)

    def test_concrete_gap_is_evidence_limited_and_remains_resumable(self):
        result = execute(reasons={'m2': gap()})
        self.assertEqual(result['research_coverage']['status'], 'EVIDENCE_LIMITED')
        self.assertEqual(result['research_coverage']['evidence_limited_count'], 1)
        self.assertFalse(result['research_complete'])
        self.assertEqual(result['research_exclusion_trace']['m2'], gap())
        self.assertEqual(result['resume_queue'][0]['next_action'], gap()['next_action'])

    def test_gap_rejects_wrong_identity_unchecked_fields_and_false_clock(self):
        for change in (
            {'match_id': 'another-match'}, {'missing_fields': ['home_route']},
            {'attempts': []}, {'next_action': ''},
        ):
            with self.subTest(change=change):
                trace = gap()
                trace.update(change)
                with self.assertRaises(StageError):
                    execute(reasons={'m2': trace})
        trace = gap()
        trace['attempts'][0]['checked_at_utc'] = '2026-10-12T16:00:00Z'
        with self.assertRaisesRegex(StageError, 'outside sweep/rank epoch'):
            execute(reasons={'m2': trace})

    def test_budget_checkpoint_needs_no_fabricated_assessment(self):
        data = c_input()
        data['matches'] = []
        result = execute(data, {'m1': 'RESEARCH_BUDGET_EXHAUSTED',
                                'm2': 'RESEARCH_BUDGET_EXHAUSTED'})
        self.assertEqual(result['status'], 'V4_RANK_RESEARCH_PENDING')
        self.assertIsNone(result['board'])
        self.assertEqual(result['research_coverage']['pending_count'], 2)
        resumed = execute(c_input(), {}, previous=result, at=LATER)
        self.assertEqual(resumed['assessed_count'], 1)
        self.assertEqual(resumed['research_coverage']['pending_count'], 1)

    def test_resume_reuses_completed_facts_and_only_needs_new_fixture(self):
        previous = execute()
        untouched = copy.deepcopy(previous)
        result = execute(c_input('m2'), {}, previous=previous, at=LATER)
        self.assertEqual(result['assessed_count'], 2)
        self.assertTrue(result['research_complete'])
        self.assertEqual(result['resume_queue'], [])
        self.assertEqual(result['reused_match_ids'], ['m1'])
        self.assertEqual(result['previous_rank_sha256'], previous['integrity_sha256'])
        self.assertEqual(previous, untouched)
        old_row = next(r for r in result['frozen_model_input']['matches'] if r['match_id'] == 'm1')
        self.assertEqual(old_row, previous['frozen_model_input']['matches'][0])
        persisted = verify_rank(readback(result), result)
        self.assertEqual(persisted['status'], 'V4_RANK_PERSISTENCE_VERIFIED')
        self.assertTrue(persisted['research_complete'])

    def test_resume_excludes_started_reused_fixture_and_preserves_old_receipt(self):
        previous = execute()
        statuses = fresh_status(sweep(snapshot(), now=NOW), now=LATER)
        statuses['matches'][0]['fixture_status'] = 'STARTED'
        result = execute(c_input('m2'), {}, previous=previous, status=statuses, at=LATER)
        self.assertEqual([r['match_id'] for r in result['board']['matches']], ['m2'])
        self.assertEqual(result['unranked_reasons']['m1'], 'PREMATCH_WINDOW_CLOSED')
        self.assertEqual(result['research_coverage']['status_excluded_count'], 1)
        self.assertEqual(previous['board']['matches'][0]['match_id'], 'm1')

    def test_resume_carries_gaps_and_does_not_silently_drop_completed_rows(self):
        previous = execute(reasons={'m2': gap()})
        data = c_input()
        data['matches'] = []
        result = execute(data, {}, previous=previous, at=LATER)
        self.assertEqual(result['research_exclusion_trace']['m2'], gap())
        self.assertEqual(result['reused_match_ids'], ['m1'])
        with self.assertRaisesRegex(StageError, 'discard completed'):
            execute(data, {'m1': 'RESEARCH_EVIDENCE_MISSING'}, previous=previous, at=LATER)

    def test_resume_requires_same_source_and_model_authority(self):
        previous = execute()
        changed = c_input('m2')
        changed['authority_commit'] = 'different-authority'
        with self.assertRaisesRegex(StageError, 'authority_commit'):
            execute(changed, {}, previous=previous, at=LATER)
        from stage import _hash
        previous['sweep_integrity_sha256'] = 'other-source'
        previous['integrity_sha256'] = _hash({k: v for k, v in previous.items() if k != 'integrity_sha256'})
        with self.assertRaisesRegex(StageError, 'source epoch'):
            execute(c_input('m2'), {}, previous=previous, at=LATER)

    def test_watch_stays_reusable_without_inflating_focus_board(self):
        data = c_input()
        make_unfunded_watch(data['matches'][0])
        previous = execute(data)
        resumed = execute(c_input('m2'), {}, previous=previous, at=LATER)
        self.assertEqual(resumed['assessed_count'], 2)
        self.assertEqual(resumed['ranked_count'], 1)
        self.assertEqual(resumed['watch_count'], 1)
        self.assertEqual(resumed['reused_match_ids'], ['m1'])


if __name__ == '__main__':
    unittest.main()
