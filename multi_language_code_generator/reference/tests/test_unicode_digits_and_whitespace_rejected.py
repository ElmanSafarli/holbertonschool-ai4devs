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

    def test_unicode_digits_and_whitespace_rejected(self):
        self.check('v /x ２００ 0\nv /x 200 ١\nv\u00a0/x 200 1\nv /é 200 1', expected(invalid=4))

