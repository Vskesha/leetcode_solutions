def count_battleships(board: list[list[str]]) -> int:
        return sum(1 
                   for i in range(len(board)) 
                   for j in range(len(board[0])) 
                   if board[i][j] == 'X' and 
                   (i == 0 or board[i-1][j] == '.') and 
                   (j == 0 or board[i][j-1] == '.'))
        
        
if __name__ == '__main__':
    print('2 ===', count_battleships([["X",".",".","X"],
                                      [".",".",".","X"],
                                      [".",".",".","X"]]))
    print('0 ===', count_battleships([["."]]))
    