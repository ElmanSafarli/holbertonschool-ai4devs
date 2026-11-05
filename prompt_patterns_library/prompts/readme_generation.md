# README Generation Prompt Template

**Category:** Documentation

## Role
You are a Developer experience engineer.

## Task
Produce a practical README for installation, local development and common troubleshooting.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [PROJECT_NAME_AND_PURPOSE]
- **Input 2:** [PROJECT_STRUCTURE]
- **Input 3:** [DEPENDENCIES_AND_VERSIONS]
- **Input 4:** [SETUP_AND_RUN_COMMANDS]

## Expected Output Format
README Markdown with overview, prerequisites, setup, configuration placeholders, usage, testing and troubleshooting. Do not fabricate commands or secrets.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Developer experience engineer.
>
> **Task:** Produce a practical README for installation, local development and common troubleshooting.
>
> **Context and inputs:**
> - [PROJECT_NAME_AND_PURPOSE]
> - [PROJECT_STRUCTURE]
> - [DEPENDENCIES_AND_VERSIONS]
> - [SETUP_AND_RUN_COMMANDS]
>
> **Expected output:** README Markdown with overview, prerequisites, setup, configuration placeholders, usage, testing and troubleshooting. Do not fabricate commands or secrets.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
