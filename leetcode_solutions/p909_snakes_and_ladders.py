from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n * n
        bfs, visited = deque([(1, 0)]), {1}
        while bfs:
            c, d = bfs.popleft()
            if c == n2:
                return d
            for i in range(c + 1, min(c + 6, n2) + 1):
                if i not in visited:
                    visited.add(i)
                    fr = (i - 1) // n
                    ld = board[n - fr - 1][n - (i - 1) % n - 1 if fr % 2 else (i - 1) % n]
                    bfs.append((i if ld == -1 else ld, d + 1))

        return -1


class Solution1:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n * n
        bfs, visited = deque([(1, 0)]), {1}
        while bfs:
            c, d = bfs.popleft()
            if c == n2:
                return d
            for j in range(c, min(c + 6, n2)):
                if j + 1 not in visited:
                    visited.add(j + 1)
                    ld = board[n - j // n - 1][n - j % n - 1 if j // n % 2 else j % n]
                    bfs.append((j + 1 if ld == -1 else ld, d + 1))

        return -1


class Solution2:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def ladder(i) -> int:
            i -= 1
            fr = i // n
            rm = i % n
            bd = fr % 2
            r = n - fr - 1
            c = n - rm - 1 if bd else rm
            return board[r][c]

        n = len(board)
        n2 = n * n
        bfs = deque()
        bfs.append((1, 0))
        visited = {1}

        while bfs:
            c, d = bfs.popleft()
            if c == n2:
                return d
            d += 1
            for i in range(c + 1, min(c + 6, n2) + 1):
                if i not in visited:
                    visited.add(i)
                    ld = ladder(i)
                    if ld == -1:
                        bfs.append((i, d))
                    else:
                        bfs.append((ld, d))
                        if ladder(ld) == -1:
                            visited.add(ld)

        return -1


class Solution3:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        row = len(board)
        column = len(board[0])
        q = deque()
        visited = set()
        parent = [-1] * ((row * column) + 1)
        distance = [-1] * ((row * column) + 1)
        q.append(1)
        distance[1] = 0
        while q:
            node = q.popleft()

            for i in range(1, 7):
                n = node + i
                if n >= len(parent):
                    continue
                # snake and ladder movement
                ft = (n - 1) // column
                r = row - 1 - ft
                c = (n - 1) % column
                if ft % 2 != 0:
                    c = column - c - 1

                # print(r,c)
                v = board[r][c]

                if v != -1:
                    n = v
                if n in visited or v == node:
                    continue

                q.append(n)
                visited.add(n)
                parent[n] = node
                distance[n] = distance[node] + 1

        return distance[-1]


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.snakesAndLadders(
        board=[[-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, 35, -1, -1, 13, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, 15, -1, -1, -1, -1]]
    ) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.snakesAndLadders(
        board=[[-1, -1],
               [-1, 3]]
    ) == 1
    print('OK')

    print('Test 3... ', end='')
    assert sol.snakesAndLadders(
        board=[[1, 1, -1],
               [1, 1, 1],
               [-1, 1, 1]]
    ) == -1
    print('OK')

    print('Test 4... ', end='')
    assert sol.snakesAndLadders(
        board=[[-1, -1, 16, 6, -1],
               [-1, 9, 25, 8, -1],
               [8, 20, 2, 7, -1],
               [-1, -1, 12, -1, -1],
               [-1, -1, -1, 12, 23]]
    ) == 2
    print('OK')

    print('Test 5... ', end='')
    assert sol.snakesAndLadders(
        board=[[-1, -1, -1, 46, 47, -1, -1, -1],
               [51, -1, -1, 63, -1, 31, 21, -1],
               [-1, -1, 26, -1, -1, 38, -1, -1],
               [-1, -1, 11, -1, 14, 23, 56, 57],
               [11, -1, -1, -1, 49, 36, -1, 48],
               [-1, -1, -1, 33, 56, -1, 57, 21],
               [-1, -1, -1, -1, -1, -1, 2, -1],
               [-1, -1, -1, 8, 3, -1, 6, 56]]
    ) == 4
    print('OK')


if __name__ == '__main__':
    test()
