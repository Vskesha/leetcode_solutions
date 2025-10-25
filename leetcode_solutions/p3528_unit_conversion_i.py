import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        lc = len(conversions)
        ans = [1] * (lc + 1)
        for fr, to, c in conversions:
            ans[to] = ans[fr] * c % mod
        return ans


class Solution2:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        lc = len(conversions)

        adj = defaultdict(list)
        for fr, to, conv in conversions:
            adj[fr].append((to, conv))

        ans = [1] * (lc + 1)
        bfs = deque()
        bfs.append((0, -1))
        while bfs:
            curr, par = bfs.popleft()
            for neib, conv in adj[curr]:
                if neib == par:
                    continue
                ans[neib] = ans[curr] * conv % mod
                bfs.append((neib, curr))

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["baseUnitConversions"] * 2,
            "kwargs": [
                dict(conversions=[[0, 1, 2], [1, 2, 3]]),
                dict(
                    conversions=[
                        [0, 1, 2],
                        [0, 2, 3],
                        [1, 3, 4],
                        [1, 4, 5],
                        [2, 5, 2],
                        [4, 6, 3],
                        [5, 7, 4],
                    ]
                ),
            ],
            "expected": [[1, 2, 6], [1, 2, 3, 8, 10, 6, 30, 24]],
        },
    ]


if __name__ == "__main__":
    unittest.main()
