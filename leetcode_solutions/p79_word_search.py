import unittest
from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        lw = len(word)

        board_count = Counter(sum(board, []))
        word_count = Counter(word)
        for char, amount in word_count.items():
            if board_count[char] < amount:
                return False
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        visited = [[False] * m for _ in range(n)]

        def traverse(i, j, char_pos):
            if char_pos == lw:
                return True
            next_char = word[char_pos]
            visited[i][j] = True
            for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if (
                    0 <= y < n
                    and 0 <= x < m
                    and not visited[y][x]
                    and board[y][x] == next_char
                    and traverse(y, x, char_pos + 1)
                ):
                    return True
            visited[i][j] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and traverse(i, j, 1):
                    return True

        return False


class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        lw = len(word)

        board_count = Counter(sum(board, []))
        word_count = Counter(word)
        for char, amount in word_count.items():
            if board_count[char] < amount:
                return False
        if word_count[word[0]] > word_count[word[-1]]:
            word = word[::-1]

        self.present = False
        visited = set()

        def traverse(i, j, char_pos):
            if self.present:
                return
            if char_pos == lw:
                self.present = True
                return
            next_char = word[char_pos]
            visited.add((i, j))
            for y, x in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if (
                    0 <= y < n
                    and 0 <= x < m
                    and (y, x) not in visited
                    and board[y][x] == next_char
                ):
                    traverse(y, x, char_pos + 1)
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    traverse(i, j, 1)

        return self.present


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        lw = len(word)

        if len(word) > m * n:
            return False

        cnt = Counter(sum(board, []))
        for ch, q in Counter(word).items():
            if cnt[ch] < q:
                return False

        visited = set()

        def dfs(y, x, i) -> bool:
            if i == lw:
                return True
            if y < 0 or x < 0 or y >= m or x >= n:
                return False
            if (y, x) in visited:
                return False
            if board[y][x] != word[i]:
                return False
            visited.add((y, x))
            i += 1
            ans = (
                dfs(y - 1, x, i)
                or dfs(y + 1, x, i)
                or dfs(y, x + 1, i)
                or dfs(y, x - 1, i)
            )
            visited.remove((y, x))
            return ans

        for y in range(m):
            for x in range(n):
                if dfs(y, x, 0):
                    return True


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_exist_1(self):
        print("Test exist 1... ", end="")
        self.assertTrue(
            self.sol.exist(
                board=[
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                word="ABCCED",
            )
        )
        print("OK")

    def test_exist_2(self):
        print("Test exist 2... ", end="")
        self.assertTrue(
            self.sol.exist(
                board=[
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                word="SEE",
            )
        )
        print("OK")

    def test_exist_3(self):
        print("Test exist 3... ", end="")
        self.assertFalse(
            self.sol.exist(
                board=[
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"],
                ],
                word="ABCB",
            )
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
