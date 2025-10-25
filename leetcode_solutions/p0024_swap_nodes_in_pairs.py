import unittest
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(next=head)
        while curr.next and curr.next.next:
            first, second, third = (
                curr.next,
                curr.next.next,
                curr.next.next.next,
            )
            curr.next, second.next, first.next = second, first, third
            curr = curr.next.next
        return dummy.next


class TestSolution(unittest.TestCase, metaclass=TestMeta):
    @staticmethod
    def array_to_linked_list(arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["swapPairs"] * 4,
            "kwargs": [
                dict(head=array_to_linked_list([1, 2, 3, 4])),
                dict(head=array_to_linked_list([])),
                dict(head=array_to_linked_list([1])),
                dict(head=array_to_linked_list([1, 2, 3])),
            ],
            "expected": [
                array_to_linked_list([2, 1, 4, 3]),
                array_to_linked_list([]),
                array_to_linked_list([1]),
                array_to_linked_list([2, 1, 3]),
            ],
            "assert_methods": ["assertLinkedListEqual"] * 4,
        },
    ]

    def assertLinkedListEqual(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> None:
        while head1 and head2:
            self.assertEqual(head1.val, head2.val)
            head1 = head1.next
            head2 = head2.next
        self.assertIsNone(head1)
        self.assertIsNone(head2)


if __name__ == "__main__":
    unittest.main()
