import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        cnt = Counter(s)
        if cnt["a"] < k or cnt["b"] < k or cnt["c"] < k:
            return -1

        r = 0
        ans = ls = len(s)

        for i, ch in enumerate(s):
            while r < ls:
                if cnt[s[r]] == k:
                    break
                cnt[s[r]] -= 1
                r += 1
            ans = min(ans, i + ls - r)
            cnt[ch] += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["takeCharacters"] * 2,
            "kwargs": [
                dict(s="aabaaaacaabc", k=2),
                dict(s="a", k=1),
            ],
            "expected": [8, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
