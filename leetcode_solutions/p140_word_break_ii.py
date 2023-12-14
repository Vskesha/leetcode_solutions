from functools import lru_cache
from typing import List


class Solution:
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
