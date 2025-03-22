import unittest
from functools import reduce
from itertools import accumulate, groupby
from math import comb

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        sum_mod = lambda x, y: (x + y) % mod
        mul_mod = lambda x, y: (x * y) % mod

        groups = [len(list(gr)) for _, gr in groupby(word)]
        total = reduce(mul_mod, groups)

        if len(groups) >= k:
            return total

        dp = [0] * k
        dp[0] = 1

        for i, gr in enumerate(groups):
            acc = list(accumulate(dp, sum_mod, initial=0))
            dp = [0] * k
            for j in range(i, k):
                dp[j] = acc[j] - acc[j - min(j - i, gr)]

        less = reduce(sum_mod, dp)
        return (total - less) % mod


# Time Limit Exceeded
class Solution1:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        groups = [len(list(gr)) for _, gr in groupby(word)]
        co = len(word) - k + 1
        dp = [1] * co

        for cgr in groups:
            ndp = [0] * co
            acc = [0]
            for val in dp:
                acc.append((val + acc[-1]) % mod)
            for oml in range(min(cgr, co)):
                ndp[oml] = acc[oml + 1] % mod
            for oml in range(cgr, co):
                ndp[oml] = (acc[oml + 1] - acc[oml - cgr + 1]) % mod
            dp = ndp
        return dp[-1]


# Time Limit Exceeded
class Solution2:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        groups = [len(list(gr)) for _, gr in groupby(word)]
        lg = len(groups)
        co = len(word) - k + 1
        dp = [1] * co

        for gi in range(lg):
            ndp = [0] * co
            cgr = groups[gi]
            for oml in range(co):
                chrs = min(oml + 1, cgr)
                for d in range(chrs):
                    ndp[oml] = (ndp[oml] + dp[oml - d]) % mod
            dp = ndp
        return dp[-1]


# Time Limit Exceeded
class Solution3:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        total = 0
        groups = 0

        for _, gr in groupby(word):
            groups += 1
            total = total * len(list(gr)) % mod

        if groups >= k:
            return total

        left = total - groups
        less = 0
        for ln in range(groups, k):
            needed = ln - groups
            less = (less + comb(left, needed)) % mod

        return (total - less) % mod


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["possibleStringCount"] * 3,
            "kwargs": [
                dict(word="aabbccdd", k=7),
                dict(word="aabbccdd", k=8),
                dict(word="aaabbb", k=3),
            ],
            "expected": [5, 1, 8],
        },
    ]


if __name__ == "__main__":
    unittest.main()
