import unittest
from main import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1.1, 1), 2.1)

    if __name__ == "__main__":
        unittest.main()
