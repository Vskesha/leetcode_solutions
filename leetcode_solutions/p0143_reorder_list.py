from functools import wraps
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def test_reorder_list():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.reorderList(head=[1, 2, 3, 4]) == [1, 4, 2, 3]
    print("OK")

    print("Test 2... ", end="")
    assert sol.reorderList(head=[1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    print("OK")


if __name__ == "__main__":
    test_reorder_list()
