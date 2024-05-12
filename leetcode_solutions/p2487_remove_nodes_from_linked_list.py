from functools import wraps
from typing import Optional, List


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

        def removeNodes(self, head: Optional[List]) -> Optional[List]:
            head = self.arr2list(head)
            result = self.original.removeNodes(head)
            return self.list2arr(result)

        def arr2list(self, arr: List[int]) -> Optional[ListNode]:
            if not arr:
                return None

            head = None
            for val in reversed(arr):
                head = ListNode(val, head)

            return head

        def list2arr(self, head: Optional[ListNode]) -> List[int]:
            arr = []

            while head:
                arr.append(head.val)
                head = head.next

            return arr

    return Wrapper


@sol_decorator
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next

        head = None
        for node in reversed(stack):
            node.next = head
            head = node

        return head


def test_remove_nodes():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.removeNodes(head=[5, 2, 13, 3, 8]) == [13, 8]  # noqa
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeNodes(head=[1, 1, 1, 1]) == [1, 1, 1, 1]  # noqa
    print("OK")


if __name__ == "__main__":
    test_remove_nodes()
