from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)


class Solution2:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix[0]), len(matrix)
        ans = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ans[j][i] = matrix[i][j]

        return ans


def test():
    sol = Solution()

    print('Test 1... ', end='')
    for a, b in zip(sol.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]):
        assert a == b
    print('OK')

    print('Test 2... ', end='')
    for a, b in zip(sol.transpose(matrix=[[1, 2, 3], [4, 5, 6]]),
                    [[1, 4], [2, 5], [3, 6]]):
        assert a == b
    print('OK')


if __name__ == '__main__':
    test()
