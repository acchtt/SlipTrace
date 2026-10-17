import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent / 'tools'))
import work_sweep as work
from test_source_completeness import source, NOW


def event(mid='100', score='FT', home='1', away='2', kickoff='20261010180000'):
    return {'Eid': mid, 'Eps': score, 'Esid': 1, 'Esd': kickoff,
            'T1': [{'ID': home, 'Nm': 'Home U23'}], 'T2': [{'ID': away, 'Nm': 'Away'}], 'Tr1': '3', 'Tr2': '2'}


class WorkSweepTests(unittest.TestCase):
    def test_competitive_history_excludes_friendlies_extra_time_and_wrong_team(self):
        payload = {'ID': '1', 'Stages': [
            {'Snm': 'Club Friendlies', 'Events': [event('friendly')]},
            {'Snm': 'Premier League', 'Events': [event(), event('aet', 'AET')]}]}
        rows = work.competitive_history(payload, '1', work.stamp(NOW))
        self.assertEqual([r['event_id'] for r in rows], ['100'])
        self.assertEqual(rows[0]['goals_for'], 3)
        payload['Stages'][1]['Events'] = [event(home='7', away='8')]
        with self.assertRaisesRegex(ValueError, 'unrelated'):
            work.competitive_history(payload, '1', work.stamp(NOW))

    def test_competition_scope_does_not_filter_adult_league_by_team_name(self):
        block = {'Snm': 'Premier League', 'Cnm': 'England', 'Events': [event()]}
        self.assertEqual(len(work.stage_blocks({'Stages': [block]})), 1)
        block['Snm'] = 'U23 Premier League'
        self.assertEqual(work.stage_blocks({'Stages': [block]}), [])
        block['Snm'] = 'UEFA Youth League'
        self.assertEqual(len(work.stage_blocks({'Stages': [block]})), 1)

    def test_unknown_status_and_pagination_fail_closed(self):
        self.assertEqual(work.event_status(event(score='mystery')), 'UNKNOWN_PROVIDER_STATUS')
        with self.assertRaisesRegex(ValueError, 'pagination'):
            work.stage_blocks({'Stages': [], 'hasMore': True})
        block = {'Snm': 'Premier League', 'Cnm': 'England', 'Events': [event(), event()]}
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            work.stage_blocks({'Stages': [block]})

    def test_listing_ready_does_not_stop_research_and_native_handoff_replays(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = source()
            request = {'run_id': original['run_id'], 'window_start_ict': original['window_start_utc'], 'window_end_ict': original['window_end_utc']}
            work.save(root / 'request.json', request)
            work.save(root / 'saved.json', original)
            before = (root / 'saved.json').read_bytes()
            with patch.object(work, 'utcnow', return_value=NOW), patch.object(work, 'acquire', side_effect=AssertionError('must not reacquire')), patch.object(work, 'research', wraps=work.research) as research:
                code = work.run(root / 'request.json', root / 'out', root / 'saved.json')
            self.assertEqual(code, 0)
            research.assert_called_once()
            self.assertEqual((root / 'saved.json').read_bytes(), before)
            self.assertEqual((root / 'out/original-source.json').read_bytes(), before)
            checkpoint = json.loads((root / 'out/checkpoint.json').read_text())
            self.assertEqual(checkpoint['status'], 'RESEARCH_PENDING')
            handoff = json.loads((root / 'out/rank-handoff.json').read_text())
            final_source = json.loads((root / 'out/source.json').read_text())
            replay = work.sweep(final_source, now=NOW)
            self.assertEqual(replay['integrity_sha256'], handoff['receipt_integrity_sha256'])
            self.assertEqual(work.digest(root / 'out/source.json'), handoff['source_file_sha256'])

    def test_full_mocked_provider_to_native_eligible_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture = event('100', 'NS', kickoff='20261012190000')
            block = {'Snm': 'Premier League', 'Cnm': 'England', 'Events': [fixture]}
            def fetch(url):
                if '/date/' in url:
                    payload = {'Stages': [block]}
                else:
                    team = url.split('/team/')[1].split('/')[0]
                    games = [event(str(200 + i), kickoff=f'2026100{i+1}180000') for i in range(4)]
                    payload = {'ID': team, 'Stages': [{'Snm': 'Premier League', 'Events': games + [fixture]}]}
                return json.dumps(payload).encode(), NOW
            work.save(root / 'request.json', {'run_id': 'V4-test', 'window_start_ict': '2026-10-12T18:10:00Z', 'window_end_ict': '2026-10-12T20:00:00Z'})
            with patch.object(work, 'utcnow', return_value=NOW), patch.object(work, 'fetch', side_effect=fetch) as fetcher:
                self.assertEqual(work.run(root / 'request.json', root / 'out'), 0)
            receipt = json.loads((root / 'out/v4_sweep_ready.json').read_text())
            self.assertEqual(receipt['eligible_count'], 1)
            self.assertEqual(receipt['eligible_queue'][0]['intake_lane'], 'GOAL_PRIORITY')
            self.assertEqual(fetcher.call_count, 5)  # ICT + UTC + independent terminal + two teams
            self.assertEqual(json.loads((root / 'out/checkpoint.json').read_text())['status'], 'RESEARCH_COMPLETE')

    def test_terminal_union_mismatch_blocks_before_history_fetch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture = event('100', 'NS', kickoff='20261012190000')
            block = {'Snm': 'Premier League', 'Cnm': 'England', 'Events': [fixture]}
            work.save(root / 'request.json', {'run_id': 'V4-test', 'window_start_ict': '2026-10-12T18:10:00Z', 'window_end_ict': '2026-10-12T20:00:00Z'})
            responses = [(json.dumps({'Stages': [block]}).encode(), NOW)] * 2 + [(b'{"Stages": []}', NOW)]
            with patch.object(work, 'utcnow', return_value=NOW), patch.object(work, 'fetch', side_effect=responses) as fetcher:
                self.assertEqual(work.run(root / 'request.json', root / 'out'), 2)
            self.assertEqual(fetcher.call_count, 3)
            self.assertFalse((root / 'out/rank-handoff.json').exists())
            self.assertTrue((root / 'out/provenance.json').exists())

    def test_resume_output_cannot_overwrite_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            work.save(root / 'out/source.json', {'preserve': True})
            with self.assertRaisesRegex(ValueError, 'fresh'):
                work.run(root / 'request.json', root / 'out')
            self.assertEqual(json.loads((root / 'out/source.json').read_text()), {'preserve': True})

    def test_time_budget_preserves_order_without_starting_more_network_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = source()
            receipt = work.sweep(original, now=NOW)
            checkpoint = {'fixtures': {}}
            with patch.object(work.time, 'monotonic', side_effect=[0, 1201]), patch.object(work, 'fetch', side_effect=AssertionError('budget exhausted')):
                work.research(original, receipt, work.Evidence(root), checkpoint)
            self.assertEqual(checkpoint['unfinished_research_order'], receipt['goal_research_order'])
            self.assertTrue((root / 'checkpoint.json').exists())

    def test_expired_request_performs_no_network_and_keeps_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            work.save(root / 'request.json', {'run_id': 'V4-old', 'window_start_ict': '2020-01-01T00:00:00Z', 'window_end_ict': '2020-01-01T01:00:00Z'})
            with patch.object(work, 'fetch', side_effect=AssertionError('network forbidden')):
                self.assertEqual(work.run(root / 'request.json', root / 'out'), 2)
            result = json.loads((root / 'out/checkpoint.json').read_text())
            self.assertIn('REQUEST_WINDOW_EXPIRED', result['error'])
            self.assertFalse((root / 'out/rank-handoff.json').exists())

    def test_failure_preserves_original_and_does_not_backdate_stale_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = source()
            original['source_observed_at_utc'] = '2020-01-01T00:00:00Z'
            work.save(root / 'source.json', original)
            work.save(root / 'request.json', {'run_id': original['run_id'], 'window_start_ict': original['window_start_utc'], 'window_end_ict': original['window_end_utc']})
            with patch.object(work, 'utcnow', return_value=NOW):
                self.assertEqual(work.run(root / 'request.json', root / 'out', root / 'source.json'), 2)
            self.assertTrue((root / 'out/original-source.json').exists())
            self.assertFalse((root / 'out/v4_sweep_ready.json').exists())
            self.assertIn('stale', json.loads((root / 'out/checkpoint.json').read_text())['error'])


if __name__ == '__main__':
    unittest.main()
