from file_utils import read_input_file
import unittest
from stacks import *


class TestStacks(unittest.TestCase):
    def test_example(self):
        read_input = read_input_file("resources/day_5_examples.txt")
        model, commands = parse_input(read_input)
        message = execute_commands(model, commands)

        self.assertEqual("MCD", message)
