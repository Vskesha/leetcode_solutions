import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:

        def is_hd_one(word1, word2):
            if len(word1) != len(word2):
                return False
            diff = False
            for a, b in zip(word1, word2):
                if a != b:
                    if diff:
                        return False
                    diff = True
            return diff

        lw = len(words)
        dp = [1] * lw
        nxt = [0] * lw

        for i in range(lw - 2, -1, -1):
            for j in range(i + 1, lw):
                if (
                    dp[i] <= dp[j]
                    and groups[i] != groups[j]
                    and is_hd_one(words[i], words[j])
                ):
                    dp[i] = dp[j] + 1
                    nxt[i] = j

        mi = dp.index(max(dp))
        ans = [words[mi]]
        while nxt[mi]:
            mi = nxt[mi]
            ans.append(words[mi])

        return ans


class Solution2:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:

        def is_hd_one(word1: str, word2: str) -> bool:
            if len(word1) != len(word2):
                return False
            diff = False
            for a, b in zip(word1, word2):
                if a != b:
                    if diff:
                        return False
                    diff = True
            return diff

        lw = len(words)
        dp = [1] * lw
        prev = [-1] * lw

        for j in range(1, lw):
            for i in range(j - 1, -1, -1):
                if (
                    dp[j] <= dp[i]
                    and groups[i] != groups[j]
                    and is_hd_one(words[i], words[j])
                ):
                    dp[j] = max(dp[j], dp[i] + 1)
                    prev[j] = i

        mi = dp.index(max(dp))
        path = [mi]
        while prev[path[-1]] != -1:
            path.append(prev[path[-1]])

        ans = [words[i] for i in reversed(path)]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getWordsInLongestSubsequence"] * 2,
            "kwargs": [
                dict(words=["bab", "dab", "cab"], groups=[1, 2, 2]),
                dict(words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]),
            ],
            "expected": [["bab", "dab"], ["a", "b", "c", "d"]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
