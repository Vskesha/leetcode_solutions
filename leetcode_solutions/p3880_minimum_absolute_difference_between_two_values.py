import unittest

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        i1 = i2 = -n
        ans = n

        for i, num in enumerate(nums):
            if num == 1:
                i1 = i
                ans = min(ans, i1 - i2)
            elif num == 2:
                i2 = i
                ans = min(ans, i2 - i1)

        return -1 if ans == n else ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minAbsoluteDifference"] * 2,
            "kwargs": [
                dict(nums=[1, 0, 0, 2, 0, 1]),
                dict(nums=[1, 0, 1, 0]),
            ],
            "expected": [2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
