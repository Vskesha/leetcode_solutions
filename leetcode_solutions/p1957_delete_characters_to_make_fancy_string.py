import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]
        for i in range(2, len(s)):
            if s[i] != ans[-1] or s[i] != ans[-2]:
                ans += s[i]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["makeFancyString"] * 3,
            "kwargs": [
                dict(s="leeetcode"),
                dict(s="aaabaaaa"),
                dict(s="aab"),
            ],
            "expected": ["leetcode", "aabaa", "aab"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
