import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        lp = len(parent)
        adj = defaultdict(list)
        for i in range(1, lp):
            adj[parent[i]].append(i)

        np = parent.copy()
        seen = defaultdict(list)

        def change(pi):
            ch = s[pi]
            seen[ch].append(pi)
            for chi in adj[pi]:
                change(chi)
            seen[ch].pop()
            if seen[ch]:
                np[pi] = seen[ch][-1]

        change(0)
        adj = defaultdict(list)
        for i in range(1, lp):
            adj[np[i]].append(i)

        ans = [1] * lp

        def dfs(pi):
            for chi in adj[pi]:
                dfs(chi)
                ans[pi] += ans[chi]

        dfs(0)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findSubtreeSizes"] * 2,
            "kwargs": [
                dict(parent=[-1, 0, 0, 1, 1, 1], s="abaabc"),
                dict(parent=[-1, 0, 4, 0, 1], s="abbba"),
            ],
            "expected": [
                [6, 3, 1, 1, 1, 1],
                [5, 2, 1, 1, 1],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
