import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        ans = odd = even = 0

        for n in arr:
            if n % 2:
                odd, even = even + 1, odd
            else:
                even += 1
            ans = (ans + odd) % mod

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numOfSubarrays"] * 3,
            "kwargs": [
                dict(arr=[1, 3, 5]),
                dict(arr=[2, 4, 6]),
                dict(arr=[1, 2, 3, 4, 5, 6, 7]),
            ],
            "expected": [4, 0, 16],
        },
    ]


if __name__ == "__main__":
    unittest.main()
