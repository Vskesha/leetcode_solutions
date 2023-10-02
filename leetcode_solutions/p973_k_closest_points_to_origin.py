from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]


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


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [[3, 3], [-2, 4]]
    print('ok')


if __name__ == '__main__':
    test()
