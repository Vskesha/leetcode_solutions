import unittest
from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        paths = list(range(n))
        adj = [[] for _ in range(n)]
        for node in range(n - 1):
            adj[node].append(node + 1)

        ans = []
        for fr, to in queries:
            adj[fr].append(to)
            if paths[to] > paths[fr] + 1:
                paths[to] = paths[fr] + 1
                q = deque([to])
                while q:
                    node = q.popleft()
                    for neib in adj[node]:
                        if paths[neib] > paths[node] + 1:
                            paths[neib] = paths[node] + 1
                            q.append(neib)
            ans.append(paths[-1])

        return ans


class Solution2:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        paths = list(range(n))
        adj = [[] for _ in range(n)]
        for node in range(1, n):
            adj[node].append(node - 1)

        ans = []
        for fr, to in queries:
            adj[to].append(fr)
            for node in range(to, n):
                paths[node] = min(paths[prev] for prev in adj[node]) + 1
            ans.append(paths[-1])

        return ans


class Solution3:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        dists = list(range(n - 1, -1, -1))
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        ans = []
        for fr, to in queries:
            adj[fr].append(to)
            for i in range(fr, -1, -1):
                for neib in adj[i]:
                    dists[i] = min(dists[i], dists[neib] + 1)
            ans.append(dists[0])

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_shortestDistanceAfterQueries_1(self):
        print("Test shortestDistanceAfterQueries 1... ", end="")
        self.assertEqual(
            self.sol.shortestDistanceAfterQueries(
                n=5, queries=[[2, 4], [0, 2], [0, 4]]
            ),
            [3, 2, 1],
        )
        print("OK")

    def test_shortestDistanceAfterQueries_2(self):
        print("Test shortestDistanceAfterQueries 2... ", end="")
        self.assertEqual(
            self.sol.shortestDistanceAfterQueries(
                n=4, queries=[[0, 3], [0, 2]]
            ),
            [1, 1],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
