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

        def reverseList(self, head: Optional[List]) -> Optional[List]:
            head = self.arr2linkedlist(head)
            revers = self.original.reverseList(head)
            return self.linkedlist2arr(revers)

        def arr2linkedlist(self, arr: Optional[List]) -> Optional[ListNode]:
            head = None
            for val in reversed(arr):
                head = ListNode(val, head)
            return head

        def linkedlist2arr(self, head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            prev, head.next, head = head, prev, head.next
        return prev


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nxt = head.next
        head.next = None

        while nxt:
            head, nxt.next, nxt = nxt, head, nxt.next

        return head


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur, nxt = head, head.next
        cur.next = None
        while nxt:
            nxt.next, nxt, cur = cur, nxt.next, nxt
        return cur


def test_reverse_list():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.reverseList(head=[1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    print("OK")

    print("Test 2... ", end="")
    assert sol.reverseList(head=[1, 2]) == [2, 1]
    print("OK")

    print("Test 3... ", end="")
    assert sol.reverseList(head=[]) == []
    print("OK")


if __name__ == "__main__":
    test_reverse_list()
