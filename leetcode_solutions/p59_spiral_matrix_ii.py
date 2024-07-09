import unittest
from typing import List, Iterable


def print_matrix(matrix: Iterable[Iterable[int]]) -> None:
    ml = len(str(max(map(max, matrix))))
    for row in matrix:
        for el in row:
            print(f"{el:>{ml}}", end=" ")
        print()
    print()


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[n * n]]
        # print_matrix(A)
        for _ in range(2 * (n - 1)):
            A = [tuple(range(A[0][0] - len(A), A[0][0])), *zip(*A[::-1])]
            # print_matrix(A)
        return list(map(list, A))


class Solution1:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[n * n]]
        while A[0][0] > 1:
            a = [tuple(range(A[0][0] - len(A), A[0][0]))]
            b = [*zip(*A[::-1])]
            A = a + b
        return [list(x) for x in A] * (n > 0)


class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        c, t, b = 1, 0, n - 1
        res = [[0] * n for _ in range(n)]
        while b > t:
            for i in range(t, b):
                res[t][i] = c
                c += 1
            for i in range(t, b):
                res[i][b] = c
                c += 1
            for i in range(b, t, -1):
                res[b][i] = c
                c += 1
            for i in range(b, t, -1):
                res[i][t] = c
                c += 1
            b -= 1
            t += 1
        if t == b:
            res[b][b] = c
        return res


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def assertSameRows(self, a: List[List[int]], b: List[List[int]]):
        for row1, row2 in zip(a, b):
            self.assertListEqual(row1, row2)

    def test_generate_matrix_1(self):
        print("Test generateMatrix 1... ", end="")
        self.assertSameRows(
            self.sol.generateMatrix(n=3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        )
        print("OK")

    def test_generate_matrix_2(self):
        print("Test generateMatrix 2... ", end="")
        self.assertSameRows(self.sol.generateMatrix(n=1), [[1]])
        print("OK")

    def test_generate_matrix_3(self):
        print("Test generateMatrix 3... ", end="")
        self.assertSameRows(
            self.sol.generateMatrix(n=4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )
        print("OK")


if __name__ == "__main__":
    unittest.main()
