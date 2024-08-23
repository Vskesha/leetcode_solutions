import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        st = 0
        for i in range(1, k - 1):
            if nums[i] != nums[i - 1] + 1:
                st = i
        ans = []
        for i in range(k - 1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                st = i
            if st < i - k + 2:
                ans.append(nums[i])
            else:
                ans.append(-1)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["resultsArray"] * 3,
            "kwargs": [
                dict(nums=[1, 2, 3, 4, 3, 2, 5], k=3),
                dict(nums=[2, 2, 2, 2, 2], k=4),
                dict(nums=[3, 2, 3, 2, 3, 2], k=2),
            ],
            "expected": [
                [3, 4, -1, -1, -1],
                [-1, -1],
                [-1, 3, -1, 3, -1],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
