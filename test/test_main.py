import unittest
from main import *


class TestDay1(unittest.TestCase):
    def test_read_input_file(self):
        expected_lines = [
            "1000\n",
            "2000\n",
            "3000\n",
            "\n",
            "4000\n",
            "\n",
            "5000\n",
            "6000\n",
            "\n",
            "7000\n",
            "8000\n",
            "9000\n",
            "\n",
            "10000\n",
        ]
        actual_lines = read_input_file("resources/day_1_examples.txt")
        self.assertEqual(expected_lines, actual_lines)

    def test_group_elves(self):
        input_list = [
            "1\n",
            "2\n",
            "3\n",
            "\n",
            "4\n",
            "\n",
            "5\n",
            "6\n",
            "\n",
            "7\n",
            "8\n",
            "9\n",
            "\n",
            "10\n",
        ]
        grouped_elves = group_elves(input_list)
        self.assertEqual(
            [[1, 2, 3], [4], [5, 6], [7, 8, 9], [10]],
            grouped_elves,
        )

    def test_sum_elves(self):
        sum_list = sum_elves([[1, 0], [1, 1], [2, 1]])
        self.assertEqual([1, 2, 3], sum_list)

        sum_list = sum_elves([[1, 0], [1, 1], [2, 1, 1]])
        self.assertEqual([1, 2, 4], sum_list)

    def test_get_highest_value(self):
        max_value = get_highest_value([1, 2, 3])
        self.assertEqual(max_value, 3)

        max_value = get_highest_value([3, 2, 1])
        self.assertEqual(max_value, 3)

        max_value = get_highest_value([1.3, 7.6, 4])
        self.assertEqual(max_value, 7.6)

    def test_day_1_part_1(self):
        calorie_list = read_input_file("resources/day_1_examples.txt")
        elves_grouped = group_elves(calorie_list)
        elf_totals = sum_elves(elves_grouped)
        highest_value = get_highest_value(elf_totals)

        self.assertEqual(24000, highest_value)

    def test_top_3_sum(self):
        input_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(7 + 6 + 5, get_top_three_sum(input_list))

    def test_day_1_part_2(self):
        calorie_list = read_input_file("resources/day_1_examples.txt")
        elves_grouped = group_elves(calorie_list)
        elf_totals = sum_elves(elves_grouped)
        top_3_sum = get_top_three_sum(elf_totals)
        self.assertEqual(top_3_sum, 45000)

    if __name__ == "__main__":
        unittest.main()
