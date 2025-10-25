import unittest
from bisect import bisect_left, bisect_right
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    mn = 10**6 + 1
    primes_grid = [True] * mn
    primes = []
    for i in range(2, mn):
        if primes_grid[i]:
            primes.append(i)
            j = i * 2
            while j < mn:
                primes_grid[j] = False
                j += i

    def closestPrimes(self, left: int, right: int) -> List[int]:
        li = bisect_left(self.primes, left)
        ri = bisect_right(self.primes, right)
        min_diff = 10**6
        ans = [-1, -1]
        for i in range(li, ri - 1):
            diff = self.primes[i + 1] - self.primes[i]
            if diff < min_diff:
                if diff == 2:
                    return [self.primes[i], self.primes[i + 1]]
                min_diff = diff
                ans = [self.primes[i], self.primes[i + 1]]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["closestPrimes"] * 3,
            "kwargs": [
                dict(left=10, right=19),
                dict(left=4, right=6),
                dict(left=19, right=31),
            ],
            "expected": [
                [11, 13],
                [-1, -1],
                [29, 31],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
