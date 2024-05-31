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


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dp(st, words, ans):
            if st == len(s):
                ans.append(' '.join(words))
                return

            for word in wordDict:
                l = len(word)
                if word == s[st:st + l]:
                    words.append(word)
                    dp(st + l, words, ans)
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


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sorted(sol.wordBreak(
        s="catsanddog",
        wordDict=["cat", "cats", "and", "sand", "dog"]
    )) == sorted(["cats and dog", "cat sand dog"])
    print('OK')

    print('Test 2... ', end='')
    assert sorted(sol.wordBreak(
        s="pineapplepenapple",
        wordDict=["apple", "pen", "applepen", "pine", "pineapple"]
    )) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    print('OK')

    print('Test 3... ', end='')
    assert sorted(sol.wordBreak(
        s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
    )) == sorted([])
    print('OK')


if __name__ == '__main__':
    test()
