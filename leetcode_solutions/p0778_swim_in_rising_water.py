from heapq import heappush, heappop
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        n -= 1

        while True:
            h, i, j = heappop(heap)

            if i == n and j == n:
                return h

            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= y <= n and 0 <= x <= n and not visited[y][x]:
                    heappush(heap, (max(h, grid[y][x]), y, x))
                    visited[y][x] = True


class Solution2:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = [[True] * n for _ in range(n)]
        visited[0][0] = False
        n -= 1

        while True:
            h, i, j = heappop(heap)

            if i == n and j == n:
                return h

            if i and visited[i - 1][j]:
                heappush(heap, (max(h, grid[i - 1][j]), i - 1, j))
                visited[i - 1][j] = False
            if j and visited[i][j - 1]:
                heappush(heap, (max(h, grid[i][j - 1]), i, j - 1))
                visited[i][j - 1] = False
            if i < n and visited[i + 1][j]:
                heappush(heap, (max(h, grid[i + 1][j]), i + 1, j))
                visited[i + 1][j] = False
            if j < n and visited[i][j + 1]:
                heappush(heap, (max(h, grid[i][j + 1]), i, j + 1))
                visited[i][j + 1] = False


def test_swim_in_water():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.swimInWater(grid=[[0, 2], [1, 3]]) == 3
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.swimInWater(
            grid=[
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
        == 16
    )
    print("OK")


if __name__ == "__main__":
    test_swim_in_water()
