"""Contract fixtures, parser boundaries, and subprocess CLI checks."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


def expected(total=0, invalid=0, visitors=0, errors=0, rate=0, size=0, paths=()):
    return dict(totalRequests=total, invalidLines=invalid, uniqueVisitors=visitors,
                errorRequests=errors, errorRateBps=rate, totalBytes=size,
                topPaths=[dict(path=p, requests=n) for p, n in paths])


class AnalyzerTests(unittest.TestCase):
    def check(self, text, result):
        analyzer = LogAnalyzer()
        self.assertEqual(analyzer.analyze(text), result)
        self.assertEqual(analyzer.analyze(text), result)

    def test_empty(self):
        self.check('', expected())

    def test_mixed(self):
        self.check('v1 /books 200 100\nv2 /authors 404 20\nv1 /books 503 0\n',
                   expected(3, 0, 2, 2, 6667, 120, [('/books', 2), ('/authors', 1)]))

    def test_malformed_no_partial_aggregation(self):
        self.check('v1 /ok 200 10\nbroken\nv2 /bad 600 5\nv3 /bad 200 -1\nv4 /ok 200 2 extra\nv5 /bad 200 01\n',
                   expected(1, 5, 1, 0, 0, 10, [('/ok', 1)]))

    def test_crlf_tabs_root(self):
        self.check('\r\n \t \r\n v1\t/\t200\t0 \r\nv1 /x 400 5\r\n',
                   expected(2, 0, 1, 1, 5000, 5, [('/', 1), ('/x', 1)]))

    def test_top_three_case_order(self):
        self.check('v1 /b 200 1\nv2 /a 200 1\nv3 /c 200 1\nv4 /d 200 1\nv1 /b 200 1\nV1 /A 200 1',
                   expected(6, 0, 5, 0, 0, 6, [('/b', 2), ('/A', 1), ('/a', 1)]))

    def test_status_boundaries_max_bytes(self):
        self.check('a /x 100 999999999\nb /x 399 0\nc /y 400 1\nd /y 599 2',
                   expected(4, 0, 4, 2, 5000, 1000000002, [('/x', 2), ('/y', 2)]))

    def test_all_invalid(self):
        self.check('bad! /x 200 1\nv1 /search?q=x 200 1\nv2 /x 200 1.5\nv3 /x 200 1000000000\nv4 /x 0200 1\nv5 /x 200 +1\nv6 /x 200 1e2', expected(invalid=7))

    def test_round_half_up(self):
        self.check('\n'.join(['v1 /x 500 0'] + ['v1 /x 200 0'] * 31),
                   expected(32, 0, 1, 1, 313, 0, [('/x', 32)]))

    def test_maximum_supported_input(self):
        self.check('\n'.join(['v1 /x 200 999999999'] * 100000),
                   expected(100000, 0, 1, 0, 0, 99999999900000, [('/x', 100000)]))

    def test_blank_lines(self):
        self.check(' \t\n\n\t\r\n', expected())

    def test_visitor_length(self):
        self.check('a' * 64 + ' / 200 0\n' + 'a' * 65 + ' / 200 0',
                   expected(1, 1, 1, 0, 0, 0, [('/', 1)]))

    def test_unicode_digits_and_whitespace_rejected(self):
        self.check('v /x ２００ 0\nv /x 200 ١\nv\u00a0/x 200 1\nv /é 200 1', expected(invalid=4))

    def test_remove_only_one_cr(self):
        self.check('v /x 200 1\r\r\n', expected(invalid=1))

    def test_no_state_between_different_calls(self):
        analyzer = LogAnalyzer()
        analyzer.analyze('v /x 500 1')
        self.assertEqual(analyzer.analyze(''), expected())

    def test_all_errors(self):
        self.check('a /x 400 2\nb /x 599 3', expected(2, 0, 2, 2, 10000, 5, [('/x', 2)]))

    def test_ascii_only_line_separators(self):
        self.check('v /x 200 1\vv /y 200 1', expected(invalid=1))

    def test_cli_json_only_and_raw_cr(self):
        script = Path(__file__).resolve().parents[1] / 'log_analyzer.py'
        result = subprocess.run([sys.executable, str(script)], input=b'v /x 200 1\r\r\n', capture_output=True, check=True)
        self.assertEqual(result.stderr, b'')
        self.assertEqual(json.loads(result.stdout), expected(invalid=1))

    def test_cli_success(self):
        script = Path(__file__).resolve().parents[1] / 'log_analyzer.py'
        result = subprocess.run([sys.executable, str(script)], input=b'v /x 200 7\r\n', capture_output=True, check=True)
        self.assertEqual(result.stderr, b'')
        self.assertEqual(json.loads(result.stdout), expected(1, 0, 1, 0, 0, 7, [('/x', 1)]))


if __name__ == '__main__':
    unittest.main()
