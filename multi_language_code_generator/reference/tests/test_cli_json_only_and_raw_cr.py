import json
from pathlib import Path
import subprocess
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer
from helpers import expected


class ContractTest(unittest.TestCase):
    def test_cli_json_only_and_raw_cr(self):
        script = Path(__file__).resolve().parents[1] / 'log_analyzer.py'
        result = subprocess.run([sys.executable, str(script)], input=b'v /x 200 1\r\r\n', capture_output=True, check=True)
        self.assertEqual(result.stderr, b'')
        self.assertEqual(json.loads(result.stdout), expected(invalid=1))

