# Performance Optimization Prompt Template

**Category:** Code Quality

## Role
You are a Performance engineer.

## Task
Identify bottlenecks and optimize runtime or memory use without changing expected results.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [LANGUAGE]
- **Input 2:** [SLOW_FUNCTION]
- **Input 3:** [SAMPLE_INPUTS_AND_CONSTRAINTS]
- **Input 4:** [PERFORMANCE_TARGET]

## Expected Output Format
Optimized code; before/after time and space complexity analysis; suggested benchmark; correctness and trade-off notes. Do not invent benchmark measurements.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Performance engineer.
>
> **Task:** Identify bottlenecks and optimize runtime or memory use without changing expected results.
>
> **Context and inputs:**
> - [LANGUAGE]
> - [SLOW_FUNCTION]
> - [SAMPLE_INPUTS_AND_CONSTRAINTS]
> - [PERFORMANCE_TARGET]
>
> **Expected output:** Optimized code; before/after time and space complexity analysis; suggested benchmark; correctness and trade-off notes. Do not invent benchmark measurements.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
