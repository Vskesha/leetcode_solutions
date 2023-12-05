from itertools import pairwise
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a, b in pairwise(points))


class Solution2:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        px, py = points[0]
        ans = 0

        for x, y in points:
            ans += max(abs(x - px), abs(y - py))
            px, py = x, y

        return ans


class Solution3:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        points = iter(points)
        px, py = next(points)
        ans = 0

        for x, y in points:
            ans += max(abs(x - px), abs(y - py))
            px, py = x, y

        return ans

def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]) == 7
    print('OK')

    print('Test 2... ', end='')
    assert sol.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]) == 5
    print('OK')


if __name__ == '__main__':
    test()
