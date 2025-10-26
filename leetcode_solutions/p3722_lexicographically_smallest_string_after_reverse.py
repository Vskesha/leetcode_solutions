import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        min_string = s

        for k in range(1, n):
            reversed_first = s[:k][::-1] + s[k:]
            if reversed_first < min_string:
                min_string = reversed_first

            reversed_last = s[:-k] + s[-k:][::-1]
            if reversed_last < min_string:
                min_string = reversed_last

        return min(s[::-1], min_string)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lexSmallest"] * 3,
            "kwargs": [
                dict(s="dcab"),
                dict(s="abba"),
                dict(s="zxy"),
            ],
            "expected": ["acdb", "aabb", "xzy"],
        },
    ]


if __name__ == "__main__":
    unittest.main()
