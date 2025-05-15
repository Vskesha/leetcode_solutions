import unittest
from itertools import pairwise
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            prev = dummy
            curr = head
            head = head.next
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            after = prev.next
            prev.next = curr
            curr.next = after

        return dummy.next


class Solution1:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            prev = dummy
            while prev.next and prev.next.val <= head.val:
                prev = prev.next
            head.next, prev.next, head = prev.next, head, head.next

        return dummy.next


class Solution2:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.sort(key=lambda node: node.val)
        for n1, n2 in pairwise(nodes):
            n1.next = n2
        nodes[-1].next = None

        return nodes[0]


class Solution3:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort(reverse=True)
        head = None
        for val in values:
            head = ListNode(val, head)
        return head


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def array_to_linked_list(arr: List[int]):
        head = None
        for n in reversed(arr):
            head = ListNode(n, head)
        return head

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["insertionSortList"] * 3,
            "kwargs": [
                dict(head=array_to_linked_list([4, 2, 1, 3])),
                dict(head=array_to_linked_list([-1, 5, 3, 4, 0])),
                dict(head=array_to_linked_list([1, 1])),
            ],
            "expected": [
                array_to_linked_list([1, 2, 3, 4]),
                array_to_linked_list([-1, 0, 3, 4, 5]),
                array_to_linked_list([1, 1]),
            ],
            "assert_methods": ["assertLinkedListEqual"] * 3,
        },
    ]

    def assertLinkedListEqual(self, actual, expected):
        if actual and expected:
            self.assertEqual(actual.val, expected.val)
            self.assertLinkedListEqual(actual.next, expected.next)
        else:
            self.assertIsNone(actual)
            self.assertIsNone(expected)


if __name__ == "__main__":
    unittest.main()
