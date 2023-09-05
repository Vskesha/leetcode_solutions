from collections import deque


def oranges_rotting(grid):  #BFS solution
    m = len(grid[0])
    n = len(grid)
    
    for i in range(n):
        if 1 in grid[i]:
            break
    else:
        return 0
    
    dist = 0
    deq = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                deq.append((i, j, 0))
                
    while len(deq) > 0:
        i, j, dist = deq.popleft()
        if i and grid[i-1][j] == 1:  #top
            grid[i-1][j] = 3
            deq.append((i-1, j, dist+1))
        if j and grid[i][j-1] == 1:  #left
            grid[i][j-1] = 3
            deq.append((i, j-1, dist+1))
        if i < n - 1 and grid[i+1][j] == 1:  # bottom
            grid[i+1][j] = 3
            deq.append((i+1, j, dist+1))
        if j < m - 1 and grid[i][j+1] == 1:  # right
            grid[i][j+1] = 3
            deq.append((i, j+1, dist+1))
    
    for i in range(n):
        if 1 in grid[i]:
            return -1
    
    return dist
    

def oranges_rotting2(grid):
    def traverse(i, j, dist=0):
        aux[i][j] = dist
        if i > 0 and grid[i-1][j] == 1 and aux[i-1][j] > dist + 1:
            traverse(i-1, j, dist+1)
        if j > 0 and grid[i][j-1] == 1 and aux[i][j-1] > dist + 1:
            traverse(i, j-1, dist+1)
        if j < m - 1 and grid[i][j+1] == 1 and aux[i][j+1] > dist + 1:
            traverse(i, j+1, dist+1)
        if i < n - 1 and grid[i+1][j] == 1 and aux[i+1][j] > dist + 1:
            traverse(i+1, j, dist+1)
    
    m = len(grid[0])
    n = len(grid)
    aux = [[100] * m for _ in range(n)]
    rotten = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]
    for coords in rotten:
        traverse(*coords)
    
    max_dist = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and max_dist < aux[i][j]:
                max_dist = aux[i][j]
    return max_dist if max_dist < 100 else -1                


if __name__ == '__main__':
    print('4 ===', oranges_rotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print('-1 ===', oranges_rotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print('0 ===', oranges_rotting(grid=[[0, 2]]))
    print('-1 ===', oranges_rotting(grid=[[0, 1]]))
    print('58 ===', oranges_rotting(grid=[[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]))
