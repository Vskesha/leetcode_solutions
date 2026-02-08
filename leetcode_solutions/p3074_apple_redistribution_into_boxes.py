import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples_to_distribute = sum(apple)
        capacity.sort(reverse=True)

        for i, box in enumerate(capacity, 1):
            apples_to_distribute -= box
            if apples_to_distribute <= 0:
                return i

        return -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumBoxes"] * 2,
            "kwargs": [
                dict(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]),
                dict(apple=[5, 5, 5], capacity=[2, 4, 2, 7]),
            ],
            "expected": [2, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
