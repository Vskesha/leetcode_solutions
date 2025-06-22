import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [s[i : i + k] for i in range(0, len(s), k)]
        ans[-1] += fill * (k - len(ans[-1]))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["divideString"] * 2,
            "kwargs": [
                dict(s="abcdefghi", k=3, fill="x"),
                dict(s="abcdefghij", k=3, fill="x"),
            ],
            "expected": [["abc", "def", "ghi"], ["abc", "def", "ghi", "jxx"]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
