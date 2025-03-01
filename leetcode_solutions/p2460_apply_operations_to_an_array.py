import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        ans = [n for n in nums if n]
        ans.extend([0] * (len(nums) - len(ans)))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["applyOperations"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 2, 1, 1, 0]),
                dict(nums=[0, 1]),
            ],
            "expected": [
                [1, 4, 2, 0, 0, 0],
                [1, 0],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
