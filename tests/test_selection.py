import unittest
from calc.selection import *


class StatisticTests(unittest.TestCase):
    def test_duplicates(self):
        values = [5, 2, 2, 9]
        self.assertEqual(statistika(values, 2, seed=1), 2)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            statistika([1, 2, 3], 0)



if __name__ == "__main__":
    unittest.main()
