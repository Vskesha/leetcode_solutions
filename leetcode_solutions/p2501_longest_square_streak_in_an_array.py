import unittest
from typing import List

from leetcode_solutions._test_meta import TestMeta


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        sq = {}

        for n in nums:
            sq[n] = sq.get(n * n, 0) + 1

        ans = max(sq.values())
        return -1 if ans == 1 else ans


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        keys = {}
        pr = 0
        head = None

        for n in nums:
            head = ListNode(n, head)
            keys[pr] = head
            pr = n

        ans = 0
        while head:
            val, cnt = head.val**2, 1
            while val in keys:
                curr = keys[val]
                curr.next = curr.next.next
                if curr.next:
                    keys[curr.next.val] = curr
                val *= val
                cnt += 1
            ans = max(ans, cnt)
            head = head.next

        return ans if ans != 1 else -1


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    test_cases = [
        {
            "class": Solution,
            "class_methods": ["longestSquareStreak"] * 3,
            "kwargs": [
                dict(nums=[4, 3, 6, 16, 8, 2]),
                dict(nums=[2, 3, 5, 6, 7]),
                dict(nums=[3, 9, 81, 6561]),
            ],
            "expected": [3, -1, 4],
        },
    ]


if __name__ == "__main__":
    unittest.main()
