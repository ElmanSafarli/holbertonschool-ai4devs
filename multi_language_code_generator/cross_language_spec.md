# Cross-Language Specification — Request Log Analyzer

## Algorithm and Purpose

Analyze a simplified HTTP request log to calculate traffic, unique visitors, HTTP errors, transferred bytes, and the most requested paths. The algorithm combines strict parsing, validation, aggregation, distinct counting, and deterministic ranking.

Implement a Python reference version, then equivalent JavaScript/Node.js and Go versions. All implementations must follow this contract rather than rely on language-specific parsing defaults. This is a simplified educational log format, not the Apache log format.

## Input Format

The logical input is a UTF-8 text string containing zero or more lines. A command-line program receives the string through standard input and prints one JSON result to standard output.

Each nonblank line must have exactly four fields separated by one or more ASCII spaces or tabs:

```text
visitorId path status bytes
```

Example:

```text
v1 /books 200 100
v2 /authors 404 20
v1 /books 503 0
```

Rules:

- Split lines on LF (`\n`). CRLF is accepted by removing exactly one trailing CR (`\r`) from each resulting line before processing. A final newline does not create a record.
- Trim ASCII spaces and tabs from both ends of each line. Empty lines after trimming are ignored: they count as neither valid nor invalid.
- `visitorId` must match `^[A-Za-z0-9_-]{1,64}$`. It is an opaque identifier, not an IP address.
- `path` must match `^/[A-Za-z0-9/_-]*$`. The root path `/` is valid. Queries, fragments, dots, percent encoding, and non-ASCII characters are outside this format.
- `status` must consist of exactly three ASCII digits and represent a number from 100 through 599.
- `bytes` must match `^(0|[1-9][0-9]{0,8})$`, representing an integer from 0 through 999999999. Signs, leading zeros except `0`, decimals, and exponents are invalid.
- Fields are case-sensitive; do not normalize identifiers or paths.
- A malformed nonblank line increments `invalidLines` once and contributes nothing to any other statistic. Never partially aggregate an invalid line.
- Supported inputs contain at most 100000 nonblank lines. Larger inputs, invalid UTF-8, and I/O failures are outside the equivalence contract. This bound keeps every total safely representable as an exact JavaScript integer.

## Output Format

Return a JSON object with exactly these fields. Counters and byte totals are nonnegative integers.

```json
{
  "totalRequests": 3,
  "invalidLines": 0,
  "uniqueVisitors": 2,
  "errorRequests": 2,
  "errorRateBps": 6667,
  "totalBytes": 120,
  "topPaths": [
    {"path": "/books", "requests": 2},
    {"path": "/authors", "requests": 1}
  ]
}
```

- `totalRequests`: number of valid request lines.
- `invalidLines`: number of malformed nonblank lines.
- `uniqueVisitors`: number of distinct visitor IDs among valid lines.
- `errorRequests`: valid requests whose status is 400–599 inclusive. Redirects are not errors.
- `errorRateBps`: error proportion in basis points: 10000 means 100%, 2500 means 25%. For zero valid requests return 0. Otherwise calculate `(errorRequests * 10000 + totalRequests // 2) // totalRequests`, where `//` means integer floor division. This rounds to the nearest basis point, with exact halves rounded upward, without floating-point ambiguity.
- `totalBytes`: sum of bytes across all valid requests, including errors.
- `topPaths`: at most three distinct paths ranked by descending request count. Break ties by ascending ASCII lexicographic path order, case-sensitive. Each entry has exactly `path` and `requests`. Return an empty array when no requests are valid.

JSON key order and whitespace are irrelevant. Array order is significant. Compare parsed JSON values. Print no banners or debugging text to standard output.

## Processing Steps

1. Split and normalize lines using the rules above.
2. Ignore blank lines; validate every field of each remaining line.
3. Count invalid lines and skip them entirely.
4. For valid lines, update request/error/byte counters, a visitor set, and a path-count map.
5. Compute the integer error rate, sort paths with the explicit tie-break rule, and select the first three.
6. Produce the JSON result.

Expected complexity: O(N + P log P) time and O(V + P) aggregation space, excluding input storage, where N is input length, P is distinct valid paths, and V is distinct valid visitors. A full sort is acceptable; optimization is not required.

## Edge Cases

- Empty input, blank lines, trailing newline, and CRLF.
- All lines invalid or valid and invalid lines mixed.
- Repeated visitors and paths; identifiers differing only by case.
- Status boundaries 100, 399, 400, 599, and invalid 600.
- Zero bytes, maximum valid byte value, and invalid numeric representations.
- Fewer than three distinct paths and ties at the third-place cutoff.
- Error-rate rounding, including an exact half-basis-point tie.

