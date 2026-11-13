# User Stories — BugBrief

## Scope and status
Planning for the five MVP features in team_ideation.md. No accounts, persistent
database, attachments, or automatic issue posting are required. These are planned
acceptance criteria, not claims of completed implementation or executed tests.
P0 stories define the usable MVP; P1 improves usability within the sprint.

## US-01 — Describe a bug (P0)
As a tester, I want to enter a title, rough notes, and optional environment details,
so that I can turn an informal observation into a useful report.
- Given the input form, when I submit valid fields, the app sends a generation request.
- The title and notes are required; environment may be omitted.
- Fields remain available when I navigate between input and draft views.

## US-02 — Receive clear validation feedback (P0)
As a reporter, I want invalid input explained beside the relevant field,
so that I can correct it without losing my notes.
- Empty or whitespace-only title/notes are rejected before a provider call.
- Title is limited to 200, notes to 10,000, and environment to 2,000 JavaScript UTF-16 code units.
- Client and server enforce the same field rules; unknown fields and non-string values are rejected by the server.
- Oversized bodies are rejected at the server's 64 KiB JSON-body boundary.

## US-03 — Generate a structured draft (P0)
As a developer, I want my notes organized into consistent sections,
so that maintainers can read the report quickly.
- A successful response includes title, reproduction steps, expected result, actual result, environment, and missing-information questions.
- The server validates provider output before the UI accepts it.
- Generated output is visibly labeled as an AI draft requiring review.

## US-04 — Identify missing facts (P0)
As a maintainer, I want missing information called out,
so that I know what to ask the reporter.
- The drafting prompt requires absent facts to appear as "Not provided." instead of invented claims.
- Missing details produce actionable questions; no questions are represented by an empty array.
- A sparse synthetic input is inspected for unsupported steps, versions, errors, or root causes.
- Schema validation checks structure only; human review still checks factual accuracy.

## US-05 — Edit every report section (P0)
As a reporter, I want to correct and complete the generated draft,
so that the exported report reflects what I actually observed.
- All six sections are editable, including steps and missing-information questions.
- Edits are retained while copying or downloading in the current tab.
- Clearing a required section produces export validation feedback.
- The AI is not called again merely because I type an edit.

## US-06 — Export Markdown (P0)
As a developer, I want to copy or download the reviewed draft,
so that I can paste it into an issue tracker.
- The export always contains six headings in a consistent order and current edited values.
- A local .md download works without contacting the backend.
- If clipboard permission fails, the UI retains the draft and offers download.
- No issue is automatically submitted to GitHub or another service.

## US-07 — Understand generation progress (P0)
As a reporter, I want visible loading feedback,
so that I know the request is running.
- While generating, the form prevents duplicate submissions and announces the busy state.
- The server applies a 20-second provider timeout; the client uses a 25-second request timeout.
- Success or failure clears the busy state.
- A response from an obsolete request cannot replace a newer draft.

## US-08 — Recover from provider failure (P0)
As a reporter, I want understandable errors and a retry option,
so that a temporary AI failure does not discard my work.
- Timeout, provider failure, invalid provider output, and rate limiting show distinct safe messages.
- Failed requests preserve input and any existing edited draft.
- Retry is user initiated; it does not run in an automatic billing loop.
- Replacing an edited draft after a successful retry requires explicit confirmation.

## US-09 — Continue with a manual template (P0)
As a reporter, I want a manual report template when generation is unavailable,
so that I can still prepare a report.
- After a generation failure, a manual-template action is offered.
- The template copies supplied title, notes as actual-result source text, and optional environment; other facts are marked "Not provided."
- The template is labeled manual, never AI-generated.
- Replacing an edited draft requires confirmation, and the resulting sections remain editable and exportable.

## US-10 — Submit content deliberately (P0)
As a reporter, I want to understand what is sent externally,
so that I can remove sensitive content before generation.
- A notice near Generate explains that form contents are sent to the configured AI provider.
- Users are told to remove credentials, personal data, and confidential material.
- API keys are server-side only; draft contents are not intentionally written to application logs.
- No localStorage, database, or account is required; refresh loses unsaved work.
- The notice does not promise that the external provider retains no data.

## US-11 — Use the app with a keyboard (P1)
As a keyboard user, I want labeled controls and predictable focus,
so that I can complete the reporting flow without a mouse.
- Every input has a visible associated label.
- Validation errors and generation status can be announced by assistive technology.
- Focus moves to a useful result/error location after submission.
- Export and manual-template actions remain keyboard operable.

## US-12 — Start a new report safely (P1)
As a tester, I want to clear the current report deliberately,
so that I do not mix two unrelated bugs.
- New Report clears input, request state, and draft only after confirmation when work exists.
- An active request is aborted or invalidated before reset.
- A late response cannot repopulate a reset form.

## Definition of done
- P0 acceptance criteria are implemented and checked with recorded evidence.
- Unit/API tests cover validation, output-schema failures, manual fallback, and Markdown export.
- A browser smoke test covers input → generation → edit → export plus provider failure.
- A synthetic AI-output review checks fact preservation and unknown markers.
- Deployment and actual team contributions are documented in later tasks.
