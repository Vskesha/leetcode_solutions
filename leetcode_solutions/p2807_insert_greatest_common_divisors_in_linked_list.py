import unittest
from math import gcd
from typing import Optional, List

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            nxt = curr.next
            curr.next = ListNode(gcd(curr.val, nxt.val), nxt)
            curr = nxt
        return head


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
            "class_methods": ["insertGreatestCommonDivisors"] * 2,
            "kwargs": [
                dict(head=array_to_linked_list([18, 6, 10, 3])),
                dict(head=array_to_linked_list([7])),
            ],
            "expected": [
                array_to_linked_list([18, 6, 6, 2, 10, 1, 3]),
                array_to_linked_list([7]),
            ],
            "assert_methods": ["assertLinkedListEqual"] * 2,
        },
    ]

    def assertLinkedListEqual(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ):
        while head1 and head2:
            self.assertEqual(head1.val, head2.val)
            head1 = head1.next
            head2 = head2.next
        self.assertIsNone(head1)
        self.assertIsNone(head2)


if __name__ == "__main__":
    unittest.main()
