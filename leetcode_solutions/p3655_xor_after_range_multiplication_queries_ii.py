import operator
import unittest
from functools import reduce
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def xorAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> int:
        mod = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for left, right, k, val in queries:
            if k < T:
                groups[k].append((left, right, val))
            else:
                for i in range(left, right + 1, k):
                    nums[i] = nums[i] * val % mod

        for k in range(1, T):
            if not groups[k]:
                continue
            dif = [1] * (n + T)
            for left, right, val in groups[k]:
                dif[left] = dif[left] * val % mod
                R = ((right - left) // k + 1) * k + left
                dif[R] = dif[R] * pow(val, mod - 2, mod) % mod

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        return reduce(operator.xor, nums)


class Solution3:
    MOD = 10**9 + 7

    def xorAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> int:
        for left, right, k, v in queries:
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        res = 0
        for x in nums:
            res ^= x

        return res


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["xorAfterQueries"] * 2,
            "kwargs": [
                dict(nums=[1, 1, 1], queries=[[0, 2, 1, 4]]),
                dict(
                    nums=[2, 3, 1, 5, 4], queries=[[1, 4, 2, 3], [0, 2, 1, 2]]
                ),
            ],
            "expected": [4, 31],
        },
    ]


if __name__ == "__main__":
    unittest.main()
