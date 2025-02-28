import unittest
from heapq import heappush, heappop

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        ugly = [(1, 0)]
        ug = 1

        for _ in range(n):
            ug, st = heappop(ugly)
            for j in range(st, 3):
                heappush(ugly, (ug * primes[j], j))

        return ug


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["nthUglyNumber"] * 2,
            "kwargs": [
                dict(n = 10),
                dict(n=1),
            ],
            "expected": [12, 1],
        },
    ]


if __name__ == '__main__':
    unittest.main()