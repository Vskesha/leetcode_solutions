from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
            matrix[i][0] += min(matrix[i - 1][:2])
            for j in range(1, n):
                matrix[i][j] += min(matrix[i - 1][j - 1 : j + 2])

        return min(matrix[-1])


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    print("OK")

    print("Test 2... ", end="")
    assert sol.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]) == -59
    print("OK")


if __name__ == "__main__":
    test()
