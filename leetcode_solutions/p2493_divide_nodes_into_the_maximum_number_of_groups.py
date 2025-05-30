import unittest
from collections import defaultdict, deque
from typing import List

from _test_meta import TestMeta


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        assigned = set()
        ans = 0
        for i in range(1, n + 1):
            if i not in assigned:
                group = {i: 0}
                bfs = deque([i])
                while bfs:
                    curr = bfs.popleft()
                    for neib in adj[curr]:
                        if neib not in group:
                            group[neib] = group[curr] + 1
                            bfs.append(neib)
                        elif abs(group[neib] - group[curr]) != 1:
                            return -1
                
                mgr = 0
                for node in group:
                    visited = {node}
                    bfs = deque([node])
                    gr = 0
                    while bfs:
                        gr += 1
                        for _ in range(len(bfs)):
                            curr = bfs.popleft()
                            for neib in adj[curr]:
                                if neib not in visited:
                                    visited.add(neib)
                                    bfs.append(neib)
                    mgr = max(mgr, gr)
                ans += mgr
                assigned.update(group)
        
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["magnificentSets"] * 3,
            "kwargs": [
                dict(n=6, edges=[[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]),
                dict(n=3, edges=[[1, 2], [2, 3], [3, 1]]),
                dict(n=26, edges=[[9,16],[8,3],[20,21],[12,16],[14,3],[7,21],[22,3],[22,18],[11,16],[25,4],[2,4],[14,21],[23,3],[17,3],[2,16],[24,16],[13,4],[10,21],[7,4],[9,18],[14,18],[14,4],[14,16],[1,3],[25,18],[17,4],[1,16],[23,4],[2,21],[5,16],[24,18],[20,18],[19,16],[24,21],[9,3],[24,3],[19,18],[25,16],[19,21],[6,3],[26,18],[5,21],[20,16],[2,3],[10,18],[26,16],[8,4],[11,21],[23,16],[13,16],[25,3],[7,18],[19,3],[20,4],[26,3],[23,18],[15,18],[17,18],[10,16],[26,21],[23,21],[7,16],[8,18],[10,4],[24,4],[7,3],[11,18],[9,4],[26,4],[13,21],[22,16],[22,21],[20,3],[6,18],[9,21],[10,3],[22,4],[1,18],[25,21],[11,4],[1,21],[15,3],[1,4],[15,16],[2,18],[13,3],[8,21],[13,18],[11,3],[15,21],[8,16],[17,16],[15,4],[12,3],[6,4],[17,21],[5,18],[6,16],[6,21],[12,4],[19,4],[5,3],[12,21],[5,4]]),
            ],
            "expected": [4, -1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