## Test Cases

Each JSON block below is a test fixture. Decode `input` as a JSON string before passing it to the analyzer. `expected` is the complete expected output.

### 1. Empty input

```json
{"input":"","expected":{"totalRequests":0,"invalidLines":0,"uniqueVisitors":0,"errorRequests":0,"errorRateBps":0,"totalBytes":0,"topPaths":[]}}
```

### 2. Mixed success and errors

```json
{"input":"v1 /books 200 100\nv2 /authors 404 20\nv1 /books 503 0\n","expected":{"totalRequests":3,"invalidLines":0,"uniqueVisitors":2,"errorRequests":2,"errorRateBps":6667,"totalBytes":120,"topPaths":[{"path":"/books","requests":2},{"path":"/authors","requests":1}]}}
```

### 3. Malformed records do not affect aggregates

```json
{"input":"v1 /ok 200 10\nbroken\nv2 /bad 600 5\nv3 /bad 200 -1\nv4 /ok 200 2 extra\nv5 /bad 200 01\n","expected":{"totalRequests":1,"invalidLines":5,"uniqueVisitors":1,"errorRequests":0,"errorRateBps":0,"totalBytes":10,"topPaths":[{"path":"/ok","requests":1}]}}
```

### 4. CRLF, tabs, root path, and whitespace

```json
{"input":"\r\n \t \r\n v1\t/\t200\t0 \r\nv1 /x 400 5\r\n","expected":{"totalRequests":2,"invalidLines":0,"uniqueVisitors":1,"errorRequests":1,"errorRateBps":5000,"totalBytes":5,"topPaths":[{"path":"/","requests":1},{"path":"/x","requests":1}]}}
```

### 5. Top-three cutoff and case-sensitive sorting

```json
{"input":"v1 /b 200 1\nv2 /a 200 1\nv3 /c 200 1\nv4 /d 200 1\nv1 /b 200 1\nV1 /A 200 1","expected":{"totalRequests":6,"invalidLines":0,"uniqueVisitors":5,"errorRequests":0,"errorRateBps":0,"totalBytes":6,"topPaths":[{"path":"/b","requests":2},{"path":"/A","requests":1},{"path":"/a","requests":1}]}}
```

### 6. Status boundaries and maximum bytes

```json
{"input":"a /x 100 999999999\nb /x 399 0\nc /y 400 1\nd /y 599 2","expected":{"totalRequests":4,"invalidLines":0,"uniqueVisitors":4,"errorRequests":2,"errorRateBps":5000,"totalBytes":1000000002,"topPaths":[{"path":"/x","requests":2},{"path":"/y","requests":2}]}}
```

### 7. All invalid: identifiers, paths, and numeric syntax

```json
{"input":"bad! /x 200 1\nv1 /search?q=x 200 1\nv2 /x 200 1.5\nv3 /x 200 1000000000\nv4 /x 0200 1\nv5 /x 200 +1\nv6 /x 200 1e2","expected":{"totalRequests":0,"invalidLines":7,"uniqueVisitors":0,"errorRequests":0,"errorRateBps":0,"totalBytes":0,"topPaths":[]}}
```

### 8. Exact rounding tie (generated fixture)

Build an input of 32 lines: one line `v1 /x 500 0`, followed by 31 lines `v1 /x 200 0`, joined with LF. Expected output:

```json
{"totalRequests":32,"invalidLines":0,"uniqueVisitors":1,"errorRequests":1,"errorRateBps":313,"totalBytes":0,"topPaths":[{"path":"/x","requests":32}]}
```

The exact unrounded error rate is 312.5 basis points, so the result must round upward to 313.

### 9. Maximum supported record count (generated fixture)

Repeat `v1 /x 200 999999999` exactly 100000 times, joined with LF. Expected output:

```json
{"totalRequests":100000,"invalidLines":0,"uniqueVisitors":1,"errorRequests":0,"errorRateBps":0,"totalBytes":99999999900000,"topPaths":[{"path":"/x","requests":100000}]}
```

## Acceptance and Future Validation

- Every language must pass all nine fixtures against the specified outputs, not only against the reference implementation.
- Repeat each fixture to verify deterministic output and absence of retained state between runs.
- Equivalent integer values and exact path/visitor semantics must hold across languages.
- Use the same generated inputs for later performance measurements. Record runtime/compiler versions, build flags, hardware, warm-up policy, and whether process startup/I/O is included. Do not report benchmark results until measured.
- This document defines the contract only; implementations and measured performance belong to later tasks.
