import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def del_parents(node):
            for neib in adj[node]:
                adj[neib].remove(node)
                del_parents(neib)

        del_parents(0)

        def find_bob_path(node: int, path: List[int]) -> bool:
            path.append(node)
            if node == bob:
                return True
            for neib in adj[node]:
                if find_bob_path(neib, path):
                    return True
            path.pop()
            return False

        bob_path = []
        find_bob_path(0, bob_path)
        lbp = len(bob_path)

        for i in range(lbp - 1, (lbp - 1) // 2, -1):
            amount[bob_path[i]] = 0
        if lbp % 2:
            amount[bob_path[lbp // 2]] //= 2

        def max_amount(node: int) -> int:
            mx = max((max_amount(neib) for neib in adj[node]), default=0)
            return mx + amount[node]

        ans = max_amount(0)
        return ans


class Solution2:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def find_bob_path(node: int, par: int, path: List[int]) -> bool:
            path.append(node)
            if node == bob:
                return True
            for neib in adj[node]:
                if neib != par:
                    if find_bob_path(neib, node, path):
                        return True
            path.pop()
            return False

        bob_path = []
        find_bob_path(0, -1, bob_path)
        lbp = len(bob_path)

        for i in range(lbp - 1, (lbp - 1) // 2, -1):
            amount[bob_path[i]] = 0
        if lbp % 2:
            amount[bob_path[lbp // 2]] //= 2

        def max_amount(node: int, par: int) -> int:
            mx = max((max_amount(neib, node) for neib in adj[node] if neib != par), default=0)
            return mx + amount[node]

        ans = max_amount(0, -1)
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["mostProfitablePath"] * 2,
            "kwargs": [
                dict(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6]),
                dict(edges=[[0, 1]], bob=1, amount=[-7280, 2350]),
            ],
            "expected": [6, -7280],
        },
    ]


if __name__ == "__main__":
    unittest.main()
