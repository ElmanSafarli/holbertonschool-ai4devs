# CarpoolConnect — User Stories

This document translates the CarpoolConnect product idea into testable user stories. Priorities: **MVP** = required for the first release; **High** = next release; **Medium** = valuable enhancement; **Low** = optional future improvement.

## User Story 1 — Join a Verified Organization
As an **employee**, I want to register using my verified work email or a company invitation so that I can access a trusted coworker carpool community.

**Acceptance Criteria**
- Given an active organization invitation or an email domain approved by the organization, the employee can begin verification.
- An account becomes active only after successful verification; unverified accounts cannot search, offer, or book rides.
- An employee account is associated with the correct organization, and ride listings from other organizations are not visible.

**Priority:** MVP

## User Story 2 — Publish a Commute Offer
As an **employee driver**, I want to publish my route, departure time, available seats, and pickup point so that coworkers can request a ride.

**Acceptance Criteria**
- A driver can create an offer with origin, destination, departure date/time, pickup point, and a positive seat count.
- The system rejects missing required fields and seat counts below 1.
- Once saved, the offer is visible in searches by verified employees of the same organization.

**Priority:** MVP

## User Story 3 — Find Matching Commutes
As an **employee passenger**, I want to search rides by location and departure window so that I can find a convenient trip to work.

**Acceptance Criteria**
- A passenger can submit an origin, destination, travel date, and departure-time window.
- Search returns only upcoming rides within the same organization that have at least one available seat.
- Every result displays departure time, approximate route, available seats, and the driver’s display name; no results produces a clear empty state.

**Priority:** MVP

## User Story 4 — Request and Confirm a Seat
As an **employee passenger**, I want to request a seat and receive confirmation so that my commute is reserved.

**Acceptance Criteria**
- A verified passenger can request a seat on an available ride and sees a **Pending** status until the driver responds.
- A driver can accept or reject a pending request; the passenger sees the updated status.
- The system prevents confirmed seats from exceeding capacity and rejects duplicate active requests by the same passenger for one ride.

**Priority:** MVP

## User Story 5 — View Trip Details and Updates
As a **confirmed ride participant**, I want to view meeting instructions and receive trip updates so that I know where and when to meet.

**Acceptance Criteria**
- Confirmed passengers and the driver can view the agreed pickup point, departure time, and ride details.
- When the driver changes departure details or cancels a ride, affected confirmed passengers receive a notification.
- A nonparticipant cannot access private pickup instructions for that ride.

**Priority:** MVP

## User Story 6 — Set Recurring Commute Preferences
As an **employee driver**, I want to repeat my commute schedule on selected weekdays so that I do not have to recreate routine rides.

**Acceptance Criteria**
- A driver can select weekdays, departure time, and an end date for recurring ride offers.
- The system creates searchable ride occurrences only for the selected dates and within the specified end date.
- The driver can stop future occurrences without deleting records of past or completed trips.

**Priority:** MVP

## User Story 7 — Manage Organization Access
As an **HR or workplace administrator**, I want to control membership in my organization so that only eligible employees can use its carpool network.

**Acceptance Criteria**
- An authorized administrator can view employee membership statuses and deactivate an employee in their own organization.
- Deactivated employees cannot create new offers or requests and cannot access organization-only searches.
- Administrative actions on one organization do not modify accounts in another organization.

**Priority:** MVP

## User Story 8 — Review Aggregate Commute Activity
As a **facilities or sustainability team member**, I want a dashboard of aggregated carpool activity so that I can evaluate adoption and parking-demand trends.

**Acceptance Criteria**
- An authorized user can view total completed shared rides, participating employees, and booked seats for a selected date range.
- Dashboard counts are calculated from recorded trip events and update after new completed rides are recorded.
- The dashboard does not reveal individual home addresses, private pickup points, or personal ride histories.

**Priority:** MVP

## User Story 9 — Estimate Shared Commute Contributions
As an **employee passenger**, I want to see an estimated cost contribution before requesting a ride so that I can decide whether it fits my budget.

**Acceptance Criteria**
- A ride offer can display a driver-entered or organization-policy-based estimated contribution with a currency.
- The displayed contribution is visible before a passenger submits a seat request.
- The UI clearly labels the amount as an **estimate** and does not imply that an in-app payment was processed.

**Priority:** High

## User Story 10 — Rate a Completed Ride
As an **employee passenger**, I want to rate a completed carpool trip so that other participants and administrators can assess service quality.

**Acceptance Criteria**
- Only a confirmed participant in a completed ride can submit one rating for that ride.
- The rating must be within the permitted scale of 1 to 5.
- Ratings are stored against the trip and can be viewed only according to the platform’s configured privacy permissions.

**Priority:** High

## User Story 11 — Report Safety Concerns
As an **employee**, I want to report inappropriate behavior connected to a ride so that an authorized moderator can investigate.

**Acceptance Criteria**
- A ride participant can submit a report with a category and description tied to a specific trip.
- The reporter receives confirmation that the report was submitted and a reference ID.
- Only authorized moderators can access report details, and the reported employee cannot read the confidential report.

**Priority:** High

## User Story 12 — See Estimated Environmental Impact
As a **sustainability team member**, I want to see estimated emissions avoided by shared commutes so that I can communicate environmental progress.

**Acceptance Criteria**
- The dashboard displays an estimated emissions-saved total for a selected time period.
- The calculation uses a documented methodology and identifiable assumptions (such as distance, occupancy, and a standard emissions factor).
- Estimated values are labeled as estimates and are not presented as directly measured emissions.

**Priority:** Medium

## Coverage Notes
- **MVP stories (1–8):** Verified membership; ride creation, discovery, booking, coordination, recurring schedules, administration, and aggregate reporting.
- **High priority stories (9–11):** Contribution estimates, ratings, and reporting concerns.
- **Medium priority story (12):** Environmental impact estimates.
- **Not in initial MVP:** Payment processing, live GPS tracking, and advanced route optimization, consistent with `product_idea.md`.
