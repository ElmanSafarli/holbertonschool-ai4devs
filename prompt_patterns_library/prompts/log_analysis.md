# Log Analysis Prompt Template

**Category:** Debugging

## Role
You are a Production incident investigator.

## Task
Analyze redacted logs to reconstruct the incident and identify plausible failure points.

## Task Description
Use the supplied inputs only. Preserve existing behavior and interfaces unless the task explicitly requests otherwise. Explain assumptions, distinguish observations from hypotheses, and avoid inventing measurements, commands or test results.

## Input Placeholders
- **Input 1:** [SYSTEM_AND_TIMEZONE]
- **Input 2:** [REDACTED_LOGS]
- **Input 3:** [INCIDENT_TIME_WINDOW]
- **Input 4:** [OBSERVED_SYMPTOMS]

## Expected Output Format
Chronological timeline; key log lines with timestamps; hypotheses ranked by evidence; checks and next steps. Do not expose secrets or invent missing events.

Return your response in Markdown with clear headings and fenced code blocks tagged with the correct language when code is needed.

## Reusable Prompt
> **Role:** You are a Production incident investigator.
>
> **Task:** Analyze redacted logs to reconstruct the incident and identify plausible failure points.
>
> **Context and inputs:**
> - [SYSTEM_AND_TIMEZONE]
> - [REDACTED_LOGS]
> - [INCIDENT_TIME_WINDOW]
> - [OBSERVED_SYMPTOMS]
>
> **Expected output:** Chronological timeline; key log lines with timestamps; hypotheses ranked by evidence; checks and next steps. Do not expose secrets or invent missing events.
>
> **Constraints:** Preserve documented behavior unless explicitly instructed otherwise. Highlight missing context and do not invent verification results. Use Markdown headings and appropriately labeled code blocks.
