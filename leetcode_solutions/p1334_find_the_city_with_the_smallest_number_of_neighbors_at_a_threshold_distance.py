import unittest
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, wt in edges:
            adj[fr].append((to, wt))
            adj[to].append((fr, wt))

        min_neibs = inf
        ans = 0
        for city in range(n - 1, -1, -1):
            heap = [(0, city)]
            dists = [inf] * n
            dists[city] = 0
            reachable = 0
            while heap:
                d, c = heappop(heap)
                for nc, nd in adj[c]:
                    nd += d
                    if nd <= distanceThreshold and dists[nc] > nd:
                        if dists[nc] is inf:
                            reachable += 1
                            if reachable >= min_neibs:
                                break
                        dists[nc] = nd
                        heappush(heap, (nd, nc))
                else:
                    continue
                break
            if reachable < min_neibs:
                min_neibs = reachable
                ans = city

        return ans


class Solution1:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, wt in edges:
            adj[fr].append((to, wt))
            adj[to].append((fr, wt))

        min_neibs = inf
        ans = 0
        for city in range(n - 1, -1, -1):
            heap = [(0, city)]
            dists = [-1] * n
            dists[city] = 0
            reachable = 0
            while heap:
                d, c = heappop(heap)
                for nc, nd in adj[c]:
                    nd += d
                    if nd > distanceThreshold:
                        continue
                    elif dists[nc] == -1:
                        reachable += 1
                        if reachable >= min_neibs:
                            break
                        dists[nc] = nd
                        heappush(heap, (nd, nc))
                    elif dists[nc] > nd:
                        dists[nc] = nd
                        heappush(heap, (nd, nc))
                else:
                    continue
                break
            if reachable < min_neibs:
                min_neibs = reachable
                ans = city

        return ans


class Solution2:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for fr, to, wt in edges:
            adj[fr].append((to, wt))
            adj[to].append((fr, wt))

        min_neibs = inf
        ans = 0
        for city in range(n - 1, -1, -1):
            heap = [(0, city)]
            dists = [inf] * n
            dists[city] = 0
            while heap:
                d, c = heappop(heap)
                for nc, nd in adj[c]:
                    nd += d
                    if nd > distanceThreshold:
                        continue
                    if dists[nc] > nd:
                        dists[nc] = nd
                        heappush(heap, (nd, nc))
            reachable = sum(d != inf for d in dists) - 1
            if reachable < min_neibs:
                min_neibs = reachable
                ans = city

        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_findTheCity_1(self):
        print("Test findTheCity 1... ", end="")
        self.assertEqual(
            3,
            self.sol.findTheCity(
                n=4,
                edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
                distanceThreshold=4,
            ),
        )
        print("OK")

    def test_findTheCity_2(self):
        print("Test findTheCity 2... ", end="")
        self.assertEqual(
            0,
            self.sol.findTheCity(
                n=5,
                edges=[
                    [0, 1, 2],
                    [0, 4, 8],
                    [1, 2, 3],
                    [1, 4, 2],
                    [2, 3, 1],
                    [3, 4, 1],
                ],
                distanceThreshold=2,
            ),
        )
        print("OK")

    def test_findTheCity_3(self):
        print("Test findTheCity 3... ", end="")
        self.assertEqual(
            5,
            self.sol.findTheCity(
                n=6,
                edges=[
                    [0, 3, 7],
                    [2, 4, 1],
                    [0, 1, 5],
                    [2, 3, 10],
                    [1, 3, 6],
                    [1, 2, 1],
                ],
                distanceThreshold=417,
            ),
        )
        print("OK")

    def test_findTheCity_4(self):
        print("Test findTheCity 4... ", end="")
        self.assertEqual(
            7,
            self.sol.findTheCity(
                n=8,
                edges=[
                    [3, 6, 5840],
                    [0, 6, 7765],
                    [0, 4, 4017],
                    [0, 3, 3930],
                    [0, 7, 1730],
                    [3, 4, 9214],
                    [0, 5, 5861],
                    [2, 6, 2600],
                    [1, 4, 1908],
                    [4, 6, 665],
                    [1, 5, 5140],
                    [5, 7, 6921],
                    [2, 7, 5674],
                    [1, 2, 4154],
                    [2, 5, 913],
                    [0, 2, 7125],
                    [6, 7, 6799],
                    [1, 7, 6166],
                    [4, 5, 5878],
                    [1, 6, 4816],
                    [1, 3, 5591],
                    [5, 6, 7226],
                    [3, 7, 3901],
                    [3, 5, 9989],
                    [2, 3, 8504],
                    [4, 7, 2366],
                ],
                distanceThreshold=919,
            ),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
