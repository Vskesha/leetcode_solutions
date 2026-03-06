import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return (i := s.find("0")) == -1 or "1" not in s[i:]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["checkOnesSegment"] * 2,
            "kwargs": [
                dict(s="1001"),
                dict(s="110"),
            ],
            "expected": [False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()
