import unittest
from collections import deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        m = len(edges2) + 1
        graph = [[] for _ in range(m)]
        for a, b in edges2:
            graph[a].append(b)
            graph[b].append(a)

        o2 = 0
        que = deque([(0, -1, 1)])
        while que:
            cur, par, odd = que.popleft()
            o2 += odd
            odd = 1 - odd
            for ch in graph[cur]:
                if ch != par:
                    que.append((ch, cur, odd))
        mx = max(o2, m - o2)

        n = len(edges1) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges1:
            graph[a].append(b)
            graph[b].append(a)

        odds = set()
        que = deque([(0, -1, 1)])
        while que:
            cur, par, odd = que.popleft()
            if odd:
                odds.add(cur)
            odd = 1 - odd
            for ch in graph[cur]:
                if ch != par:
                    que.append((ch, cur, odd))
        o1 = len(odds)
        e1 = n - o1

        ans = [mx] * n
        for i in range(n):
            ans[i] += o1 if i in odds else e1

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTargetNodes"] * 2,
            "kwargs": [
                dict(
                    edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                    edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
                ),
                dict(
                    edges1=[[0, 1], [0, 2], [0, 3], [0, 4]],
                    edges2=[[0, 1], [1, 2], [2, 3]],
                ),
            ],
            "expected": [[8, 7, 7, 8, 8], [3, 6, 6, 6, 6]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
