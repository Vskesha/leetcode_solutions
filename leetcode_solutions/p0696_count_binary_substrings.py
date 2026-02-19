import unittest
from itertools import groupby, pairwise

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = 0
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans += min(curr, prev)
                prev = curr
                curr = 1

        ans += min(curr, prev)
        return ans


class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(gr)) for _, gr in groupby(s)]
        return sum(min(a, b) for a, b in pairwise(groups))


class Solution3:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(
            min(a, b)
            for a, b in pairwise(len(list(gr)) for _, gr in groupby(s))
        )


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countBinarySubstrings"] * 2,
            "kwargs": [
                dict(s="00110011"),
                dict(s="10101"),
            ],
            "expected": [6, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
