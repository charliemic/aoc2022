from file_utils import read_input_file
import unittest
from game import *
from parameterized import parameterized


class TestDayPart2(unittest.TestCase):
    def test_sum_scores_with_choice(self):
        guess_list = strip_newlines(read_input_file("resources/day_2_examples.txt"))
        total = sum_with_choice(guess_list)
        self.assertEqual(12, total)

    @parameterized.expand(
        [
            ("rock_draw", ["A Y"], 4),
            ("rock_lose", ["A X"], 3),
            ("rock_win", ["A Z"], 8),
            ("paper_draw", ["B Y"], 5),
            ("paper_lose", ["B X"], 1),
            ("paper_win", ["B Z"], 9),
            ("scissors_win", ["C Z"], 7),
            ("scissors_lose", ["C X"], 2),
            ("scissors_draw", ["C Y"], 6),
        ]
    )
    def test_strategy(self, name, inp, exp):
        self.assertEqual(exp, sum_with_choice(inp))
