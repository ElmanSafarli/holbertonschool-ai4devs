# AI Code Review Simulator

## Task 0: Task filtering feature

Requires Python 3.10+ and only the standard library. Run from the repository root:

```python
from ai_code_review_simulator.task_filter import Task, Status, filter_tasks

tasks = [
    Task(1, "Review API", Status.TODO, "2026-11-13"),
    Task(2, "Write tests", Status.DONE, "2026-11-14"),
    Task(3, "Plan release"),
]
result = filter_tasks(tasks, status="todo", due_to="2026-11-13", query="api")
assert [task.id for task in result] == [1]
```

Filters combine with AND. Dates use strict `YYYY-MM-DD` format and inclusive
bounds. Undated tasks are excluded only when a date filter is active. Search is
a case-insensitive literal substring, with surrounding query whitespace ignored.
No sorting or input mutation occurs. Invalid model values and filters raise
`ValueError`; non-Task input elements raise `TypeError`.

## Tests

```sh
python -m unittest discover -s ai_code_review_simulator/tests -v
python -m unittest discover -s multi_language_code_generator/reference/tests -v
```

See `pr_description.md` for the change summary and review context.
