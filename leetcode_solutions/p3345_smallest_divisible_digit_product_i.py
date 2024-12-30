import operator
import unittest
from functools import reduce

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n % 10 and reduce(operator.mul, (int(d) for d in str(n))) % t:
            n += 1
        return n


class Solution2:
    def smallestNumber(self, n: int, t: int) -> int:
        for k in range(n, n + 10):
            pr = 1
            for d in str(k):
                pr *= int(d)
            if pr % t == 0:
                return k


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["smallestNumber"] * 2,
            "kwargs": [
                dict(n=10, t=2),
                dict(n=15, t=3),
            ],
            "expected": [10, 16],
        },
    ]


if __name__ == "__main__":
    unittest.main()
