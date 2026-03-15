import unittest
from math import gcd

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        gcds = []

        for n in nums:
            if n > mx:
                mx = n
            gcds.append(gcd(n, mx))

        gcds.sort()

        return sum(gcd(gcds[i], gcds[~i]) for i in range(len(gcds) // 2))


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["gcdSum"] * 2,
            "kwargs": [
                dict(nums=[2, 6, 4]),
                dict(nums=[3, 6, 2, 8]),
            ],
            "expected": [2, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()
