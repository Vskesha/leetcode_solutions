import unittest
from typing import Optional, List

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        head = curr = ListNode(next=head)

        while curr and curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head.next


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_linked_list(arr: Optional[List[int]]) -> Optional[ListNode]:
        if not arr:
            return None
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head


    test_cases = [
        {
            "class": Solution,
            "class_methods": ["modifiedList"] * 3,
            "kwargs": [
                dict(nums = [1,2,3], head = array_to_linked_list([1,2,3,4,5])),
                dict(nums = [1], head = array_to_linked_list([1,2,1,2,1,2])),
                dict(nums = [5], head = array_to_linked_list([1,2,3,4])),
            ],
            "expected": [
                array_to_linked_list([4,5]),
                array_to_linked_list([2,2,2]),
                array_to_linked_list([1,2,3,4])
            ],
            "assert_methods": ["assertLinkedListEqual"] * 3,
        },
    ]

    def assertLinkedListEqual(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        while l1 and l2:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
        self.assertIsNone(l1)
        self.assertIsNone(l2)


if __name__ == '__main__':
    unittest.main()
