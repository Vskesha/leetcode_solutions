import unittest
from collections import defaultdict
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        ln = len(nums)

        adj = defaultdict(set)
        for fr, to in edges:
            adj[fr].add(to)
            adj[to].add(fr)

        parents = [set() for _ in range(ln)]
        xors = nums.copy()

        def dfs(node: int):
            for neib in adj[node]:
                adj[neib].remove(node)
                parents[neib] = parents[node] | {node}
                dfs(neib)
                xors[node] ^= xors[neib]

        dfs(0)
        ans = inf

        for node2 in range(2, ln):
            for node1 in range(1, node2):
                x1 = xors[node1]
                x2 = xors[node2]

                if node1 in parents[node2]:
                    x1 = xors[node1] ^ xors[node2]
                elif node2 in parents[node1]:
                    x2 = xors[node2] ^ x1

                x3 = xors[0] ^ x1 ^ x2

                res = max(x1, x2, x3) - min(x1, x2, x3)
                if res < ans:
                    ans = res
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumScore"] * 2,
            "kwargs": [
                dict(
                    nums=[1, 5, 5, 4, 11],
                    edges=[[0, 1], [1, 2], [1, 3], [3, 4]]
                ),
                dict(
                    nums=[5, 5, 2, 4, 4, 2],
                    edges=[[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]],
                ),
            ],
            "expected": [9, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
