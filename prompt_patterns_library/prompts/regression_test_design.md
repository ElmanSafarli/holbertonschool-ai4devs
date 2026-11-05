# Regression Test Design Prompt Template

**Category:** Testing

## Role
You are a Software regression test engineer.

## Task
Create a test reproducing the original defect and verifying the fix persists.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [LANGUAGE_AND_TEST_FRAMEWORK]
- **Input 2:** [BUG_REPORT_AND_REPRODUCTION]
- **Input 3:** [ROOT_CAUSE_AND_FIX_DESCRIPTION]
- **Input 4:** [AFFECTED_SOURCE_AND_EXISTING_TESTS]

## Expected Output Format
Regression test code or precise pseudocode; expected failure before fix and pass afterward; edge cases; execution instructions. Do not claim tests were run.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Software regression test engineer.
>
> **Task:** Create a test reproducing the original defect and verifying the fix persists.
>
> **Context and inputs:**
> - [LANGUAGE_AND_TEST_FRAMEWORK]
> - [BUG_REPORT_AND_REPRODUCTION]
> - [ROOT_CAUSE_AND_FIX_DESCRIPTION]
> - [AFFECTED_SOURCE_AND_EXISTING_TESTS]
>
> **Expected output:** Regression test code or precise pseudocode; expected failure before fix and pass afterward; edge cases; execution instructions. Do not claim tests were run.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
