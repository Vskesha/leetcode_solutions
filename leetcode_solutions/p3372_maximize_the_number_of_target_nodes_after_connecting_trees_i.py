import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        gr1 = [[] for _ in range(n)]
        gr2 = [[] for _ in range(m)]
        for a, b in edges1:
            gr1[a].append(b)
            gr1[b].append(a)
        for a, b in edges2:
            gr2[a].append(b)
            gr2[b].append(a)

        def dfs(i, par, gr, k):
            if not k:
                return 1
            ans = sum(dfs(ni, i, gr, k - 1) for ni in gr[i] if ni != par)
            return ans + 1

        max2 = max(dfs(i, -1, gr2, k - 1) for i in range(m))
        ans = [max2] * n
        for i in range(n):
            ans[i] += dfs(i, -1, gr1, k)
        return ans


class Solution2:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        def dfs(i, par, k):
            if not k:
                return 1
            return 1 + sum(dfs(ni, i, k - 1) for ni in gr[i] if ni != par)

        if not k:
            return [1] * (len(edges1) + 1)
        m = len(edges2) + 1
        gr = [[] for _ in range(m)]
        for a, b in edges2:
            gr[a].append(b)
            gr[b].append(a)
        max2 = max(dfs(i, -1, k - 1) for i in range(m))

        n = len(edges1) + 1
        gr = [[] for _ in range(n)]
        for a, b in edges1:
            gr[a].append(b)
            gr[b].append(a)

        return [dfs(i, -1, k) + max2 for i in range(n)]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTargetNodes"] * 2,
            "kwargs": [
                dict(
                    edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                    edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
                    k=2,
                ),
                dict(
                    edges1=[[0, 1], [0, 2], [0, 3], [0, 4]],
                    edges2=[[0, 1], [1, 2], [2, 3]],
                    k=1,
                ),
            ],
            "expected": [[9, 7, 9, 8, 8], [6, 3, 3, 3, 3]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
