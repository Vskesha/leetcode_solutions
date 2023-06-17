from collections import defaultdict


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


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        n = len(grid)
        ans = 0
        rows = defaultdict(int)

        for line in grid:
            rows[tuple(line)] += 1

        for j in range(n):
            ans += rows[tuple(grid[k][j] for k in range(n))]

        return ans

    def equalPairs2(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trie = Trie()
        for row in grid:
            trie.insert(row)

        ans = 0
        for col in range(n):
            ans += trie.search([grid[i][col] for i in range(n)])

        return ans
