import unittest
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insert(word):
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = [{}, 1]
                else:
                    curr[ch][1] += 1
                curr = curr[ch][0]
            curr[end] = word

        def remove(word):
            curr = trie
            for ch in word:
                next = curr[ch][0]
                if curr[ch][1] == 1:
                    del curr[ch]
                else:
                    curr[ch][1] -= 1
                curr = next
            del curr[end]

        def dfs(i, j, curr):
            visited[i][j] = True
            if end in curr:
                self.ans.append(curr[end])
                remove(curr[end])
            for ni, nj, nch in neibs[i][j]:
                if not visited[ni][nj] and nch in curr:
                    dfs(ni, nj, curr[nch][0])
            visited[i][j] = False

        self.ans = []
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        trie = {}
        end = "*"

        neibs = [[[] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i:
                    neibs[i][j].append((i - 1, j, board[i - 1][j]))
                    neibs[i - 1][j].append((i, j, board[i][j]))
                if j:
                    neibs[i][j].append((i, j - 1, board[i][j - 1]))
                    neibs[i][j - 1].append((i, j, board[i][j]))

        for word in words:
            insert(word)

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch in trie:
                    dfs(i, j, trie[ch][0])

        return self.ans


class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insert(word):
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = [{}, 1]
                else:
                    curr[ch][1] += 1
                curr = curr[ch][0]
            curr[end] = word

        def remove(word):
            curr = trie
            for ch in word:
                next = curr[ch][0]
                if curr[ch][1] == 1:
                    del curr[ch]
                else:
                    curr[ch][1] -= 1
                curr = next
            del curr[end]

        def neibs(i, j):
            ns = []
            if i:
                ns.append((i - 1, j, board[i - 1][j]))
            if j:
                ns.append((i, j - 1, board[i][j - 1]))
            if i != m - 1:
                ns.append((i + 1, j, board[i + 1][j]))
            if j != n - 1:
                ns.append((i, j + 1, board[i][j + 1]))
            return ns

        def dfs(i, j, curr):
            visited[i][j] = True
            if end in curr:
                self.ans.append(curr[end])
                remove(curr[end])
            for ni, nj, nch in neibs(i, j):
                if not visited[ni][nj] and nch in curr:
                    dfs(ni, nj, curr[nch][0])
            visited[i][j] = False

        self.ans = []
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        trie = {}
        end = "*"

        for word in words:
            insert(word)

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch in trie:
                    dfs(i, j, trie[ch][0])

        return self.ans


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.usages = {}

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
                curr.usages[char] = 1
            else:
                curr.usages[char] += 1
            curr = curr.children[char]
        curr.is_end = True

    def remove(self, word):
        curr = self
        for char in word:
            if curr.usages[char] == 1:
                temp = curr.children[char]
                del curr.usages[char]
                del curr.children[char]
                curr = temp
            else:
                curr.usages[char] -= 1
                curr = curr.children[char]
        curr.is_end = False


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        n = len(board)
        m = len(board[0])
        result = []

        def dfs(i, j, curr, visited, word):
            visited.add((i, j))
            curr = curr.children[board[i][j]]
            word += board[i][j]
            if curr.is_end:
                result.append(word)
                trie.remove(word)
            for y, x in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= y < n and 0 <= x < m:
                    if (y, x) not in visited:
                        if board[y][x] in curr.children:
                            dfs(y, x, curr, visited, word)
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.children:
                    dfs(i, j, trie, visited=set(), word="")

        return result


class Solution3:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def insert(word):
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = [{}, 1]
                else:
                    curr[ch][1] += 1
                curr = curr[ch][0]
            curr[end] = word

        def remove(word):
            curr = trie
            for ch in word:
                next = curr[ch][0]
                if curr[ch][1] == 1:
                    del curr[ch]
                else:
                    curr[ch][1] -= 1
                curr = next
            del curr[end]

        def neibs(i, j):
            ns = []
            if i:
                ns.append((i - 1, j))
            if j:
                ns.append((i, j - 1))
            if i != m - 1:
                ns.append((i + 1, j))
            if j != n - 1:
                ns.append((i, j + 1))
            return ns

        def dfs(i, j, curr):
            ch = board[i][j]
            if ch not in curr:
                return

            curr = curr[ch][0]
            visited[i][j] = True

            if end in curr:
                self.ans.append(curr[end])
                remove(curr[end])

            for ni, nj in neibs(i, j):
                if not visited[ni][nj]:
                    dfs(ni, nj, curr)

            visited[i][j] = False

        self.ans = []
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        trie = {}
        end = "*"

        for word in words:
            insert(word)

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return self.ans


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameWords(self, words1, words2):
        self.assertSetEqual(set(words1), set(words2))

    def test_find_words_1(self):
        print("Test findWords 1... ", end="")
        self.assertSameWords(
            self.sol.findWords(
                board=[
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                words=["oath", "pea", "eat", "rain"],
            ),
            ["eat", "oath"],
        )
        print("OK")

    def test_find_words_2(self):
        print("Test findWords 2... ", end="")
        self.assertSameWords(
            self.sol.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]),
            [],
        )
        print("OK")

    def test_find_words_3(self):
        print("Test findWords 3... ", end="")
        self.assertSameWords(
            self.sol.findWords(
                board=[
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                words=["oath", "pea", "eat", "rain", "hklf", "hf"],
            ),
            ["oath", "eat", "hklf", "hf"],
        )
        print("OK")

    def test_find_words_4(self):
        print("Test findWords 4... ", end="")
        self.assertSameWords(
            self.sol.findWords(
                board=[
                    ["o", "a", "b", "n"],
                    ["o", "t", "a", "e"],
                    ["a", "h", "k", "r"],
                    ["a", "f", "l", "v"],
                ],
                words=["oa", "oaa"],
            ),
            ["oa", "oaa"],
        )
        print("OK")

    def test_find_words_5(self):
        print("Test findWords 5... ", end="")
        self.assertSameWords(
            self.sol.findWords(
                board=[
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ],
                words=[
                    "a",
                    "aa",
                    "aaa",
                    "aaaa",
                    "aaaaa",
                    "aaaaaa",
                    "aaaaaaa",
                    "aaaaaaaa",
                    "aaaaaaaaa",
                    "aaaaaaaaaa",
                ],
            ),
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
