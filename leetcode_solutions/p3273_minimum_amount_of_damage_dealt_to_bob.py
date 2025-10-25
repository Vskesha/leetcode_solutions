import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minDamage(
        self, power: int, damage: List[int], health: List[int]
    ) -> int:
        n = len(damage)

        times = [(h - 1) // power + 1 for h in health]
        dpt = [(d / t, d, t) for d, t in zip(damage, times)]
        dpt.sort(reverse=True)

        td = sum(damage)
        ans = 0

        for _, d, t in dpt:
            ans += td * t
            td -= d

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minDamage"] * 3,
            "kwargs": [
                dict(power=4, damage=[1, 2, 3, 4], health=[4, 5, 6, 8]),
                dict(power=1, damage=[1, 1, 1, 1], health=[1, 2, 3, 4]),
                dict(power=8, damage=[40], health=[59]),
            ],
            "expected": [39, 20, 320],
        },
    ]


if __name__ == "__main__":
    unittest.main()
