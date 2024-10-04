import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        chem = 0

        for i in range(len(skill) // 2):
            if skill[i] + skill[~i] != target:
                return -1
            chem += skill[i] * skill[~i]

        return chem


class Solution2:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        chem = 0

        for a, b in zip(skill[: len(skill) // 2], reversed(skill)):
            if a + b != target:
                return -1
            chem += a * b

        return chem


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["dividePlayers"] * 3,
            "kwargs": [
                dict(skill=[3, 2, 5, 1, 3, 4]),
                dict(skill=[3, 4]),
                dict(skill=[1, 1, 2, 3]),
            ],
            "expected": [22, 12, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
