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

    def test_top_three_case_order(self):
        self.check('v1 /b 200 1\nv2 /a 200 1\nv3 /c 200 1\nv4 /d 200 1\nv1 /b 200 1\nV1 /A 200 1',
                   expected(6, 0, 5, 0, 0, 6, [('/b', 2), ('/A', 1), ('/a', 1)]))

