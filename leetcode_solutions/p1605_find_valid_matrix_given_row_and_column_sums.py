from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(colSum)
        n = len(rowSum)
        mat = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            if rowSum[i] < colSum[j]:
                mat[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i += 1
            else:
                mat[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j += 1

        return mat


def test():
    sol = Solution()

    print('Test 1... ', end='')
    for a, b in zip(sol.restoreMatrix(rowSum=[3, 8], colSum=[4, 7]), [[3, 0], [1, 7]]):
        assert a == b
    print('OK')

    print('Test 2... ', end='')
    # print(sol.restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))
    for a, b in zip(sol.restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]), [[5, 0, 0], [3, 4, 0], [0, 2, 8]]):
        assert a == b
    print('OK')


if __name__ == '__main__':
    test()
