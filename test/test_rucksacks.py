from file_utils import read_input_file
import unittest
from rucksacks import *


class TestDay3(unittest.TestCase):
    def test_halve(self):
        test_string = "vJrwpWtwJgWrhcsFMMfFFhFp"
        first, second = halve(test_string)
        self.assertEqual("vJrwpWtwJgWr", first)
        self.assertEqual("hcsFMMfFFhFp", second)

        test_string = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        first, second = halve(test_string)
        self.assertEqual("jqHRNqRjqzjGDLGL", first)
        self.assertEqual("rsFMfFZSrLrFZsSL", second)

    def common_letters(self):
        test_string = "vJrwpWtwJgWrhcsFMMfFFhFp"
        first, second = halve(test_string)
        self.assertEqual(["p"], common_letters(first, second))

        test_string = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
        first, second = halve(test_string)
        self.assertEqual(["L"], common_letters(first, second))

    def find_common_item_in_rucksacks(self):
        common = find_common_item_in_rucksacks(
            ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"]
        )
        self.assertEqual([["p"], ["L"]], common)

    def score(self):
        self.assertEqual(1, "a")
        self.assertEqual(2, "b")
        self.assertEqual(27, "A")

    def sum_items(self):
        common = find_common_item_in_rucksacks(
            ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"]
        )
        self.assertEqual(54, sum_items(common))

    def test_example(self):
        rucksacks = read_input_file("resources/day_3_examples.txt")
        common = find_common_item_in_rucksacks(rucksacks)
        total = sum_items(common)
        self.assertEqual(157, total)

    def test_example_part_2(self):
        rucksacks = read_input_file("resources/day_3_examples.txt")
        common = calculate_common_in_3_group(rucksacks)
        total = sum_items(common)
        self.assertEqual(70, total)

    def test_calculate_common_in_3_group(self):
        group = ["ab", "ac", "ad"]
        self.assertEqual([["a"]], calculate_common_in_3_group(group))

        group = ["ab", "ac", "ad", "ba", "bb", "bc"]
        self.assertEqual([["a"], ["b"]], calculate_common_in_3_group(group))
