# MVP Concept - Feedback Hub

## Problem Statement
Small startup teams receive product feedback through scattered chats and emails. They struggle to keep suggestions together, identify recurring problems, and track what has been reviewed. Feedback Hub is a small web application that collects structured feedback in one place and lets a product owner search, review, and export it.

## Target Users
- Early product testers who want to report a problem or suggest an improvement.
- Startup founders and product managers who need to review feedback.
- UX researchers who want a simple, searchable collection of observations.

## Core Features
1. **Submit feedback:** A form accepts a required title (1-100 characters), description (1-2000 characters), and category (Bug, Feature Request, or General). Whitespace-only fields are rejected. A successful submission receives an ID, creation timestamp, and New status.
2. **Browse and search:** A dashboard lists feedback newest first, searches titles and descriptions case-insensitively, and filters by category and status. It shows a clear empty state when no entries match.
3. **Track review status:** The product owner can mark an entry New, Under Review, or Resolved. Changing status preserves the original text and creation timestamp.
4. **Persist feedback:** Save entries and status changes in browser localStorage so they remain available after a page refresh in the same browser and origin. Show an error if saving fails rather than reporting success.
5. **Export CSV:** Export the currently filtered entries with ID, title, description, category, status, and creation timestamp. Escape commas, quotes, and line breaks correctly and neutralize spreadsheet formula prefixes in user-entered cells.

## Constraints
- **Prototype scope:** One responsive web application built with HTML, CSS, and JavaScript, with AI assistance. No paid APIs or services are required.
- **No authentication or backend:** This is a single-browser demonstration. Submitter and reviewer are usage roles, not enforced permissions. Anyone using the same browser profile can review entries.
- **Local storage only:** Data is not shared between users, browsers, or devices. Clearing browser storage removes the data. Real shared collection and access control require a future backend.
- **Capacity:** Store at most 100 feedback entries. At the limit, reject new submissions with a clear message while keeping existing entries intact.
- **Privacy:** Use fictional or non-sensitive demo feedback. Do not collect passwords, contact details, or confidential customer information.
- **Accessibility and responsiveness:** Support keyboard navigation, labelled fields, visible focus, readable contrast, and layouts without horizontal overflow on mobile and desktop.
- **Out of scope:** AI categorization, chat, notifications, attachments, user accounts, and external integrations.

## MVP Success Criteria
- A valid submission appears on the dashboard and remains after refresh.
- Invalid input produces useful validation messages and creates no entry.
- Search, filters, and status changes produce the expected results.
- CSV export reflects the current filters and preserves text safely.
- The 101st entry is rejected without losing the first 100 entries.
