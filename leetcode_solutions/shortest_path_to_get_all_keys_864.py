from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[set() for _ in range(m)] for _ in range(n)]
        keys = 'abcdef'  # {'a', 'b', 'c', 'd', 'e', 'f'}  # change to set
        locks = 'ABCDEF'  # {'A', 'B', 'C', 'D', 'E', 'F'}  # change to set

        keys_amount = 0
        y, x = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] in keys:
                    keys_amount += 1
                if grid[i][j] == '@':
                    y, x = i, j
                    grid[i] = grid[i].replace('@', '.')

        bfs = deque()
        bfs.append((y, x, '', 0))
        visited[y][x].add('')

        while bfs:
            i, j, my_keys, moves = bfs.popleft()
            for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if 0 <= y < n and 0 <= x < m:
                    if grid[y][x] == '#':
                        continue
                    elif grid[y][x] in locks:
                        if grid[y][x].lower() not in my_keys:
                            continue
                        elif my_keys not in visited[y][x]:
                            bfs.append((y, x, my_keys, moves + 1))
                            visited[y][x].add(my_keys)
                    elif grid[y][x] == '.':
                        if my_keys not in visited[y][x]:
                            bfs.append((y, x, my_keys, moves + 1))
                            visited[y][x].add(my_keys)
                    # elif grid[y][x] in keys and grid[y][x] not in my_keys:
                    else:
                        new_keys = ''.join(sorted(set(my_keys + grid[y][x])))
                        if len(new_keys) == keys_amount:
                            return moves + 1
                        if new_keys not in visited[y][x]:
                            bfs.append((y, x, new_keys, moves + 1))
                            visited[y][x].add(new_keys)
        return -1


def main():
    sol = Solution()
    print('-1 ===', sol.shortestPathAllKeys(grid=["@Aa"]))
    print('8 ===', sol.shortestPathAllKeys(grid=["@.a..", "###.#", "b.A.B"]))
    print('6 ===', sol.shortestPathAllKeys(grid=["@..aA", "..B#.", "....b"]))


if __name__ == '__main__':
    main()
