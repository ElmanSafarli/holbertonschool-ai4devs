"""Validated, dependency-free task filtering for the code review simulator."""

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Iterable


class Status(str, Enum):
    """Supported task lifecycle states."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


def _parse_date(value: str | None, field: str) -> date | None:
    """Accept only canonical YYYY-MM-DD dates, or an omitted value."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a YYYY-MM-DD string")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{field} must be a valid YYYY-MM-DD date") from exc
    if parsed.isoformat() != value:
        raise ValueError(f"{field} must use YYYY-MM-DD format")
    return parsed


def _parse_status(value: str | Status) -> Status:
    """Reject unknown statuses without silently normalizing user input."""
    try:
        return Status(value)
    except (ValueError, TypeError) as exc:
        raise ValueError("status must be todo, in_progress, or done") from exc


@dataclass(frozen=True)
class Task:
    """Immutable task; optional due dates use calendar dates without timezones."""

    id: int
    title: str
    status: Status = Status.TODO
    due_date: str | None = None

    def __post_init__(self) -> None:
        if type(self.id) is not int or self.id <= 0:
            raise ValueError("id must be a positive integer")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("title must be a non-empty string")
        object.__setattr__(self, "status", _parse_status(self.status))
        _parse_date(self.due_date, "due_date")


def filter_tasks(
    tasks: Iterable[Task],
    *,
    status: str | Status | None = None,
    due_from: str | None = None,
    due_to: str | None = None,
    query: str | None = None,
) -> list[Task]:
    """Return tasks matching every supplied filter in their original order.

    Date bounds are inclusive. Undated tasks match only when neither date
    bound is supplied. Text search is a case-insensitive literal substring
    of the title; an empty or whitespace-only query imposes no restriction.
    Filters are validated even if the iterable is empty. Input objects are
    never modified and the returned list is always a new collection.
    """
    selected_status = None if status is None else _parse_status(status)
    lower = _parse_date(due_from, "due_from")
    upper = _parse_date(due_to, "due_to")
    if lower is not None and upper is not None and lower > upper:
        raise ValueError("due_from must not be later than due_to")
    if query is not None and not isinstance(query, str):
        raise ValueError("query must be a string")
    needle = query.strip().casefold() if query is not None else ""
    has_date_filter = lower is not None or upper is not None
    matches = []

    for task in tasks:
        if not isinstance(task, Task):
            raise TypeError("tasks must contain only Task instances")
        if selected_status is not None and task.status != selected_status:
            continue
        if needle and needle not in task.title.casefold():
            continue
        due = _parse_date(task.due_date, "due_date")
        if has_date_filter:
            if due is None:
                continue
            if lower is not None and due < lower:
                continue
            if upper is not None and due > upper:
                continue
        matches.append(task)

    return matches
