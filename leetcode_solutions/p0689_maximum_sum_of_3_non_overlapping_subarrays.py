import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ln = len(nums)
        sums = []
        ws = sum(nums[: k - 1])
        for nc, np in zip(nums[k - 1 :], nums):
            ws += nc
            sums.append(ws)
            ws -= np

        m1, i10 = sums[0], 0
        m2, i20, i21 = m1 + sums[k], 0, k
        m3, i30, i31, i32 = m2 + sums[k * 2], 0, k, k * 2

        for i3 in range(2 * k + 1, ln - k + 1):
            i2 = i3 - k
            i1 = i2 - k
            if sums[i1] > m1:
                m1, i10 = sums[i1], i1
            if sums[i2] + m1 > m2:
                m2, i20, i21 = sums[i2] + m1, i10, i2
            if sums[i3] + m2 > m3:
                m3, i30, i31, i32 = sums[i3] + m2, i20, i21, i3

        return [i30, i31, i32]


class Solution2:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ln = len(nums)
        sums = []
        ws = sum(nums[: k - 1])
        for nc, np in zip(nums[k - 1 :], nums):
            ws += nc
            sums.append(ws)
            ws -= np

        maxs1 = [(sums[0], 0)]
        for i1 in range(1, ln - 3 * k + 1):
            if sums[i1] > maxs1[-1][0]:
                maxs1.append((sums[i1], i1))
            else:
                maxs1.append(maxs1[-1])

        maxs2 = [(maxs1[0][0] + sums[k], maxs1[0][1], k)]
        for i2, j in zip(range(k + 1, ln - 2 * k + 1), range(1, ln)):
            cs = sums[i2] + maxs1[j][0]
            if cs > maxs2[-1][0]:
                maxs2.append((cs, maxs1[j][1], i2))
            else:
                maxs2.append(maxs2[-1])

        maxs3 = [(maxs2[0][0] + sums[k * 2], maxs2[0][1], maxs2[0][2], k * 2)]
        for i3, j in zip(range(2 * k + 1, ln - k + 1), range(1, ln)):
            cs = sums[i3] + maxs2[j][0]
            if cs > maxs3[-1][0]:
                maxs3.append((cs, maxs2[j][1], maxs2[j][2], i3))
            else:
                maxs3.append(maxs3[-1])

        return list(maxs3[-1][1:])


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxSumOfThreeSubarrays"] * 2,
            "kwargs": [
                dict(nums=[1, 2, 1, 2, 6, 7, 5, 1], k=2),
                dict(nums=[1, 2, 1, 2, 1, 2, 1, 2, 1], k=2),
            ],
            "expected": [[0, 3, 5], [0, 2, 4]],
            "assert_methods": ["assertListEqual"] * 2,
        },
    ]


if __name__ == "__main__":
    unittest.main()
