import unittest
from communication import *
from file_utils import read_input_file


class TestCommunications(unittest.TestCase):
    def test_find_signal_start(self):
        signal = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        start = find_signal_start(signal)
        self.assertEqual(7, start)

        signal = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        start = find_signal_start(signal)
        self.assertEqual(5, start)

        signal = "nppdvjthqldpwncqszvftbrmjlhg"
        start = find_signal_start(signal)
        self.assertEqual(6, start)

        signal = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        start = find_signal_start(signal)
        self.assertEqual(10, start)

        signal = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        start = find_signal_start(signal)
        self.assertEqual(11, start)

    def test_example_from_file(self):
        signal = read_input_file("resources/day_6_example.txt")[0]
        start = find_signal_start(signal)
        self.assertEqual(7, start)

    def test_find_signal_message(self):
        signal = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        start = find_message(signal)
        self.assertEqual(19, start)

        signal = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        start = find_message(signal)
        self.assertEqual(23, start)

        signal = "nppdvjthqldpwncqszvftbrmjlhg"
        start = find_message(signal)
        self.assertEqual(23, start)

        signal = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        start = find_message(signal)
        self.assertEqual(29, start)

        signal = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        start = find_message(signal)
        self.assertEqual(26, start)
