from typing import List


class Solution:
    def numSubmatrixSumTarget(
        self, matrix: List[List[int]], target: int
    ) -> int:
        r, c = len(matrix), len(matrix[0])
        acc = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            row_sum = 0
            for j in range(c):
                row_sum += matrix[i][j]
                acc[i + 1][j + 1] = acc[i][j + 1] + row_sum

        ans = 0
        for y2 in range(1, r + 1):
            for x2 in range(1, c + 1):
                tot = acc[y2][x2]
                for y1 in range(y2):
                    for x1 in range(x2):
                        if (
                            tot - acc[y1][x2] - acc[y2][x1] + acc[y1][x1]
                            == target
                        ):
                            ans += 1

        return ans


class Solution2:
    def numSubmatrixSumTarget(
        self, matrix: List[List[int]], target: int
    ) -> int:
        c = len(matrix[0])
        res = 0
        for row in matrix:
            for col in range(1, len(matrix[0])):
                row[col] += row[col - 1]
        for col in range(len(matrix[0])):
            for k in range(col, len(matrix[0])):
                cur_sum = 0
                d = {0: 1}
                for row in matrix:
                    cur_sum += row[k] - (row[col - 1] if col >= 1 else 0)
                    if cur_sum - target in d:
                        res += d[cur_sum - target]
                    if cur_sum in d:
                        d[cur_sum] += 1
                    else:
                        d[cur_sum] = 1
        return res


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.numSubmatrixSumTarget(
            matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0
        )
        == 4
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0) == 5
    print("OK")

    print("Test 3... ", end="")
    assert sol.numSubmatrixSumTarget(matrix=[[904]], target=0) == 0
    print("OK")

    print("Test 4... ", end="")
    assert (
        sol.numSubmatrixSumTarget(
            matrix=[
                [0, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 0],
                [1, 0, 0, 1, 0, 0],
            ],
            target=0,
        )
        == 43
    )
    print("OK")


if __name__ == "__main__":
    test()
