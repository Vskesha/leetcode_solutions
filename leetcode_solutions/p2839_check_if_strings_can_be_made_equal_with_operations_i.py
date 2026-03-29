import unittest
from collections import Counter

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(
            s1[1::2]
        ) == Counter(s2[1::2])


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["canBeEqual"] * 2,
            "kwargs": [
                dict(s1="abcd", s2="cdab"),
                dict(s1="abcd", s2="dacb"),
            ],
            "expected": [True, False],
        },
    ]


if __name__ == "__main__":
    unittest.main()
