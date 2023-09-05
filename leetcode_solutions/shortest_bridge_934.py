from collections import deque

def shortest_bridge(grid: list[list[int]]):
    n = len(grid)
    island = deque()
    dfs = deque()
    i = j = 0
    
    # locate cell of first island
    while i < n:
        j = 0
        while j < n:
            if grid[i][j]:
                island.append((i, j, 0))
                dfs.append((i, j))
                grid[i][j] = 2
                i = j = n
            else:
                grid[i][j] = 3
            j += 1 
        i += 1

    # add all cells of first island to the queue
    while dfs:
        i, j = dfs.popleft()
        
        for y, x in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
            if 0 <= x < n and 0 <= y < n and grid[y][x] == 1:     
                grid[y][x] = 2
                dfs.append((y, x))
                island.append((y, x, 0))
    
    # traverse through empty fields with keeping distance
    while island:
        i, j, dist = island.popleft()
        
        for y, x in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
            if 0 <= x < n and 0 <= y < n:     
                if grid[y][x] == 1:
                    return dist
                elif grid[y][x] == 0:
                    grid[y][x] = 2
                    island.append((y, x, dist+1))


if __name__ == '__main__':
    print('1 ===', shortest_bridge([[0,1],
                                    [1,0]]))
    print('2 ===', shortest_bridge([[0,1,0],
                                    [0,0,0],
                                    [0,0,1]]))
    print('1 ===', shortest_bridge([[1,1,1,1,1],
                                    [1,0,0,0,1],
                                    [1,0,1,0,1],
                                    [1,0,0,0,1],
                                    [1,1,1,1,1]]))
    print('1 ===', shortest_bridge([[0,1,0,0,0],
                                    [0,1,0,1,1],
                                    [0,0,0,0,1],
                                    [0,0,0,0,0],
                                    [0,0,0,0,0]]))
    print('h ===', shortest_bridge([[0,0,0,0,0,0],
                                    [0,1,0,0,0,0],
                                    [1,1,0,0,0,0],
                                    [1,1,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,1,1,0,0]]))