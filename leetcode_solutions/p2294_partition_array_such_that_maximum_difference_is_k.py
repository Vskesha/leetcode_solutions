import unittest
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        prev = -inf
        cnt = 0

        for num in sorted(nums):
            if num - prev > k:
                cnt += 1
                prev = num

        return cnt


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["partitionArray"] * 3,
            "kwargs": [
                dict(nums=[3, 6, 1, 2, 5], k=2),
                dict(nums=[1, 2, 3], k=1),
                dict(nums=[2, 2, 4, 5], k=0),
            ],
            "expected": [2, 2, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
