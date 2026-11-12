import json
from pathlib import Path
import subprocess
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer
from helpers import expected


class ContractTest(unittest.TestCase):
    def check(self, text, result):
        analyzer = LogAnalyzer()
        self.assertEqual(analyzer.analyze(text), result)
        self.assertEqual(analyzer.analyze(text), result)

    def test_malformed_no_partial_aggregation(self):
        self.check('v1 /ok 200 10\nbroken\nv2 /bad 600 5\nv3 /bad 200 -1\nv4 /ok 200 2 extra\nv5 /bad 200 01\n',
                   expected(1, 5, 1, 0, 0, 10, [('/ok', 1)]))

