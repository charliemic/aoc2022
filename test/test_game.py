from file_utils import read_input_file
import unittest
from game import *

rock_them, rock_me = "A", "X"
paper_them, paper_me = "B", "Y"
scissors_them, scissors_me = "C", "Z"


class TestDayPart1(unittest.TestCase):
    def test_sum_scores(self):
        guess_list = strip_newlines(read_input_file("resources/day_2_examples.txt"))
        total = sum_scores(guess_list)
        self.assertEqual(15, total)

    def test_rock_draw(self):
        self.assertEqual(score(rock_them, rock_me), 4)

    def test_paper_draw(self):
        self.assertEqual(score(paper_them, paper_me), 5)

    def test_scissors_draw(self):
        self.assertEqual(score(scissors_them, scissors_me), 6)

    def test_rock_vs_paper(self):
        self.assertEqual(score(rock_them, paper_me), 8)

    def test_rock_vs_scissors(self):
        self.assertEqual(score(rock_them, scissors_me), 3)

    def test_paper_vs_rock(self):
        self.assertEqual(score(paper_them, rock_me), 1)

    def test_paper_vs_scissors(self):
        self.assertEqual(score(paper_them, scissors_me), 9)

    def test_scissors_vs_rock(self):
        self.assertEqual(score(scissors_them, rock_me), 7)

    def test_scissors_vs_paper(self):
        self.assertEqual(score(scissors_them, paper_me), 2)


if __name__ == "__main__":
    main()
