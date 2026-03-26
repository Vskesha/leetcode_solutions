import unittest
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        ans = []
        esum = sum(n for n in nums if n % 2 == 0)

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                esum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                esum += nums[idx]
            ans.append(esum)

        return ans


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["sumEvenAfterQueries"] * 2,
            "kwargs": [
                dict(
                    nums=[1, 2, 3, 4],
                    queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]],
                ),
                dict(nums=[1], queries=[[4, 0]]),
            ],
            "expected": [[8, 6, 2, 4], [0]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
