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

    def test_maximum_supported_input(self):
        self.check('\n'.join(['v1 /x 200 999999999'] * 100000),
                   expected(100000, 0, 1, 0, 0, 99999999900000, [('/x', 100000)]))

