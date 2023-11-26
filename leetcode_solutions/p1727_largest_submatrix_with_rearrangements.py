from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        prev = matrix[0]
        m = len(prev)
        n = len(matrix)

        for i in range(1, n):
            row = matrix[i]
            for j in range(m):
                if row[j]:
                    row[j] += prev[j]
            prev = row

        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for i, n in enumerate(row, 1):
                ans = max(ans, i * n)

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.largestSubmatrix(matrix = [[0,0,1],[1,1,1],[1,0,1]]) == 4
    print('OK')

    print('Test 2... ', end='')
    assert sol.largestSubmatrix(matrix = [[1,0,1,0,1]]) == 3
    print('OK')

    print('Test 3... ', end='')
    assert sol.largestSubmatrix(matrix = [[1,1,0],[1,0,1]]) == 2
    print('OK')


if __name__ == '__main__':
    test()
