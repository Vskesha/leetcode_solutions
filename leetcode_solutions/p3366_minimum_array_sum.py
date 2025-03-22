import unittest
from bisect import bisect_left
from functools import cache
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        nums.sort()
        k2 = k % 2
        ln = len(nums)
        i = bisect_left(nums, k)
        mj = bisect_left(nums, k * 2 - 1)
        j = ln - 1

        while op1 and j >= mj:
            nums[j] = (nums[j] + 1) // 2
            op1 -= 1
            if op2:
                nums[j] -= k
                op2 -= 1
            j -= 1

        candidates = set()
        while op2 and i <= j:
            if k2 and nums[i] % 2 == 0:
                candidates.add(i)
            nums[i] -= k
            op2 -= 1
            i += 1

        swaps = 0
        while op1 and i <= j:
            if k2 and nums[j] % 2:
                swaps += 1
            nums[j] = (nums[j] + 1) // 2
            op1 -= 1
            j -= 1

        if op1:
            snums = sorted([(nums[si], si) for si in range(i)])
            while op1:
                n, si = snums.pop()
                nums[si] = (n + 1) // 2
                if swaps and si in candidates:
                    nums[si] -= 1
                    swaps -= 1
                op1 -= 1

        return sum(nums)


class Solution1:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        nums.sort()
        ln = len(nums)
        mi = i = bisect_left(nums, k)
        mj = bisect_left(nums, k * 2 - 1)
        j = ln - 1

        while op1 and j >= mj:
            nums[j] = (nums[j] + 1) // 2
            op1 -= 1
            if op2:
                nums[j] -= k
                op2 -= 1
            j -= 1

        while op2 and i <= j:
            nums[i] -= k
            op2 -= 1
            i += 1

        if k % 2:
            swaps = 0
            while op1 and i <= j:
                swaps += nums[j] % 2
                nums[j] = (nums[j] + 1) // 2
                op1 -= 1
                j -= 1
            pi = mi - 1
            while op1:
                if j < mi or (pi >= 0 and nums[pi] > nums[j]):
                    nums[pi] = (nums[pi] + 1) // 2
                    pi -= 1
                else:
                    is_candidate = nums[j] % 2
                    nums[j] = (nums[j] + 1) // 2
                    if swaps and is_candidate:
                        nums[j] -= 1
                        swaps -= 1
                    j -= 1
                op1 -= 1
        else:
            while op1 and i <= j:
                nums[j] = (nums[j] + 1) // 2
                op1 -= 1
                j -= 1
            pi = mi - 1
            while op1:
                if j < mi or (pi >= 0 and nums[pi] > nums[j]):
                    nums[pi] = (nums[pi] + 1) // 2
                    pi -= 1
                else:
                    nums[j] = (nums[j] + 1) // 2
                    j -= 1
                op1 -= 1

        return sum(nums)


class Solution2:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @cache
        def dp(i, op1, op2):
            if op1 < 0 or op2 < 0:
                return -inf
            if i < 0:
                return 0
            ans = dp(i - 1, op1, op2)
            if nums[i] >= k:
                ans = max(ans, k + dp(i - 1, op1, op2 - 1))
                pr12 = dp(i - 1, op1 - 1, op2 - 1)
                d = nums[i] - (nums[i] - k + 1) // 2
                ans = max(ans, d + pr12)
                if nums[i] >= k * 2 - 1:
                    d = nums[i] - (nums[i] + 1) // 2 + k
                    ans = max(ans, d + pr12)
            ans = max(ans, nums[i] // 2 + dp(i - 1, op1 - 1, op2))

        red = dp(len(nums) - 1, op1, op2)
        return sum(nums) - red


class Solution3:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        dp = [[0] * (op2 + 1) for _ in range(op1 + 1)]
        ndp = [[0] * (op2 + 1) for _ in range(op1 + 1)]

        for i, n in enumerate(nums):
            for o1 in range(op1 + 1):
                for o2 in range(op2 + 1):
                    ans = dp[o1][o2]
                    if n >= k and o2:
                        ans = max(ans, k + dp[o1][o2 - 1])
                        if o1:
                            d = n - (n - k + 1) // 2
                            ans = max(ans, d + dp[o1 - 1][o2 - 1])
                            if n >= k * 2 - 1:
                                d = n // 2 + k
                                ans = max(ans, d + dp[o1 - 1][o2 - 1])
                    if o1:
                        ans = max(ans, n // 2 + dp[o1 - 1][o2])
                    ndp[o1][o2] = ans
            dp, ndp = ndp, dp

        res = sum(nums)
        res -= dp[-1][-1]
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minArraySum"] * 4,
            "kwargs": [
                dict(
                    nums=[882, 307, 624, 469, 329, 684, 851, 608, 317, 205],
                    k=431,
                    op1=9,
                    op2=4,
                ),
                dict(nums=[2, 8, 3, 19, 3], k=3, op1=1, op2=1),
                dict(nums=[2, 4, 3], k=3, op1=2, op2=1),
                dict(
                    nums=[1, 3, 5, 7, 9, 12, 12, 12, 13, 15, 15, 15, 16, 17, 19, 20],
                    k=11,
                    op1=15,
                    op2=4,
                ),
            ],
            "expected": [1582, 23, 3, 77],
        },
    ]


if __name__ == "__main__":
    unittest.main()
