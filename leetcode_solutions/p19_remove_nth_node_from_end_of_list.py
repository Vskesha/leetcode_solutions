from functools import wraps
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        this = self
        while this and other:
            if this.val != other.val:
                return False
            this, other = this.next, other.next
        return this is None and other is None


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def removeNthFromEnd(self, head: Optional[List], n: int) -> Optional[ListNode]:
            head = self.arr2linkedlist(head)
            return self.original.removeNthFromEnd(head, n)
            # deleted = self.original.removeNthFromEnd(head, n)
            # return self.linkedlist2arr(deleted)

        def arr2linkedlist(self, arr: List[int]) -> Optional[ListNode]:
            head = None
            nxt = None
            for num in reversed(arr):
                head = ListNode(num, nxt)
                nxt = head
            return head

        def linkedlist2arr(self, head: Optional[ListNode]) -> Optional[List[int]]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if n == length:
            return head.next
        before_del = head
        for _ in range(length - n - 1):
            before_del = before_del.next
        before_del.next = before_del.next.next
        return head


class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


def test_remove_nth_from_end():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2) == sol.arr2linkedlist(
        [1, 2, 3, 5]
    )
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeNthFromEnd(head=[1], n=1) == sol.arr2linkedlist([])
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeNthFromEnd(head=[1, 2], n=1) == sol.arr2linkedlist([1])
    print("OK")


if __name__ == "__main__":
    test_remove_nth_from_end()
