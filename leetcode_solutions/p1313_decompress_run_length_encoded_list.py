import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return sum(
            ([nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)), start=[]
        )


class Solution2:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans.extend([nums[i + 1]] * nums[i])
        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["decompressRLElist"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 3, 4]),
                dict(nums=[1, 1, 2, 3]),
            ],
            "expected": [[2, 4, 4, 4], [1, 3, 3]],
        },
    ]


if __name__ == "__main__":
    unittest.main()
