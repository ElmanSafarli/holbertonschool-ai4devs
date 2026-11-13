# High-Level Architecture Plan — BugBrief

## Scope and status
This is the planned architecture for the MVP described in team_ideation.md and
user_stories.md. It has not yet been implemented or deployed. The design uses
React/Vite, a Node.js/Express API, and a server-side AI-provider adapter. The exact
provider/model and hosting platform will be selected during implementation.
The three application entities are specified in data_model.md.

## Components

| Component | Responsibility | Boundary |
| --- | --- | --- |
| React form and state | Collect input, validate fields, track current request and draft, handle reset/retry. | Browser; temporary tab memory only. |
| Report editor and exporter | Edit all six report sections; validate and serialize Markdown; copy/download locally. | Browser; no export network call. |
| Express API | Validate requests, enforce limits, call adapter, validate output, return safe errors. | Trusted server configuration; submitted text is untrusted. |
| Provider adapter | Build grounding prompt, call one configured AI service, enforce timeout and response bounds. | API credentials remain server-side. |
| External AI service | Return proposed structured report content. | External trust/retention boundary; output remains untrusted. |

Deploy the Vite build and /api routes under one origin when feasible. This keeps
the browser flow simple. If separate hosting is required, allow only the configured
frontend origin through CORS; CORS is not an authentication or cost-control system.
No database, background worker, or queue is needed for the MVP.

## End-to-end flow
1. The user enters a title/notes and optional environment and sees the provider-submission notice.
2. The browser validates input, snapshots it, creates clientRequestId, enters pending state, and sends POST /api/reports/generate.
3. Express applies JSON-body and rate limits, validates the request, and normalizes optional environment.
4. The adapter sends trusted instructions separately from submitted text; the model has no tools or code execution.
5. The server bounds and validates the returned report structure. Invalid output becomes a safe error, never an editable success result.
6. The browser accepts a response only for the active request ID, creates an AI-origin draft, and opens the editor. If edited work exists, it requests confirmation before replacement.
7. The user reviews facts, edits fields, and exports Markdown locally.
8. On failure, the input and current draft remain intact. The user can retry or create a labeled manual template.

## API contract

| Route | Input | Successful response |
| --- | --- | --- |
| POST /api/reports/generate | title, notes, optional environment, clientRequestId | 200 with echoed clientRequestId and the six-field report object. |
| GET /api/health | None | 200 with a basic process-health status; no provider call or secret output. |

POST is the single product endpoint; health is an operational check. Schemas,
field bounds, unknown markers, and examples are defined in data_model.md. Reuse
validation definitions across client/server where practical. Server validation
remains authoritative.

| Failure | HTTP status | Code |
| --- | ---: | --- |
| Invalid JSON, fields, types, or request ID | 400 | BAD_REQUEST |
| JSON body exceeds 64 KiB | 413 | PAYLOAD_TOO_LARGE |
| Request allowance exhausted | 429 | RATE_LIMITED |
| AI provider failure/configuration unavailable | 503 | AI_UNAVAILABLE |
| Provider exceeds 20 seconds | 504 | AI_TIMEOUT |
| Provider content fails parsing/schema/size checks | 502 | INVALID_AI_OUTPUT |

Errors return {error: {code, message}} and include clientRequestId only when it
was successfully validated. Do not return stack traces, provider credentials,
or raw provider error bodies. The client maps network failures to NETWORK_ERROR
and its own abort/timeout to CANCELLED or AI_TIMEOUT as appropriate. No automatic
retry is performed.

## AI integration and factual limits
- Trusted instructions require organization of supplied facts only, no invented reproduction details, environment versions, error strings, or root causes.
- Require exactly six content fields with limits from data_model.md; use provider schema constraints where supported and always validate again server-side.
- Use "Not provided." for absent factual sections and ask specific questions in missingInformation.
- Treat notes containing instructions as report content; they do not override the system prompt.
- Disable tools and external retrieval for this workflow.
- Bound provider output with an output-token limit and reject response bodies above 64 KiB before JSON parsing.
- Structural validation cannot detect every hallucination. Show a draft label and require human factual review.
- Test AI behavior using a small synthetic set: sparse observations, complete notes, conflicting details, and embedded instruction-like text. Record observations honestly rather than claiming deterministic semantic correctness.

## Reliability and state
- Provider timeout: 20 seconds with request cancellation when supported.
- Browser timeout: 25 seconds, leaving time for server error delivery.
- A pending request disables duplicate Generate submissions; retry creates a new request ID.
- Reset invalidates the current request and aborts its client fetch; stale responses are ignored.
- Keep one current draft; never overwrite edited content silently.
- A failed retry preserves the prior draft.
- Manual fallback is implemented in the browser from existing input; it never claims an AI call succeeded.
- Clipboard errors offer file download; export uses the latest validated edited content.

## Security and operational controls
- Store provider credentials in server environment configuration; never prefix them as frontend-exposed variables.
- Use HTTPS in deployment; serve user text as plain text and do not inject raw HTML.
- Avoid storing or logging input/drafts; log safe status/timing metadata.
- Apply a small demo allowance, initially 5 generation requests per minute per client IP, plus a provider-budget/concurrency limit; tune during smoke testing.
- In-memory rate limits cover a single-instance demo only. Configure trusted proxy handling explicitly; do not blindly trust forwarded-IP headers.
- Anonymous public generation can incur cost despite IP limits. Use provider spending limits and keep access controlled until the demo configuration has been checked.
- On multi-instance hosting, a shared limiter would be a later requirement; the MVP assumes one API instance.
- Input notices explain external submission and ask users to remove secrets; no provider-retention guarantees are invented.

## Proposed source layout
| Path | Contents |
| --- | --- |
| frontend/src/ | Form, editor, state handling, fallback, and Markdown export. |
| server/src/ | Express routes, AI adapter, request guards, and safe errors. |
| shared/ | Request/report schemas, shared limits, and serializers where appropriate. |
| tests/ | Unit/API checks, synthetic AI fixtures, and browser-flow smoke tests. |

These are proposed directories for the implementation task, not existing files.

## Verification plan
- Unit: field validation/normalization, manual template mapping, Markdown serialization and export limits.
- API with a mocked adapter: success, invalid input, oversized body, rate limit, timeout, provider failure, invalid/oversized output.
- UI: duplicate-submit prevention, editable fields, failed-retry preservation, replacement confirmation, stale-response suppression, reset, clipboard failure.
- Integration: a real provider call using synthetic notes; inspect fact preservation and unknown markers.
- Browser smoke test: input → generate → edit → download; repeat with provider failure and manual fallback.
- Deployment: confirm HTTPS, health route, server-only credentials, request limits, and useful errors from a clean session.
- Record actual commands/results during implementation; none are claimed as passed here.

## Delivery order and tradeoffs
First agree on shared schemas; then build a mocked end-to-end path, integrate the
provider, exercise errors, and deploy. In-memory state keeps the sprint small but
loses work on refresh. Anonymous access avoids account development but requires
cost controls. Provider-generated text improves drafting speed but needs human
review. Accounts, persistent history, issue posting, uploads, and team workspaces
remain outside the MVP.
