import unittest
from typing import List

from _test_meta import TestMeta


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find(node: int) -> int:
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]

        root = list(range(len(edges) + 1))
        for edge in edges:
            root1 = find(edge[0])
            root2 = find(edge[1])
            if root1 == root2:
                return edge
            else:
                root[root2] = root1
        return [-1, -1]


class DisjointSet:
    def __init__(self, n: int):
        self.root = list(range(n))

    def find(self, node: int):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, edge: List[int]) -> bool:
        root1 = self.find(edge[0])
        root2 = self.find(edge[1])
        if root1 == root2:
            return True
        else:
            self.root[root2] = root1
            return False


class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet(len(edges) + 1)
        for e in edges:
            if ds.union(e):
                return e
        return [-1, -1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findRedundantConnection"] * 2,
            "kwargs": [
                dict(edges=[[1, 2], [1, 3], [2, 3]]),
                dict(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]),
            ],
            "expected": [[2, 3], [1, 4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
