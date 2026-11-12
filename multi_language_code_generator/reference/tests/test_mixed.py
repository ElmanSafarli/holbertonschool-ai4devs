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

    def test_mixed(self):
        self.check('v1 /books 200 100\nv2 /authors 404 20\nv1 /books 503 0\n',
                   expected(3, 0, 2, 2, 6667, 120, [('/books', 2), ('/authors', 1)]))

