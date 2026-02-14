import unittest
from functools import lru_cache
from itertools import pairwise
from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        ls = len(s)
        ans = []

        def backtrack(comb, ans):
            if comb[-1] == ls:
                ans.append(" ".join(s[st:end] for st, end in pairwise(comb)))
                return

            curr = trie
            for i in range(comb[-1], ls):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.is_end:
                    comb.append(i + 1)
                    backtrack(comb, ans)
                    comb.pop()

        backtrack([0], ans)
        return ans


class Solution0:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def insert(word):
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr["*"] = True

        trie = {}
        for word in wordDict:
            insert(word)
        self.combs = []
        ls = len(s)

        def dfs(i, comb):
            if i == ls:
                self.combs.append(" ".join(comb))
            curr = trie
            for j in range(i, ls):
                ch = s[j]
                if ch not in curr:
                    break
                curr = curr[ch]
                if "*" in curr:
                    word = s[i : j + 1]
                    comb.append(word)
                    dfs(j + 1, comb)
                    comb.pop()

        dfs(0, [])
        return self.combs


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(st, words, ans):
            if st == len(s):
                ans.append(" ".join(words))
                return

            for word in wordDict:
                lw = len(word)
                if word == s[st : st + lw]:
                    words.append(word)
                    dp(st + lw, words, ans)
                    words.pop()

        words, ans = [], []
        dp(0, words, ans)
        return ans


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(word, path):
            if not word:
                res.append(path[1:])

            for i in range(len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordDict:
                    dfs(suffix, path + " " + prefix)

        res = []

        dfs(s, "")

        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameStrings(self, strs1: List[str], strs2: List[str]):
        self.assertEqual(len(strs1), len(strs2))
        self.assertSetEqual(set(strs1), set(strs2))

    def test_wordBreak_1(self):
        print("Test wordBreak 1... ", end="")
        self.assertSameStrings(
            ["cats and dog", "cat sand dog"],
            self.sol.wordBreak(
                s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]
            ),
        )
        print("OK")

    def test_wordBreak_2(self):
        print("Test wordBreak 2... ", end="")
        self.assertSameStrings(
            [
                "pine apple pen apple",
                "pineapple pen apple",
                "pine applepen apple",
            ],
            self.sol.wordBreak(
                s="pineapplepenapple",
                wordDict=["apple", "pen", "applepen", "pine", "pineapple"],
            ),
        )
        print("OK")

    def test_wordBreak_3(self):
        print("Test wordBreak 3... ", end="")
        self.assertSameStrings(
            [],
            self.sol.wordBreak(
                s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
