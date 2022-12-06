import unittest
from parameterized import parameterized_class
from communication import *
from file_utils import read_input_file


@parameterized_class(
    ("signal", "exp_start"),
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
class TestSignalStart(unittest.TestCase):
    def test_find_signal_start(self):
        start = find_signal_start(self.signal)
        self.assertEqual(self.exp_start, start)


@parameterized_class(
    ("signal", "exp_msg"),
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
class TestSignalMessage(unittest.TestCase):
    def test_find_signal_message(self):
        start = find_message(self.signal)
        self.assertEqual(self.exp_msg, start)


class TestExampleFromFile(unittest.TestCase):
    def test_example_from_file(self):
        signal = read_input_file("resources/day_6_example.txt")[0]
        start = find_signal_start(signal)
        self.assertEqual(7, start)


if __name__ == "__main__":
    main()
