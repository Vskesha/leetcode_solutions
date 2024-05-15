from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return 0

        n = len(grid)

        bfs = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])

        dist = 2
        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= di < n and 0 <= dj < n and grid[di][dj] == 0:
                        grid[di][dj] = dist
                        bfs.append((di, dj))
            dist += 1

        heap = [(-grid[0][0], 0, 0)]
        visited = [[True] * n for _ in range(n)]
        visited[0][0] = False
        while True:
            s, i, j = heappop(heap)
            if n - 1 == i == j:
                return -s - 1
            for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= di < n and 0 <= dj < n and visited[di][dj]:
                    ns = max(s, -grid[di][dj])
                    heappush(heap, (ns, di, dj))
                    visited[di][dj] = False


class Solution1:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        bfs = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])

        dist = 2
        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= di < n and 0 <= dj < n and grid[di][dj] == 0:
                        grid[di][dj] = dist
                        bfs.append((di, dj))
            dist += 1

        safety = [[0] * n for _ in range(n)]
        safety[0][0] = grid[0][0]
        bfs = deque([(0, 0)])
        while bfs:
            i, j = bfs.popleft()
            s = safety[i][j]
            for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= di < n and 0 <= dj < n:
                    ns = min(s, grid[di][dj])
                    if ns > safety[di][dj]:
                        safety[di][dj] = ns
                        bfs.append((di, dj))

        return safety[-1][-1] - 1


class Solution2:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.ans = 0
        n = len(grid)
        bfs = deque()
        safe = [[-1] * n for _ in grid]
        visited = [[False] * n for _ in grid]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    safe[i][j] = 0
                    bfs.append((i, j))

        dist = 1
        n -= 1

        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= di <= n and 0 <= dj <= n and safe[di][dj] == -1:
                        safe[di][dj] = dist
                        bfs.append((di, dj))
            dist += 1

        def dfs(i, j, mx):
            mx = min(mx, safe[i][j])

            if n == i == j:
                self.ans = mx

            visited[i][j] = True

            for di, dj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                if (
                    0 <= di <= n
                    and 0 <= dj <= n
                    and not visited[di][dj]
                    and safe[di][dj] >= self.ans
                ):
                    dfs(di, dj, mx)

            visited[i][j] = False

        dfs(0, 0, 3 * n)

        return self.ans


def test_maximum_safeness_factor():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
    print("OK")

    print("Test 2... ", end="")
    assert sol.maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
    print("OK")

    print("Test 3... ", end="")
    assert (
        sol.maximumSafenessFactor(
            grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
        )
        == 2
    )
    print("OK")

    print("Test 4... ", end="")
    assert (
        sol.maximumSafenessFactor(
            grid=[
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0],
            ]
        )
        == 1
    )
    print("OK")


if __name__ == "__main__":
    test_maximum_safeness_factor()
