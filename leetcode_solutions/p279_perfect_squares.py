import math
from bisect import bisect_right


class Solution:
    constr = 10000
    sq = [pow(i, 2) for i in range(1, round(math.sqrt(constr)) + 1)]
    psn = list(range(constr + 1))
    for i in range(1, constr + 1):
        ri = bisect_right(sq, i)
        for j in range(ri):
            psn[i] = min(psn[i], psn[i - sq[j]] + 1)

    def numSquares(self, n: int) -> int:
        return Solution.psn[n]


class Solution2:
    def numSquares(self, n: int) -> int:
        sq = [pow(i, 2) for i in range(1, round(math.sqrt(n)) + 1)]
        psn = list(range(n + 1))
        for i in range(1, n + 1):
            for j in range(bisect_right(sq, i)):
                psn[i] = min(psn[i], psn[i - sq[j]] + 1)
        return psn[n]


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.numSquares(n=12) == 3
    print("OK")

    print("Test 2... ", end="")
    assert sol.numSquares(n=13) == 2
    print("OK")


if __name__ == "__main__":
    test()
