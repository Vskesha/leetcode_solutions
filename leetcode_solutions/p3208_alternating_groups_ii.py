import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[: k - 1])
        prev = -1
        streak = 0
        ans = 0

        for curr in colors:
            if curr == prev:
                streak = 0
            streak += 1
            ans += streak >= k
            prev = curr

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfAlternatingGroups"] * 3,
            "kwargs": [
                dict(colors=[0, 1, 0, 1, 0], k=3),
                dict(colors=[0, 1, 0, 0, 1, 0, 1], k=6),
                dict(colors=[1, 1, 0, 1], k=4),
            ],
            "expected": [3, 2, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
