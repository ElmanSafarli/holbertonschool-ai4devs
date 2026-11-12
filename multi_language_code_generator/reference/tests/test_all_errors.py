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

    def test_all_errors(self):
        self.check('a /x 400 2\nb /x 599 3', expected(2, 0, 2, 2, 10000, 5, [('/x', 2)]))

