import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {ch: i for i, ch in enumerate("aeiou")}
        seen = {0: -1}
        mask = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch in vowels:
                mask ^= 1 << vowels[ch]
            if mask in seen:
                curr = i - seen[mask]
                ans = max(ans, curr)
            else:
                seen[mask] = i

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findTheLongestSubstring"] * 3,
            "kwargs": [
                dict(s="eleetminicoworoep"),
                dict(s="leetcodeisgreat"),
                dict(s="bcbcbc"),
            ],
            "expected": [13, 5, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()
