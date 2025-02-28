import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {}

        def find(stone):
            if stone != root.get(stone, stone):
                root[stone] = find(root.get(stone, stone))
            return root.get(stone, stone)

        def union(stone1, stone2):
            root1 = find(stone1)
            root2 = find(stone2)
            if root1 != root2:
                root[root2] = root1
                return 1
            return 0

        ans = 0
        rows, cols = defaultdict(list), defaultdict(list)
        for x, y in stones:
            stone1 = (x, y)
            for stone2 in rows[x]:
                ans += union(stone1, stone2)
            for stone2 in cols[y]:
                ans += union(stone1, stone2)
            rows[x].append(stone1)
            cols[y].append(stone1)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["removeStones"] * 3,
            "kwargs": [
                dict(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]),
                dict(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]),
                dict(stones=[[0, 0]]),
            ],
            "expected": [5, 3, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
