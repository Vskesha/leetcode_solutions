from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        def move_to(fi, fj, tree) -> int:
            bfs = deque()
            bfs.append([fi, fj, 0])
            visited = set()
            visited.add((fi, fj))

            while bfs:
                i, j, mv = bfs.popleft()
                if forest[i][j] == tree:
                    return i, j, mv
                if i and forest[i - 1][j] and (i - 1, j) not in visited:  # TOP
                    bfs.append([i - 1, j, mv + 1])
                    visited.add((i - 1, j))
                if (
                    j and forest[i][j - 1] and (i, j - 1) not in visited
                ):  # LEFT
                    bfs.append([i, j - 1, mv + 1])
                    visited.add((i, j - 1))
                if (
                    i < n - 1
                    and forest[i + 1][j]
                    and (i + 1, j) not in visited
                ):  # DOWN
                    bfs.append([i + 1, j, mv + 1])
                    visited.add((i + 1, j))
                if (
                    j < m - 1
                    and forest[i][j + 1]
                    and (i, j + 1) not in visited
                ):  # RIGHT
                    bfs.append([i, j + 1, mv + 1])
                    visited.add((i, j + 1))

            return fi, fj, -1

        m, n = len(forest[0]), len(forest)
        trees = [
            forest[i][j]
            for i in range(n)
            for j in range(m)
            if forest[i][j] > 1
        ]

        total = 0
        i, j = 0, 0  # start position

        for tree in sorted(trees):
            i, j, moves = move_to(i, j, tree)
            if moves == -1:
                return -1
            else:
                total += moves

        return total


def test():
    sol = Solution()
    print("Test 1 ... ", end="")
    assert 6 == sol.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]])
    print("ok")
    print("Test 2 ... ", end="")
    assert -1 == sol.cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]])
    print("ok")
    print("Test 3 ... ", end="")
    assert 6 == sol.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]])
    print("ok")


if __name__ == "__main__":
    test()
