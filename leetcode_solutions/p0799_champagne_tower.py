import unittest
from functools import cache

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def champagneTower(
        self, poured: int, query_row: int, query_glass: int
    ) -> float:
        row = [poured]

        for i in range(1, query_row + 1):
            new = [0] * (i + 1)
            for j, fl in enumerate(row):
                if fl < 1:
                    continue
                fl = (fl - 1) / 2
                new[j] += fl
                new[j + 1] += fl
            row = new

        return min(row[query_glass], 1)


class Solution2:
    def champagneTower(
        self, poured: int, query_row: int, query_glass: int
    ) -> float:

        @cache
        def get_poured_in(row, glass):
            if row == 0:
                return poured if glass == 0 else 0

            if glass < 0 or glass > row:
                return 0

            left = get_poured_in(row - 1, glass - 1)
            right = get_poured_in(row - 1, glass)

            return max(0, (left - 1) / 2) + max(0, (right - 1) / 2)

        return min(1, get_poured_in(query_row, query_glass))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["champagneTower"] * 3,
            "kwargs": [
                dict(poured=1, query_row=1, query_glass=1),
                dict(poured=2, query_row=1, query_glass=1),
                dict(poured=100000009, query_row=33, query_glass=17),
            ],
            "expected": [0.0000, 0.5000, 1.0000],
            "assert_methods": ["assertAlmostEqualFivePlaces"],
        },
    ]

    def assertAlmostEqualFivePlaces(self, first, second):
        self.assertAlmostEqual(first, second, places=5)


if __name__ == "__main__":
    unittest.main()
