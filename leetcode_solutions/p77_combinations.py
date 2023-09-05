from itertools import combinations


class Solution:
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


class Solution1:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        for comb in combinations(range(1, n + 1), k):
            res.append(list(comb))
        return res


def main():
    sol = Solution()
    print(' [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]\n', sol.combine(4, 2))
    print(' [[1]]\n', sol.combine(1, 1))
    print(' [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], '
          '[1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]\n',
          sol.combine(5, 3))


if __name__ == '__main__':
    main()
