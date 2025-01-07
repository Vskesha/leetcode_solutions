import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = moves = 0
        ans = [0] * len(boxes)

        for i, b in enumerate(boxes):
            moves += balls
            ans[i] = moves
            balls += int(b)

        balls = moves = 0

        for i in range(len(boxes) - 1, -1, -1):
            moves += balls
            ans[i] += moves
            balls += int(boxes[i])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minOperations"] * 2,
            "kwargs": [
                dict(boxes="110"),
                dict(boxes="001011"),
            ],
            "expected": [[1, 1, 3], [11, 8, 5, 4, 3, 4]],
        },
    ]


if __name__ == "__main__":
    unittest.main()
