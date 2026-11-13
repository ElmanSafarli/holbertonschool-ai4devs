# Team Ideation

## Project Context
- Project: AI-Enhanced Team Hackathon — Task 0: Ideation.
- Date: 2026-11-13.
- Format: a planned 24-hour development sprint.
- Status: planning only; implementation, deployment, and team participation have not yet been completed.
- Working product name: BugBrief.

## Brainstormed Ideas

| Idea | Problem and users | Smallest useful product | 24-hour feasibility |
| --- | --- | --- | --- |
| AI Study Sprint | Students spend time turning notes into a practical study plan. | Paste notes and generate a short study checklist with editable tasks. | High, but assessing educational accuracy adds review work. |
| Sender Request Checker | Telecom operations teams repeatedly receive registration requests for the same sender and country. | Submit sender/country/client and flag exact duplicate sender-country pairs. | High for exact matching, but realistic data and registration rules require domain decisions. |
| **BugBrief — AI Bug Report Assistant (chosen)** | Developers and testers receive incomplete, unstructured bug descriptions that slow reproduction and triage. | Turn rough notes into an editable structured bug report and flag missing information. | High with a narrow text-only workflow; builds naturally on the debugging exercises. |

### Selection Rationale
BugBrief combines a concrete development problem with a small end-to-end workflow:
paste notes, generate a draft, review it, and export Markdown. React and a Node.js
backend fit the proposed implementation. The value of AI is visible in the demo,
while the user remains responsible for confirming facts. It requires no production
telecom integration, payments, or organization-wide workflow migration.

## Chosen Problem Statement
Developers and testers often describe bugs in chat messages that omit reproduction
steps, expected results, actual results, or environment details. Maintainers must
ask follow-up questions before they can investigate.

BugBrief helps a reporter convert rough notes into a consistent bug report. The AI
organizes supplied facts, highlights missing details, and proposes questions. It
must not invent reproduction steps, error messages, root causes, or environment
information. The reporter reviews and edits the draft before exporting it.

### Target User and Success Scenario
A tester pastes: "After resetting the filter, orders still show only pending ones
in Chrome." The tool preserves those facts, marks the exact reproduction steps and
browser version as missing, and asks for them. The tester adds details and copies
a structured Markdown report ready to paste into an issue tracker.

## MVP Features
1. **Bug-note input:** A form accepts a short title, rough description, and optional environment details; validates required fields and caps input size.
2. **AI report drafting:** A server-side AI call returns title, reproduction steps, expected result, actual result, environment, and missing-information questions. Unknown facts are explicitly marked "Not provided."
3. **Human review and editing:** Every generated section is editable before export; the UI labels AI output as a draft and warns users to remove secrets or personal data before submission.
4. **Markdown export:** Copy or download the reviewed report as Markdown without automatically creating an external issue.
5. **Resilient demo flow:** Show loading and useful error states. If the AI service is unavailable, offer a clearly labeled manual report template; do not present template output as an AI response.

### MVP Acceptance Criteria
- A valid submission produces all six report sections, even when some contain "Not provided."
- Missing information results in questions rather than invented details.
- Users can edit and export the draft without an account.
- Empty or oversized submissions are rejected with readable messages.
- Invalid provider output or a provider failure leaves the input intact and exposes the manual-template option.
- AI API credentials stay on the server and are never bundled into frontend assets.
- A small synthetic example set checks supplied-fact preservation and missing-field behavior; these checks do not imply AI output is guaranteed accurate.

## Team Roles

The actual team roster has not been supplied. The table assigns responsibilities
for planning; it does not claim that additional people have joined or performed
work. Elman is the proposed coordinator. Unassigned roles must be confirmed before
a real team sprint.

| Member / assignment status | Role | Responsibilities | Handoff / deliverable |
| --- | --- | --- | --- |
| Elman Seferli — proposed coordinator | Product and integration lead | Confirm scope, prioritize backlog, coordinate handoffs, review integration, and own the demo narrative. | Agreed scope, integrated MVP, and demo checklist. |
| Unassigned teammate A | Frontend and UX lead | Build the input form, editable report, loading/error states, and Markdown export. | Working UI against a shared response schema. |
| Unassigned teammate B | Backend and AI prompt lead | Implement the generation endpoint, server-side credentials, output validation, timeout handling, and grounded drafting prompt. | API contract, endpoint, and safe failure behavior. |
| Unassigned teammate C | QA and deployment lead | Test normal/empty/oversized/failure paths, check report fidelity, prepare hosting, and verify the live demo. | Test evidence and deployment instructions. |

AI assistance (Codex/ChatGPT) supports brainstorming, code drafting, test ideas, and
documentation. It is a tool, not a substitute for a human teammate or independent
human review. If this is completed solo, Elman can cover the roles sequentially,
but the retrospective must describe it as a solo simulation.

## Proposed Implementation and Scope Boundaries
- Frontend: React with Vite.
- Backend: Node.js with Express and one report-generation endpoint.
- AI: a server-side provider call with a constrained output schema; exact provider/model selected during implementation.
- Storage: no database in the MVP; keep the current draft in browser memory and allow explicit export.
- Hosting: choose a compatible frontend/backend platform during the deployment task; no deployment is claimed here.
- Excluded: accounts, team workspaces, file uploads, screenshots, automatic issue-tracker posting, code execution, automatic root-cause claims, and production repository integration.
- No autonomous tool execution from submitted text. Report notes are untrusted content to be structured, not instructions that override the drafting prompt.

## Proposed 24-Hour Sprint

| Time from start | Focus | Exit condition |
| --- | --- | --- |
| Hours 0–2 | Scope, user story, wireframe, API schema | Team agrees on the sample input and expected report structure. |
| Hours 2–8 | Frontend and backend development | UI and endpoint work independently against the same schema. |
| Hours 8–14 | AI integration and editable report flow | One complete input-to-export path works with a real provider. |
| Hours 14–19 | Regression checks and failure handling | Input validation, grounded output checks, and fallback paths pass. |
| Hours 19–22 | Deployment and smoke testing | A live demo is checked from a clean browser session. |
| Hours 22–24 | Demo preparation and retrospective | Demo script, known limitations, and honest contribution notes are recorded. |

## Collaboration Plan
- Create short-lived feature branches and review changes before merging.
- Agree on the report schema before implementing either side of the API.
- Keep tasks small and record an owner, acceptance criteria, and blocker for each.
- Check progress at scope agreement, first integration, and pre-deployment.
- Log AI suggestions, important manual corrections, and actual contributions for the later reflection.
- Keep the first working end-to-end path ahead of optional visual polish.

## Main Risks and Mitigations
- **AI invents details:** Explicitly require unknown markers, validate structure, inspect synthetic examples, and require human review before export.
- **Provider configuration or availability blocks the demo:** Verify credentials early and retain a labeled manual-template path.
- **Scope exceeds the sprint:** Defer every feature outside the five-item MVP.
- **Team roster remains incomplete:** Confirm participants before assigning actual work; document a solo simulation honestly if necessary.
