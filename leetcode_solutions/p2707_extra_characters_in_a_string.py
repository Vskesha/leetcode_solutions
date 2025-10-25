import unittest
from functools import lru_cache

from leetcode_solutions._test_meta import TestMeta


# recursive dp solution using trie
class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        curr.is_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:

        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        ls = len(s)
        dp = [0] * (ls + 1)

        for i in range(ls - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            curr = trie
            for j in range(i, ls):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]


# iterative dp solution
class Solution1:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        ls = len(s)
        dp = [0] * (ls + 1)

        for i in range(ls - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for word in dictionary:
                if word[0] == s[i] and word == s[i : i + len(word)]:
                    dp[i] = min(dp[i], dp[i + len(word)])

        return dp[0]


# recursive dp solution
class Solution2:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        ls = len(s)

        @lru_cache(None)
        def dp(i) -> int:
            if i == ls:
                return 0
            ans = dp(i + 1) + 1
            for word in dictionary:
                if word == s[i : i + len(word)]:
                    ans = min(ans, dp(i + len(word)))
            return ans

        return dp(0)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minExtraChar"] * 2,
            "kwargs": [
                dict(s="leetscode", dictionary=["leet", "code", "leetcode"]),
                dict(s="sayhelloworld", dictionary=["hello", "world"]),
            ],
            "expected": [1, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()


def main():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert (
        sol.minExtraChar(
            s="leetscode", dictionary=["leet", "code", "leetcode"]
        )
        == 1
    )
    print("ok\nTest 2 ... ", end="")
    assert (
        sol.minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]) == 3
    )
    print("ok")


if __name__ == "__main__":
    main()
