import unittest
from collections import defaultdict
from typing import List

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        inds = defaultdict(list)
        for i, n in enumerate(nums):
            inds[n].append(i)

        res = [0] * len(nums)

        for indices in inds.values():
            li = len(indices)
            curr = 0
            for ii in range(1, li):
                curr += ii * (indices[ii] - indices[ii - 1])
                res[indices[ii]] = curr
            curr = els = 0
            for ii in range(li - 2, -1, -1):
                els += 1
                curr += els * (indices[ii + 1] - indices[ii])
                res[indices[ii]] += curr

        return res


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["distance"] * 2,
            "kwargs": [
                dict(nums=[1, 3, 1, 1, 2]),
                dict(nums=[0, 5, 3]),
            ],
            "expected": [[5, 0, 3, 4, 0], [0, 0, 0]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
