import unittest
from collections import defaultdict, deque
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        ans = 0
        for node in range(n):
            if node in seen:
                continue
            visited = {node}
            que = deque([node])
            while que:
                curr = que.popleft()
                for neib in adj[curr]:
                    if neib not in visited:
                        visited.add(neib)
                        que.append(neib)
            seen.update(visited)
            ln = len(visited) - 1
            ans += all(len(adj[c]) == ln for c in visited)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["countCompleteComponents"] * 2,
            "kwargs": [
                dict(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]),
                dict(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]),
            ],
            "expected": [3, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
