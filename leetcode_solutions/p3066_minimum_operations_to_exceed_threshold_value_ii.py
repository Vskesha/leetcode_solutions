import unittest
from heapq import heapify, heappush, heappop
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        heapify(nums)
        while nums[0] < k:
            heappush(nums, heappop(nums) * 2 + heappop(nums))

        return ln - len(nums)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 2,
            "kwargs": [
                dict(nums=[2, 11, 10, 1, 3], k=10),
                dict(nums=[1, 1, 2, 4, 9], k=20),
            ],
            "expected": [2, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
