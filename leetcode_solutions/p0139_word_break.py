import unittest
from functools import cache, lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dp(st) -> bool:
            if st == len(s):
                return True

            for word in wordDict:
                l = len(word)
                if word == s[st : st + l] and dp(st + l):
                    return True

            return False

        return dp(0)


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def wb(i):
            if i == ls:
                return True
            for word in wordDict:
                if len(word) > ls - i:
                    continue
                for j, ch in enumerate(word, i):
                    if s[j] != ch:
                        break
                else:
                    if wb(i + len(word)):
                        return True
            return False

        ls = len(s)
        return wb(0)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_wordBreak_1(self):
        print("Test wordBreak 1... ", end="")
        self.assertTrue(self.sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))
        print("OK")

    def test_wordBreak_2(self):
        print("Test wordBreak 2... ", end="")
        self.assertTrue(
            self.sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
        )
        print("OK")

    def test_wordBreak_3(self):
        print("Test wordBreak 3... ", end="")
        self.assertFalse(
            self.sol.wordBreak(
                s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
