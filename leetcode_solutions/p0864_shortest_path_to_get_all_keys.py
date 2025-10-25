import unittest
from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = "abcdef"
        locks = keys.upper()
        nk = sum(c in keys for s in grid for c in s)
        sti = 0
        while "@" not in grid[sti]:
            sti += 1
        stj = grid[sti].index("@")

        visited = [[set() for _ in range(n)] for _ in range(m)]
        bfs = deque([(sti, stj, "")])
        visited[sti][stj].add("")

        mvs = 0
        while bfs:
            for _ in range(len(bfs)):
                i, j, k = bfs.popleft()
                if grid[i][j] in keys:
                    k += grid[i][j]
                    k = "".join(sorted(set(k)))
                    if len(k) == nk:
                        return mvs
                    visited[i][j].add(k)
                for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                    if 0 <= y < m and 0 <= x < n:
                        ch = grid[y][x]
                        if ch != "#" and (ch not in locks or ch.lower() in k):
                            if k not in visited[y][x]:
                                visited[y][x].add(k)
                                bfs.append((y, x, k))
            mvs += 1
        return -1


class Solution2:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[set() for _ in range(m)] for _ in range(n)]
        keys = "abcdef"  # {'a', 'b', 'c', 'd', 'e', 'f'}  # change to set
        locks = "ABCDEF"  # {'A', 'B', 'C', 'D', 'E', 'F'}  # change to set

        keys_amount = 0
        y, x = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] in keys:
                    keys_amount += 1
                if grid[i][j] == "@":
                    y, x = i, j
                    grid[i] = grid[i].replace("@", ".")

        bfs = deque()
        bfs.append((y, x, "", 0))
        visited[y][x].add("")

        while bfs:
            i, j, my_keys, moves = bfs.popleft()
            for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if 0 <= y < n and 0 <= x < m:
                    if grid[y][x] == "#":
                        continue
                    elif grid[y][x] in locks:
                        if grid[y][x].lower() not in my_keys:
                            continue
                        elif my_keys not in visited[y][x]:
                            bfs.append((y, x, my_keys, moves + 1))
                            visited[y][x].add(my_keys)
                    elif grid[y][x] == ".":
                        if my_keys not in visited[y][x]:
                            bfs.append((y, x, my_keys, moves + 1))
                            visited[y][x].add(my_keys)
                    # elif grid[y][x] in keys and grid[y][x] not in my_keys:
                    else:
                        new_keys = "".join(sorted(set(my_keys + grid[y][x])))
                        if len(new_keys) == keys_amount:
                            return moves + 1
                        if new_keys not in visited[y][x]:
                            bfs.append((y, x, new_keys, moves + 1))
                            visited[y][x].add(new_keys)
        return -1


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_shortest_path_all_keys_1(self):
        print("Test shortestPathAllKeys 1... ", end="")
        self.assertEqual(
            self.sol.shortestPathAllKeys(grid=["@.a..", "###.#", "b.A.B"]), 8
        )
        print("OK")

    def test_shortest_path_all_keys_2(self):
        print("Test shortestPathAllKeys 2... ", end="")
        self.assertEqual(
            self.sol.shortestPathAllKeys(grid=["@..aA", "..B#.", "....b"]), 6
        )
        print("OK")

    def test_shortest_path_all_keys_3(self):
        print("Test shortestPathAllKeys 3... ", end="")
        self.assertEqual(self.sol.shortestPathAllKeys(grid=["@Aa"]), -1)
        print("OK")

    def test_shortest_path_all_keys_4(self):
        print("Test shortestPathAllKeys 4... ", end="")
        self.assertEqual(
            self.sol.shortestPathAllKeys(grid=["@...a", ".###A", "b.BCc"]), 10
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
