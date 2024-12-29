import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        def diameter(edges: List[List[int]]) -> int:
            if not edges:
                return 0
            adj = defaultdict(set)
            for fr, to in edges:
                adj[fr].add(to)
                adj[to].add(fr)
            ends = deque(node for node, neibs in adj.items() if len(neibs) == 1)
            dia = defaultdict(int)
            while len(ends) > 1:
                node = ends.popleft()
                neib = adj[node].pop()
                adj[neib].remove(node)
                if len(adj[neib]) <= 1:
                    dia[neib] += dia[node] + 1
                    if len(adj[neib]) == 1:
                        ends.append(neib)
            return dia[ends.pop()]

        d1 = diameter(edges1)
        d2 = diameter(edges2)
        if d1 < d2:
            d1, d2 = d2, d1
        r11 = (d1 + 1) // 2
        r12 = d1 // 2
        r21 = (d2 + 1) // 2 + 1
        return r11 + max(r12, r21)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumDiameterAfterMerge"] * 3,
            "kwargs": [
                dict(edges1=[[0, 1]], edges2=[[0, 1]]),
                dict(edges1=[[0, 1], [0, 2], [0, 3]], edges2=[[0, 1]]),
                dict(
                    edges1=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
                    edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
                ),
            ],
            "expected": [3, 3, 5],
        },
    ]


if __name__ == "__main__":
    unittest.main()
