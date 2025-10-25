import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        return sum(set(w).issubset(allow) for w in words)


class Solution1:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    break
            else:
                ans += 1
        return ans


class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = [False] * 125
        for ch in allowed:
            allow[ord(ch)] = True
        ans = 0
        for word in words:
            for ch in word:
                if not allow[ord(ch)]:
                    break
            else:
                ans += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countConsistentStrings"] * 3,
            "kwargs": [
                dict(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]),
                dict(
                    allowed="abc",
                    words=["a", "b", "c", "ab", "ac", "bc", "abc"],
                ),
                dict(
                    allowed="cad",
                    words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
                ),
            ],
            "expected": [2, 7, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
