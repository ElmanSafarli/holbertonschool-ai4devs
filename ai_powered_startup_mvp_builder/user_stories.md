# User Stories - Feedback Hub

These requirements implement [the MVP concept](mvp_concept.md). Submitter and reviewer describe activities, not authenticated roles. All data stays in the same browser and origin.

## US-01 - Submit feedback
As a tester, I want to submit a title, description, and category so that I can record a suggestion or problem.
- A valid submission receives a unique ID, UTC creation timestamp, and New status.
- The entry appears only after successful persistence; the form then clears and confirms success.
- Repeated clicks during saving do not create duplicates.

## US-02 - Validate input
As a tester, I want specific validation messages so that I can correct my submission.
- Trim leading and trailing whitespace before checking lengths.
- Require title length 1-100 and description length 1-2000 characters.
- Accept only Bug, Feature Request, or General.
- Invalid input creates no entry and remains available for correction.

## US-03 - Browse feedback
As a reviewer, I want to see feedback newest first so that I can find recent submissions.
- Show title, full description, category, status, and creation time.
- Sort by creation time descending; break ties by ID ascending.
- Show an informative empty state when no feedback exists.

## US-04 - Search feedback
As a reviewer, I want to search titles and descriptions so that I can find related observations.
- Match a trimmed query case-insensitively as a substring in either field.
- An empty query matches every entry.
- Searching does not modify stored feedback.

## US-05 - Filter feedback
As a reviewer, I want category and status filters so that I can focus my review.
- Each filter offers All and the supported values.
- Search and both filters combine using AND.
- Show a no-results message and a way to clear filters when nothing matches.

## US-06 - Update review status
As a reviewer, I want to change status so that I can track review progress.
- Allow New, Under Review, or Resolved, including reopening a resolved entry.
- Preserve ID, title, description, category, and creation time.
- Persist before confirming the change; on failure keep the previous status.

## US-07 - Restore saved feedback
As a returning user, I want saved entries to survive refresh so that my work is retained.
- Load and validate the versioned localStorage document on startup.
- Restore entries and statuses in the same browser and origin.
- If stored data is malformed or unsupported, show an error and block writes rather than silently overwriting it.

## US-08 - Handle storage failures and capacity
As a user, I want clear limits and failure messages so that I know whether my work was saved.
- Permit at most 100 entries; reject the 101st without losing existing entries.
- Handle unavailable storage and quota errors with a visible message.
- Keep unsaved form content and never display a false success confirmation.

## US-09 - Export filtered feedback
As a researcher, I want a CSV download of the visible results so that I can inspect them in a spreadsheet.
- Include ID, title, description, category, status, and creation timestamp.
- Export the same filtered results and order as the dashboard.
- Escape commas, double quotes, and line breaks; neutralize formula prefixes in user text.
- With no results, export a header-only CSV; exporting never changes saved data.

## US-10 - Use the app on different devices
As a user, I want a responsive, keyboard-accessible interface so that I can submit and review feedback comfortably.
- At 320px mobile and 1280px desktop widths, controls remain usable without horizontal page overflow.
- All fields have labels; interactive controls have visible keyboard focus.
- Associate errors with fields and announce save success or failure through an accessible status region.
- Clearly state that this demo stores data locally and does not share it with a team.
