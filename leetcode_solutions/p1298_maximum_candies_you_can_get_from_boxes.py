import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        ans = 0
        closed = set()
        que = deque()

        for box in initialBoxes:
            if status[box]:
                que.append(box)
            else:
                closed.add(box)

        while que:
            curr = que.popleft()
            ans += candies[curr]

            for key in keys[curr]:
                if not status[key]:
                    if key in closed:
                        closed.remove(key)
                        que.append(key)
                    status[key] = 1

            for box in containedBoxes[curr]:
                if status[box]:
                    que.append(box)
                else:
                    closed.add(box)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxCandies"] * 2,
            "kwargs": [
                dict(
                    status=[1, 0, 1, 0],
                    candies=[7, 5, 4, 100],
                    keys=[[], [], [1], []],
                    containedBoxes=[[1, 2], [3], [], []],
                    initialBoxes=[0],
                ),
                dict(
                    status=[1, 0, 0, 0, 0, 0],
                    candies=[1, 1, 1, 1, 1, 1],
                    keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                    containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []],
                    initialBoxes=[0],
                ),
            ],
            "expected": [16, 6],
        },
    ]


if __name__ == "__main__":
    unittest.main()
