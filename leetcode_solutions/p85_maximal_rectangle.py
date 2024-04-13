from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [[0] * n for _ in range(m)]
        heights[0] = [int(k) for k in matrix[0]]

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[i][j] = heights[i - 1][j] + 1

        max_area = 0
        for i in range(m):
            for st in range(n):
                min_height = heights[i][st]
                max_area = max(max_area, min_height)
                for end in range(st + 1, n):
                    min_height = min(min_height, heights[i][end])
                    curr_area = min_height * (end - st + 1)
                    max_area = max(max_area, curr_area)

        return max_area


class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        best = 0
        for row in matrix:
            for col in range(n):
                heights[col] = heights[col] + 1 if row[col] == "1" else 0
            stack = [-1]
            for col in range(n + 1):
                while heights[col] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = col - stack[-1] - 1
                    best = max(best, h * w)
                stack.append(col)
        return best


def test_maximal_rectangle():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.maximalRectangle(
            matrix=[
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
        == 6
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.maximalRectangle(matrix=[["0"]]) == 0
    print("OK")

    print("Test 3... ", end="")
    assert sol.maximalRectangle(matrix=[["1"]]) == 1
    print("OK")


if __name__ == "__main__":
    test_maximal_rectangle()
