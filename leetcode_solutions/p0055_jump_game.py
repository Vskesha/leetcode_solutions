import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0

        for i, n in enumerate(nums):
            if i > can_reach:
                return False
            can_reach = max(can_reach, i + n)

        return True


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln == 1:
            return True
        if nums[0] == 0:
            return False

        zi = 0
        for i in range(ln - 2, -1, -1):
            if not (zi or nums[i]):
                zi = i
            elif zi and i + nums[i] > zi:
                zi = 0
        return not zi


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canJump"] * 2,
            "kwargs": [
                dict(nums=[2, 3, 1, 1, 4]),
                dict(nums=[3, 2, 1, 0, 4]),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
