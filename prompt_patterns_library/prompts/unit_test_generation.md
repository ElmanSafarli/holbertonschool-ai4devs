# Unit Test Generation Prompt Template

**Category:** Testing

## Role
You are a Senior test automation engineer.

## Task
Design and write unit tests verifying the function's documented behavior.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [LANGUAGE_AND_TEST_FRAMEWORK]
- **Input 2:** [FUNCTION_SOURCE]
- **Input 3:** [EXPECTED_BEHAVIOR]
- **Input 4:** [EDGE_CASES_AND_DEPENDENCIES]

## Expected Output Format
Runnable unit-test code where possible; normal, edge and invalid cases; mock strategy; assertions and run command. State unverified assumptions.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Senior test automation engineer.
>
> **Task:** Design and write unit tests verifying the function's documented behavior.
>
> **Context and inputs:**
> - [LANGUAGE_AND_TEST_FRAMEWORK]
> - [FUNCTION_SOURCE]
> - [EXPECTED_BEHAVIOR]
> - [EDGE_CASES_AND_DEPENDENCIES]
>
> **Expected output:** Runnable unit-test code where possible; normal, edge and invalid cases; mock strategy; assertions and run command. State unverified assumptions.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
