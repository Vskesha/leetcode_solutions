import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t = sum(nums) % p
        if not t:
            return 0
        rems = {0: 0}
        r, ans = 0, len(nums)
        for i, n in enumerate(nums, 1):
            r = (r + n) % p
            ct = (r - t) % p
            if ct in rems:
                ans = min(ans, i - rems[ct])
            rems[r] = i

        return -1 if ans == len(nums) else ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minSubarray"] * 3,
            "kwargs": [
                dict(nums=[3, 1, 4, 2], p=6),
                dict(nums=[6, 3, 5, 2], p=9),
                dict(nums=[1, 2, 3], p=3),
            ],
            "expected": [1, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
