import unittest
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[int(v) for v in row] for row in matrix]
        m, n = len(dp), len(dp[0])

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j]:
                    dp[i][j] = (
                        min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    )

        return max(max(row) for row in dp) ** 2


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0

        for row in matrix:
            stack = []
            for i, c in enumerate(row + ["0"]):
                h = heights[i] = heights[i] + 1 if c == "1" else 0
                w = 0
                while stack and stack[-1][0] >= h:
                    ch, cw = stack.pop()
                    w += cw
                    ans = max(ans, min(ch, w))
                stack.append((h, w + 1))

        return ans**2


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_maximal_square_1(self):
        print("Test maximalSquare 1... ", end="")
        self.assertEqual(
            self.sol.maximalSquare(
                matrix=[
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ),
            4,
        )
        print("OK")

    def test_maximal_square_2(self):
        print("Test maximalSquare 2... ", end="")
        self.assertEqual(
            self.sol.maximalSquare(matrix=[["0", "1"], ["1", "0"]]), 1
        )
        print("OK")

    def test_maximal_square_3(self):
        print("Test maximalSquare 3... ", end="")
        self.assertEqual(
            self.sol.maximalSquare(
                matrix=[
                    ["0", "0", "0", "1"],
                    ["1", "1", "0", "1"],
                    ["1", "1", "1", "1"],
                    ["0", "1", "1", "1"],
                    ["0", "1", "1", "1"],
                ]
            ),
            9,
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
