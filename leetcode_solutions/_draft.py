import string
import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = Counter(s)
        lc = string.ascii_lowercase
        prev = {lc[i]: lc[i - 1] for i in range(26)}

        for _ in range(t):
            ndp = Counter()
            for ch in lc:
                ndp[ch] = dp[prev[ch]]
            ndp["b"] += dp["z"]
            dp = ndp

        return sum(dp.values())


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lengthAfterTransformations"] * 2,
            "kwargs": [
                dict(s = "abcyy", t = 2),
                dict(s = "azbk", t = 1),
            ],
            "expected": [7, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()
