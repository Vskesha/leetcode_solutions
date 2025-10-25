import json
import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countWinningSequences(self, s: str) -> int:
        ls = len(s)
        mod = 10**9 + 7
        mcs = "FWE"
        s = [mcs.find(ch) for ch in s]

        dp = [Counter() for _ in range(3)]

        for mc in range(3):
            d = (mc - s[0] + 1) % 3 - 1
            dp[mc][d] = 1

        for i in range(1, ls):
            ndp = [Counter() for _ in range(3)]
            for mc in range(3):
                d = (mc - s[i] + 1) % 3 - 1
                for nmc in range(mc + 1, mc + 3):
                    for v, combs in dp[nmc % 3].items():  # noqa
                        ndp[mc][v + d] = (ndp[mc][v + d] + combs) % mod
            dp = ndp

        return (
            sum(sum(v for k, v in cnt.items() if k > 0) % mod for cnt in dp)
            % mod
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countWinningSequences"] * 2,
            "kwargs": [
                dict(s="FFF"),
                dict(s="FWEFW"),
            ],
            "expected": [3, 18],
        },
    ]


if __name__ == "__main__":
    unittest.main()
