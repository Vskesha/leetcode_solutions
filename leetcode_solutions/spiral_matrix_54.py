def spiral_order(matrix):
    left = top = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    res = []
    while right >= left and bottom >= top:
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        if right < left or bottom < top:
            break
        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


def spiral_order2(matrix):
    n = len(matrix)
    m = len(matrix[0])
    r = min(m, n)
    mid = r // 2
    res = []
    for i in range(mid):
        for j in range(i, m-i):
            res.append(matrix[i][j])
        for j in range(i+1, n-i-1):
            res.append(matrix[j][m-i-1])
        for j in range(m-i-1, i-1, -1):
            res.append(matrix[n-i-1][j])
        for j in range(n-i-2, i, -1):
            res.append(matrix[j][i])
    if r % 2:
        for j in range(mid, m - mid):
            res.append(matrix[mid][j])
        for j in range(mid + 1, n - mid):
            res.append(matrix[j][m - mid - 1])
    return res


if __name__ == '__main__':
    print('[1, 2, 3, 6, 9, 8, 7, 4, 5] ===', spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print('[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] ===', spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print('[3, 2] ===', spiral_order([[3], [2]]))
