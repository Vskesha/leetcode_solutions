import unittest
from typing import Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        ln = 1
        while tail.next:
            tail = tail.next
            ln += 1

        shift = k % ln
        if not shift:
            return head

        tail.next = head
        for _ in range(ln - shift):
            tail = tail.next
        head = tail.next
        tail.next = None

        return head


class TestSolution(unittest.TestCase, metaclass=TestMeta):

    @staticmethod
    def array_to_linked_list(arr: list) -> Optional[ListNode]:
        if not arr:
            return None

        head = None
        for val in reversed(arr):
            head = ListNode(val, head)
        return head

    test_cases = [
        {
            "class": Solution,
            "class_methods": ["rotateRight"] * 2,
            "kwargs": [
                dict(head=array_to_linked_list([1, 2, 3, 4, 5]), k=2),
                dict(head=array_to_linked_list([0, 1, 2]), k=4),
            ],
            "expected": [
                array_to_linked_list([4, 5, 1, 2, 3]),
                array_to_linked_list([2, 0, 1]),
            ],
            "assert_methods": ["assertLinkedListsEqual"] * 2,
        },
    ]

    def assertLinkedListsEqual(
        self, actual: Optional[ListNode], expected: Optional[ListNode]
    ) -> None:
        if actual and expected:
            self.assertEqual(actual.val, expected.val)
            self.assertLinkedListsEqual(actual.next, expected.next)
        else:
            self.assertIsNone(actual)
            self.assertIsNone(expected)


if __name__ == "__main__":
    unittest.main()
