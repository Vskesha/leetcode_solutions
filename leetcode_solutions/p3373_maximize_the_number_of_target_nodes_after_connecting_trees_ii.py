import unittest
from collections import Counter, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def build(edges):
            adj = [set() for _ in range(len(edges) + 1)]
            for a, b in edges:
                adj[a].add(b)
                adj[b].add(a)
            pairs = [0] * len(adj)
            bfs = deque([(0, 0)])
            while bfs:
                curr, p = bfs.popleft()
                pairs[curr] = p
                for neib in adj[curr]:
                    adj[neib].remove(curr)
                    bfs.append((neib, 1 - p))
            return pairs

        pairs = build(edges1)
        cnt = Counter(pairs)
        ad = max(Counter(build(edges2)).values())

        return [cnt[p] + ad for p in pairs]


class Solution2:
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


class Solution3:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def build(edges):
            adj = [set() for _ in range(len(edges) + 1)]
            for a, b in edges:
                adj[a].add(b)
                adj[b].add(a)
            return adj

        def fill(adj):
            pairs = [0] * len(adj)
            bfs = deque([(0, 0)])
            while bfs:
                curr, p = bfs.popleft()
                pairs[curr] = p
                for neib in adj[curr]:
                    adj[neib].remove(curr)
                    bfs.append((neib, 1 - p))
            return pairs

        adj1 = build(edges1)
        adj2 = build(edges2)
        pairs1 = fill(adj1)
        pairs2 = fill(adj2)
        ev1, od1 = pairs1.count(0), pairs1.count(1)
        ev2, od2 = pairs2.count(0), pairs2.count(1)
        ad = max(ev2, od2)

        ans = [(od1 if p else ev1) + ad for i, p in enumerate(pairs1)]
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTargetNodes"] * 3,
            "kwargs": [
                dict(
                    edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                    edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
                ),
                dict(
                    edges1=[[0, 1], [0, 2], [0, 3], [0, 4]],
                    edges2=[[0, 1], [1, 2], [2, 3]],
                ),
                dict(
                    edges1=[[0, 1]],
                    edges2=[[0, 1], [1, 2]],
                ),
            ],
            "expected": [[8, 7, 7, 8, 8], [3, 6, 6, 6, 6], [3, 3]],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
