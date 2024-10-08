import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minSwaps(self, s: str) -> int:
        l, r = 0, len(s) - 1
        bal = ans = 0

        while l < r:
            if s[l] == "[":
                bal += 1
            elif bal:
                bal -= 1
            else:
                while s[r] == "]":
                    r -= 1
                r -= 1
                bal += 1
                ans += 1
            l += 1
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minSwaps"] * 3,
            "kwargs": [
                dict(s="][]["),
                dict(s="]]][[["),
                dict(s="[]"),
            ],
            "expected": [1, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
