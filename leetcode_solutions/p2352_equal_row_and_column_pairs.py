from collections import Counter, defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rc = Counter(map(tuple, grid))
        return sum(rc[col] for col in zip(*grid))


class Solution1:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        ans = 0
        rows = defaultdict(int)

        for line in grid:
            rows[tuple(line)] += 1

        for j in range(n):
            ans += rows[tuple(grid[k][j] for k in range(n))]

        return ans


class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0

    def insert(self, arr):
        curr = self
        for num in arr:
            if num not in curr.children:
                curr.children[num] = Trie()
            curr = curr.children[num]
        curr.count += 1

    def search(self, arr) -> int:
        curr = self
        for num in arr:
            if num not in curr.children:
                return 0
            curr = curr.children[num]
        return curr.count


class Solution2:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trie = Trie()
        for row in grid:
            trie.insert(row)

        ans = 0
        for col in range(n):
            ans += trie.search([grid[i][col] for i in range(n)])

        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.equalPairs(
            grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        )
        == 3
    )
    print("OK")


if __name__ == "__main__":
    test()
