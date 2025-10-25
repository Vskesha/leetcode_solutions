import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def matchPlayersAndTrainers(
        self, players: List[int], trainers: List[int]
    ) -> int:
        players.sort()
        trainers.sort()
        lt = len(trainers)
        ans = j = 0

        for player in players:
            while j < lt and trainers[j] < player:
                j += 1
            if j == lt:
                break
            ans += 1
            j += 1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["matchPlayersAndTrainers"] * 2,
            "kwargs": [
                dict(players=[4, 7, 9], trainers=[8, 2, 5, 8]),
                dict(players=[1, 1, 1], trainers=[10]),
            ],
            "expected": [2, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
