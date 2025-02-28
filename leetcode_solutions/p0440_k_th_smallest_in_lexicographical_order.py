import unittest

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count(n, pr1, pr2):
            cnt = 0
            while pr1 <= n:
                cnt += min(n + 1, pr2) - pr1
                pr1 *= 10
                pr2 *= 10
            return cnt

        curr = 1
        k -= 1

        while k > 0:
            cnt = count(n, curr, curr + 1)
            if cnt <= k:
                curr += 1
                k -= cnt
            else:
                curr *= 10
                k -= 1

        return curr


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["findKthNumber"] * 2,
            "kwargs": [
                dict(n = 13, k = 2),
                dict(n = 1, k = 1),
            ],
            "expected": [10, 1],
        },
    ]


if __name__ == '__main__':
    unittest.main()
