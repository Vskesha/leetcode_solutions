import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        left, right = 0, (start[-1] - start[0] + d) // (len(start) - 1)

        while left < right:
            mid = (left + right + 1) // 2
            nn = start[0]
            for n in start:
                if nn > n + d:
                    break
                if nn < n:
                    nn = n
                nn += mid
            else:
                left = mid
                continue
            right = mid - 1

        return left


class Solution2:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        def fit(diff: int) -> bool:
            nn = start[0]
            for n in start:
                if nn > n + d:
                    return False
                if nn < n:
                    nn = n
                nn += diff
            return True

        start.sort()
        left, right = 0, (start[-1] - start[0] + d) // (len(start) - 1)

        while left < right:
            mid = (left + right + 1) // 2
            if fit(mid):
                left = mid
            else:
                right = mid - 1

        return left


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxPossibleScore"] * 3,
            "kwargs": [
                dict(start=[6, 0, 3], d=2),
                dict(start=[2, 6, 13, 13], d=5),
                dict(start=[100, 1000000000, 0], d=1009),
            ],
            "expected": [4, 5, 1109],
        },
    ]


if __name__ == "__main__":
    unittest.main()
