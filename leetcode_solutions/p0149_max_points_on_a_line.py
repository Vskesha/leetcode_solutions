from collections import Counter
from fractions import Fraction
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lp = len(points)
        res = Counter()
        inf = float('inf')
        ans = 0
        for i in range(lp):
            xi, yi = points[i]
            for j in range(i):
                xj, yj = points[j]
                if xi == xj:
                    res[inf] += 1
                else:
                    res[(yi - yj) / (xi - xj)] += 1
            if res:
                ans = max(ans, *res.values())
                res.clear()

        return ans + 1


class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        lp = len(points)
        res = [Counter() for _ in range(lp)]
        ans = 0
        for i in range(lp):
            xi, yi = points[i]
            for j in range(i):
                xj, yj = points[j]
                if xj - xi:
                    k = (yj - yi) / (xj - xi)
                else:
                    k = float('inf')
                if res[j][k] >= res[i][k]:
                    res[i][k] = res[j][k] + 1
                    ans = max(ans, res[i][k])

        return ans + 1


class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        lp = len(points)
        res = [Counter() for _ in range(lp)]
        ans = 0
        for i in range(lp):
            xi, yi = points[i]
            for j in range(i):
                xj, yj = points[j]
                if xj - xi:
                    k = Fraction(yj - yi, xj - xi)
                else:
                    k = float('inf')
                if res[j][k] >= res[i][k]:
                    res[i][k] = res[j][k] + 1
                    ans = max(ans, res[i][k])

        return ans + 1


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
    print('OK')

    print('Test 2... ', end='')
    assert sol.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    print('OK')

    print('Test 3... ', end='')
    assert sol.maxPoints(
        points=[[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7], [-11, 12], [7, 19],
                [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10], [-13, 8], [7, -5],
                [-4, -9], [-11, 2], [-9, -9], [-5, -16], [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5],
                [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6],
                [-1, -2], [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0], [9, -10], [6, 20],
                [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20], [15, -14], [9, -17],
                [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5], [15, -2], [-12, 11], [19, -18],
                [8, 7], [-5, -3], [-17, -1], [-18, 13], [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12], [-15, 19],
                [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13], [10, -7], [-2, -10], [9, 10], [-1, 7], [-17, -6],
                [-15, 20], [5, -17], [6, -6], [-11, -8]]) == 6
    print('OK')


if __name__ == '__main__':
    test()
