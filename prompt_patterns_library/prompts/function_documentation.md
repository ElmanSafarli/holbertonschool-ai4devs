# Function Documentation Prompt Template

**Category:** Documentation

## Role
You are a Technical documentation engineer.

## Task
Write accurate documentation for the provided function without assuming undocumented behavior.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [LANGUAGE]
- **Input 2:** [FUNCTION_SIGNATURE_AND_SOURCE]
- **Input 3:** [PARAMETER_AND_RETURN_EXPECTATIONS]
- **Input 4:** [DOCUMENTATION_STYLE]

## Expected Output Format
Ready-to-paste docstring; parameters; return type/value; raised errors; one usage example; unanswered questions when behavior is ambiguous.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Technical documentation engineer.
>
> **Task:** Write accurate documentation for the provided function without assuming undocumented behavior.
>
> **Context and inputs:**
> - [LANGUAGE]
> - [FUNCTION_SIGNATURE_AND_SOURCE]
> - [PARAMETER_AND_RETURN_EXPECTATIONS]
> - [DOCUMENTATION_STYLE]
>
> **Expected output:** Ready-to-paste docstring; parameters; return type/value; raised errors; one usage example; unanswered questions when behavior is ambiguous.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
