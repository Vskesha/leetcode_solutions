from functools import wraps
from typing import List, Optional, Tuple


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

        def deleteNode(self, head: Optional[List], node: int) -> Optional[List]:
            head, node = self.arr2linkedlist(head, node)
            self.original.deleteNode(node)
            return self.linkedlist2arr(head)

        def arr2linkedlist(self, arr: List, node: int) -> Tuple[ListNode, ListNode]:
            head = None
            lnode = None
            for val in reversed(arr):
                prev = ListNode(val)
                prev.next = head
                head = prev
                if val == node:
                    lnode = head
            return head, lnode

        def linkedlist2arr(self, head: Optional[ListNode]) -> Optional[List]:
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

    return Wrapper


@sol_decorator
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.deleteNode(head=[4, 5, 1, 9], node=5) == [4, 1, 9]  # noqa
    print("OK")

    print("Test 2... ", end="")
    assert sol.deleteNode(head=[4, 5, 1, 9], node=1) == [4, 5, 9]  # noqa
    print("OK")


if __name__ == "__main__":
    test()
