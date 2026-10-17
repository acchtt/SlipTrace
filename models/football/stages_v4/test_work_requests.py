import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parent / 'tools'))
import work_requests as requests


class RequestSelectionTests(unittest.TestCase):
    def test_pr_and_first_branch_push_never_replay_old_requests(self):
        with patch.object(requests.subprocess, 'check_output', side_effect=AssertionError('no diff')):
            self.assertEqual(requests.select({}, 'pull_request'), [])
            self.assertEqual(requests.select({'before': '0' * 40}, 'push'), [])

    def test_code_only_push_does_not_acquire_and_changed_requests_are_scoped(self):
        event = {'before': 'a' * 40, 'after': 'b' * 40}
        with patch.object(requests.subprocess, 'check_output', return_value=''):
            self.assertEqual(requests.select(event, 'push'), [])
        name = requests.PREFIX + 'V4-new.json'
        with patch.object(requests.subprocess, 'check_output', return_value=name + '\n'), patch.object(requests, 'validated_path', side_effect=lambda x: x):
            self.assertEqual(requests.select(event, 'push'), [{'request': name, 'source': ''}])

    def test_path_traversal_and_outside_source_rejected(self):
        for name in ('/tmp/request.json', requests.PREFIX + '../source.json', 'models/football/other.json'):
            with self.assertRaises(ValueError):
                requests.validated_path(name)
