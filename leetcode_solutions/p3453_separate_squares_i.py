import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        diff = 0.00001

        def squares_are_bigger_or_equal_below(coord) -> bool:
            lower, upper = 0.0, 0.0

            for _, y, l in squares:
                if y >= coord:
                    upper += l * l
                elif y + l > coord:
                    upper += l * (y + l - coord)
                    lower += l * (coord - y)
                else:
                    lower += l * l

            return lower >= upper

        left = min(sq[1] for sq in squares)
        right = max(sq[1] + sq[2] for sq in squares)

        while right - left >= diff:
            mid = (left + right) / 2
            if squares_are_bigger_or_equal_below(mid):
                right = mid
            else:
                left = mid

        return (left + right) / 2


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["separateSquares"] * 2,
            "kwargs": [
                dict(squares=[[0, 0, 1], [2, 2, 1]]),
                dict(squares=[[0, 0, 2], [1, 1, 1]]),
            ],
            "expected": [1.00000, 1.16667],
            "assert_methods": ["assertAlmostEqualFivePlaces"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
