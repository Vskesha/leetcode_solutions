from collections import deque
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            row = grid[i]
            q = deque([1])
            if row[1] < row[0]:
                q.appendleft(0)
            for j in range(2, n):
                while q and row[j] >= row[q[-1]]:
                    q.pop()
                q.append(j)
                row[j - 2] = row[q[0]]
                if q[0] == j - 2:
                    q.popleft()

        for j in range(n - 2):
            q = deque([1])
            if grid[1][j] < grid[0][j]:
                q.appendleft(0)
            for i in range(2, n):
                while q and grid[i][j] >= grid[q[-1]][j]:
                    q.pop()
                q.append(i)
                grid[i - 2][j] = grid[q[0]][j]
                if q[0] == i - 2:
                    q.popleft()

        return [grid[i][: n - 2] for i in range(n - 2)]


class Solution2:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            for j in range(n - 2):
                grid[i][j] = max(grid[i][j : j + 3])

        for j in range(n - 2):
            for i in range(n - 2):
                grid[i][j] = max([grid[i][j], grid[i + 1][j], grid[i + 2][j]])

        return [grid[i][: n - 2] for i in range(n - 2)]


class Solution3:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [
                max(
                    grid[y][x]
                    for y in range(i, i + 3)
                    for x in range(j, j + 3)
                )
                for j in range(len(grid) - 2)
            ]
            for i in range(len(grid) - 2)
        ]


class Solution4:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [
                max(grid[i + k // 3][j + k % 3] for k in range(9))
                for j in range(len(grid) - 2)
            ]
            for i in range(len(grid) - 2)
        ]


def test_largest_local():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.largestLocal(
        grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    ) == [[9, 9], [8, 6]]
    print("OK")

    print("Test 2... ", end="")
    assert sol.largestLocal(
        grid=[
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    ) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    print("OK")


if __name__ == "__main__":
    test_largest_local()
