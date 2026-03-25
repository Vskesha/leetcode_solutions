import unittest
from itertools import accumulate

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def minimumChairs(self, s: str) -> int:
        return max(accumulate(1 if c == "E" else -1 for c in s))


class Solution2:
    def minimumChairs(self, s: str) -> int:
        ans = seats = 0
        for c in s:
            if c == "E":
                seats += 1
                if ans < seats:
                    ans = seats
            else:
                seats -= 1
        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumChairs"] * 3,
            "kwargs": [
                dict(s="EEEEEEE"),
                dict(s="ELELEEL"),
                dict(s="ELEELEELLL"),
            ],
            "expected": [7, 2, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
