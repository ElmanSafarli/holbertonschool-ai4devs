# Pull Request: Add Task Filtering by Status, Due Date, and Title

## Summary
Implement a dependency-free Python task filtering feature for the AI Code Review
Simulator. Callers can combine status, inclusive due-date bounds, and a
case-insensitive title search while preserving the original task order.

## Changes
- Add an immutable `Task` model and `Status` enum with input validation.
- Add `filter_tasks()` with combined AND filters and support for iterable input.
- Validate canonical ISO calendar dates and reject reversed date ranges.
- Exclude undated tasks when a date bound is supplied.
- Add 12 unit tests covering normal behavior, invalid inputs, Unicode search,
  empty results, generators, leap dates, and immutability.
- Add usage instructions and reproducible test commands.

## Context
Task 0 of the AI Code Review Simulator requires a meaningful feature of roughly
100–200 lines and a structured PR description. The feature implementation is
102 lines, excluding tests and documentation. This self-contained task filtering
module provides concrete validation and boundary behavior for later AI and human
reviews. No related issue exists; this PR implements the assignment directly.

## Validation
Run from the repository root with Python 3.10 or newer:

```sh
python -m unittest discover -s ai_code_review_simulator/tests -v
python -m unittest discover -s multi_language_code_generator/reference/tests -v
```

Results: all 12 new tests and all 18 existing tests passed (30 total).
No external packages are required.

## Scope
This PR supplies an in-memory Python API. Persistence, HTTP endpoints, pagination,
and later assignment stages (AI review, human comparison, reflection) are outside
Task 0. The pull request remains open for review.
