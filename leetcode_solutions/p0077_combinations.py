from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []

        def backtrack(i, k, comb):
            if not k:
                self.ans.append(comb.copy())
                return

            for j in range(i, n - k + 2):
                comb.append(j)
                backtrack(j + 1, k - 1, comb)
                comb.pop()

        backtrack(1, k, [])
        return self.ans


class Solution1:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        curr = []

        def comb(st):
            lc = len(curr)

            if lc == k:
                res.append(curr.copy())
                return

            for i in range(st, n - k + lc + 2):
                curr.append(i)
                comb(i + 1)
                curr.pop()

        comb(1)
        return res


class Solution2:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [list(c) for c in combinations(range(1, n + 1), k)]


class Solution3:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        for comb in combinations(range(1, n + 1), k):
            res.append(list(comb))
        return res


def main():
    sol = Solution()

    print("Test 1... ", end="")
    output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    res = sol.combine(4, 2)
    for comb in res:
        assert comb in output
    for comb in output:
        assert comb in res
    print("OK")

    print("Test 2... ", end="")
    output = [[1]]
    res = sol.combine(1, 1)
    for comb in res:
        assert comb in output
    for comb in output:
        assert comb in res
    print("OK")

    print("Test 3... ", end="")
    output = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    res = sol.combine(5, 3)
    for comb in res:
        assert comb in output
    for comb in output:
        assert comb in res
    print("OK")


if __name__ == "__main__":
    main()
