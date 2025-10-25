import unittest
from typing import List


class neighborSum:
    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.inds = {
            grid[i][j]: (i, j) for i in range(self.n) for j in range(self.n)
        }
        self.adj_cache = {}
        self.dia_cache = {}

    def adjacentSum(self, value: int) -> int:
        if value in self.adj_cache:
            return self.adj_cache[value]

        i, j = self.inds[value]
        ans = 0
        if i:
            ans += self.grid[i - 1][j]
        if j:
            ans += self.grid[i][j - 1]
        if i < self.n - 1:
            ans += self.grid[i + 1][j]
        if j < self.n - 1:
            ans += self.grid[i][j + 1]

        self.adj_cache[value] = ans
        return ans

    def diagonalSum(self, value: int) -> int:
        if value in self.dia_cache:
            return self.dia_cache[value]

        i, j = self.inds[value]
        ans = 0
        if i and j:
            ans += self.grid[i - 1][j - 1]
        if i and j < self.n - 1:
            ans += self.grid[i - 1][j + 1]
        if i < self.n - 1 and j:
            ans += self.grid[i + 1][j - 1]
        if i < self.n - 1 and j < self.n - 1:
            ans += self.grid[i + 1][j + 1]

        self.dia_cache[value] = ans
        return ans

    def __repr__(self):
        return f"neighborSum({self.grid})"


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)


class Meta(type):
    def __init__(self, *args, **kwargs):
        for i, case in enumerate(self.test_cases):
            arguments = case["arguments"]
            sol = neighborSum(*arguments[0])
            for j in range(1, len(arguments)):
                setattr(
                    self,
                    f"test_case_{i + 1}_{j}",
                    self.get_test_method(sol, i, j),
                )
        super().__init__(*args, **kwargs)

    def get_test_method(self, sol, i, j):
        def test_method(obj):
            print(f"Test case {i + 1}_{j} ...", end="")
            command = obj.test_cases[i]["commands"][j]
            arguments = obj.test_cases[i]["arguments"][j]
            result = getattr(sol, command)(*arguments)
            expected = obj.test_cases[i]["expected"][j]
            obj.assertEqual(result, expected)
            print("OK")

        return test_method


class TestSolution(unittest.TestCase, metaclass=Meta):
    null = None
    test_cases = [
        {
            "commands": [
                "neighborSum",
                "adjacentSum",
                "adjacentSum",
                "diagonalSum",
                "diagonalSum",
            ],
            "arguments": [
                [[[0, 1, 2], [3, 4, 5], [6, 7, 8]]],
                [1],
                [4],
                [4],
                [8],
            ],
            "expected": [null, 6, 16, 16, 4],
        },
        {
            "commands": ["neighborSum", "adjacentSum", "diagonalSum"],
            "arguments": [
                [
                    [
                        [1, 2, 0, 3],
                        [4, 7, 15, 6],
                        [8, 9, 10, 11],
                        [12, 13, 14, 5],
                    ]
                ],
                [15],
                [9],
            ],
            "expected": [null, 23, 45],
        },
    ]


if __name__ == "__main__":
    unittest.main()
