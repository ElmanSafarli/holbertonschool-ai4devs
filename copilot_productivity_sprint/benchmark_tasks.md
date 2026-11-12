# Coding Benchmark Tasks

## Shared Protocol

Each task targets 15–30 minutes per attempt for a developer familiar with JavaScript. This is an estimate, not a measured result. Implement each task once without AI and once with OpenAI Codex, using identical requirements and starting files. Do not reuse the first solution in the second attempt.

Use Node.js and CommonJS modules. Record the actual Node.js version before starting. Use the built-in `node:test` and `node:assert/strict` modules for tests. Task 2 uses the built-in `node:http` module; no external packages are needed.

Timing includes reading requirements, implementation, tests, debugging, and review. Stop when all acceptance criteria pass, or record an incomplete attempt at 30 minutes. Record elapsed time, passed/total tests, nonblank noncomment solution lines, defects, and review observations. Keep tests and solution line counts separate. Do not fabricate results. Use the same test cases for both attempts. Prepare the acceptance checks before either timed attempt and keep them unchanged between trials. Record trial order and acknowledge practice effects; alternate which condition runs first across tasks.

## Task 1 — Summarize Orders

**Category:** Data processing and validation.

**Estimated duration:** 15–30 minutes per attempt.

**Requirements:** Implement and export `summarizeOrders(orders)` in `order_summary.js`. Each order contains `id` (non-empty string), `status` (`paid` or `cancelled`), and `amountCents` (nonnegative safe integer). IDs must be unique. Reject invalid input with `TypeError`; reject a total exceeding JavaScript's safe integer range with `RangeError`. Do not mutate the input. Additional fields may be ignored.

**Inputs:** An array of order objects. Example:

```json
[
  {"id":"o1","status":"paid","amountCents":1200},
  {"id":"o2","status":"cancelled","amountCents":500},
  {"id":"o3","status":"paid","amountCents":800}
]
```

**Outputs:** An object containing `totalOrders`, `paidOrders`, `cancelledOrders`, and `revenueCents`. Revenue includes paid orders only. Expected example:

```json
{"totalOrders":3,"paidOrders":2,"cancelledOrders":1,"revenueCents":2000}
```

**Acceptance criteria:**

- The example produces exactly the output above.
- An empty array returns all four fields with value zero.
- Cancelled amounts are excluded from revenue; zero amounts are valid.
- Non-array input, null entries, missing required fields, whitespace-only IDs, unsupported statuses, fractional/negative/unsafe amounts, and duplicate IDs produce `TypeError`.
- IDs are compared exactly and case-sensitively; whitespace is checked for emptiness but is not otherwise normalized.
- All orders are validated, including cancelled orders.
- Paid revenue exceeding `Number.MAX_SAFE_INTEGER` produces `RangeError`.
- Input arrays and objects are unchanged after processing.
- Automated tests cover valid, empty, invalid, duplicate, overflow, and immutability cases.

## Task 2 — Create a User over HTTP

**Category:** API implementation and integration testing.

**Estimated duration:** 15–30 minutes per attempt.

**Requirements:** Implement `POST /users` using `node:http` in `users_api.js`. Export `createServer()` returning an unstarted HTTP server with its own in-memory user array and ID counter. Do not connect a database or implement authentication. Accept a JSON object with `name` and `email`; ignore additional fields. Trim both fields, lowercase email, and enforce unique normalized email addresses. Store users until that server instance is discarded.

**Inputs:** A POST request with `Content-Type: application/json` (an optional charset is allowed) and body:

```json
{"name":" Ada Lovelace ","email":" ADA@example.com "}
```

**Outputs:** HTTP 201 with JSON:

```json
{"id":1,"name":"Ada Lovelace","email":"ada@example.com"}
```

Errors use JSON `{"error":"<message>"}`; exact message wording is flexible. All responses use `application/json`.

**Acceptance criteria:**

- A valid request returns 201 and the normalized stored user.
- Name must be a string of 1–80 characters after trimming.
- Email must be a string matching `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` after trimming and lowercasing. This is a deliberately simple validation rule.
- Malformed JSON, null/array bodies, missing fields, or invalid name/email return 400.
- A non-JSON content type returns 415.
- Reusing an email with different case or surrounding whitespace returns 409.
- Successful creations receive sequential integer IDs starting at 1. Rejected requests do not consume IDs.
- Other method/path combinations return 404.
- Each server instance has independent state.
- Integration tests start the server on an ephemeral port and close it afterward; cover success, validation, malformed JSON, content type, duplicates, IDs, and unknown routes.

## Task 3 — Repair a Pagination Function

**Category:** Debugging, boundary conditions, and regression testing.

**Estimated duration:** 15–30 minutes per attempt.

**Starting code:** Copy this exact baseline into `paginate.js` for BOTH attempts:

```javascript
function paginate(items, page = 1, pageSize = 10) {
  const start = page * pageSize;
  return {
    items: items.splice(start, pageSize),
    page,
    pageSize,
    totalItems: items.length,
    totalPages: Math.floor(items.length / pageSize)
  };
}

module.exports = { paginate };
```

**Requirements:** Fix and export `paginate(items, page = 1, pageSize = 10)` without changing its public signature or result fields. Pages are one-based. Do not mutate the source array. Reject non-array `items` with `TypeError`. Both numeric arguments must be positive safe integers; otherwise throw `RangeError`. Any item values are allowed; a shallow selection is sufficient.

**Inputs:** Example call:

```javascript
paginate(["a", "b", "c", "d", "e"], 2, 2)
```

**Outputs:**

```json
{"items":["c","d"],"page":2,"pageSize":2,"totalItems":5,"totalPages":3}
```

**Acceptance criteria:**

- The example returns exactly the output above.
- Default arguments select the first 10 items, or all available items if fewer than 10.
- Partial last pages are included; `totalPages` rounds upward.
- An empty source produces `items: []`, `totalItems: 0`, and `totalPages: 0`.
- A page beyond the last returns an empty selection while retaining the requested `page`, `pageSize`, and correct totals.
- Source length, order, and values remain unchanged after repeated calls.
- Zero, negative, fractional, nonnumeric, infinite, and unsafe numeric arguments throw `RangeError`; explicit `undefined` uses the defaults.
- Extremely large but valid page values return an empty selection when beyond the end, without erroneous wraparound.
- Add regression tests covering the original off-by-one, mutation, total-count, and rounding defects, plus empty input and validation.

## Completion and Comparison

A task is complete only when all listed criteria pass. Record actual results separately for each attempt; a generated solution is not automatically a correct solution. Compare time alongside test outcomes, readability, and manual corrections. Do not infer overall productivity from these three tasks alone.
