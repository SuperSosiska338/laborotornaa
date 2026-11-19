import unittest
from calc.selection import *


class StatisticTests(unittest.TestCase):
    def test_duplicates(self):
        values = [5, 2, 2, 9]
        self.assertEqual(statistika(values, 2, seed=1), 2)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            statistika([1, 2, 3], 0)

    def test_sample_array(self):
        base = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        self.assertEqual(statistika(base[:], 1, seed=1), 11)
        self.assertEqual(statistika(base[:], 4, seed=1), 35)
        self.assertEqual(statistika(base[:], 9, seed=1), 87)

    def test_all_ranks(self):
        original = [5, -1, 2, 2]
        expected = sorted(original)
        for k in range(1, len(original) + 1):
            with self.subTest(k=k):
                data = original[:]
                result = statistika(data, k, seed=1)
                self.assertEqual(result, expected[k - 1])
                self.assertEqual(sorted(data), expected)

    def test_elements(self):
        self.assertEqual(statistika([42], 1, seed=1), 42)
        self.assertEqual(statistika([7, 7, 7, 7], 3, seed=5), 7)

    def test_empty_etc(self):
        invalid_cases = [
            ([], 1),
            ([1, 2, 3], 0),
            ([1, 2, 3], -2),
            ([1, 2, 3], 4),
            ([1, 2, 3], 1.5),
            ([1, 2, 3], True),
        ]
        for arr, k in invalid_cases:
            with self.subTest(arr=arr, k=k):
                with self.assertRaises(ValueError):
                    statistika(arr[:], k)



if __name__ == "__main__":
    unittest.main()
