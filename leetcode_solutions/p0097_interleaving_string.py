import unittest
from collections import Counter
from functools import cache, lru_cache

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)

        if ls3 != ls1 + ls2:
            return False

        if Counter(s1 + s2) != Counter(s3):
            return False

        @lru_cache(None)
        def interleave(i, j):
            if not i:
                return s2[:j] == s3[:j]
            if not j:
                return s1[:i] == s3[:i]

            k = i + j
            if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                return interleave(i - 1, j) or interleave(i, j - 1)
            if s1[i - 1] == s3[k - 1]:
                return interleave(i - 1, j)
            if s2[j - 1] == s3[k - 1]:
                return interleave(i, j - 1)

            return False

        return interleave(ls1, ls2)


# iterative dp solution
class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        if l2 > l1:
            s1, l1, s2, l2 = s2, l2, s1, l1

        dp = [False] * (l2 + 1)
        dp[0] = True
        j = 0
        while j < l2 and s2[j] == s3[j]:
            dp[j + 1] = True
            j += 1

        for i in range(l1):
            new_dp = [False] * (l2 + 1)
            new_dp[0] = dp[0] and s1[i] == s3[i]
            for j in range(1, l2 + 1):
                new_dp[j] = (dp[j] and s1[i] == s3[i + j]) or (new_dp[j - 1] and s2[j - 1] == s3[i + j])
            dp = new_dp

        return dp[l2]


# recursive dp solution
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        @cache
        def dp(i, j) -> bool:
            if i + j == l3:
                return True
            return ((i < l1 and s1[i] == s3[i + j] and dp(i + 1, j)) or
                    (j < l2 and s2[j] == s3[i + j] and dp(i, j + 1)))

        return dp(0, 0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["isInterleave"] * 3,
            "kwargs": [
                dict(s1="aabcc", s2="dbbca", s3="aadbbcbcac"),
                dict(s1="aabcc", s2="dbbca", s3="aadbbbaccc"),
                dict(s1="", s2="", s3=""),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == '__main__':
    unittest.main()
