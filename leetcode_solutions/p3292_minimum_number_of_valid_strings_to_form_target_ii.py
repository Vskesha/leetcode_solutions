import unittest
from functools import cache
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        lt = len(target)

        def is_valid_prefix(pref: str) -> bool:
            for word in words:
                if word.startswith(pref):
                    return True
            return False

        dp = [0] * (lt + 1)
        left = 0
        for right in range(1, lt + 1):
            while left < right and not is_valid_prefix(target[left:right]):
                left += 1
            if left == right:
                return -1
            dp[right] = dp[left] + 1
        return dp[-1]


class Solution2:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        lt = len(target)

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

        def is_valid_prefix(pref: str) -> bool:
            curr = trie
            for ch in pref:
                if ch not in curr:
                    return False
                curr = curr[ch]
            return True

        dp = [0] * (lt + 1)
        left = 0
        for r in range(1, lt + 1):
            while left < r and not is_valid_prefix(target[left:r]):
                left += 1
            if left == r:
                return -1
            dp[r] = dp[left] + 1
        return dp[-1]


class Solution3:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        lt = len(target)

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

        memo = [inf] * lt
        memo.append(0)

        def dp(i):
            if memo[i] != inf:
                return memo[i]
            ans = inf
            curr = trie
            j = i
            while j < lt and target[j] in curr:
                res = dp(j + 1) + 1
                ans = min(ans, res)
                curr = curr[target[j]]
                j += 1

            memo[i] = ans
            return ans

        ans = dp(0)
        return -1 if ans == inf else ans


class Solution4:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        lt = len(target)

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

        @cache
        def dp(i):
            if i == lt:
                return 0
            ans = inf
            curr = trie
            while i < lt and target[i] in curr:
                res = dp(i + 1) + 1
                ans = min(ans, res)
                curr = curr[target[i]]
                i += 1
            return ans

        ans = dp(0)
        return -1 if ans == inf else ans


class Solution5:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        lt = len(target)

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

        dp = [inf] * lt
        dp.append(0)
        for i in range(lt - 1, -1, -1):
            curr = trie
            for j in range(i, lt):
                if target[j] not in curr:
                    break
                dp[i] = min(dp[i], 1 + dp[j + 1])
                curr = curr[target[j]]

        return -1 if dp[0] == inf else dp[0]


class Solution6:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        lt = len(target)

        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]

        dp = [inf] * lt
        dp.append(0)
        stack = [(0, lt)]
        for i in range(lt - 1, -1, -1):
            curr = trie
            cnt = 0
            for j in range(i, lt):
                if target[j] not in curr:
                    break
                cnt += 1
                curr = curr[target[j]]
            mi = i + cnt
            if stack[-1][1] <= mi:
                while len(stack) > 1 and stack[-2][1] <= mi:
                    stack.pop()
                dp[i] = stack[-1][0] + 1
                stack.append((dp[i], i))

        return -1 if dp[0] == inf else dp[0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minValidStrings"] * 3,
            "kwargs": [
                dict(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"),
                dict(words=["abababab", "ab"], target="ababaababa"),
                dict(words=["abcdef"], target="xyz"),
            ],
            "expected": [3, 2, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
