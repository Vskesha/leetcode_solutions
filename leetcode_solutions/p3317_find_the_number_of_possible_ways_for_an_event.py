import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10 ** 9 + 7

        stirling = [0] * (x + 1)
        stirling[1] = 1
        for sn in range(2, n + 1):
            for sk in range(min(sn, x), 1, -1):
                stirling[sk] = (stirling[sk] * sk + stirling[sk - 1]) % mod

        comb = [1]
        for cr in range(1, x + 1):
            for ci in range(cr - 1, 0, -1):
                comb[ci] = (comb[ci] + comb[ci - 1]) % mod
            comb.append(1)

        pw = fact = 1
        ans = 0

        for i in range(1, min(x, n) + 1):
            pw = (pw * y) % mod
            fact = (fact * i) % mod
            ans = (ans + comb[i] * stirling[i] * fact * pw) % mod

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfWays"] * 3,
            "kwargs": [
                dict(n=1, x=2, y=3),
                dict(n=5, x=2, y=1),
                dict(n=3, x=3, y=4),
            ],
            "expected": [6, 32, 684],
        },
    ]


if __name__ == "__main__":
    unittest.main()
