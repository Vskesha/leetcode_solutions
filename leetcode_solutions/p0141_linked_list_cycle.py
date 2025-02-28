from functools import wraps
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sol_decorator(cls):
    @wraps(cls, updated=())
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.original = cls(*args, **kwargs)

        def hasCycle(self, head: Optional[List], pos: int) -> bool:
            head = self.arr2linkedlist(head, pos)
            return self.original.hasCycle(head)

        def arr2linkedlist(self, arr: Optional[List], pos: int) -> Optional[ListNode]:
            if not arr:
                return None

            dummy = node = ListNode(None)
            cycle = None
            for i, x in enumerate(arr):
                node.next = ListNode(x)
                node = node.next
                if i == pos:
                    cycle = node
            node.next = cycle
            return dummy.next

    return Wrapper


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if hasattr(head, "pos"):
                return True
            head.pos = 0
            head = head.next

        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


def test_has_cycle():
    sol = sol_decorator(Solution)()

    print("Test 1... ", end="")
    assert sol.hasCycle(head=[3, 2, 0, -4], pos=1) is True
    print("OK")

    print("Test 2... ", end="")
    assert sol.hasCycle(head=[1, 2], pos=0) is True
    print("OK")

    print("Test 3... ", end="")
    assert sol.hasCycle(head=[1], pos=-1) is False
    print("OK")


if __name__ == "__main__":
    test_has_cycle()
