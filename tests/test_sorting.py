import unittest
from calc.sorting import *

class SortingTests(unittest.TestCase):
    def test_all_methods(self):
        samples = [
            list(),
            list((42,)),
            list((3, 1, 2, 2, -5)),
            list((1, 2, 3, 4, 5)),
            list((5, 4, 3, 2, 1)),
            list((-100, 0, 100, 0, -100)),
        ]
        for method_name, sort_func in METHODS.items():
            for descending in (False, True):
                for original in samples:
                    with self.subTest(
                        method=method_name,
                        descending=descending,
                        original=original,
                    ):
                        values = original[:]
                        result = sort_func(values, descending=descending)
                        self.assertIsNone(result)
                        self.assertEqual(
                            values, sorted(original, reverse=descending)
                        )