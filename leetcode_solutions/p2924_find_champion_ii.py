import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        income = [0] * n
        for fr, to in edges:
            income[to] += 1
        champs = [i for i in range(n) if income[i] == 0]
        return champs[0] if len(champs) == 1 else -1


class Solution2:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set(range(n))
        for _, t in edges:
            teams.discard(t)
        return teams.pop() if len(teams) == 1 else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findChampion"] * 2,
            "kwargs": [
                dict(n=3, edges=[[0, 1], [1, 2]]),
                dict(n=4, edges=[[0, 2], [1, 3], [1, 2]]),
            ],
            "expected": [0, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
