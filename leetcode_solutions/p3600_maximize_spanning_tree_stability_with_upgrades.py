import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        root = list(range(n))
        groups = n

        def find(node: int) -> int:
            if root[node] != node:
                root[node] = find(root[node])
            return root[node]

        optional = []
        ans = inf

        for u, v, s, m in edges:
            if m:
                root1 = find(u)
                root2 = find(v)
                if root1 == root2:
                    return -1
                root[root2] = root1
                groups -= 1
                if s < ans:
                    ans = s
            else:
                heappush(optional, (-s, u, v))

        if groups == 1:
            return ans

        strengths = []
        while optional:
            s, u, v = heappop(optional)
            root1 = find(u)
            root2 = find(v)
            if root1 == root2:
                continue
            root[root2] = root1
            groups -= 1
            strengths.append(-s)
            if groups == 1:
                break

        if groups > 1:
            return -1

        ans = min(ans, strengths[-1] * 2)
        if len(strengths) > k and strengths[-1 - k] < ans:
            return strengths[-1 - k]
        return ans


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.groops = n

    def find(self, node: int) -> int:
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.groops -= 1

    def connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)

    def all_connected(self) -> bool:
        return self.groops == 1


class Solution2:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ds = DisjointSet(n)
        optional = []
        ans = inf

        for u, v, s, m in edges:
            if m == 1:
                if ds.connected(u, v):
                    return -1
                ds.union(u, v)
                ans = min(ans, s)
            else:
                heappush(optional, (-s, u, v))

        if ds.all_connected():
            return ans

        strengths = []

        while optional:
            s, u, v = heappop(optional)
            if ds.connected(u, v):
                continue
            ds.union(u, v)
            strengths.append(-s)
            if ds.all_connected():
                break

        if not ds.all_connected():
            return -1

        ans = min(ans, strengths[-1] * 2)
        if len(strengths) > k:
            ans = min(ans, strengths[-1 - k])

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxStability"] * 3,
            "kwargs": [
                dict(
                    n=3,
                    edges=[[0, 1, 2, 1], [1, 2, 3, 0]],
                    k=1,
                ),
                dict(
                    n=3,
                    edges=[[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]],
                    k=2,
                ),
                dict(
                    n=3,
                    edges=[[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]],
                    k=0,
                ),
            ],
            "expected": [
                2,
                6,
                -1,
            ],
        },
    ]


if __name__ == "__main__":
    unittest.main()
