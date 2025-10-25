from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = (
                    matrix[~j][i],
                    matrix[i][j],
                    matrix[j][~i],
                    matrix[~i][~j],
                )


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix[::-1]))


def test():
    sol = Solution()

    print("Test 1... ", end="")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print("OK")

    print("Test 2... ", end="")
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    assert matrix == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]
    print("OK")


if __name__ == "__main__":
    test()
