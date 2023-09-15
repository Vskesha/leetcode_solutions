from typing import List
from heapq import heapify, heappop


class UF:
    def __init__(self, n: int):
        self.root = list(range(n))
        self.sep = n - 1

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, dist, node1, node2) -> int:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.root[root2] = root1
            self.sep -= 1
            return dist
        else:
            return 0

    def all_connected(self):
        return not self.sep


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        q = []
        lp = len(points)

        for i in range(lp):
            for j in range(i + 1, lp):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                q.append((d, i, j))

        heapify(q)
        uf = UF(lp)
        res = 0

        while not uf.all_connected():
            res += uf.union(*heappop(q))

        return res


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    print('ok\nTest 2 ... ', end='')
    assert sol.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]])
    print('ok')


if __name__ == '__main__':
    test()
