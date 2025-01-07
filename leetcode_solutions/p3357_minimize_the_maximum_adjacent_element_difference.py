import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        prev = 0
        for n in nums:
            if n > 0:
                prev = n
                break

        i, sti, ln = 0, 0, len(nums)
        gaps = []
        max_gap = 0

        while i < ln:
            if nums[i] == -1:
                sti = i
                i += 1
                while i < ln and nums[i] == -1:
                    i += 1
                if i == ln:
                    gaps.append((prev, prev, i - sti))
                    break
                elif nums[i] > prev:
                    gaps.append((prev, nums[i], i - sti))
                else:
                    gaps.append((nums[i], prev, i - sti))
            else:
                max_gap = max(max_gap, abs(nums[i] - prev))
            prev = nums[i]
            i += 1

        if not gaps:
            return max_gap

        maxb = max(g for _, g, _ in gaps)
        minb = min(g for g, _, _ in gaps)

        ld, rd = max_gap, (maxb - minb + 1) // 2

        while ld < rd:
            md = (ld + rd) // 2
            possible = True
            x = minb + md
            y = maxb - md
            for lb, rb, am in gaps:
                if (
                        (
                                abs(rb - x) <= md and
                                abs(x - lb) <= md
                        )
                        or (
                        abs(rb - y) <= md and
                        abs(y - lb) <= md)
                        or (
                        am > 1
                        and abs(rb - y) <= md
                        and abs(y - x) <= md
                        and abs(x - lb) <= md
                )
                ):
                    continue
                possible = False
                break

            if possible:
                rd = md
            else:
                ld = md + 1

        return ld


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minDifference"] * 4,
            "kwargs": [
                dict(nums=[1, 2, -1, 10, 8]),
                dict(nums=[-1, -1, -1]),
                dict(nums=[-1, 10, -1, 8]),
                dict(nums=[1, 12]),
            ],
            "expected": [4, 0, 1, 11],
        },
    ]


if __name__ == "__main__":
    unittest.main()
