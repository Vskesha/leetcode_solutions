import unittest
from collections import defaultdict
from heapq import nlargest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        for i, j, w in edges:
            graph[i].append((j, w))
            graph[j].append((i, w))

        def dfs(i, par):
            res = 0
            diff = []
            for j, w in graph[i]:
                if j == par:
                    continue
                v1, v2 = dfs(j, i)
                res += v2
                diff.append(max(0, v1 + w - v2))
            r1 = res + sum(nlargest(k - 1, diff))
            r2 = res + sum(nlargest(k, diff))
            return r1, r2

        return dfs(0, -1)[1]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maximizeSumOfWeights"] * 2,
            "kwargs": [
                dict(edges=[[0, 1, 4], [0, 2, 2], [2, 3, 12], [2, 4, 6]], k=2),
                dict(
                    edges=[
                        [0, 1, 5],
                        [1, 2, 10],
                        [0, 3, 15],
                        [3, 4, 20],
                        [3, 5, 5],
                        [0, 6, 10],
                    ],
                    k=3,
                ),
            ],
            "expected": [22, 65],
        },
    ]


if __name__ == "__main__":
    unittest.main()
