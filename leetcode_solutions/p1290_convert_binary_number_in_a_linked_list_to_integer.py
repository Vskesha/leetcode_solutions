import unittest
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next

        return ans


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def arr_to_linked_list(arr: List[int]):
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["getDecimalValue"] * 2,
            "kwargs": [
                dict(head=arr_to_linked_list([1, 0, 1])),
                dict(head=arr_to_linked_list([0])),
            ],
            "expected": [5, 0],
        },
    ]


if __name__ == "__main__":
    unittest.main()
