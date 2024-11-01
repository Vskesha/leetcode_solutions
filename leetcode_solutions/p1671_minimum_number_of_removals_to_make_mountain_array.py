import unittest
from bisect import bisect_left
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        ln = len(nums)
        st = []
        ml = [0] * ln

        for i, n in enumerate(nums):
            si = bisect_left(st, n)
            ml[i] = si
            if si == len(st):
                st.append(n)
            else:
                st[si] = n

        st.clear()
        mr = [0] * ln
        for i in range(ln - 1, -1, -1):
            n = nums[i]
            si = bisect_left(st, n)
            mr[i] = si
            if si == len(st):
                st.append(n)
            else:
                st[si] = n

        mm = max(a + b for a, b in zip(ml, mr) if a and b) + 1
        return ln - mm


class Solution2:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        ln = len(nums)
        st = []
        ml = [0] * ln

        for i, n in enumerate(nums):
            si = bisect_left(st, n)
            ml[i] = si
            if si == len(st):
                st.append(n)
            else:
                st[si] = n

        st.clear()
        mm = 0
        for i in range(ln - 1, -1, -1):
            n = nums[i]
            si = bisect_left(st, n)
            if si and ml[i]:
                mm = max(mm, si + ml[i])
            if si == len(st):
                st.append(n)
            else:
                st[si] = n

        return ln - mm - 1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["minimumMountainRemovals"] * 3,
            "kwargs": [
                dict(nums=[100, 92, 89, 77, 74, 66, 64, 66, 64]),
                dict(nums=[1, 3, 1]),
                dict(nums=[2, 1, 1, 5, 6, 2, 3, 1]),
            ],
            "expected": [6, 0, 3],
        },
    ]


if __name__ == "__main__":
    unittest.main()
