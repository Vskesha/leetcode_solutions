import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                cnt = -1
                for ch in reversed(bin(n)):
                    if ch == "1":
                        cnt += 1
                    else:
                        break
                ans.append(n - (1 << cnt))
        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minBitwiseArray"] * 2,
            "kwargs": [
                dict(nums=[2, 3, 5, 7]),
                dict(nums=[11, 13, 31]),
            ],
            "expected": [
                [-1, 1, 4, 3],
                [9, 12, 15],
            ],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
