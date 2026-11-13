"""Regression tests for the Python bug fixes; run from repository root."""
import unittest
from smart_bug_bounty.bug_fixes.bug1_fixed import last_items
from smart_bug_bounty.bug_fixes.bug4_fixed import add_tag


class LastItemsTests(unittest.TestCase):
    def test_original_failure(self):
        self.assertEqual(last_items([10, 20, 30, 40, 50], 3), [30, 40, 50])

    def test_count_boundaries(self):
        for count, expected in [(0, []), (1, [3]), (3, [1, 2, 3]), (4, [1, 2, 3]), (99, [1, 2, 3])]:
            with self.subTest(count=count):
                self.assertEqual(last_items([1, 2, 3], count), expected)

    def test_empty_input(self):
        self.assertEqual(last_items([], 0), [])
        self.assertEqual(last_items([], 10), [])

    def test_invalid_counts(self):
        for count in [-1, 1.5, '2', None, True, False]:
            with self.subTest(count=count), self.assertRaises(ValueError):
                last_items([1, 2, 3], count)

    def test_no_input_mutation_and_new_list(self):
        original = [1, 2, 3]
        result = last_items(original, 99)
        self.assertIsNot(result, original)
        result.append(4)
        self.assertEqual(original, [1, 2, 3])


class TagTests(unittest.TestCase):
    def test_independent_default_calls(self):
        first = add_tag('security')
        second = add_tag('performance')
        self.assertEqual(first, ['security'])
        self.assertEqual(second, ['performance'])
        self.assertIsNot(first, second)

    def test_explicit_empty_list_identity(self):
        supplied = []
        self.assertIs(add_tag('security', supplied), supplied)
        self.assertEqual(supplied, ['security'])

    def test_existing_list_appends(self):
        supplied = ['existing']
        self.assertIs(add_tag('new', supplied), supplied)
        self.assertEqual(supplied, ['existing', 'new'])

    def test_separate_supplied_lists(self):
        first, second = [], []
        add_tag('a', first)
        add_tag('b', second)
        self.assertEqual(first, ['a'])
        self.assertEqual(second, ['b'])

    def test_invalid_tags_do_not_mutate(self):
        for tag in ['', '  ', None, 42]:
            supplied = ['existing']
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                add_tag(tag, supplied)
            self.assertEqual(supplied, ['existing'])


if __name__ == '__main__':
    unittest.main()
