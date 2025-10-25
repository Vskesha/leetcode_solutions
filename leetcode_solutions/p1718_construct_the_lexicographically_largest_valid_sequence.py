import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seen = [False] * (n + 1)
        lr = 2 * n - 1
        res = [0] * lr

        def backtrack(i: int) -> bool:
            if i == lr:
                return True
            if res[i]:
                return backtrack(i + 1)

            for j in range(n, 0, -1):
                if not seen[j]:
                    seen[j] = True
                    res[i] = j
                    if j == 1:
                        if backtrack(i + 1):
                            return True
                    elif i + j < lr and res[i + j] == 0:
                        res[i + j] = j
                        if backtrack(i + 1):
                            return True
                        res[i + j] = 0
                    res[i] = 0
                    seen[j] = False

            return False

        backtrack(0)
        return res


class Solution1:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seen = [False] * (n + 1)
        lr = 2 * n - 1
        res = [0] * lr

        def backtrack(i: int) -> bool:
            while i < lr and res[i]:
                i += 1
            if i == lr:
                return True
            for j in range(n, 1, -1):
                if seen[j] or i + j >= lr or res[i + j]:
                    continue
                seen[j] = True
                res[i] = res[i + j] = j
                if backtrack(i + 1):
                    return True
                res[i] = res[i + j] = 0
                seen[j] = False

            if not seen[1]:
                res[i] = 1
                seen[1] = True
                if backtrack(i + 1):
                    return True
                res[i] = 0
                seen[1] = False

            return False

        backtrack(0)
        return res


class Solution2:
    def constructDistancedSequence(self, n: int) -> List[int]:
        nums = SortedList(range(1, n + 1))
        lr = 2 * n - 1
        res = [0] * lr

        def dfs(nums, mi):
            if not nums:
                return True

            while res[mi]:
                mi += 1

            desc = list(reversed(nums))
            for n in desc:
                if n == 1:
                    res[mi] = n
                    nums.remove(n)
                    if dfs(nums, mi):
                        return True
                    res[mi] = 0
                    nums.add(n)
                elif mi + n < lr and res[mi + n] == 0:
                    res[mi] = res[mi + n] = n
                    nums.remove(n)
                    if dfs(nums, mi + 1):
                        return True
                    res[mi] = res[mi + n] = 0
                    nums.add(n)

            return False

        dfs(nums, 0)
        return res


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["constructDistancedSequence"] * 3,
            "kwargs": [
                dict(n=3),
                dict(n=5),
                dict(n=7),
            ],
            "expected": [
                [3, 1, 2, 3, 2],
                [5, 3, 1, 4, 3, 5, 2, 4, 2],
                [7, 5, 3, 6, 4, 3, 5, 7, 4, 6, 2, 1, 2],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
