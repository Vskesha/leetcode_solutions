from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
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
                if 0 <= y < n and 0 <= x < m and (y, x) not in visited and board[y][x] == next_char:
                    traverse(y, x, char_pos + 1)
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    traverse(i, j, 1)

        return self.present
