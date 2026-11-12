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

    def test_crlf_tabs_root(self):
        self.check('\r\n \t \r\n v1\t/\t200\t0 \r\nv1 /x 400 5\r\n',
                   expected(2, 0, 1, 1, 5000, 5, [('/', 1), ('/x', 1)]))

