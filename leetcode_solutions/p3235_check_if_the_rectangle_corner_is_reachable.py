import unittest
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1

    def connected(self, node1, node2) -> bool:
        return self.find(node1) == self.find(node2)


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        lc = len(circles)
        ds = DisjointSet(lc + 2)

        for i in range(lc):
            x1, y1, r1 = circles[i]
            if x1 <= r1 or Y - y1 <= r1:
                ds.union(lc, i)
            if y1 <= r1 or X - x1 <= r1:
                ds.union(lc + 1, i)
            for j in range(i):
                x2, y2, r2 = circles[j]
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if dist <= r1 + r2:
                    ds.union(i, j)

        return not ds.connected(lc, lc + 1)


class Solution2:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        lc = len(circles)
        root = list(range(lc + 2))

        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]

        for i in range(lc):
            x1, y1, r1 = circles[i]
            if x1 <= r1 or Y - y1 <= r1:
                root[i] = lc
            if y1 <= r1 or X - x1 <= r1:
                if root[i] == lc:
                    return False
                root[i] = lc + 1
            for j in range(i):
                x2, y2, r2 = circles[j]
                sqdist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if sqdist <= (r1 + r2) ** 2:
                    root1 = find(i)
                    root2 = find(j)
                    if root1 != root2:
                        root[root2] = root1

        return find(lc) != find(lc + 1)


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_canReachCorner_1(self):
        print("Test canReachCorner 1... ", end="")
        self.assertTrue(self.sol.canReachCorner(X=3, Y=4, circles=[[2, 1, 1]]))
        print("OK")

    def test_canReachCorner_2(self):
        print("Test canReachCorner 2... ", end="")
        self.assertFalse(
            self.sol.canReachCorner(X=3, Y=3, circles=[[1, 1, 2]])
        )
        print("OK")

    def test_canReachCorner_3(self):
        print("Test canReachCorner 3... ", end="")
        self.assertFalse(
            self.sol.canReachCorner(X=3, Y=3, circles=[[2, 1, 1], [1, 2, 1]])
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
