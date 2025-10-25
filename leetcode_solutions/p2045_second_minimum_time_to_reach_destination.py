import unittest
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj = [[] for _ in range(n + 1)]
        for fr, to in edges:
            adj[fr].append(to)
            adj[to].append(fr)

        heap = [(0, 1)]
        times1 = [inf for _ in range(n + 1)]
        times2 = [inf for _ in range(n + 1)]
        times1[1] = 0
        last_visited = inf

        while heap:
            ctime, curr = heappop(heap)
            if curr == n:
                if ctime > last_visited:
                    return ctime
                last_visited = ctime
            if ctime // change % 2:
                ctime = (ctime // change + 1) * change + time
            else:
                ctime += time

            for neib in adj[curr]:
                if ctime < times1[neib]:
                    times2[neib] = times1[neib]
                    times1[neib] = ctime
                    heappush(heap, (ctime, neib))
                elif ctime < times2[neib] and ctime != times1[neib]:
                    times2[neib] = ctime
                    heappush(heap, (ctime, neib))

        return -1


class Solution2:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj = [[] for _ in range(n + 1)]
        for fr, to in edges:
            adj[fr].append(to)
            adj[to].append(fr)

        heap = [(0, 1)]
        times = [(inf, inf) for _ in range(n + 1)]
        times[1] = (0, inf)
        last_visited = inf

        while heap:
            ctime, curr = heappop(heap)
            if curr == n:
                if ctime > last_visited:
                    return ctime
                last_visited = ctime
            cycles = ctime // change
            if cycles % 2:
                ctime = (cycles + 1) * change
            for neib in adj[curr]:
                ntime = ctime + time
                first, second = times[neib]
                if ntime < second:
                    if ntime < first:
                        times[neib] = (ntime, first)
                    elif ntime != first:
                        times[neib] = (first, ntime)
                    heappush(heap, (ntime, neib))

        return -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_secondMinimum_1(self):
        print("Test secondMinimum 1... ", end="")
        self.assertEqual(
            13,
            self.sol.secondMinimum(
                n=5,
                edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]],
                time=3,
                change=5,
            ),
        )
        print("OK")

    def test_secondMinimum_2(self):
        print("Test secondMinimum 2... ", end="")
        self.assertEqual(
            11,
            self.sol.secondMinimum(n=2, edges=[[1, 2]], time=3, change=2),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
