from heapq import heappop, heappush
from typing import List


# dijkstra optimized
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m = len(heights[0])
        n = len(heights)

        aux = [[1_000_000] * m for _ in range(n)]
        aux[0][0] = 0
        bfs = [(0, 0, 0)]

        while bfs:
            ch, i, j = heappop(bfs)
            if i == n - 1 and j == m - 1:
                return ch

            if i and ch < aux[i - 1][j]:
                d = max(abs(heights[i][j] - heights[i - 1][j]), ch)
                if d < aux[i - 1][j]:
                    aux[i - 1][j] = d
                    heappush(bfs, (d, i - 1, j))

            if j and ch < aux[i][j - 1]:
                d = max(abs(heights[i][j] - heights[i][j - 1]), ch)
                if d < aux[i][j - 1]:
                    aux[i][j - 1] = d
                    heappush(bfs, (d, i, j - 1))

            if i < n - 1 and ch < aux[i + 1][j]:
                d = max(abs(heights[i][j] - heights[i + 1][j]), ch)
                if d < aux[i + 1][j]:
                    aux[i + 1][j] = d
                    heappush(bfs, (d, i + 1, j))

            if j < m - 1 and ch < aux[i][j + 1]:
                d = max(abs(heights[i][j] - heights[i][j + 1]), ch)
                if d < aux[i][j + 1]:
                    aux[i][j + 1] = d
                    heappush(bfs, (d, i, j + 1))


# dijkstra modified
class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m = len(heights[0])
        n = len(heights)

        aux = [[1_000_000] * m for _ in range(n)]
        aux[0][0] = 0
        bfs = [(0, 0, 0)]

        while bfs:
            ch, i, j = heappop(bfs)
            if i == n - 1 and j == m - 1:
                return ch

            for y, x in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if 0 <= y < n and 0 <= x < m:
                    d = max(abs(heights[i][j] - heights[y][x]), ch)
                    if d < aux[y][x]:
                        aux[y][x] = d
                        heappush(bfs, (d, y, x))


# TLE Time Limit Exceeded
class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights[0])
        n = len(heights)

        self.mh = 10_000_000
        visited = set()

        def dfs(ch, i, j):
            if not (i or j):
                self.mh = ch
                return
            visited.add((i, j))

            neibs = []
            for y, x in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                if 0 <= y < n and 0 <= x < m:
                    if (y, x) not in visited:
                        d = abs(heights[i][j] - heights[y][x])
                        neibs.append((max(ch, d), y, x))
            neibs.sort()
            for d, y, x in neibs:
                if d < self.mh:
                    dfs(d, y, x)

            visited.remove((i, j))
        dfs(0, n - 1, m - 1)

        return self.mh


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.minimumEffortPath(heights=[[1, 2, 2],
                                          [3, 8, 2],
                                          [5, 3, 5]]) == 2
    print('ok\nTest 2 ... ', end='')
    assert sol.minimumEffortPath(heights=[[1, 2, 3],
                                          [3, 8, 4],
                                          [5, 3, 5]]) == 1
    print('ok\nTest 3 ... ', end='')
    assert sol.minimumEffortPath(heights=[[1, 2, 1, 1, 1],
                                          [1, 2, 1, 2, 1],
                                          [1, 2, 1, 2, 1],
                                          [1, 2, 1, 2, 1],
                                          [1, 1, 1, 2, 1]]) == 0
    print('ok')


if __name__ == '__main__':
    test()
