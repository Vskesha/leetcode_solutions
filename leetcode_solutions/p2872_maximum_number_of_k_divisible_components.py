import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        ts = sum(values)
        if ts % k:
            return 0

        adj = defaultdict(set)
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        ends = deque()
        for node, neibs in adj.items():
            if len(neibs) == 1:
                ends.append(node)

        ans = 1
        while len(ends) > 1:
            node = ends.popleft()
            neib = adj[node].pop()
            adj[neib].remove(node)
            if len(adj[neib]) == 1:
                ends.append(neib)
            if values[node] % k:
                values[neib] += values[node]
            else:
                ans += 1
            values[node] = 0

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxKDivisibleComponents"] * 2,
            "kwargs": [
                dict(
                    n=5,
                    edges=[[0, 2], [1, 2], [1, 3], [2, 4]],
                    values=[1, 8, 1, 4, 4],
                    k=6,
                ),
                dict(
                    n=7,
                    edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
                    values=[3, 0, 6, 1, 5, 2, 1],
                    k=3,
                ),
            ],
            "expected": [2, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
