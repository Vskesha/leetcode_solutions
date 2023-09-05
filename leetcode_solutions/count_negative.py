def count_negative(grid):
    h = len(grid)
    w = len(grid[0])
    res = 0
    for i in range(h):
        j = w
        while j > 0 and grid[i][j - 1] < 0:
            j -= 1
        res += (w - j) * (h - i)
        w = j
        if not w:
            break
    return res


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(count_negative(grid))
