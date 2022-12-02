from file_utils import read_input_file
import unittest
from game import *

GAME_CONFIG = {
    "rock": {"opponent": "A", "strategy": "X", "score": 1},
    "paper": {"opponent": "B", "strategy": "Y", "score": 2},
    "scissors": {"opponent": "C", "strategy": "Z", "score": 3},
}

rock = "A"
paper = "B"
scissors = "C"
lose = "X"
draw = "Y"
win = "Z"


class TestDayPart2(unittest.TestCase):
    def test_sum_scores_with_choice(self):
        guess_list = strip_newlines(read_input_file("resources/day_2_examples.txt"))
        total = sum_with_choice(guess_list)
        self.assertEqual(12, total)

    def test_rock_draw(self):
        self.assertEqual(sum_with_choice(["A Y"]), 4)

    # I choose scissors
    def test_rock_lose(self):
        self.assertEqual(sum_with_choice(["A X"]), 3)

    # I choose paper
    def test_rock_win(self):
        self.assertEqual(sum_with_choice(["A Z"]), 8)

    def test_paper_draw(self):
        self.assertEqual(sum_with_choice(["B Y"]), 5)

    # I choose rock
    def test_paper_lose(self):
        self.assertEqual(sum_with_choice(["B X"]), 1)

    # I choose scissors
    def test_paper_win(self):
        self.assertEqual(sum_with_choice(["B Z"]), 9)

    # I choose rock
    def test_scissors_win(self):
        self.assertEqual(sum_with_choice(["C Z"]), 7)

    # I choose paper
    def test_scissors_lose(self):
        self.assertEqual(sum_with_choice(["C X"]), 2)

    def test_scissors_draw(self):
        self.assertEqual(sum_with_choice(["C Y"]), 6)
