from file_utils import read_input_file
import unittest
from rucksacks import *


class TestDay3(unittest.TestCase):
    def halve(self):
        pass

    def common_letters(self):
        pass

    def find_common_item_in_rucksacks(self):
        pass

    def score(self):
        pass

    def sum_items(self):
        pass

    def test_example(self):
        rucksacks = read_input_file("resources/day_3_examples.txt")
        common = find_common_item_in_rucksacks(rucksacks)
        total = sum_items(common)
        self.assertEqual(157, total)
