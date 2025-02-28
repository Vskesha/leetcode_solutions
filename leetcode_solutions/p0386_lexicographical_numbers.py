import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans, k = [], 1

        for _ in range(n):
            ans.append(k)
            if k * 10 <= n:
                k *= 10
            else:
                while k % 10 == 9 or k >= n:
                    k //= 10
                k += 1

        return ans


class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:

        def dfs(curr, res):
            if curr > n:
                return
            res.append(curr)
            curr *= 10
            for i in range(curr, curr + 10):
                if i > n:
                    break
                dfs(i, res)

        res = []
        for d in range(1, 10):
            dfs(d, res)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lexicalOrder"] * 2,
            "kwargs": [
                dict(n=13),
                dict(n=2),
            ],
            "expected": [[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
