import unittest
from collections import defaultdict

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestBalanced"] * 3,
            "kwargs": [
                dict(s="abbac"),
                dict(s="zzabccy"),
                dict(s="aba"),
            ],
            "expected": [4, 4, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
