import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def can_rob_k_houses(capability):
            cnt = 0
            taken = False
            for n in nums:
                if taken:
                    taken = False
                elif n <= capability:
                    cnt += 1
                    taken = True

            return cnt >= k

            # or...

            # i = cnt = 0
            # while i < len(nums):
            #     if nums[i] <= capability:
            #         cnt += 1
            #         i += 2
            #     else:
            #         i += 1
            # return cnt >= k

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_k_houses(mid):
                right = mid
            else:
                left = mid + 1
        return right


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minCapability"] * 2,
            "kwargs": [
                dict(nums=[2, 3, 5, 9], k=2),
                dict(nums=[2, 7, 9, 3, 1], k=2),
            ],
            "expected": [5, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
