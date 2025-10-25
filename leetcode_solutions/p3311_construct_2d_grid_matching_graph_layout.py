import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def constructGridLayout(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        gr = [[] for _ in range(n)]
        for fr, to in edges:
            gr[fr].append(to)
            gr[to].append(fr)

        corner = min(range(n), key=lambda i: len(gr[i]))
        lc = len(gr[corner])
        row = [corner]
        seen = [0] * n
        seen[corner] = 1
        while len(row) < 2 or len(gr[row[-1]]) > lc:
            gr[row[-1]].sort(key=lambda i: len(gr[i]))
            for neib in gr[row[-1]]:
                if not seen[neib]:
                    row.append(neib)
                    seen[neib] = 1
                    break

        ans = [row]
        for _ in range(n // len(row) - 1):
            nrow = []
            for top in ans[-1]:
                for bot in gr[top]:
                    if not seen[bot]:
                        nrow.append(bot)
                        seen[bot] = 1
                        break
            ans.append(nrow)
        return ans


class Solution2:
    def constructGridLayout(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        graph = defaultdict(set)
        for fr, to in edges:
            graph[fr].add(to)
            graph[to].add(fr)

        corner = 0
        ml = 2 - (len(edges) == n - 1)
        for node, neibs in graph.items():
            if len(neibs) == ml:
                corner = node
                break

        if ml == 1:
            ans = [0] * n
            ans[0] = corner
            for i in range(1, n):
                corner = ans[i] = graph[corner].pop()
                graph[corner].remove(ans[i - 1])
            return [ans]

        ans = [[], []]
        ans[0].append(corner)
        right, bottom = graph[corner].pop(), graph[corner].pop()
        ans[0].append(right)
        ans[1].append(bottom)
        graph[right].remove(corner)
        graph[bottom].remove(corner)

        while True:
            top, left = ans[0][-1], ans[1][-1]
            common = (graph[top] & graph[left]).pop()
            ans[1].append(common)
            graph[common].remove(top)
            graph[top].remove(common)
            graph[common].remove(left)
            graph[left].remove(common)
            if graph[top]:
                right = graph[top].pop()
                ans[0].append(right)
                graph[right].remove(top)
            else:
                break

        while graph[ans[-1][0]]:
            prevrow = iter(ans[-1])
            top = next(prevrow)
            bottom = graph[top].pop()
            ans.append([bottom])
            graph[bottom].remove(top)
            for top in prevrow:
                left = ans[-1][-1]
                common = graph[top].pop()
                ans[-1].append(common)
                graph[common].remove(top)
                graph[common].remove(left)
                graph[left].remove(common)

        return ans


class Solution3:
    def constructGridLayout(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        deg = [len(row) for row in adj]
        root = deg.index(min(deg))
        path = [root]
        seen = [0] * n
        seen[root] = 1
        for node in path:
            if len(path) >= 2 and deg[path[-1]] == deg[root]:
                break
            adj[node].sort(key=deg.__getitem__)
            for nei in adj[node]:
                if not seen[nei] and deg[nei] <= deg[root] + 1:
                    path.append(nei)
                    seen[nei] = 1
                    break

        cols = len(path)
        rows = n // cols
        ans = [[0] * cols for _ in range(rows)]
        ans[0] = path
        for r in range(1, rows):
            for c in range(cols):
                for nei in adj[ans[r - 1][c]]:
                    if not seen[nei]:
                        ans[r][c] = nei
                        seen[nei] = 1
                        break

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["constructGridLayout"] * 3,
            "kwargs": [
                dict(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]]),
                dict(n=5, edges=[[0, 1], [1, 3], [2, 3], [2, 4]]),
                dict(
                    n=9,
                    edges=[
                        [0, 1],
                        [0, 4],
                        [0, 5],
                        [1, 7],
                        [2, 3],
                        [2, 4],
                        [2, 5],
                        [3, 6],
                        [4, 6],
                        [4, 7],
                        [6, 8],
                        [7, 8],
                    ],
                ),
            ],
            "expected": [
                [[3, 1], [2, 0]],
                [[4, 2, 3, 1, 0]],
                [[8, 6, 3], [7, 4, 2], [1, 0, 5]],
            ],
            "assert_methods": ["assertValidLayout"] * 3,
        },
    ]

    def assertValidLayout(
        self, layout: List[List[int]], expected: List[List[int]]
    ):
        valid = False
        for i in range(4):
            if valid:
                break
            valid = self.is_equal_matrices(layout, expected)
            expected = self.turnRight(expected)
        if not valid:
            expected = self.mirrored(expected)
        for i in range(4):
            if valid:
                break
            valid = self.is_equal_matrices(layout, expected)
            expected = self.turnRight(expected)
        self.assertTrue(valid)

    def is_equal_matrices(
        self, list1: List[List[int]], list2: List[List[int]]
    ) -> bool:
        for a, b in zip(list1, list2):
            if a != b:
                return False
        return True

    def turnRight(self, A: List[List[int]]) -> List[List[int]]:
        return [list(t) for t in zip(*A[::-1])]

    def mirrored(self, A: List[List[int]]) -> List[List[int]]:
        return [row[::-1] for row in A]


if __name__ == "__main__":
    unittest.main()
