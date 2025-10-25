import unittest
from collections import Counter
from itertools import permutations

from leetcode_solutions._test_meta import TestMeta


class Solution:
    fact = [1] * 8
    for i in range(2, 8):
        fact[i] = fact[i - 1] * i

    def numTilePossibilities(self, tiles: str) -> int:
        cnt = list(Counter(tiles).values())
        lc = len(cnt)

        def dfs(i, taken, fact) -> int:
            if i == lc:
                ans = fact[sum(taken)]
                for v in taken:
                    ans //= fact[v]
                return ans

            ans = 0
            for v in range(cnt[i] + 1):
                taken.append(v)
                ans += dfs(i + 1, taken, fact)
                taken.pop()

            return ans

        return dfs(0, [], self.fact) - 1


class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        for i in range(1, len(tiles) + 1):
            for p in permutations(tiles, i):
                res.add(p)

        return len(res)


class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)

        result = set()

        for length in range(1, n + 1):
            for perm in permutations(tiles, length):
                result.add("".join(perm))

        return len(result)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["numTilePossibilities"] * 3,
            "kwargs": [
                dict(tiles="AAB"),
                dict(tiles="AAABBC"),
                dict(tiles="V"),
            ],
            "expected": [8, 188, 1],
        },
    ]


if __name__ == "__main__":
    unittest.main()
