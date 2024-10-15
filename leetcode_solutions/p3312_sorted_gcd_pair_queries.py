import unittest
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        cnt = [0] * (mx + 1)
        for n in nums:
            cnt[n] += 1

        gcd = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            tn = 0
            exc = 0
            for nd in range(d, mx + 1, d):
                tn += cnt[nd]
                exc += gcd[nd]
            gcd[d] = tn * (tn - 1) // 2 - exc

        acc = list(accumulate(gcd))
        ans = []
        for q in queries:
            cd = bisect_right(acc, q)
            ans.append(cd)

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["gcdValues"] * 3,
            "kwargs": [
                dict(nums=[2, 3, 4], queries=[0, 2, 2]),
                dict(nums=[4, 4, 2, 1], queries=[5, 3, 1, 0]),
                dict(nums=[2, 2], queries=[0, 0]),
            ],
            "expected": [
                [1, 2, 2],
                [4, 2, 1, 1],
                [2, 2],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
