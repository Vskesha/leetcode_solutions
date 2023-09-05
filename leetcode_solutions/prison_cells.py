def prison_cells(cells, n):
    for _ in range(n):
        tmp = [0] * 8
        for i in range(1, 7):
            tmp[i] = int(cells[i - 1] == cells[i + 1])
        cells = tmp
        print(cells)
    return cells


if __name__ == '__main__':
    prison_cells([1, 1, 1, 1, 1, 1, 1, 1], 100)
