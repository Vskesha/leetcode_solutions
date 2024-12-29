import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, pv = 0, 1
        for val in values:
            pv -= 1
            ans = max(ans, pv + val)
            if val > pv:
                pv = val
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxScoreSightseeingPair"] * 2,
            "kwargs": [
                dict(values=[8, 1, 5, 2, 6]),
                dict(values=[1, 2]),
            ],
            "expected": [11, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
