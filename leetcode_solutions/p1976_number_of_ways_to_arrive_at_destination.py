import unittest
from heapq import heappop, heappush
from math import inf
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7

        adj = [[] for _ in range(n)]
        for a, b, t in roads:
            adj[a].append((b, t))
            adj[b].append((a, t))

        time = [inf] * n
        ways = [0] * n
        time[0] = 0
        ways[0] = 1
        n -= 1

        heap = [(0, 0)]
        while heap:
            ct, curr = heappop(heap)
            if curr == n:
                return ways[n]
            for neib, tt in adj[curr]:
                tt += ct
                if tt < time[neib]:
                    heappush(heap, (tt, neib))
                    time[neib] = tt
                    ways[neib] = ways[curr]
                elif tt == time[neib]:
                    ways[neib] = (ways[neib] + ways[curr]) % mod

        return ways[n]


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countPaths"] * 2,
            "kwargs": [
                dict(
                    n=7,
                    roads=[
                        [0, 6, 7],
                        [0, 1, 2],
                        [1, 2, 3],
                        [1, 3, 3],
                        [6, 3, 3],
                        [3, 5, 1],
                        [6, 5, 1],
                        [2, 5, 1],
                        [0, 4, 5],
                        [4, 6, 2],
                    ],
                ),
                dict(n=2, roads=[[1, 0, 10]]),
            ],
            "expected": [4, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
