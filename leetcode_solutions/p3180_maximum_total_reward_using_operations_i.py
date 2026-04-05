import unittest
from typing import List

from sortedcontainers import SortedList

from leetcode_solutions._test_meta import TestCaseExtended, TestMeta


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewards = sorted(set(rewardValues))
        ldp = rewards[-1] * 2
        dp = [False] * ldp
        dp[0] = True

        for val in rewards:
            for i in range(min(ldp, val * 2) - 1, val - 1, -1):
                dp[i] = dp[i] or dp[i - val]

        for i in range(ldp - 1, -1, -1):
            if dp[i]:
                return i
        return 0


class Solution2:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        sl = SortedList()
        sl.add(0)
        rewardValues.sort()

        for val in rewardValues:
            i = 0
            while i < len(sl) and sl[i] < val:
                new_val = sl[i] + val
                if new_val not in sl:
                    sl.add(new_val)
                i += 1

        return sl[-1]


class TestSolution(TestCaseExtended, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["maxTotalReward"] * 2,
            "kwargs": [
                dict(rewardValues=[1, 1, 3, 3]),
                dict(rewardValues=[1, 6, 4, 3, 2]),
            ],
            "expected": [4, 11],
        },
    ]


if __name__ == "__main__":
    unittest.main()
