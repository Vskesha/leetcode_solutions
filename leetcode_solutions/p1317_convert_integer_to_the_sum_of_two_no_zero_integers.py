import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if not ("0" in str(a) or "0" in str(b)):
                return [a, b]
        return [n, 0]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getNoZeroIntegers"] * 2,
            "kwargs": [
                dict(n=2),
                dict(n=11),
            ],
            "expected": [[1, 1], [2, 9]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
