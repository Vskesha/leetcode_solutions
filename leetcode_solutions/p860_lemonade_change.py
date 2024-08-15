from typing import List
from collections import Counter
import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            elif tens:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            if fives < 0:
                return False

        return True


class Solution1:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif not fives:
                return False
            elif bill == 10:
                fives -= 1
                tens += 1
            elif tens:
                fives -= 1
                tens -= 1
            else:
                if fives < 3:
                    return False
                fives -= 3

        return True


class Solution2:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = Counter()

        for bill in bills:
            if bill == 20:
                if change[10] and change[5]:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
            elif bill == 10:
                if change[5]:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            else:
                change[5] += 1

        return True


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lemonadeChange"] * 3,
            "kwargs": [
                dict(bills=[5, 5, 5, 10, 20]),
                dict(bills=[5, 5, 10, 10, 20]),
                dict(
                    bills=[
                        5,
                        5,
                        10,
                        20,
                        5,
                        5,
                        5,
                        5,
                        5,
                        5,
                        5,
                        5,
                        5,
                        10,
                        5,
                        5,
                        20,
                        5,
                        20,
                        5,
                    ]
                ),
            ],
            "expected": [True, False, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()
