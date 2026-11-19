import unittest
from calc.arrays import *


class ShuffleTests(unittest.TestCase):
    def test_composition(self):
        original = [2, 2, -1, 5]
        values = original[:]
        result = shuffle(values, seed=1)
        self.assertIsNone(result)
        self.assertEqual(sorted(values), sorted(original))

    def test_edge_cases(self):
        for original in ([], [10], [4, 4, 4, 4]):
            with self.subTest(original=original):
                values = original[:]
                result = shuffle(values, seed=1)
                self.assertIsNone(result)
                self.assertEqual(values, original)

    def test_reproducibility(self):
        original = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        first = original[:]
        second = original[:]
        shuffle(first, seed=123)
        shuffle(second, seed=123)
        self.assertEqual(first, second)
        self.assertCountEqual(first, original)
