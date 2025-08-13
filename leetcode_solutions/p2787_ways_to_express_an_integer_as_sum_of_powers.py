import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        ls = [it for it in range(1, n + 1)]
        f = [0] * (n + 1)
        f[0] = 1
        for k in range(1, n + 1):
            v = k**x
            if v > n:
                break
            for j in range(n, v - 1, -1):
                f[j] = f[j] + f[j - v]

        return f[-1] % 1_000_000_007


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfWays"] * 3,
            "kwargs": [
                dict(n = 10, x = 2),
                dict(n = 4, x = 1),
                dict(n = 64, x = 3),
            ],
            "expected": [1, 2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
