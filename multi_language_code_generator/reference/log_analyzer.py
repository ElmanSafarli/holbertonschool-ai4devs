"""Reference analyzer for the simplified request-log specification."""

import json
import re
import sys
from collections import Counter


class LogAnalyzer:
    """Stateless parser and aggregator; each analyze call is independent."""

    def parse_line(self, line: str):
        """Return validated fields, or None for a malformed normalized line."""
        fields = re.split(r"[ \t]+", line)
        if len(fields) != 4:
            return None
        visitor, path, status, size = fields
        if not (
            re.fullmatch(r"[A-Za-z0-9_-]{1,64}", visitor)
            and re.fullmatch(r"/[A-Za-z0-9/_-]*", path)
            and re.fullmatch(r"[1-5][0-9]{2}", status)
            and re.fullmatch(r"0|[1-9][0-9]{0,8}", size)
        ):
            return None
        return visitor, path, int(status), int(size)

    def analyze(self, text: str) -> dict:
        """Analyze LF/CRLF text and return the specified JSON-compatible object."""
        total = invalid = errors = byte_total = 0
        visitors = set()
        paths = Counter()
        for line in text.split("\n"):
            if line.endswith("\r"):
                line = line[:-1]
            line = line.strip(" \t")
            if not line:
                continue
            record = self.parse_line(line)
            if record is None:
                invalid += 1
                continue
            visitor, path, status, size = record
            total += 1
            errors += status >= 400
            byte_total += size
            visitors.add(visitor)
            paths[path] += 1
        ranked = sorted(paths.items(), key=lambda item: (-item[1], item[0]))[:3]
        return {
            "totalRequests": total,
            "invalidLines": invalid,
            "uniqueVisitors": len(visitors),
            "errorRequests": errors,
            "errorRateBps": (errors * 10000 + total // 2) // total if total else 0,
            "totalBytes": byte_total,
            "topPaths": [{"path": path, "requests": count} for path, count in ranked],
        }


def main():
    """Read UTF-8 bytes without universal-newline conversion; emit only JSON."""
    text = sys.stdin.buffer.read().decode("utf-8")
    json.dump(LogAnalyzer().analyze(text), sys.stdout)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
