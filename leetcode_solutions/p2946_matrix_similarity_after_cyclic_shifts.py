import unittest
from itertools import cycle
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n

        for ki, row in zip(cycle((k, n - k)), mat):
            if row != row[ki:] + row[:ki]:
                return False

        return True


# fmt: off
class Solution2:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(row == row[ki:] + row[:ki] for ki, row in zip(cycle((k % len(mat[0]), len(mat[0]) - k % len(mat[0]))), mat))  # noqa: E501
# fmt: on


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["areSimilar"] * 3,
            "kwargs": [
                dict(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4),
                dict(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2),
                dict(mat=[[2, 2], [2, 2]], k=3),
            ],
            "expected": [False, True, True],
        },
    ]


if __name__ == "__main__":
    unittest.main()
