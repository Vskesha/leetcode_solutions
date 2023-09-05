def generate_matrix(n):
    A = [[n*n]]
    while A[0][0] > 1:
        a = [range(A[0][0] - len(A), A[0][0])]
        b = [*zip(*A[::-1])]
        A = a + b
    return [list(x) for x in A] * (n > 0)


def generate_matrix2(n):
    c, t, b = 1, 0, n - 1
    res = [[0] * n for _ in range(n)]
    while b > t:
        for i in range(t, b):
            res[t][i] = c
            c += 1
        for i in range(t, b):
            res[i][b] = c
            c += 1
        for i in range(b, t, -1):
            res[b][i] = c
            c += 1
        for i in range(b, t, -1):
            res[i][t] = c
            c += 1
        b -= 1
        t += 1
    if t == b:
        res[b][b] = c
    return res


if __name__ == '__main__':
    print('[[1, 2, 3], [8, 9, 4], [7, 6, 5]] ===', generate_matrix(3))
    print('[[1]] ===', generate_matrix(1))
    print('[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7] ===', generate_matrix(4))

