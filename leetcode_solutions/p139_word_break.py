from functools import lru_cache, cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def dp(st) -> bool:
            if st == len(s):
                return True

            for word in wordDict:
                l = len(word)
                if word == s[st:st + l] and dp(st + l):
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


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.wordBreak(s="leetcode", wordDict=["leet", "code"]) is True
    print('OK')

    print('Test 2... ', end='')
    assert sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) is True
    print('OK')

    print('Test 3... ', end='')
    assert sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) is False
    print('OK')


if __name__ == '__main__':
    test()
