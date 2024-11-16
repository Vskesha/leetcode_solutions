import unittest
from functools import cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    primes = [True] * 1001
    primes[0] = primes[1] = False
    for n in range(2, 1001):
        if primes[n]:
            for k in range(n * 2, 1001, n):
                primes[k] = False

    @cache
    def get_next_prime(self, n):
        for k in range(n + 1, 1001):
            if self.primes[k]:
                return k
        return 1001

    def primeSubOperation(self, nums: List[int]) -> bool:
        ln = len(nums)
        for i in range(ln - 2, -1, -1):
            diff = nums[i] - nums[i + 1]
            if diff < 0:
                continue
            pr = self.get_next_prime(diff)
            if pr < nums[i]:
                nums[i] -= pr
            else:
                return False

        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["primeSubOperation"] * 3,
            "kwargs": [
                dict(nums=[4, 9, 6, 10]),
                dict(nums=[6, 8, 11, 12]),
                dict(nums=[5, 8, 3]),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
