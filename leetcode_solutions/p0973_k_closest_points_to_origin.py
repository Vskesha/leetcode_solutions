import unittest
from heapq import heapify, heappop, nsmallest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(sum(c**2 for c in p) ** 0.5, p) for p in points]
        heapify(heap)
        return [x[1] for x in nsmallest(k, heap)]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for p in points:
            dists.append((p[0] ** 2 + p[1] ** 2, p))
        heapify(dists)
        ans = []
        for _ in range(k):
            _, p = heappop(dists)
            ans.append(p)
        return ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSamePoints(self, points1, points2):
        p1 = set(tuple(p) for p in points1)
        p2 = set(tuple(p) for p in points2)
        self.assertSetEqual(p1, p2)

    def test_kClosest_1(self):
        print("Test kClosest 1... ", end="")
        self.assertSamePoints(
            [[-2, 2]], self.sol.kClosest(points=[[1, 3], [-2, 2]], k=1)
        )
        print("OK")

    def test_kClosest_2(self):
        print("Test kClosest 2... ", end="")
        self.assertSamePoints(
            [[3, 3], [-2, 4]],
            self.sol.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2),
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
