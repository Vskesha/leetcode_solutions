from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        res = []
        while right >= left and bottom >= top:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left or bottom < top:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix[0]), len(matrix)
        ans = []

        for i in range(min(m, n) // 2):
            for j in range(i, m - i - 1):
                ans.append(matrix[i][j])
            for j in range(i, n - i - 1):
                ans.append(matrix[j][m - i - 1])
            for j in range(i, m - i - 1):
                ans.append(matrix[n - i - 1][m - j - 1])
            for j in range(i, n - i - 1):
                ans.append(matrix[n - j - 1][i])

        if n < m:
            if n % 2:
                mid = n // 2
                for j in range(mid, m - mid):
                    ans.append(matrix[mid][j])
        elif m % 2:
            mid = m // 2
            for i in range(mid, n - mid):
                ans.append(matrix[i][mid])

        return ans


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        r = min(m, n)
        mid = r // 2
        res = []
        for i in range(mid):
            for j in range(i, m - i):
                res.append(matrix[i][j])
            for j in range(i + 1, n - i - 1):
                res.append(matrix[j][m - i - 1])
            for j in range(m - i - 1, i - 1, -1):
                res.append(matrix[n - i - 1][j])
            for j in range(n - i - 2, i, -1):
                res.append(matrix[j][i])
        if r % 2:
            for j in range(mid, m - mid):
                res.append(matrix[mid][j])
            for j in range(mid + 1, n - mid):
                res.append(matrix[j][m - mid - 1])
        return res


def test():
    sol = Solution()

    print('Test 1... ', end='')
    assert sol.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print('OK')

    print('Test 2... ', end='')
    assert sol.spiralOrder(matrix=[[1, 2, 3, 4],
                                   [5, 6, 7, 8],
                                   [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print('OK')


if __name__ == '__main__':
    test()
