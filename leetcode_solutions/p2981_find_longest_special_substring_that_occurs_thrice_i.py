import unittest
from collections import Counter
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = Counter()

        for k, gr in groupby(s):
            ln = len(list(gr))
            for i in range(min(3, ln)):
                cnt[k * (ln - i)] += i + 1

        ans = -1
        for k, v in cnt.items():
            if v > 2:
                ans = max(ans, len(k))

        return ans


class Solution2:
    def maximumLength(self, s: str) -> int:
        ls = len(s)
        i = ans = 0
        cnt = Counter()

        while i < ls:
            sti = i
            while i < ls and s[i] == s[sti]:
                i += 1
            d = i - sti
            while d > ans:
                cnt[s[sti] * d] += i - sti - d + 1
                if cnt[s[sti] * d] > 2:
                    ans = d
                d -= 1

        return ans if ans else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumLength"] * 3,
            "kwargs": [
                dict(s="aaaa"),
                dict(s="abcdef"),
                dict(s="abcaba"),
            ],
            "expected": [2, -1, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
