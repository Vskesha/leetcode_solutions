import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    primes = [True] * 50001
    primes[0] = primes[1] = False

    for i in range(2, 50001):
        if primes[i]:
            for j in range(i * 2, 50001, i):
                primes[j] = False

    def primeSubarray(self, nums: List[int], k: int) -> int:
        ci = pi = -1
        ans = sti = 0
        sl = SortedList()

        for i, n in enumerate(nums):
            if self.primes[n]:
                pi = ci
                ci = i
                sl.add(n)
                while sl and sl[-1] - sl[0] > k:
                    if self.primes[nums[sti]]:
                        sl.remove(nums[sti])
                    sti += 1

            if len(sl) > 1:
                ans += pi - sti + 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["primeSubarray"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 3], k=1),
                dict(nums=[2, 3, 5, 7], k=3),
            ],
            "expected": [2, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
