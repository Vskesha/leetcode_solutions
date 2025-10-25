import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:
        ln = len(nums)
        nis = sorted((n, i) for i, n in enumerate(nums))
        j = 0
        while j < ln:
            vals, inds = [nis[j][0]], [nis[j][1]]
            j += 1
            while j < ln and nis[j][0] <= vals[-1] + limit:
                vals.append(nis[j][0])
                inds.append(nis[j][1])
                j += 1
            inds.sort()
            for n, i in zip(vals, inds):
                nums[i] = n
        return nums


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["lexicographicallySmallestArray"] * 3,
            "kwargs": [
                dict(nums=[1, 5, 3, 9, 8], limit=2),
                dict(nums=[1, 7, 6, 18, 2, 1], limit=3),
                dict(nums=[1, 7, 28, 19, 10], limit=3),
            ],
            "expected": [
                [1, 3, 5, 8, 9],
                [1, 6, 7, 18, 1, 2],
                [1, 7, 28, 19, 10],
            ],
            "assert_methods": ["assertListEqual"] * 3,
        },
    ]


if __name__ == "__main__":
    unittest.main()
