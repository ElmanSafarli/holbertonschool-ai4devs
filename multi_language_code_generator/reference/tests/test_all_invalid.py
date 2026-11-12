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

    def test_all_invalid(self):
        self.check('bad! /x 200 1\nv1 /search?q=x 200 1\nv2 /x 200 1.5\nv3 /x 200 1000000000\nv4 /x 0200 1\nv5 /x 200 +1\nv6 /x 200 1e2', expected(invalid=7))

