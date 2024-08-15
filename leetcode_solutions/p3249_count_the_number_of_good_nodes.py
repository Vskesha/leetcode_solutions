import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for fr, to in edges:
            adj[fr].append(to)
            adj[to].append(fr)

        def dfs(node, parent):
            sizes = [dfs(neib, node) for neib in adj[node] if neib != parent]
            if not sizes or len(set(sizes)) == 1:
                self.ans += 1
            return sum(sizes) + 1

        self.ans = 0
        dfs(0, 0)

        return self.ans


class Solution1:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for fr, to in edges:
            adj[fr].append(to)
            adj[to].append(fr)

        def dfs(node, parent) -> tuple[int, int]:
            sizes = []
            good_nodes = 0
            for neib in adj[node]:
                if neib != parent:
                    gn, sz = dfs(neib, node)
                    sizes.append(sz)
                    good_nodes += gn
            if not sizes or len(set(sizes)) == 1:
                good_nodes += 1
            return good_nodes, sum(sizes) + 1

        return dfs(0, 0)[0]


class Solution2:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [set() for _ in range(n)]

        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        self.ans = 0

        def dfs(node, par) -> int:
            adj[node].discard(par)
            sizes = [dfs(neib, node) for neib in adj[node]]
            if len(set(sizes)) in (0, 1):
                self.ans += 1
            return sum(sizes) + 1

        dfs(0, 0)
        return self.ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countGoodNodes"] * 3,
            "kwargs": [
                dict(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]),
                dict(
                    edges=[
                        [0, 1],
                        [1, 2],
                        [2, 3],
                        [3, 4],
                        [0, 5],
                        [1, 6],
                        [2, 7],
                        [3, 8],
                    ]
                ),
                dict(
                    edges=[
                        [0, 1],
                        [1, 2],
                        [1, 3],
                        [1, 4],
                        [0, 5],
                        [5, 6],
                        [6, 7],
                        [7, 8],
                        [0, 9],
                        [9, 10],
                        [9, 12],
                        [10, 11],
                    ]
                ),
            ],
            "expected": [7, 6, 12],
        },
    ]


if __name__ == "__main__":
    unittest.main()
