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

    def test_round_half_up(self):
        self.check('\n'.join(['v1 /x 500 0'] + ['v1 /x 200 0'] * 31),
                   expected(32, 0, 1, 1, 313, 0, [('/x', 32)]))

