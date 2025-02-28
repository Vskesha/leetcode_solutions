import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rgraph = [[] for _ in range(n)]
        income = [0] * n
        for i, adj in enumerate(graph):
            for j in adj:
                rgraph[j].append(i)
                income[i] += 1

        ts = [i for i in range(n) if not income[i]]
        i = 0
        while i < len(ts):
            for neib in rgraph[ts[i]]:
                income[neib] -= 1
                if not income[neib]:
                    ts.append(neib)
            i += 1

        ts.sort()
        return ts


class Solution2:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        cycled = set()
        ans = set()

        def lead_to_cycle(node: int, track: set):
            if node in ans or node in cycled:
                return
            for neib in graph[node]:
                if neib in track:
                    cycled.add(node)
                    return
                track.add(neib)
                lead_to_cycle(neib, track)
                if neib in cycled:
                    cycled.add(node)
                    return
                track.remove(neib)
            ans.add(node)
            return

        for i in range(len(graph)):
            lead_to_cycle(i, {i})
        return sorted(ans)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["eventualSafeNodes"] * 2,
            "kwargs": [
                dict(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]),
                dict(graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]),
            ],
            "expected": [[2, 4, 5, 6], [4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
