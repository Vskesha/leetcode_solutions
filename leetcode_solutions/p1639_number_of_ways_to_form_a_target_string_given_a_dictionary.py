import unittest
from collections import Counter
from functools import cache, lru_cache
from typing import List

from leetcode_solutions._test_meta import TestMeta


# the best iterative dp solution
class Solution:
    def numWays(self, words: list[str], target: str) -> int:

        lt, lw = len(target), len(words[0])
        if lw < lt:
            return 0
        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]
        size = lw - lt + 2
        dp = [1] * size

        for i in range(1, lt + 1):
            new = [0] * size
            for j in range(1, size):
                new[j] = (new[j - 1] + aux[i + j - 2][target[i - 1]] * dp[j]) % mod
            dp = new

        return dp[-1]


# 2 better iterative dp solutions
class Solution1:
    def numWays(self, words: list[str], target: str) -> int:

        lt, lw = len(target), len(words[0])
        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]
        dp = [1] * (lw + 1)

        for i in range(1, lt + 1):
            new = [0] * (lw + 1)
            for j in range(i, lw - lt + i + 1):
                new[j] = (new[j - 1] + aux[j - 1][target[i - 1]] * dp[j - 1]) % mod
            dp = new

        return dp[lw]


class Solution2:
    def numWays(self, words: list[str], target: str) -> int:

        lt, lw = len(target), len(words[0])
        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]
        dp = [[0] * (lw + 1) for _ in range(lt + 1)]
        dp[0] = [1] * (lw + 1)

        for i in range(1, lt + 1):
            for j in range(i, lw - lt + i + 1):
                dp[i][j] = (
                    dp[i][j - 1] + aux[j - 1][target[i - 1]] * dp[i - 1][j - 1]
                ) % mod

        return dp[lt][lw]


# better recursive dp solution
class Solution3:
    def numWays(self, words: list[str], target: str) -> int:

        lw = len(words[0])
        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]

        @lru_cache(None)
        def dp(it, iw):
            if iw < it:
                return 0
            if not it:
                return 1
            res = dp(it, iw - 1)
            val = aux[iw - 1][target[it - 1]]
            res += val * dp(it - 1, iw - 1)
            return res % mod

        return dp(len(target), lw)


# iterative dp solution
class Solution4:
    def numWays(self, words: list[str], target: str) -> int:

        lw, lt = len(words[0]), len(target)
        if lw < lt:
            return 0

        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]

        dp = [[0] * (lw + 1) for _ in range(lt + 1)]
        dp[0] = [1] * (lw + 1)

        for i in range(1, lt + 1):
            ch = target[i - 1]
            for j in range(i, lw - lt + i + 1):
                for k in range(i, j + 1):
                    val = aux[k - 1][ch]
                    if val:
                        dp[i][j] += val * dp[i - 1][k - 1]
                        dp[i][j] %= mod

        return dp[lt][lw]


# recursive dp solution
class Solution5:
    def numWays(self, words: list[str], target: str) -> int:

        lw, lt = len(words[0]), len(target)
        if lw < lt:
            return 0

        mod = 1_000_000_007
        aux = [Counter(w[i] for w in words) for i in range(lw)]

        @lru_cache(None)
        def dp(iw, it) -> int:
            if it < 0:
                return 1
            res = 0
            ch = target[it]
            for i in range(it, iw + 1):
                res += aux[i][ch] * dp(i - 1, it - 1)
                res %= mod
            return res

        return dp(lw - 1, lt - 1)


class Solution6:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        lt, lw = len(target), len(words[0])
        aux = [Counter(w[i] for w in words) for i in range(lw)]

        @cache
        def dp(ti, wi):
            if ti == lt:
                return 1
            if wi == lw:
                return 0
            cnt = aux[wi]
            ch = target[ti]
            ans = dp(ti, wi + 1)
            if cnt[ch]:
                ans = (ans + cnt[ch] * dp(ti + 1, wi + 1)) % mod
            return ans

        return dp(0, 0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numWays"] * 2,
            "kwargs": [
                dict(words=["acca", "bbbb", "caca"], target="aba"),
                dict(words=["abba", "baab"], target="bab"),
            ],
            "expected": [6, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
