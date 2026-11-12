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

    def test_visitor_length(self):
        self.check('a' * 64 + ' / 200 0\n' + 'a' * 65 + ' / 200 0',
                   expected(1, 1, 1, 0, 0, 0, [('/', 1)]))

