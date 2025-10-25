from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        start, end = (0, 0), (0, 0)
        path = m * n
        for i, row in enumerate(grid):
            for j, f in enumerate(row):
                if f == 0:
                    continue
                elif f == -1:
                    path -= 1
                elif f == 1:
                    start = (i, j)
                elif f == 2:
                    end = (i, j)

        visited = set()

        def dfs(fr, dist) -> int:
            if fr == end:
                return int(dist == path)
            if fr in visited:
                return 0
            y, x = fr
            if y < 0 or x < 0 or y >= n or x >= m or grid[y][x] == -1:
                return 0
            dist += 1
            ans = 0
            visited.add(fr)
            for to in ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)):
                ans += dfs(to, dist)
            visited.remove(fr)
            return ans

        return dfs(start, 1)


class Solution1:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        start, end = (0, 0), (0, 0)
        path = m * n
        for i, row in enumerate(grid):
            for j, f in enumerate(row):
                if f == 0:
                    continue
                elif f == -1:
                    path -= 1
                elif f == 1:
                    start = (i, j)
                elif f == 2:
                    end = (i, j)

        visited = set()

        def dfs(fr, dist) -> int:
            if fr == end:
                return int(dist == path)
            if fr in visited:
                return 0
            y, x = fr
            if grid[y][x] == -1:
                return 0
            dist += 1
            ans = 0
            visited.add(fr)
            if y:
                ans += dfs((y - 1, x), dist)
            if x:
                ans += dfs((y, x - 1), dist)
            if y < n - 1:
                ans += dfs((y + 1, x), dist)
            if x < m - 1:
                ans += dfs((y, x + 1), dist)
            visited.remove(fr)
            return ans

        return dfs(start, 1)


class Solution2:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        start, end = (), ()
        path = 2
        # find start square , end square and squares to walk over
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    path += 1

        visited = set()

        def dfs(start, end, curpath):
            # check if square is visited or obstacle
            if start in visited or grid[start[0]][start[1]] == -1:
                return 0
            # check if destination is reached and all nodes are visited
            if start == end:
                if curpath == path:
                    return 1
                else:
                    return 0

            count = 0
            # add square to visited
            visited.add(start)
            # 4-directional walks
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= (x + start[0]) < ROW and 0 <= (y + start[1]) < COL:
                    # increment count
                    count += dfs(
                        (x + start[0], y + start[1]), end, curpath + 1
                    )
                    # remove square from visited
            visited.remove(start)
            return count

        return dfs(start, end, 1)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]])
        == 2
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]])
        == 4
    )
    print("OK")

    print("Test 3... ", end="")
    assert sol.uniquePathsIII(grid=[[0, 1], [2, 0]]) == 0
    print("OK")


if __name__ == "__main__":
    test()
