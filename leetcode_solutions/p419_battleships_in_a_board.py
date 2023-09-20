from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board[0])
        n = len(board)
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] =='.'):
                    ans += 1
        return ans


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert 2 == sol.countBattleships([["X", ".", ".", "X"],
                                      [".", ".", ".", "X"],
                                      [".", ".", ".", "X"]])
    print('ok\nTest 2 ... ', end='')
    assert 0 == sol.countBattleships([["."]])
    print('ok')


if __name__ == '__main__':
    test()
