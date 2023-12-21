from itertools import pairwise
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(b - a for a, b in pairwise(sorted(x for x, _ in points)))


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
    print('OK')

    print('Test 2... ', end='')
    assert sol.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3
    print('OK')


if __name__ == '__main__':
    test()
