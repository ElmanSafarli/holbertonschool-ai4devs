# Data Model — BugBrief

## Modeling decision
The MVP has three logical entities: ReportInput, GenerationAttempt, and ReportDraft.
They are application objects, not database tables. React retains the current input,
latest attempt, and current draft in tab memory. Express holds request data only
while processing it. There is no persistent history, database, or localStorage.
The relationships describe identity and traceability; they do not require retaining
all past objects. IDs use browser/server UUID generation and are not authentication.

## Entity 1: ReportInput
Represents the reporter-supplied facts for one report.

| Field | Type | Required | Rules |
| --- | --- | --- | --- |
| id | UUID string | Yes | Created in browser; reused while editing this report. |
| title | string | Yes | Trimmed; 1–200 UTF-16 code units. |
| notes | string | Yes | Trimmed; 1–10,000 UTF-16 code units. |
| environment | string | Yes internally | Trimmed; 0–2,000 code units; empty string represents omitted optional input. |
| createdAt | ISO 8601 UTC string | Yes | Browser timestamp for local state; not trusted for server authorization. |
| updatedAt | ISO 8601 UTC string | Yes | Updated after local edits. |

The public generation endpoint accepts only title, notes, environment, and
clientRequestId. Input IDs and local timestamps do not need to cross that boundary.
Client/server field lengths use JavaScript string.length consistently. Body size
has a separate byte limit. Text is rendered as text rather than executable HTML.

## Entity 2: GenerationAttempt
Represents a single user-triggered AI request, including a failed request.

| Field | Type | Required | Rules |
| --- | --- | --- | --- |
| clientRequestId | UUID string | Yes | Browser creates a fresh ID per attempt; server echoes validated ID. |
| inputId | UUID string | Yes locally | Links to the input whose values were snapshotted at submission. |
| state | enum | Yes | pending, succeeded, failed, or cancelled. |
| startedAt | ISO UTC string | Yes | Local start time. |
| completedAt | ISO UTC string or null | Yes | Null while pending; terminal attempts record completion. |
| errorCode | enum or null | Yes | BAD_REQUEST, PAYLOAD_TOO_LARGE, RATE_LIMITED, AI_UNAVAILABLE, AI_TIMEOUT, INVALID_AI_OUTPUT, NETWORK_ERROR, or CANCELLED. |
| inputSnapshot | title/notes/environment object | Yes locally | Captures exactly what was submitted, so subsequent input edits do not change the active request. |

A failed/cancelled attempt creates no AI draft. On retry, create a new attempt ID.
Keep only the latest attempt in active UI state. Previous IDs may remain as a
current draft's source reference without retaining their complete attempt objects.
A client timeout or abort does not prove the provider stopped processing.

## Entity 3: ReportDraft
Represents generated or manually prepared content that the user can edit/export.

| Field | Type | Required | Rules |
| --- | --- | --- | --- |
| id | UUID string | Yes | Created locally when a draft is accepted. |
| inputId | UUID string | Yes | Links to the current report input. |
| sourceAttemptId | UUID string or null | Yes | AI drafts link to the successful attempt; manual drafts use null. |
| origin | enum | Yes | ai or manual; remains unchanged after edits. |
| title | string | Yes | Non-empty; at most 200 code units. |
| steps | array of strings | Yes | 1–20 non-empty entries; at most 1,000 code units per entry. Unknown steps use one "Not provided." entry. |
| expectedResult | string | Yes | Non-empty; at most 10,000 code units. Unknown value: "Not provided.". |
| actualResult | string | Yes | Non-empty; at most 10,000 code units. Unknown value: "Not provided.". |
| environment | string | Yes | Non-empty; at most 2,000 code units. Unknown value: "Not provided.". |
| missingInformation | array of strings | Yes | 0–10 non-empty questions; at most 500 code units each. Empty array means no questions identified. |
| isEdited | boolean | Yes | Set after a user edit; controls overwrite confirmation. |
| createdAt | ISO UTC string | Yes | Local creation time. |
| updatedAt | ISO UTC string | Yes | Local last-edit time. |

The six report-content fields are title, steps, expectedResult, actualResult,
environment, and missingInformation. Origin and IDs are application metadata,
not fields invented by the model. A provider response is validated against the
content schema, capped at 64 KiB before parsing, then wrapped with metadata locally.
At export, validate edited content using the same field limits.

## Relationships and lifecycle
- One ReportInput can lead to multiple GenerationAttempts over time; only the latest attempt is retained in active state.
- A successful GenerationAttempt can supply one ReportDraft; failed attempts supply none.
- A ReportInput can have AI and manual drafts over its lifecycle, but the UI retains only one current draft.
- Manual-template creation links to ReportInput and has no source attempt.
- A successful retry replaces the current draft only after confirmation if it is edited.
- New Report clears all current objects and invalidates in-flight requests.
- Refresh/closing the tab discards local state. Exported files are the user's durable copy.

## Request/response projection
POST /api/reports/generate request:

```json
{
  "clientRequestId": "2e037b15-a059-45f2-b0c1-a0825cf25dc5",
  "title": "Order filter does not reset",
  "notes": "After resetting the filter, orders still show only pending ones in Chrome.",
  "environment": "Chrome; version not provided."
}
```

200 response (illustrative target, not recorded provider output):

```json
{
  "clientRequestId": "2e037b15-a059-45f2-b0c1-a0825cf25dc5",
  "report": {
    "title": "Order filter does not reset",
    "steps": ["Not provided."],
    "expectedResult": "Not provided.",
    "actualResult": "After resetting the filter, orders still show only pending ones.",
    "environment": "Chrome; version not provided.",
    "missingInformation": [
      "What exact steps reproduce the issue?",
      "What result did you expect after resetting the filter?",
      "Which Chrome version was used?"
    ]
  }
}
```

## Validation and retention boundaries
- Reject unexpected JSON properties, wrong types, whitespace-only required input, and invalid UUIDs.
- The client may omit environment; the server normalizes it to an empty string before provider input.
- Do not infer missing facts from field names or common browser behavior.
- Schema checks cannot establish factual correctness; user review is required.
- Application logs contain status, timing, and an internal correlation ID, not report content, raw provider output, or credentials.
- External-provider processing/retention depends on its configuration; the UI must not claim zero provider retention.
- No User, Organization, or Permission entity is required because authentication and shared storage are excluded.
