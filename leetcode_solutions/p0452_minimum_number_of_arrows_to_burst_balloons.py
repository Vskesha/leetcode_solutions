from math import inf
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end = float("-inf")
        ans = 0
        for p in points:
            if p[0] > end:
                ans += 1
                end = p[1]
        return ans


class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        end = -inf
        ans = 0
        for xs, xe in points:
            if xs > end:
                ans += 1
                end = xe
            else:
                end = min(end, xe)
        return ans


def test_find_min_arrow_shots():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    print("OK")

    print("Test 3... ", end="")
    assert sol.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    print("OK")


if __name__ == "__main__":
    test_find_min_arrow_shots()
