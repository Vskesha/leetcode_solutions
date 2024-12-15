import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findScore(self, nums: List[int]) -> int:
        ln = len(nums)
        numi = sorted((n, i) for i, n in enumerate(nums, 1))
        marked = [False] * (ln + 2)
        score = 0
        for n, i in numi:
            if not marked[i]:
                score += n
                marked[i - 1] = True
                marked[i] = True
                marked[i + 1] = True
        return score


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findScore"] * 2,
            "kwargs": [
                dict(nums=[2, 1, 3, 4, 5, 2]),
                dict(nums=[2, 3, 5, 1, 3, 2]),
            ],
            "expected": [7, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()
