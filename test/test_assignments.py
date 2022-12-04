from file_utils import read_input_file
import unittest
from assignments import *


class TestAssignments(unittest.TestCase):
    def test_parse_input(self):
        data = ["2-4,6-8\n", "2-3,4-5\n"]
        output = parse_input(data)
        self.assertEqual(
            ["2-4", "6-8", "2-3", "4-5"],
            output,
        )

    def test_example(self):
        read_input = read_input_file("resources/day_4_examples.txt")
        assignments = parse_input(read_input)
        total = contained_ranges(assignments)
        self.assertEqual(2, total)

    def test_non_examples(self):
        data = ["2-10,6-8\n", "2-3,4-5\n"]
        assignments = parse_input(data)
        total = contained_ranges(assignments)
        self.assertEqual(1, total)

    def test_first_contained_in_second(self):
        data = ["6-6,6-8\n", "2-3,4-5\n"]
        assignments = parse_input(data)
        total = contained_ranges(assignments)
        self.assertEqual(1, total)

    def test_large_example(self):
        data = ["0-1000,6-8\n", "2-3,4-5\n"]
        assignments = parse_input(data)
        total = contained_ranges(assignments)
        self.assertEqual(1, total)

    def test_compare(self):
        self.assertTrue(3 <= 1000)
        self.assertTrue(2 >= 0)

        self.assertTrue(3 <= 1000 and 2 >= 0)

    def test_non_overlapping(self):
        data = ["1-2", "3-4"]
        total = overlapping_ranges(data)
        self.assertEqual(0, total)

    def test_overlapping(self):
        data = ["1-2", "2-2"]
        total = overlapping_ranges(data)
        self.assertEqual(1, total)

    def test_example_part_2(self):
        read_input = read_input_file("resources/day_4_examples.txt")
        assignments = parse_input(read_input)
        total = overlapping_ranges(assignments)
        self.assertEqual(4, total)
