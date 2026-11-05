# API Endpoint Documentation Prompt Template

**Category:** Documentation

## Role
You are a API technical writer.

## Task
Document the endpoint with its contract and safe, realistic examples.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [HTTP_METHOD_AND_ROUTE]
- **Input 2:** [REQUEST_SCHEMA_AND_AUTH]
- **Input 3:** [RESPONSE_SCHEMA_AND_STATUS_CODES]
- **Input 4:** [VALIDATION_AND_ERROR_CODES]

## Expected Output Format
Markdown endpoint reference including purpose, authentication, path/query/body fields, request/response examples, success and error cases. Mark unknown fields as TBD.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a API technical writer.
>
> **Task:** Document the endpoint with its contract and safe, realistic examples.
>
> **Context and inputs:**
> - [HTTP_METHOD_AND_ROUTE]
> - [REQUEST_SCHEMA_AND_AUTH]
> - [RESPONSE_SCHEMA_AND_STATUS_CODES]
> - [VALIDATION_AND_ERROR_CODES]
>
> **Expected output:** Markdown endpoint reference including purpose, authentication, path/query/body fields, request/response examples, success and error cases. Mark unknown fields as TBD.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
