import unittest
from collections import deque
from functools import wraps
from typing import List, Optional

from leetcode_solutions._test_meta import TestMeta


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def reorderList(self, head: Optional[List]) -> Optional[ListNode]:
            head = self.arr2linkedlist(head)
            self.original.reorderList(head)
            return self.linkedlist2arr(head)

        @staticmethod
        def linkedlist2arr(head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

        @staticmethod
        def arr2linkedlist(arr: Optional[List]) -> Optional[ListNode]:
            head = None
            for val in reversed(arr):
                head = ListNode(val, head)
            return head

    return Wrapper


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = middle = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            middle = middle.next
        tail = middle.next
        middle.next = None
        nxt = tail.next
        tail.next = None
        while nxt:
            tmp = nxt.next
            nxt.next = tail
            tail = nxt
            nxt = tmp
        front = head
        while tail:
            tmp = front.next
            front.next = tail
            front = tmp
            tmp = tail.next
            tail.next = front
            tail = tmp


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = tail = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            tail = tail.next
        tail.next, tail = None, tail.next
        tail.next, nxt = None, tail.next
        while nxt:
            nxt.next, nxt, tail = tail, nxt.next, nxt
        while tail:
            head.next, head = tail, head.next
            tail.next, tail = head, tail.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = deque()
        dummy = ListNode(next=head)
        while head:
            nodes.append(head)
            head = head.next
        prev = dummy
        while len(nodes) > 1:
            prev.next = nodes.popleft()
            prev = prev.next
            prev.next = nodes.pop()
            prev = prev.next
        if nodes:
            prev.next = nodes.pop()
            prev = prev.next
        prev.next = None
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
            "class_methods": ["reorderList"] * 2,
            "kwargs": [
                dict(head=array_to_linked_list([1, 2, 3, 4])),
                dict(head=array_to_linked_list([1, 2, 3, 4, 5])),
            ],
            "expected": [
                array_to_linked_list([1, 4, 2, 3]),
                array_to_linked_list([1, 5, 2, 4, 3]),
            ],
            "assert_methods": ["assertLinkedListEqual"] * 2,
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

# def test_reorder_list():
#     sol = sol_decorator(Solution)()
#
#     print("Test 1... ", end="")
#     assert sol.reorderList(head=[1, 2, 3, 4]) == [1, 4, 2, 3]
#     print("OK")
#
#     print("Test 2... ", end="")
#     assert sol.reorderList(head=[1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
#     print("OK")


# if __name__ == "__main__":
#     test_reorder_list()
