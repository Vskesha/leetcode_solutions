import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        energyDrinkA[1] += energyDrinkA[0]
        energyDrinkB[1] += energyDrinkB[0]

        for i in range(2, len(energyDrinkA)):
            energyDrinkA[i] += max(energyDrinkA[i - 1], energyDrinkB[i - 2])
            energyDrinkB[i] += max(energyDrinkB[i - 1], energyDrinkA[i - 2])

        return max(energyDrinkA[-1], energyDrinkB[-1])


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxEnergyBoost"] * 2,
            "kwargs": [
                dict(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]),
                dict(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]),
            ],
            "expected": [5, 7],
        },
    ]


if __name__ == '__main__':
    unittest.main()