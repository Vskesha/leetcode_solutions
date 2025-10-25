import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximumEnergy"] * 2,
            "kwargs": [
                dict(energy=[5, 2, -10, -5, 1], k=3),
                dict(energy=[-2, -3, -1], k=2),
            ],
            "expected": [3, -1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
