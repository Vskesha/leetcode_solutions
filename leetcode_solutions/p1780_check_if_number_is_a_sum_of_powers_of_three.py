import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = 1
        while p <= n:
            p *= 3

        while p:
            p //= 3
            if p <= n:
                n -= p

        return n == 0


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkPowersOfThree"] * 3,
            "kwargs": [
                dict(n=12),
                dict(n=91),
                dict(n=21),
            ],
            "expected": [True, True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
