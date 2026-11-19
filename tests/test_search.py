import unittest
from calc.arrays import *


class SearchTests(unittest.TestCase):
    def test_found_and_missing(self):
        data = [-10, 0, 2, 2, 15, 42]
        self.assertEqual(binary_search(data, -10), 0)
        idx = binary_search(data, 2)
        self.assertIsNotNone(idx)
        self.assertEqual(data[idx], 2)
        self.assertIsNone(binary_search(data, 99))
        self.assertIsNone(binary_search([], 5))


if __name__ == "__main__":
    unittest.main()
