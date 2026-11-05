# Prompt Use Cases

This document identifies reusable AI prompt use cases for software-development workflows. Each use case describes a goal, input, and expected output.

## Code Quality

### 1. Refactoring
- **Goal:** Improve readability and maintainability without changing behavior.
- **Input:** An existing function in `[LANGUAGE]` and its intended behavior.
- **Output:** Refactored code, an explanation of changes, and confirmation of preserved behavior.

### 2. Style Enforcement
- **Goal:** Apply consistent naming, formatting, and project conventions.
- **Input:** A code block, the language, and a style guide (for example, PEP 8).
- **Output:** Reformatted code and a brief list of style issues fixed.

### 3. Performance Optimization
- **Goal:** Reduce unnecessary computation or memory usage.
- **Input:** A slow function, sample inputs, and performance constraints.
- **Output:** An optimized implementation, complexity comparison, and potential trade-offs.

## Debugging

### 4. Error Explanation
- **Goal:** Understand an error and identify likely causes.
- **Input:** An error message, relevant stack trace, and the related code.
- **Output:** A plain-language explanation, likely root causes, and diagnostic steps.

### 5. Bug Fix Proposal
- **Goal:** Fix a reproducible defect with minimal code changes.
- **Input:** Bug description, expected versus actual behavior, and relevant source code.
- **Output:** A proposed patch, explanation of the root cause, and a regression test.

### 6. Log Analysis
- **Goal:** Find patterns that explain application failures.
- **Input:** Redacted application logs and the time window of an incident.
- **Output:** A timeline, suspicious log entries, possible causes, and next checks.

## Documentation

### 7. Function Documentation
- **Goal:** Explain how a function should be used.
- **Input:** A function signature, source code, and language.
- **Output:** A docstring describing parameters, return values, exceptions, and an example.

### 8. README Generation
- **Goal:** Help developers set up and run a project.
- **Input:** Project structure, dependencies, installation steps, and available commands.
- **Output:** A README with prerequisites, setup instructions, usage, and troubleshooting.

### 9. API Endpoint Documentation
- **Goal:** Describe an API endpoint for consumers.
- **Input:** HTTP method, route, request schema, response schema, and error codes.
- **Output:** Endpoint documentation with sample requests and responses.

## Testing

### 10. Unit Test Generation
- **Goal:** Verify the expected behavior of an individual function.
- **Input:** Function code, expected behavior, and a test framework.
- **Output:** Unit tests covering normal inputs, edge cases, and invalid inputs.

### 11. Integration Test Planning
- **Goal:** Validate that multiple components work together.
- **Input:** Service architecture, API contracts, and a user workflow.
- **Output:** Integration test scenarios, setup requirements, and expected results.

### 12. Regression Test Design
- **Goal:** Prevent a previously fixed bug from returning.
- **Input:** Bug report, root cause, and description of the fix.
- **Output:** A regression test that fails before the fix and passes afterward.

## Summary

- **Code Quality:** 3 use cases
- **Debugging:** 3 use cases
- **Documentation:** 3 use cases
- **Testing:** 3 use cases
- **Total:** 12 use cases
