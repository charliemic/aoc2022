from file_utils import read_input_file
import unittest
from game import *
from parameterized import parameterized


class TestDayPart1(unittest.TestCase):
    def test_sum_scores(self):
        guess_list = strip_newlines(read_input_file("resources/day_2_examples.txt"))
        total = sum_scores(guess_list)
        self.assertEqual(15, total)

    @parameterized.expand(
        [
            ("rock_draw", "A", "X", 4),
            ("paper_draw", "B", "Y", 5),
            ("scissors_draw", "C", "Z", 6),
            ("rock_paper", "A", "Y", 8),
            ("rock_scissors", "A", "Z", 3),
            ("paper_rock", "B", "X", 1),
            ("paper_scissors", "B", "Z", 9),
            ("scissors_rock", "C", "X", 7),
            ("scissors_paper", "C", "Y", 2),
        ]
    )
    def test_score(self, name, them, me, exp):
        self.assertEqual(exp, score(them, me))


if __name__ == "__main__":
    main()
