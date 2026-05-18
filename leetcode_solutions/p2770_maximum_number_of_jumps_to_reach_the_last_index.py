import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        sl = SortedList()
        sl.add((0, nums[0]))
        ln = len(nums)

        for i in range(1, ln - 1):
            for j in range(len(sl) - 1, -1, -1):
                if abs(sl[j][1] - nums[i]) <= target:
                    sl.add((sl[j][0] + 1, nums[i]))
                    break

        for j in range(len(sl) - 1, -1, -1):
            if abs(sl[j][1] - nums[-1]) <= target:
                return sl[j][0] + 1

        return -1


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumJumps"] * 3,
            "kwargs": [
                dict(nums=[1, 3, 6, 4, 1, 2], target=2),
                dict(nums=[1, 3, 6, 4, 1, 2], target=3),
                dict(nums=[1, 3, 6, 4, 1, 2], target=0),
            ],
            "expected": [3, 5, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
