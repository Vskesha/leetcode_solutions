import unittest
from bisect import bisect_left
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        lp = len(potions)
        return [
            lp - bisect_left(potions, (success - 1) // spell + 1)
            for spell in spells
        ]


class Solution2:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        result = []
        lp = len(potions)

        for spell in spells:
            min_potion = (success - 1) // spell + 1
            idx = bisect_left(potions, min_potion)
            result.append(lp - idx)

        return result


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["successfulPairs"] * 2,
            "kwargs": [
                dict(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7),
                dict(spells=[3, 1, 2], potions=[8, 5, 8], success=16),
            ],
            "expected": [[4, 0, 3], [2, 0, 2]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
