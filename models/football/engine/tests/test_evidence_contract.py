import copy
import unittest

from adapter import ContractError, _g4_research_profile, parse_assessment, run_board
from core import c_goal4_funded
from evidence_contract import g4_diagnostics
from evidence_fixtures import attach_g4_evidence
from production_scope import scope_profile
from test_board_pair import c_row, payload
from test_football_assessment_pair import football
from test_xi_user_screenshot_only import snapshot
from xi_portable import _football_and_optional_price


def rejected():
    row = c_row()
    row.update(independent_upper_tail=False,
               g4_research_status='G4_RESEARCH_COMPLETE_REJECTED',
               g4_carrier_path='FAILED', g4_distributed_path='FAILED',
               g4_reply_path='FAILED', g4_continuation_after_g3='MEDIUM',
               g4_research_basis='Synthetic prospective negative research')
    return attach_g4_evidence(row)


def review(row):
    return _g4_research_profile(row, parse_assessment(row), model='c')


class EvidenceContractTests(unittest.TestCase):
    def test_resolved_negative_is_complete(self):
        self.assertEqual(review(rejected())['g4_evidence_disposition'], 'NEGATIVE')

    def test_missing_evidence_is_pending_and_input_immutable(self):
        row = rejected()
        del row['g4_path_evidence']
        original = copy.deepcopy(row)
        self.assertEqual(review(row)['g4_research_status'], 'G4_RESEARCH_INCOMPLETE')
        self.assertEqual(row, original)
        self.assertIn('G4_REJECTION_EVIDENCE_GAPS', run_board(payload('c', row))['qa_flags'])

    def test_xi_scope_block_does_not_emit_manual_price_verdict(self):
        data = football('c', status='PREMATCH_CONFIRMED', score=None, minute=None, event='NONE_VERIFIED')
        data['match'].update(country='Netherlands', competition='Eredivisie Women', competition_kind='WOMENS_TOP_FLIGHT')
        result = _football_and_optional_price(data, price_c=None, screenshot=snapshot(data))
        self.assertEqual(result['price_check']['status'], 'PRODUCTION_SCOPE_BLOCKED')
        self.assertFalse(result['price_check']['execution_authorized'])

    def test_unavailable_is_limited_not_negative(self):
        row = rejected()
        for key in row['g4_path_evidence']:
            row[key] = 'UNAVAILABLE'
        self.assertEqual(review(row)['g4_evidence_disposition'], 'EVIDENCE_LIMITED')

    def test_mixed_is_not_negative(self):
        row = rejected()
        row['g4_reply_path'] = 'MIXED'
        self.assertEqual(review(row)['g4_evidence_disposition'], 'MIXED')

    def test_supported_route_requires_actual_global_blocker(self):
        row = rejected()
        row['g4_carrier_path'] = 'SUPPORTED'
        self.assertIn('g4_global_blockers', review(row)['g4_evidence_gaps'])
        row['g4_global_blockers'] = [{
            'condition': 'INDEPENDENT_TRANSFERABLE_TAIL_REQUIRED',
            'basis': 'Synthetic transferable tail absent', 'evidence_refs': ['pre-match-source']}]
        self.assertFalse(review(row)['g4_evidence_gaps'])

    def test_reply_uncertainty_does_not_prove_carrier_failure(self):
        row = rejected()
        row['failure_mechanisms']['test-mechanism']['kind'] = 'OPPONENT_REPLY_ONLY'
        self.assertIn('g4_carrier_path.reply_only_is_not_carrier_failure', review(row)['g4_evidence_gaps'])

    def test_shared_mechanism_is_identified_without_changing_grades(self):
        row = rejected()
        before = parse_assessment(row)
        result = review(row)
        self.assertEqual(len(result['shared_failure_mechanisms']), 1)
        self.assertEqual(before, parse_assessment(row))
        self.assertFalse(result['predictive_grades_changed_by_evidence_contract'])

    def test_stall_requires_identified_mechanism(self):
        row = rejected()
        row['burden_stall_risk'] = 'HIGH'
        row['grade_evidence']['burden_stall_risk']['mechanism_ids'] = []
        self.assertIn('burden_stall_risk.high_requires_mechanism', review(row)['g4_evidence_gaps'])

    def test_carrier_can_fund_g4_with_weak_reply(self):
        row = c_row()
        row['away_route'] = 'WEAK'
        a = parse_assessment(row)
        self.assertTrue(c_goal4_funded(a))
        self.assertTrue(g4_diagnostics(a)['goal4_funded'])

    def test_scope_excludes_dutch_women_but_allows_japan(self):
        row = c_row()
        row.update(country='Netherlands', competition='Eredivisie Women', competition_kind='WOMENS_TOP_FLIGHT')
        self.assertFalse(scope_profile(row)['production_allowed'])
        with self.assertRaisesRegex(ContractError, 'SCOPE'):
            run_board(payload('c', row))
        row.update(country='Japan', competition='WE League')
        self.assertTrue(scope_profile(row)['production_allowed'])

    def test_missing_scope_and_exception_are_not_production(self):
        self.assertFalse(scope_profile({})['production_allowed'])
        row = c_row()
        row.update(country='Netherlands', competition='Eredivisie Women', competition_kind='WOMENS_TOP_FLIGHT')
        context = {'scope_override': {'match_id': row['match_id'], 'policy': 'FOOTBALL_C_SCOPE_V1',
                   'authorization': 'EXPLICIT_USER_SCOPE_EXCEPTION', 'user_instruction_reference': 'user-message', 'basis': 'explicit exception'}}
        result = scope_profile(row, context)
        self.assertEqual(result['status'], 'EXPLICIT_OUT_OF_SCOPE_ANALYSIS')
        self.assertFalse(result['production_allowed'])


if __name__ == '__main__':
    unittest.main()
