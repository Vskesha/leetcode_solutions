import unittest
from functools import cache
from itertools import groupby

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for ch, _ in groupby(s))
        ls = len(s)
        dp = [[0] * ls for _ in range(ls + 1)]
        for i in range(ls):
            dp[i][i] = 1
        for ln in range(2, ls + 1):
            for st, end in zip(range(ls), range(ln - 1, ls)):
                dp[st][end] = 1 + dp[st + 1][end]
                for i in range(st + 2, end + 1):
                    if s[i] == s[st]:
                        dp[st][end] = min(
                            dp[st][end], dp[st][i - 1] + dp[i + 1][end]
                        )

        return dp[0][ls - 1]


class Solution2:
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for ch, _ in groupby(s))

        @cache
        def dp(st: int, end: int) -> int:
            if st > end:
                return 0
            min_turns = 1 + dp(st + 1, end)
            for i in range(st + 1, end + 1):
                if s[i] == s[st]:
                    cur_turns = dp(st, i - 1) + dp(i + 1, end)
                    min_turns = min(min_turns, cur_turns)
            return min_turns

        return dp(0, len(s) - 1)


# iterative solution
class Solution3:
    def strangePrinter(self, s: str) -> int:
        s = "".join(k for k, _ in groupby(s))
        ls = len(s)
        dp = [[0] * ls for _ in range(ls)]

        for ln in range(0, ls):
            for l in range(0, ls - ln):
                r = l + ln
                for j in range(l, r):
                    if s[j] != s[r]:
                        break
                else:
                    dp[l][r] = 0
                    continue

                dp[l][r] = (
                    min(dp[j][i] + dp[i + 1][r] for i in range(j, r)) + 1
                )

        return dp[0][ls - 1] + 1


# recursive dp solution
class Solution4:
    def strangePrinter(self, s: str) -> int:

        @cache
        def dp(l, r):
            for j in range(l, r):
                if s[j] != s[r]:
                    break
            else:
                return 0

            min_turn = min(dp(j, i) + dp(i + 1, r) for i in range(j, r))

            return min_turn + 1

        s = "".join(k for k, _ in groupby(s))
        return 1 + dp(0, len(s) - 1)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["strangePrinter"] * 3,
            "kwargs": [
                dict(s="aaabbb"),
                dict(s="aba"),
                dict(s="baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"),
            ],
            "expected": [2, 2, 19],
        },
    ]


if __name__ == "__main__":
    unittest.main()
