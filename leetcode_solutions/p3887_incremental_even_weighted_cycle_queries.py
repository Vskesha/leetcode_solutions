import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        root = list(range(n))
        colors = [0] * n
        adj = [[] for _ in range(n)]
        root_size = [1] * n

        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]

        def change_color(node, adj, visited):
            bfs = deque([node])
            visited.add(node)
            while bfs:
                node = bfs.popleft()
                colors[node] = 1 - colors[node]
                for neib in adj[node]:
                    if neib not in visited:
                        bfs.append(neib)
                        visited.add(neib)

        ans = 0
        for u, v, w in edges:
            rootu, rootv = find(u), find(v)
            if rootu != rootv:
                ans += 1
                root[rootv] = rootu
                adj[u].append(v)
                adj[v].append(u)
                if w == int(colors[u] == colors[v]):
                    if root_size[rootu] > root_size[rootv]:
                        change_color(v, adj, {u})
                    else:
                        change_color(u, adj, {v})
                root_size[rootu] += root_size[rootv]
                root_size[rootv] = 0
            elif w != int(colors[u] == colors[v]):
                ans += 1
                adj[u].append(v)
                adj[v].append(u)

        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numberOfEdgesAdded"] * 2,
            "kwargs": [
                dict(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 1]]),
                dict(n=3, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 0]]),
            ],
            "expected": [2, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
