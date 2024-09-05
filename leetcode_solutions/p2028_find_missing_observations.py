import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        left = mean * (len(rolls) + n) - sum(rolls)
        if left < n or left > n * 6:
            return []
        d, k = divmod(left, n)
        return [d + (i < k) for i in range(n)]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["missingRolls"] * 3,
            "kwargs": [
                dict(rolls = [3,2,4,3], mean = 4, n = 2),
                dict(rolls = [1,5,6], mean = 3, n = 4),
                dict(rolls = [1,2,3,4], mean = 6, n = 4),
            ],
            "expected": [[6,6], [2,3,2,2], []],
            "assert_methods": ["assertCorrectMissingRolls"] * 3,
        },
    ]

    def assertCorrectMissingRolls(self, result, expected):
        self.assertEqual(len(result), len(expected))
        self.assertEqual(sum(result), sum(expected))


if __name__ == '__main__':
    unittest.main()
