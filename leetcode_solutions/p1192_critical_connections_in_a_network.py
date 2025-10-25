import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        def dfs(node, time, parent):
            low[node] = time
            for neib in graph[node]:
                if neib != parent:
                    if not low[neib]:
                        dfs(neib, time + 1, node)
                        if low[neib] > time:
                            critical.append([node, neib])
                    low[node] = min(low[node], low[neib])

        graph = defaultdict(list)
        [
            (graph[fr].append(to), graph[to].append(fr))
            for fr, to in connections
        ]
        low, critical = [0] * n, []
        dfs(0, 1, -1)
        return critical


class Solution1:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        def dfs(node, time, parent):
            low[node] = time
            for neib in graph[node]:
                if neib != parent:
                    if not low[neib]:
                        dfs(neib, time + 1, node)
                        if low[neib] > time:
                            critical.append([node, neib])
                    low[node] = min(low[node], low[neib])

        graph = defaultdict(list)
        for fr, to in connections:
            graph[fr].append(to)
            graph[to].append(fr)
        low = [0] * n
        critical = []
        dfs(0, 1, -1)
        return critical


class Solution2:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        disc = [-1] * n
        low = [-1] * n
        criticalConnections = []
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(vertex, parent=-1, time=0):
            low[vertex] = disc[vertex] = time
            for neighbour in graph[vertex]:
                if disc[neighbour] == -1:
                    dfs(neighbour, vertex, time + 1)
                    if low[neighbour] > disc[vertex]:
                        criticalConnections.append([vertex, neighbour])
                    low[vertex] = min(low[vertex], low[neighbour])
                elif parent != neighbour:
                    low[vertex] = min(low[vertex], disc[neighbour])
            return

        dfs(connections[0][0])

        return criticalConnections


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["criticalConnections"] * 2,
            "kwargs": [
                dict(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]),
                dict(n=2, connections=[[0, 1]]),
            ],
            "expected": [[[1, 3]], [[0, 1]]],
            "assert_methods": ["assertSameConnections"] * 2,
        },
    ]

    def assertSameConnections(self, actual, expected):
        actual_set = set(tuple(sorted(conn)) for conn in actual)
        expected_set = set(tuple(sorted(conn)) for conn in expected)
        self.assertSetEqual(actual_set, expected_set)


if __name__ == "__main__":
    unittest.main()
