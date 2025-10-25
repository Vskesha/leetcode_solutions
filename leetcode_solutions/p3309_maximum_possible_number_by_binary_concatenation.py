import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        return int(
            "".join(
                sorted(
                    [bin(n)[2:] for n in nums],
                    reverse=True,
                    key=lambda x: x * 7,
                )
            ),
            2,
        )


class Solution2:
    def maxGoodNumber(self, nums: List[int]) -> int:
        bins = [bin(n)[2:] for n in nums]
        bins.sort(reverse=True, key=lambda x: x * 7)
        ans = "".join(bins)
        return int(ans, 2)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxGoodNumber"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 3]),
                dict(nums=[2, 8, 16]),
            ],
            "expected": [30, 1296],
        },
    ]


if __name__ == "__main__":
    unittest.main()
