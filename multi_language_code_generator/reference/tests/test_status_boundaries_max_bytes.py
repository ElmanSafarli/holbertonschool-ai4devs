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

    def test_status_boundaries_max_bytes(self):
        self.check('a /x 100 999999999\nb /x 399 0\nc /y 400 1\nd /y 599 2',
                   expected(4, 0, 4, 2, 5000, 1000000002, [('/x', 2), ('/y', 2)]))

