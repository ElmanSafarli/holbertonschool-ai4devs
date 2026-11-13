"""Behavioral and boundary tests for task filtering."""

from dataclasses import FrozenInstanceError
import unittest

from ai_code_review_simulator.task_filter import Status, Task, filter_tasks


class TaskFilterTests(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task(1, "Review API", due_date="2026-11-13"),
            Task(2, "Write API tests", Status.IN_PROGRESS, "2026-11-14"),
            Task(3, "Publish notes", Status.DONE, "2026-11-15"),
            Task(4, "Review Straße"),
        ]

    def ids(self, **filters):
        return [task.id for task in filter_tasks(self.tasks, **filters)]

    def test_no_filters_returns_new_list_in_input_order(self):
        result = filter_tasks(self.tasks)
        self.assertEqual(result, self.tasks)
        self.assertIsNot(result, self.tasks)
        self.assertIs(result[0], self.tasks[0])

    def test_each_status(self):
        for status, expected in [("todo", [1, 4]), ("in_progress", [2]), ("done", [3])]:
            with self.subTest(status=status):
                self.assertEqual(self.ids(status=status), expected)

    def test_inclusive_date_range(self):
        self.assertEqual(self.ids(due_from="2026-11-13", due_to="2026-11-14"), [1, 2])
        self.assertEqual(self.ids(due_from="2026-11-14", due_to="2026-11-14"), [2])

    def test_one_sided_bounds_exclude_undated_tasks(self):
        self.assertEqual(self.ids(due_from="2026-11-14"), [2, 3])
        self.assertEqual(self.ids(due_to="2026-11-14"), [1, 2])

    def test_combines_all_filters(self):
        self.assertEqual(self.ids(status="in_progress", due_to="2026-11-14", query="API"), [2])

    def test_unicode_case_insensitive_literal_search(self):
        self.assertEqual(self.ids(query=" STRASSE "), [4])
        self.assertEqual(self.ids(query=".*"), [])

    def test_empty_search_has_no_effect(self):
        self.assertEqual(self.ids(query="  "), [1, 2, 3, 4])

    def test_generator_input(self):
        self.assertEqual(filter_tasks(iter(self.tasks), status=Status.DONE), [self.tasks[2]])

    def test_empty_and_no_matching_tasks(self):
        self.assertEqual(filter_tasks([]), [])
        self.assertEqual(self.ids(query="missing"), [])

    def test_invalid_filters_rejected_even_with_empty_input(self):
        cases = [
            {"status": "unknown"}, {"status": []}, {"query": 42},
            {"due_from": "2026-02-30"}, {"due_to": "20261113"},
            {"due_to": 42}, {"due_from": "2026-11-15", "due_to": "2026-11-13"},
        ]
        for filters in cases:
            with self.subTest(filters=filters), self.assertRaises(ValueError):
                filter_tasks([], **filters)

    def test_invalid_tasks_rejected(self):
        for fields in [{"id": True}, {"id": 0}, {"title": " "},
                       {"status": "unknown"}, {"due_date": "2026-02-29"}]:
            values = {"id": 1, "title": "Valid", **fields}
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                Task(**values)
        with self.assertRaises(TypeError):
            filter_tasks([{"id": 1}], status="done")

    def test_leap_date_and_immutable_tasks(self):
        task = Task(1, "Leap day", due_date="2028-02-29")
        self.assertEqual(filter_tasks([task], due_to="2028-02-29"), [task])
        with self.assertRaises(FrozenInstanceError):
            task.title = "Changed"


if __name__ == "__main__":
    unittest.main()
