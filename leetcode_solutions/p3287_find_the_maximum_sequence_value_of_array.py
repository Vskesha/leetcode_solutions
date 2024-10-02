import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        def masks(nums):
            tm = {(1, 0)}
            ans = {}
            for i, n in enumerate(nums[:-k], 1):
                tmp = set()
                for taken, mask in tm:
                    mask |= n
                    if taken < k:
                        tmp.add((taken + 1, mask))
                    elif taken == k and mask not in ans:
                        ans[mask] = i
                tm.update(tmp)
            return ans

        ln = len(nums)
        a = masks(nums)
        b = masks(nums[::-1])
        return max(m1 ^ m2 for m1 in a for m2 in b if a[m1] + b[m2] <= ln)


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxValue"] * 2,
            "kwargs": [
                dict(nums=[2, 6, 7], k=1),
                dict(nums=[4, 2, 5, 6, 7], k=2),
            ],
            "expected": [5, 2],
        },
    ]


if __name__ == "__main__":
    unittest.main()
