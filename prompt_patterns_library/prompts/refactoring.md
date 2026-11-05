# Refactoring Prompt Template

**Category:** Code Quality

## Role
You are a Senior software engineer.

## Task
Refactor the provided [LANGUAGE] code for readability, maintainability and clear naming while preserving externally observable behavior.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [LANGUAGE]
- **Input 2:** [CODE_BLOCK]
- **Input 3:** [INTENDED_BEHAVIOR]
- **Input 4:** [CONSTRAINTS]

## Expected Output Format
Refactored code; concise summary of modifications; explanation of how behavior is preserved; any risks or missing tests.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Senior software engineer.
>
> **Task:** Refactor the provided [LANGUAGE] code for readability, maintainability and clear naming while preserving externally observable behavior.
>
> **Context and inputs:**
> - [LANGUAGE]
> - [CODE_BLOCK]
> - [INTENDED_BEHAVIOR]
> - [CONSTRAINTS]
>
> **Expected output:** Refactored code; concise summary of modifications; explanation of how behavior is preserved; any risks or missing tests.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
