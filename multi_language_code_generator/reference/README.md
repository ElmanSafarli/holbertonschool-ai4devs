# Python Reference Implementation

Implements the simplified request-log contract in `../cross_language_spec.md` using only the Python standard library.

From the repository root, run all 18 tests:

```sh
python -m unittest discover -s multi_language_code_generator/reference/tests -v
```

Run the CLI (UTF-8 standard input to JSON standard output):

```sh
python multi_language_code_generator/reference/log_analyzer.py < requests.log
```

On Windows PowerShell:

```powershell
Get-Content -Raw -Encoding utf8 requests.log | py multi_language_code_generator/reference/log_analyzer.py
```

Python API: `LogAnalyzer().analyze(text)`. Each call has independent state. Invalid nonblank records are counted and skipped. No third-party dependencies are required. Tests cover all nine specification fixtures, additional parsing boundaries, and subprocess CLI behavior.
