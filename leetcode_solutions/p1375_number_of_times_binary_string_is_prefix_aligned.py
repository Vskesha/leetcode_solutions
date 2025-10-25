import unittest
from heapq import heappush
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        return sum(
            1 for i, m in enumerate(accumulate(flips, func=max), 1) if i == m
        )


class Solution1:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, m = 0, 0

        for i, fl in enumerate(flips, 1):
            m = max(m, fl)
            ans += m == i

        return ans


class Solution2:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, h = 0, []

        for i, fl in enumerate(flips, 1):
            heappush(h, -fl)
            ans += h[0] == -i

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numTimesAllBlue"] * 2,
            "kwargs": [
                dict(flips=[3, 2, 4, 1, 5]),
                dict(flips=[4, 1, 2, 3]),
            ],
            "expected": [2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
