from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix[0]), len(matrix)
        self.sums = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            rowsum = 0
            for j in range(m):
                rowsum += matrix[i][j]
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + rowsum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][
            col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


def test():
    mat = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

    print('Test 1 ... ', end='')
    assert mat.sumRegion(2, 1, 4, 3) == 8
    print('ok')

    print('Test 2 ... ', end='')
    assert mat.sumRegion(1, 1, 2, 2) == 11
    print('ok')

    print('Test 3 ... ', end='')
    assert mat.sumRegion(1, 2, 2, 4) == 12
    print('ok')


if __name__ == '__main__':
    test()
